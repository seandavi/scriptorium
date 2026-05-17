# Sample input — reviewer-simulation

A synthetic manuscript abstract + a short discussion paragraph,
designed to surface critiques under multiple lenses.

---

## Abstract

**Background.** Bariatric surgery is increasingly used in patients with
type 2 diabetes (T2D), but predictors of durable diabetes remission
remain unclear. **Methods.** We retrospectively analyzed 287 patients
who underwent Roux-en-Y gastric bypass at a single academic center
between 2018 and 2023. Diabetes remission was defined as HbA1c <6.5%
off all glucose-lowering medication for ≥12 months. We built a logistic
regression model with pre-operative HbA1c, BMI, diabetes duration,
C-peptide, and age as predictors. **Results.** Remission was achieved
in 64% of patients at 24 months. Shorter diabetes duration (<5 years)
and lower pre-op HbA1c were independent predictors (p<0.001 each).
A 5-variable model achieved AUC=0.79 in the development cohort.
**Conclusions.** Our model can be used to predict diabetes remission
after bariatric surgery and should be incorporated into pre-operative
counseling.

---

## Discussion (excerpt)

Our findings extend the existing literature on bariatric-surgery
outcomes [@thompson2021]. The single most important predictor in our
model was diabetes duration, consistent with the hypothesis that
β-cell reserve declines monotonically with disease duration. Patients
with diabetes duration <5 years had remission rates exceeding 80%,
supporting earlier referral to surgery in this population. The
model's discrimination (AUC=0.79) compares favorably to previously
published scores [@kim2019].

The clinical implications are substantial. Earlier referral for
bariatric surgery in T2D patients could prevent decades of
microvascular complications. Insurers should consider covering
surgery within 5 years of T2D diagnosis based on these findings.

---

## MANUSCRIPT_STATE.yaml

```yaml
project:
  title: "Predicting diabetes remission after Roux-en-Y gastric bypass: a single-center retrospective cohort study"
  target_type: manuscript
  target_venue: "Diabetes Care"
  source_format: markdown

document_phase:
  current: review
  submission_target_date: "2026-08-01"

core_claims:
  - "Shorter diabetes duration and lower pre-operative HbA1c predict diabetes remission after Roux-en-Y gastric bypass."
  - "A five-variable model achieves AUC=0.79 for predicting 24-month remission."
  - "Earlier surgical referral in T2D patients may improve remission rates."

known_weaknesses:
  - "Single-center retrospective design limits generalizability."
  - "No external validation cohort."

terminology:
  preferred: ["Roux-en-Y gastric bypass", "type 2 diabetes (T2D)"]
  forbidden: ["cure", "very", "highly significant"]

style:
  tone: ["quantitative", "restrained"]
  voice: active
  audience: "clinical endocrinologists and bariatric surgeons"

constraints:
  preserve_citations: true
  preserve_statistics: true
  avoid_hype: true

bibliography:
  paths: ["references.bib"]
  format: bibtex
```

## What this snippet is designed to surface

A well-tuned reviewer-simulation pass should flag:

- **Statistical:** sample size for 5-variable model relative to events; missing internal validation (bootstrap, cross-validation); no calibration discussed; TRIPOD reporting guideline likely not followed.
- **Methodological skeptic:** single-center retrospective design (already in `known_weaknesses` — should be noted as acknowledged); no information on missing data handling; selection bias for patients reaching 24-month follow-up.
- **Translational / clinical:** "should be incorporated into pre-operative counseling" overclaims without external validation; insurer-coverage recommendation goes well beyond what an unvalidated single-center model can support; absent external validation cohort is acknowledged but the recommendation language doesn't reflect that.
- **Domain expert:** the comparison to "previously published scores [@kim2019]" is sparse — no discussion of how the present model improves on or differs from prior work; the duration-monotonicity hypothesis is asserted without nuance about confounding by treatment history.
- **Enthusiasm drivers:** clinically important problem; restrained tone in MANUSCRIPT_STATE; appropriate variable selection given the outcome.
