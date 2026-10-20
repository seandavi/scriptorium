"""Tests for the ``guards:`` registry in ``skills/*/manifest.yaml``.

See ``knowledge/conventions/author-authority.md``. A skill may declare no
guards. Each declared guard needs the required fields and valid enum
values, a policy guard must name its source, and scope and accuracy
guards must default to refuse. An id is unique within a
manifest. Several skills may share an id only if they define it
identically.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

GUARD_FIELDS = ("id", "kind", "summary", "source", "default")
REQUIRED_FIELDS = ("id", "kind", "summary", "default")
GUARD_KINDS = ("policy", "scope", "accuracy")
GUARD_DEFAULTS = ("ask", "refuse")
GUARD_ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def guard_problems(manifests: dict[str, Any]) -> list[str]:
    """Return one message per problem in the ``guards:`` of each manifest."""
    problems: list[str] = []
    definitions: dict[str, tuple[str, dict[str, Any]]] = {}
    for skill, manifest in manifests.items():
        guards = manifest.get("guards", [])
        if not isinstance(guards, list):
            problems.append(f"{skill}: guards must be a list")
            continue
        seen: set[str] = set()
        for index, guard in enumerate(guards):
            where = f"{skill}: guards[{index}]"
            if not isinstance(guard, dict):
                problems.append(f"{where}: must be a mapping")
                continue
            problems += [f"{where}: missing {f!r}" for f in REQUIRED_FIELDS if f not in guard]
            problems += [f"{where}: unknown field {f!r}" for f in guard if f not in GUARD_FIELDS]
            for field in ("id", "summary", "source"):
                value = guard.get(field)
                if field in guard and (not isinstance(value, str) or not value.strip()):
                    problems.append(f"{where}: {field} must be a non-empty string")
            guard_id = guard.get("id")
            if isinstance(guard_id, str):
                where = f"{skill}: guard {guard_id!r}"
                if not GUARD_ID_RE.match(guard_id):
                    problems.append(f"{where}: id must be kebab-case")
                if guard_id in seen:
                    problems.append(f"{where}: declared twice in this manifest")
                seen.add(guard_id)
            if isinstance(guard.get("summary"), str) and "\n" in guard["summary"].strip():
                problems.append(f"{where}: summary must be one line")
            kind = guard.get("kind")
            if "kind" in guard and kind not in GUARD_KINDS:
                problems.append(f"{where}: kind {kind!r} not in {GUARD_KINDS}")
            default = guard.get("default")
            if "default" in guard and default not in GUARD_DEFAULTS:
                problems.append(f"{where}: default {default!r} not in {GUARD_DEFAULTS}")
            if kind == "policy" and "source" not in guard:
                problems.append(f"{where}: policy guards must name a source")
            if kind in ("scope", "accuracy") and default != "refuse":
                problems.append(f"{where}: {kind} guards must default to refuse")
            if isinstance(guard_id, str):
                first = definitions.setdefault(guard_id, (skill, guard))
                if first[0] != skill and first[1] != guard:
                    problems.append(f"{where}: defined differently in {first[0]}")
    return problems


def _load_manifests() -> dict[str, Any]:
    manifests: dict[str, Any] = {}
    for path in sorted(SKILLS_DIR.glob("*/manifest.yaml")):
        parsed = yaml.safe_load(path.read_text(encoding="utf-8"))
        manifests[path.parent.name] = parsed if isinstance(parsed, dict) else {}
    return manifests


def test_bundled_manifest_guards_are_valid() -> None:
    manifests = _load_manifests()
    assert manifests, f"no manifests found under {SKILLS_DIR}"
    assert guard_problems(manifests) == []


POLICY_GUARD = {
    "id": "nih-application-prose",
    "kind": "policy",
    "summary": "NIH may not treat AI-developed sections as the applicant's own.",
    "source": "NIH NOT-OD-25-132",
    "default": "ask",
}


def test_guard_problems_accepts_valid_and_absent_guards() -> None:
    shared_scope = {
        "id": "blank-slate-drafting",
        "kind": "scope",
        "summary": "Nothing declared to ground against.",
        "source": "knowledge/conventions/declared-work-scope.md",
        "default": "refuse",
    }
    accuracy = {
        "id": "no-invented-citations",
        "kind": "accuracy",
        "summary": "Citations must exist.",
        "default": "refuse",
    }
    manifests = {
        "specific-aims": {"guards": [POLICY_GUARD, shared_scope, accuracy]},
        "gap-finder": {"guards": [dict(shared_scope)]},
        "tour": {},
    }
    assert guard_problems(manifests) == []


@pytest.mark.parametrize(
    ("changes", "expected"),
    [
        ({"id": None}, "missing 'id'"),
        ({"summary": None}, "missing 'summary'"),
        ({"default": None}, "missing 'default'"),
        ({"kind": None}, "missing 'kind'"),
        ({"overridable": True}, "unknown field 'overridable'"),
        ({"id": "NIH_prose"}, "id must be kebab-case"),
        ({"kind": "legal"}, "kind 'legal' not in"),
        ({"default": "warn"}, "default 'warn' not in"),
        ({"source": None}, "policy guards must name a source"),
        ({"source": " "}, "source must be a non-empty string"),
        ({"summary": "Line one.\nLine two."}, "summary must be one line"),
        ({"kind": "scope", "default": "ask"}, "scope guards must default to refuse"),
        ({"kind": "accuracy", "default": "ask"}, "accuracy guards must default to refuse"),
    ],
)
def test_guard_problems_flags_invalid_entry(changes: dict[str, Any], expected: str) -> None:
    guard = {**POLICY_GUARD, **changes}
    guard = {k: v for k, v in guard.items() if v is not None}
    problems = guard_problems({"specific-aims": {"guards": [guard]}})
    assert any(expected in p for p in problems), problems


def test_guard_problems_flags_duplicate_id_in_one_manifest() -> None:
    problems = guard_problems({"specific-aims": {"guards": [POLICY_GUARD, POLICY_GUARD]}})
    assert any("declared twice in this manifest" in p for p in problems), problems


def test_guard_problems_flags_shared_id_with_different_definition() -> None:
    changed = {**POLICY_GUARD, "default": "refuse"}
    problems = guard_problems(
        {
            "specific-aims": {"guards": [POLICY_GUARD]},
            "aims-significance-coherence": {"guards": [changed]},
        }
    )
    assert problems == [
        "aims-significance-coherence: guard 'nih-application-prose': "
        "defined differently in specific-aims"
    ]


@pytest.mark.parametrize("guards", ["nih-application-prose", {"id": "x"}, ["not-a-mapping"]])
def test_guard_problems_flags_malformed_guards(guards: Any) -> None:
    assert guard_problems({"specific-aims": {"guards": guards}})
