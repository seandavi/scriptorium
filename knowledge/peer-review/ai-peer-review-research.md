# AI Peer Review: What's Validated, What's Speculative

*Last updated: 2026-05-17*

## Synthesis

The literature on LLMs as peer reviewers is young (most substantive work is 2023–2026), contested, and moving fast. Two findings have begun to replicate. First, large-scale empirical work (Liang et al. 2024, *NEJM AI* / Stanford-led) shows that GPT-4–generated feedback overlaps with human reviewer feedback at roughly the same rate that two human reviewers overlap with each other — ~30% point-overlap on Nature-family papers, ~39% on ICLR papers, versus ~28% and ~35% for human–human comparisons [1]. Second, randomized field experiments (Liang et al. 2026, *Nature Machine Intelligence*; ICLR 2025 with >20,000 reviews) show that giving reviewers AI-generated feedback before they finalize their own reviews increases review informativeness and engagement, with ~27% of reviewers updating their reviews in response [2].

These results are not, however, evidence that LLMs can *replace* peer review. The most-cited normative paper (Hosseini & Horbach 2023, *Research Integrity and Peer Review*) is explicit: LLM reviewers "amplify human biases, miss critical flaws, and remain susceptible to adversarial attacks such as prompt injection," and "the fundamental opacity of LLMs' inner workings... raise questions and concerns about potential biases and the reliability of review reports" [3]. The two most-cited specific failure modes are (a) hallucinated citations and missing prior work, and (b) surface-level engagement — critiques that sound competent but do not interrogate study design at depth.

Editorial policy has converged faster than the science. Nature Portfolio, Science, and most major publishers as of 2025 prohibit uploading manuscripts to public-facing generative AI tools (a confidentiality concern, not primarily a quality one), require disclosure when AI tools materially contribute to review, and reserve final editorial judgment for humans [4]. The policy stance is conservative: AI may *support* peer review, not perform it.

Scriptorium's `reviewer-simulation` skill is positioned within this consensus, not against it. The skill simulates reviewer attention to help authors stress-test their own manuscript *before* submission. It is not a substitute for editorial peer review, does not produce ratings or recommendations, and operates with explicit awareness of the failure modes the literature documents.

## Evidence

**Liang et al. (2024) — the large-scale comparison [1, 5].** Published in *NEJM AI* (2024) and the methodologically detailed Stanford manuscript that fed *Nature Human Behaviour* coverage. Method: prompt GPT-4 with a complete paper PDF and a standardized peer-review elicitation prompt; compare the generated feedback to actual reviewer feedback on the same papers using both retrospective overlap (15 Nature family journals, 3,096 papers; ICLR 2022, 1,709 papers) and prospective user study (308 researchers from 110 institutions in AI and computational biology).

- Retrospective overlap of points raised: GPT-4 vs. human reviewer mean overlap = 30.85% (Nature) / 39.23% (ICLR); human vs. human mean overlap = 28.58% / 35.25%.
- 57.4% of users in the prospective study rated GPT-4 feedback "helpful" or "very helpful"; 82.4% found it more beneficial than at least one human reviewer they had received.
- Limitations the authors flag: GPT-4 feedback over-indexes on superficial aspects (writing, organization) relative to human reviewers, who attend more to design and significance.

**Liang et al. (2026, *Nature Machine Intelligence*) — randomized RCT in production [2].** Randomized trial at ICLR 2025: >20,000 reviews. Reviewers receiving LLM-generated draft feedback before finalizing their reviews produced more informative reviews; 27% updated their reviews based on AI suggestions. This is the first large-scale RCT showing causal effect of AI on review *quality as judged by authors and editors*, not just overlap. The study supports AI-as-assist; it does not test AI-as-replace.

**Hosseini & Horbach (2023) — the conceptual critique [3].** *Research Integrity and Peer Review* (BMC), the most cited normative paper on LLM peer review. Key claims: LLMs can reduce reviewer fatigue and assist in drafting reports, but (i) confidentiality is broken by uploading manuscripts to public services; (ii) LLMs lack reasoning over methodology in many domains; (iii) bias inherited from training data may compound bias already present in human review; (iv) prompt-injection attacks on review-time LLM use are plausible. The paper's recommendations: disclose AI use, retain human accountability, do not upload to public-facing tools.

**Hallucinated citations and surface engagement.** Multiple 2024–2025 analyses document hallucinated references in AI-assisted writing and review. GPTZero (commercial analysis) reported ~50 ICLR submissions with at least one obviously hallucinated citation [6]. Independent academic analyses (e.g., "HalluCitation Matters," arXiv 2601.18724 [TODO verify]) document that across major venues, the share of papers with at least one suspect citation has risen sharply 2021→2025. Mitigations identified: mandatory citation grounding, section-wise ingestion, "critique-then-verify" workflows that bind every critique to explicit textual evidence.

**Detection is unreliable.** A 2025 *Nature* news piece, "AI is transforming peer review — and many scientists are worried," summarizes findings that AI-text detection tools fail to identify most LLM-generated peer reviews; estimates of LLM-influenced reviews at major AI conferences range from 6.5% to 16.9% [7]. This makes editorial policy enforcement difficult.

**Editorial policy synthesis (2025) [4].** Nature Portfolio's policy: (a) LLMs do not meet authorship criteria; (b) AI use in writing must be disclosed in Methods; (c) AI-assisted copy editing does not require disclosure; (d) "absolute consensus prohibiting editors and peer reviewers from uploading any portion of a submitted manuscript into a public-facing generative AI tool"; (e) if AI was used to evaluate the manuscript, reviewers must declare it transparently. Science and most other major publishers have aligned variants.

## How this informs scriptorium

Scriptorium threads the needle by being explicit about three things the literature converges on:

1. **Author-side use, not editorial-side use.** `reviewer-simulation` runs against the author's own manuscript before submission. There is no confidentiality issue (the author owns the text), no editorial-policy violation (the skill is not used as part of journal peer review), and no inference about acceptance/rejection.

2. **Structured outputs, evidence-bound critiques.** Following the "critique-then-verify" pattern from the AI-peer-review failure literature: every critique scriptorium surfaces should cite a specific manuscript passage (line/section reference) and a specific concern category from [[common-critiques-taxonomy]]. Critiques without textual anchors should be suppressed or down-weighted. This addresses the surface-engagement failure mode head-on.

3. **No hallucinated citations.** Per the DESIGN.md "no citation hallucination" rule, `reviewer-simulation` may identify *missing prior work as a concern* (e.g., "this claim would benefit from comparison to the prior art in X") but must not invent specific citations. The `citation-audit` skill handles citation issues with verifiable provenance.

4. **Acknowledged limitations as a first-class output.** Scriptorium's simulated reviews should end with an explicit "limitations of this simulation" section: which families of critique were under-explored, which the model is structurally weaker at (typically: deep methodological grounding in unfamiliar subfields), and where human review remains necessary. This is what the Hosseini & Horbach recommendations look like operationally.

5. **Not a substitute for editorial review.** Scriptorium's README and skill cards should be explicit: this is a stress-test, not a substitute. The empirical evidence (Liang 2024, 2026) supports AI as a *complement* to human review — useful when paired with human judgment, not as a replacement.

## Open questions / weak evidence

- **Does the overlap finding (Liang 2024) generalize beyond CS/ML and Nature-family biomed?** The two domains tested are well-represented in GPT-4's training data and have unusually structured review traditions. Humanities, social science, and small-field domains are unstudied.
- **Are the "helpful" ratings authors give to LLM feedback measuring quality or fluency?** The user-study evidence is suggestive but cannot distinguish "this critique is right" from "this critique is well-written and plausible-sounding." Some 2025 commentary (e.g., the *Nature* news piece) raises this concern explicitly [7].
- **Adversarial robustness.** Prompt-injection attacks against review-time LLM use are documented in proof-of-concept but not at scale. The 2025 arXiv paper "BadScientist" [TODO verify exact DOI] explores whether an LLM-generated paper can fool LLM reviewers; results are preliminary and concerning.
- **The agentic-pipeline question.** Almost all published evidence concerns single-call LLM review (one prompt → one review). Scriptorium's multi-skill architecture (citation-audit + reviewer-simulation + argumentative-flow + …) is not directly tested in the literature. Whether composed agentic critique outperforms single-call critique is the empirical question scriptorium itself is structured to answer.
- **Pre-print vs. peer-reviewed status.** The Liang 2024 *NEJM AI* paper is peer-reviewed. The 2026 *Nature Machine Intelligence* RCT is peer-reviewed. Several supporting findings cited here (HalluCitation Matters, BadScientist, the AI-detection benchmark papers) are arXiv pre-prints and should be treated as preliminary.

## References

1. Liang W, Zhang Y, Cao H, Wang B, Ding DY, Yang X, Vodrahalli K, He S, Smith DS, Yin Y, McFarland DA, Zou J. Can large language models provide useful feedback on research papers? A large-scale empirical analysis. *NEJM AI* 1(8) (2024). DOI: [10.1056/AIoa2400196](https://doi.org/10.1056/AIoa2400196). Code: https://github.com/Weixin-Liang/LLM-scientific-feedback.
2. Liang W et al. A large-scale randomized study of large language model feedback in peer review. *Nature Machine Intelligence* (2026). DOI: [10.1038/s42256-026-01188-x](https://doi.org/10.1038/s42256-026-01188-x) [TODO verify exact DOI].
3. Hosseini M, Horbach SPJM. Fighting reviewer fatigue or amplifying bias? Considerations and recommendations for use of ChatGPT and other large language models in scholarly peer review. *Research Integrity and Peer Review* 8: 4 (2023). DOI: [10.1186/s41073-023-00133-5](https://doi.org/10.1186/s41073-023-00133-5). PMID: 36865238.
4. Nature Portfolio editorial policies — Artificial Intelligence (AI). https://www.nature.com/nature-portfolio/editorial-policies/ai. (Accessed 2026-05.)
5. Liang W et al. Stanford preprint and *Nature Human Behaviour* version of the large-scale comparison. https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf [TODO verify final DOI].
6. GPTZero analysis of ICLR submissions with hallucinated citations (2025). Reported widely in academic press; original GPTZero post and *The Decoder* coverage. [TODO verify a peer-reviewed source rather than commercial blog.]
7. "AI is transforming peer review — and many scientists are worried." *Nature* news (2025). https://www.nature.com/articles/d41586-025-00894-7. (News piece; not peer-reviewed research, but synthesizes the field's concerns.)

See also: [[reviewer-archetypes-evidence]], [[common-critiques-taxonomy]], [[critique-quality-evidence]].
