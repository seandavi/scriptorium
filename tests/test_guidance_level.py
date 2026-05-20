"""Tests for the meta.guidance_level convention.

Covers three things:

1. The schema accepts the three enum values and rejects others.
2. The starter template and the example template both validate.
3. Every skill that elicits author input grounds in the guidance-level
   convention note, so its description of how to adapt cannot drift
   from the canonical convention.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_FILE = REPO_ROOT / "schemas" / "manuscript-state.schema.json"
CONVENTION_NOTE = REPO_ROOT / "knowledge" / "conventions" / "guidance-level.md"
SKILLS_DIR = REPO_ROOT / "skills"

# Skills whose SKILL.md must reference the guidance-level convention.
# Pure CLI commands (validate, prompt-pack, list, trace) don't have a
# conversation to adapt; they are intentionally excluded.
SKILLS_THAT_ADAPT = (
    "init",
    "citation-audit",
    "reviewer-simulation",
    "argumentative-flow",
    "explain",
)


@pytest.fixture(scope="module")
def schema() -> dict:
    return json.loads(SCHEMA_FILE.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def validator(schema: dict) -> Draft202012Validator:
    return Draft202012Validator(schema)


def test_schema_declares_meta_guidance_level(schema: dict) -> None:
    meta = schema["properties"].get("meta")
    assert meta is not None, "schema is missing top-level `meta` property"
    guidance = meta["properties"].get("guidance_level")
    assert guidance is not None, "meta.guidance_level not declared"
    assert guidance["enum"] == ["terse", "standard", "full"]
    assert guidance["default"] == "standard"


@pytest.mark.parametrize("level", ["terse", "standard", "full"])
def test_schema_accepts_valid_guidance_levels(validator: Draft202012Validator, level: str) -> None:
    doc = {
        "meta": {"guidance_level": level},
        "project": {"title": "x", "target_type": "manuscript"},
        "document_phase": {"current": "draft"},
    }
    errors = list(validator.iter_errors(doc))
    assert not errors, f"valid level {level!r} was rejected: {[e.message for e in errors]}"


def test_schema_rejects_invalid_guidance_level(validator: Draft202012Validator) -> None:
    doc = {
        "meta": {"guidance_level": "expert"},
        "project": {"title": "x", "target_type": "manuscript"},
        "document_phase": {"current": "draft"},
    }
    errors = list(validator.iter_errors(doc))
    assert errors, "invalid guidance level 'expert' was accepted"


def test_schema_meta_disallows_unknown_properties(validator: Draft202012Validator) -> None:
    doc = {
        "meta": {"guidance_level": "full", "extra_field": "nope"},
        "project": {"title": "x", "target_type": "manuscript"},
        "document_phase": {"current": "draft"},
    }
    errors = list(validator.iter_errors(doc))
    assert errors, "meta block should reject additionalProperties"


def test_convention_note_exists() -> None:
    assert CONVENTION_NOTE.is_file(), f"missing {CONVENTION_NOTE}"
    text = CONVENTION_NOTE.read_text(encoding="utf-8")
    # The three levels and the check-in protocol are the load-bearing
    # parts of the convention; their absence means the file has been
    # gutted by a regression.
    assert "### `terse`" in text
    assert "### `standard`" in text
    assert "### `full`" in text
    assert "check-in protocol" in text.lower()


@pytest.mark.parametrize("skill_name", SKILLS_THAT_ADAPT)
def test_skill_grounds_in_guidance_convention(skill_name: str) -> None:
    skill_md = SKILLS_DIR / skill_name / "SKILL.md"
    assert skill_md.is_file(), f"missing {skill_md}"
    text = skill_md.read_text(encoding="utf-8")
    # Frontmatter sits between the first two `---` lines.
    assert text.startswith("---")
    end = text.find("\n---", 3)
    frontmatter = text[3:end]
    parsed = yaml.safe_load(frontmatter)
    grounding = parsed.get("grounding", [])
    assert "knowledge/conventions/guidance-level.md" in grounding, (
        f"skill {skill_name!r} does not ground in the guidance-level convention"
    )


def test_example_template_includes_meta_block() -> None:
    """The example template doubles as documentation — it should show the
    meta block so a reader copying it learns the field exists."""
    example = REPO_ROOT / "templates" / "MANUSCRIPT_STATE.example.yaml"
    data = yaml.safe_load(example.read_text(encoding="utf-8"))
    assert "meta" in data
    assert data["meta"]["guidance_level"] in {"terse", "standard", "full"}
