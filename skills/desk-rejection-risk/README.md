# desk-rejection-risk

Author-side pre-submission audit that flags triggers likely to result
in desk rejection before peer review. Outputs a structured markdown
report with a qualitative risk band (`low / moderate / high`) and
per-category findings.

**Category:** critique
**Modifies the manuscript?** No.
**Editorial-side use?** No — this is **author-side only**. See below.

## Author-side only — load-bearing policy note

Using this skill on a manuscript the user did *not* author —
specifically, using it as an aid in editorial triage of someone
else's submission — violates current peer-review policy at ICMJE,
NIH, Elsevier, and Nature. The skill will refuse to run in that
context. Same posture as
[`reviewer-simulation`](../reviewer-simulation/README.md).

The intended workflow is: the author runs the audit on their own
draft before submitting, addresses high-leverage findings, and
submits a manuscript less likely to be triaged out at the editor's
desk.

## Why this skill exists

At top journals the modal outcome is *desk rejection*, not peer
review. Reported rates run 70–80%+ at *Nature*, *Cell*, *Science*,
~90% at *NEJM* and *Lancet*, and 30–60% at mid-tier subject journals
([`editorial-decision-making`](../../knowledge/peer-review/editorial-decision-making.md)).
The editor's decision is made in 1–3 days from the cover letter, the
abstract, and a glance at figures — applying a small number of triage
heuristics: scope fit, methodological adequacy detectable from the
abstract, novelty, language quality, policy compliance.

The asymmetry is the whole point. A pre-submission audit takes hours;
the submit–wait–reject–resubmit cycle takes months. Catching one
desk-rejection trigger saves more time than catching all the
reviewer-level concerns combined.

## Pairs with `reviewer-simulation`

`desk-rejection-risk` and `reviewer-simulation` do different work and
should not be substituted for each other:

- **`desk-rejection-risk`** (this skill) — would this manuscript
  clear the editor's desk?
- **`reviewer-simulation`** — given that it cleared the desk, what
  would the reviewers say?

Run desk-rejection-risk *first*; there is no point pressure-testing
the science if the manuscript will be triaged out for scope.

## What it does

For each of five editorial-triage categories, surfaces findings
anchored to specific manuscript passages (or notes "not present"
when the absence is itself the finding). Each category carries a
severity flag (`high / moderate / low / not-a-concern / cannot-assess`),
and an overall qualitative risk band rolls them up.

The five categories:

1. **Scope / audience mismatch** — is the manuscript *about* what
   the target venue publishes, in language that audience uses?
2. **Format and length** — word / figure / table limits, abstract
   structure, required statements (data availability, ethics, COI,
   funding, AI disclosure).
3. **Structure and required sections** — are the structurally
   required sections present? Missing Methods, missing Limitations,
   missing reporting-guideline elements (CONSORT, STROBE, ARRIVE,
   PRISMA) detectable from the abstract.
4. **Significance framing** — does the abstract articulate why this
   work matters, why now, for whom? Specific beneficiaries beat
   aspirational language.
5. **Presentation** — title weight-bearing, language quality, figure
   captions, cover letter scope-naming.

Output sections:

- **Summary** — qualitative risk band with a one-paragraph
  justification.
- **Risk findings** — per-category subsections, each with a severity
  flag.
- **Recommended pre-submission actions** — concrete, scoped,
  one-pass-each, ordered by leverage.
- **Cross-checked against MANUSCRIPT_STATE** — acknowledged
  weaknesses are not re-raised as new triggers.
- **What this assessment did NOT check** — honest limits.

## What it does not do

- **Replace peer review.** This is editor-level triage, not
  reviewer-level critique. For the latter, run `reviewer-simulation`.
- **Audit citations.** That's [`citation-audit`](../citation-audit/README.md).
- **Recompute statistics.** Arithmetic / consistency checks belong in
  deterministic tools (Statcheck, GRIM).
- **Produce numeric probabilities.** The base-rate evidence does not
  support per-manuscript probabilistic claims; the audit emits
  qualitative bands only.
- **Run without `project.target_venue`.** Desk rejection is
  venue-conditional. The skill refuses to run without a named
  target — a generic audit produces platitudes.
- **Modify the manuscript or cover letter.**
- **Editorial-side use.** Same posture as `reviewer-simulation`.

## Inputs

- **Manuscript text** — file path or pasted prose. Title, abstract,
  introduction-closer, figure captions and methods abstract-paragraph
  are load-bearing; partial drafts can still surface scope and
  structure risks.
- **`MANUSCRIPT_STATE.yaml`** — usually at the manuscript root. The
  load-bearing fields are `project.target_venue` (required),
  `project.target_type`, `document_phase.current`, `core_claims`,
  `known_weaknesses`, `constraints.max_word_count`, and
  `style.audience`.
- **Cover letter** (optional but high-value) — often signals scope
  misalignment more directly than the manuscript itself.

## Using it

### Inside Claude Code

```text
/scriptorium:desk-rejection-risk
```

Then point Claude at the manuscript file and ensure
`MANUSCRIPT_STATE.yaml` is reachable from the project root with
`project.target_venue` set.

### Outside Claude Code (Codex, Gemini, ChatGPT, …)

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to run
`desk-rejection-risk` on your manuscript.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/desk-rejection-risk/prompt.md
```

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`editorial-decision-making`](../../knowledge/peer-review/editorial-decision-making.md)
  — establishes the 70–90% desk-rejection rates at top journals
  (*Nature*/*Cell*/*Science* 70–80%+, *NEJM*/*Lancet* ~90%, mid-tier
  30–60%), the five triage-heuristic categories editors actually
  use, and Bornmann's inter-reviewer-agreement evidence (κ ≈ 0.17)
  that motivates why the editor's discretion at triage is
  load-bearing. This is the load-bearing knowledge note for the
  whole skill.
- [`significance-positioning`](../../knowledge/scientific-writing/significance-positioning.md)
  — informs the significance-framing category. Day & Gastel's
  problem / what / new / why-it-matters pattern; Lin et al. 2022
  *PNAS* on novel-plus-conventional outperforming purely-novel; the
  NIH Simplified Review Framework Factor 1 (Importance of the
  Research).
- [`common-critiques-taxonomy`](../../knowledge/peer-review/common-critiques-taxonomy.md)
  — Bordage 2001 *Acad Med* top-10 reject reasons seed the recurring
  patterns desk editors catch and reviewers later confirm. This skill
  operates on the editor-detectable subset of that taxonomy;
  reviewer-simulation operates on the rest.
- [`guidance-level`](../../knowledge/conventions/guidance-level.md) —
  the convention this skill adapts conversational framing to.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Venue is mandatory.** A desk-rejection audit without a target
  venue is incoherent — *Nature*'s triage logic and *PLOS ONE*'s
  triage logic share almost nothing. The skill refuses to run if
  `project.target_venue` is empty rather than emit platitudes.
- **Per-category coverage is explicit.** Every category gets a flag,
  including `cannot-assess` when the input doesn't support
  assessment. Silence on a category is the false-confidence failure
  mode this audit exists to *not* produce.
- **Editor-level, not reviewer-level.** The category boundary is
  deliberate. Mechanistic depth and deep statistical critique belong
  in `reviewer-simulation`; this skill stops at what a triage editor
  can see from the abstract.
- **Qualitative bands, not probabilities.** Base-rate evidence
  supports order-of-magnitude statements about journal-level rates;
  it does not support per-manuscript probability estimates.

## See also

- [`reviewer-simulation`](../reviewer-simulation/README.md) — the
  partner skill. Run after this one clears the desk-rejection check.
- [`citation-audit`](../citation-audit/README.md) — the first v0.1
  critique skill; same author-side, evidence-anchored, no-modify
  posture.
- GitHub issue [#73](https://github.com/seandavi/scriptorium/issues/73)
  — the canonical tracking issue.
