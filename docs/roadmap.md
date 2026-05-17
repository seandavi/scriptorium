# Roadmap

The release plan for scriptorium, synthesized from the
[`knowledge/`](../knowledge/) evidence base. Each phase's contents are
chosen because the research justifies them — not because they're easy
or because they sound impressive.

The implementation-priority section of every knowledge document feeds
this roadmap. Findings that the research concluded should **not**
become skills are documented in [Explicit non-goals](#explicit-non-goals)
so the project's claims stay honest.

## v0.1 — Foundation (in flight)

The first release proves the architectural pattern. Three leaf skills,
shared state, a CLI, and the knowledge layer that grounds the skills
in evidence.

| Component | Grounded in |
|---|---|
| `citation-audit` skill | [`citation-claim-alignment`](../knowledge/critique-techniques/citation-claim-alignment.md), [`citation-accuracy-evidence`](../knowledge/citations/citation-accuracy-evidence.md), [`citation-overreach-research`](../knowledge/citations/citation-overreach-research.md), [`hallucination-in-llm-citations`](../knowledge/citations/hallucination-in-llm-citations.md) |
| `reviewer-simulation` skill | [`reviewer-archetypes-evidence`](../knowledge/peer-review/reviewer-archetypes-evidence.md), [`common-critiques-taxonomy`](../knowledge/peer-review/common-critiques-taxonomy.md), [`ai-peer-review-research`](../knowledge/peer-review/ai-peer-review-research.md), [`critique-quality-evidence`](../knowledge/peer-review/critique-quality-evidence.md) |
| `argumentative-flow` skill | [`reader-expectation-approach`](../knowledge/scientific-writing/reader-expectation-approach.md), [`narrative-frameworks`](../knowledge/scientific-writing/narrative-frameworks.md), [`argument-mapping`](../knowledge/critique-techniques/argument-mapping.md), [`semantic-preservation`](../knowledge/editing/semantic-preservation.md) |
| `MANUSCRIPT_STATE.yaml` schema + Venice example | All of the above |
| `scriptorium` CLI (`install`, `validate`, `prompt-pack`, `list`) | Self-evident |
| Claude Code plugin packaging | — |
| Knowledge layer (~40 docs) | — |
| DESIGN.md with scope statement + defensive-design section | [`ai-writing-failure-modes`](../knowledge/prior-art/ai-writing-failure-modes.md), [`discipline-conventions`](../knowledge/scientific-writing/discipline-conventions.md) |

**Success criterion for v0.1:** the three skills run usefully against
the Venice 2026 manuscript (and any other manuscript with a populated
`MANUSCRIPT_STATE.yaml`). Output structure is consistent enough that a
future orchestrator can consume it.

## v0.2 — Coordination + targeted critique additions

After v0.1 has been used on real manuscripts and the structured-output
discipline is proven, the next priorities are coordination and the two
highest-ROI critique additions identified in research.

| Component | Justification |
|---|---|
| `manuscript-pipeline` orchestrator | Sequences leaf skills; consumes structured outputs. Spec ready; built once the leaves are stable. |
| `desk-rejection-risk` skill | [`editorial-decision-making`](../knowledge/peer-review/editorial-decision-making.md) — 70–90% desk-rejection rates at top journals; scriptorium's value proposition includes catching what would trigger desk rejection. |
| `MANUSCRIPT_STATE.yaml` schema: add `contributors:` field | [`credit-taxonomy-authorship`](../knowledge/peer-review/credit-taxonomy-authorship.md) — CRediT 14 roles is the established standard; embed ICMJE authorship checks in `reviewer-simulation`. |
| `MANUSCRIPT_STATE.yaml` schema: add `reporting_guidelines:` field | [`reporting-guidelines`](../knowledge/scientific-writing/reporting-guidelines.md) — saves every skill from re-detecting which checklist applies. |
| ESL-aware checks embedded in `argumentative-flow` | [`esl-writers-swales-hyland`](../knowledge/scientific-writing/esl-writers-swales-hyland.md) — large non-native-English audience; Paperpal/Trinka territory. |

## v0.3 — Validation skills + reporting compliance

Once the structured-output pattern handles critique and transformation
reliably, validation skills become the next leverage point. Most need
deterministic scripts called out from skills, not LLM arithmetic.

| Component | Justification |
|---|---|
| `statistics-consistency` skill | [`statistical-inconsistency`](../knowledge/critique-techniques/statistical-inconsistency.md) — Statcheck/GRIM/GRIMMER/SPRITE/Carlisle. Skill orchestrates external scripts; does not pretend to recompute in-band. |
| `figure-text-alignment` skill | [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md), [`visualization-figures`](../knowledge/scientific-writing/visualization-figures.md) (when research completes). LLM vision is improving but unreliable for scientific figures; skill flags possible mismatches for human review. |
| `terminology-normalization` skill | [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md), [`style-guides`](../knowledge/scientific-writing/style-guides.md) — terminology drift detection; preferred-term enforcement from `MANUSCRIPT_STATE.yaml`. |
| `reporting-compliance` skill | [`reporting-guidelines`](../knowledge/scientific-writing/reporting-guidelines.md) — maps manuscript sections to CONSORT/STROBE/PRISMA/etc. checklist items; per-item present/partial/missing/N-A. |
| `compression` skill | [`narrative-frameworks`](../knowledge/scientific-writing/narrative-frameworks.md) — page-limit driven; preserves citations, statistics, and core claims. |

## v0.4 — Generation skills

Generation skills are deferred until critique + validation are mature
enough to catch generation mistakes. Generating prose is the most
opinionated and the most failure-prone class of skills.

| Component | Justification |
|---|---|
| `specific-aims` skill | [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md), [`nih-significance-patterns`](../knowledge/grants/nih-significance-patterns.md). NIH 2025 Simplified Review Framework bundles Significance + Innovation — skill must ladder both. |
| `results-narrative` skill | [`narrative-frameworks`](../knowledge/scientific-writing/narrative-frameworks.md), [`reader-expectation-approach`](../knowledge/scientific-writing/reader-expectation-approach.md). |
| `discussion-drafting` skill | [`narrative-frameworks`](../knowledge/scientific-writing/narrative-frameworks.md), [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md). |
| `lay-summary` skill | (pending `plain-language-lay-summaries` research) — funder requirements (NIH, Wellcome, EU CTR 536/2014) are increasing. |

## v0.5+ — Platform reach + knowledge expansion

| Component | Justification |
|---|---|
| Codex / Gemini / Hermes adapters | Audience reach beyond Claude Code. Most reusable via the `prompt.md` files already shipped per skill; thin per-platform installer scripts in `adapters/`. |
| Per-discipline knowledge layers (physics, CS/ML, mathematics, qualitative social science) | [`discipline-conventions`](../knowledge/scientific-writing/discipline-conventions.md) — currently scope-limited to biomedical/clinical. Expand only when non-biomedical adoption emerges. |
| Astro/Starlight docs site (with Quarto preprocessing) | Mirrors the quartobot pattern. Phase 1.5; placeholder shipped in v0.1. |

## Explicit non-goals

Findings the research concluded should **not** become skills, with
reasons. This list is load-bearing: it keeps the project honest about
what it does and doesn't claim.

- **No general-purpose writing-quality score** — [`quantitative-quality-measures`](../knowledge/scientific-writing/quantitative-quality-measures.md) (pending). Flesch-Kincaid / SMOG / Coleman-Liau systematically misrate scientific prose (technical terms inflate difficulty). A quality score would be theater.
- **No authorial-voice preservation guarantee** — [`ai-writing-failure-modes`](../knowledge/prior-art/ai-writing-failure-modes.md). Detection of "ChatGPT smell" (Kobak 2024 et al.) is possible at corpus level; correction at sentence level is unreliable. Scriptorium's conservative-edit posture mitigates this but doesn't claim to eliminate it.
- **No forensic-expert replacement** — [`forensic-methodology`](../knowledge/critique-techniques/forensic-methodology.md). Bik-style image forensics, Cabanac tortured-phrase detection, and statistical forensics (Carlisle, Statcheck, GRIM, SPRITE) require domain experts. Scriptorium is a pre-submission first pass that catches cheap errors before a manuscript reaches reviewers — not a replacement for sleuths or institutional integrity review.
- **No autonomous reviewing** — [`ai-peer-review-research`](../knowledge/peer-review/ai-peer-review-research.md). Scriptorium's `reviewer-simulation` is explicitly author-side: the author runs it on their own work to pressure-test before submission. Editorial-side use is contrary to current ICMJE, NIH, and major-publisher policies (and we agree with those policies).
- **No replacement for reference managers** — [`reference-managers`](../knowledge/prior-art/reference-managers.md). Citation auditing works with whatever bibliography Zotero/Mendeley/Paperpile/BibTeX produces; scriptorium does not manage references itself.
- **No discipline-specific defaults beyond biomedical/clinical at v0.1–v0.3** — [`discipline-conventions`](../knowledge/scientific-writing/discipline-conventions.md). The evidence base is biomedical-coded. Expanding to physics, CS/ML, math, humanities requires per-discipline knowledge layers that don't exist yet; PRs welcome.

## Update cadence

This roadmap is reviewed at each release. Issues open against deferred
items are welcome but get triaged against the priority order above.
