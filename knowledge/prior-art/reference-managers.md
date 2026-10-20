# Reference managers and citation philosophy

*Last updated: 2026-10-20*

## Synthesis

Reference managers are the closest thing scholarly writing has to a piece of widely-adopted infrastructure. Almost every researcher uses one; the ecosystem is mature; the file formats (BibTeX, RIS, CSL-JSON) are interoperable; and the philosophical differences between products are real — open-source-community (Zotero) vs. publisher-owned (Mendeley) vs. modern-commercial (Paperpile) vs. legacy-enterprise (EndNote).

What unifies them is a focus on **citation throughput**: getting references into a library, formatting them in a target style, generating bibliographies. What is conspicuously absent across all of them is **citation accuracy at the claim level** — that is, whether the cited work actually supports the claim it is attached to. This is the gap scite.ai partially addresses (covered in [[peer-review-platforms]]) and that scriptorium's `citation-audit` is designed to fill at the manuscript level.

The LLM-integration story across reference managers changed between late 2025 and October 2026. All three commercial products now ship AI features: Mendeley's Reading Assistant / Ask My Library / Compare Experiments (December 2025) [19], Paperpile's Ask AI hand-off to external assistants (public beta May 2026) [21], and EndNote Fusion's single-document Research Assistant (October 2026) [23]. These features read, summarise, and answer questions about PDFs; none of them checks whether a manuscript's in-text claims are supported by the works cited for them. Zotero itself still ships no built-in LLM features in its 2026 releases [13][14][15]; its LLM story remains community-driven (plugins such as llm-for-zotero, and Model Context Protocol servers such as zotero-mcp) [3][32]. Better BibTeX remains the indispensable bridge from Zotero to LaTeX/Markdown workflows, now sitting on top of a native Zotero citation-key field [16][17].

For scriptorium, the implication is clear: don't replace the reference manager, but assume one exists, expose its bibliography as the citation source of truth, and operate at the claim/citation linkage level that no reference manager touches.

## Landscape

### Zotero

**What it is.** Free, open-source reference manager, originally created at the Roy Rosenzweig Center for History and New Media (George Mason University) and now a project of the Corporation for Digital Scholarship, a nonprofit [11]. Cross-platform (Windows, Mac, Linux). Integrates with Word, LibreOffice, Google Docs, and OnlyOffice.

**Repo.** `zotero/zotero` has 15,675 stars, last pushed 2026-10-15 [1] — among the most active scholarly-software repos.

**Editorial philosophy.** Open-source, community-governed, data-portable. Local-first storage with optional sync. No tracking by default. The 2024 release of Zotero 7 (9 August 2024) modernized the UI and introduced a new plugin architecture with restartless plugins and built-in integration points [12]. In January 2026 Zotero moved to a rapid release cycle — feature releases roughly every 6–10 weeks — and has since shipped Zotero 8 (22 January 2026), Zotero 9 (10 April 2026), and Zotero 10 (17 August 2026) [13][14][15].

**LLM integration story.** Zotero is the platform of choice for LLM-curious researchers because of its plugin ecosystem; none of the 2026 major releases adds a built-in LLM feature [13][14][15].
- **Aria** (AI Research Assistant, `lifan0127/ai-research-assistant`) — community plugin embedding LLM chat in Zotero [2]. Its repository was last pushed on 2025-04-01 [31] — an early example of the sustainability risk flagged below.
- **llm-for-zotero** (`yilewang/llm-for-zotero`) — side-panel chat in the PDF reader; works with any OpenAI-compatible API including local models via Ollama [3]. Now described as "An open-source research agent system for your Zotero library" (3,361 stars, last pushed 2026-10-18) [3].
- **MCP servers** — Model Context Protocol servers expose a Zotero library to Claude, ChatGPT, and other agents; the most-starred, `54yyyu/zotero-mcp` (created March 2025; 5,482 stars, last pushed 2026-10-16), lets assistants search the library, read papers, and analyse citations [32].
- **Local-LLM workflows** — researchers connect Zotero to local Ollama/Open WebUI for private LLM analysis of personal libraries.

**Strengths.** Most flexible. Most private. Best for power users.

**Weaknesses.** Setup-heavy. Sync quotas; cloud storage is paid above 300 MB. Some users on the Zotero forums have complained that the rapid release cadence breaks plugins; the Zotero team's reply is that citation-key behaviour beyond the native field belongs to Better BibTeX [16].

### Mendeley (Elsevier)

**What it is.** Reference manager and academic social network, acquired by Elsevier in 2013.

**Editorial philosophy and controversy.** The Elsevier acquisition was contested. David Dobbs's *New Yorker* commentary [4] suggested Elsevier's motive could have been "to acquire its user data and/or to destroy or co-opt an open-science icon that threatens its business model." Subsequent events did not allay concern:
- 2018: An update caused users to lose PDFs and annotations [5].
- 2021: Mobile apps removed from iOS/Android stores.
- 2022: Mendeley Desktop downloads discontinued in favor of the new Mendeley Reference Manager.
- 2024–2025: Elsevier had planned to end sign-ins to legacy Mendeley Desktop; citing customer feedback, it reversed course in July 2025, keeping Desktop available with essential maintenance but no new feature development [10][18].

Privacy concerns about reading-habit and citation-pattern data being used by Elsevier persist and are unresolved.

**LLM integration story.** Publisher-driven and in-product. In December 2025 Mendeley launched three AI features — Reading Assistant (citation-supported answers about a PDF), Compare Experiments (side-by-side tables across up to ten PDFs), and Ask My Library (questions across a whole library); the launch posts link to Mendeley's pricing page, which suggests a paid tier, though they do not say so explicitly [19]. There is still no plugin ecosystem comparable to Zotero's.

**Strengths.** Free to start. Easy onboarding. Familiar to many researchers.

**Weaknesses.** Trust deficit. Active migration off Mendeley by open-science-aligned researchers is common; the standard advice in ResearchGate threads and university LibGuides is to migrate to Zotero or Paperpile.

### Paperpile

**What it is.** Commercial cloud-only reference manager built around Google Docs and the Google ecosystem. Plans are billed annually; with the 50% academic discount, the Regular plan is listed at $4.15/month (as of October 2026) [20]. iOS/Android apps; Chrome extension. Started as a Chrome-only product, expanded to a standalone web app and mobile.

**Editorial philosophy.** Modern-commercial. Tight Google integration is the value proposition: PDF scraping into Google Drive, inline citation insertion in Google Docs, fast search across large libraries. The product mark is reliability and polish, not openness.

**LLM integration story.** Paperpile chose hand-off over a built-in model. Its **Ask AI** integration — private beta December 2025, public beta 11 May 2026 — sends PDFs from the library, with curated research prompts, to the user's own ChatGPT, Claude, Gemini, Copilot, or NotebookLM account, and links quotes in the answer back to the source PDF [21]. The batch size follows each assistant's limit: up to ten PDFs at a time for ChatGPT, Claude, Gemini, and Copilot, while a NotebookLM notebook holds 50 PDFs on Google's free plan and up to 600 on its highest tier [21]. A public REST API and an MCP server are listed as "Started" on its roadmap [22]. Less openness than Zotero, more polish than Mendeley.

**Strengths.** Best Google Docs integration in the market. Fast. Affordable. Cloud-first.

**Weaknesses.** No local storage option. Less portable than Zotero. Vendor lock-in for Word-heavy workflows.

### EndNote (Clarivate)

**What it is.** The legacy enterprise reference manager. Owned by Clarivate, which also owns Web of Science.

**Editorial philosophy.** Comprehensive feature set and integration with Web of Science as a data source. EndNote 2025 made its Find Full-Text and Find Reference Updates tools more visible in the desktop panel, and announced proactive notifications of updated reference and citation information for a later release [6].

**LLM integration story.** EndNote 2025 was the first EndNote release with AI features: "Key Takeaway" (a summary drawn only from the individual paper, "without using any other document in the library or public LLMs") and "Find A Journal" (journal suggestions from the manuscript's title and abstract); a generative research assistant was announced for later [6]. On 6 October 2026 Clarivate's RefWorks became **EndNote Fusion**, a cloud product combining EndNote and RefWorks capabilities; EndNote Desktop and EndNote Online remain available and unchanged [23]. Fusion's Research Assistant summarises, answers questions about, and translates a PDF using retrieval-augmented generation, with "responses ... based only on the document being analyzed" [23]. Clarivate's stated roadmap includes writing support that will "flag potential issues in a reference list, such as incomplete metadata or cases where a more recent or authoritative version of record is available" [24] — metadata-level checking, not claim-level support. The integration is closed and publisher-owned, like Mendeley. No plugin ecosystem.

**Strengths.** Institutional-grade. Web of Science integration. Stable.

**Weaknesses.** Expensive. Slow innovation. Heavy. The user base is aging.

### Zettlr

**What it is.** Free, open-source Markdown editor explicitly designed for academic writing; its documentation describes it as community-managed, with no paid staff [7]. Cross-platform.

**Editorial philosophy.** Markdown-first, Zettelkasten-friendly, no telemetry, no cloud, no forced sync. Integrates with Zotero/JabRef/Juris-M for citations. Exports via Pandoc-powered export profiles [7].

**Strengths for scriptorium-style workflows.** Zettlr is one of the few editors that natively supports `[@doi:...]`-style citations against an external library, has Pandoc-grade export, and respects plain-text-first conventions. It is the spiritual cousin of the manubot/Quarto pattern at the editor level.

**Weaknesses.** Solo-author workflow primarily; weaker on multi-author co-editing than Google Docs / Overleaf.

### Better BibTeX (Zotero plugin)

**What it is.** A Zotero plugin by `retorquere/zotero-better-bibtex` (7,226 stars, last pushed 2026-10-19) [8] that gives Zotero LaTeX-grade BibTeX export with **stable, pinned citation keys**, automatic export-on-save, and rich customization of citation-key format.

**Why it matters.** Without Better BibTeX, Zotero historically generated citation keys that could change when metadata was updated, breaking citations in any LaTeX manuscript; Better BibTeX's "pin" mechanism guaranteed that a key, once assigned, stayed stable. That has now partly moved into Zotero itself. Zotero 7.0.31 (January 2026) introduced an official Citation Key field [16]. Better BibTeX 8.0, released for Zotero 8, migrated keys into that native field: "The concept of pinning keys is gone; keys are _always_ pinned now," auto-pin became "auto-fill," and keys now sync with the library [17]. Later releases restored a manual "Pin" command for some configurations, and Better BibTeX 9 requires Zotero 8+ [17]. Practically, a Zotero citation key is now first-class, synced library data rather than plugin state — a notable change that brings the broader Zotero ecosystem closer to LaTeX users' expectations.

**Editorial philosophy.** "Citations are infrastructure; stability matters more than perfection." This is the exact disposition scriptorium needs from a reference layer.

### Other tools worth a mention

- **JabRef** — Java-based BibTeX/biblatex reference manager. Popular in LaTeX-heavy domains.
- **Citavi** — Was the Windows-focused academic suite; its developer, Swiss Academic Software, was bought by QSR International in February 2021, and QSR co-founded Lumivero in 2022 [25]. Its market position has narrowed sharply: German universities including Göttingen (licence ends 30 November 2026), Bochum (30 September 2026), and TU Freiberg (30 November 2026) are ending campus licences — Göttingen and Freiberg recommend Zotero, Bochum Zotero or EndNote — with Bochum citing sharp price increases, one-sided product development, and declining support quality since the ownership change [26][27][28]. Paperpile added import of Citavi project files in September 2026 [21].
- **ReadCube Papers** — Closed-commercial. Papers was acquired from Springer Nature by ReadCube, a Digital Science portfolio company, in 2016 [29]; Digital Science also fully owns Writefull (since November 2023) [30].
- **Bibtex / biblatex** — The underlying file format. CSL-JSON is the increasingly-dominant JSON-native alternative.

## How this informs scriptorium

- **Don't try to be a reference manager.** Scriptorium's `citation-audit` skill assumes a bibliography exists. The skill's contract should be: *given a manuscript with citations and a resolvable bibliography (BibTeX, CSL-JSON, or DOIs-only), assess whether the claims are appropriately supported*. It is not the skill's job to format references, sync libraries, or deduplicate entries.
- **Better BibTeX is the precedent for "infrastructure that supports manuscripts as software."** A plugin to a reference manager that exists primarily to make citation keys stable for downstream tooling — that's exactly the supporting-infrastructure mindset scriptorium needs from upstream tools, and exactly what it should not try to replicate. Zotero's 2026 adoption of a native citation-key field shows that pattern being absorbed upstream.
- **Zotero is the natural reference partner.** Open API, plugin culture, local-first storage, identifier-driven CSL-JSON output. A scriptorium recipe that says "use Zotero + Better BibTeX + manubot/Quarto + scriptorium" is internally coherent. Zotero MCP servers also mean an agent running scriptorium skills may be able to read the author's library directly; that is an input channel, not licence for a skill to add entries to it.
- **The Mendeley story is a strategic warning.** Open-source vault → publisher acquisition → trust erosion → migration. Scriptorium's MIT license and minimal-vendor-state design protect against this failure mode, but only if the project itself remains community-maintained. The 2026 Citavi licence cancellations are a second instance of the same pattern after a change of ownership.
- **Identifier-resolution is non-negotiable for AI-assisted citation work.** Citation hallucination is a well-known LLM failure mode. The defense is: the LLM never invents a DOI; it operates on the bibliography that the reference manager exported. That bibliography is the author's source of truth, but it is not proof of correct metadata — reference managers still mis-capture some output types (for example dataset citations [34]).
- **Reference-manager AI is reading support, not claim auditing.** The 2025–2026 AI features in Mendeley, Paperpile, and EndNote answer questions about PDFs the user already holds; EndNote's announced reference-list checks are about metadata and versions of record [19][21][23][24]. None does claim-level citation–support auditing of a draft. The niche for `citation-audit` is unchanged.
- **Most reference managers have weak LLM integration with manuscript workflows.** This is the scriptorium opportunity. The skills should be designed such that a reference manager's exported bibliography (CSL-JSON in particular) can feed `citation-audit` directly, and the audit's output is structured enough that a human can take it back to the reference manager for fixes.

## Implementation priority for scriptorium

**Verdict:** No.

**Why this is useful context anyway:** the roadmap lists "No replacement for reference managers" as an explicit non-goal, and this note is its grounding. The landscape fixes `citation-audit`'s input contract (consume whatever bibliography Zotero, Mendeley, Paperpile, EndNote, or BibTeX produces) and confirms that the claim-level audit remains unaddressed by every product reviewed here. The 2026-10 sweep — commercial AI reading assistants, Zotero's native citation keys, EndNote Fusion, Citavi's decline — did not change the verdict. **Maybe later** (not committed): an optional read-only path that lets `citation-audit` fetch abstracts or full texts from the author's Zotero library via an MCP server; the condition would be a stable, widely used Zotero MCP interface plus a demonstrated gain in audit confidence over abstract-only assessment.

## Open questions / weak evidence

- **No recent evaluation of citation accuracy across reference managers.** The community knows from experience that auto-fetched metadata varies in quality (especially for older or non-DOI references). Older head-to-head studies exist — e.g. a 2017 comparison of the bibliographic accuracy of references generated by EndNote, Mendeley, RefWorks and Zotero for medical citation styles [33] — and a 2025 study of seven reference managers found that "a majority of frequently used reference managers do not adequately support data citation" [34]. There is no recent general benchmark for journal-article metadata.
- **The LLM-integration arms race is early.** Aria, llm-for-zotero, Zotero MCP servers, and similar community tools date from 2023–2026; Aria's repository has not been pushed since April 2025 [31], and llm-for-zotero's current repository dates from January 2026 [3]. Their long-term sustainability is uncertain. Scriptorium should not depend on any specific plugin.
- **CSL-JSON vs. BibTeX is not yet a settled choice.** LaTeX users prefer BibTeX/biblatex; modern web/Markdown workflows prefer CSL-JSON. Scriptorium should consume either; producing CSL-JSON internally is the conservative bet.
- **The "do these citations actually support the claims?" problem has no commercial product.** scite.ai (see [[peer-review-platforms]]) classifies citation *intent* in already-published literature. Its Reference Check does take a draft manuscript, but it evaluates each cited *source* against scite's data — retractions, contradicting citations, other flags — rather than checking whether the source supports the sentence citing it [35]. This is scriptorium's most defensible niche.

## References

1. zotero/zotero GitHub. https://github.com/zotero/zotero (15,675 stars; pushedAt 2026-10-15; checked 2026-10-20).
2. Aria (AI Research Assistant) plugin for Zotero. https://github.com/lifan0127/ai-research-assistant
3. yilewang/llm-for-zotero GitHub. https://github.com/yilewang/llm-for-zotero (3,361 stars; created 2026-01-29; pushedAt 2026-10-18; checked 2026-10-20).
4. Dobbs D. "When the Rebel Alliance Sells Out." *The New Yorker*, 12 April 2013 (cited via Wikipedia, *Mendeley*). https://en.wikipedia.org/wiki/Mendeley
5. Mendeley 2018 data-loss event, documented on Wikipedia and Zotero forums.
6. Clarivate. EndNote 2025 announcement. https://clarivate.com/academia-government/blog/introducing-endnote-2025-the-next-generation-of-reference-management/
7. Zettlr. https://www.zettlr.com/ ; user manual https://docs.zettlr.com/en/
8. retorquere/zotero-better-bibtex GitHub. https://github.com/retorquere/zotero-better-bibtex (7,226 stars; pushedAt 2026-10-19; checked 2026-10-20). Documentation: https://retorque.re/zotero-better-bibtex/
9. Paperpile. https://paperpile.com/
10. Mendeley (Elsevier). https://www.mendeley.com/ ; Wikipedia: https://en.wikipedia.org/wiki/Mendeley
11. Zotero. About. https://www.zotero.org/about/
12. Stillman D. Zotero 7. Zotero blog, 9 August 2024. https://www.zotero.org/blog/zotero-7/
13. Stillman D. Zotero 8. Zotero blog, 22 January 2026. https://www.zotero.org/blog/zotero-8/ ; A faster release cycle for Zotero, 22 January 2026. https://www.zotero.org/blog/a-faster-release-cycle-for-zotero/
14. Stillman D. Zotero 9. Zotero blog, 10 April 2026. https://www.zotero.org/blog/zotero-9/
15. Stillman D. Zotero 10. Zotero blog, 17 August 2026. https://www.zotero.org/blog/zotero-10/
16. Zotero Forums. "Zotero 8/9, BBT, and citation keys" (Zotero team reply, 13 April 2026: "The only change we made — in 7.0.31 — was to introduce an official Citation Key field"). https://forums.zotero.org/discussion/130917/zotero-8-9-bbt-and-citation-keys ; Zotero 7.0 changelog: https://www.zotero.org/support/7.0_changelog
17. Better BibTeX for Zotero. Changelog (v8.0.0, v8.0.38, v9.0.0, v9.0.8). https://retorque.re/zotero-better-bibtex/changelog/index.html
18. Mendeley. "Mendeley Desktop is Here to Stay." Mendeley blog, 9 July 2025. https://blog.mendeley.com/2025/07/09/mendeley-is-not-going-anywhere/
19. Mendeley. "The Future in Mendeley: AI features are here!" Mendeley blog, 8 December 2025. https://blog.mendeley.com/2025/12/08/the-future-in-mendeley-ai-features-are-here/ ; "Boost Your Research Efficiency with new AI Features in Mendeley," 12 January 2026. https://blog.mendeley.com/2026/01/12/boost-your-research-efficiency-with-mendeleys-ai-tools/
20. Paperpile. Pricing (checked 2026-10-20). https://paperpile.com/pricing/
21. Paperpile. "New integration: bring your research library to any AI assistant." Paperpile blog, May 2026. https://paperpile.com/blog/pdf-ai-assistant/ ; changelog (Ask AI private beta 16 December 2025; public beta 11 May 2026; Citavi import 29 September 2026). https://paperpile.com/changelog/
22. Paperpile. Roadmap (checked 2026-10-20). https://paperpile.com/roadmap/
23. Kemp A. "EndNote Fusion is here: A new chapter for reference management." Clarivate blog, 14 October 2026. https://clarivate.com/academia-government/blog/endnote-fusion-is-here-a-new-chapter-for-reference-management/ (mirror: https://librarytechnology.org/pr/33032/endnote-fusion-is-here-a-new-chapter-for-reference-management/)
24. Clarivate. "EndNote Fusion: A unified reference management platform from Clarivate." Clarivate blog, 2026. https://clarivate.com/academia-government/blog/introducing-endnote-fusion/ (text read via a search provider's extraction; direct fetch blocked, HTTP 403)
25. Wikipedia. Citavi. https://en.wikipedia.org/wiki/Citavi
26. Universität Göttingen. "Termination of the Citavi campus licence in one year." 19 November 2025. https://news.uni-goettingen.de/blog/2025/11/19/beendigung-der-citavi-campuslizenz-in-einem-jahr-termination-of-the-citavi-campus-licence-in-one-year/
27. Ruhr-Universität Bochum IT.Services. "Citavi: Campuslizenz endet zum 30. September 2026." 18 March 2026. https://www.it-services.ruhr-uni-bochum.de/news/news00637.html.de
28. TU Bergakademie Freiberg. "Citavi site license expires on 30 November 2026." https://tu-freiberg.de/en/news/citavi-site-license-expires-30-november-2026
29. Digital Science. "ReadCube Acquires Papers from Springer Nature." 16 March 2016. https://www.digital-science.com/press-releases/readcube-acquires-papers-springer-nature-2/
30. Digital Science. "AI for academia: Digital Science acquires Writefull." 21 November 2023. https://www.digital-science.com/press-releases/digital-science-acquires-writefull/
31. lifan0127/ai-research-assistant GitHub (1,729 stars; pushedAt 2025-04-01; checked 2026-10-20). https://github.com/lifan0127/ai-research-assistant
32. 54yyyu/zotero-mcp GitHub (5,482 stars; created 2025-03-22; pushedAt 2026-10-16; checked 2026-10-20). https://github.com/54yyyu/zotero-mcp
33. Kratochvíl J. Comparison of the accuracy of bibliographical references generated for medical citation styles by EndNote, Mendeley, RefWorks and Zotero. *The Journal of Academic Librarianship*. 2017;43(1):57–66. doi:10.1016/j.acalib.2016.09.001.
34. Vrouwenvelder K, Raia NH, Thomer AK. Obstacles to dataset citation using bibliographic management software. *Data Science Journal*. 2025. doi:10.5334/dsj-2025-017.
35. scite. Reference Check guide. https://docs.scite.ai/guides/reference-check
