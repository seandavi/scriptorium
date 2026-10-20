"""Tests for the author-authority convention's ``meta.overrides`` block.

See ``knowledge/conventions/author-authority.md``. The schema checks the
shape of each override entry; ``scriptorium validate`` then checks each
entry against the guards the bundled skills declare.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from click.testing import CliRunner
from jsonschema import Draft202012Validator

from scriptorium import cli

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_FILE = REPO_ROOT / "schemas" / "manuscript-state.schema.json"


@pytest.fixture(scope="module")
def validator() -> Draft202012Validator:
    return Draft202012Validator(json.loads(SCHEMA_FILE.read_text(encoding="utf-8")))


def _state(overrides: Any) -> dict[str, Any]:
    return {
        "meta": {"overrides": overrides},
        "project": {"title": "x", "target_type": "grant"},
        "document_phase": {"current": "draft"},
    }


@pytest.mark.parametrize(
    "overrides",
    [
        [],
        [{"guard": "nih-application-prose", "skills": ["specific-aims"]}],
        [{"guard": "blank-slate-drafting", "skills": ["*"], "note": "Invited, see notes."}],
    ],
)
def test_schema_accepts_valid_overrides(validator: Draft202012Validator, overrides: Any) -> None:
    errors = list(validator.iter_errors(_state(overrides)))
    assert not errors, [e.message for e in errors]


@pytest.mark.parametrize(
    "overrides",
    [
        [{"skills": ["specific-aims"]}],
        [{"guard": "nih-application-prose"}],
        [{"guard": "nih-application-prose", "skills": []}],
        [{"guard": "nih-application-prose", "skills": "specific-aims"}],
        [{"guard": "NIH_Application_Prose", "skills": ["specific-aims"]}],
        [{"guard": "nih-application-prose", "skills": ["Specific Aims"]}],
        [{"guard": "nih-application-prose", "skills": ["specific-aims"], "extra": True}],
        {"guard": "nih-application-prose", "skills": ["specific-aims"]},
    ],
)
def test_schema_rejects_invalid_overrides(validator: Draft202012Validator, overrides: Any) -> None:
    assert list(validator.iter_errors(_state(overrides)))


def test_starter_template_shows_commented_overrides() -> None:
    text = (REPO_ROOT / "templates" / "MANUSCRIPT_STATE.yaml").read_text(encoding="utf-8")
    assert "#   overrides:" in text
    assert "author-authority.md" in text


def test_example_template_shows_commented_overrides() -> None:
    path = REPO_ROOT / "templates" / "MANUSCRIPT_STATE.example.yaml"
    text = path.read_text(encoding="utf-8")
    assert "# overrides:" in text
    # Commented out: the entry is illustrative, and a live entry for a
    # guard no bundled skill declares fails `scriptorium validate`.
    assert "overrides" not in yaml.safe_load(text)["meta"]


SPECIFIC_AIMS_GUARDS = """\
guards:
  - id: nih-application-prose
    kind: policy
    summary: NIH may not treat AI-developed sections as the applicant's own.
    source: NIH NOT-OD-25-132
    default: ask
  - id: blank-slate-drafting
    kind: scope
    summary: Nothing declared to ground the draft against.
    source: knowledge/conventions/declared-work-scope.md
    default: refuse
  - id: no-invented-citations
    kind: accuracy
    summary: Citations must exist.
    default: refuse
"""

GAP_FINDER_GUARDS = """\
guards:
  - id: blank-slate-drafting
    kind: scope
    summary: Nothing declared to ground the draft against.
    source: knowledge/conventions/declared-work-scope.md
    default: refuse
"""


@pytest.fixture
def bundled_skills(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Point ``_iter_skills`` at two skills with guards; leave schemas real."""
    skills_root = tmp_path / "skills"
    for name, manifest in (
        ("specific-aims", SPECIFIC_AIMS_GUARDS),
        ("gap-finder", GAP_FINDER_GUARDS),
        ("tour", "name: tour\n"),
    ):
        (skills_root / name).mkdir(parents=True)
        (skills_root / name / "manifest.yaml").write_text(manifest, encoding="utf-8")
    real_bundled_dir = cli._bundled_dir

    def _fake_bundled_dir(pkg: str, repo: str) -> Any:
        return skills_root if repo == "skills" else real_bundled_dir(pkg, repo)

    monkeypatch.setattr(cli, "_bundled_dir", _fake_bundled_dir)


def _validate(tmp_path: Path, overrides: list[dict[str, Any]]) -> tuple[int, str]:
    state = tmp_path / "MANUSCRIPT_STATE.yaml"
    state.write_text(yaml.safe_dump(_state(overrides)), encoding="utf-8")
    result = CliRunner().invoke(cli.main, ["validate", str(state)])
    return result.exit_code, (result.output or "") + (getattr(result, "stderr", None) or "")


@pytest.mark.usefixtures("bundled_skills")
@pytest.mark.parametrize(
    "overrides",
    [
        [{"guard": "nih-application-prose", "skills": ["specific-aims"]}],
        [{"guard": "blank-slate-drafting", "skills": ["specific-aims", "gap-finder"]}],
        [{"guard": "blank-slate-drafting", "skills": ["*"], "note": "Invited."}],
    ],
)
def test_validate_accepts_overrides_of_declared_guards(
    tmp_path: Path, overrides: list[dict[str, Any]]
) -> None:
    exit_code, output = _validate(tmp_path, overrides)
    assert exit_code == 0, output
    assert "valid" in output


@pytest.mark.usefixtures("bundled_skills")
@pytest.mark.parametrize("skills", [["specific-aims"], ["*"]])
def test_validate_rejects_unknown_guard(tmp_path: Path, skills: list[str]) -> None:
    exit_code, output = _validate(tmp_path, [{"guard": "no-such-guard", "skills": skills}])
    assert exit_code != 0
    assert "meta/overrides/0: unknown guard 'no-such-guard'" in output


@pytest.mark.usefixtures("bundled_skills")
def test_validate_rejects_accuracy_guard_override(tmp_path: Path) -> None:
    exit_code, output = _validate(
        tmp_path, [{"guard": "no-invented-citations", "skills": ["specific-aims"]}]
    )
    assert exit_code != 0
    assert "accuracy guard and cannot be overridden" in output


@pytest.mark.usefixtures("bundled_skills")
@pytest.mark.parametrize("skill_name", ["gap-finder", "tour", "not-a-skill"])
def test_validate_rejects_skill_that_does_not_declare_guard(
    tmp_path: Path, skill_name: str
) -> None:
    exit_code, output = _validate(
        tmp_path, [{"guard": "nih-application-prose", "skills": ["specific-aims", skill_name]}]
    )
    assert exit_code != 0
    assert (
        f"skill {skill_name!r} does not declare guard 'nih-application-prose' "
        "(declared by: specific-aims)"
    ) in output


@pytest.mark.usefixtures("bundled_skills")
def test_validate_reports_every_override_error(tmp_path: Path) -> None:
    exit_code, output = _validate(
        tmp_path,
        [
            {"guard": "nih-application-prose", "skills": ["specific-aims"]},
            {"guard": "no-such-guard", "skills": ["*"]},
            {"guard": "no-invented-citations", "skills": ["*"]},
        ],
    )
    assert exit_code != 0
    assert "meta/overrides/1:" in output
    assert "meta/overrides/2:" in output
    assert "meta/overrides/0:" not in output
    assert "(2 error(s))" in output


def test_validate_skips_cross_check_without_overrides(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def _fail() -> list[dict[str, Any]]:
        raise AssertionError("_iter_skills should not run without overrides")

    monkeypatch.setattr(cli, "_iter_skills", _fail)
    exit_code, output = _validate(tmp_path, [])
    assert exit_code == 0, output
