---
title: Case study — bariatric-surgery discussion paragraph
description: A worked end-to-end example of citation-audit + reviewer-simulation + argumentative-flow on a realistic biomedical discussion paragraph.
sidebar:
  order: 20
---

This page works one realistic manuscript paragraph through three
scriptorium skills — `citation-audit`, `reviewer-simulation`, and
`argumentative-flow` — and shows the before, the structured output,
and the after. It exists because the most common question we get
about scriptorium is "what does the actual output look like?" — the
abstract category labels in [DESIGN.md](/concepts/design/) only get
you so far.

The manuscript below is **constructed**, not real. It is a plausible
single-center retrospective cohort study of bariatric surgery
outcomes in type 2 diabetes, written specifically to exercise the
skills — every flagged issue corresponds to a critique pattern the
relevant skill is grounded in (and that we have seen in the wild on
real manuscripts). When we have permission to publish a worked
example on a real manuscript, this page will be replaced; for now,
the example is a transparency device, not a proof of capability.

The corresponding `MANUSCRIPT_STATE.yaml` for this paragraph lives
at [`skills/reviewer-simulation/examples/sample-input.md`](https://github.com/seandavi/scriptorium/blob/main/skills/reviewer-simulation/examples/sample-input.md).

## Step 0: the manuscript paragraph

The paragraph in question — a discussion-section excerpt:

> Our findings extend the existing literature on bariatric-surgery
> outcomes [@thompson2021]. The single most important predictor in
> our model was diabetes duration, consistent with the hypothesis
> that β-cell reserve declines monotonically with disease duration.
> Patients with diabetes duration <5 years had remission rates
> exceeding 80%, supporting earlier referral to surgery in this
> population. The model's discrimination (AUC=0.79) compares
> favorably to previously published scores [@kim2019].
>
> The clinical implications are substantial. Earlier referral for
> bariatric surgery in T2D patients could prevent decades of
> microvascular complications. Insurers should consider covering
> surgery within 5 years of T2D diagnosis based on these findings.

The author has already declared, in `MANUSCRIPT_STATE.yaml`:

```yaml
core_claims:
  - "Shorter diabetes duration and lower pre-operative HbA1c predict
     diabetes remission after Roux-en-Y gastric bypass."
  - "A five-variable model achieves AUC=0.79 for predicting 24-month
     remission."
  - "Earlier surgical referral in T2D patients may improve remission
     rates."

known_weaknesses:                # see schema-note caveat below
  - "Single-center retrospective design limits generalizability."
  - "No external validation cohort."
```

The `known_weaknesses` field is the author's record of limitations
they have already chosen to disclose — every skill below reads it.
See the [schema reference](/reference/manuscript-state-schema/#a-note-on-known_weaknesses)
for why the name is under review.

## Step 1: `citation-audit` — claim-by-claim assessment

`citation-audit` reads the paragraph and the bibliography and
returns a structured table. No citations are added. No prose is
modified. This is what the author sees:

| Claim | Citation | Strength | Assessment | Recommendation |
|---|---|---|---|---|
| "Our findings extend the existing literature on bariatric-surgery outcomes." | `[@thompson2021]` | Weak fit | `thompson2021` is a *narrative review* of bariatric-surgery outcomes broadly; it does not address the duration-based predictor pattern the paragraph claims to extend. | Either cite a primary cohort study that reported diabetes-duration effects on remission, or soften the framing to "consistent with prior reviews" with the review citation retained. |
| "β-cell reserve declines monotonically with disease duration." | (none) | Unsupported | The hypothesis is asserted without citation. The β-cell-reserve literature is established but heterogeneous — UKPDS legacy data, the DiRECT trial substudies, and the Saisho-group histology work all support a *general* monotonic pattern but with substantial individual variation. | Add a primary citation (UKPDS or a histology study); change "monotonically" to "with disease duration" to avoid asserting strict monotonicity, which is stronger than the cited evidence supports. |
| "AUC=0.79 compares favorably to previously published scores." | `[@kim2019]` | Partial fit | `kim2019` reports AUC=0.74 for a comparable model — the comparison is real, but "compares favorably" without naming the comparison value lets the reader infer a bigger gap than 0.05. | State the comparison value explicitly: "AUC=0.79, compared to 0.74 reported by Kim et al. [@kim2019]". |
| "Earlier referral for bariatric surgery in T2D patients could prevent decades of microvascular complications." | (none) | Causal overreach | This is a strong causal claim about long-horizon clinical outcomes drawn from a 24-month retrospective single-center cohort. The author's own `known_weaknesses` flags both the design and the absence of external validation. | Either downgrade ("may reduce the risk of …") or pair with a citation to a long-horizon outcome study; do not assert the causal chain from a single 24-month cohort. |
| "Insurers should consider covering surgery within 5 years of T2D diagnosis based on these findings." | (none) | Policy claim outside data | A policy recommendation requires evidence the paper does not contain (cost-effectiveness, external validation, generalisability across surgical centers). The single-center retrospective design is acknowledged in `known_weaknesses` but the policy claim is not calibrated to that limitation. | Remove the policy recommendation, or move it to a clearly-labelled "Future implications" subsection with explicit reference to what would need to be established first. |

`citation-audit` does not modify the paragraph; it surfaces what it
sees. Whether to fix any of these is the author's call.

## Step 2: `reviewer-simulation` — four-lens pressure test

`reviewer-simulation` runs the same paragraph through four
attentional lenses. Each lens emits the same six-section structure:
Major Critiques / Minor Critiques / Fatal Concerns / Enthusiasm
Drivers / Suggested Revisions / Acceptance Risk. The point is to
show what would land if the author submitted as-is.

The output below shows each lens emitting concrete, anchored
critiques — not framing attacks, not vague "your narrative is
unconvincing" prose. Each finding names the specific section,
sentence, or table cell the critique applies to.

### Methodological skeptic

**Major critiques.**

- The single-center retrospective design is acknowledged in
  `known_weaknesses` and so is not flagged as a fatal concern — but
  the discussion paragraph does not propagate that limitation into
  its causal claims. The last sentence's microvascular-complications
  language reads as a prospective conclusion the data cannot
  support.
- Missing-data handling is not described in Methods §2.3. With a
  retrospective cohort of n=287 and a 5-variable model, the imputation
  strategy (or complete-case rationale) is load-bearing — please
  describe.
- Selection bias for patients reaching the 24-month outcome window
  is not addressed. What fraction of the original cohort had
  sufficient follow-up to be included, and how does loss-to-follow-up
  distribute across the predictors?

**Minor critiques.**

- The phrase "single most important predictor" needs a numerical
  anchor (standardised coefficient, or a sensitivity analysis with
  the predictor removed).

**Fatal concerns.** None at this stage.

**Enthusiasm drivers.** Restrained tone in the stated MANUSCRIPT_STATE;
clinically important question; the duration-based predictor is
biologically plausible.

**Acceptance risk.** Moderate. Methodological transparency edits
unlock this.

### Domain expert

**Major critiques.**

- The "β-cell reserve declines monotonically" hypothesis is too
  strong. The bariatric literature distinguishes baseline β-cell
  function (C-peptide trajectory) from the disease-duration proxy;
  conflating them oversimplifies a contested mechanism. Please
  separate the disease-duration finding (which the data support)
  from the β-cell-reserve interpretation (which is downstream).
- The comparison to `kim2019` is asserted, not characterised — what
  population, what surgical procedure, what remission definition,
  what time horizon? The reader needs to know whether AUC=0.79 vs
  0.74 is comparing models on like data or unlike data.

**Minor critiques.**

- "Bariatric-surgery outcomes" in sentence 1 is unspecific. The
  cohort is Roux-en-Y gastric bypass only; if the discussion is
  limited to RYGB the framing should match.

**Fatal concerns.** None.

**Enthusiasm drivers.** The question is real; the predictor set is
clinically tractable.

**Acceptance risk.** Moderate. Domain-specific precision edits.

### Translational / clinical

**Major critiques.**

- "Insurers should consider covering surgery within 5 years of T2D
  diagnosis based on these findings" overreaches by ~one
  evidence-grade: a single-center retrospective 24-month outcome is
  not the kind of evidence on which payer-coverage recommendations
  are based. Please soften, or pair with an explicit framing of what
  the next steps would be (multicenter validation, cost-effectiveness
  analysis).
- "Earlier referral … could prevent decades of microvascular
  complications" is a 30-year-horizon claim drawn from a 24-month
  cohort. The verb "could" reads as conditional but the sentence
  structure presents it as a clinical implication. Please rework so
  the time-horizon mismatch is visible.

**Minor critiques.**

- An external validation cohort is acknowledged as missing in
  `known_weaknesses`; the discussion should explicitly route the
  policy-implication paragraph through that limitation.

**Fatal concerns.** None — the issues are calibration, not data
integrity.

**Enthusiasm drivers.** Genuine clinical relevance.

**Acceptance risk.** Moderate-to-high before edits; the policy
overreach is the kind of sentence a careful reviewer or editor will
push back on at desk-review.

### Statistical

**Major critiques.**

- Sample size for a 5-variable model with a binary outcome and an
  event rate of 64% (n_events ≈ 184) yields ~37 events per
  predictor — adequate by EPV ≥ 10 heuristic, but the model
  validation discussion is missing. Please report internal
  validation (bootstrap optimism, k-fold CV) and model calibration
  (Hosmer-Lemeshow, calibration plot, or calibration-in-the-large).
- "AUC=0.79" without confidence intervals or calibration is
  under-reported. Please add the 95% CI for the AUC.

**Minor critiques.**

- "Statistically significant" appears with no effect size for
  diabetes duration. Please report the OR with 95% CI alongside the
  p-value.

**Fatal concerns.** None.

**Enthusiasm drivers.** EPV is in a defensible range; the predictor
selection is principled.

**Acceptance risk.** Moderate. Most of these are easy edits — they
just need to be made before submission. None of them is a "this
paper is bad" critique; each one is a fixable bench/stats task that
strengthens the paper.

## Step 3: `argumentative-flow` on the second sub-paragraph

The first paragraph is in reasonable shape. The second sub-paragraph
("The clinical implications are substantial. …") is the one with
the calibration problem the reviewer simulation flagged. The author
invokes `argumentative-flow` on it.

`argumentative-flow` is the only transformation skill in the workflow
above. It modifies prose, under a preservation contract: every
citation is preserved, every quantitative statement is preserved,
declared terminology is preserved, and the author's hedging stance
is honoured. The skill's output includes a structural diagnosis, a
proposed outline, the revised prose, a diff against the source, and
a "Remaining weaknesses" section listing problems it did not solve.

### Structural diagnosis (what the skill saw)

The sub-paragraph asserts a clinical implication (sentence 2) and a
policy recommendation (sentence 3) on top of a one-sentence claim
("The clinical implications are substantial") that does not yet say
what those implications are. The reader is asked to accept the
implications before they are named, and the policy recommendation
arrives without the calibration step that would link it back to the
study design. The declared `known_weaknesses` items (single-center,
no external validation) are not surfaced in the prose.

### Revised prose

> The clinical implications follow from the duration finding.
> Patients with diabetes duration <5 years had remission rates
> exceeding 80% in our cohort — a magnitude consistent with the
> shorter-duration arm of prior bariatric-surgery cohorts
> [@thompson2021], and one that supports earlier evaluation for
> surgery in this population. Whether this finding generalises to
> other centers, surgical procedures, or longer outcome horizons
> remains open: our cohort is single-center, retrospective, and
> tracked to 24 months. Multicenter validation would be required
> before the duration cutoff could inform payer-coverage policy.

### Diff against source (preservation report)

- **Citations.** `[@thompson2021]` retained. No citations added; no
  citations dropped.
- **Statistics.** "80%" remission rate preserved; AUC=0.79 not in
  this sub-paragraph, untouched. No quantitative values changed.
- **Terminology.** "Roux-en-Y gastric bypass" was not in this
  sub-paragraph; "bariatric surgery" / "surgery" retained as the
  source paragraph used. `MANUSCRIPT_STATE.yaml#terminology.preferred`
  honoured.
- **Hedging.** Source used "could prevent decades of microvascular
  complications" (strongly causal) and "Insurers should consider …"
  (policy-prescriptive). The revision routes both through
  `known_weaknesses` — the conditional language ("whether this
  finding generalises … remains open"; "Multicenter validation would
  be required before …") matches the declared limitations. This is
  a deliberate hedging shift the author should review.
- **Voice.** Source voice was active. Revision is active. No passive
  reframing.
- **Sentence count.** Three sentences → four sentences. The added
  sentence is the validation-required clause; it surfaces a declared
  weakness rather than introducing a new claim.

### Remaining weaknesses

- The revised paragraph still does not name *which* prior cohort
  studies support the shorter-duration finding. `citation-audit`
  flagged `thompson2021` as a review rather than a primary study;
  the citation choice is left for the author to revisit.
- The phrase "evaluation for surgery" is intentionally vague (the
  source used "referral"); the author may want to choose between
  "evaluation," "referral," and "consultation" based on the
  specialty audience.
- The β-cell-reserve hypothesis remains in the prior sub-paragraph
  and was not touched by this run.

## Why each step earned its place

This is what the author actually gets out of the run, not what the
catalog page describes in the abstract:

- `citation-audit` flagged the **`thompson2021` mismatch** —
  citing a review for what reads like a primary-cohort claim. A
  careful human reader skimming the discussion would not
  necessarily catch this; the skill catches it because the
  reference type is checkable.
- `reviewer-simulation` flagged the **policy-implication
  overreach** — a 30-year-horizon claim from a 24-month cohort.
  This is the kind of sentence a careful reviewer would flag at
  desk review; surfacing it before submission lets the author
  rewrite once rather than twice.
- `argumentative-flow` made the **declared `known_weaknesses` items
  visible in the prose** — the rewrite routes the policy implication
  through the single-center, no-external-validation limitations the
  author has already chosen to acknowledge. The author owns whether
  to accept the rewrite; the skill preserves citations, statistics,
  and the author's terminology while doing it.

The skills are read-mostly and conservative by design. None of them
graded the paragraph. None of them produced an overall score. None
of them said the paper is bad. What they did was anchor each finding
to a specific sentence and explain the call.
