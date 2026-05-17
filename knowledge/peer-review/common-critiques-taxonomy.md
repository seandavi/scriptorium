# Common Critiques: A Taxonomy from the Literature

*Last updated: 2026-05-17*

## Synthesis

What do reviewers actually say? Across four decades of content-analysis studies and one decade of NLP-driven analyses of large review corpora, the empirical record is remarkably stable. Reviewers cluster on a small number of recurring critique categories — methods/statistics, design, framing, literature engagement, presentation — and the *fatal* critiques (those that predict rejection or downstream low impact) concentrate in two of them: methodological design and the relevance/framing of the contribution. Bordage's 2001 content analysis of medical-education manuscripts produced what remains the canonical top-10 reasons for rejection [1]; Bornmann, Weymuth & Daniel (2010) replicated the basic shape of this taxonomy in chemistry [2]; and NLP analyses of NIPS/ICLR reviews (PeerRead, ASAP-Review) reproduce essentially the same aspect categories at scale [3, 4].

For scriptorium, this means a taxonomy is not speculative — it can be empirically grounded. The taxonomy below collapses the literature's categories into seven critique families, mapped to the personas in `reviewer-simulation`. Different personas should not have non-overlapping critique sets (the literature shows reviewers share concerns), but they should *weight* the families differently. A statistical reviewer who never mentions sample-size or analysis-choice issues is not behaving like a statistical reviewer.

A second pattern: the literature distinguishes *surface* from *deep* critiques. Surface critiques (typos, unclear figures, missing citations) are common but rarely fatal. Deep critiques (study design, generalizability, the inferential leap from evidence to claim) are less common per reviewer but heavily over-represented in rejection decisions. Bordage 2001 made this explicit: "ignoring the literature, designing poor studies, choosing inappropriate instruments, and writing poor manuscripts" are likely "fatal flaws warranting rejection" [1]. Scriptorium should not reward personas for finding many surface issues if they miss the design-level concerns.

## Evidence

**Bordage 2001 — the canonical reject-reasons list (Acad Med).** Content analysis of 151 manuscripts and reviewer comments from the Research in Medical Education conference. The top-10 reasons for rejection:

1. Inappropriate or incomplete statistics
2. Over-interpretation of results
3. Inappropriate or suboptimal instrumentation
4. Sample too small or biased
5. Text difficult to follow
6. Insufficient problem statement
7. Inaccurate or inconsistent data reported
8. Incomplete, inaccurate, or outdated review of the literature
9. Insufficient data presented
10. Defective tables or figures

Strengths of accepted manuscripts: importance/timeliness of the problem, excellent writing, sound design. Bordage's headline conclusion: surface problems (statistics, overclaiming) can be fixed; design and framing problems are typically fatal [1].

**Bornmann, Weymuth & Daniel 2010 (Scientometrics) — chemistry replication.** Content analysis of reviewer comments at Angewandte Chemie International Edition. Manuscripts later published in high-impact venues received comparatively few negative comments in "Relevance of contribution" and "Design/Conception"; those that ended up in low-impact venues received many. This adds an effect-size claim: it is concentrated negative comments in these two categories that predict downstream impact, not the raw count of negative comments [2].

**PeerRead (Kang et al., NAACL 2018) — ACL/NIPS/ICLR.** 14.7K paper drafts, 10.7K full review texts. Provides a structured rating across aspects: originality, soundness/correctness, substance, clarity, impact/significance, recommendation. Simple models can predict accept/reject from review text with ~21% error reduction over majority baseline — i.e., review text contains decision-relevant signal beyond the numeric rating, and that signal lives in the same aspect categories Bordage identified manually [3].

**ASAP-Review (Yuan, Liu & Neubig 2021/2022) — aspect-level annotation.** ICLR and NIPS reviews annotated at the sentence level (~17K sentences over 1,199 reviews) across four layers: section correspondence, aspect category (motivation, originality, soundness/correctness, substance, replicability, meaningful comparison, clarity), review functionality (summary, strength, weakness, suggestion), and significance. Confirms that "soundness/correctness" and "substance" together carry the majority of weakness-tagged sentences [4].

**Recent NLP work (2024–2025) — same aspects re-emerge.** "Identifying Aspects in Peer Reviews" (Mahta et al. 2025 arXiv) finds the same six-to-eight aspect families recur in modern conference reviews and proposes them as a stable schema. The category set has not changed materially since Bordage 2001.

## Taxonomy for scriptorium

Seven critique families, with primary persona assignment (the persona most likely to surface each, per the literature). All personas can raise any family; weighting differs.

| Family | What it covers | Primary persona | Bordage rank |
|---|---|---|---|
| **Design / Conception** | Study design, control groups, confounders, internal validity | Methodological skeptic | High (fatal) |
| **Statistics / Analysis** | Statistical tests, power, sample size, multiple comparisons, model choice | Statistical reviewer | Very high (fatal) |
| **Generalizability / External validity** | Population scope, translational reach, cohort bias | Translational reviewer | High (often fatal) |
| **Relevance / Framing** | Why does this matter? Problem statement, significance | Domain expert | High (fatal) |
| **Literature engagement** | Missing prior work, miscitation, weak comparison | Domain expert | High (fatal) |
| **Overclaiming / Inference** | Conclusions outrun evidence; missing limitations | All four, weighted to translational | High (often fatal) |
| **Presentation** | Figures, tables, writing, jargon, organization | Any; not specialized | Medium (rarely fatal alone) |

**Empirical anchoring rules for scriptorium reviewer-simulation:**

- A persona's critique distribution should approximate the literature's: ≥60% of critiques should land in the persona's primary families. A statistical reviewer producing 80% presentation critiques is a calibration failure.
- The *count* of critiques should not be optimized. Bornmann et al. (2010) found that concentration of negative comments in "Relevance" and "Design/Conception" predicted downstream impact better than total count [2]. Quality of critique > volume.
- Each persona should explicitly note when a presumed-fatal family (Design, Statistics, Generalizability, Relevance, Literature, Overclaiming) is *not* a concern. Silence on a fatal family is ambiguous; explicit "no concerns here" makes the simulation auditable.
- The `MANUSCRIPT_STATE.yaml` "known weaknesses" field should be cross-checked: if the manuscript has already acknowledged a limitation, a simulated reviewer raising it as a *new* critique is producing noise. Scriptorium should suppress or down-weight such duplicates.

## How this informs scriptorium

- The taxonomy gives `reviewer-simulation` a concrete schema for structured output. Each persona emits critiques tagged by family, allowing downstream skills (e.g., a future `critique-prioritization` skill) to surface fatal-family critiques first.
- It also gives the skill a way to measure its own quality over time: if scriptorium logs simulated critiques, the empirical distribution across families can be compared against the literature's distribution. Drift toward presentation-only critiques is a known LLM failure mode worth monitoring.
- The "fatal flaws vs. surface fixes" distinction (Bordage 2001) maps directly onto scriptorium's edit posture: fatal-family critiques imply revision recommendations the author should weigh before resubmission; surface-family critiques can flow into `argumentative-flow`, `compression`, or copy-editing skills automatically.

## Open questions / weak evidence

- **Field generalization.** Bordage 2001 is medical education; Bornmann 2010 is chemistry; PeerRead/ASAP-Review are ML/NLP. Convergence is striking but not iron-clad for, e.g., humanities, qualitative social science, or theoretical physics. The taxonomy above is most defensible for empirical/quantitative work.
- **Aspect category boundaries.** "Soundness/correctness" in ML reviews overlaps with "Statistics" and "Design" in biomedicine. Scriptorium should expose the taxonomy as a schema rather than a fixed enum, with field-specific overrides over time.
- **Are LLMs faithful to the distribution?** Liang et al. (2024) report point-level overlap between GPT-4 and human reviewers ~30%. The aspect-level distribution of LLM critiques has not, to our knowledge, been formally compared to the Bordage taxonomy. This is worth a small in-house study with scriptorium's own logs.
- **What about reproducibility/data-availability critiques?** This family has grown sharply in the post-replication-crisis literature but was not a top Bordage category in 2001. Scriptorium should treat it as a real eighth family — under-represented in the historical record, but rising — and pre-emptively assign it to the methodological skeptic.

## References

1. Bordage G. Reasons reviewers reject and accept manuscripts: the strengths and weaknesses in medical education reports. *Acad Med* 76(9): 889–896 (2001). DOI: [10.1097/00001888-200109000-00021](https://doi.org/10.1097/00001888-200109000-00021). PMID: 11553504.
2. Bornmann L, Weymuth C, Daniel HD. A content analysis of referees' comments: how do comments on manuscripts rejected by a high-impact journal and later published in either a low- or high-impact journal differ? *Scientometrics* 83(2): 493–506 (2010). DOI: [10.1007/s11192-009-0011-4](https://doi.org/10.1007/s11192-009-0011-4).
3. Kang D, Ammar W, Dalvi B, van Zuylen M, Kohlmeier S, Hovy E, Schwartz R. A dataset of peer reviews (PeerRead): collection, insights and NLP applications. *NAACL-HLT* 2018: 1647–1661. arXiv:1804.09635. DOI: [10.18653/v1/N18-1149](https://doi.org/10.18653/v1/N18-1149).
4. Yuan W, Liu P, Neubig G. Can we automate scientific reviewing? *Journal of Artificial Intelligence Research* 75: 171–212 (2022). The ASAP-Review aspect annotation schema. DOI: [10.1613/jair.1.12862](https://doi.org/10.1613/jair.1.12862) [TODO verify exact DOI for ASAP-Review specifically].

See also: [[reviewer-archetypes-evidence]], [[critique-quality-evidence]], [[ai-peer-review-research]].
