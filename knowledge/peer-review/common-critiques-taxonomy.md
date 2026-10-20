# Common Critiques: A Taxonomy from the Literature

*Last updated: 2026-10-20*

## Synthesis

What do reviewers actually say? Across four decades of content-analysis studies and one decade of NLP-driven analyses of large review corpora, the empirical record is remarkably stable. Reviewers cluster on a small number of recurring critique categories — methods/statistics, design, framing, literature engagement, presentation — but the two best-known content analyses disagree in part about which categories are *fatal*. Bordage's 2001 content analysis of medical-education manuscripts produced what remains the canonical top-10 reasons for rejection, and judged ignoring the literature, poor study design, inappropriate instruments, and poor writing to be likely fatal, while wrong statistics and overstated results could be fixed [1]. Bornmann, Weymuth & Daniel (2010) found, in chemistry, that many negative comments on the relevance of the contribution and on design/conception signalled that a rejected manuscript would not later appear in a high-impact journal, while negative comments on method/statistics, literature, writing, and discussion of results did not [2]. The robust overlap is **design**; relevance/framing is supported by Bornmann; literature and writing are fatal in Bordage's judgment but not predictive in Bornmann's data. NLP analyses of ML-conference reviews (PeerRead for ACL/NIPS/ICLR, ASAP-Review for ICLR/NeurIPS) use closely related aspect categories at scale [3, 4] (researcher interpretation: these aspect sets are compatible with, not derived from, Bordage's categories).

For scriptorium, this means a taxonomy is not speculative — it can be empirically grounded. The taxonomy below collapses the literature's categories into seven critique families, mapped to the personas in `reviewer-simulation`. Different personas should not have non-overlapping critique sets (the literature shows reviewers share concerns), but they should *weight* the families differently. A statistical reviewer who never mentions sample-size or analysis-choice issues is not behaving like a statistical reviewer.

A second pattern: the literature distinguishes *fixable* from *fatal* critiques, and how often a problem is cited is not the same as how fatal it is. In Bordage's data the two top-ranked reasons (inappropriate statistics, over-interpretation) were the ones he judged fixable; he concluded that "while overstating the results and applying the wrong statistics can be fixed, other problems that the reviewers identified (ignoring the literature, designing poor studies, choosing inappropriate instruments, and writing poor manuscripts) are likely to be fatal flaws warranting rejection" [1]. Deep critiques of study design are the one category both content analyses treat as decisive. Scriptorium should not reward personas for finding many easily-fixed issues if they miss the design-level concerns.

## Evidence

**Bordage 2001 — the canonical reject-reasons list (Acad Med).** Content analysis of reviewers' comments on 151 research manuscripts submitted to the 1997 and 1998 Research in Medical Education (RIME) conference proceedings: negative comments on 123 manuscripts that at least one reviewer rated for exclusion, and positive comments on 28 manuscripts unanimously recommended for acceptance. The top-10 reasons for rejection:

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

Strengths of accepted manuscripts: importance/timeliness of the problem, excellent writing, sound design. Bordage's headline conclusion: overstated results and wrong statistics can be fixed; ignoring the literature, poor study design, inappropriate instruments, and poor writing are likely fatal [1].

**Bornmann, Weymuth & Daniel 2010 (Scientometrics) — chemistry.** Content analysis of the referee comments that led to rejection at *Angewandte Chemie International Edition* for manuscripts later published in either a lower-impact journal (*Tetrahedron Letters*, n = 54) or a high-impact journal (*Journal of the American Chemical Society*, n = 42). A large number of negative comments in "Relevance of contribution" and "Design/Conception" were "clear signs" that the manuscript would not later be published in the high-impact journal; the number of negative comments in "Writing/Presentation," "Discussion of results," "Method/Statistics," and "Reference to the literature and documentation" had no statistically significant influence [2]. The implication for scriptorium (researcher interpretation): *where* negative comments concentrate matters more than how many there are.

**PeerRead (Kang et al., NAACL 2018) — ACL/NIPS/ICLR.** 14.7K paper drafts with accept/reject decisions, 10.7K textual peer reviews. Part of the data carries reviewer aspect scores (e.g., originality, soundness/correctness, substance, clarity, impact, recommendation). Simple models can predict acceptance with up to 21% error reduction over the majority baseline, and can predict aspect scores better than the mean baseline for high-variance aspects such as originality and impact [3]. Researcher interpretation: review content carries decision-relevant signal organized around aspect categories close to those Bordage identified manually.

**ASAP-Review (Yuan, Liu & Neubig 2021/2022) — aspect-level annotation.** ICLR (2017–2020) and NeurIPS (2016–2019) reviews; 8,742 unique papers and 25,986 paper–review pairs after filtering. Eight aspect categories adapted from the ACL review guidelines — summary, motivation/impact, originality, soundness/correctness, substance, replicability, meaningful comparison, clarity — with every aspect except summary marked positive or negative. 1,000 reviews were annotated by humans at the text-span level (two annotators each); the rest were labelled by a trained tagger. The paper also found that system-generated reviews touched on more aspects than human reviews but were less constructive for all aspects except explaining the paper's core idea [4]. *(An earlier version of this note described ASAP-Review as a sentence-level, four-layer annotation of ~17K sentences and said soundness and substance carry most weakness sentences. The sentence figure is a garbled version of the paper's aspect-tagger setup, which segmented the human-annotated reviews into sentences: 900 reviews gave 16,543 training sentences and 100 gave 1,700 validation sentences [4]. The four-layer schema and the weakness-share claim do not appear in the paper and have been removed.)*

**Recent NLP work (2025) — data-driven aspects.** Lu, Kuznetsov & Gurevych ("Identifying Aspects in Peer Reviews," Findings of EMNLP 2025) argue that "the notion of aspect remains poorly formalized," propose an operational definition of aspect and a bottom-up, data-driven schema for deriving aspects from a review corpus, and show that the choice of aspects affects downstream applications such as detecting LLM-generated reviews [5]. This supports treating any aspect taxonomy, including the one below, as a revisable schema rather than a settled list.

## Taxonomy for scriptorium

Seven critique families, with primary persona assignment (the persona most likely to surface each, per the literature). All personas can raise any family; weighting differs. The last column records what the two content analyses say about fatality; it is not a single ranking.

| Family | What it covers | Primary persona | Evidence on fatality (Bordage [1] / Bornmann [2]) |
|---|---|---|---|
| **Design / Conception** | Study design, control groups, confounders, internal validity, instrumentation | Methodological skeptic | Fatal in both: poor design and inappropriate instruments likely fatal (Bordage #3); Design/Conception predictive (Bornmann) |
| **Statistics / Analysis** | Statistical tests, power, sample size, multiple comparisons, model choice | Statistical reviewer | Top-ranked reason (Bordage #1) but judged fixable; Method/Statistics not predictive (Bornmann). A too-small or biased sample (Bordage #4) can be a design-level problem |
| **Generalizability / External validity** | Population scope, translational reach, cohort bias | Translational reviewer | Not measured as a separate category in either study; partly captured by over-interpretation |
| **Relevance / Framing** | Why does this matter? Problem statement, significance | Domain expert | Predictive (Bornmann "Relevance of contribution"); insufficient problem statement is Bordage #6, and importance of the problem was the top strength of accepted papers |
| **Literature engagement** | Missing prior work, miscitation, weak comparison | Domain expert | Contested: "ignoring the literature" likely fatal (Bordage #8); not predictive (Bornmann) |
| **Overclaiming / Inference** | Conclusions outrun evidence; missing limitations | All four, weighted to translational | Ranked #2 by Bordage (over-interpretation) but judged fixable; "Discussion of results" not predictive (Bornmann) |
| **Presentation** | Figures, tables, writing, jargon, organization | Any; not specialized | Contested: poor writing likely fatal (Bordage #5, text difficult to follow); Writing/Presentation not predictive (Bornmann). Bordage's fatal list names poor writing only; it does not mention defective tables or figures (#10) |

**Empirical anchoring rules for scriptorium reviewer-simulation:**

- A persona's critique distribution should approximate the literature's: ≥60% of critiques should land in the persona's primary families. A statistical reviewer producing 80% presentation critiques is a calibration failure. (The 60% threshold is a scriptorium design choice, not a figure from the cited studies.)
- The *count* of critiques should not be optimized. Bornmann et al. (2010) found that many negative comments in "Relevance" and "Design/Conception" signalled the downstream outcome, while negative-comment counts in the other categories did not [2]. Quality of critique > volume.
- Each persona should explicitly note when a high-stakes family (Design, Statistics, Generalizability, Relevance, Literature, Overclaiming) is *not* a concern. Silence on a high-stakes family is ambiguous; explicit "no concerns here" makes the simulation auditable.
- Only Design/Conception is treated as fatal by both content analyses; Relevance is supported by one. Severity labels ("fatal" vs. "fixable") should follow the table above rather than treating every top-ranked family as fatal.
- The `MANUSCRIPT_STATE.yaml` "known weaknesses" field should be cross-checked: if the manuscript has already acknowledged a limitation, a simulated reviewer raising it as a *new* critique is producing noise. Scriptorium should suppress or down-weight such duplicates.

## How this informs scriptorium

- The taxonomy gives `reviewer-simulation` a concrete schema for structured output. Each persona emits critiques tagged by family, allowing downstream skills (e.g., a future `critique-prioritization` skill) to surface fatal-family critiques first.
- It also gives the skill a way to measure its own quality over time: if scriptorium logs simulated critiques, the empirical distribution across families can be compared against the literature's distribution. Over-weighting minor issues is a documented LLM failure mode worth monitoring: in a 2026 expert-annotation study, one of the recurring weaknesses of AI reviewers that humans did not share was an "overly critical stance on minor issues" [6]. Drift toward presentation-only critiques is a related risk to monitor (researcher inference; that study does not report it).
- The "fatal flaws vs. fixable problems" distinction (Bordage 2001) maps directly onto scriptorium's edit posture: fatal-family critiques imply revision recommendations the author should weigh before resubmission; fixable and surface-family critiques can flow into `argumentative-flow`, `compression`, or copy-editing skills automatically. Statistics and overclaiming critiques are common and serious but, on this evidence, usually fixable in revision rather than grounds for rejection.

## Implementation priority for scriptorium

**Verdict:** Yes (shipped) — this note supplies the critique-family schema and lens mapping used by `reviewer-simulation`, seeds the recurring reject-reason patterns that `desk-rejection-risk` checks at the editor-detectable level, and is also cited by `gap-finder` and `init`.
**Scope change from this refresh:** severity labelling. Statistics/Analysis and Overclaiming should be labelled common-but-usually-fixable rather than fatal; Design/Conception is the only family both studies treat as fatal; Literature and Presentation are contested. The seven families and persona mapping are unchanged.
**Required data:** manuscript text and `MANUSCRIPT_STATE.yaml` (including `known_weaknesses`).

## Open questions / weak evidence

- **Field generalization.** Bordage 2001 is medical education; Bornmann 2010 is chemistry; PeerRead/ASAP-Review are ML/NLP. Convergence is striking but not iron-clad for, e.g., humanities, qualitative social science, or theoretical physics. The taxonomy above is most defensible for empirical/quantitative work.
- **Small and dated samples behind the fatality labels.** Bordage analysed 151 manuscripts from two conference years; Bornmann et al. analysed 96 rejected manuscripts from one journal. Their disagreement on literature and presentation critiques may reflect field, venue, or outcome measure (rejection vs. later venue impact).
- **Aspect category boundaries.** "Soundness/correctness" in ML reviews overlaps with "Statistics" and "Design" in biomedicine. Scriptorium should expose the taxonomy as a schema rather than a fixed enum, with field-specific overrides over time.
- **Are LLMs faithful to the distribution?** Liang et al. (2024) report point-level overlap between GPT-4 and human reviewers ~30%. The aspect-level distribution of LLM critiques has not, to our knowledge, been formally compared to the Bordage taxonomy. This is worth a small in-house study with scriptorium's own logs.
- **What about reproducibility/data-availability critiques?** This family has grown sharply in the post-replication-crisis literature but was not a top Bordage category in 2001. Scriptorium should treat it as a real eighth family — under-represented in the historical record, but rising — and pre-emptively assign it to the methodological skeptic. (ASAP-Review's "replicability" aspect is the closest ML-review analogue [4].)

## References

1. Bordage G. Reasons reviewers reject and accept manuscripts: the strengths and weaknesses in medical education reports. *Acad Med* 76(9): 889–896 (2001). DOI: [10.1097/00001888-200109000-00010](https://doi.org/10.1097/00001888-200109000-00010). PMID: 11553504.
2. Bornmann L, Weymuth C, Daniel HD. A content analysis of referees' comments: how do comments on manuscripts rejected by a high-impact journal and later published in either a low- or high-impact journal differ? *Scientometrics* 83(2): 493–506 (2010). DOI: [10.1007/s11192-009-0011-4](https://doi.org/10.1007/s11192-009-0011-4).
3. Kang D, Ammar W, Dalvi B, van Zuylen M, Kohlmeier S, Hovy E, Schwartz R. A dataset of peer reviews (PeerRead): collection, insights and NLP applications. *NAACL-HLT* 2018: 1647–1661. arXiv:1804.09635. DOI: [10.18653/v1/N18-1149](https://doi.org/10.18653/v1/N18-1149).
4. Yuan W, Liu P, Neubig G. Can we automate scientific reviewing? *Journal of Artificial Intelligence Research* 75: 171–212 (2022). Introduces the ASAP-Review dataset and aspect annotation schema. DOI: [10.1613/jair.1.12862](https://doi.org/10.1613/jair.1.12862). Preprint: arXiv:2102.00176. Data and code: https://github.com/neulab/ReviewAdvisor.
5. Lu S, Kuznetsov I, Gurevych I. Identifying aspects in peer reviews. *Findings of the Association for Computational Linguistics: EMNLP 2025*. arXiv:2504.06910. https://aclanthology.org/2025.findings-emnlp.326/.
6. Kim S, Yoon D, Gashteovski K, et al. (incl. Neubig G). On the limits and opportunities of AI reviewers: reviewing the reviews of Nature-family papers with 45 expert scientists. arXiv:2605.20668 (2026, preprint). [https://arxiv.org/abs/2605.20668](https://arxiv.org/abs/2605.20668).

See also: [[reviewer-archetypes-evidence]], [[critique-quality-evidence]], [[ai-peer-review-research]].
