# reporting-guideline-fit — infer which EQUATOR checklist applies

Reads the manuscript's methods section and infers which EQUATOR
Network reporting guideline applies — CONSORT 2010, STROBE,
PRISMA 2020, ARRIVE 2.0, TRIPOD/TRIPOD+AI 2024, STARD 2015, CARE,
COREQ, CHEERS 2022, plus AI-extensions (CONSORT-AI, SPIRIT-AI,
STARD-AI, TRIPOD+AI) where applicable.

This is the **upstream inference** in the reporting-guidelines
workflow. Stops at "which checklist?"; the downstream
`reporting-guideline-compliance` skill (planned v0.3) runs the full
checklist against the manuscript.

## When to invoke

- The author asks "which reporting checklist applies to my
  study?"
- Before running the downstream `reporting-guideline-compliance` audit
  (v0.3) and the right checklist isn't yet known.
- The author is on the edge between two adjacent designs
  (non-randomised intervention → CONSORT or STROBE?) and wants
  a methods-anchored recommendation.

## Why this is a skill, not a schema field

The originally-planned `reporting_guidelines:` MANUSCRIPT_STATE
field was dropped because authors often don't know which EQUATOR
checklist applies to their study design — there are dozens,
with extensions and AI-specific variants, and the discrimination
between adjacent designs (RCT vs. cohort; PRISMA vs. scoping
review) needs the methods in hand. A schema field that the
author declares with confidence on first run is the
**wrong-data-confidently-declared** failure mode for this
question.

So: infer from the methods (this skill), confirm with the author,
optionally cache as a downstream input. The schema doesn't carry
the cache field by default — the inference can re-run.

## Three honesty disciplines

The skill takes a stand on three forms of honesty:

1. **Confidence levels are honest.** Low confidence is the
   right answer when the methods is too sketchy to
   discriminate, not a confident wrong guess.
2. **Multi-checklist applicability is surfaced.** An animal
   randomised intervention study uses ARRIVE + CONSORT (or
   CONSORT-AI). The skill never picks one when several apply.
3. **Versioning is honest.** PRISMA 2020 over PRISMA 2009;
   TRIPOD+AI 2024 over TRIPOD 2015 for AI-based prediction
   models. The skill names supersession explicitly when
   relevant.

## What it explicitly will not do

- Run the full reporting-guideline-compliance audit (that's the
  downstream v0.3 skill).
- Declare a checklist as authoritatively applicable.
  Recommendation only — the author confirms.
- Operate on outline-phase manuscripts (no methods to infer
  from).
- Force a confident answer when methods is too sketchy.
- Write to MANUSCRIPT_STATE.yaml.
- Critique study design (the skill infers from the methods as
  written, not whether the design was the right choice).
- Editor-side enforcement. Author-side decision support only.

## Grounding

Primarily grounded in
[`knowledge/scientific-writing/reporting-guidelines.md`](../../knowledge/scientific-writing/reporting-guidelines.md)
— the EQUATOR Network registry, design-specific checklists
(CONSORT 2010, STROBE, PRISMA 2020, ARRIVE 2.0, STARD 2015,
TRIPOD+AI 2024, CARE, COREQ, CHEERS 2022), the AI-extension
landscape (CONSORT-AI/SPIRIT-AI 2020, TRIPOD+AI 2024,
STARD-AI), and the rationale for why standardised reporting
matters.

## See also

- [`SKILL.md`](SKILL.md) — full Claude Code skill (operational
  protocol, output template, hard constraints).
- [`prompt.md`](prompt.md) — platform-neutral version.
- [`manifest.yaml`](manifest.yaml) — machine-readable metadata.
- `/scriptorium:reporting-guideline-compliance` (planned v0.3) — the
  downstream skill that runs the chosen checklist against the
  manuscript.
- `/scriptorium:reviewer-simulation` — pairs naturally before
  submission; reviewers check reporting-guideline compliance.
- `/scriptorium:desk-rejection-risk` — pairs naturally when
  `target_venue` is set; some venues desk-reject for
  reporting-guideline non-compliance.
- `/scriptorium:explain reporting-guideline-fit` — full design
  tour.
