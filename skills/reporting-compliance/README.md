# reporting-compliance — audit a manuscript against its EQUATOR checklist

Walks an EQUATOR Network reporting-guideline checklist (CONSORT
2010, STROBE, PRISMA 2020, ARRIVE 2.0, STARD 2015, TRIPOD 2015 /
TRIPOD+AI 2024, CARE, COREQ, CHEERS 2022, plus AI-extensions
where applicable) against a manuscript, and classifies every
checklist item as `present`, `partial`, `missing`, or
`not-applicable`. Each `present` and `partial` row anchors in a
quoted manuscript excerpt; each `missing` row names the gap
explicitly without proposing replacement prose.

This is the **downstream audit** in the reporting-guidelines
workflow. The upstream `reporting-guideline-fit` skill (v0.2)
infers *which* EQUATOR checklist applies; this skill runs the
chosen checklist.

**Category:** validation
**Modifies the manuscript?** No. Output is a structured
markdown report; the author addresses the gaps.
**Invocation:** explicit. Invoke when the applicable checklist
is known and the manuscript is in `draft` / `revision` /
`submission` phase.

## What it does

- **Per-item classification.** Every checklist item is walked
  and labelled `present`, `partial`, `missing`, or
  `not-applicable`. Coverage is the point — items the audit is
  unsure about are `partial` (with "what would tip to
  `present`") or `not-applicable` (with justification), never
  silently skipped.
- **Quoted anchors.** Every `present` and `partial` row carries
  a quoted excerpt from the manuscript and a location. An
  unsourced "yes, this is covered" is the failure mode this
  skill exists to avoid.
- **Explicit gaps.** Every `missing` row names what is absent
  ("no allocation-concealment mechanism described") — the skill
  does not propose replacement prose.
- **`not-applicable` as a first-class outcome.** Items that
  genuinely don't apply (CONSORT item 17b on binary outcomes
  for a continuous-outcome trial; PRISMA item 12 when no
  synthesis is performed) are marked `not-applicable` with a
  one-sentence justification rather than padded with "consider
  adding…".
- **Acknowledged-but-unaddressed cross-reference.** Items the
  author has named in `MANUSCRIPT_STATE.yaml#known_weaknesses`
  but not yet addressed in the prose are surfaced as `partial`
  (acknowledged) rather than `missing` (surprise).
- **Version honesty.** PRISMA 2020 (not 2009). TRIPOD+AI 2024
  (not TRIPOD 2015) for AI-based prediction models. CONSORT-AI
  extension when applicable. The named version is load-bearing
  — item numbers shift between versions.

## What it does not do

- **Infer which checklist applies.** That is the upstream
  `reporting-guideline-fit` skill's job (v0.2). When the
  applicable checklist isn't known, this skill refuses and
  points the author there. It does not guess.
- **Invent prose.** This skill names gaps; it does not write
  replacement sentences or propose phrasing. The author owns
  the fix.
- **Modify the manuscript.** Validation only.
- **Critique study design.** The audit assesses what is
  reported, not whether the design was the right choice.
- **Audit quantitative internal consistency** (Table 1 N vs.
  methods N; abstract percentages vs. figure percentages) —
  that is the planned `statistics-consistency` skill's job.
- **Audit figure / text alignment.** Planned
  `figure-text-alignment` skill.
- **Audit citation accuracy.** That is `citation-audit`'s job.
- **Operate on outline-phase manuscripts.** No substrate.
- **Editor-side enforcement.** Author-side decision support
  only.

## Inputs

- **Manuscript text** — file path(s) or pasted prose. For
  multi-file projects, every file declared under `sections`
  and `supplements` is read.
- **`MANUSCRIPT_STATE.yaml`** — `document_phase.current` is
  load-bearing (refuses on `outline`). Optional but useful:
  `project.target_venue` (venue-specific layered requirements),
  `core_claims` (intent disambiguation), `known_weaknesses`
  (acknowledged-but-unaddressed cross-reference),
  `meta.guidance_level` (framing).
- **Which checklist to audit.** One of: output from a prior
  `reporting-guideline-fit` run; an explicit checklist named in
  the invocation (`with CONSORT 2010`, etc.); or (when the
  schema carries it) `MANUSCRIPT_STATE.yaml#reporting_guideline`.

If the applicable checklist isn't supplied, the skill refuses
and points the author at `reporting-guideline-fit`.

## Using it

### Inside Claude Code

```text
/scriptorium:reporting-compliance
```

Then point Claude at the manuscript file(s) and ensure
`MANUSCRIPT_STATE.yaml` is reachable from the project root. If
you haven't already run `reporting-guideline-fit`, do so first.

### Outside Claude Code (Codex, Gemini, Hermes, ChatGPT, …)

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to
run `reporting-compliance` on your manuscript.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/reporting-compliance/prompt.md
```

## Output structure

```markdown
# Reporting compliance

## Summary
- Checklist audited: <NAME VERSION>
- Item count: N
- Present: N | Partial: N | Missing: N | Not-applicable: N
- Highest-priority gaps: <one-line list>

## Checklist audit
| Item | Status | Anchor or gap | Notes |

## Highest-priority gaps
(Subset of missing rows; ordered by reviewer / desk-rejection
priority.)

## Acknowledged-but-unaddressed items
(Items present in `known_weaknesses` but not yet in the prose.)

## Venue-specific requirements
(Only when `project.target_venue` adds layered requirements.)

## What this audit did NOT check
```

## Why "present / partial / missing / not-applicable"

Reporting guidelines are minimum-information standards, not
style advice. The four-state classification reflects how
checklist items actually map to manuscript prose:

- `present` and `missing` are the easy cases.
- `partial` is the **honest answer** when an item is touched
  but not fully satisfied — e.g., randomisation named but
  allocation-concealment mechanism not described. Forcing such
  items into a binary present/missing is the audit failure
  mode this skill exists to avoid.
- `not-applicable` is a **first-class outcome**. Several
  checklist items don't apply to every study (continuous-outcome
  trial → item 17b on binary outcomes is N/A; *in silico*
  arm of a study with an animal arm → ARRIVE housing items
  don't apply to the *in silico* arm). Padding these with
  "consider adding…" is dishonest; marking them cleanly with
  a one-sentence justification is the right answer.

## Why "do not invent prose"

The skill names gaps; the author writes the prose. This is the
declared-work-scope principle ([`declared-work-scope`](../../knowledge/conventions/declared-work-scope.md))
at the validation surface: scriptorium operates on prose the
author has written or scaffolding the author has declared, and
refuses cleanly when asked to produce prose from blankness.
Reporting-compliance gaps are precisely where "consider adding…"
phrasing slips into ghostwritten reporting language; this skill
takes the harder discipline of pointing at the gap and stopping
there.

## Sibling-skill relationship

`reporting-compliance` is the **downstream audit** in a
two-skill workflow:

1. `reporting-guideline-fit` (v0.2) — **upstream inference**.
   Reads the methods section, infers which EQUATOR checklist
   applies (CONSORT? STROBE? PRISMA? ARRIVE? TRIPOD+AI?), with
   confidence levels. Stops at the recommendation.
2. `reporting-compliance` (v0.3 — this skill) — **downstream
   audit**. Walks the chosen checklist against the manuscript;
   classifies each item.

Conflating the two produces a single audit that fails silently
when the upstream inference is wrong (a STROBE checklist run
against an RCT misses randomisation reporting entirely). The
two skills are deliberately separate.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`reporting-guidelines`](../../knowledge/scientific-writing/reporting-guidelines.md)
  — the primary anchor. The EQUATOR Network registry, the
  design-specific checklists (CONSORT 2010, STROBE, PRISMA
  2020, ARRIVE 2.0, STARD 2015, TRIPOD 2015 / TRIPOD+AI 2024,
  CARE, COREQ, CHEERS 2022) with their canonical citations,
  the AI-extension landscape (CONSORT-AI / SPIRIT-AI /
  STARD-AI / TRIPOD+AI), and the framing of reporting
  guidelines as the **validation contract** for scholarly
  writing. The note names this skill explicitly as the
  per-item present / partial / missing / not-applicable
  audit "with a span pointer for each 'present' claim" —
  the output table is exactly that.
- [`declared-work-scope`](../../knowledge/conventions/declared-work-scope.md)
  — the convention. The audit operates on declared manuscript
  prose; refuses cleanly on outline or when the applicable
  checklist is unknown; never invents prose to fill missing
  items.
- [`internal-consistency`](../../knowledge/critique-techniques/internal-consistency.md)
  — the bookkeeping framing. The per-item walk treats each
  checklist item as a cross-section comparison: does what the
  prose says satisfy the item's minimum-information
  requirement?
- [`guidance-level`](../../knowledge/conventions/guidance-level.md)
  — the framing-level convention shared by every
  conversation-bearing skill.

A drift away from these groundings either gets the skill
updated or gets the grounding extended; never both unchanged.

## Design notes

- **Validation, not transformation.** The skill emits a report;
  the author edits the manuscript. The conservative-edit
  posture in [DESIGN.md](../../DESIGN.md) places critique and
  validation strictly upstream of any prose modification; this
  skill sits in the validation tier.
- **No invented prose.** The temptation in a checklist audit is
  to write the missing sentence ("consider adding: 'Allocation
  was concealed using sequentially numbered opaque envelopes…'").
  This skill explicitly does not. The author owns the fix; the
  audit names the gap. The harder discipline produces a more
  trustworthy report.
- **Coverage over confidence.** Walking every item — even with
  honest `partial` and `not-applicable` labels — is more useful
  than walking only the items the audit is sure about. Coverage
  is the value proposition.
- **Version-anchored.** PRISMA 2020 has 27 items in a different
  layout from PRISMA 2009's 27 items; TRIPOD+AI 2024's 27 items
  are different again from TRIPOD 2015's 22. Naming the version
  is load-bearing.
- **Pairs naturally with `reviewer-simulation` and
  `desk-rejection-risk`.** Reviewers at high-tier journals
  routinely check checklist compliance; some venues
  desk-reject manuscripts missing required items. Running this
  audit before submission catches both content and reporting
  gaps.

## See also

- [`reporting-guideline-fit`](../reporting-guideline-fit/README.md)
  — the upstream skill that infers which EQUATOR checklist
  applies. Run it first when the applicable checklist isn't
  known.
- [`reviewer-simulation`](../reviewer-simulation/README.md) —
  pairs naturally before submission.
- [`desk-rejection-risk`](../desk-rejection-risk/README.md) —
  pairs naturally when `target_venue` is set.
- [`citation-audit`](../citation-audit/README.md) — orthogonal:
  this skill audits what the prose reports; citation-audit
  audits what the prose cites.
- [`knowledge/scientific-writing/reporting-guidelines.md`](../../knowledge/scientific-writing/reporting-guidelines.md)
  — the grounding note with the canonical references.
