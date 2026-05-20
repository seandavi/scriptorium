"""Regression guards for `argumentative-flow`'s grounding contract.

The skill's preservation contract treats hedging as a fourth preserved
category (alongside citations, statistics, and declared terminology).
That promotion is grounded in the Swales / Hyland synthesis under
`knowledge/scientific-writing/esl-writers-swales-hyland.md`. If a future
refactor drops the ESL grounding reference from the skill, or quietly
removes the active hedging check from the operational protocol, those
checks will catch it — see issue #75.
"""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = REPO_ROOT / "skills" / "argumentative-flow" / "SKILL.md"
PROMPT_MD = REPO_ROOT / "skills" / "argumentative-flow" / "prompt.md"
MANIFEST = REPO_ROOT / "skills" / "argumentative-flow" / "manifest.yaml"
ESL_NOTE = "knowledge/scientific-writing/esl-writers-swales-hyland.md"


def _frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---"), f"{path} missing YAML frontmatter"
    end = text.find("\n---", 3)
    assert end > 0, f"{path} frontmatter not terminated"
    return yaml.safe_load(text[3:end])


def test_skill_md_grounds_in_esl_note() -> None:
    """SKILL.md must reference the Swales / Hyland note in `grounding:`."""
    grounding = _frontmatter(SKILL_MD).get("grounding", [])
    assert ESL_NOTE in grounding, (
        f"argumentative-flow SKILL.md grounding must include {ESL_NOTE!r}; "
        f"the active ESL-aware hedging check depends on it (issue #75)."
    )


def test_manifest_grounds_in_esl_note() -> None:
    """manifest.yaml must mirror SKILL.md's grounding."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    grounding = data.get("grounding", [])
    assert ESL_NOTE in grounding, (
        f"argumentative-flow manifest.yaml grounding must include {ESL_NOTE!r}."
    )


def test_manifest_declares_hedging_preservation_constraint() -> None:
    """Hedging is a fourth preserved category alongside citations,
    statistics, and declared terminology."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    constraints = data.get("preservation_constraints", [])
    assert "hedging" in constraints, (
        "manifest.yaml must declare `hedging` in preservation_constraints "
        "so the contract is machine-discoverable (issue #75)."
    )


def test_skill_md_inventories_hedging_in_protocol() -> None:
    """The operational protocol's inventory step must include hedging,
    so the active check is part of the documented procedure, not just
    aspirational prose in the grounding section."""
    text = SKILL_MD.read_text(encoding="utf-8")
    # The inventory step lives under "Inventory before transforming."
    # If a future refactor moves the heading, update this anchor too.
    inventory_anchor = "Inventory before transforming"
    assert inventory_anchor in text, (
        f"SKILL.md missing inventory step anchor {inventory_anchor!r}"
    )
    # Cheap content check: the hedging vocabulary must appear in the
    # inventory step. Using "epistemic" as the anchor — it is specific
    # enough that an accidental removal will surface here.
    assert "epistemic" in text.lower(), (
        "SKILL.md inventory step no longer enumerates hedging markers "
        "(epistemic modals / adverbs). The active ESL check has been "
        "weakened — see issue #75."
    )


def test_prompt_md_mirrors_hedging_inventory() -> None:
    """prompt.md (platform-neutral) must mirror the hedging inventory
    step so users of non-Claude agents get the same contract."""
    text = PROMPT_MD.read_text(encoding="utf-8")
    assert "epistemic" in text.lower(), (
        "prompt.md no longer enumerates hedging markers in the inventory "
        "step; platform-neutral users would lose the ESL-aware check."
    )


def test_skill_md_preservation_report_breaks_out_hedging() -> None:
    """The preservation report output format must explicitly enumerate
    hedging patterns retained vs. modified, with rationale for any
    modification."""
    text = SKILL_MD.read_text(encoding="utf-8")
    assert "Hedging patterns retained vs. modified" in text, (
        "SKILL.md preservation report no longer includes the hedging "
        "breakdown sub-section; the per-hedge audit is gone."
    )
