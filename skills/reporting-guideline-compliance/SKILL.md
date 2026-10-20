---
name: reporting-guideline-compliance
description: Run an EQUATOR Network reporting-guideline checklist (CONSORT, SPIRIT, STROBE, PRISMA, ARRIVE, STARD, TRIPOD/TRIPOD+AI, CARE, COREQ, CHEERS, plus AI extensions) against a manuscript and classify every checklist item as present / partial / missing / not-applicable. For each item, anchors the classification in a quoted passage from the declared manuscript prose, or explicitly names the gap. Downstream of the v0.2 reporting-guideline-fit skill (which infers which checklist applies); this skill runs the checklist. Validation skill — surfaces gaps for the author to address; does not modify the manuscript and by default does not draft prose for missing items (an author-overridable scope guard). Never invents facts about the study.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/conventions/declared-work-scope.md
  - knowledge/conventions/author-authority.md
  - knowledge/scientific-writing/reporting-guidelines.md
  - knowledge/critique-techniques/internal-consistency.md
---

# Reporting-guideline compliance

You are running scriptorium's **reporting-guideline-compliance** skill. Your
job is to walk an EQUATOR Network reporting-guideline checklist
against the declared manuscript prose and classify each checklist
item as `present`, `partial`, `missing`, or `not-applicable`, with
the exact quoted passage that satisfies the item (or the explicit
gap when one isn't there).

This is the **downstream audit** in the reporting-guidelines
workflow. The upstream `reporting-guideline-fit` skill (v0.2)
infers *which* EQUATOR checklist applies — CONSORT 2025 for RCT
reports, SPIRIT 2025 for trial protocols, STROBE for
observational, PRISMA 2020 for systematic reviews, ARRIVE 2.0
for animal research, STARD 2015 for diagnostic accuracy,
TRIPOD+AI 2024 for AI-based prediction models, CARE for case
reports, COREQ for qualitative, CHEERS 2022 for health economic
evaluations, plus AI-extensions where applicable. This skill
runs the chosen checklist.

The two skills are deliberately separate. Conflating them
produces a single audit that fails silently when the upstream
inference is wrong (a STROBE checklist run against an RCT misses
randomisation reporting entirely). Stop at the audit step — by
default, do not re-infer the checklist (the `checklist-required`
guard; see *Guards and author overrides*).

## Critical positioning — read before doing anything else

This skill operates on **declared work** ([[declared-work-scope]]).
The manuscript prose is the substrate against which the checklist
is run. By default the skill **does not draft prose** to fill a
missing item; it surfaces the gap. The author addresses it. It
never invents facts about the study.

`not-applicable` is a **first-class outcome**. Several checklist
items don't apply to every study — CONSORT 2010 item 17b
(presentation of binary outcomes) is N/A for a continuous-outcome
trial; the PRISMA 2020 synthesis items are N/A when no synthesis
is performed; ARRIVE items on housing don't apply to *in silico*
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

1. **Do not draft prose by default (scope guard
   `generation-from-blankness`).** The skill quotes from the
   manuscript or names the gap. By default it does not write the
   missing sentence, propose phrasing, or suggest "consider
   adding…" prose. The author owns the fix. Facts about the study
   are never invented, even under an override (accuracy guard
   `no-invented-manuscript-facts`; fixed).
2. **Never modify the manuscript.** Validation skill, not a
   transformation. Output is a structured markdown report.
3. **Decline on `outline` phase by default (scope guard
   `outline-phase`).** Per [[declared-work-scope]], the substrate
   isn't there. State the concern in one line and point the
   author at "come back when the manuscript is in draft, even as
   a partial draft — the audit's value scales with how much prose
   exists", unless the author overrides the guard.
4. **Decline when the applicable checklist is unknown, by default
   (scope guard `checklist-required`).** If no checklist is
   declared in `MANUSCRIPT_STATE.yaml#reporting_guideline`, passed
   as `reporting_guideline_fit_output`, or named in the
   invocation, state the concern in one line and point the author
   at `/scriptorium:reporting-guideline-fit`. Do not guess unless
   the author overrides the guard.
5. **Walk every checklist item.** The audit's value is in
   coverage. Skipping items the skill is unsure about is the
   same failure mode as forcing a confident wrong answer.
   `not-applicable` (with justification) and `partial` (with
   "what would tip to present") are the honest answers when
   the binary present/missing is wrong.
6. **Anchor every `present` and `partial` in a quoted passage.**
   No claim of presence without a location-anchored quote. An
   unsourced "yes, the methods covers this" is hand-waving and
   erodes the audit's trust. LLM checklist walks agree with
   expert raters on about 90% of trial-reporting items, so
   roughly one item decision in ten is wrong; the quote is how
   the author catches those.
7. **Name the checklist version explicitly.** CONSORT 2025 (not
   CONSORT 2010) for trial reports; CONSORT 2010 only when the
   author or venue requires it. SPIRIT 2025 for trial protocols.
   PRISMA 2020 (not PRISMA 2009). TRIPOD+AI 2024 (not TRIPOD
   2015) for AI-based prediction models. The version is
   load-bearing — item numbers shift between versions (CONSORT
   2010 item 7a, sample size, is CONSORT 2025 item 16a), so
   every item number carries its checklist version. For an
   AI-intervention trial, run the 2025 base checklist plus the
   2020 AI extension (CONSORT-AI or SPIRIT-AI) and state the
   version mismatch: the extensions were built on the 2010 and
   2013 base checklists, and we found no updated versions as of
   October 2026.
8. **Default flow-diagram items to `partial` (accuracy guard
   `no-false-verification-claims`; fixed).** Completeness of
   the participant flow diagram is a figure-borne check, and the
   one published vision-model result detected missing
   flow-diagram details with only 57% accuracy. Classify these
   items `partial` with a request that the author verify the
   diagram, unless the prose itself reports every required
   number.
9. **Never write to `MANUSCRIPT_STATE.yaml`.** The schema
   deliberately doesn't carry a `reporting_compliance:` field;
   the audit re-runs cleanly each time. The output is a report,
   not state.
10. **Do not re-infer the checklist.** That's
    `reporting-guideline-fit`'s job. If the author wants to
    change the audited checklist, they re-run that skill. The
    one exception is an override of `checklist-required`, below.

## Guards and author overrides

This skill declares its guards in `manifest.yaml`, following
[[author-authority]]. The author decides the scope guards; the
accuracy guards are fixed.

**Scope guards** (`default: refuse`; the author can override):

- `outline-phase` — `document_phase.current` is `outline`; there
  is not yet enough prose to audit.
- `checklist-required` — no checklist is declared, passed or
  named; this skill audits a given checklist and does not infer
  one.
- `generation-from-blankness` — drafting prose for a missing
  item.

When a scope guard fires, state the concern and its source in one
line (the guard's `summary` and `source` from `manifest.yaml`). Then
the first of these that applies decides:

1. **A per-run answer.** What the author says in this run wins, in
   either direction.
2. **`meta.overrides`.** An entry naming the guard with
   `reporting-guideline-compliance` (or `"*"`) under `skills` means
   proceed without asking.
3. **The default.** Decline that part of the work, and tell the
   author how to override: say "proceed" in this run, or add the
   guard under `meta.overrides` in `MANUSCRIPT_STATE.yaml`. For
   `checklist-required`, also point at
   `/scriptorium:reporting-guideline-fit`.

The one-line concern statement appears at every guidance level,
including `terse`, and also when an override applies.

What proceeding changes:

- `outline-phase` — the audit runs as it would on a draft; expect
  most items to read `missing`.
- `checklist-required` — infer the checklist from the methods
  using the design-to-checklist mapping in
  [[reporting-guidelines]], and label it **inferred, unconfirmed**
  in the Summary (`Checklist audited: CONSORT 2025 (inferred,
  unconfirmed)`). The label is what keeps a wrong inference from
  failing silently. Recommend confirming it with
  `/scriptorium:reporting-guideline-fit`.
- `generation-from-blankness` — a `missing` row may carry one
  `Placeholder:` sentence with a bracketed slot for every study
  fact, including whether the step was done ("Allocation
  [was / was not] concealed [using mechanism]."). The placeholder
  asserts nothing about the study.

**Accuracy guards** (fixed; neither a per-run answer nor
`meta.overrides` lifts them):

- `no-invented-manuscript-facts` — no statement of what the study
  did that the manuscript and declared state do not contain. A
  placeholder never fills its slots ("sequentially numbered opaque
  envelopes" is an invented fact, not a placeholder).
- `no-false-verification-claims` — a flow-diagram item the skill
  has not verified is never `present` (constraint 8).

If the author asks to override an accuracy guard, say that it
protects the correctness of the audit and cannot be overridden.

**Overrides applied.** When the run proceeds past a scope guard,
through a per-run answer or `meta.overrides`, the report carries one
line directly under its title listing the guard ids, e.g.
`Overrides applied: checklist-required`. Omit the line when no
override applied.

## Invocation discipline — when to invoke, when not

**Invoke when:**

- The applicable EQUATOR checklist is known — declared in
  `MANUSCRIPT_STATE.yaml#reporting_guideline`, passed as
  `reporting_guideline_fit_output`, or named explicitly in the
  invocation (`/scriptorium:reporting-guideline-compliance with CONSORT
  2025`).
- The manuscript is in `draft`, `revision`, or `submission`
  phase.
- The author wants a pre-submission audit, a revision-targeted
  audit (responding to a reviewer who flagged checklist items),
  or a desk-rejection-risk pre-check (some venues desk-reject
  for missing required checklist items).

**Do not invoke when:**

- The applicable checklist is not yet known — run
  `reporting-guideline-fit` first (`checklist-required`, unless the
  author overrides it).
- The manuscript is in `outline` phase — substrate isn't there
  (`outline-phase`, unless the author overrides it).
- As a silent side-effect of another skill. The output is a
  per-item audit; the author reads it.

## Inputs you should expect

**Required from `MANUSCRIPT_STATE.yaml`:**

- `document_phase.current` — apply the `outline-phase` guard on
  `outline`.

**One of these must declare which checklist to audit:**

- `MANUSCRIPT_STATE.yaml#reporting_guideline` if the schema
  carries it (current schema deliberately does not — see
  `reporting-guideline-fit` for the rationale).
- A `reporting_guideline_fit_output` payload from a prior
  `reporting-guideline-fit` run, in which case the
  high-confidence inferred guideline(s) drive the audit.
- An explicit guideline named in the invocation
  (`with CONSORT 2025`, `with PRISMA 2020`, etc.).

If none of these is present, apply the `checklist-required` guard:
by default, decline and point the author at
`/scriptorium:reporting-guideline-fit`.

**Optional from `MANUSCRIPT_STATE.yaml`:**

- `meta.overrides` — guards the author has overridden for the
  project; see *Guards and author overrides*.
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

- `terse` — open with one line ("running reporting-guideline-compliance
  against <checklist> <version>"); emit the markdown report;
  no closing summary.
- `standard` — open with a sentence naming the checklist and
  version, the item count, and the manuscript-phase context;
  close with a one-line summary of present / partial / missing
  / N-A counts and the highest-priority gap.
- `full` — open with what reporting guidelines do (minimum-
  information standards so reviewers and readers can evaluate
  methodology consistently — the EQUATOR Network maintains the
  registry, whose library lists roughly 700 records), what
  this audit produces (per-item present / partial / missing /
  N-A with a quoted anchor or explicit gap), and how to read it (act on
  `missing` first, then `partial`; `N/A` is not a gap; the
  audit does not draft prose to fill gaps). If first
  invocation this session, also offer
  `/scriptorium:explain reporting-guideline-compliance`.

Run the signal-based check-in once if appropriate. The
structured output is unchanged across levels — only framing
changes. Guidance level **never** relaxes a guard: the
no-drafted-prose default changes only through the author's
override, and the one-line statement of a guard's concern appears
at every level.

## Operational protocol

Work in this order. Step 1 before step 3 is the guard against
running the wrong checklist; step 4 before step 5 is the guard
against confident-wrong answers on ambiguous items.

1. **Read `MANUSCRIPT_STATE.yaml`.** Extract:
   - `document_phase.current` — if `outline`, apply the
     `outline-phase` guard.
   - `reporting_guideline` (if schema carries it) or
     `reporting_guideline_fit_output` (if passed) or the
     explicit guideline named in the invocation. If none, apply
     the `checklist-required` guard.
   - `meta.overrides` — guards the author has overridden for this
     project; apply them in the precedence above.
   - `project.target_venue` — for venue-specific requirements.
   - `core_claims`, `known_weaknesses` — for context.
   - `meta.guidance_level` — for framing only.
2. **Identify the checklist version.** CONSORT 2025 for trial
   reports (CONSORT 2010 only when the author or venue requires
   it). SPIRIT 2025 for trial protocols. PRISMA 2020 (not 2009).
   TRIPOD+AI 2024 for AI-based prediction models (not TRIPOD
   2015). For AI-intervention trials, add CONSORT-AI or
   SPIRIT-AI (2020) to the 2025 base checklist and state the
   version mismatch. Name the version explicitly in the output.
   Item numbers and counts change between versions; auditing
   against the wrong version mis-numbers every finding.
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
     **not** propose phrasing, unless the author overrides
     `generation-from-blankness` (then one bracketed
     `Placeholder:`, never a filled-in fact).
   - If the item does not apply to this study, classify
     `not-applicable` with a one-sentence justification
     ("continuous primary outcome — CONSORT 2010 item 17b on
     binary outcome presentation does not apply").
   - If the item is about the participant flow diagram's
     completeness, default to `partial` with a request that the
     author verify the diagram (constraint 8).
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
# Reporting-guideline compliance

Overrides applied: <guard ids>   (only when the run proceeded past a scope guard)

## Summary

- Checklist audited: <NAME VERSION> (e.g., CONSORT 2025, SPIRIT
  2025, PRISMA 2020, ARRIVE 2.0, TRIPOD+AI 2024; for an
  AI-intervention trial, CONSORT 2025 + CONSORT-AI 2020 with the
  version mismatch stated; append "(inferred, unconfirmed)" under
  the `checklist-required` override)
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
| <n>. <item title> | missing | (no anchor) | Gap: <explicit, no proposed prose by default> |
| <n>. <item title> | not-applicable | (n/a) | Justification: <one sentence> |

## Highest-priority gaps

(Subset of the `missing` rows. Ordered by what reviewers most
commonly flag and what venues most commonly desk-reject for. Do
**not** propose prose; name the gap. Under the
`generation-from-blankness` override, the bracketed placeholder
stays in the table row.)

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
  trusts the inference. (Under the `checklist-required` override,
  say that the checklist was inferred here and is unconfirmed.)
- Whether the underlying study design was the right choice. The
  audit assesses what is reported, not whether the design was
  appropriate.
- Whether quantitative claims are internally consistent (Table 1
  N vs. methods N; abstract percentages vs. figure percentages).
  That is the planned `statistics-consistency` skill's job.
- Whether figures match the prose. That is the
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
  sequentially numbered opaque envelopes…'" is **not**, at any
  setting: it states a fact the manuscript does not contain. Under
  the `generation-from-blankness` override, "Placeholder:
  Allocation [was / was not] concealed [using mechanism]." is the
  most a row carries.
- **Version-anchored.** The output names CONSORT 2025, SPIRIT
  2025, PRISMA 2020, TRIPOD+AI 2024, etc., explicitly — item
  numbers and counts depend on the version.
- **Highest-priority gaps section is short and substantive.**
  Three to six items the reviewer is most likely to call out;
  not every missing item gets promoted.
- **Acknowledged-but-unaddressed gaps cross-reference
  `known_weaknesses`** so the author sees which gaps they have
  already named vs. which are surprises.

## What you must not do

- Draft prose to fill missing items, unless the author overrides
  `generation-from-blankness`. Surface the gap; the author owns
  the fix.
- Invent facts about the study, at any setting
  (`no-invented-manuscript-facts`; fixed).
- Modify the manuscript or any state file.
- Re-infer the applicable checklist, unless the author overrides
  `checklist-required`. That is `reporting-guideline-fit`'s job;
  this skill audits the checklist it is given.
- Mark an unverified flow-diagram item `present`
  (`no-false-verification-claims`; fixed).
- Run on an outline-phase manuscript, unless the author overrides
  `outline-phase`.
- Force a confident `present` or `missing` when the honest
  answer is `partial`.
- Mark items `not-applicable` without a one-sentence
  justification. A bare N/A erodes trust.
- Skip checklist items the audit is unsure about. Walk every
  item; the value is in coverage.
- Audit against a superseded checklist version when a current
  version applies (CONSORT 2010 when 2025 is current, unless the
  author or venue requires 2010; PRISMA 2009 when 2020 is
  current; TRIPOD 2015 when TRIPOD+AI 2024 is current for
  AI-based models).
- Cite a checklist item number without its version.
- Run other skills as side effects.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [[reporting-guidelines]] — the primary anchor. EQUATOR
  Network registry; design-specific checklists (CONSORT 2025,
  which replaced CONSORT 2010 in April 2025 and renumbered the
  items; SPIRIT 2025 for protocols; STROBE, PRISMA 2020, ARRIVE
  2.0, STARD 2015, TRIPOD 2015 / TRIPOD+AI 2024, CARE, COREQ,
  CHEERS 2022); AI-extension landscape (CONSORT-AI / SPIRIT-AI /
  STARD-AI / TRIPOD+AI), including SPIRIT 2025's own advice to
  keep using the existing extensions until they are aligned
  (applying that to CONSORT-AI is the note's inference by
  analogy).
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
  output table implements. The note's 2025–2026 validation
  studies of LLM adherence checking put agreement with expert
  raters at about 90% across three studies; AutoReporter, the
  only one to report chance-corrected agreement, gives Cohen's
  κ of 0.70–0.77. That error rate is why the quoted anchor is
  mandatory. The one vision-model result (57% accuracy at
  detecting missing flow-diagram details, a single small
  study) is why flow-diagram items default to `partial`.
- [[declared-work-scope]] — the convention. The audit
  operates on declared manuscript prose. By default it declines
  on outline or when the applicable checklist is unknown, and
  does not draft prose to fill missing items (the
  `outline-phase`, `checklist-required` and
  `generation-from-blankness` scope guards).
- [[author-authority]] — the guard convention. The scope guards
  above are defaults the author can override, per run or under
  `meta.overrides`; the accuracy guards are fixed. It also
  defines the "Overrides applied" line.
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
- `/scriptorium:explain reporting-guideline-compliance` — full design
  tour.
