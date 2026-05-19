"""Tests for the ``scriptorium`` CLI."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import click
import pytest
import yaml
from click.testing import CliRunner

from scriptorium import cli

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def runner() -> CliRunner:
    """Provide a Click ``CliRunner``."""
    return CliRunner()


def _combined_output(result: Any) -> str:
    """Return stdout + stderr from a CliRunner result.

    Click 8.2 always separates stderr; older versions only do so when
    ``mix_stderr=False``. Using the union avoids brittle assertions.
    """
    out = result.output or ""
    err = getattr(result, "stderr", None) or ""
    return out + err


def test_help_lists_all_subcommands(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["--help"])
    assert result.exit_code == 0
    for command in ("install", "validate", "prompt-pack", "list", "init"):
        assert command in result.output


def test_version_flag(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["--version"])
    assert result.exit_code == 0
    assert "scriptorium" in result.output


def test_validate_valid_fixture(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["validate", str(FIXTURES / "valid_state.yaml")])
    assert result.exit_code == 0, result.output
    assert "valid" in result.output


def test_validate_invalid_fixture(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["validate", str(FIXTURES / "invalid_state.yaml")])
    assert result.exit_code != 0
    assert "invalid" in _combined_output(result).lower()


def test_validate_malformed_yaml(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["validate", str(FIXTURES / "malformed.yaml")])
    assert result.exit_code != 0
    assert "yaml" in _combined_output(result).lower()


def test_validate_non_mapping(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["validate", str(FIXTURES / "not_a_mapping.yaml")])
    assert result.exit_code != 0
    assert "mapping" in _combined_output(result).lower()


def test_validate_missing_file(runner: CliRunner, tmp_path: Path) -> None:
    missing = tmp_path / "nope.yaml"
    result = runner.invoke(cli.main, ["validate", str(missing)])
    assert result.exit_code != 0


def test_init_creates_state_file(runner: CliRunner, tmp_path: Path) -> None:
    manuscript = tmp_path / "manuscript"
    result = runner.invoke(cli.main, ["init", str(manuscript)])
    assert result.exit_code == 0, result.output
    dest = manuscript / "MANUSCRIPT_STATE.yaml"
    assert dest.is_file()
    parsed = yaml.safe_load(dest.read_text(encoding="utf-8"))
    assert "project" in parsed
    assert "document_phase" in parsed


def test_init_then_validate_roundtrip(runner: CliRunner, tmp_path: Path) -> None:
    """The scaffolded MANUSCRIPT_STATE.yaml should pass its own schema."""
    manuscript = tmp_path / "manuscript"
    runner.invoke(cli.main, ["init", str(manuscript)])
    result = runner.invoke(cli.main, ["validate", str(manuscript / "MANUSCRIPT_STATE.yaml")])
    assert result.exit_code == 0, result.output


def test_init_refuses_to_overwrite_without_force(runner: CliRunner, tmp_path: Path) -> None:
    runner.invoke(cli.main, ["init", str(tmp_path)])
    result = runner.invoke(cli.main, ["init", str(tmp_path)])
    assert result.exit_code != 0
    assert "already exists" in _combined_output(result)


def test_init_force_overwrites(runner: CliRunner, tmp_path: Path) -> None:
    runner.invoke(cli.main, ["init", str(tmp_path)])
    (tmp_path / "MANUSCRIPT_STATE.yaml").write_text("clobbered: true\n")
    result = runner.invoke(cli.main, ["init", str(tmp_path), "--force"])
    assert result.exit_code == 0
    parsed = yaml.safe_load((tmp_path / "MANUSCRIPT_STATE.yaml").read_text())
    assert "project" in parsed


def test_init_example_writes_filled_template(runner: CliRunner, tmp_path: Path) -> None:
    manuscript = tmp_path / "example-manuscript"
    result = runner.invoke(cli.main, ["init", str(manuscript), "--example"])
    assert result.exit_code == 0, result.output
    assert "example" in result.output
    parsed = yaml.safe_load((manuscript / "MANUSCRIPT_STATE.yaml").read_text())
    # The example is filled-in: core_claims has at least one entry, and
    # known_weaknesses is populated. The blank template has empty lists
    # for both — that's the load-bearing difference.
    assert isinstance(parsed["core_claims"], list) and len(parsed["core_claims"]) >= 1
    assert isinstance(parsed["known_weaknesses"], list) and len(parsed["known_weaknesses"]) >= 1
    assert parsed["project"]["title"]
    assert parsed["project"]["target_type"] in {
        "manuscript",
        "grant",
        "review",
        "preprint",
        "book-chapter",
        "thesis",
        "white-paper",
        "other",
    }


def test_init_example_passes_validate(runner: CliRunner, tmp_path: Path) -> None:
    manuscript = tmp_path / "example-manuscript"
    runner.invoke(cli.main, ["init", str(manuscript), "--example"])
    result = runner.invoke(cli.main, ["validate", str(manuscript / "MANUSCRIPT_STATE.yaml")])
    assert result.exit_code == 0, result.output


def test_init_example_with_force(runner: CliRunner, tmp_path: Path) -> None:
    runner.invoke(cli.main, ["init", str(tmp_path)])
    result = runner.invoke(cli.main, ["init", str(tmp_path), "--example", "--force"])
    assert result.exit_code == 0
    parsed = yaml.safe_load((tmp_path / "MANUSCRIPT_STATE.yaml").read_text())
    assert len(parsed["core_claims"]) >= 1


def test_init_example_without_force_refuses_to_overwrite(runner: CliRunner, tmp_path: Path) -> None:
    runner.invoke(cli.main, ["init", str(tmp_path)])
    result = runner.invoke(cli.main, ["init", str(tmp_path), "--example"])
    assert result.exit_code != 0
    assert "already exists" in _combined_output(result)


def test_list_runs(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["list"])
    assert result.exit_code == 0


def test_list_finds_bundled_citation_audit(runner: CliRunner) -> None:
    """The real bundled skills (not monkeypatched) load and surface."""
    result = runner.invoke(cli.main, ["list"])
    assert result.exit_code == 0
    assert "citation-audit" in result.output
    assert "knowledge/critique-techniques/citation-claim-alignment.md" in result.output


def test_prompt_pack_includes_citation_audit(runner: CliRunner) -> None:
    """The bundled citation-audit skill's prompt body lands in the pack."""
    result = runner.invoke(cli.main, ["prompt-pack"])
    assert result.exit_code == 0
    assert "## Skill: citation-audit" in result.output
    assert "Citation audit (platform-neutral prompt)" in result.output


def test_list_shows_bundled_skills(runner: CliRunner, monkeypatch: pytest.MonkeyPatch) -> None:
    fake = [
        {
            "name": "citation-audit",
            "description": "Audit citations against the bibliography.",
            "grounding": ["docs/skills/citation-audit.md"],
            "prompt": "...prompt body...",
        }
    ]
    monkeypatch.setattr(cli, "_iter_skills", lambda: fake)
    result = runner.invoke(cli.main, ["list"])
    assert result.exit_code == 0
    assert "citation-audit" in result.output
    assert "Audit citations" in result.output
    assert "docs/skills/citation-audit.md" in result.output


def test_prompt_pack_to_stdout(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["prompt-pack"])
    assert result.exit_code == 0
    assert "scriptorium prompt pack" in result.output


def test_prompt_pack_to_file(runner: CliRunner, tmp_path: Path) -> None:
    out = tmp_path / "pack.md"
    result = runner.invoke(cli.main, ["prompt-pack", "--output", str(out)])
    assert result.exit_code == 0
    assert out.is_file()
    assert "scriptorium prompt pack" in out.read_text(encoding="utf-8")


def test_prompt_pack_with_bundled_skills(
    runner: CliRunner, monkeypatch: pytest.MonkeyPatch
) -> None:
    fake = [
        {
            "name": "skill-a",
            "description": "Does A.",
            "grounding": [],
            "prompt": "Prompt for A.",
        },
        {
            "name": "skill-b",
            "description": None,
            "grounding": [],
            "prompt": None,
        },
    ]
    monkeypatch.setattr(cli, "_iter_skills", lambda: fake)
    result = runner.invoke(cli.main, ["prompt-pack"])
    assert result.exit_code == 0
    assert "## Skill: skill-a" in result.output
    assert "Prompt for A." in result.output
    assert "## Skill: skill-b" not in result.output


def test_install_copy_into_tmpdir(runner: CliRunner, tmp_path: Path) -> None:
    target = tmp_path / "plugins" / "scriptorium"
    result = runner.invoke(cli.main, ["install", "--mode", "copy", "--target", str(target)])
    assert result.exit_code == 0, result.output
    assert (target / ".claude-plugin" / "plugin.json").is_file()
    assert (target / "schemas" / cli.SCHEMA_FILENAME).is_file()


def test_install_refuses_to_overwrite_without_force(runner: CliRunner, tmp_path: Path) -> None:
    target = tmp_path / "plug"
    runner.invoke(cli.main, ["install", "--mode", "copy", "--target", str(target)])
    result = runner.invoke(cli.main, ["install", "--mode", "copy", "--target", str(target)])
    assert result.exit_code != 0
    assert "already exists" in _combined_output(result)


def test_install_force_overwrites(runner: CliRunner, tmp_path: Path) -> None:
    target = tmp_path / "plug"
    runner.invoke(cli.main, ["install", "--mode", "copy", "--target", str(target)])
    result = runner.invoke(
        cli.main, ["install", "--mode", "copy", "--target", str(target), "--force"]
    )
    assert result.exit_code == 0, result.output


def test_install_force_overwrites_symlink(runner: CliRunner, tmp_path: Path) -> None:
    target = tmp_path / "plug"
    other = tmp_path / "other"
    other.mkdir()
    target.symlink_to(other, target_is_directory=True)
    result = runner.invoke(
        cli.main, ["install", "--mode", "copy", "--target", str(target), "--force"]
    )
    assert result.exit_code == 0, result.output
    assert not target.is_symlink()


def test_install_force_overwrites_file(runner: CliRunner, tmp_path: Path) -> None:
    target = tmp_path / "plug"
    target.write_text("preexisting")
    result = runner.invoke(
        cli.main, ["install", "--mode", "copy", "--target", str(target), "--force"]
    )
    assert result.exit_code == 0, result.output
    assert target.is_dir()


def test_install_dev_link_when_repo_found(
    runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fake_repo = tmp_path / "fake-repo"
    fake_repo.mkdir()
    monkeypatch.setattr(cli, "_repo_root", lambda: fake_repo)
    target = tmp_path / "plug"
    result = runner.invoke(cli.main, ["install", "--mode", "dev-link", "--target", str(target)])
    assert result.exit_code == 0, result.output
    assert target.is_symlink()
    assert target.resolve() == fake_repo.resolve()


def test_install_dev_link_errors_when_repo_missing(
    runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(cli, "_repo_root", lambda: None)
    target = tmp_path / "plug"
    result = runner.invoke(cli.main, ["install", "--mode", "dev-link", "--target", str(target)])
    assert result.exit_code != 0
    assert "editable install" in _combined_output(result)


def test_install_default_target_uses_home(
    runner: CliRunner, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fake_home = tmp_path / "home"
    fake_home.mkdir()
    monkeypatch.setattr(cli, "DEFAULT_INSTALL_TARGET", fake_home / "plug")
    result = runner.invoke(cli.main, ["install", "--mode", "copy"])
    assert result.exit_code == 0, result.output
    assert (fake_home / "plug" / ".claude-plugin" / "plugin.json").is_file()


def test_parse_skill_metadata_extracts_description() -> None:
    text = (
        "---\n"
        "name: example\n"
        "description: An example skill.\n"
        "grounding:\n"
        "  - docs/a.md\n"
        "  - docs/b.md\n"
        "---\n"
        "Body of skill.\n"
    )
    description, grounding = cli._parse_skill_metadata(text)
    assert description == "An example skill."
    assert grounding == ["docs/a.md", "docs/b.md"]


def test_parse_skill_metadata_missing_frontmatter() -> None:
    description, grounding = cli._parse_skill_metadata("Just body, no frontmatter.")
    assert description is None
    assert grounding == []


def test_parse_skill_metadata_unterminated_frontmatter() -> None:
    description, grounding = cli._parse_skill_metadata("---\nname: x\n")
    assert description is None
    assert grounding == []


def test_parse_skill_metadata_invalid_yaml() -> None:
    text = "---\n:::not yaml:::\n---\nbody\n"
    description, grounding = cli._parse_skill_metadata(text)
    assert description is None
    assert grounding == []


def test_iter_skills_reads_bundled_layout(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Point ``_iter_skills`` at a temporary skills tree on disk."""
    skills_root = tmp_path / "skills"
    skill_a = skills_root / "skill-a"
    skill_a.mkdir(parents=True)
    (skill_a / "SKILL.md").write_text(
        "---\nname: skill-a\ndescription: A.\ngrounding:\n  - docs/a.md\n---\nbody\n",
        encoding="utf-8",
    )
    (skill_a / "prompt.md").write_text("Prompt A.\n", encoding="utf-8")
    # A non-directory entry should be ignored.
    (skills_root / "stray.txt").write_text("ignore me", encoding="utf-8")

    def _fake_bundled_dir(pkg: str, repo: str) -> Path | None:
        return skills_root if repo == "skills" else None

    monkeypatch.setattr(cli, "_bundled_dir", _fake_bundled_dir)
    skills = cli._iter_skills()
    assert len(skills) == 1
    assert skills[0]["name"] == "skill-a"
    assert skills[0]["description"] == "A."
    assert skills[0]["grounding"] == ["docs/a.md"]
    assert skills[0]["prompt"] == "Prompt A.\n"


def test_iter_skills_returns_empty_when_unbundled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(cli, "_bundled_dir", lambda pkg, repo: None)
    assert cli._iter_skills() == []


def test_load_template_errors_when_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(cli, "_bundled_dir", lambda pkg, repo: None)
    with pytest.raises(click.ClickException) as exc_info:
        cli._load_template()
    assert "Template" in str(exc_info.value.message)


def test_repo_root_finds_real_repo() -> None:
    """Sanity check: editable install should locate the repo root."""
    repo = cli._repo_root()
    # In an editable install this returns the repo; in a wheel install it
    # returns None. Both are valid outcomes — but the type must hold.
    assert repo is None or (repo / "pyproject.toml").is_file()


def test_iter_skills_skill_md_without_prompt(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    skills_root = tmp_path / "skills"
    skill = skills_root / "x"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nname: x\ndescription: X.\n---\nbody\n", encoding="utf-8")

    monkeypatch.setattr(
        cli,
        "_bundled_dir",
        lambda pkg, repo: skills_root if repo == "skills" else None,
    )
    skills: list[dict[str, Any]] = cli._iter_skills()
    assert skills[0]["prompt"] is None
    assert skills[0]["grounding"] == []


# ---------------------------------------------------------------------------
# trace subcommand


TRANSCRIPTS_DIR = FIXTURES / "transcripts"


def _trace_records_from_output(out: str) -> list[dict[str, Any]]:
    """Parse stdout from `trace` (jsonl form) into a list of dicts."""
    records: list[dict[str, Any]] = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        records.append(json.loads(line))
    return records


def test_trace_extracts_user_slash_invocation(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        ["trace", "--projects-dir", str(TRANSCRIPTS_DIR), "--project", "-tmp-project-a"],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    # project-a has two sessions: one slash + one tool-use; both should be picked up
    skill_names = sorted(r["skill"]["name"] for r in records)
    assert "citation-audit" in skill_names
    assert "reviewer-simulation" in skill_names


def test_trace_extracts_tool_use_invocation(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--skill",
            "reviewer-simulation",
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    assert len(records) == 1
    rec = records[0]
    assert rec["skill"]["name"] == "reviewer-simulation"
    assert rec["skill"]["invocation_surface"] == "claude-code"
    assert rec["model"]["provider"] == "anthropic"
    assert rec["model"]["name"] == "claude-opus-4-7"
    assert rec["provenance"]["source"] == "claude-code-transcript"


def test_trace_multi_invocation_session(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--skill",
            "argumentative-flow",
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    # argumentative-flow appears in both the multi-session and the thinking-session
    assert len(records) == 2


def test_trace_records_thinking_used_but_no_text(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--project",
            "-tmp-project-b",
            "--tier",
            "output-text",
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    # Find the record from the thinking session
    thinking_records = [r for r in records if r["model"].get("thinking_used")]
    assert len(thinking_records) >= 1
    for rec in thinking_records:
        # Thinking text is never captured from transcripts
        assert rec["model"]["thinking_text_captured"] is False
        # Even at output-text tier, thinking text must not leak in as output text
        text = rec.get("skill_output", {}).get("text", "")
        assert "thinking" not in text.lower() or "argumentative" in text.lower()


def test_trace_malformed_lines_skipped(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    # The malformed-line transcript still contributes its single invocation
    sessions = {r["provenance"].get("session_id") for r in records}
    assert "00000000-1111-2222-3333-eeeeeeeeeeee" in sessions


def test_trace_default_tier_excludes_text(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    assert records, "expected records to be emitted"
    for rec in records:
        assert rec["consent_tier"] == "structured-only"
        assert "manuscript_chunk" not in rec
        skill_output = rec.get("skill_output", {})
        assert "text" not in skill_output


def test_trace_output_text_tier_includes_text(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--tier",
            "output-text",
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    with_text = [r for r in records if r.get("skill_output", {}).get("text")]
    assert with_text, "expected at least one record with skill_output.text at output-text tier"
    for rec in records:
        assert rec["consent_tier"] == "output-text"
        assert "manuscript_chunk" not in rec


def test_trace_emits_records_that_match_schema(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    schema = cli._load_trace_schema()
    from jsonschema import Draft202012Validator

    validator = Draft202012Validator(schema)
    for rec in records:
        errors = list(validator.iter_errors(rec))
        assert not errors, f"record failed schema: {errors}"


def test_trace_json_format(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--format",
            "json",
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    parsed = json.loads(result.output)
    assert isinstance(parsed, list)
    assert all(isinstance(r, dict) for r in parsed)


def test_trace_skill_filter(runner: CliRunner) -> None:
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--skill",
            "citation-audit",
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    assert records, "expected at least one citation-audit record"
    assert all(r["skill"]["name"] == "citation-audit" for r in records)


def test_trace_project_filter_decoded_path(runner: CliRunner) -> None:
    # The decoded directory name should match the --project value too.
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--project",
            "/tmp/project/a",
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    records = _trace_records_from_output(result.output)
    # All records should come from project-a sessions
    session_ids = {r["provenance"].get("session_id") for r in records}
    assert session_ids <= {
        "00000000-1111-2222-3333-aaaaaaaaaaaa",
        "00000000-1111-2222-3333-bbbbbbbbbbbb",
    }


def test_trace_missing_projects_dir_errors(runner: CliRunner, tmp_path: Path) -> None:
    missing = tmp_path / "does-not-exist"
    result = runner.invoke(cli.main, ["trace", "--projects-dir", str(missing)])
    assert result.exit_code != 0
    assert "not found" in _combined_output(result).lower()


def test_trace_writes_to_output_file(runner: CliRunner, tmp_path: Path) -> None:
    out = tmp_path / "traces.jsonl"
    result = runner.invoke(
        cli.main,
        [
            "trace",
            "--projects-dir",
            str(TRANSCRIPTS_DIR),
            "--output",
            str(out),
        ],
    )
    assert result.exit_code == 0, _combined_output(result)
    assert out.exists()
    lines = [line for line in out.read_text().splitlines() if line.strip()]
    assert lines, "expected at least one record written"
    for line in lines:
        rec = json.loads(line)
        assert "skill" in rec


def test_trace_parse_since_iso_date() -> None:
    parsed = cli._parse_since("2026-05-17")
    assert parsed.year == 2026 and parsed.month == 5 and parsed.day == 17


def test_trace_parse_since_iso_datetime() -> None:
    parsed = cli._parse_since("2026-05-17T14:30:00Z")
    assert parsed.year == 2026 and parsed.hour == 14


def test_trace_parse_since_invalid_raises() -> None:
    with pytest.raises(click.BadParameter):
        cli._parse_since("not-a-date")


def test_decode_project_dir_name_round_trip() -> None:
    assert (
        cli._decode_project_dir_name("-Users-davsean-Documents-git-scriptorium")
        == "/Users/davsean/Documents/git/scriptorium"
    )
    # No leading hyphen → returned as-is
    assert cli._decode_project_dir_name("plain") == "plain"


def test_detect_invocation_user_slash() -> None:
    msg = {
        "role": "user",
        "content": [
            {"type": "text", "text": "<command-name>/scriptorium:citation-audit</command-name>"}
        ],
    }
    result = cli._detect_invocation(msg)
    assert result == ("citation-audit", "user-slash")


def test_detect_invocation_string_content() -> None:
    # Some transcript variants use string content instead of a list
    msg = {
        "role": "user",
        "content": "<command-name>/scriptorium:reviewer-simulation</command-name>",
    }
    result = cli._detect_invocation(msg)
    assert result == ("reviewer-simulation", "user-slash")


def test_detect_invocation_assistant_tool_use() -> None:
    msg = {
        "role": "assistant",
        "content": [
            {
                "type": "tool_use",
                "name": "Skill",
                "input": {"skill": "scriptorium:argumentative-flow"},
            }
        ],
    }
    result = cli._detect_invocation(msg)
    assert result == ("argumentative-flow", "assistant-tool")


def test_detect_invocation_ignores_non_scriptorium_skill() -> None:
    msg = {
        "role": "assistant",
        "content": [{"type": "tool_use", "name": "Skill", "input": {"skill": "other-plugin:foo"}}],
    }
    assert cli._detect_invocation(msg) is None


def test_detect_invocation_returns_none_for_plain_text() -> None:
    msg = {"role": "user", "content": [{"type": "text", "text": "hi there"}]}
    assert cli._detect_invocation(msg) is None


def test_load_trace_schema_errors_when_unbundled(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cli, "_bundled_dir", lambda pkg, repo: None)
    with pytest.raises(click.ClickException) as exc_info:
        cli._load_trace_schema()
    assert "Trace schema" in str(exc_info.value.message)
