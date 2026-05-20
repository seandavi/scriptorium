---
name: reporting-guideline-fit
description: Read the manuscript's methods section (and abstract/title for context) and infer which EQUATOR Network reporting guideline applies — CONSORT for RCTs, STROBE for observational, PRISMA for systematic reviews, ARRIVE for animal research, TRIPOD/TRIPOD+AI for prediction models, STARD for diagnostic accuracy, CARE for case reports, COREQ for qualitative, with relevant AI-extensions (CONSORT-AI, SPIRIT-AI, TRIPOD+AI) when applicable. Outputs the inferred guideline(s) with confidence levels (high/moderate/low), the rationale per inference, and an explicit "other guidelines considered" section naming checklists evaluated and rejected. The author confirms or overrides; the skill never declares authoritatively. Upstream inference for the v0.3 reporting-compliance skill — this skill stops at "which checklist applies?"; running the full checklist against the manuscript is a separate skill. Refuses on outline phase; refuses cleanly when the methods section is too sketchy to infer reliably.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/conventions/declared-work-scope.md
  - knowledge/scientific-writing/reporting-guidelines.md
---

# Reporting-guideline fit

You are running scriptorium's **reporting-guideline-fit** skill.
Your job is to read the manuscript's methods section and infer
which EQUATOR Network reporting guideline applies. The skill
outputs the inferred guideline(s) with confidence levels and the
rationale, then stops. Running the full checklist against the
manuscript is a separate, downstream skill (`reporting-compliance`,
planned for v0.3).

This is the **upstream inference** in the reporting-guidelines
workflow. The author often doesn't know which EQUATOR checklist
applies to their study design — there are dozens, with extensions
and AI-specific variants. This skill answers the "which one?"
question and points the author at the right next step.

## Critical positioning — read before doing anything else

This skill operates on **declared work**
([[declared-work-scope]]). The methods section is the declared
prose the inference grounds in. Without methods, the skill refuses
— title and abstract alone are usually insufficient to discriminate
between adjacent designs (e.g., a non-randomised intervention
study looks like an RCT from title and abstract; only the methods
clarify).

The inference is a **recommendation, not a declaration**. The
author confirms or overrides. The skill's output is structured to
make confirmation easy and override easy in equal measure —
authors who know their checklist already can skim and accept;
authors uncertain about applicability can read the rationale and
decide.

The skill **does not run the checklist itself**. That's the
`reporting-compliance` skill's job (planned for v0.3). Conflating
the two would produce a single skill that's too long to be useful
and that fails on the upstream "which checklist?" question
silently when the inference is wrong. Keep the steps separate.

## Critical constraints — read before doing anything else

1. **Refuse on `outline` phase.** Per [[declared-work-scope]],
   no methods section yet to infer from. Refuse cleanly and
   point the author at "come back when methods is drafted, even
   as a stub describing the design".
2. **Refuse when methods is too sketchy to infer.** Confidence
   levels are honest: `low confidence — methods section is too
   sketchy to infer reliably` is the right answer when the design
   isn't clear, not a confident wrong guess. The honest default
   when uncertain is to say so.
3. **Multiple checklists can apply.** An animal randomised
   intervention study uses both ARRIVE 2.0 and CONSORT (or
   CONSORT-AI if AI-enabled). The skill must surface the
   multi-checklist case explicitly; never picks one when several
   apply.
4. **Honest about extensions and successors.** PRISMA 2020
   replaced PRISMA 2009. TRIPOD+AI 2024 supersedes TRIPOD 2015
   for AI-based prediction models. CONSORT-AI extends CONSORT
   for AI-enabled trials. The skill names the current version
   and any superseded version the author may have been planning
   to use.
5. **Never declare authoritatively.** The skill recommends; the
   author confirms. Even at high confidence, the output frames
   the inference as "the design as described points to X" rather
   than "this is a CONSORT manuscript".
6. **Do not run the full checklist.** Stop at the inference
   step. Point the author at `/scriptorium:reporting-compliance`
   (v0.3) as the next step for running the chosen checklist
   against the manuscript.
7. **Never write to MANUSCRIPT_STATE.yaml.** The schema
   deliberately does not carry a `reporting_guidelines:` field
   (declared with confidence-by-the-author is the wrong-data-
   confidently-declared failure mode for this question — the
   author often doesn't know which checklist applies, which is
   why this skill exists). The skill's output is recommendation
   prose; the author owns any downstream action.

## Inputs you should expect

**Required from `MANUSCRIPT_STATE.yaml`:**

- `document_phase.current` (load-bearing: refuse on `outline`).

**Optional from `MANUSCRIPT_STATE.yaml`:**

- `project.target_type` — confirms the work is a primary research
  manuscript (where reporting guidelines apply) vs. a review,
  thesis, white paper, etc. Most EQUATOR checklists target
  primary research; reviews use PRISMA.
- `project.target_venue` — some journals require specific
  checklists or note which they prefer; the skill mentions
  venue-specific requirements when relevant.
- `core_claims` — clarifies what's being argued, which sometimes
  disambiguates adjacent designs (a paper claiming causal
  inference vs. one claiming association).

**Required from the manuscript:**

- The **methods section** is load-bearing. Without it, the skill
  refuses (title and abstract alone are insufficient).
- The **title and abstract** add context, particularly for
  disambiguation.

**Optional:**

- The **study-design diagram** or flow diagram if present.
- Any **registration metadata** (ClinicalTrials.gov, PROSPERO,
  OSF registration) which the methods section sometimes
  references — strong signals about applicable checklists.

## The detection heuristics

The skill applies design-specific signals from the methods
section. Detection is structured and rule-based, not
opportunistic.

### CONSORT 2010 (and CONSORT-AI 2020) — RCTs

Signals: random allocation to two or more groups; allocation
concealment; intention-to-treat (or per-protocol) analysis;
participant flow diagram; trial registration. CONSORT-AI extends
when the intervention is AI-based (algorithm description, input
data handling, error analysis, human/AI interaction).

### STROBE — observational studies

Signals: no random allocation; cohort / case-control /
cross-sectional design language; "consecutive patients", "all
patients meeting criteria", or population-based sampling;
exposure-outcome framing; confounding-adjustment language. The
three design-specific arms (cohort, case-control,
cross-sectional) each have specific items.

### PRISMA 2020 — systematic reviews and meta-analyses

Signals: protocol-based literature search; database-and-search-
strategy methods; PRISMA flow diagram (or its language); PROSPERO
registration; eligibility criteria; risk-of-bias assessment;
synthesis methodology. Replaced PRISMA 2009 (still seen in some
older manuscripts).

### ARRIVE 2.0 — animal research

Signals: animal-based experiments; species/strain reporting;
housing and husbandry; sample size justification; randomisation
and blinding (the "Essential 10" tier 1); statistical methods.
ARRIVE 2.0's two priority tiers (Essential 10, Recommended Set)
matter — the skill flags which tier the manuscript is hitting.
ARRIVE often co-applies with CONSORT (animal RCTs) or with
TRIPOD (animal prediction models).

### STARD 2015 — diagnostic accuracy

Signals: index test vs. reference standard comparison;
sensitivity / specificity / predictive value reporting; ROC
analysis; participant flow from eligibility through testing.
STARD-AI extension exists for AI-based diagnostic tools.

### TRIPOD 2015 / TRIPOD+AI 2024 — prediction models

Signals: multivariable predictive model development /
validation / update; training/validation/test set language;
discrimination and calibration metrics; AUC/C-statistic. TRIPOD+AI
expanded to 27 items, unified regression and ML reporting, added
fairness and trustworthiness items. Skill recommends TRIPOD+AI
2024 over TRIPOD 2015 for new manuscripts unless venue
explicitly requires the older version.

### CARE — case reports

Signals: single-patient or small-case-series narrative;
timeline / diagnostic-process description; outcomes following
intervention; informed-consent statement specific to case
reporting.

### COREQ — qualitative research

Signals: qualitative methodology (interviews, focus groups,
observational); thematic / framework / grounded-theory
analysis; researcher reflexivity; data-saturation language.
COREQ has 32 items across research-team-and-reflexivity, study
design, and analysis-and-findings.

### CHEERS 2022 — health economic evaluations

Signals: cost-effectiveness / cost-utility / cost-benefit
analysis; QALY / DALY measurement; sensitivity analysis on
economic parameters.

### Reviews and editorials — usually no EQUATOR checklist

Signals: narrative review of literature without systematic
methodology; editorial commentary; opinion / perspective piece.
The skill names this case explicitly — "no EQUATOR checklist
applies; this is a [narrative review / editorial]" — rather
than picking a wrong checklist.

### Mixed and unclear cases

When the design genuinely spans categories (an RCT with
embedded qualitative interviews; a systematic review with a
small meta-analysis sub-component), the skill names all
applicable checklists and notes the multi-checklist
applicability is intentional, not a confusion.

## Conversational style

Read `meta.guidance_level` from `MANUSCRIPT_STATE.yaml` (default
`standard` if absent). Adapt framing per [[guidance-level]]:

- `terse` — open with one line ("running reporting-guideline-fit
  inference"); emit the markdown report; no closing summary.
- `standard` — open with one sentence naming the methods-section
  signal strength (clear / moderately clear / sketchy) and the
  count of applicable checklists; close with the recommended
  next step (`/scriptorium:reporting-compliance` against the
  chosen checklist, planned v0.3).
- `full` — open with what reporting guidelines do (standardise
  reporting so reviewers and readers can evaluate methodology
  consistently — the EQUATOR Network maintains the registry of
  ~500 active guidelines), why the inference matters (authors
  often don't know which checklist applies to their study
  design, especially across the AI-extension landscape), and
  the major design-to-checklist mapping. If first invocation
  this session, also offer
  `/scriptorium:explain reporting-guideline-fit`.

Run the signal-based check-in once if appropriate. The
structured output is unchanged across levels — only framing
changes.

## Operational protocol

1. **Read the inputs.** `MANUSCRIPT_STATE.yaml` (refuse on
   outline; note `project.target_type` and `project.target_venue`
   for context), the manuscript methods section (load-bearing —
   refuse if absent), title and abstract for disambiguation,
   any registration metadata if visible in the methods.
2. **Apply each detection heuristic** systematically (not
   opportunistic). For each guideline, check the methods
   against the detection signals; tag the match as high /
   moderate / low / no-match.
3. **Identify multi-checklist applicability.** Animal RCTs
   need ARRIVE + CONSORT. AI-based diagnostic tools need
   STARD-AI (and STARD baseline). Systematic reviews with a
   meta-analysis sub-component need PRISMA. Surface all
   applicable checklists, not just the most prominent.
4. **Confirm with high-vs-low confidence assignment.** For each
   recommended guideline:
   - **High confidence**: methods clearly describes a design
     that matches the checklist's scope. RCT with randomisation
     and allocation concealment → CONSORT high confidence.
   - **Moderate confidence**: design matches but some signals
     are ambiguous. A cohort study with non-standard
     observational structure → STROBE moderate confidence.
   - **Low confidence**: methods is sketchy or design genuinely
     unclear. Skill recommends the checklist but flags that the
     methods needs to be fleshed out before the
     reporting-compliance step is useful.
5. **Surface rejected candidates explicitly.** The "Other
   guidelines considered" section names checklists the skill
   evaluated but rejected — particularly important when the
   manuscript is on the edge between two designs (a
   non-randomised intervention study would consider both
   CONSORT and STROBE; the skill names which and why one was
   chosen).
6. **Recommend the next step.** Point the author at the v0.3
   `reporting-compliance` skill (or, while that's not yet
   built, at the EQUATOR-published checklist URL and a
   manual checklist walkthrough). Never run the checklist
   itself.
7. **Emit the structured markdown report.**

## Output format

Emit a markdown document with exactly these section headings,
in order:

```markdown
# Reporting-guideline fit

## Summary

<one paragraph: methods-section signal strength (clear /
moderately clear / sketchy); count and names of inferred
applicable guidelines; recommended next step.>

## Inferred guideline(s)

<per recommended guideline: name (with version — CONSORT 2010,
PRISMA 2020, ARRIVE 2.0, TRIPOD+AI 2024, etc.); confidence
(high / moderate / low); one paragraph naming the methods-
section signals that matched, with quotes where useful;
URL or DOI for the checklist (from EQUATOR registry); whether
an AI-extension applies and which.>

## Why this guideline (per inference)

<expanded rationale per guideline. The methods quotes from
the inferred-guideline section get expanded here with
additional context — "the methods describes random allocation
to two arms (intent-to-treat analysis named on p. 7), which
maps to CONSORT 2010 items 8-9 and 16". Useful when the
author wants to verify the inference against their own
understanding of the design.>

## Other guidelines considered

<checklists the skill evaluated and rejected, per item:
guideline name; the methods signals that initially suggested
it; the signal that ruled it out. Particularly important for
edge cases (non-randomised intervention → considered CONSORT
but rejected because allocation was not randomised; chose
STROBE instead).>

## Multi-checklist applicability

<only when more than one checklist applies. Names the
combination explicitly (animal RCT → ARRIVE 2.0 + CONSORT
2010; AI-based diagnostic → STARD 2015 + STARD-AI extension).
Notes that multi-checklist applicability is intentional, not
a confusion of the inference.>

## What the methods section needs to do

<only at moderate or low confidence. Names what's currently
sketchy or ambiguous; suggests what the author could clarify
to raise confidence. "The methods describes 'two-arm trial'
but doesn't explicitly describe randomisation method —
clarifying whether allocation was randomised (CONSORT) or
deliberately allocated (STROBE) would resolve the
ambiguity.">

## Recommended next step

<concrete: "Once you confirm the inference, run
/scriptorium:reporting-compliance with [chosen guideline] to
audit the manuscript against the checklist items. Until
reporting-compliance lands in v0.3, the EQUATOR Network
publishes the [checklist] at [URL]; a manual walkthrough is
feasible for any of the v0.1 supported checklists." Concrete
URLs where stable.>

## What this inference did NOT do

<explicit boundaries: not the full reporting-compliance audit
(this skill stops at the inference); not a declaration of
which guideline must be used (recommendation only — the
author confirms); not a study-design critique (the skill
infers from the methods as written, not whether the design
was the right choice); not editor-side enforcement.>
```

## What "good output" looks like

- **Single inferred guideline at high confidence**: methods is
  clear, design matches the checklist scope cleanly, output is
  concise (Summary + Inferred + Recommended next step
  substantive; other sections empty or brief).
- **Multi-checklist applicability surfaced explicitly**: when
  ARRIVE + CONSORT both apply, the Multi-checklist section names
  the combination and the author isn't surprised when the
  reporting-compliance step runs against both.
- **Low confidence is named cleanly**: "Methods section is too
  sketchy to discriminate between CONSORT (randomised) and
  STROBE (observational); flesh out the allocation method
  before running the reporting-compliance step" is the honest
  output when the design isn't clear.
- **Rejected candidates have rationale**: not just "considered
  STROBE", but "considered STROBE because the prose used
  'cohort' language; rejected because the methods also describes
  randomisation to two arms, which moves the design to CONSORT".
- **Version honesty**: PRISMA 2020 over PRISMA 2009; TRIPOD+AI
  2024 over TRIPOD 2015 for AI-based prediction models. The
  skill names supersession explicitly.
- **AI-extensions surfaced when applicable**: CONSORT-AI for
  AI-enabled trials; SPIRIT-AI for the protocol; TRIPOD+AI for
  AI-based prediction models; STARD-AI for AI-based diagnostic
  tools.

## What you must not do

- Run the full reporting-compliance audit (separate v0.3
  skill).
- Declare a checklist as authoritatively applicable. The skill
  recommends; the author confirms.
- Operate on outline-phase manuscripts (refuse cleanly).
- Force a confident answer when the methods is too sketchy
  to discriminate. Low confidence is honest; confident wrong
  is not.
- Write to MANUSCRIPT_STATE.yaml. The schema doesn't carry a
  `reporting_guidelines:` field (deliberately — authors often
  don't know which checklist applies, which is why this skill
  exists; declaring with confidence in state is the
  wrong-data-confidently-declared failure mode).
- Conflate the inference with the full audit. Stop at "which
  checklist?" — never start running the checklist itself.
- Recommend a checklist version that's been superseded
  (PRISMA 2009 when PRISMA 2020 is current; TRIPOD 2015 when
  TRIPOD+AI 2024 is current for AI-based prediction models).
- Run other skills as side effects.

## Grounding

This skill is grounded in published research:

- [[reporting-guidelines]] — the primary anchor. The EQUATOR
  Network registry, the design-specific checklists (CONSORT
  2010, STROBE, PRISMA 2020, ARRIVE 2.0, STARD 2015,
  TRIPOD+AI 2024, CARE, COREQ, CHEERS 2022), the AI-extension
  landscape (CONSORT-AI / SPIRIT-AI / STARD-AI / TRIPOD+AI),
  and the EQUATOR-published rationale for why standardised
  reporting matters. The skill's detection heuristics map
  directly to the design-discriminating signals each checklist
  was built to capture.
- [[declared-work-scope]] — the convention. The inference
  operates on the declared methods section; refuses cleanly
  on outline or when methods is too sketchy; does not run the
  full checklist (separate, downstream).
- [[guidance-level]] — the framing-level convention.

This skill is the **upstream inference** in the
reporting-guidelines workflow; the v0.3 `reporting-compliance`
skill (planned) is the downstream checklist runner. The two are
deliberately separate — conflating them produces a skill that's
too long, and that fails silently on the inference step when
it's wrong.

## See also

- `/scriptorium:reporting-compliance` (planned v0.3) — the
  downstream skill that runs the inferred checklist against
  the manuscript. Natural follow-on.
- `/scriptorium:reviewer-simulation` — pairs naturally before
  submission. Reviewers at high-tier journals check
  reporting-guideline compliance; running both before
  submission catches both content and reporting issues.
- `/scriptorium:desk-rejection-risk` — pairs naturally when
  `target_venue` is set. Some venues desk-reject manuscripts
  that don't meet their required reporting guideline.
- `/scriptorium:explain reporting-guideline-fit` — full design
  tour.
