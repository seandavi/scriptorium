"""Regression guards for `compression`'s grounding and preservation contract.

`compression` is a transformation skill that inherits the same
preservation discipline as `argumentative-flow` and adds two
specialisations:

1. Every declared `core_claim` in `MANUSCRIPT_STATE.yaml` must be
   preserved across proposed edits.
2. Distinct claims may not be merged into one (granularity loss
   looks like compression but reads as a stealth scope change).

The forbidden-transforms list draws explicitly on the AI-writing
failure-modes literature (Kobak 2024 et al.) — the things compression
must NOT do are exactly the AI-writing tells that surface when
unconstrained shorten-this prompts are run.

If a future refactor drops the AI-writing-failure-modes grounding
reference, the core-claims preservation constraint, or the
suggest-don't-apply posture, those checks will catch it.
"""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "compression"
SKILL_MD = SKILL_DIR / "SKILL.md"
PROMPT_MD = SKILL_DIR / "prompt.md"
MANIFEST = SKILL_DIR / "manifest.yaml"
README = SKILL_DIR / "README.md"

AI_WRITING_NOTE = "knowledge/prior-art/ai-writing-failure-modes.md"
SEMANTIC_PRESERVATION_NOTE = "knowledge/editing/semantic-preservation.md"
NARRATIVE_FRAMEWORKS_NOTE = "knowledge/scientific-writing/narrative-frameworks.md"
COPYEDITING_NOTE = "knowledge/editing/copyediting-vs-developmental.md"


def _frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---"), f"{path} missing YAML frontmatter"
    end = text.find("\n---", 3)
    assert end > 0, f"{path} frontmatter not terminated"
    return yaml.safe_load(text[3:end])


def test_skill_files_exist() -> None:
    """The four required files for a scriptorium skill are present."""
    for fname in ("SKILL.md", "prompt.md", "manifest.yaml", "README.md"):
        assert (SKILL_DIR / fname).is_file(), f"missing {fname}"


def test_skill_md_grounds_in_narrative_frameworks() -> None:
    """The roadmap names narrative-frameworks as the primary grounding
    for compression (page-limit driven, preserves citations, statistics,
    and core claims). SKILL.md must reference it explicitly."""
    grounding = _frontmatter(SKILL_MD).get("grounding", [])
    assert NARRATIVE_FRAMEWORKS_NOTE in grounding, (
        f"compression SKILL.md grounding must include {NARRATIVE_FRAMEWORKS_NOTE!r}; "
        f"it is the primary grounding the v0.3 roadmap names for this skill."
    )


def test_skill_md_grounds_in_semantic_preservation() -> None:
    """Every transformation skill that promises preservation must
    ground in the semantic-preservation note — the BERTScore antonymy
    discussion is the reason embedding similarity cannot be the safety
    check."""
    grounding = _frontmatter(SKILL_MD).get("grounding", [])
    assert SEMANTIC_PRESERVATION_NOTE in grounding


def test_skill_md_grounds_in_copyediting_distinction() -> None:
    """compression sits at line editing, one level below
    argumentative-flow's developmental scope. The editing-taxonomy
    note (Mossop / Einsohn / CSE) is what grounds that placement."""
    grounding = _frontmatter(SKILL_MD).get("grounding", [])
    assert COPYEDITING_NOTE in grounding


def test_skill_md_grounds_in_ai_writing_failure_modes() -> None:
    """The forbidden-transforms list (no em-dash overuse, no
    rule-of-three, no inflated symbolism, no elevated synonyms) draws
    directly from the AI-writing failure-modes literature. Dropping the
    grounding reference would silently disconnect the forbidden list
    from its evidence base."""
    grounding = _frontmatter(SKILL_MD).get("grounding", [])
    assert AI_WRITING_NOTE in grounding, (
        f"compression SKILL.md grounding must include {AI_WRITING_NOTE!r}; "
        f"the forbidden-transforms list depends on it."
    )


def test_manifest_mirrors_skill_grounding() -> None:
    """manifest.yaml must mirror the primary groundings listed in
    SKILL.md frontmatter so the contract is machine-discoverable."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    grounding = data.get("grounding", [])
    for note in (
        NARRATIVE_FRAMEWORKS_NOTE,
        SEMANTIC_PRESERVATION_NOTE,
        COPYEDITING_NOTE,
        AI_WRITING_NOTE,
    ):
        assert note in grounding, f"compression manifest.yaml grounding must include {note!r}"


def test_manifest_declares_transformation_category() -> None:
    """compression is a transformation skill — same category as
    argumentative-flow. The category drives invocation discipline and
    consumer expectations."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    assert data.get("category") == "transformation"


def test_manifest_declares_explicit_invocation() -> None:
    """Transformation skills must be explicit-invocation only — never
    auto-invoke, never run as a follow-up to another skill's output
    without the user re-asking. Surprise length reductions are exactly
    the failure mode the contract is designed to prevent."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    invocation = data.get("invocation", "")
    # accepted forms: "explicit", "explicit-only" (matches argumentative-flow).
    assert invocation.startswith("explicit"), (
        f"compression manifest must declare explicit-style invocation, got {invocation!r}"
    )


def test_manifest_modifies_is_empty() -> None:
    """compression suggests but does not apply. modifies: [] is the
    machine-readable form of the suggest-don't-apply posture."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    assert data.get("modifies") == [], (
        "compression manifest.yaml must declare `modifies: []` — the skill "
        "emits a report; the author applies edits."
    )


def test_manifest_declares_core_claims_preservation() -> None:
    """Beyond the citations / statistics / terminology / voice / hedging
    inherited from argumentative-flow, compression adds a fifth
    preservation surface: every declared core_claim. Re-scoping a
    declared claim under the guise of "shortening" is the stealth
    scope-change failure mode this constraint prevents."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    constraints = data.get("preservation_constraints", [])
    assert "core_claims" in constraints, (
        "manifest.yaml must declare `core_claims` in preservation_constraints "
        "so the contract is machine-discoverable."
    )


def test_manifest_declares_claim_granularity_preservation() -> None:
    """Two distinct claims may not be merged into one. Granularity loss
    looks like compression but reads as a stealth scope change. The
    manifest names this as a discrete constraint so a future refactor
    cannot drop it without surfacing the change."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    constraints = data.get("preservation_constraints", [])
    assert "claim_granularity" in constraints, (
        "manifest.yaml must declare `claim_granularity` in preservation_constraints"
    )


def test_manifest_declares_hedging_preservation() -> None:
    """Hedging preservation is inherited from argumentative-flow.
    Only hedging *stacks* are legitimate compression targets;
    removing the hedge itself is forbidden."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    constraints = data.get("preservation_constraints", [])
    assert "hedging" in constraints


def test_manifest_declares_length_target_input() -> None:
    """A target-less compression is an opinion about the author's prose,
    not a service. The manifest must declare length_target as a
    required input so the contract is machine-discoverable."""
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    inputs = data.get("inputs", [])
    names = [i.get("name") for i in inputs]
    assert "length_target" in names, (
        "manifest.yaml must declare a `length_target` input — compression "
        "without a target is an opinion, not a service."
    )
    target = next(i for i in inputs if i.get("name") == "length_target")
    assert target.get("required") is True, (
        "length_target must be declared required so the skill refuses to run without it."
    )


def test_skill_md_inventory_includes_core_claims() -> None:
    """The operational protocol's inventory step must explicitly extract
    declared core_claims so the preservation report can verify against
    them. If a future refactor moves the inventory step's content into a
    section that no longer enumerates core_claims, the active check has
    been weakened."""
    text = SKILL_MD.read_text(encoding="utf-8")
    inventory_anchor = "Inventory before proposing edits"
    assert inventory_anchor in text, f"SKILL.md missing inventory step anchor {inventory_anchor!r}"
    assert "core_claims" in text, (
        "SKILL.md inventory step no longer mentions core_claims; the "
        "core-claims preservation check has been disconnected from "
        "the operational protocol."
    )


def test_skill_md_inventory_includes_hedging_vocabulary() -> None:
    """Hedging preservation requires an explicit inventory step that
    enumerates the markers (epistemic modals / adverbs / approximators
    / attributive verbs / indirect attributions). 'epistemic' is the
    specific anchor — its removal signals the ESL-aware check has
    been gutted."""
    text = SKILL_MD.read_text(encoding="utf-8")
    assert "epistemic" in text.lower(), (
        "SKILL.md no longer enumerates hedging markers (epistemic modals "
        "/ adverbs). The ESL-aware preservation check has been weakened."
    )


def test_prompt_md_mirrors_skill_md_contracts() -> None:
    """The platform-neutral prompt must mirror the load-bearing
    contracts: core_claims preservation, hedging inventory,
    no-AI-writing-tells, suggest-don't-apply."""
    text = PROMPT_MD.read_text(encoding="utf-8")
    assert "core_claim" in text, (
        "prompt.md must mention core_claim preservation; platform-neutral "
        "users would lose the constraint."
    )
    assert "epistemic" in text.lower(), (
        "prompt.md no longer enumerates hedging markers; platform-neutral "
        "users would lose the ESL-aware check."
    )
    # Suggest-don't-apply posture must be present.
    lowered = text.lower()
    assert "suggest" in lowered or "not apply" in lowered or "does not apply" in lowered


def test_skill_md_forbids_ai_writing_tells() -> None:
    """The forbidden-transforms list must call out AI-writing tells
    explicitly — em-dashes, rule-of-three, inflated symbolism, or
    elevated synonyms. These are the exact patterns Kobak 2024 et al.
    documented as the lexical fingerprint of LLM-edited scientific
    prose. A compression pass that introduces them has imported the
    failure mode this skill exists to defend against."""
    text = SKILL_MD.read_text(encoding="utf-8").lower()
    # At least one of the specific AI-writing-tell anchors must appear.
    anchors = (
        "em-dash",
        "rule-of-three",
        "rule of three",
        "inflated symbolism",
        "elevated synonym",
    )
    assert any(a in text for a in anchors), (
        "SKILL.md no longer names AI-writing tells (em-dash overuse, "
        "rule-of-three, inflated symbolism, elevated synonyms) in the "
        "forbidden-transforms list."
    )


def test_skill_md_preservation_report_includes_core_claims() -> None:
    """The preservation report output format must explicitly account
    for declared core_claims, alongside citations / numbers / terminology
    / voice / hedging. Dropping this row would let a violation slip
    through with a clean-looking report."""
    text = SKILL_MD.read_text(encoding="utf-8").lower()
    assert "declared core claims" in text or "core_claims" in text.lower(), (
        "SKILL.md preservation report no longer includes a core-claims row."
    )


def test_skill_md_output_includes_edits_not_proposed() -> None:
    """The honesty surface for this skill is the 'Edits NOT proposed'
    section — passages where redundancy looked likely but compression
    would risk losing a load-bearing nuance. A compression pass that
    proposes every candidate has not done the load-bearing-vs-extraneous
    classification carefully."""
    text = SKILL_MD.read_text(encoding="utf-8")
    assert "Edits NOT proposed" in text, (
        "SKILL.md output format no longer includes the 'Edits NOT proposed' "
        "section; the honesty surface has been removed."
    )


def test_skill_md_requires_length_target() -> None:
    """compression refuses to run without a declared or supplied length
    target. SKILL.md must surface this refusal explicitly."""
    text = SKILL_MD.read_text(encoding="utf-8").lower()
    assert "target" in text and (
        "without a target" in text or "without a declared" in text or "no length target" in text
    ), (
        "SKILL.md no longer states that compression refuses without a "
        "length target; the contract is at risk of being silently relaxed."
    )
