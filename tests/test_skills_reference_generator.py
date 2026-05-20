"""Tests for the manifest-driven ``reference/skills.md`` generator.

The generator lives in ``docs/scripts/preprocess.py`` (it runs as part
of the docs preprocess pass, not as a CLI subcommand). These tests
import it dynamically — the script is not installed as a package — and
exercise the rendering surface end-to-end so the docs page cannot
silently drift from the manifests.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_SRC = REPO_ROOT / "skills"
PREPROCESS_PATH = REPO_ROOT / "docs" / "scripts" / "preprocess.py"


@pytest.fixture(scope="module")
def preprocess_module() -> object:
    """Load ``docs/scripts/preprocess.py`` as a module for testing.

    The script has inline ``# /// script`` metadata so it can run as
    ``./scripts/preprocess.py`` via uv. Importing it directly here
    requires ``pyyaml`` already available (it is, via the
    ``agentic-scriptorium`` runtime deps in ``pyproject.toml``).
    """
    spec = importlib.util.spec_from_file_location("_preprocess_under_test", PREPROCESS_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _shipped_skill_names() -> list[str]:
    """Every directory under ``skills/`` with a ``manifest.yaml``."""
    return sorted(
        d.name for d in SKILLS_SRC.iterdir() if d.is_dir() and (d / "manifest.yaml").is_file()
    )


def test_load_manifests_finds_every_shipped_skill(preprocess_module) -> None:  # type: ignore[no-untyped-def]
    manifests = preprocess_module._load_manifests()
    loaded_names = sorted(m["name"] for m in manifests)
    assert loaded_names == _shipped_skill_names()


def test_every_manifest_declares_lifecycle_phases(preprocess_module) -> None:  # type: ignore[no-untyped-def]
    """The generator's lifecycle column requires ``lifecycle_phases``.

    The check lives here (not in the schema) so adding a new skill
    without the field surfaces as a test failure rather than as an
    empty cell in the rendered page.
    """
    manifests = preprocess_module._load_manifests()
    missing = [m["name"] for m in manifests if not m.get("lifecycle_phases")]
    assert not missing, f"Skills missing lifecycle_phases: {missing}"


def test_lifecycle_phases_are_valid(preprocess_module) -> None:  # type: ignore[no-untyped-def]
    """Each declared phase must be one of the schema's enum values."""
    valid = {
        "outline",
        "draft",
        "review",
        "revision",
        "submission",
        "post-submission",
        "accepted",
    }
    manifests = preprocess_module._load_manifests()
    for m in manifests:
        for phase in m.get("lifecycle_phases") or []:
            assert phase in valid, f"Skill {m['name']} declares unknown phase {phase!r}"


def test_generated_page_includes_every_skill(preprocess_module) -> None:  # type: ignore[no-untyped-def]
    """The rendered markdown must reference every shipped skill by name."""
    manifests = preprocess_module._load_manifests()
    page = preprocess_module._generate_skills_page(manifests)
    for name in _shipped_skill_names():
        # Either rendered as `name` (table cell) or [`name`](url) (link).
        assert f"`{name}`" in page, f"Skill {name} missing from rendered page"


def test_generated_page_has_required_sections(preprocess_module) -> None:  # type: ignore[no-untyped-def]
    manifests = preprocess_module._load_manifests()
    page = preprocess_module._generate_skills_page(manifests)
    for section in (
        "## Categorisation axes",
        "## All shipped skills",
        "## Per-category detail",
        "## Lifecycle fit, summarised",
        "## Author-side only",
        "## Source of truth",
    ):
        assert section in page, f"Generated page missing section: {section}"


def test_generated_page_is_deterministic(preprocess_module) -> None:  # type: ignore[no-untyped-def]
    """Two consecutive renders against unchanged manifests are identical."""
    manifests = preprocess_module._load_manifests()
    first = preprocess_module._generate_skills_page(manifests)
    second = preprocess_module._generate_skills_page(manifests)
    assert first == second


def test_generated_page_has_frontmatter_and_do_not_edit_marker(  # type: ignore[no-untyped-def]
    preprocess_module,
) -> None:
    manifests = preprocess_module._load_manifests()
    page = preprocess_module._generate_skills_page(manifests)
    assert page.startswith("---\n"), "Page must lead with YAML frontmatter"
    assert "title: Skills" in page.splitlines()[1:6]  # frontmatter top
    assert "GENERATED FILE" in page, "Page must include a do-not-edit marker"


def test_modifies_column_renders_expected_values(preprocess_module) -> None:  # type: ignore[no-untyped-def]
    """Spot-check the modifies-column heuristic on known skills."""
    manifests = {m["name"]: m for m in preprocess_module._load_manifests()}
    render = preprocess_module._render_modifies

    # transformation/normalization always suggest
    assert render(manifests["argumentative-flow"]) == "suggests"
    assert render(manifests["compression"]) == "suggests"
    assert render(manifests["terminology-normalization"]) == "suggests"
    # init is utility writing only the state file
    assert render(manifests["init"]) == "state file only"
    # venue-fit is critique-category but writes the state file opt-in
    assert render(manifests["venue-fit"]) == "state file only (opt-in)"
    # plain critique skills modify nothing
    assert render(manifests["citation-audit"]) == "no"
    assert render(manifests["gap-finder"]) == "no"


def test_author_side_only_renders_for_positioned_skills(  # type: ignore[no-untyped-def]
    preprocess_module,
) -> None:
    manifests = {m["name"]: m for m in preprocess_module._load_manifests()}
    render = preprocess_module._render_author_side
    assert render(manifests["reviewer-simulation"]) == "**yes**"
    assert render(manifests["desk-rejection-risk"]) == "**yes**"
    assert render(manifests["citation-audit"]) == "no"
    assert render(manifests["init"]) == "no"


def test_process_skills_reference_writes_file(  # type: ignore[no-untyped-def]
    preprocess_module, tmp_path, monkeypatch
) -> None:
    """``process_skills_reference`` must write the file and return the count."""
    out = tmp_path / "reference" / "skills.md"
    monkeypatch.setattr(preprocess_module, "SKILLS_OUT", out)
    count = preprocess_module.process_skills_reference()
    assert count == len(_shipped_skill_names())
    assert out.is_file()
    text = out.read_text(encoding="utf-8")
    assert "## All shipped skills" in text
