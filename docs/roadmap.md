# Roadmap

The release plan for scriptorium, synthesized from the
[`knowledge/`](../knowledge/) evidence base. Each phase's contents are
chosen because the research justifies them — not because they're easy
or because they sound impressive.

The implementation-priority section of every knowledge document feeds
this roadmap. Findings that the research concluded should **not**
become skills are documented in [Explicit non-goals](#explicit-non-goals)
so the project's claims stay honest.

Grounding lists below match the `grounding:` front matter in each
shipped skill's `SKILL.md`. Every skill also grounds in the two
project-wide conventions,
[`declared-work-scope`](../knowledge/conventions/declared-work-scope.md)
and [`guidance-level`](../knowledge/conventions/guidance-level.md);
those are not repeated per row.

## v0.1 — Foundation (released as 0.1.0.dev0, 2026-05-19)

The first release proves the architectural pattern. Three leaf skills,
shared state, a CLI, and the knowledge layer that grounds the skills
in evidence.

| Component | Grounded in |
|---|---|
| `citation-audit` skill | [`citation-claim-alignment`](../knowledge/critique-techniques/citation-claim-alignment.md), [`citation-accuracy-evidence`](../knowledge/citations/citation-accuracy-evidence.qmd), [`citation-overreach-research`](../knowledge/citations/citation-overreach-research.md), [`hallucination-in-llm-citations`](../knowledge/citations/hallucination-in-llm-citations.md), [`reference-managers`](../knowledge/prior-art/reference-managers.md), [`peer-review-platforms`](../knowledge/prior-art/peer-review-platforms.md) |
| `reviewer-simulation` skill | [`reviewer-archetypes-evidence`](../knowledge/peer-review/reviewer-archetypes-evidence.md), [`common-critiques-taxonomy`](../knowledge/peer-review/common-critiques-taxonomy.md), [`ai-peer-review-research`](../knowledge/peer-review/ai-peer-review-research.md), [`critique-quality-evidence`](../knowledge/peer-review/critique-quality-evidence.md), [`reporting-guidelines`](../knowledge/scientific-writing/reporting-guidelines.md), [`ai-writing-failure-modes`](../knowledge/prior-art/ai-writing-failure-modes.md), [`peer-review-platforms`](../knowledge/prior-art/peer-review-platforms.md), [`credit-taxonomy-authorship`](../knowledge/peer-review/credit-taxonomy-authorship.md) |
| `argumentative-flow` skill | [`reader-expectation-approach`](../knowledge/scientific-writing/reader-expectation-approach.md), [`narrative-frameworks`](../knowledge/scientific-writing/narrative-frameworks.md), [`argument-mapping`](../knowledge/critique-techniques/argument-mapping.md), [`semantic-preservation`](../knowledge/editing/semantic-preservation.md), [`revision-research`](../knowledge/editing/revision-research.md), [`esl-writers-swales-hyland`](../knowledge/scientific-writing/esl-writers-swales-hyland.md) |
| `MANUSCRIPT_STATE.yaml` schema + Venice example | All of the above |
| `scriptorium` CLI (`install`, `validate`, `prompt-pack`, `list`) | Self-evident |
| Claude Code plugin packaging | — |
| Knowledge layer (~40 docs) | — |
| DESIGN.md with scope statement + defensive-design section | [`ai-writing-failure-modes`](../knowledge/prior-art/ai-writing-failure-modes.md), [`discipline-conventions`](../knowledge/scientific-writing/discipline-conventions.md) |

**Success criterion for v0.1:** the three skills run usefully against
the Venice 2026 manuscript (and any other manuscript with a populated
`MANUSCRIPT_STATE.yaml`). Output structure is consistent enough that a
future orchestrator can consume it.

## v0.2 — Coordination + targeted critique additions (released as 0.2.0, 2026-05-20)

After v0.1 has been used on real manuscripts and the structured-output
discipline is proven, the next priorities are coordination and the two
highest-ROI critique additions identified in research.

| Component | Status / Justification |
|---|---|
| `manuscript-pipeline` orchestrator | **Not built; not in 0.2.0.** Sequences leaf skills; consumes structured outputs. Spec ready; built once the leaves are stable. Should allow re-entry rather than a strict linear sequence ([`revision-research`](../knowledge/editing/revision-research.md)). |
| `desk-rejection-risk` skill | **Landed.** Most submissions to top general journals are declined without full peer review; the skill quotes only rates the journals disclose themselves and states that desk outcomes carry selection the manuscript cannot change. Grounded in [`editorial-decision-making`](../knowledge/peer-review/editorial-decision-making.md), [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md), [`common-critiques-taxonomy`](../knowledge/peer-review/common-critiques-taxonomy.md), [`peer-review-platforms`](../knowledge/prior-art/peer-review-platforms.md). |
| `venue-fit` skill | **Landed.** Tiered venue recommendation with predatory refusal, funder APC rules in the hard filter, a preprint mode (PCI, Review Commons, F1000Research, eLife post-2022) that is opt-in except for HHMI-covered original research, and bias-managed pub-history calibration. Grounded in [`venue-selection`](../knowledge/peer-review/venue-selection.md), [`predatory-publishing`](../knowledge/peer-review/predatory-publishing.md), [`preprint-landscape`](../knowledge/peer-review/preprint-landscape.md), [`editorial-decision-making`](../knowledge/peer-review/editorial-decision-making.md), [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md). |
| ESL-aware checks embedded in `argumentative-flow` | **Landed.** [`esl-writers-swales-hyland`](../knowledge/scientific-writing/esl-writers-swales-hyland.md). |
| `author-contribution-audit` skill | **Landed.** Replaces the originally-planned `contributors:` schema addition. Per [`declared-work-scope`](../knowledge/conventions/declared-work-scope.md), scriptorium operates on declared prose where it lives — duplicating contributions in `MANUSCRIPT_STATE.yaml` would have created a sync problem. The skill audits the Author Contributions section against ICMJE's four authorship criteria and CRediT's 14 contributor roles, and checks AI-use disclosure placement against ICMJE Section V. Grounded in [`credit-taxonomy-authorship`](../knowledge/peer-review/credit-taxonomy-authorship.md). |
| `reporting-guideline-fit` skill | **Landed.** Replaces the originally-planned `reporting_guidelines:` schema addition. Authors often don't know which EQUATOR checklist applies — declaring it in state was the wrong-data-confidently-declared failure mode. The skill infers from the manuscript methods; the author confirms. Grounded in [`reporting-guidelines`](../knowledge/scientific-writing/reporting-guidelines.md). |

## v0.3 — Validation skills + reporting-guideline compliance (released as 0.3.0, 2026-10-20)

0.3.0 ships `figure-text-alignment` (text-only),
`reporting-guideline-compliance`, `compression` and
`outlier-sentence-detector`; `terminology-normalization` and
`gap-finder` shipped early, in 0.2.0. See `[0.3.0]` in the
[CHANGELOG](../CHANGELOG.md). `statistics-consistency`,
`voice-profile` and `persona-calibration` are deferred and not in
0.3.0; each has a design memo.

Once the structured-output pattern handles critique and transformation
reliably, validation skills become the next leverage point. Most need
deterministic scripts called out from skills, not LLM arithmetic.

| Component | Status / Justification |
|---|---|
| `statistics-consistency` skill | **Deferred; not in 0.3.0.** [`statistical-inconsistency`](../knowledge/critique-techniques/statistical-inconsistency.md) — Statcheck, GRIM, GRIMMER and DEBIT on extracted values; SPRITE is heuristic and not a verdict, and Carlisle-style corpus analysis is out of scope. LLM extraction feeds deterministic recomputation, and the report states coverage (results found vs. checked); the skill does not recompute in-band. Design memo: [`docs/design/v0.3-statistics-consistency.md`](design/v0.3-statistics-consistency.md). |
| `figure-text-alignment` skill | **Shipped in 0.3.0 (text-only sub-skill A).** [`visualization-figures`](../knowledge/scientific-writing/visualization-figures.md), [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md), [`forensic-methodology`](../knowledge/critique-techniques/forensic-methodology.md). Classifies caption ↔ body-text-reference pairs as aligned / partially aligned / misaligned / cannot-determine, plus pattern flags (orphan figure, phantom reference, panel mismatch, axis/units divergence, direction divergence). Text-vs-text by default. Reading figure images is opt-in through the `figure-image-reading` scope guard, and every image-derived finding is then labelled "unvalidated vision". A validated multimodal sub-skill B (LLM-vision) remains deferred until reliability is validated against a known-mismatch test set; current multimodal benchmarks (PRISMM-Bench, MuSciClaims) support the deferral. Image-integrity claims stay out of scope (the `no-image-integrity-claims` accuracy guard, not overridable). |
| `terminology-normalization` skill | **Shipped early, in 0.2.0.** [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md), [`style-guides`](../knowledge/scientific-writing/style-guides.md), [`promotional-register`](../knowledge/scientific-writing/promotional-register.md), [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md) — terminology drift detection; preferred-term enforcement from `MANUSCRIPT_STATE.yaml`; an opt-in promotional-register catalog whose entries are labelled corpus-grounded or practice-derived. Shipped during v0.2 ramp because the grounding notes existed and the schema fields (`terminology.preferred` / `forbidden` / `synonyms`) were already in place. |
| `gap-finder` skill | **Shipped early, in 0.2.0.** Identifies gaps in declared draft prose, organised by seven categories: five adapted from Miles (2017; Adu & Miles 2023) plus two manuscript-internal additions (counterargument, internal-consistency). Each finding anchors in a specific manuscript passage; suggested directions are pasteable search strategies by default, never invented citations. Named papers are opt-in through the `citation-recommendations` scope guard and limited to works resolved against Crossref or PubMed in the session. Grounded in [`research-gap-detection`](../knowledge/critique-techniques/research-gap-detection.md), [`literature-search-strategies`](../knowledge/scientific-writing/literature-search-strategies.md), [`argument-mapping`](../knowledge/critique-techniques/argument-mapping.md), [`logical-fallacy-detection`](../knowledge/critique-techniques/logical-fallacy-detection.md), [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md), [`common-critiques-taxonomy`](../knowledge/peer-review/common-critiques-taxonomy.md), [`hallucination-in-llm-citations`](../knowledge/citations/hallucination-in-llm-citations.md). |
| `reporting-guideline-compliance` skill | **Shipped in 0.3.0.** [`reporting-guidelines`](../knowledge/scientific-writing/reporting-guidelines.md), [`internal-consistency`](../knowledge/critique-techniques/internal-consistency.md). Walks an EQUATOR Network checklist (CONSORT, SPIRIT, STROBE, PRISMA, ARRIVE, STARD, TRIPOD/TRIPOD+AI, CARE, COREQ, CHEERS, plus AI-extensions) item by item and classifies each as present / partial / missing / not-applicable, with quoted manuscript anchors. Trial reports default to CONSORT 2025 and protocols to SPIRIT 2025; every item number carries its checklist version. Downstream of v0.2's `reporting-guideline-fit` (which infers which checklist applies; this skill runs it). |
| `compression` skill | **Shipped in 0.3.0.** [`narrative-frameworks`](../knowledge/scientific-writing/narrative-frameworks.md), [`semantic-preservation`](../knowledge/editing/semantic-preservation.md), [`copyediting-vs-developmental`](../knowledge/editing/copyediting-vs-developmental.md), [`revision-research`](../knowledge/editing/revision-research.md), [`reader-expectation-approach`](../knowledge/scientific-writing/reader-expectation-approach.md), [`hayes-flower-writing-model`](../knowledge/scientific-writing/hayes-flower-writing-model.md), [`esl-writers-swales-hyland`](../knowledge/scientific-writing/esl-writers-swales-hyland.md), [`ai-writing-failure-modes`](../knowledge/prior-art/ai-writing-failure-modes.md). Page-limit-driven section compression that preserves every citation, statistic, declared `core_claim`, terminology choice, and hedging stack. Per-edit suggestions; never auto-applies. Sits one editorial level below `argumentative-flow` (line-edit posture vs. block-rewrite). |
| `outlier-sentence-detector` skill | **Shipped in 0.3.0.** [`quantitative-quality-measures`](../knowledge/scientific-writing/quantitative-quality-measures.md), [`copyediting-vs-developmental`](../knowledge/editing/copyediting-vs-developmental.md). Flags sentences that are outliers against the manuscript's own distribution on length, syntactic complexity and nominalization density, for human review. No quality score; does not edit. |
| `voice-profile` skill | **Deferred; not in 0.3.0.** [`corpus-based-stylometry`](../knowledge/scientific-writing/corpus-based-stylometry.md), [`author-role-evidence`](../knowledge/author-roles/author-role-evidence.md) — extract author writing patterns from a small single-author corpus. Design memo: [`docs/design/v0.3-voice-profile.md`](design/v0.3-voice-profile.md). |
| `persona-calibration` skill | **Deferred; not in 0.3.0.** [`author-role-evidence`](../knowledge/author-roles/author-role-evidence.md), [`ai-peer-review-research`](../knowledge/peer-review/ai-peer-review-research.md) — checkpoint synthetic feedback against the real author. Design memo: [`docs/design/v0.3-persona-calibration.md`](design/v0.3-persona-calibration.md). |

## v0.4 — Grant-specific skills and bounded transformations

**Originally framed as "Generation skills".** Reframed once
[`declared-work-scope`](../knowledge/conventions/declared-work-scope.md)
landed: by default, scriptorium does not generate prose from blankness. Generation
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
| `specific-aims` skill | Transforms declared significance + hypotheses + methods (in `MANUSCRIPT_STATE.yaml` and the manuscript's existing methods scaffolding) into structured NIH-aims prose. Grant-specific; the author has typically already committed to the aims via mentor discussion before invoking — the skill renders them in canonical structure. Grounded in [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md) and [`nih-significance-patterns`](../knowledge/grants/nih-significance-patterns.md). NIH 2025 Simplified Review Framework bundles Significance + Innovation — the skill ladders both, and the NIH Factor 1 / Factor 2 framing is the target structure. In scope because the inputs are declared. For NIH targets, rendering application prose sits behind the `nih-application-prose` policy guard (`default: ask`, source NIH NOT-OD-25-132); see the decision below. |
| `aims-significance-coherence` skill | Critique skill — audits whether the declared significance is coherent with the stated aims (cross-section consistency check for grants). Pairs with `reviewer-simulation`'s grant-archetype variant (study-section roles); the aims-significance gap is one of the most common NIH-reviewer flags. Grounded in [`nih-significance-patterns`](../knowledge/grants/nih-significance-patterns.md), [`significance-positioning`](../knowledge/scientific-writing/significance-positioning.md), and [`reviewer-archetypes-grants`](../knowledge/grants/reviewer-archetypes-grants.md). |
| `lay-summary` skill | Translation of declared manuscript or grant prose into plain-language form, against funder-specific length and reading-level requirements (NIH 2025 Public Access requirements; Wellcome Trust; EU Clinical Trials Regulation 536/2014). Strongly transformative — both source and target style are declared. Grounded in [`plain-language-lay-summaries`](../knowledge/scientific-writing/plain-language-lay-summaries.md). |

### Inputs from the October 2026 knowledge refresh

The refresh (#125) changed the grounding for the unshipped v0.4 work.
These are inputs to the v0.4 design, not shipped behaviour:

- **`specific-aims`** ([`nih-significance-patterns`](../knowledge/grants/nih-significance-patterns.md), #138):
  NIH NOT-OD-25-132 says NIH will not consider applications, or
  sections of applications, that are substantially developed by AI to
  be the applicants' original ideas. The note recommends that, for NIH
  targets, the skill default to a slot audit plus author-written
  suggestions, with prose rendering only on explicit request and
  labelled with the policy.
- **`aims-significance-coherence`** ([`nih-significance-patterns`](../knowledge/grants/nih-significance-patterns.md)):
  check SRF Factor 1 (importance) first, because NIH's scoring
  guidance makes it a ceiling on Overall Impact. As pure critique, it
  cannot conflict with NOT-OD-25-132, which makes it the safer first
  v0.4 deliverable.
- **Grant reviewer personas** for `reviewer-simulation`
  ([`reviewer-archetypes-grants`](../knowledge/grants/reviewer-archetypes-grants.md)):
  use the funder's current discussion line (the top third under
  NIH's emergency rules); check NSF Broader Impacts against the 2025
  priorities guidance; date the persona text; never map scores to
  paylines or funding probabilities (that stays fixed, as the
  `no-numeric-outcome-probability` accuracy guard). Simulating or
  drafting reviews of applications the user was assigned to review
  (NOT-OD-23-149) becomes a policy guard rather than a fixed
  refusal: the skill states the concern and its source and the
  author decides. The shipped `editorial-side-use` guard
  (`default: ask`) already covers reviewers and editors of submitted
  work and cites NOT-OD-23-149.
- **`terminology-normalization` venue-manual layer**
  ([`style-guides`](../knowledge/scientific-writing/style-guides.md), #146):
  a possible opt-in layer beneath the author's declared terminology
  lists, citing the manual and edition for each suggestion. Maybe
  later; it needs its own design decision.

**Decision (2026-10-20, #156):** `specific-aims` may render NIH
application prose, behind the `nih-application-prose` policy guard
(`default: ask`, source NIH NOT-OD-25-132). For an NIH target the
skill states the NOT-OD-25-132 concern in one line and asks before
rendering; an author can record a standing answer under
`meta.overrides`. This follows the
[`author-authority`](../knowledge/conventions/author-authority.md)
convention: whether a given use is "substantially developed by AI" is
a judgement the author makes and answers for. The guard id is
reserved for `specific-aims`; `scriptorium validate` rejects overrides
of it until the skill ships.

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
| Astro/Starlight docs site (with Quarto preprocessing) | **Landed.** Built from `docs/` (`docs/scripts/preprocess.py` copies the knowledge layer and renders Quarto) and deployed to GitHub Pages by `docs-deploy.yml`. |

## Explicit non-goals

Findings the research concluded should **not** become skills, with
reasons. This list is load-bearing: it keeps the project honest about
what it does and doesn't claim.

- **No blank-slate prose generation by default** — [`declared-work-scope`](../knowledge/conventions/declared-work-scope.md). Scriptorium operates on prose the author has written or scaffolding the author has declared. The proposer role in Hayes' 2012 writing-process model (generating content from nothing) is the author's; scriptorium occupies the translator and evaluator roles. Generation skills *are* in scope when they transform declared scaffolding (v0.4 `specific-aims`, `lay-summary`). Generation from a blank section, or "help me figure out what to write about", is not, and the originally-planned v0.4 `discussion-drafting` and `results-narrative` skills were dropped under this scope: the discussion involves substantial proposer judgment (what does this mean? what should be emphasized?) and the "results narrative" risks slipping claims that go beyond the declared data. The shape of those concerns is covered by `argumentative-flow` + `gap-finder` (for an existing discussion) and `figure-text-alignment` (for results-prose-vs-data consistency). The boundary refusals in shipped skills are scope guards with `default: refuse`; under [`author-authority`](../knowledge/conventions/author-authority.md) an author can override them, but no skill is built for blank-slate drafting.
- **No general-purpose writing-quality score** — [`quantitative-quality-measures`](../knowledge/scientific-writing/quantitative-quality-measures.md). Flesch-Kincaid / SMOG / Coleman-Liau systematically misrate scientific prose (technical terms inflate difficulty). A quality score would be theater.
- **No authorial-voice preservation guarantee** — [`ai-writing-failure-modes`](../knowledge/prior-art/ai-writing-failure-modes.md). Detection of "ChatGPT smell" (Kobak et al. 2025) is possible at corpus level; correction at sentence level is unreliable. Scriptorium's conservative-edit posture mitigates this but doesn't claim to eliminate it.
- **No forensic-expert replacement** — [`forensic-methodology`](../knowledge/critique-techniques/forensic-methodology.md). Bik-style image forensics, Cabanac tortured-phrase detection, and statistical forensics (Carlisle, Statcheck, GRIM, SPRITE) require domain experts. Scriptorium is a pre-submission first pass that catches cheap errors before a manuscript reaches reviewers — not a replacement for sleuths or institutional integrity review.
- **No autonomous reviewing** — [`ai-peer-review-research`](../knowledge/peer-review/ai-peer-review-research.md), [`peer-review-platforms`](../knowledge/prior-art/peer-review-platforms.md). Scriptorium's `reviewer-simulation` and `desk-rejection-risk` are explicitly author-side: the author runs them on their own work to pressure-test before submission. Editorial-side use would mean uploading a confidential manuscript and delegating the critique to AI, which current reviewer policies restrict. Run by a reviewer or editor of a submitted manuscript, those skills (and `venue-fit` and `author-contribution-audit`) apply the `editorial-side-use` policy guard (`default: ask`): they state the concern and its sources and ask before proceeding. NIH prohibits its reviewers from using generative AI to analyse or formulate critiques of grant applications (NOT-OD-23-149). Elsevier and Springer Nature (2026) allow limited, disclosed, supportive reviewer use but forbid delegating the critique to AI. ICMJE requires reviewers to follow the journal's AI policy or request the journal's permission. We agree with those policies.
- **No replacement for reference managers** — [`reference-managers`](../knowledge/prior-art/reference-managers.md). Citation auditing works with whatever bibliography Zotero/Mendeley/Paperpile/BibTeX produces; scriptorium does not manage references itself.
- **No discipline-specific defaults beyond biomedical/clinical at v0.1–v0.3** — [`discipline-conventions`](../knowledge/scientific-writing/discipline-conventions.md). The evidence base is biomedical-coded. Expanding to physics, CS/ML, math, humanities requires per-discipline knowledge layers that don't exist yet; PRs welcome.

## Update cadence

This roadmap is reviewed at each release. Issues open against deferred
items are welcome but get triaged against the priority order above.
