"""Tests for the author-authority convention's ``meta.overrides`` block.

See ``knowledge/conventions/author-authority.md``. The schema checks the
shape of each override entry.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from jsonschema import Draft202012Validator

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
