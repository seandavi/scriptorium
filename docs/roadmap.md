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

| Component | Status / Justification |
|---|---|
| `manuscript-pipeline` orchestrator | Sequences leaf skills; consumes structured outputs. Spec ready; built once the leaves are stable. |
| `desk-rejection-risk` skill | **Landed.** [`editorial-decision-making`](../knowledge/peer-review/editorial-decision-making.md) — 70–90% desk-rejection rates at top journals; scriptorium's value proposition includes catching what would trigger desk rejection. |
| `venue-fit` skill | **Landed.** Tiered venue recommendation with predatory refusal, opt-in preprint mode (PCI, Review Commons, F1000Research, eLife post-2022), and bias-managed pub-history calibration. Grounded in three new knowledge notes: [`venue-selection`](../knowledge/peer-review/venue-selection.md), [`predatory-publishing`](../knowledge/peer-review/predatory-publishing.md), [`preprint-landscape`](../knowledge/peer-review/preprint-landscape.md). |
| ESL-aware checks embedded in `argumentative-flow` | **Landed.** [`esl-writers-swales-hyland`](../knowledge/scientific-writing/esl-writers-swales-hyland.md). |
| `author-contribution-audit` skill | **Landed.** Replaces the originally-planned `contributors:` schema addition. Per [`declared-work-scope`](../knowledge/conventions/declared-work-scope.md), scriptorium operates on declared prose where it lives — duplicating contributions in `MANUSCRIPT_STATE.yaml` would have created a sync problem. The skill audits the Author Contributions section against ICMJE's four authorship criteria and CRediT's 14 contributor roles. Grounded in [`credit-taxonomy-authorship`](../knowledge/peer-review/credit-taxonomy-authorship.md). |
| `reporting-guideline-fit` skill | **Landed.** Replaces the originally-planned `reporting_guidelines:` schema addition. Authors often don't know which EQUATOR checklist applies — declaring it in state was the wrong-data-confidently-declared failure mode. The skill infers from the manuscript methods; the author confirms. Grounded in [`reporting-guidelines`](../knowledge/scientific-writing/reporting-guidelines.md). |

## v0.3 — Validation skills + reporting-guideline compliance

Once the structured-output pattern handles critique and transformation
reliably, validation skills become the next leverage point. Most need
deterministic scripts called out from skills, not LLM arithmetic.

| Component | Status / Justification |
|---|---|
| `statistics-consistency` skill | [`statistical-inconsistency`](../knowledge/critique-techniques/statistical-inconsistency.md) — Statcheck/GRIM/GRIMMER/SPRITE/Carlisle. Skill orchestrates external scripts; does not pretend to recompute in-band. Design memo: [`docs/design/v0.3-statistics-consistency.md`](design/v0.3-statistics-consistency.md). |
| `figure-text-alignment` skill | **Landed (text-only sub-skill A).** [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md), [`visualization-figures`](../knowledge/scientific-writing/visualization-figures.md). Classifies caption ↔ body-text-reference pairs as aligned / partially aligned / misaligned / cannot-determine, plus pattern flags (orphan figure, phantom reference, panel mismatch, axis/units divergence, direction divergence). Pure text-vs-text; no image reading. Multimodal sub-skill B (LLM-vision) remains deferred until reliability is validated against a known-mismatch test set. |
| `terminology-normalization` skill | **Landed (early).** [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md), [`style-guides`](../knowledge/scientific-writing/style-guides.md) — terminology drift detection; preferred-term enforcement from `MANUSCRIPT_STATE.yaml`. Shipped during v0.2 ramp because the grounding notes existed and the schema fields (`terminology.preferred` / `forbidden` / `synonyms`) were already in place. |
| `gap-finder` skill | **Landed (early).** Identifies gaps in declared draft prose, organised by a seven-category taxonomy. Each finding anchors in a specific manuscript passage; suggested directions are pasteable search strategies, never invented citations. Grounded in two new knowledge notes: [`research-gap-detection`](../knowledge/critique-techniques/research-gap-detection.md), [`literature-search-strategies`](../knowledge/scientific-writing/literature-search-strategies.md). |
| `reporting-guideline-compliance` skill | **Landed.** [`reporting-guidelines`](../knowledge/scientific-writing/reporting-guidelines.md), [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md). Walks an EQUATOR Network checklist (CONSORT, STROBE, PRISMA, ARRIVE, STARD, TRIPOD/TRIPOD+AI, CARE, COREQ, CHEERS, plus AI-extensions) item by item and classifies each as present / partial / missing / not-applicable, with quoted manuscript anchors. Downstream of v0.2's `reporting-guideline-fit` (which infers which checklist applies; this skill runs it). |
| `compression` skill | **Landed.** [`narrative-frameworks`](../knowledge/scientific-writing/narrative-frameworks.md), [`semantic-preservation`](../knowledge/editing/semantic-preservation.md), [`copyediting-vs-developmental`](../knowledge/editing/copyediting-vs-developmental.md). Page-limit-driven section compression that preserves every citation, statistic, declared `core_claim`, terminology choice, and hedging stack. Per-edit suggestions; never auto-applies. Sits one editorial level below `argumentative-flow` (line-edit posture vs. block-rewrite). |
| `voice-profile` skill | [`corpus-based-stylometry`](../knowledge/scientific-writing/corpus-based-stylometry.md), [`author-role-evidence`](../knowledge/author-roles/author-role-evidence.md) — extract author writing patterns from a small single-author corpus. Design memo: [`docs/design/v0.3-voice-profile.md`](design/v0.3-voice-profile.md). |
| `persona-calibration` skill | [`author-role-evidence`](../knowledge/author-roles/author-role-evidence.md), [`ai-peer-review-research`](../knowledge/peer-review/ai-peer-review-research.md) — checkpoint synthetic feedback against the real author. Design memo: [`docs/design/v0.3-persona-calibration.md`](design/v0.3-persona-calibration.md). |

## v0.4 — Grant-specific skills and bounded transformations

**Originally framed as "Generation skills".** Reframed once
[`declared-work-scope`](../knowledge/conventions/declared-work-scope.md)
landed: scriptorium does not generate prose from blankness. Generation
*is* in scope when it transforms declared scaffolding into a known
target form — the v0.4 work concentrates there. Most of the
originally-planned v0.4 skills (`discussion-drafting`,
`results-narrative`) involved substantial proposer-side judgment
incompatible with the scope and have been dropped (see
[Explicit non-goals](#explicit-non-goals)); two transformations
remain in scope and one grant-specific critique is added.

The unifying frame for v0.4 is **the grant-writing workflow**, where
the author has typically done substantial proposer-side work (mentor
discussions, aim selection, significance framing) before sitting down
to write, and where the value of bounded-transformation skills is
highest.

| Component | Justification |
|---|---|
| `specific-aims` skill | Transforms declared significance + hypotheses + methods (in `MANUSCRIPT_STATE.yaml` and the manuscript's existing methods scaffolding) into structured NIH-aims prose. Grant-specific; the author has typically already committed to the aims via mentor discussion before invoking — the skill renders them in canonical structure. Grounded in [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md) and [`nih-significance-patterns`](../knowledge/grants/nih-significance-patterns.md). NIH 2025 Simplified Review Framework bundles Significance + Innovation — the skill ladders both, and the NIH Factor 1 / Factor 2 framing is the target structure. In scope because the inputs are declared. |
| `aims-significance-coherence` skill | Critique skill — audits whether the declared significance is coherent with the stated aims (cross-section consistency check for grants). Pairs with `reviewer-simulation`'s grant-archetype variant (study-section roles); the aims-significance gap is one of the most common NIH-reviewer flags. Grounded in [`nih-significance-patterns`](../knowledge/grants/nih-significance-patterns.md), [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md), and [`reviewer-archetypes-grants`](../knowledge/grants/reviewer-archetypes-grants.md). |
| `lay-summary` skill | Translation of declared manuscript or grant prose into plain-language form, against funder-specific length and reading-level requirements (NIH 2025 Public Access requirements; Wellcome Trust; EU Clinical Trials Regulation 536/2014). Strongly transformative — both source and target style are declared. Grounded in [`plain-language-lay-summaries`](../knowledge/scientific-writing/plain-language-lay-summaries.md). |

Skills outside this list that were on the previous v0.4 roadmap —
`results-narrative`, `discussion-drafting` — have been dropped under
declared-work-scope. The remaining grant-side work (cover letters,
biosketch-fit, funder-specific compliance checks) is plausibly
v0.5+ once v0.4 lands; not committed yet.

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

- **No blank-slate prose generation** — [`declared-work-scope`](../knowledge/conventions/declared-work-scope.md). Scriptorium operates on prose the author has written or scaffolding the author has declared. The proposer role in Hayes' 2012 writing-process model (generating content from nothing) is the author's; scriptorium occupies the translator and evaluator roles. Generation skills *are* in scope when they transform declared scaffolding (v0.4 `specific-aims`, `lay-summary`). Generation from a blank section, or "help me figure out what to write about", is not, and the originally-planned v0.4 `discussion-drafting` and `results-narrative` skills were dropped under this scope: the discussion involves substantial proposer judgment (what does this mean? what should be emphasized?) and the "results narrative" risks slipping claims that go beyond the declared data. The shape of those concerns is covered by `argumentative-flow` + `gap-finder` (for an existing discussion) and `figure-text-alignment` (for results-prose-vs-data consistency).
- **No general-purpose writing-quality score** — [`quantitative-quality-measures`](../knowledge/scientific-writing/quantitative-quality-measures.md) (pending). Flesch-Kincaid / SMOG / Coleman-Liau systematically misrate scientific prose (technical terms inflate difficulty). A quality score would be theater.
- **No authorial-voice preservation guarantee** — [`ai-writing-failure-modes`](../knowledge/prior-art/ai-writing-failure-modes.md). Detection of "ChatGPT smell" (Kobak 2024 et al.) is possible at corpus level; correction at sentence level is unreliable. Scriptorium's conservative-edit posture mitigates this but doesn't claim to eliminate it.
- **No forensic-expert replacement** — [`forensic-methodology`](../knowledge/critique-techniques/forensic-methodology.md). Bik-style image forensics, Cabanac tortured-phrase detection, and statistical forensics (Carlisle, Statcheck, GRIM, SPRITE) require domain experts. Scriptorium is a pre-submission first pass that catches cheap errors before a manuscript reaches reviewers — not a replacement for sleuths or institutional integrity review.
- **No autonomous reviewing** — [`ai-peer-review-research`](../knowledge/peer-review/ai-peer-review-research.md). Scriptorium's `reviewer-simulation` is explicitly author-side: the author runs it on their own work to pressure-test before submission. Editorial-side use is contrary to current ICMJE, NIH, and major-publisher policies (and we agree with those policies).
- **No replacement for reference managers** — [`reference-managers`](../knowledge/prior-art/reference-managers.md). Citation auditing works with whatever bibliography Zotero/Mendeley/Paperpile/BibTeX produces; scriptorium does not manage references itself.
- **No discipline-specific defaults beyond biomedical/clinical at v0.1–v0.3** — [`discipline-conventions`](../knowledge/scientific-writing/discipline-conventions.md). The evidence base is biomedical-coded. Expanding to physics, CS/ML, math, humanities requires per-discipline knowledge layers that don't exist yet; PRs welcome.

## Update cadence

This roadmap is reviewed at each release. Issues open against deferred
items are welcome but get triaged against the priority order above.
