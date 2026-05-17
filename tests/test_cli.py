"""Tests for the ``scriptorium`` CLI."""

from __future__ import annotations

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


def test_list_runs(runner: CliRunner) -> None:
    result = runner.invoke(cli.main, ["list"])
    assert result.exit_code == 0


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
