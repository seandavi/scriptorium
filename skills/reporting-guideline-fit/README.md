# reporting-guideline-fit — infer which EQUATOR checklist applies

Reads the manuscript's methods section and infers which EQUATOR
Network reporting guideline applies — CONSORT 2025, SPIRIT 2025,
STROBE, PRISMA 2020, ARRIVE 2.0, TRIPOD/TRIPOD+AI 2024, STARD
2015, CARE, COREQ, CHEERS 2022, TRIPOD-LLM, REFINE, CHART, plus
AI-extensions (CONSORT-AI, SPIRIT-AI, STARD-AI, TRIPOD+AI) where
applicable. When the manuscript declares generative-AI use, it
also surfaces GAMER as an add-on disclosure checklist; GAMER
never replaces the design checklist.

This is the **upstream inference** in the reporting-guidelines
workflow. Stops at "which checklist?"; the downstream
`reporting-guideline-compliance` skill (v0.3) runs the full
checklist against the manuscript.

## When to invoke

- The author asks "which reporting checklist applies to my
  study?"
- Before running the downstream `reporting-guideline-compliance`
  audit and the right checklist isn't yet known.
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
   randomised intervention study uses ARRIVE 2.0 + CONSORT 2025
   (plus CONSORT-AI 2020 if AI-enabled). The skill never picks
   one when several apply.
3. **Versioning is honest.** CONSORT 2025 over CONSORT 2010;
   SPIRIT 2025 for trial protocols; PRISMA 2020 over PRISMA
   2009; TRIPOD+AI 2024 over TRIPOD 2015 for AI-based
   prediction models. CONSORT-AI and SPIRIT-AI (2020) were
   built on the older base checklists, so pairing them with a
   2025 checklist comes with the version mismatch named. The
   skill names supersession explicitly when relevant.

## What it explicitly will not do

- Run the full reporting-guideline-compliance audit (that's the
  downstream skill).
- Declare a checklist as authoritatively applicable.
  Recommendation only — the author confirms.
- Operate on outline-phase manuscripts (no methods to infer
  from), or without a methods section, by default.
- Force a confident answer when methods is too sketchy.
- Write to MANUSCRIPT_STATE.yaml.
- Critique study design (the skill infers from the methods as
  written, not whether the design was the right choice).
- Editor-side enforcement. Author-side decision support only.

## Guards and overrides

The skill declares its guards in `manifest.yaml`, following
[`author-authority`](../../knowledge/conventions/author-authority.md).

| Guard | Kind | Default | If the author overrides |
|---|---|---|---|
| `outline-phase` | scope | refuse | Infers from whatever methods stub exists. |
| `methods-section-required` | scope | refuse | Infers from title, abstract and registration metadata, every inference capped at `low` confidence. |
| `no-inference-beyond-evidence` | accuracy | refuse | Cannot be overridden. |

When a scope guard fires, the skill states the concern and its
source in one line at every guidance level. A per-run answer wins;
otherwise an entry under `meta.overrides` in `MANUSCRIPT_STATE.yaml`
lets the skill proceed without asking:

```yaml
meta:
  overrides:
    - guard: methods-section-required
      skills: [reporting-guideline-fit]
```

When the run proceeds past a scope guard, the report carries an
`Overrides applied: <guard ids>` line under its title. This line is
the one addition to the output contract.

## Grounding

Primarily grounded in
[`knowledge/scientific-writing/reporting-guidelines.md`](../../knowledge/scientific-writing/reporting-guidelines.md)
— the EQUATOR Network registry, design-specific checklists
(CONSORT 2025, SPIRIT 2025, STROBE, PRISMA 2020, ARRIVE 2.0,
STARD 2015, TRIPOD+AI 2024, CARE, COREQ, CHEERS 2022), the
AI-extension landscape (CONSORT-AI/SPIRIT-AI 2020, TRIPOD+AI
2024, STARD-AI), the 2025–2026 LLM guidelines (TRIPOD-LLM,
REFINE, CHART, and the GAMER disclosure checklist), and the
rationale for why standardised reporting matters. The note's
routing guidance for this skill: trial protocols to SPIRIT
2025, trial reports to CONSORT 2025 (plus CONSORT-AI for AI
interventions), LLM-evaluation studies to TRIPOD-LLM or REFINE,
chatbot health-advice studies to CHART, and GAMER as an
additional disclosure checklist whenever generative AI was
used.

The guards follow
[`knowledge/conventions/author-authority.md`](../../knowledge/conventions/author-authority.md):
scope guards are author-overridable defaults, and the accuracy
guard is fixed.

## See also

- [`SKILL.md`](SKILL.md) — full Claude Code skill (operational
  protocol, output template, hard constraints).
- [`prompt.md`](prompt.md) — platform-neutral version.
- [`manifest.yaml`](manifest.yaml) — machine-readable metadata.
- `/scriptorium:reporting-guideline-compliance` — the downstream
  skill that runs the chosen checklist against the manuscript.
- `/scriptorium:reviewer-simulation` — pairs naturally before
  submission; reviewers check reporting-guideline compliance.
- `/scriptorium:desk-rejection-risk` — pairs naturally when
  `target_venue` is set; some venues desk-reject for
  reporting-guideline non-compliance.
- `/scriptorium:explain reporting-guideline-fit` — full design
  tour.
