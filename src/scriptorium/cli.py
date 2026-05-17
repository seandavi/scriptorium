"""Command-line interface for scriptorium.

The CLI exposes five subcommands:

* ``install`` — copy or link the plugin into a Claude Code plugins dir.
* ``validate`` — lint a ``MANUSCRIPT_STATE.yaml`` against the JSON Schema.
* ``prompt-pack`` — concatenate bundled skill prompts for platform-neutral use.
* ``list`` — list bundled skills with descriptions and grounding references.
* ``init`` — scaffold a starter ``MANUSCRIPT_STATE.yaml`` in a directory.
"""

from __future__ import annotations

import json
import shutil
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
SCHEMA_FILENAME = "manuscript-state.schema.json"
TEMPLATE_FILENAME = "MANUSCRIPT_STATE.yaml"
EXAMPLE_TEMPLATE_FILENAME = "MANUSCRIPT_STATE.example.yaml"
DEFAULT_INSTALL_TARGET = Path.home() / ".claude" / "plugins" / "scriptorium"


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


if __name__ == "__main__":  # pragma: no cover
    main()
