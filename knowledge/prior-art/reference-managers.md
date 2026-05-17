# Reference managers and citation philosophy

*Last updated: 2026-05-17*

## Synthesis

Reference managers are the closest thing scholarly writing has to a piece of widely-adopted infrastructure. Almost every researcher uses one; the ecosystem is mature; the file formats (BibTeX, RIS, CSL-JSON) are interoperable; and the philosophical differences between products are real — open-source-community (Zotero) vs. publisher-owned (Mendeley) vs. modern-commercial (Paperpile) vs. legacy-enterprise (EndNote).

What unifies them is a focus on **citation throughput**: getting references into a library, formatting them in a target style, generating bibliographies. What is conspicuously absent across all of them is **citation accuracy at the claim level** — that is, whether the cited work actually supports the claim it is attached to. This is the gap scite.ai partially addresses (covered in [[peer-review-platforms]]) and that scriptorium's `citation-audit` is designed to fill at the manuscript level.

The LLM-integration story across reference managers is uneven and largely community-driven. Zotero has the richest plugin ecosystem (Aria, llm-for-zotero, local-LLM workflows). Paperpile, EndNote, and Mendeley have mostly added LLM features as marketing surface rather than as deep integrations. Better BibTeX remains the indispensable bridge from any reference manager to LaTeX/Markdown workflows.

For scriptorium, the implication is clear: don't replace the reference manager, but assume one exists, expose its bibliography as the citation source of truth, and operate at the claim/citation linkage level that no reference manager touches.

## Landscape

### Zotero

**What it is.** Free, open-source reference manager from the Roy Rosenzweig Center for History and New Media. Cross-platform (Windows, Mac, Linux). Integrates with Word, LibreOffice, Google Docs, and OnlyOffice.

**Repo.** `zotero/zotero` has 14,179 stars, last pushed 2026-05-13 [1] — among the most active scholarly-software repos.

**Editorial philosophy.** Open-source, community-governed, data-portable. Local-first storage with optional sync. No tracking by default. The 2024 release of Zotero 7 modernized the UI and exposed a local HTTP API that enables third-party integrations.

**LLM integration story.** Zotero is the platform of choice for LLM-curious researchers because of its plugin ecosystem and local API.
- **Aria** (AI Research Assistant) — community plugin embedding LLM chat in Zotero [2].
- **llm-for-zotero** (`yilewang/llm-for-zotero`) — side-panel chat in the PDF reader; works with any OpenAI-compatible API including local models via Ollama [3].
- **Local-LLM workflows** — researchers connect Zotero to local Ollama/Open WebUI for private LLM analysis of personal libraries.

**Strengths.** Most flexible. Most private. Best for power users.

**Weaknesses.** Setup-heavy. Sync quotas; cloud storage is paid above 300 MB.

### Mendeley (Elsevier)

**What it is.** Reference manager and academic social network, acquired by Elsevier in 2013.

**Editorial philosophy and controversy.** The Elsevier acquisition was contested. David Dobbs's *New Yorker* commentary [4] suggested Elsevier's motive could have been "to acquire its user data and/or to destroy or co-opt an open-science icon that threatens its business model." Subsequent events did not allay concern:
- 2018: An update caused users to lose PDFs and annotations [5].
- 2021: Mobile apps removed from iOS/Android stores.
- 2022: Mendeley Desktop downloads discontinued in favor of a web-based product.
- 2024–2025: Elsevier planned to discontinue Mendeley Desktop entirely; community pushback caused a reversal in July 2025.

Privacy concerns about reading-habit and citation-pattern data being used by Elsevier persist and are unresolved.

**LLM integration story.** Limited and publisher-driven. No plugin ecosystem comparable to Zotero's. Elsevier's broader Scopus AI and ScienceDirect AI features sit alongside but are not deeply integrated into Mendeley.

**Strengths.** Free to start. Easy onboarding. Familiar to many researchers.

**Weaknesses.** Trust deficit. Active migration off Mendeley by open-science-aligned researchers is common; the standard advice in ResearchGate threads and university LibGuides is to migrate to Zotero or Paperpile.

### Paperpile

**What it is.** Commercial cloud-only reference manager built around Google Docs and the Google ecosystem. $2.99/month for academics; iOS/Android apps; Chrome extension. Started as a Chrome-only product, expanded to a standalone web app and mobile.

**Editorial philosophy.** Modern-commercial. Tight Google integration is the value proposition: PDF scraping into Google Drive, inline citation insertion in Google Docs, fast search across large libraries. The product mark is reliability and polish, not openness.

**LLM integration story.** Paperpile has been adding AI features — including chat with library, summarization — through its main product, not via a third-party plugin model. Less openness than Zotero, more polish than Mendeley.

**Strengths.** Best Google Docs integration in the market. Fast. Affordable. Cloud-first.

**Weaknesses.** No local storage option. Less portable than Zotero. Vendor lock-in for Word-heavy workflows.

### EndNote (Clarivate)

**What it is.** The legacy enterprise reference manager. Sold as a perpetual license (~$300) rather than subscription. Owned by Clarivate, which also owns Web of Science.

**Editorial philosophy.** Comprehensive feature set, integration with Web of Science as a data source, retraction alerts as you write, large-team collaboration (up to 400 co-authors on a synced library) [6].

**LLM integration story.** EndNote 2025 announced AI features — primarily abstract summarization and "smarter" searching. The integration is closed and publisher-owned, like Mendeley. No plugin ecosystem.

**Strengths.** Institutional-grade. Web of Science integration. Stable.

**Weaknesses.** Expensive. Slow innovation. Heavy. The user base is aging.

### Zettlr

**What it is.** Free, open-source Markdown editor explicitly designed for academic writing, built by Hendrik Erz. Cross-platform.

**Editorial philosophy.** Markdown-first, Zettelkasten-friendly, no telemetry, no cloud, no forced sync. Integrates with Zotero/JabRef/Juris-M for citations. Exports via Pandoc to 30+ formats [7].

**Strengths for scriptorium-style workflows.** Zettlr is one of the few editors that natively supports `[@doi:...]`-style citations against an external library, has Pandoc-grade export, and respects plain-text-first conventions. It is the spiritual cousin of the manubot/Quarto pattern at the editor level.

**Weaknesses.** Solo-author workflow primarily; weaker on multi-author co-editing than Google Docs / Overleaf.

### Better BibTeX (Zotero plugin)

**What it is.** A Zotero plugin by `retorquere/zotero-better-bibtex` (6,689 stars, last pushed 2026-05-16) [8] that gives Zotero LaTeX-grade BibTeX export with **stable, pinned citation keys**, automatic export-on-save, and rich customization of citation-key format.

**Why it matters.** Without Better BibTeX, Zotero generates citation keys that can change when metadata is updated, breaking citations in any LaTeX manuscript. Better BibTeX's "pin" mechanism guarantees a citation key once assigned remains stable. As of Zotero 8, pinning is automatic — a notable change that brings the broader Zotero ecosystem closer to LaTeX users' expectations.

**Editorial philosophy.** "Citations are infrastructure; stability matters more than perfection." This is the exact disposition scriptorium needs from a reference layer.

### Other tools worth a mention

- **JabRef** — Java-based BibTeX/biblatex reference manager. Popular in LaTeX-heavy domains.
- **Citavi** — Was the Windows-focused academic suite; acquired by QSR / Lumivero in 2021; market position has narrowed.
- **ReadCube Papers** — Closed-commercial, sold to Digital Science (same parent as Writefull).
- **Bibtex / biblatex** — The underlying file format. CSL-JSON is the increasingly-dominant JSON-native alternative.

## How this informs scriptorium

- **Don't try to be a reference manager.** Scriptorium's `citation-audit` skill assumes a bibliography exists. The skill's contract should be: *given a manuscript with citations and a resolvable bibliography (BibTeX, CSL-JSON, or DOIs-only), assess whether the claims are appropriately supported*. It is not the skill's job to format references, sync libraries, or deduplicate entries.
- **Better BibTeX is the precedent for "infrastructure that supports manuscripts as software."** A plugin to a reference manager that exists primarily to make citation keys stable for downstream tooling — that's exactly the supporting-infrastructure mindset scriptorium needs from upstream tools, and exactly what it should not try to replicate.
- **Zotero is the natural reference partner.** Open API, plugin culture, local-first storage, identifier-driven CSL-JSON output. A scriptorium recipe that says "use Zotero + Better BibTeX + manubot/Quarto + scriptorium" is internally coherent.
- **The Mendeley story is a strategic warning.** Open-source vault → publisher acquisition → trust erosion → migration. Scriptorium's MIT license and minimal-vendor-state design protect against this failure mode, but only if the project itself remains community-maintained.
- **Identifier-resolution is non-negotiable for AI-assisted citation work.** Citation hallucination is a well-known LLM failure mode. The defense is: the LLM never invents a DOI; it operates on the bibliography that the reference manager has already verified.
- **Most reference managers have weak LLM integration.** This is the scriptorium opportunity. The skills should be designed such that a reference manager's exported bibliography (CSL-JSON in particular) can feed `citation-audit` directly, and the audit's output is structured enough that a human can take it back to the reference manager for fixes.

## Open questions / weak evidence

- **No published evaluation of citation accuracy across reference managers.** The community knows from experience that auto-fetched metadata varies in quality (especially for older or non-DOI references), but there is no recent benchmark.
- **The LLM-integration arms race is early.** Aria, llm-for-zotero, and similar plugins are 2024–2025 efforts; their long-term sustainability is uncertain. Scriptorium should not depend on any specific plugin.
- **CSL-JSON vs. BibTeX is not yet a settled choice.** LaTeX users prefer BibTeX/biblatex; modern web/Markdown workflows prefer CSL-JSON. Scriptorium should consume either; producing CSL-JSON internally is the conservative bet.
- **The "do these citations actually support the claims?" problem has no commercial product.** scite.ai (see [[peer-review-platforms]]) classifies citation *intent* in already-published literature but does not audit a draft manuscript's citation/claim alignment. This is scriptorium's most defensible niche.

## References

1. zotero/zotero GitHub. https://github.com/zotero/zotero (14,179 stars; pushedAt 2026-05-13).
2. Aria (AI Research Assistant) plugin for Zotero. Various community sources.
3. yilewang/llm-for-zotero GitHub. https://github.com/yilewang/llm-for-zotero
4. Dobbs D. (cited via Wikipedia, *Mendeley*). https://en.wikipedia.org/wiki/Mendeley
5. Mendeley 2018 data-loss event, documented on Wikipedia and Zotero forums.
6. Clarivate. EndNote 2025 announcement. https://clarivate.com/academia-government/blog/introducing-endnote-2025-the-next-generation-of-reference-management/
7. Zettlr. https://www.zettlr.com/ ; user manual https://docs.zettlr.com/en/
8. retorquere/zotero-better-bibtex GitHub. https://github.com/retorquere/zotero-better-bibtex (6,689 stars; pushedAt 2026-05-16). Documentation: https://retorque.re/zotero-better-bibtex/
9. Paperpile. https://paperpile.com/
10. Mendeley (Elsevier). https://www.mendeley.com/ ; Wikipedia: https://en.wikipedia.org/wiki/Mendeley
