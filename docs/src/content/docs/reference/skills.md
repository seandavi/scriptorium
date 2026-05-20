---
title: Skills
description: Every shipped scriptorium skill, organised by category and lifecycle stage, with grounding pointers.
sidebar:
  order: 10
---

Every scriptorium skill is single-responsibility, reads
`MANUSCRIPT_STATE.yaml`, and emits structured markdown. The table
below is the source of truth for what ships. The data is pulled
from each skill's `manifest.yaml` in the repo — `category` comes
straight from the manifest field; lifecycle fit, modifies-manuscript,
and other axes are encoded per skill below.

Each row links to the skill's `README.md` in the repo, which is the
full operational contract (inputs, outputs, refusal behaviours,
output schema, complete grounding list).

## Categorisation axes

Three axes give you most of what you need to decide which skill to
run next:

- **Category** — what kind of operation the skill performs.
  - *critique* — assesses; does not modify the manuscript.
  - *validation* — checks against an external standard; does not modify.
  - *normalization* — enforces declared style; suggests edits, never auto-applies.
  - *transformation* — modifies prose under a preservation contract.
  - *meta* — orientation or explanation; no manuscript modification.
  - *utility* — bootstrap; modifies only `MANUSCRIPT_STATE.yaml`.
- **Lifecycle stage** — which `document_phase` values the skill is
  invokable in. Skills refuse to run on phases for which they do
  not have enough declared state to ground against (e.g. `gap-finder`
  refuses on `outline`).
- **Modifies the manuscript?** — *no* (most critique skills), *suggests*
  (normalization and transformation skills emit diffs the author
  reviews and applies), or *state file only* (utility).

Two additional flags some authors need:

- **Author-side only?** — *yes* for `reviewer-simulation` and
  `desk-rejection-risk`. Editorial-side use violates ICMJE / NIH /
  major-publisher policy and the skill itself refuses to run on a
  manuscript the user did not author.
- **Requires bibliography?** — *yes* for `citation-audit`;
  *optional* for skills that read citation context as a side input;
  *no* for most others.

## All shipped skills

| Skill | Category | Lifecycle fit | Modifies | Author-side only | Reqs bib |
|---|---|---|---|---|---|
| [`init`](https://github.com/seandavi/scriptorium/blob/main/skills/init/README.md) | utility | any phase | state file only | no | no |
| [`tour`](https://github.com/seandavi/scriptorium/blob/main/skills/tour/README.md) | meta | any phase | no | no | no |
| [`explain`](https://github.com/seandavi/scriptorium/blob/main/skills/explain/README.md) | meta | any phase | no | no | no |
| [`citation-audit`](https://github.com/seandavi/scriptorium/blob/main/skills/citation-audit/README.md) | critique | draft · review · revision · submission | no | no | yes |
| [`reviewer-simulation`](https://github.com/seandavi/scriptorium/blob/main/skills/reviewer-simulation/README.md) | critique | review · revision · submission | no | **yes** | optional |
| [`gap-finder`](https://github.com/seandavi/scriptorium/blob/main/skills/gap-finder/README.md) | critique | draft · review · revision | no | no | optional |
| [`figure-text-alignment`](https://github.com/seandavi/scriptorium/blob/main/skills/figure-text-alignment/README.md) | critique | draft · review · revision | no | no | no |
| [`desk-rejection-risk`](https://github.com/seandavi/scriptorium/blob/main/skills/desk-rejection-risk/README.md) | critique | revision · submission | no | **yes** | no |
| [`venue-fit`](https://github.com/seandavi/scriptorium/blob/main/skills/venue-fit/README.md) | critique | review · revision · submission | state file only (`candidate_venues`, opt-in) | no | no |
| [`author-contribution-audit`](https://github.com/seandavi/scriptorium/blob/main/skills/author-contribution-audit/README.md) | critique | review · revision · submission | no | no | no |
| [`reporting-guideline-fit`](https://github.com/seandavi/scriptorium/blob/main/skills/reporting-guideline-fit/README.md) | critique | draft · review · revision | no | no | no |
| [`reporting-guideline-compliance`](https://github.com/seandavi/scriptorium/blob/main/skills/reporting-guideline-compliance/README.md) | validation | review · revision · submission | no | no | no |
| [`terminology-normalization`](https://github.com/seandavi/scriptorium/blob/main/skills/terminology-normalization/README.md) | normalization | draft · review · revision | suggests | no | no |
| [`argumentative-flow`](https://github.com/seandavi/scriptorium/blob/main/skills/argumentative-flow/README.md) | transformation | draft · review · revision | suggests | no | no |
| [`compression`](https://github.com/seandavi/scriptorium/blob/main/skills/compression/README.md) | transformation | revision · submission | suggests | no | no |

## Per-category detail

### Critique

Critique skills assess existing prose and emit structured findings.
They do not modify the manuscript and they do not invent citations.

| Skill | One line | Primary grounding |
|---|---|---|
| `citation-audit` | For each scientific claim: identify citation support, evaluate evidence strength, flag overreach. | [`citation-claim-alignment`](https://github.com/seandavi/scriptorium/blob/main/knowledge/critique-techniques/citation-claim-alignment.md), [`hallucination-in-llm-citations`](https://github.com/seandavi/scriptorium/blob/main/knowledge/citations/hallucination-in-llm-citations.md) |
| `reviewer-simulation` | Four attentional lenses (methodological skeptic, domain expert, translational/clinical, statistical), each emitting Major / Minor / Fatal / Enthusiasm / Suggested / Risk. | [`reviewer-archetypes-evidence`](https://github.com/seandavi/scriptorium/blob/main/knowledge/peer-review/reviewer-archetypes-evidence.md), [`common-critiques-taxonomy`](https://github.com/seandavi/scriptorium/blob/main/knowledge/peer-review/common-critiques-taxonomy.md) |
| `desk-rejection-risk` | Author-side audit of triggers that get manuscripts rejected before peer review — scope, format, weak significance, missing required sections. | [`editorial-decision-making`](https://github.com/seandavi/scriptorium/blob/main/knowledge/peer-review/editorial-decision-making.md) |
| `venue-fit` | Tiered venue recommendation (likely fit / stretch / probably premature) with explicit predatory-venue refusal and opt-in preprint mode. | [`venue-selection`](https://github.com/seandavi/scriptorium/blob/main/knowledge/peer-review/venue-selection.md), [`predatory-publishing`](https://github.com/seandavi/scriptorium/blob/main/knowledge/peer-review/predatory-publishing.md), [`preprint-landscape`](https://github.com/seandavi/scriptorium/blob/main/knowledge/peer-review/preprint-landscape.md) |
| `gap-finder` | Identify gaps in declared draft prose, by a seven-category taxonomy. Anchored to passages; suggested directions are search strategies, not invented citations. | [`research-gap-detection`](https://github.com/seandavi/scriptorium/blob/main/knowledge/critique-techniques/research-gap-detection.md), [`literature-search-strategies`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/literature-search-strategies.md) |
| `figure-text-alignment` | Text-only audit of figure captions against body-text references. Aligned / partial / misaligned / cannot-determine. Does not read figure images. | [`internal-consistency`](https://github.com/seandavi/scriptorium/blob/main/knowledge/critique-techniques/internal-consistency.md), [`visualization-figures`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/visualization-figures.md) |
| `author-contribution-audit` | Audit Author Contributions against ICMJE's four authorship criteria and CRediT's 14 contributor roles. LLM-as-author hard refusal. | [`credit-taxonomy-authorship`](https://github.com/seandavi/scriptorium/blob/main/knowledge/peer-review/credit-taxonomy-authorship.md) |
| `reporting-guideline-fit` | Infer which EQUATOR reporting guideline applies (CONSORT, STROBE, PRISMA, ARRIVE, TRIPOD, STARD, CARE, COREQ, CHEERS plus AI extensions). | [`reporting-guidelines`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/reporting-guidelines.md) |

### Validation

Validation skills check existing prose against an external standard
and emit structured findings. They do not modify the manuscript.

| Skill | One line | Primary grounding |
|---|---|---|
| `reporting-guideline-compliance` | Run an EQUATOR reporting-guideline checklist against the manuscript. Each item: present / partial / missing / not-applicable, with a quoted manuscript anchor. | [`reporting-guidelines`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/reporting-guidelines.md) |

### Normalization

Normalization skills enforce author-declared style and terminology.
They emit a structured report plus a list of suggested edits. They
do not auto-apply edits to the manuscript file.

| Skill | One line | Primary grounding |
|---|---|---|
| `terminology-normalization` | Detect terminology drift across a manuscript and enforce the `preferred` / `forbidden` / `synonyms` lists declared in `MANUSCRIPT_STATE.yaml`. | [`internal-consistency`](https://github.com/seandavi/scriptorium/blob/main/knowledge/critique-techniques/internal-consistency.md), [`style-guides`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/style-guides.md) |

### Transformation

Transformation skills modify prose. Both shipped transformation
skills inherit the same preservation contract — citations,
statistics, declared terminology, declared core claims, and the
author's hedging stance are preserved or surfaced as per-edit notes.
Both are explicit-invocation only and operate on a single named
section at a time. The author reviews each diff and decides.

| Skill | One line | Primary grounding |
|---|---|---|
| `argumentative-flow` | Improve a section's logical and argumentative coherence while preserving every citation, statistic, and declared terminology choice. Emits structural diagnosis, proposed outline, revised text, and a preservation report. | [`reader-expectation-approach`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/reader-expectation-approach.md), [`argument-mapping`](https://github.com/seandavi/scriptorium/blob/main/knowledge/critique-techniques/argument-mapping.md), [`semantic-preservation`](https://github.com/seandavi/scriptorium/blob/main/knowledge/editing/semantic-preservation.md) |
| `compression` | Propose page-limit-driven length reductions while preserving every citation, statistic, core claim, and declared terminology choice. Per-edit diffs plus a list of edits NOT proposed because compression would risk a load-bearing nuance. | [`narrative-frameworks`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/narrative-frameworks.md), [`semantic-preservation`](https://github.com/seandavi/scriptorium/blob/main/knowledge/editing/semantic-preservation.md) |

### Meta

Meta skills orient new users and explain scriptorium itself. They
read no manuscript content and modify nothing.

| Skill | One line | Primary grounding |
|---|---|---|
| `tour` | Conversational onboarding. Three or four turns. Ends with one concrete next move. Strictly read-only. | [`guidance-level`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/guidance-level.md) |
| `explain` | Explain scriptorium itself, a named skill, or a named `MANUSCRIPT_STATE` field. Reads `SKILL.md` frontmatter and grounding notes; no manuscript content consumed. | [`guidance-level`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/guidance-level.md) |

### Utility

Utility skills set up scriptorium state. They modify
`MANUSCRIPT_STATE.yaml` (and only that file) when the author confirms.

| Skill | One line | Primary grounding |
|---|---|---|
| `init` | Conversationally bootstrap `MANUSCRIPT_STATE.yaml`. Infers what it can from the filesystem; elicits subjective fields one at a time; validates against the JSON Schema before writing. | [`manuscript-state-schema`](/reference/manuscript-state-schema/) |

## Lifecycle fit, summarised

Skills declare which `document_phase` values they are designed for.
They refuse cleanly on phases for which they do not have enough
declared state to ground against.

| Phase | Typical scriptorium skills |
|---|---|
| **`outline`** | `init`, `tour`, `explain`, `venue-fit`. No critique skills — outline-phase manuscripts do not have enough declared prose for the critique skills to anchor against. |
| **`draft`** | Add `citation-audit`, `gap-finder`, `figure-text-alignment`, `reporting-guideline-fit`, `terminology-normalization`, `argumentative-flow` (per-section). |
| **`review` · `revision`** | All of the above plus `reviewer-simulation`, `author-contribution-audit`, `reporting-guideline-compliance`. |
| **`submission`** | All of the above plus `desk-rejection-risk`, `compression`. |

`MANUSCRIPT_STATE.yaml#document_phase` is set by `scriptorium:init`
and is what the skills read.

## Author-side only

Two skills are explicitly author-side and refuse to run on a
manuscript the user did not author:

- `reviewer-simulation` — editorial-side use violates ICMJE, NIH,
  and major-publisher peer-review policy.
- `desk-rejection-risk` — same family of concern. The skill is a
  pre-submission self-check; AI-triaging submissions on the
  editorial side is contrary to current policy.

The refusal is encoded in the skill's `manifest.yaml` and in the
skill's operational protocol.

## Source of truth

This page is generated by hand from each skill's `manifest.yaml`.
The authoritative source for any single skill is its
`skills/<name>/manifest.yaml` and `skills/<name>/README.md` in the
repo. Future work: auto-generate this table at build time from the
manifests so the two surfaces cannot drift.
