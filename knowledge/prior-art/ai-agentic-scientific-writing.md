# Agentic AI for scientific writing and discovery

*Last updated: 2026-05-17*

## Synthesis

The agentic-AI-for-science landscape circa mid-2026 is bifurcated. On one side are **fully-autonomous research systems** (Sakana's AI Scientist, FutureHouse's Crow/Falcon/Owl/Phoenix, Stanford's CellVoyager) that aim to do science end-to-end: hypothesis, code, experiment, manuscript, review. On the other are **single-task agents** (AutoBA for bioinformatics pipelines, GeneAgent for gene-set annotation, ChemCrow/Phoenix for synthesis planning) that wrap LLMs around domain APIs to make one capability more reliable. The first group makes large claims that are only partially validated; the second group makes narrower claims that hold up better in benchmarking.

What is conspicuously absent from this landscape is anything that treats **manuscript improvement as the unit of work**. The fully-autonomous systems generate manuscripts as a side-effect of doing research; they do not iteratively improve a manuscript that a human has drafted. The single-task agents do not concern themselves with prose at all. The closest neighbor is the AI-peer-review work (Liang et al., AgentReview, OpenReviewer, Stanford's PaperReview.ai), which produces critique but does not coordinate revision.

Scriptorium occupies that gap. It is not trying to write papers from scratch and it is not trying to replace peer review. It is trying to be the operating layer that sits between the human author and the agents, with `MANUSCRIPT_STATE.yaml` as the editorial source of truth — the thing none of the above systems have.

## Landscape

### Fully-autonomous research / writing systems

**Sakana AI Scientist (Lu et al., 2024)** — The most-cited end-to-end system. The original arXiv paper (arXiv:2408.06292) [1] proposed a pipeline that generates ideas, writes code, runs experiments, produces a manuscript, and runs a simulated review. The GitHub repo `SakanaAI/AI-Scientist` has 13,640 stars and was last pushed 2025-12-19 [2]. A v2 successor (`SakanaAI/AI-Scientist-v2`, 6,267 stars, last pushed 2025-12-19) was released, and a paper describing the system was published in *Nature* in March 2026 [3]. Notably, Sakana reports an unedited AI-generated paper passing peer review at the ICLR 2025 'ICBINB' workshop, outperforming 55% of human papers there.

The independent evaluation by Beel et al. (arXiv:2502.14297) [4] is unsparing: 42% of experiments failed due to coding errors; literature reviews used simplistic keyword search and misclassified established concepts (e.g., micro-batching for SGD) as novel; generated papers had a median of 5 citations; outputs contained structural errors including missing figures and placeholder text like "Conclusions Here". Cost was the headline finding: complete papers for $6–15. Sakana addressed many critiques in v2 by removing the human template dependency.

**FutureHouse platform (Crow, Falcon, Owl, Phoenix)** — Launched 2025-05-01 by the Eric-Schmidt-backed nonprofit FutureHouse, headed by Andrew White [5]. Crow is the production version of the open-source PaperQA2 (`Future-House/paper-qa`, 8,497 stars, last pushed 2026-03-20 [6]) and is a literature-QA agent. Falcon is the deep-review agent with access to specialized databases (OpenTargets, etc.). Owl ("HasAnyone") answers "Has anyone done X before?". Phoenix is an evolution of ChemCrow for chemistry. FutureHouse claims Crow/Falcon/Owl have been "experimentally validated" as having "better precision than PhD-level researchers in head-to-head literature search tasks" [5]. On the LitQA benchmark, expert biologists scored ~67% while the FutureHouse models scored ~90% in blind tests [7]. The platform is free with API access.

**CellVoyager (Alber, Chen, Zou et al., Stanford)** — Published in *Nature Methods* (May 2026 [8], bioRxiv 2025-06-03). An LLM-based agent that autonomously explores scRNA-seq datasets in a live Jupyter environment, generating and refining "exploration blueprints." Reported to outperform GPT-4o and o3-mini by up to 23% in predicting which analyses the original authors conducted, given only the papers' background sections. In three case studies (COVID-19, cell–cell communication, aging), expert reviewers consistently rated CellVoyager-generated findings as creative and scientifically sound.

### Single-task biomedical / bioinformatics agents

**AutoBA (Zhou et al., 2024, KAUST)** — Published in *Advanced Science* [9]. An agent that takes three inputs (data path, data description, objective) and autonomously produces analysis plans, code, and execution. Supports WGS/WES, ChIP-seq, RNA-seq, scRNA-seq, spatial transcriptomics. Has an automated code repair (ACR) mechanism. Repo: `JoshuaChou2018/AutoBA`, 227 stars, last pushed 2024-11-04 [10]. Activity has slowed since publication — a useful warning sign about post-paper sustainability.

**GeneAgent (Wang et al., NIH NLM)** — Published in *Nature Methods* (August 2025, 22:1677–1685 [11], arXiv:2405.16205 preprint). A self-verification language agent that interacts with 18 biomedical databases via 4 Web APIs to verify its own gene-set annotations. Four-stage pipeline: generate, self-verify, modify, summarize. On 1,106 gene sets, GeneAgent was "consistently more accurate than GPT-4 by a significant margin." Repo: `ncbi-nlp/GeneAgent`, 110 stars, last pushed 2025-12-25.

**Biomni (Stanford)** — General-purpose biomedical AI agent integrating 105 software tools, 150 specialized biological tools, 59 databases (bioRxiv 2025.05.30 [12]). Benchmarked on causal gene prioritization, drug repurposing, rare disease diagnosis, microbiome analysis, molecular cloning. Available at biomni.stanford.edu.

**ChemCrow / Phoenix** — Tool-using LLM for synthesis planning, evolved into FutureHouse Phoenix. The benchmarking is thinner than the other FutureHouse agents.

### AI-peer-review systems (closest neighbors to scriptorium's `reviewer-simulation`)

**Liang et al.** — Two studies. The first (NEJM AI, arXiv:2310.01783) compared GPT-4 feedback to human reviewers on 3,096 Nature-family papers and 1,709 ICLR papers; GPT-4–to-human overlap was 30.85% (Nature) and 39.23% (ICLR), comparable to human-to-human overlap of 28.58% and 35.25% respectively; 57.4% of 308 surveyed researchers found GPT-4 feedback helpful, 82.4% found it more useful than some human reviewers [13]. A follow-up randomized study was published in *Nature Machine Intelligence* (8:326–336, 2026) [14].

**Stanford PaperReview.ai** — Agentic system grounded in arXiv literature. Reports a Spearman correlation of 0.42 between AI score and human score, versus 0.41 between two human reviewers [15].

**AgentReview** — Multi-agent simulation of peer review with reviewers, area chairs, and authors as distinct LLM agents [16]. **ReviewerToo** — Validated on 1,963 ICLR 2025 papers with 81.8% binary accept/reject accuracy. **OpenReviewer** (`maxidl/openreviewer`) — A specialized LLM for generating critical reviews (arXiv:2412.11948).

**Springer Nature** — Launched the first publisher-side AI tool for detecting suspicious peer reviews in 2026 [17] plus tools for irrelevant-reference detection.

### General-purpose "research assistant" agents

**Genspark Super Agent** — Multi-model "super agent" that produces Sparkpages (dynamically synthesized research documents). Marketed broadly; no peer-reviewed evaluation of research-quality outputs.

**SciSpace Agent** — Bills itself as uniting 150+ academic tools (covered in [[ai-writing-tools-survey]]).

**Jenni** — Workspace-style writing assistant with citation tracing.

### What "claims" vs. "demonstrated outputs" looks like across this space

| System | Headline claim | Demonstrated output |
|---|---|---|
| Sakana AI Scientist v1/v2 | Fully autonomous discovery | Workshop-accepted paper; 42% experiment failure rate; thin citations |
| FutureHouse Crow/Falcon | "Better than PhDs" on LitQA | 90% vs. 67% on a narrow benchmark; no end-to-end paper evidence |
| CellVoyager | Novel scientific findings | 3 case studies rated creative by experts; 23% improvement on author-prediction proxy |
| AutoBA | Fully automated multi-omic analysis | Works across many pipelines; activity has stalled post-publication |
| GeneAgent | Reduced hallucinations via DB verification | Significant accuracy gain over GPT-4 on 1,106 gene sets |
| AgentReview / OpenReviewer | Simulated peer review | Useful for studying review dynamics; not yet a substitute |

## How this informs scriptorium

- **Scope discipline.** None of the fully-autonomous systems coordinates iterative improvement of a human-authored manuscript. Scriptorium's positioning is "operating system between author and agents," not "another autonomous researcher." This is a genuinely empty seat.
- **Single-responsibility as a design principle, not just a preference.** AutoBA's slowing activity and Sakana's 42% experiment-failure rate are warnings: wide-scope agents are hard to maintain and harder to trust. Scriptorium's leaf skills (`citation-audit`, `reviewer-simulation`, `argumentative-flow`) are a deliberate bet that narrow + composable beats wide + autonomous.
- **`reviewer-simulation` is in a contested arena.** Liang et al.'s 30.85% overlap result is the baseline this skill should be benchmarked against. PaperReview.ai's 0.42 Spearman is a closer comparison. Scriptorium should publish how its four-persona output compares to single-LLM review.
- **Domain databases ground hallucinations.** GeneAgent's self-verification pattern (generate → check against DB → modify → summarize) is directly transferable to `citation-audit`: every citation claim should be verifiable against Crossref/PubMed metadata before it lands in the audit report.
- **Manuscript state is the missing primitive.** FutureHouse has agents but no shared editorial state. Sakana has a pipeline but no editorial state. The scriptorium thesis — that `MANUSCRIPT_STATE.yaml` is the gravity well — is testable against this absence.

## Open questions / weak evidence

- **No published evaluation of any "manuscript improvement" agent on real revisions.** All evaluations to date measure either generation quality or critique overlap, not whether agent-assisted revisions actually result in better papers (by reviewer scores, acceptance rates, citation counts). This is the evaluation scriptorium should aim to produce.
- **The "AI peer reviewer" question is unresolved as a policy matter.** Elsevier bans AI in peer review; Springer Nature allows limited use; NIH prohibits it for grant review. Scriptorium's `reviewer-simulation` is for self-use by authors, not for use *as* peer review — that distinction needs to remain crisp in documentation. See [[peer-review-platforms]].
- **Post-paper sustainability is the dominant failure mode.** AutoBA's activity dropped sharply after publication; meta-review (the manubot manuscript itself) has not been updated since 2020. Scriptorium needs a story for how it stays alive past v0.1.
- **No standard benchmark for manuscript-improvement agents exists.** LitQA exists for retrieval; ICLR papers exist for review; there is no equivalent for "manuscript before vs. after." Building one would itself be a contribution.

## References

1. Lu C, Lu C, Lange RT, Foerster J, Clune J, Ha D. "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." arXiv:2408.06292 (2024). https://arxiv.org/abs/2408.06292
2. SakanaAI/AI-Scientist GitHub. https://github.com/SakanaAI/AI-Scientist (13,640 stars; pushedAt 2025-12-19).
3. Lu et al. "The AI Scientist: Towards Fully Automated AI Research." *Nature* (2026). Sakana announcement: https://sakana.ai/ai-scientist-nature/
4. Beel J, et al. "Evaluating Sakana's AI Scientist for Autonomous Research." arXiv:2502.14297 (2025). https://arxiv.org/abs/2502.14297
5. FutureHouse Platform launch. https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents
6. Future-House/paper-qa GitHub. https://github.com/Future-House/paper-qa (8,497 stars; pushedAt 2026-03-20).
7. MIT News. "Accelerating scientific discovery with AI." 2025-06-30. https://news.mit.edu/2025/futurehouse-accelerates-scientific-discovery-with-ai-0630
8. Alber S, Chen B, Zou J, et al. "CellVoyager: AI CompBio agent generates new insights by autonomously analyzing biological data." *Nature Methods* (2026). https://www.nature.com/articles/s41592-026-03029-6
9. Zhou J, et al. "An AI Agent for Fully Automated Multi-Omic Analyses." *Advanced Science* (2024). DOI: 10.1002/advs.202407094
10. JoshuaChou2018/AutoBA GitHub. https://github.com/JoshuaChou2018/AutoBA (227 stars; pushedAt 2024-11-04).
11. Wang Z, et al. "GeneAgent: self-verification language agent for gene-set analysis using domain databases." *Nature Methods* 22:1677–1685 (2025). DOI: 10.1038/s41592-025-02748-6. arXiv:2405.16205.
12. Biomni team. "Biomni: A General-Purpose Biomedical AI Agent." bioRxiv 2025.05.30.656746. https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1
13. Liang W, et al. "Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis." *NEJM AI* (2024). arXiv:2310.01783.
14. Thakkar N, Yuksekgonul M, Silberg J, et al. "A large-scale randomized study of large language model feedback in peer review." *Nature Machine Intelligence* 8:326–336 (2026). DOI: 10.1038/s42256-026-01188-x
15. Stanford PaperReview.ai. https://paperreview.ai/tech-overview
16. AgentReview project. https://agentreview.github.io/
17. *Nature* news. "First AI tool to detect suspicious peer reviews rolled out by academic publisher." 2026. https://www.nature.com/articles/d41586-026-01454-3
