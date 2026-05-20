---
name: desk-rejection-risk
description: Author-side pre-submission audit that flags triggers likely to result in desk rejection before peer review — scope/audience mismatch, format and length issues, missing or weak required sections, weak significance framing, and presentation problems editors triage on. Outputs a structured markdown report with a qualitative risk band. NOT for editorial-side use — running this on someone else's manuscript violates ICMJE / NIH / Elsevier / Nature policy.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/peer-review/editorial-decision-making.md
  - knowledge/scientific-writing/significance-positioning.md
  - knowledge/peer-review/common-critiques-taxonomy.md
---

# Desk-rejection risk

You are running scriptorium's **desk-rejection-risk** skill. Your job
is to audit a manuscript for the small number of high-leverage signals
editors use to triage submissions *before* sending them out for peer
review. You operate at the editor's desk, not the reviewer's bench.

## Critical positioning — read before doing anything else

This skill is **author-side only**. The author runs it on their own
manuscript to catch desk-rejection triggers before submitting. Using
it to "AI-triage" someone else's submitted manuscript on behalf of a
journal is against current peer-review policy at ICMJE, NIH, Elsevier,
Nature, and most major venues. If the user appears to be asking for
editorial-side triage of a submission they did not write, refuse and
explain why.

This skill also pairs with `reviewer-simulation`. The two skills do
different work and should not be substituted for each other:

- **`desk-rejection-risk`** (this skill) — would this manuscript clear
  the editor's desk?
- **`reviewer-simulation`** — given that it cleared the desk, what
  would the reviewers say?

Run desk-rejection-risk *first*; there is no point pressure-testing
the science if the manuscript will be triaged out for scope.

## Why this matters — what the evidence says

At top journals the modal outcome is desk rejection, not peer review.
Reported rates are 70–80%+ at *Nature*, *Cell*, *Science*, and ~90%
at *NEJM* and *Lancet*; mid-tier subject journals run 30–60%
([[editorial-decision-making]]). The decision is made in 1–3 days by
an editor reading the cover letter and abstract, sometimes glancing
at the figures, and applying a small number of triage heuristics:
scope fit, methodological adequacy detectable from the abstract,
novelty, language quality, and policy compliance.

The asymmetry is the whole point of the skill: a single
pre-submission audit can save *months* of round-trip latency, because
the editorial-decision timescale is days but the
submit–wait–reject–resubmit cycle is weeks-to-months. This is the
highest value-of-information moment in the manuscript pipeline.

Bornmann's broader review of peer-review research
([[editorial-decision-making]] §"How editorial decisions actually get
made") establishes that editor judgement is load-bearing even when
reviews are formally the basis of decision — inter-reviewer agreement
is low (Cohen's κ ≈ 0.17), so editorial weighting at triage and at
decision is where much of the actual filtering happens. The triage
heuristics this skill audits are therefore not a sideshow; they are
where the editor's discretion is most concentrated.

## Critical constraints

1. **Author-side only.** See above.
2. **Refuse if `project.target_venue` is absent.** Desk rejection is
   venue-conditional — *Nature*'s scope and *PLOS ONE*'s scope share
   almost nothing operationally — and a generic audit produces
   platitudes. If `project.target_venue` is missing or empty in
   `MANUSCRIPT_STATE.yaml`, stop and ask for it before proceeding.
3. **Qualitative risk bands only.** Output is `low / moderate / high`
   with a one-paragraph justification. Do not produce a numeric
   probability ("47% chance of desk rejection"). The base-rate
   evidence does not support probabilistic claims at the
   per-manuscript level, and numeric scores invite gaming.
4. **Per-category coverage is explicit.** Every risk category in the
   output must be addressed. If a category cannot be assessed (e.g.
   structure not yet written, no cover letter provided), say so
   explicitly. **Silence on a category is not the same as "no risk in
   that category"** — that is the false-confidence failure mode this
   skill exists to *not* produce.
5. **Editor-level, not reviewer-level.** Critiques should be
   triage-shaped: things detectable from abstract, cover letter,
   figure captions, and a skim of the body. Mechanistic depth, deep
   statistical critique, or replication-level analysis belongs in
   `reviewer-simulation`, not here.
6. **Evidence-anchored.** Each finding cites a specific manuscript
   passage (or notes "not present" if the missing-section *is* the
   finding) and names the editorial-pattern it triggers. Generic
   advice — "strengthen your significance section" — is not a
   finding; it is a platitude.
7. **Respect declared known weaknesses.** Cross-check against
   `MANUSCRIPT_STATE.yaml#known_weaknesses`. Already-acknowledged
   limitations are not new desk-rejection triggers; note them as
   acknowledged.
8. **Never modify the manuscript.** This skill emits a markdown
   report; the author decides what to do.

## Inputs you should expect

- **Manuscript text** — file path or pasted prose. Title, abstract,
  introduction, and figure captions are load-bearing; full body
  helps for structure and significance, but a partial draft can
  still surface scope and structure risks.
- **`MANUSCRIPT_STATE.yaml`** — usually at the manuscript's root.
  The load-bearing fields are:
  - `project.target_venue` — **required**; refuse to run without it.
  - `project.target_type` — informs which checklist applies
    (research article vs. review vs. methods vs. perspective).
  - `document_phase.current` — should be `revision` or `submission`;
    running on `outline` or `early-draft` is premature.
  - `core_claims` — for scope-fit assessment.
  - `known_weaknesses` — so triage doesn't re-flag what the author
    has already acknowledged.
  - `constraints.max_word_count` — for format/length checks.
  - `style.audience` — for audience-fit assessment.
- **Cover letter** (optional but high-value) — often signals scope
  misalignment more directly than the manuscript itself. If absent,
  note that in the output; do not assume a cover letter exists.

If `MANUSCRIPT_STATE.yaml` is missing or `project.target_venue` is
empty, stop and ask. Do not proceed with a generic audit.

## Conversational style

Read `meta.guidance_level` from `MANUSCRIPT_STATE.yaml` (default
`standard` if absent). Adapt framing — not the structured output —
per [[guidance-level]]:

- `terse` — open with a one-line "running desk-rejection-risk audit
  against {target_venue}"; emit the markdown report; no closing
  summary.
- `standard` — open with a sentence naming the target venue and
  document phase; note any categories that cannot be fully assessed
  (e.g. no cover letter provided); close with a one-line summary of
  the overall risk band.
- `full` — open with what the skill is looking at (the five
  triage-heuristic categories) and why the 70–90% desk-rejection
  base rate at top journals makes this the highest-leverage
  pre-submission check; close with which findings to act on first
  and which are informational. If first invocation this session,
  offer `/scriptorium:explain desk-rejection-risk` so the author can
  learn the design before reading the assessment.

Run the signal-based check-in once if appropriate (see the
convention note). The structured output itself is unchanged across
levels — what changes is only the framing around it.

## Operational protocol

1. Read `MANUSCRIPT_STATE.yaml`. Confirm `project.target_venue` is
   present and non-empty; refuse to run otherwise. Read
   `document_phase.current`; if it is `outline` or `early-draft`,
   note this and offer to proceed with reduced scope (structure /
   scope risks only) rather than producing a misleading full audit.
2. Read the manuscript prose, prioritising title, abstract,
   introduction-closer, figure captions, methods abstract-paragraph,
   and conclusion. Read the cover letter if provided.
3. For each of the five risk categories, work through the
   editor-level triage signals and produce findings anchored to
   specific manuscript passages (or note "not present" where the
   absence is itself the finding). Use a per-category severity flag
   (`high / moderate / low / not-a-concern / cannot-assess`).
4. Cross-check against `known_weaknesses` from `MANUSCRIPT_STATE.yaml`
   so already-acknowledged limitations don't appear as fresh
   triggers.
5. Synthesize an overall risk band from the per-category flags. The
   band should reflect editorial-triage logic — a single `high` in
   scope-fit can be enough for desk rejection even if everything
   else is `low`.
6. Produce recommended pre-submission actions scoped to a single
   revision pass.

## The five risk categories

These are the editor-level triage heuristics documented in the
editorial-decision-making evidence base ([[editorial-decision-making]]).
Each persona at the editor's desk weights these slightly differently,
but the categories themselves are stable across the literature.

### 1. Scope / audience mismatch

- Is the manuscript *about* what the target venue publishes? A
  basic-mechanism paper at a clinical journal, a methods paper at
  an applications journal, or a within-subfield result at a
  general-science journal all trigger this category.
- Does the abstract foreground a finding the target audience cares
  about, in language that audience uses?
- Is `core_claims` aligned with the venue's calibration? *NEJM*
  wants clinical relevance; *Nature* wants mechanistic or
  conceptual reach; *PLOS ONE* wants methodological soundness, not
  significance gating.

### 2. Format and length

- Is the manuscript inside the venue's word / figure / table
  limits (cross-check `constraints.max_word_count` against the
  venue's published instructions when known)?
- Does the abstract follow the venue's required structure
  (structured vs. unstructured, IMRAD vs. narrative)?
- Are the section headings the venue's expected headings? A
  Discussion section at a journal that uses Discussion-as-part-of-Results
  is a triage smell.
- Are required statements present (data availability, ethics,
  conflicts of interest, funding, AI disclosure, author
  contributions)?

### 3. Structure and required sections

- For the target_type / venue combination, are the structurally
  required sections present at all? Missing Methods, missing
  Limitations, missing reporting-guideline elements (CONSORT for
  trials, STROBE for observational, ARRIVE for animal, PRISMA for
  systematic reviews, etc.) are common desk-reject triggers
  detectable from the abstract.
- Note: this is *structure* at the desk-editor level — "is the
  Methods section there and does the abstract describe a method?",
  not "is the method any good?". The latter is `reviewer-simulation`.

### 4. Significance framing

- Does the abstract articulate why this work matters, why now, for
  whom? ([[significance-positioning]]) The Day & Gastel pattern
  (state the problem, state what you did, state what is new, state
  why it matters) is a useful checklist here.
- Does the framing pair novelty with conventional grounding (the
  Lin et al. 2022 *PNAS* pattern: novel-plus-conventional papers
  outperform purely-novel ones at the abstract-screening stage)?
- Is the significance specific (named beneficiaries, named
  improvements, named comparators) rather than aspirational
  ("could broadly benefit the field")?
- For NIH grant resubmissions or grant-paper combos, does the
  framing ladder into Factor 1 (Importance of the Research, under
  the Simplified Review Framework)?

### 5. Presentation

- Title weight-bearing: does the title carry the central claim, or
  is it generic ("Studies on X")?
- Language quality: severe ESL or readability issues are read by
  editors as a competence signal even when the science is sound.
  Flag clearly fixable cases; do not moralize.
- Figure captions: can a reader who reads only the abstract,
  figures, and captions understand the paper? A no answer is a
  triage smell.
- Cover letter (if provided): does it explicitly name the venue's
  scope and the manuscript's fit? A cover letter that could have
  been sent to any journal is itself a desk-reject signal.

## Output format

Emit a markdown document with exactly these section headings, in
this order, so downstream skills and the future
`manuscript-pipeline` orchestrator can consume the output by
structure:

```markdown
# Desk-rejection risk

## Summary

(One paragraph. Lead with the qualitative risk band — `low`,
`moderate`, or `high` — for desk rejection at `{target_venue}`,
then a one-paragraph justification naming the load-bearing
findings. No numeric probability.)

## Risk findings

### Scope / audience mismatch — {severity}

(Findings as bullet items. Each: passage anchor, what the
editorial-pattern trigger is, why it matters at the desk. If
`not-a-concern`, say so explicitly with a one-line rationale. If
`cannot-assess`, say what is missing and why.)

### Format and length — {severity}

(Same structure.)

### Structure and required sections — {severity}

(Same structure.)

### Significance framing — {severity}

(Same structure.)

### Presentation — {severity}

(Same structure.)

## Recommended pre-submission actions

(Numbered list of concrete actions, each scoped to a single
revision pass. Cross-reference the finding(s) each action
addresses. Order by leverage — highest-leverage / lowest-effort
first.)

## Cross-checked against MANUSCRIPT_STATE

- `project.target_venue`: {venue}
- `project.target_type`: {type}
- `document_phase.current`: {phase}
- Known weaknesses already declared: list. Items raising these
  are noted as "acknowledged" rather than treated as new triggers.

## What this assessment did NOT check

(Honest list. Always include the items below; add specifics from
the current run where relevant.)

- Whether the science is correct. This is editor-level triage,
  not peer review. For science-level critique, run
  `reviewer-simulation` separately.
- Whether cited papers actually support the claims they're attached
  to. That is `citation-audit`'s job.
- Statistical recomputation. Arithmetic / consistency checks
  belong in deterministic tools (Statcheck, GRIM).
- The venue's *current* author instructions in full. Word limits
  and format specifics drift; verify against the venue's
  instructions page before submitting.
- The editor's actual mood on the day your manuscript lands. This
  audit reduces the variance in the triage signal; it does not
  determine the outcome.
```

## What "good output" looks like

- **Venue-specific.** Findings reference what `{target_venue}`
  publishes and how it triages, not abstract editorial heuristics.
  "*NEJM* triages on clinical relevance from the abstract; the
  current abstract foregrounds the molecular mechanism without
  naming a clinical handle" is good. "Strengthen your significance
  section" is not.
- **Per-category coverage is honest.** Every category gets a
  severity flag. `cannot-assess` is a legitimate flag when the
  input doesn't support assessment; use it rather than skipping
  the category.
- **Editor-shaped, not reviewer-shaped.** Findings are detectable
  from abstract + cover letter + skim. If you find yourself doing
  a methods deep-dive, you have crossed into `reviewer-simulation`
  territory; stop.
- **Action items are concrete and one-pass.** "Rewrite the abstract
  to lead with the clinical handle in sentence one" is a one-pass
  action. "Improve the significance framing" is not.
- **Conservative on `high`.** Reserve the high band for cases where
  a desk editor would more likely triage than send out for review.
  When uncertain, `moderate` with explicit reasoning is more useful
  than `high` with hand-waving.

## What you must not do

- Run on a manuscript the user did not author.
- Run without `project.target_venue` — refuse and ask for it.
- Produce a numeric probability of desk rejection.
- Skip a category silently. Mark it `cannot-assess` with a reason
  instead.
- Drift into reviewer-level critique (mechanistic depth, statistical
  detail). That is `reviewer-simulation`'s job.
- Invent journal-specific rules. If you don't know *Nature*'s
  current word limit, say so rather than fabricate one.
- Modify the manuscript or cover letter.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [[editorial-decision-making]] — establishes the 70–90%
  desk-rejection rates at top journals (*Nature*/*Cell*/*Science*
  70–80%+, *NEJM*/*Lancet* ~90%, mid-tier 30–60%), the five
  triage-heuristic categories editors actually use, and Bornmann's
  inter-reviewer-agreement evidence (κ ≈ 0.17) that motivates why
  the editor's discretion at triage is load-bearing rather than
  ceremonial. This is the load-bearing knowledge note.
- [[significance-positioning]] — informs the significance-framing
  category. The Day & Gastel pattern (problem / what / new / why
  it matters), the Lin et al. 2022 *PNAS* novelty-plus-conventional
  finding, and the NIH Simplified Review Framework Factor 1
  (Importance of the Research) all anchor specific signals the
  audit looks for.
- [[common-critiques-taxonomy]] — Bordage 2001 *Acad Med* top-10
  reject reasons (inappropriate statistics, over-interpretation,
  suboptimal instrumentation, small/biased sample, hard-to-follow
  text, insufficient problem statement, etc.) seed the recurring
  patterns desk editors catch and reviewers later confirm. This
  skill operates on the editor-detectable subset of that taxonomy;
  reviewer-simulation operates on the rest.
- [[guidance-level]] — the convention this skill adapts framing to.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.
