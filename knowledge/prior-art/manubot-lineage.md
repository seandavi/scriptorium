# The manubot lineage: manuscript-as-software

*Last updated: 2026-05-17*

## Synthesis

Manubot (Himmelstein et al., 2019) is the conceptual anchor for scriptorium. It articulated the **manuscript-as-software** pattern: a scholarly manuscript should be a git repository whose source files are plain text, whose builds are automated, whose changes are reviewable as pull requests, and whose citations are identifier-driven rather than copy-pasted bibliographies. Manubot's seven-year track record demonstrates that the pattern works in practice — dozens of papers have been authored in manubot, including the manubot paper itself.

Yet the pattern has limits. The git-based manuscript culture remains a niche of computational biology and the open-science movement. Most scholars still write in Word or Overleaf, with manual citation management. And critically — for the scriptorium thesis — **manubot's coordination model is a build pipeline, not an editorial pipeline**. It tracks who edited what, but it does not have a shared notion of "what this manuscript is arguing," "what the core claims are," "what terminology should be preserved." Those concerns live in author heads, not in the repo.

Scriptorium extends manubot in exactly this way. It adopts the manubot inheritance — git-tracked manuscripts, plain-text source, identifier-driven citations, inspectable transformations — and adds the missing primitive: shared editorial state (`MANUSCRIPT_STATE.yaml`) that AI agents and human authors both read.

## Landscape

### Manubot (the foundational paper)

**Himmelstein DS, Rubinetti V, Slochower DR, Hu D, Malladi VS, Greene CS, Gitter A.** "Open collaborative writing with Manubot." *PLOS Computational Biology* 15(6): e1007128 (2019). DOI: 10.1371/journal.pcbi.1007128. PMID: 31233491. PMC6611653. [1]

Key contributions of the paper:

1. **The pattern.** Manuscripts written in Markdown, stored in git, hosted on GitHub, built continuously into HTML/PDF. Multiple authors propose changes via pull requests; a cloud service evaluates them.
2. **Citation-by-identifier.** Authors write `[@doi:10.1371/journal.pcbi.1007128]` or `[@pubmed:31233491]` and manubot retrieves the metadata and converts to a target style. This eliminates the "wrong bibliography entry" failure mode that plagues Word workflows.
3. **Continuous publication.** When source changes, rendered outputs rebuild and republish to a web page. There is no "submission" event; there is a continuously-current version.
4. **Versioned, immutable history.** The git log is the manuscript's history; nothing is lost.

The software is at `manubot/manubot` (474 stars, last pushed 2026-01-01) [2] and the user-facing template is `manubot/rootstock` (479 stars, last pushed 2026-01-18) [3]. The paper itself was authored in manubot at `greenelab/meta-review` (50 stars, last pushed 2020-05-25) [4] — that repo has not been updated since 2020, a useful datapoint on post-publication maintenance.

### The Greene Lab lineage

The manubot pattern was used for multiple Greene Lab papers and collaborations, most notably the [deep-review project](https://github.com/greenelab/deep-review) on deep learning in biology and medicine. The pattern proved itself at scale (40+ contributors on a single manuscript). The Greene Lab's broader contribution is that *peer-review-grade manuscripts can be authored using software-engineering conventions*: branching, merging, CI, PRs, issue tracking, public version history.

### Quarto Manuscripts (Posit, 2023–)

Quarto is Posit's open-source successor to R Markdown and the most active current development in the manuscript-as-software space.

- `quarto-dev/quarto-cli` has 5,640 stars, last pushed 2026-05-15 [5] — actively maintained.
- "Reproducible Manuscripts with Quarto" (Çetinkaya-Rundel, 2023) at posit::conf [6] introduced the **Quarto Manuscript** project template: a self-contained directory whose source produces HTML, PDF, JATS XML, and a connected `index.qmd` with executable code blocks.
- The USGS published a Quarto manuscript template [7] and *Journal of Fish and Wildlife Management* has a reproducible-manuscript workflow piece [8] — early evidence of journal-side adoption.

Quarto Manuscripts extends manubot in two ways: (a) **executable code embedded in the manuscript** (R, Python, Julia, Observable JS via Jupyter/Knitr); (b) **multi-format build with rich cross-references** (sub-figures, layout panels, hoverable citations, callouts). Where manubot is "manuscript-as-prose-software," Quarto Manuscripts is "manuscript-as-executable-document."

### `quartobot` and Quarto + manubot

Less formalized than either parent. `quartobot` exists as a community pattern combining manubot's citation-by-identifier with Quarto's rendering, but is not a sustained codebase [TODO verify current state]. The conceptual point: Quarto and manubot are converging, with Quarto absorbing most of the manuscript-as-software energy circa 2025–2026.

### Distill.pub

Distill was a peer-reviewed ML journal (founded 2017, supported by Google, OpenAI, DeepMind, Y Combinator Research) [9] that demonstrated **interactive scientific publishing**: articles could include explorable visualizations, live model interactions, and code-driven figures. Articles included Olah's "Building Blocks of Interpretability," Carter & Nielsen's "Using Artificial Intelligence to Augment Human Intelligence," and others that defined a new aesthetic for ML communication.

Distill went on **indefinite hiatus in 2021**. The published explanation cited reviewer burnout, the editorial cost of interactive articles, and the difficulty of sustaining a journal that was also a research artifact. The lesson for scriptorium: **the editorial labor cost of high-quality publication does not vanish when you change the technology** — it shifts. Distill failed not because the tooling was bad but because the editorial pipeline was expensive.

### Idyll

Idyll (Conlen & Heer, ACM UIST 2018, DOI: 10.1145/3242587.3242600) [10] is a markup language for authoring interactive narratives. Repo `idyll-lang/idyll` has 2,033 stars, last pushed 2023-02-04 — effectively dormant. Idyll's intellectual contribution (a structured author interface to JavaScript components, allowing rich interactivity without becoming a web developer) has been largely absorbed by Observable, Quarto, and Svelte-based article systems.

### Observable / Observable Notebooks

Mike Bostock's (d3.js) Observable platform [11] is the most active interactive-publishing environment as of 2026. Observable Notebooks are reactive JavaScript documents with executable cells and inline visualization. The Observable Framework is a static-site generator for data apps. Observable was directly involved with Distill and is conceptually intertwined with the manuscript-as-software pattern.

### What the pattern has and hasn't achieved

**Has:**
- Reproducibility of computational figures (Quarto, Observable).
- Citation accuracy via identifiers (manubot).
- Git-tracked, multi-author manuscript history (manubot, Quarto).
- Open-by-default authoring (manubot, Distill while it lived).
- Continuous publication / no "submission" event (manubot).

**Hasn't:**
- Mainstream adoption. Word and Overleaf still dominate.
- A shared model of *what the manuscript is doing* (claims, terminology, target venue, constraints). Manubot and Quarto track *what is written*, not *what is meant*.
- Editorial workflows beyond the build. There is no "review this PR for argument structure" in the manubot pipeline — only "does it build?" and "do humans approve?"
- AI integration. Manubot pre-dates the LLM era; Quarto post-dates it but does not integrate AI capabilities natively.
- Sustainability of high-end interactive publication (Distill is the cautionary tale).

## How this informs scriptorium

- **Scriptorium is an *editorial layer*, not a manuscript-rendering layer.** Manubot and Quarto handle source → output rendering. Scriptorium handles source → improved-source. The two are complementary: a Quarto manuscript can be the host for `MANUSCRIPT_STATE.yaml`, and scriptorium skills can operate on the Markdown/Qmd source.
- **The `MANUSCRIPT_STATE.yaml` file is the missing primitive in the lineage.** Manubot's `content/` directory and `metadata.yaml` track structure. Quarto's `_quarto.yml` tracks build config. Neither tracks editorial intent. This is exactly where scriptorium contributes.
- **Identifier-driven citations are non-negotiable, but the syntax is not.** The right unit is the persistent identifier itself (DOI / PMID / arXiv ID), not any particular cite-key convention. Manubot's `[@doi:...]` form is one resolver's encoding; CSL-JSON entries, BibTeX entries with verified DOIs, or even plain markdown DOI links (`[DOI: 10.x/y](https://doi.org/10.x/y)`) all satisfy the requirement. Scriptorium's `citation-audit` assumes an identifier-resolved bibliography and refuses to operate on bare-text citations, but is deliberately agnostic to which resolver (manubot, quartobot, biblatex, none) the author uses — see the "Skill citation discipline" section in `CONTRIBUTING.md`.
- **Distill's failure mode is a design lesson.** The editorial labor of producing a great paper does not go away when you add AI; it gets redistributed. Scriptorium should be designed so that AI capabilities reduce the *load* on editorial labor, not just add a new ingestion task ("now you also have to maintain this YAML file").
- **The greenelab/meta-review repo's 2020-05-25 last-commit date is a sustainability signal.** The manubot paper itself stopped being maintained five years ago. Scriptorium will face the same pull. The defense is: keep the surface area small, document the pattern such that others can carry it, and make `MANUSCRIPT_STATE.yaml` valuable enough that authors maintain it whether or not the toolchain is alive.

## Open questions / weak evidence

- **No published evaluation of manubot's claimed benefits.** The 2019 paper makes the case theoretically; there is no empirical study (then or since) of whether manubot manuscripts are better, more accurate, more reproducible, or more widely cited than Word-authored equivalents. Scriptorium could contribute by being designed for evaluation from the start.
- **Quarto Manuscripts is still pre-mainstream.** USGS adoption is encouraging, but the workflow is most common among R-centric researchers. JATS XML output is the strongest signal for journal-side integration.
- **The manubot/Quarto convergence is partial.** Quarto has not absorbed identifier-driven citations as a first-class concept (it supports CSL but citation entries are still local). A formal bridge would be valuable.
- **The "is markdown enough for science?" debate is unsettled.** Word-style track changes, semantic comments, and graphical annotation are difficult to replicate in pure-text workflows. The biggest practical adoption blocker is not the tooling but the social workflow of co-author commentary.

## References

1. Himmelstein DS, Rubinetti V, Slochower DR, Hu D, Malladi VS, Greene CS, Gitter A. "Open collaborative writing with Manubot." *PLOS Computational Biology* 15(6): e1007128 (2019). DOI: 10.1371/journal.pcbi.1007128. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007128
2. manubot/manubot GitHub. https://github.com/manubot/manubot (474 stars; pushedAt 2026-01-01).
3. manubot/rootstock GitHub. https://github.com/manubot/rootstock (479 stars; pushedAt 2026-01-18).
4. greenelab/meta-review GitHub. https://github.com/greenelab/meta-review (50 stars; pushedAt 2020-05-25).
5. quarto-dev/quarto-cli GitHub. https://github.com/quarto-dev/quarto-cli (5,640 stars; pushedAt 2026-05-15).
6. Çetinkaya-Rundel M. "Reproducible Manuscripts with Quarto." posit::conf 2023. https://mine.quarto.pub/manuscripts-conf23/
7. USGS. "A Reproducible Manuscript Workflow with a Quarto Template." https://www.usgs.gov/publications/a-reproducible-manuscript-workflow-a-quarto-template
8. *Journal of Fish and Wildlife Management*. "A Reproducible Manuscript Workflow With a Quarto Template." 15(1):251. https://meridian.allenpress.com/jfwm/article/15/1/251/501496/A-Reproducible-Manuscript-Workflow-With-a-Quarto
9. Distill journal. https://distill.pub/about/ ; Wikipedia entry on Distill (journal). Indefinite hiatus announcement: https://distill.pub/2021/distill-hiatus/
10. Conlen M, Heer J. "Idyll: A Markup Language for Authoring and Publishing Interactive Articles on the Web." ACM UIST 2018. DOI: 10.1145/3242587.3242600. https://dl.acm.org/doi/10.1145/3242587.3242600 ; repo idyll-lang/idyll (2,033 stars; pushedAt 2023-02-04).
11. Observable. https://observablehq.com/
