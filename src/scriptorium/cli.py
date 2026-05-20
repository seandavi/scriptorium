"""Command-line interface for scriptorium.

The CLI exposes six subcommands:

* ``install`` — copy or link the plugin into a Claude Code plugins dir.
* ``validate`` — lint a ``MANUSCRIPT_STATE.yaml`` against the JSON Schema.
* ``prompt-pack`` — concatenate bundled skill prompts for platform-neutral use.
* ``list`` — list bundled skills with descriptions and grounding references.
* ``init`` — scaffold a starter ``MANUSCRIPT_STATE.yaml`` in a directory.
* ``trace`` — extract scriptorium skill invocations from Claude Code
  transcripts as structured trace records (see ``schemas/trace.schema.json``).
"""

from __future__ import annotations

import json
import re
import shutil
import uuid
from collections.abc import Iterator
from datetime import datetime, timezone
from importlib import resources
from importlib.abc import Traversable
from pathlib import Path
from typing import Any

import click
import yaml
from jsonschema import Draft202012Validator

from scriptorium import __version__

PACKAGE = "scriptorium"
SCHEMA_SUBDIR = "_schemas"
PLUGIN_SUBDIR = "_claude_plugin"
TEMPLATES_SUBDIR = "_templates"
SKILLS_SUBDIR = "_skills"
KNOWLEDGE_SUBDIR = "_knowledge"
SCHEMA_FILENAME = "manuscript-state.schema.json"
TRACE_SCHEMA_FILENAME = "trace.schema.json"
TRACE_SCHEMA_VERSION = 1
SCRIPTORIUM_SKILL_PREFIX = "scriptorium:"
TIER_STRUCTURED_ONLY = "structured-only"
TIER_OUTPUT_TEXT = "output-text"
TIER_MANUSCRIPT_CHUNK = "manuscript-chunk"
CONSENT_TIERS = (TIER_STRUCTURED_ONLY, TIER_OUTPUT_TEXT, TIER_MANUSCRIPT_CHUNK)
DEFAULT_PROJECTS_DIR = Path.home() / ".claude" / "projects"
TEMPLATE_FILENAME = "MANUSCRIPT_STATE.yaml"
EXAMPLE_TEMPLATE_FILENAME = "MANUSCRIPT_STATE.example.yaml"
DEFAULT_INSTALL_TARGET = Path.home() / ".claude" / "plugins" / "scriptorium"
COMMAND_NAME_RE = re.compile(r"<command-name>/scriptorium:([\w-]+)</command-name>")


def _package_root() -> Traversable:
    return resources.files(PACKAGE)


def _repo_root() -> Path | None:
    # Editable installs leave the package files under <repo>/src/scriptorium;
    # wheel installs don't, so this returns None for them.
    pkg_file = Path(__file__).resolve()
    for candidate in (pkg_file.parent.parent.parent, pkg_file.parent.parent):
        if (candidate / "pyproject.toml").is_file() and (candidate / ".claude-plugin").is_dir():
            return candidate
    return None


def _bundled_dir(pkg_subdir: str, repo_subdir: str) -> Traversable | None:
    # Hatchling force-include populates package data inside built wheels.
    # Editable installs don't apply force-include, so fall back to the
    # repo source layout when running from `pip install -e .`.
    pkg_dir = _package_root().joinpath(pkg_subdir)
    if pkg_dir.is_dir():
        return pkg_dir
    repo = _repo_root()
    if repo is not None:
        candidate = repo / repo_subdir
        if candidate.is_dir():
            return candidate
    return None


def _copy_traversable(src: Traversable, dest: Path) -> None:
    if src.is_dir():
        dest.mkdir(parents=True, exist_ok=True)
        for child in src.iterdir():
            _copy_traversable(child, dest / child.name)
    else:
        dest.write_bytes(src.read_bytes())


def _load_schema() -> dict[str, Any]:
    schemas_dir = _bundled_dir(SCHEMA_SUBDIR, "schemas")
    if schemas_dir is None:
        raise click.ClickException("JSON Schema is not bundled in this build.")
    text = schemas_dir.joinpath(SCHEMA_FILENAME).read_text(encoding="utf-8")
    parsed: dict[str, Any] = json.loads(text)
    return parsed


def _load_trace_schema() -> dict[str, Any]:
    schemas_dir = _bundled_dir(SCHEMA_SUBDIR, "schemas")
    if schemas_dir is None:
        raise click.ClickException("Trace schema is not bundled in this build.")
    text = schemas_dir.joinpath(TRACE_SCHEMA_FILENAME).read_text(encoding="utf-8")
    parsed: dict[str, Any] = json.loads(text)
    return parsed


def _now_iso() -> str:
    """Return the current time as an ISO 8601 string with Z suffix."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _decode_project_dir_name(encoded: str) -> str:
    """Convert Claude Code's encoded-cwd directory name back into a path.

    Claude Code stores transcripts under ``~/.claude/projects/<encoded>/``
    where ``<encoded>`` replaces path separators with hyphens. For example
    ``-Users-davsean-Documents-git-scriptorium`` decodes to
    ``/Users/davsean/Documents/git/scriptorium``. The encoding is lossy
    (hyphens in real path components are indistinguishable from separators),
    so this is best-effort, used only for the ``--project`` filter.
    """
    if not encoded.startswith("-"):
        return encoded
    return "/" + encoded[1:].replace("-", "/")


def _detect_invocation(message: dict[str, Any]) -> tuple[str, str] | None:
    """Detect a scriptorium skill invocation in a single message.

    Returns ``(skill_name, source_kind)`` where ``source_kind`` is one of
    ``"user-slash"`` (the user typed ``/scriptorium:foo`` and Claude Code
    wrapped it in a ``<command-name>`` tag) or ``"assistant-tool"`` (the
    assistant called the ``Skill`` tool with a ``scriptorium:`` skill).
    Returns ``None`` if the message is not a skill invocation.
    """
    role = message.get("role")
    content = message.get("content")

    if role == "user":
        text_blocks: list[str] = []
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get("type") == "text":
                    text_blocks.append(str(c.get("text", "")))
        elif isinstance(content, str):
            text_blocks.append(content)
        for text in text_blocks:
            match = COMMAND_NAME_RE.search(text)
            if match:
                return match.group(1), "user-slash"

    if role == "assistant" and isinstance(content, list):
        for c in content:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use" and c.get("name") == "Skill":
                skill_id = str(c.get("input", {}).get("skill", ""))
                if skill_id.startswith(SCRIPTORIUM_SKILL_PREFIX):
                    return skill_id[len(SCRIPTORIUM_SKILL_PREFIX) :], "assistant-tool"

    return None


def _extract_invocations(
    transcript_path: Path,
) -> Iterator[dict[str, Any]]:
    """Walk a JSONL transcript and yield raw invocation summaries.

    Each yielded dict carries:
      - ``skill_name``, ``source_kind``
      - ``session_id`` (from the transcript header, may be None)
      - ``invoked_at`` (timestamp string from the invocation line, may be None)
      - ``model_name`` (assistant ``message.model`` field, may be None)
      - ``thinking_used`` (bool: was a ``type=thinking`` block seen during
        the response window)
      - ``output_chunks`` (list of assistant text-block strings from the
        response window — used to populate ``skill_output.text`` at tiers
        that permit it; never includes thinking text)
      - ``transcript_path`` (the file the invocation was read from)
    """
    session_id: str | None = None
    current: dict[str, Any] | None = None
    text: str
    try:
        text = transcript_path.read_text(encoding="utf-8")
    except OSError:
        return

    def _finalize(c: dict[str, Any]) -> dict[str, Any]:
        c["session_id"] = session_id
        c["transcript_path"] = str(transcript_path)
        return c

    for raw_line in text.splitlines():
        if not raw_line.strip():
            continue
        try:
            d = json.loads(raw_line)
        except json.JSONDecodeError:
            continue
        if not isinstance(d, dict):
            continue

        if session_id is None:
            session_id = d.get("sessionId") or None

        msg = d.get("message")
        if not isinstance(msg, dict):
            continue

        invocation = _detect_invocation(msg)
        if invocation is not None:
            if current is not None:
                yield _finalize(current)
            current = {
                "skill_name": invocation[0],
                "source_kind": invocation[1],
                "invoked_at": d.get("timestamp"),
                "model_name": None,
                "thinking_used": False,
                "output_chunks": [],
            }
            continue

        if current is None:
            continue

        role = msg.get("role")
        if role == "user":
            # User turn ends the response window for the current invocation.
            yield _finalize(current)
            current = None
            continue

        if role == "assistant":
            if current["model_name"] is None:
                model = msg.get("model")
                if isinstance(model, str):
                    current["model_name"] = model
            content = msg.get("content")
            if isinstance(content, list):
                for c in content:
                    if not isinstance(c, dict):
                        continue
                    block_type = c.get("type")
                    if block_type == "thinking":
                        current["thinking_used"] = True
                    elif block_type == "text":
                        chunk = c.get("text")
                        if isinstance(chunk, str) and chunk:
                            current["output_chunks"].append(chunk)

    if current is not None:
        yield _finalize(current)


def _build_trace_record(invocation: dict[str, Any], *, tier: str) -> dict[str, Any]:
    """Build a trace record from a raw invocation summary, applying the tier."""
    model_name = invocation.get("model_name")
    provider = "unknown"
    if isinstance(model_name, str) and "claude" in model_name.lower():
        provider = "anthropic"

    record: dict[str, Any] = {
        "trace_schema_version": TRACE_SCHEMA_VERSION,
        "submission_id": str(uuid.uuid4()),
        "submitted_at": _now_iso(),
        "scriptorium_version": __version__,
        "consent_tier": tier,
        "provenance": {
            "source": "claude-code-transcript",
            "transcript_path": invocation.get("transcript_path", ""),
        },
        "skill": {
            "name": invocation["skill_name"],
            "invocation_surface": "claude-code",
        },
        "model": {
            "provider": provider,
            "thinking_used": bool(invocation.get("thinking_used")),
            "thinking_text_captured": False,
        },
    }
    if isinstance(model_name, str):
        record["model"]["name"] = model_name
    session_id = invocation.get("session_id")
    if isinstance(session_id, str) and session_id:
        record["provenance"]["session_id"] = session_id

    if tier in (TIER_OUTPUT_TEXT, TIER_MANUSCRIPT_CHUNK):
        chunks = invocation.get("output_chunks") or []
        text = "\n\n".join(chunks).strip()
        if text:
            record["skill_output"] = {"text": text}

    return record


def _iter_transcripts(projects_dir: Path) -> Iterator[Path]:
    """Yield JSONL transcript files under ``projects_dir``."""
    if not projects_dir.is_dir():
        return
    for project_dir in sorted(projects_dir.iterdir()):
        if not project_dir.is_dir():
            continue
        yield from sorted(project_dir.glob("*.jsonl"))


def _parse_since(value: str) -> datetime:
    """Parse a ``--since`` value as an ISO 8601 date or datetime."""
    candidates = (value, value + "T00:00:00", value + "T00:00:00+00:00")
    for candidate in candidates:
        try:
            parsed = datetime.fromisoformat(candidate.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed
        except ValueError:
            continue
    raise click.BadParameter(
        f"--since must be ISO 8601 (e.g. 2026-05-17 or 2026-05-17T14:30:00Z); got {value!r}"
    )


def _load_template(*, example: bool = False) -> str:
    """Load the bundled MANUSCRIPT_STATE.yaml template text.

    When ``example=True``, returns the fully-populated reference template
    (fictional biomedical manuscript). Otherwise returns the blank-with-
    comments starter template.
    """
    templates_dir = _bundled_dir(TEMPLATES_SUBDIR, "templates")
    filename = EXAMPLE_TEMPLATE_FILENAME if example else TEMPLATE_FILENAME
    if templates_dir is None:
        raise click.ClickException(f"Template {filename} is not bundled in this build.")
    template_resource = templates_dir.joinpath(filename)
    if not template_resource.is_file():
        raise click.ClickException(f"Template {filename} is not bundled in this build.")
    return template_resource.read_text(encoding="utf-8")


def _parse_skill_metadata(skill_md_text: str) -> tuple[str | None, list[str]]:
    # SKILL.md files use YAML frontmatter delimited by `---`. Pull the
    # `description` and `grounding` fields out; ignore the body.
    if not skill_md_text.startswith("---"):
        return None, []
    end = skill_md_text.find("\n---", 3)
    if end == -1:
        return None, []
    frontmatter = skill_md_text[3:end]
    try:
        parsed = yaml.safe_load(frontmatter)
    except yaml.YAMLError:
        return None, []
    if not isinstance(parsed, dict):
        return None, []
    description = parsed.get("description")
    grounding_raw = parsed.get("grounding", [])
    grounding: list[str] = (
        [str(g) for g in grounding_raw] if isinstance(grounding_raw, list) else []
    )
    return (str(description) if description else None), grounding


def _iter_skills() -> list[dict[str, Any]]:
    skills_root = _bundled_dir(SKILLS_SUBDIR, "skills")
    if skills_root is None:
        return []
    out: list[dict[str, Any]] = []
    for entry in sorted(skills_root.iterdir(), key=lambda e: e.name):
        if not entry.is_dir():
            continue
        description: str | None = None
        grounding: list[str] = []
        prompt: str | None = None
        skill_md = entry.joinpath("SKILL.md")
        if skill_md.is_file():
            description, grounding = _parse_skill_metadata(skill_md.read_text(encoding="utf-8"))
        prompt_md = entry.joinpath("prompt.md")
        if prompt_md.is_file():
            prompt = prompt_md.read_text(encoding="utf-8")
        out.append(
            {
                "name": entry.name,
                "description": description,
                "grounding": grounding,
                "prompt": prompt,
            }
        )
    return out


def _remove_existing(dest: Path) -> None:
    if dest.is_symlink() or dest.is_file():
        dest.unlink()
    elif dest.is_dir():
        shutil.rmtree(dest)


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="scriptorium")
def main() -> None:
    """Scriptorium: agentic operating system for scholarly writing."""


@main.command()
@click.option(
    "--mode",
    type=click.Choice(["dev-link", "copy"]),
    default="copy",
    show_default=True,
    help="dev-link symlinks the source repo; copy installs from package data.",
)
@click.option(
    "--target",
    type=click.Path(path_type=Path),
    default=None,
    help="Install target (default: ~/.claude/plugins/scriptorium).",
)
@click.option("--force", is_flag=True, help="Overwrite an existing install.")
def install(mode: str, target: Path | None, force: bool) -> None:
    """Install scriptorium into the Claude Code plugins directory."""
    dest = target if target is not None else DEFAULT_INSTALL_TARGET
    if dest.exists() or dest.is_symlink():
        if not force:
            raise click.ClickException(f"{dest} already exists. Re-run with --force to overwrite.")
        _remove_existing(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if mode == "dev-link":
        repo = _repo_root()
        if repo is None:
            raise click.ClickException(
                "dev-link requires an editable install with the source repo "
                "reachable from the installed package."
            )
        dest.symlink_to(repo, target_is_directory=True)
        click.echo(f"Linked {repo} -> {dest}")
        return
    dest.mkdir()
    plugin_src = _bundled_dir(PLUGIN_SUBDIR, ".claude-plugin")
    if plugin_src is None:
        raise click.ClickException("Plugin manifest is not bundled in this build.")
    _copy_traversable(plugin_src, dest / ".claude-plugin")
    schemas_src = _bundled_dir(SCHEMA_SUBDIR, "schemas")
    if schemas_src is None:
        raise click.ClickException("JSON Schema is not bundled in this build.")
    _copy_traversable(schemas_src, dest / "schemas")
    skills_src = _bundled_dir(SKILLS_SUBDIR, "skills")
    if skills_src is not None:
        _copy_traversable(skills_src, dest / "skills")
    templates_src = _bundled_dir(TEMPLATES_SUBDIR, "templates")
    if templates_src is not None:
        _copy_traversable(templates_src, dest / "templates")
    knowledge_src = _bundled_dir(KNOWLEDGE_SUBDIR, "knowledge")
    if knowledge_src is not None:
        _copy_traversable(knowledge_src, dest / "knowledge")
    click.echo(f"Installed scriptorium plugin at {dest}")


@main.command()
@click.argument(
    "path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
)
def validate(path: Path) -> None:
    """Validate a MANUSCRIPT_STATE.yaml file against the JSON Schema."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise click.ClickException(f"YAML parse error: {exc}") from exc
    if not isinstance(data, dict):
        raise click.ClickException(
            f"Top-level YAML document must be a mapping (got {type(data).__name__})."
        )
    schema = _load_schema()
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    if errors:
        for err in errors:
            location = "/".join(str(p) for p in err.absolute_path) or "<root>"
            click.echo(f"  {location}: {err.message}", err=True)
        raise click.ClickException(f"{path} is invalid ({len(errors)} error(s)).")
    click.echo(f"{path}: valid")


@main.command(name="prompt-pack")
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path, dir_okay=False),
    default=None,
    help="Write the prompt pack to a file instead of stdout.",
)
def prompt_pack(output: Path | None) -> None:
    """Concatenate bundled skill prompts into one platform-neutral file."""
    skills = _iter_skills()
    parts: list[str] = [
        "# scriptorium prompt pack",
        "",
        f"_Generated from scriptorium v{__version__}._",
        "",
    ]
    included = 0
    for skill in skills:
        prompt = skill["prompt"]
        if not prompt:
            continue
        included += 1
        parts.append("---")
        parts.append(f"## Skill: {skill['name']}")
        if skill["description"]:
            parts.append("")
            parts.append(f"_{skill['description']}_")
        parts.append("")
        parts.append(prompt.rstrip())
        parts.append("")
    if included == 0:
        parts.append("_(no skills with prompt.md are bundled in this build)_")
        parts.append("")
    text = "\n".join(parts)
    if output is not None:
        output.write_text(text, encoding="utf-8")
        click.echo(f"Wrote {output} ({included} skill(s)).")
    else:
        click.echo(text)


@main.command(name="list")
def list_skills() -> None:
    """List bundled skills with descriptions and grounding references."""
    skills = _iter_skills()
    if not skills:
        click.echo("(no skills bundled in this build)")
        return
    for skill in skills:
        description = skill["description"] or "(no description)"
        click.echo(f"{skill['name']}: {description}")
        for grounding in skill["grounding"]:
            click.echo(f"  grounding: {grounding}")


@main.command()
@click.argument(
    "manuscript_dir",
    type=click.Path(file_okay=False, path_type=Path),
)
@click.option(
    "--force",
    is_flag=True,
    help="Overwrite an existing MANUSCRIPT_STATE.yaml.",
)
@click.option(
    "--example",
    "use_example",
    is_flag=True,
    help=(
        "Write a fully-populated reference manuscript (fictional biomedical "
        "paper) instead of the blank starter. Useful for learning the schema."
    ),
)
def init(manuscript_dir: Path, force: bool, use_example: bool) -> None:
    """Scaffold a starter MANUSCRIPT_STATE.yaml in a manuscript directory."""
    manuscript_dir.mkdir(parents=True, exist_ok=True)
    dest = manuscript_dir / TEMPLATE_FILENAME
    if dest.exists() and not force:
        raise click.ClickException(f"{dest} already exists. Re-run with --force to overwrite.")
    dest.write_text(_load_template(example=use_example), encoding="utf-8")
    flavor = "example" if use_example else "blank"
    click.echo(f"Wrote {dest} ({flavor})")


@main.command()
@click.option(
    "--projects-dir",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help=(
        "Directory of Claude Code transcripts (default: ~/.claude/projects). "
        "Each subdirectory contains JSONL session files."
    ),
)
@click.option(
    "--skill",
    "skill_filter",
    default=None,
    help="Only emit records for invocations of this skill name.",
)
@click.option(
    "--since",
    default=None,
    help="Only emit records for invocations on or after this ISO 8601 date / datetime.",
)
@click.option(
    "--project",
    "project_filter",
    default=None,
    help=(
        "Only emit records from transcripts of the project at this path. "
        "Matched against the decoded directory name under projects-dir."
    ),
)
@click.option(
    "--tier",
    type=click.Choice(CONSENT_TIERS),
    default=TIER_STRUCTURED_ONLY,
    show_default=True,
    help=(
        "Consent tier to apply. structured-only (default) emits counts and "
        "metadata only. output-text adds skill output text. manuscript-chunk "
        "adds the manuscript chunk the skill ran on (not yet inferrable from "
        "transcripts, so currently equivalent to output-text)."
    ),
)
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path, dir_okay=False),
    default=None,
    help="Write trace records to a file instead of stdout.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["jsonl", "json"]),
    default="jsonl",
    show_default=True,
    help="Output format: jsonl (one record per line) or json (one array).",
)
def trace(
    projects_dir: Path | None,
    skill_filter: str | None,
    since: str | None,
    project_filter: str | None,
    tier: str,
    output: Path | None,
    output_format: str,
) -> None:
    """Extract scriptorium skill invocations from Claude Code transcripts.

    Reads JSONL transcripts under the projects directory, finds skill
    invocations (user-typed /scriptorium:foo slash commands and assistant
    Skill tool calls targeting scriptorium:*), and emits trace records
    conforming to schemas/trace.schema.json.

    Local-only: this command reads transcripts and writes records to your
    disk. No network calls. No transcript files are modified.

    Note on thinking: Claude Code transcripts persist thinking-block
    structure but not thinking text content. Records record whether
    thinking was used (model.thinking_used) but never include the thinking
    text itself; model.thinking_text_captured is always false for records
    from this command.
    """
    src_dir = projects_dir if projects_dir is not None else DEFAULT_PROJECTS_DIR
    if not src_dir.is_dir():
        raise click.ClickException(f"Projects directory not found: {src_dir}")

    since_dt = _parse_since(since) if since else None
    schema = _load_trace_schema()
    validator = Draft202012Validator(schema)

    records: list[dict[str, Any]] = []
    transcripts_seen = 0
    invocations_seen = 0
    invalid_records = 0

    for transcript_path in _iter_transcripts(src_dir):
        if project_filter is not None:
            decoded = _decode_project_dir_name(transcript_path.parent.name)
            raw_name = transcript_path.parent.name
            if decoded != str(project_filter) and raw_name != str(project_filter):
                continue
        if since_dt is not None:
            try:
                mtime = datetime.fromtimestamp(transcript_path.stat().st_mtime, tz=timezone.utc)
            except OSError:
                continue
            if mtime < since_dt:
                continue
        transcripts_seen += 1

        for invocation in _extract_invocations(transcript_path):
            invocations_seen += 1
            if skill_filter is not None and invocation["skill_name"] != skill_filter:
                continue
            record = _build_trace_record(invocation, tier=tier)
            errors = sorted(validator.iter_errors(record), key=lambda e: list(e.absolute_path))
            if errors:
                invalid_records += 1
                click.echo(
                    f"warning: invalid record from {transcript_path}: {errors[0].message}",
                    err=True,
                )
                continue
            records.append(record)

    if output_format == "jsonl":
        text = "\n".join(json.dumps(r, sort_keys=True) for r in records)
        if records:
            text += "\n"
    else:
        text = json.dumps(records, indent=2, sort_keys=True)
        if not text.endswith("\n"):
            text += "\n"

    if output is not None:
        output.write_text(text, encoding="utf-8")
        click.echo(
            f"Wrote {len(records)} record(s) to {output} "
            f"(scanned {transcripts_seen} transcript(s), "
            f"found {invocations_seen} invocation(s)).",
            err=True,
        )
    else:
        click.echo(text, nl=False)
        if invalid_records:
            click.echo(
                f"({invalid_records} record(s) skipped as invalid)",
                err=True,
            )


if __name__ == "__main__":  # pragma: no cover
    main()
