# AI-assisted peer review platforms and tools

*Last updated: 2026-05-17*

## Synthesis

AI in peer review is the most contested adjacent space to scriptorium. The work falls into four buckets: (1) **statistical and methodological check tools** that pre-screen manuscripts for reporting completeness (StatReviewer, Penelope); (2) **citation-intent and integrity tools** that operate post-publication (scite.ai, Springer Nature's irrelevant-reference detector); (3) **LLM-as-reviewer systems** that simulate or generate critical reviews (Stanford PaperReview.ai, AgentReview, OpenReviewer, Liang et al.'s GPT-4 pipeline); and (4) **platform-level innovation** in how peer review is organized (OpenReview, ResearchHub).

The strongest empirical signal in the space is Liang et al.'s pair of studies: GPT-4 feedback on 3,096 Nature-family papers and 1,709 ICLR papers overlaps with individual human reviewers at roughly the same rate that two human reviewers overlap with each other (~30% Nature, ~39% ICLR). A follow-up randomized study in *Nature Machine Intelligence* (2026) confirmed the result at larger scale. This is the most-cited evidence that LLM critique is non-trivially useful, but it does not justify replacing human peer review — only augmenting it.

The policy landscape is unsettled. Elsevier and NIH ban AI in peer review. Springer Nature allows limited AI for language editing. PLOS has investigated ~150 papers since 2024 over peer-review integrity concerns. Two recent studies of open-peer-review reports found hundreds of suspiciously templated reviews across publishers.

For scriptorium, the key positioning is: `reviewer-simulation` is an **author-side critique tool** that helps a manuscript get ready for human peer review. It is explicitly not a substitute for peer review and should never be marketed as one.

## Landscape

### Methodological / statistical pre-screening

**StatReviewer (Houle & DeVoss).** Pre-LLM, rule-based tool for statistical and reporting integrity. Created by Timothy Houle (Wake Forest) and Chadwick DeVoss (Next Digital Publishing) [1]. Checks against CONSORT, STROBE, ICMJE; identifies IMRAD structure; flags numerical errors, statistical-test appropriateness, decimal-place precision. Integrated with Aries Editorial Manager. The tool's positioning has remained "pre-review screening to augment human reviewers," and it predates the LLM era by years — a useful reminder that rule-based tooling can do real work without generation.

**Penelope.ai.** Covered in [[ai-writing-tools-survey]]; the closest production example of inspectable, journal-side compliance checks. 30+ checks per manuscript, customizable per journal, linked back to manuscript text.

### Citation-intent and integrity tools

**scite.ai (Nicholson et al.).** Published in *Quantitative Science Studies* (MIT Press) [2]. Uses deep learning to classify citation context as *supporting*, *contrasting*, or *mentioning*. Built on 25M+ full-text articles; 880M+ classified citation statements. Average distribution: 92.6% mentioning, 6.5% supporting, 0.8% contrasting.

Critically, the **independent evaluation by Nicholson et al. and follow-up studies have produced mixed results**. The supporting/contrasting distinction is the value proposition, but a Hypothesis Research Journal study [3] found F-measures of 0.0–0.58 across categories, with scite frequently misclassifying supporting/contrasting citations as mentions. scite's own pipeline reports 70% citation-context-to-DOI association for raw PDFs and 95% for structured JATS XML. The product is widely deployed in university libraries; the literature on its accuracy is unsettled.

**Springer Nature AI tools (2024–2026).** Springer Nature launched AI tools to: (a) identify irrelevant references in submitted manuscripts (April 2025) [4]; (b) detect suspicious / templated peer reviews [5]. The peer-review-detection tool was *Nature*'s lead story in early 2026 as "the first AI tool to detect suspicious peer reviews rolled out by an academic publisher."

### LLM-as-reviewer systems

**Liang et al. (Stanford, GPT-4 reviewer feedback).** The empirical foundation for the LLM-reviewer literature. Two key papers:

1. *NEJM AI* (2024) / arXiv:2310.01783 — "Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis." [6] Compared GPT-4 feedback to human reviews on 3,096 Nature-family papers and 1,709 ICLR papers. **GPT-4-to-human overlap: 30.85% (Nature), 39.23% (ICLR). Human-to-human overlap: 28.58% (Nature), 35.25% (ICLR).** In a prospective survey of 308 AI/compbio researchers, 57.4% found GPT-4 feedback helpful; 82.4% found it more useful than at least some human reviewers.

2. *Nature Machine Intelligence* 8:326–336 (2026) — Thakkar, Yuksekgonul, Silberg et al. "A large-scale randomized study of large language model feedback in peer review." DOI: 10.1038/s42256-026-01188-x. [7] The follow-up randomized study confirming the result at scale.

These two papers are the most-cited empirical work on AI peer review and the natural benchmark for `reviewer-simulation` to position against.

**Stanford PaperReview.ai.** Agentic system grounded in recent arXiv literature [8]. Reports a Spearman correlation of 0.42 between AI score and a single human reviewer, compared to 0.41 between two human reviewers — a near-identical level of inter-rater consistency. Free to use; intended as author-side feedback.

**AgentReview.** Multi-agent simulation of academic peer review with distinct reviewer / area-chair / author agents [9]. Designed to study the *dynamics* of peer review (e.g., reviewer commitment, the role of intention vs. expertise) rather than to substitute for it.

**ReviewerToo.** Validated on a 1,963-paper ICLR 2025 dataset with official decisions; reports 81.8% binary accept/reject accuracy via a multi-agent ensemble [TODO verify exact citation].

**OpenReviewer** (`maxidl/openreviewer`). Specialized LLM for generating ML-conference reviews. arXiv:2412.11948 [10]. Open-source, narrow-domain.

**Liang et al. "Monitoring AI-Modified Content at Scale."** ICML 2024 [11]. Estimated 6.5–16.9% of ICLR/NeurIPS/CoRL/EMNLP 2024 reviews showed signs of AI modification. This is the "are reviewers already using LLMs?" datapoint — and the answer is "yes, more than journals officially allow."

### Platform-level innovation

**OpenReview.** Free, open-source cloud platform powering peer review for many ML/AI conferences (ICLR, NeurIPS, COLM, AAAI). Features: configurable open peer review, post-publication discussion, **automated reviewer recommendation** via expertise-matching, conflict-of-interest tracking, programmatic API [12]. OpenReview is significant for scriptorium not because of its AI features (which are limited to the recommendation system) but because it demonstrates that **peer review can be structured as transparent, API-accessible state** — exactly the disposition scriptorium takes toward manuscripts.

**ResearchHub.** Decentralized peer review platform co-founded by Brian Armstrong (Coinbase). Uses cryptocurrency (ResearchCoin / RSC) to compensate reviewers — reportedly $150 in RSC per review [13]. Has facilitated >$1.2M in research funding and ~$1M in reviewer earnings. Featured in *Nature* in 2024 as a notable DeSci experiment. The model is contested: critics argue token incentives misalign quality; advocates argue they solve the labor problem of peer review.

### Journal-side AI screening

In addition to Springer Nature's tools, multiple publishers have AI-based image-integrity screening (Imagetwin, ProofIg), text-similarity (iThenticate), and reference-list integrity. These are quality-control rather than peer-review-augmenting tools but share the same disposition: inspectable, rule-or-ML-based pre-screening.

## How this informs scriptorium

- **`reviewer-simulation` lives in a benchmarked space.** Liang's 30.85% overlap, PaperReview.ai's 0.42 Spearman, and ReviewerToo's 81.8% accept/reject accuracy are the comparators. Scriptorium's four-persona output (methodological skeptic, domain expert, translational reviewer, statistical reviewer) should be evaluated against these baselines on the same datasets where possible. The four-persona contract is a hypothesis: that structured, persona-decomposed critique is more useful to authors than monolithic GPT-4 feedback. That hypothesis is testable.
- **Author-side use only.** Elsevier, NIH, and Cell Press ban AI in peer review proper. Springer Nature allows limited use for language editing only. Scriptorium's `reviewer-simulation` is an author-side critique tool — it helps a manuscript get ready for human peer review. The skill description should state this explicitly and should not be repurposed for reviewer-side use without an explicit policy review.
- **scite.ai's failure mode is instructive.** scite's deep-learning citation classifier is widely deployed but unevenly validated, with F-measures spanning 0.0–0.58 across categories. The pattern is: a flashy AI classifier deployed at scale, with mixed independent evaluation, in production. `citation-audit` should aim to be *more conservative* than scite: refuse to assert support/contrast classifications without high confidence, flag uncertainty explicitly, and link back to the cited paper's relevant passage rather than asserting a label.
- **Penelope is the design role model for inspectable critique.** Every flag links to the manuscript text. Every check is named. Critics know why. Scriptorium's structured output discipline should match this.
- **The "are reviewers already using LLMs?" datapoint (6.5–16.9%) reframes the question.** AI is already in peer review — typically without disclosure. The realistic policy question is not "should AI be in peer review?" but "how should AI be transparent and accountable when it is in peer review?" Scriptorium should be designed such that its outputs are inspectable and quotable — a reviewer who uses scriptorium and discloses it should be in a better position than one who silently pastes a paper into ChatGPT.
- **OpenReview's API-accessible state is the architectural cousin.** Like `MANUSCRIPT_STATE.yaml`, OpenReview treats the review process as structured, queryable data. Scriptorium could in principle emit OpenReview-style structured critique that downstream platforms consume.

## Open questions / weak evidence

- **No agreed benchmark for AI-reviewer quality.** Liang et al.'s overlap metric is the de facto standard but is criticized for measuring overlap rather than usefulness. PaperReview.ai's inter-rater correlation is closer to a quality measure but is on a much smaller dataset.
- **The ethics of AI in peer review remain contested across disciplines.** ML/AI conferences (ICLR, NeurIPS) tacitly accept some AI assistance; biomedical journals are stricter; the humanities are mostly hostile. Scriptorium's positioning has to be domain-portable.
- **scite.ai's validation literature is thin.** The most-cited validation studies are from scite's own publications. Independent evaluations have been small-scale, often with conflicting conclusions. A larger independent study would be valuable.
- **Persona-decomposed critique is unbenchmarked.** Scriptorium's four-persona design is design-justified (different reviewers care about different things) but not empirically validated against monolithic critique. Producing such an evaluation would itself be a contribution.
- **The reviewer-labor problem.** ResearchHub's $150-in-RSC reviews show one approach. The unanswered question is whether AI-augmented review can reduce reviewer workload enough to make voluntary peer review sustainable, or whether the structural problem (too many submissions, too few reviewers) requires economic reform.

## References

1. StatReviewer / Aries Editorial Manager integration. https://www.ariessys.com/news-and-events/press-releases/aries-agreement-statreviewer-increases-availability-decision-support-tools-editorial-manager-peer-review-workflow/
2. Nicholson J et al. "scite: A smart citation index that displays the context of citations and classifies their intent using deep learning." *Quantitative Science Studies* 2(3):882–898 (2021). MIT Press. https://direct.mit.edu/qss/article/2/3/882/102990/
3. "Evaluating the Accuracy of scite, a Smart Citation Index." *Hypothesis: Research Journal for Health Information Professionals* (2023). https://journals.indianapolis.iu.edu/index.php/hypothesis/article/view/26528
4. Springer Nature. "New research integrity AI tool added to Springer Nature's growing portfolio." (April 2025) https://group.springernature.com/gp/group/media/press-releases/new-research-integrity-ai-tool/27769148
5. *Nature* news. "First AI tool to detect suspicious peer reviews rolled out by academic publisher." (2026) https://www.nature.com/articles/d41586-026-01454-3
6. Liang W et al. "Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis." *NEJM AI* (2024). arXiv:2310.01783. https://arxiv.org/abs/2310.01783
7. Thakkar N, Yuksekgonul M, Silberg J et al. "A large-scale randomized study of large language model feedback in peer review." *Nature Machine Intelligence* 8:326–336 (2026). DOI: 10.1038/s42256-026-01188-x. https://www.nature.com/articles/s42256-026-01188-x
8. Stanford PaperReview.ai. https://paperreview.ai/tech-overview
9. AgentReview project. https://agentreview.github.io/
10. OpenReviewer. arXiv:2412.11948. https://arxiv.org/abs/2412.11948 ; repo `maxidl/openreviewer`.
11. Liang W et al. "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews." *ICML* (2024). https://proceedings.mlr.press/v235/liang24b.html
12. OpenReview. https://openreview.net/
13. ResearchHub. https://researchhub.com/ ; blog: https://blog.researchhub.foundation/peer-reviewing-on-researchhub/
14. Discussion of AI-in-peer-review policy variation across publishers: Wang et al. "A Cross-Disciplinary Analysis of AI Policies in Academic Peer Review." *Learned Publishing* (2026). https://onlinelibrary.wiley.com/doi/10.1002/leap.2035
