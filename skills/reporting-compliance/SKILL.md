---
name: reporting-compliance
description: Run an EQUATOR Network reporting-guideline checklist (CONSORT, STROBE, PRISMA, ARRIVE, STARD, TRIPOD/TRIPOD+AI, CARE, COREQ, CHEERS, plus AI extensions) against a manuscript and classify every checklist item as present / partial / missing / not-applicable. For each item, anchors the classification in a quoted passage from the declared manuscript prose, or explicitly names the gap. Downstream of the v0.2 reporting-guideline-fit skill (which infers which checklist applies); this skill runs the checklist. Validation skill — surfaces gaps for the author to address; does not modify the manuscript and does not invent prose to fill missing items.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/conventions/declared-work-scope.md
  - knowledge/scientific-writing/reporting-guidelines.md
  - knowledge/critique-techniques/internal-consistency.md
---

# Reporting compliance

You are running scriptorium's **reporting-compliance** skill. Your
job is to walk an EQUATOR Network reporting-guideline checklist
against the declared manuscript prose and classify each checklist
item as `present`, `partial`, `missing`, or `not-applicable`, with
the exact quoted passage that satisfies the item (or the explicit
gap when one isn't there).

This is the **downstream audit** in the reporting-guidelines
workflow. The upstream `reporting-guideline-fit` skill (v0.2)
infers *which* EQUATOR checklist applies — CONSORT 2010 for RCTs,
STROBE for observational, PRISMA 2020 for systematic reviews,
ARRIVE 2.0 for animal research, STARD 2015 for diagnostic
accuracy, TRIPOD+AI 2024 for AI-based prediction models, CARE for
case reports, COREQ for qualitative, CHEERS 2022 for health
economic evaluations, plus AI-extensions where applicable. This
skill runs the chosen checklist.

The two skills are deliberately separate. Conflating them
produces a single audit that fails silently when the upstream
inference is wrong (a STROBE checklist run against an RCT misses
randomisation reporting entirely). Stop at the audit step — do
not re-infer the checklist.

## Critical positioning — read before doing anything else

This skill operates on **declared work** ([[declared-work-scope]]).
The manuscript prose is the substrate against which the checklist
is run. The skill **does not invent prose** to fill a missing
item; it surfaces the gap. The author addresses it.

`not-applicable` is a **first-class outcome**. Several checklist
items don't apply to every study — CONSORT item 17b (presentation
of binary outcomes) is N/A for a continuous-outcome trial; PRISMA
item 12 (risk-of-bias in synthesis) is N/A when no synthesis is
performed; ARRIVE items on housing don't apply to *in silico*
studies that happen to live alongside an animal arm. Mark these
cleanly with a one-sentence justification rather than padding
with "consider adding…". A genuine N/A is not a gap.

`partial` is the **right call when the mapping is ambiguous**.
When an item is touched but not fully satisfied — randomisation
named but allocation-concealment mechanism not described, sample
size justified but the assumed effect size not stated — the
honest classification is `partial` with the quoted excerpt and a
one-line "what would tip this to `present`" note. Forcing such
items into a binary present/missing is the failure mode this
skill exists to avoid.

## Critical constraints — read before doing anything else

1. **Never invent prose.** The skill quotes from the manuscript
   or names the gap. It does not write the missing sentence,
   propose phrasing, or suggest "consider adding…" prose. The
   author owns the fix.
2. **Never modify the manuscript.** Validation skill, not a
   transformation. Output is a structured markdown report.
3. **Refuse on `outline` phase.** Per [[declared-work-scope]],
   the substrate isn't there. Refuse cleanly and point the
   author at "come back when the manuscript is in draft, even
   as a partial draft — the audit's value scales with how much
   prose exists."
4. **Refuse when the applicable checklist is unknown.** If
   neither `MANUSCRIPT_STATE.yaml#reporting_guideline` nor a
   passed `reporting_guideline_fit_output` declares which
   checklist to run, refuse and point the author at
   `/scriptorium:reporting-guideline-fit`. Do not guess.
5. **Walk every checklist item.** The audit's value is in
   coverage. Skipping items the skill is unsure about is the
   same failure mode as forcing a confident wrong answer.
   `not-applicable` (with justification) and `partial` (with
   "what would tip to present") are the honest answers when
   the binary present/missing is wrong.
6. **Anchor every `present` and `partial` in a quoted passage.**
   No claim of presence without a location-anchored quote. An
   unsourced "yes, the methods covers this" is hand-waving and
   erodes the audit's trust.
7. **Name the checklist version explicitly.** PRISMA 2020 (not
   PRISMA 2009). TRIPOD+AI 2024 (not TRIPOD 2015) for AI-based
   prediction models. CONSORT-AI extension when applicable. The
   version is load-bearing — item numbers shift between
   versions.
8. **Never write to `MANUSCRIPT_STATE.yaml`.** The schema
   deliberately doesn't carry a `reporting_compliance:` field;
   the audit re-runs cleanly each time. The output is a report,
   not state.
9. **Do not re-infer the checklist.** That's
   `reporting-guideline-fit`'s job. If the author wants to
   change the audited checklist, they re-run that skill.

## Invocation discipline — when to invoke, when not

**Invoke when:**

- The applicable EQUATOR checklist is known — declared in
  `MANUSCRIPT_STATE.yaml#reporting_guideline`, passed as
  `reporting_guideline_fit_output`, or named explicitly in the
  invocation (`/scriptorium:reporting-compliance with CONSORT
  2010`).
- The manuscript is in `draft`, `revision`, or `submission`
  phase.
- The author wants a pre-submission audit, a revision-targeted
  audit (responding to a reviewer who flagged checklist items),
  or a desk-rejection-risk pre-check (some venues desk-reject
  for missing required checklist items).

**Do not invoke when:**

- The applicable checklist is not yet known — run
  `reporting-guideline-fit` first.
- The manuscript is in `outline` phase — substrate isn't there.
- As a silent side-effect of another skill. The output is a
  per-item audit; the author reads it.

## Inputs you should expect

**Required from `MANUSCRIPT_STATE.yaml`:**

- `document_phase.current` — refuse on `outline`.

**One of these must declare which checklist to audit:**

- `MANUSCRIPT_STATE.yaml#reporting_guideline` if the schema
  carries it (current schema deliberately does not — see
  `reporting-guideline-fit` for the rationale).
- A `reporting_guideline_fit_output` payload from a prior
  `reporting-guideline-fit` run, in which case the
  high-confidence inferred guideline(s) drive the audit.
- An explicit guideline named in the invocation
  (`with CONSORT 2010`, `with PRISMA 2020`, etc.).

If none of these is present, refuse and point the author at
`/scriptorium:reporting-guideline-fit`.

**Optional from `MANUSCRIPT_STATE.yaml`:**

- `project.target_venue` — some venues require specific
  checklists or have additional reporting requirements layered
  on the standard checklist. The skill notes venue-specific
  items when relevant.
- `core_claims` — disambiguates intent when an item's
  applicability turns on what the manuscript is arguing.
- `known_weaknesses` — limitations the author has acknowledged.
  An item already covered as a declared weakness reads as
  `partial` (acknowledged but not resolved) rather than
  `missing`.

**Required from the manuscript:**

- The **full manuscript text** is load-bearing — the audit
  walks each section. At minimum: title, abstract, methods,
  results, discussion, and any flow diagram or supplement
  declared in `sections` or `supplements`.

**Optional:**

- The **participant flow diagram** (CONSORT, STROBE, PRISMA)
  or **prediction model flow diagram** (TRIPOD/TRIPOD+AI) if
  declared as a section or supplement.
- Trial / review **registration metadata** (ClinicalTrials.gov,
  PROSPERO, OSF) — specific checklist items map directly to
  the registration record.

## Conversational style

Read `meta.guidance_level` from `MANUSCRIPT_STATE.yaml` (default
`standard` if absent). Adapt framing per [[guidance-level]]:

- `terse` — open with one line ("running reporting-compliance
  against <checklist> <version>"); emit the markdown report;
  no closing summary.
- `standard` — open with a sentence naming the checklist and
  version, the item count, and the manuscript-phase context;
  close with a one-line summary of present / partial / missing
  / N-A counts and the highest-priority gap.
- `full` — open with what reporting guidelines do (minimum-
  information standards so reviewers and readers can evaluate
  methodology consistently — the EQUATOR Network maintains the
  registry of ~600 active guidelines), what this audit
  produces (per-item present / partial / missing / N-A with a
  quoted anchor or explicit gap), and how to read it (act on
  `missing` first, then `partial`; `N/A` is not a gap; the
  audit does not invent prose to fill gaps). If first
  invocation this session, also offer
  `/scriptorium:explain reporting-compliance`.

Run the signal-based check-in once if appropriate. The
structured output is unchanged across levels — only framing
changes. The no-invented-prose posture is **never** relaxed
based on guidance level.

## Operational protocol

Work in this order. Step 1 before step 3 is the guard against
running the wrong checklist; step 4 before step 5 is the guard
against confident-wrong answers on ambiguous items.

1. **Read `MANUSCRIPT_STATE.yaml`.** Extract:
   - `document_phase.current` — if `outline`, decline the run.
   - `reporting_guideline` (if schema carries it) or
     `reporting_guideline_fit_output` (if passed) or the
     explicit guideline named in the invocation. If none, refuse
     and point at `/scriptorium:reporting-guideline-fit`.
   - `project.target_venue` — for venue-specific requirements.
   - `core_claims`, `known_weaknesses` — for context.
   - `meta.guidance_level` — for framing only.
2. **Identify the checklist version.** PRISMA 2020 (not 2009).
   TRIPOD+AI 2024 for AI-based prediction models (not TRIPOD
   2015). Name the version explicitly in the output. Item
   numbers and counts change between versions; auditing against
   the wrong version mis-numbers every finding.
3. **Read the manuscript.** Title, abstract, methods, results,
   discussion, and any flow diagram or supplement. Multi-file
   manuscripts: read each file declared under `sections` or
   `supplements`.
4. **Walk each checklist item systematically.** For each item:
   - Search for the prose passage(s) that would satisfy it.
   - If found and complete, classify `present` with a quoted
     excerpt and the location (section:line if available, or
     section name with a quoted span).
   - If touched but not fully satisfied, classify `partial`
     with the quoted excerpt and a one-line "what would tip
     this to `present`" note.
   - If not found and the item applies to the study design,
     classify `missing` with an explicit gap statement
     ("no allocation-concealment mechanism described"). Do
     **not** propose phrasing.
   - If the item does not apply to this study, classify
     `not-applicable` with a one-sentence justification
     ("continuous primary outcome — item 17b on binary
     outcome presentation does not apply").
5. **Cross-check against `known_weaknesses`.** An item the
   author has already named in `known_weaknesses` is `partial`
   (the gap is acknowledged but not addressed in the prose),
   not `missing`. Note the acknowledgement explicitly.
6. **Layer in venue-specific requirements (if any).** If
   `project.target_venue` is set and the venue carries
   additional reporting requirements beyond the base checklist
   (some journals require trial-registration evidence in the
   abstract; others require specific subgroup-analysis
   reporting), surface those as additional rows.
7. **Tally and emit the structured report.** Use the section
   headings below verbatim so downstream skills and future
   orchestrators can consume the output by structure.

## Output format

Emit a markdown document with exactly these section headings,
in order:

```markdown
# Reporting compliance

## Summary

- Checklist audited: <NAME VERSION> (e.g., CONSORT 2010, PRISMA
  2020, ARRIVE 2.0, TRIPOD+AI 2024)
- Item count: N
- Present: N
- Partial: N
- Missing: N
- Not-applicable: N
- Highest-priority gaps: <one-line list of the missing items the
  author should address first — items that journals routinely
  desk-reject for, or that the upstream `reporting-guideline-fit`
  flagged as high-confidence required>

## Checklist audit

(One row per checklist item. The item numbering matches the
named version. Quoted excerpts use the manuscript's own prose.
Locations are section names — or section:line if available.)

| Item | Status | Anchor or gap | Notes |
|---|---|---|---|
| <n>. <item title> | present | <section:line> — "<quoted excerpt>" | <one-line context if useful> |
| <n>. <item title> | partial | <section:line> — "<quoted excerpt>" | What would tip to present: <one-line note> |
| <n>. <item title> | missing | (no anchor) | Gap: <explicit, no proposed prose> |
| <n>. <item title> | not-applicable | (n/a) | Justification: <one sentence> |

## Highest-priority gaps

(Subset of the `missing` rows. Ordered by what reviewers most
commonly flag and what venues most commonly desk-reject for. Do
**not** propose prose; name the gap.)

1. **Item <n>. <title>.** <One-paragraph statement of what is
   missing and why this item is high-priority. No proposed
   replacement text.>
2. …

## Acknowledged-but-unaddressed items

(Items the author has named in `known_weaknesses` but that the
manuscript prose does not yet address. These are `partial` in
the table above; this section calls them out as a group.)

- <Item n. title> — acknowledged in `known_weaknesses` as
  "<quoted weakness>". The manuscript prose does not yet
  address this in <section>.

## Venue-specific requirements

(Only when `project.target_venue` is set and the venue layers
additional reporting requirements on the base checklist. Empty
otherwise.)

- <Venue>: <additional requirement>. Status: present / partial
  / missing.

## What this audit did NOT check

(Honest list. Always include the items below; add specifics from
the current run where relevant.)

- Whether the chosen checklist was the right one. That is the
  upstream `reporting-guideline-fit` skill's job; this audit
  trusts the inference.
- Whether the underlying study design was the right choice. The
  audit assesses what is reported, not whether the design was
  appropriate.
- Whether quantitative claims are internally consistent (Table 1
  N vs. methods N; abstract percentages vs. figure percentages).
  That is the planned `statistics-consistency` skill's job.
- Whether figures match the prose. That is the planned
  `figure-text-alignment` skill's job.
- The bibliography itself. Reporting guidelines specify *what*
  must be reported, not citation accuracy — that is the
  `citation-audit` skill's job.
- Editor-side enforcement. Author-side decision support.
```

## What "good output" looks like

- **Anchored.** Every `present` and `partial` row carries a
  quoted excerpt from the manuscript and a location. An
  unsourced "yes, randomisation is described" is the failure
  mode this audit exists to avoid.
- **Honest about `partial`.** Items touched but not fully
  satisfied are `partial` with a one-line "what would tip this
  to `present`" — never forced into binary present/missing.
- **`not-applicable` carries justification.** A clean N/A with
  a one-sentence rationale is a first-class outcome, not
  padding. The author should see why the audit skipped each
  N/A item.
- **Missing rows name the gap; they do not propose prose.**
  "No allocation-concealment mechanism described" is the right
  level. "Consider adding: 'Allocation was concealed using
  sequentially numbered opaque envelopes…'" is **not**.
- **Version-anchored.** The output names CONSORT 2010, PRISMA
  2020, TRIPOD+AI 2024, etc., explicitly — item numbers and
  counts depend on the version.
- **Highest-priority gaps section is short and substantive.**
  Three to six items the reviewer is most likely to call out;
  not every missing item gets promoted.
- **Acknowledged-but-unaddressed gaps cross-reference
  `known_weaknesses`** so the author sees which gaps they have
  already named vs. which are surprises.

## What you must not do

- Invent prose to fill missing items. Surface the gap; the
  author owns the fix.
- Modify the manuscript or any state file.
- Re-infer the applicable checklist. That is
  `reporting-guideline-fit`'s job; this skill audits the
  checklist it is given.
- Force a confident `present` or `missing` when the honest
  answer is `partial`.
- Mark items `not-applicable` without a one-sentence
  justification. A bare N/A erodes trust.
- Skip checklist items the audit is unsure about. Walk every
  item; the value is in coverage.
- Audit against a superseded checklist version when a current
  version applies (PRISMA 2009 when 2020 is current; TRIPOD
  2015 when TRIPOD+AI 2024 is current for AI-based models).
- Run other skills as side effects.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [[reporting-guidelines]] — the primary anchor. EQUATOR
  Network registry; design-specific checklists (CONSORT 2010,
  STROBE, PRISMA 2020, ARRIVE 2.0, STARD 2015, TRIPOD 2015 /
  TRIPOD+AI 2024, CARE, COREQ, CHEERS 2022); AI-extension
  landscape (CONSORT-AI / SPIRIT-AI / STARD-AI / TRIPOD+AI).
  The note's framing of reporting guidelines as the
  **validation contract** ("a trial paper that omits
  randomization details is not recoverable by good prose") is
  the design rationale for this skill being validation-shaped:
  the audit surfaces gaps the prose cannot recover from.
  The note also names this skill explicitly as "a direct
  mapping from manuscript sections to checklist items. Output:
  per-item status (present / partial / missing /
  not-applicable) with a span pointer for each 'present'
  claim" — that anchor pattern is exactly what this skill's
  output table implements.
- [[declared-work-scope]] — the convention. The audit
  operates on declared manuscript prose; refuses cleanly on
  outline or when the applicable checklist is unknown; never
  invents prose to fill missing items.
- [[internal-consistency]] — the bookkeeping framing. The
  per-item walk treats each checklist item as a cross-section
  comparison: does what the prose says satisfy the item's
  minimum-information requirement? This is the same posture
  internal-consistency takes for terminology drift and
  number-matching; here it is applied to checklist
  coverage.
- [[guidance-level]] — the framing-level convention.

This skill is the **downstream audit** in the
reporting-guidelines workflow; the v0.2
`reporting-guideline-fit` skill is the upstream inference.
The two are deliberately separate.

## See also

- `/scriptorium:reporting-guideline-fit` (v0.2) — the upstream
  skill that infers which EQUATOR checklist applies. Run it
  first when the applicable checklist isn't known.
- `/scriptorium:reviewer-simulation` — pairs naturally before
  submission. Reviewers at high-tier journals check
  reporting-guideline compliance; running both before
  submission catches both content and reporting issues.
- `/scriptorium:desk-rejection-risk` — pairs naturally when
  `target_venue` is set. Some venues desk-reject manuscripts
  that don't meet their required reporting guideline; this
  audit is the upstream check.
- `/scriptorium:citation-audit` — orthogonal: this skill
  audits what the prose reports; citation-audit audits what
  the prose cites. Both run cleanly side by side.
- `/scriptorium:explain reporting-compliance` — full design
  tour.
