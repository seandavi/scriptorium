# Literature-search strategies: from boolean queries to citation chasing

*Last updated: 2026-05-20*

## Synthesis

A researcher with a gap to fill turns to literature search by some
combination of three strategies: **boolean database search**
(formulating MeSH / Emtree / keyword queries against PubMed,
Embase, Web of Science, Scopus, Google Scholar), **citation
chasing** (forward citation search from a seed paper using Web
of Science / Scopus / Google Scholar / Semantic Scholar, or
backward citation walking through reference lists), and
**snowballing** (combining the two iteratively until saturation).
The systematic-review methodology literature has documented these
strategies extensively and agrees on the broad shape, even when
specific tool recommendations shift [1, 2, 3]. For a manuscript-
internal skill that *suggests directions* for closing a research
gap, the right framing is not to invent the citations the author
should add — that's the hallucination failure mode — but to
hand the author a search strategy they can actually run.

Two patterns matter for gap-direction suggestion. **First**:
boolean query construction has well-documented best practices
(MeSH-term anchoring for PubMed; PICO / PICOS structuring; field
operators; date ranges; the EQUATOR-recommended Cochrane
Handbook chapters on search-strategy development [3]). A skill
that names *search terms and field operators* gives the author
something they can paste into PubMed; a skill that just says
"search for related work" is unhelpful. **Second**: citation
chasing is the underused complement to database search,
particularly for emerging topics where MeSH terms haven't caught
up. Semantic Scholar's API-accessible citation graph and
connectedpapers.com's visual citation-network browsers are the
contemporary tools for this; the methodology dates to
Greenhalgh & Peacock's snowballing-vs-database-search comparison
[4] and Wohlin's formalisation in software-engineering
systematic reviews [5].

The contemporary LLM-era complication is that **LLM-suggested
literature is often hallucinated**: the model produces a
plausible-sounding citation that doesn't exist, or that exists
but doesn't say what the model claims. The mitigation in
agentic-system design is documented in the
[[ai-agentic-scientific-writing]] note (GeneAgent's
generate→verify→modify pattern) and is the same pattern that
underlies scriptorium's no-invent-citations posture: the skill
suggests *what to search for*, not *which papers to cite*. The
author runs the search, evaluates results, and decides what to
cite. The skill never bridges that gap.

For scriptorium specifically, the practical takeaway is that
gap-finder's "Suggested directions" output should be
operationalised as a **search strategy** the author can run,
not as a citation list the author can copy. The strategies the
note synthesises here are the menu of techniques the skill draws
from.

## Evidence and frameworks

### Boolean database search

The Cochrane Handbook for Systematic Reviews [3] is the canonical
reference for boolean query construction. The core methodology:

- **PICO / PICOS / PCC** structuring. Decompose the question
  into Population, Intervention, Comparison, Outcome (and
  optionally Study type for PICOS, or Population / Concept /
  Context for scoping-review PCC). Each axis becomes a search
  block; blocks combine with AND; synonyms within blocks combine
  with OR.
- **MeSH-term anchoring for PubMed.** MeSH (Medical Subject
  Headings) is the controlled vocabulary that lets a query
  capture all the synonyms used in indexing. A MeSH search for
  "Diabetes Mellitus, Type 2"[Mesh] catches T2DM, NIDDM, etc.,
  without manual synonym enumeration. Free-text searches miss
  this and are correspondingly less reliable for systematic
  retrieval.
- **Emtree for Embase**, **subject headings for CINAHL**, and
  similar controlled vocabularies in other databases. Each
  database has its own; cross-database searches need parallel
  query construction.
- **Field operators.** Search-string syntax for limiting to
  title, abstract, journal, author, date range, publication
  type. Reduces noise; PubMed's `[ti]`, `[au]`, `[journal]`
  operators are the most-used.

For a gap-finder skill's direction-suggestion output, the right
shape is a **structured search-string draft** keyed to the
specific database the author is most likely to use given the
manuscript's field. For biomedical work that's usually PubMed;
for clinical psychology it might be APA PsycInfo; for engineering
it might be IEEE Xplore.

### Citation chasing — forward and backward

Forward citation chasing finds papers that cite a known seed
paper; backward citation chasing finds papers that the seed paper
cites. Both are essential for topics where database indexing is
weak (emerging methods, interdisciplinary work, very recent
literature where MeSH hasn't caught up).

**Greenhalgh & Peacock (2005) [4]** documented citation chasing
as a complement to database search in their landmark BMJ study —
in their case, the chasing strategies found half of the relevant
papers that database search missed. **Wohlin (2014) [5]**
formalised snowballing for software-engineering systematic
reviews and argued snowballing alone can produce comparable
coverage to database search if iterated to saturation.

Contemporary tools that operationalise citation chasing:

- **Web of Science Citation Index** — the original; subscription
  required.
- **Scopus** — Elsevier's competitor; subscription required.
- **Google Scholar's "Cited by" link** — free, broad, less
  curated.
- **Semantic Scholar** — free, has an API, includes citation
  intent classification.
- **connectedpapers.com** — visual citation-network browser;
  useful for exploring a topic without knowing the seed
  citations.
- **Inciteful.xyz** and **Research Rabbit** — newer citation-
  network tools with explicit "snowball" modes.

For gap-finder, the practical recommendation pattern is: if the
manuscript already cites work on topic X, suggest **forward
citation chasing from <specific cited paper>** as a way to find
recent work the manuscript may not have engaged with. If the
manuscript needs literature it doesn't cite, suggest **starting
from <specific recent landmark paper> and snowballing backward**.

### Snowballing as iterative method

Snowballing combines database search and citation chasing
iteratively: start with a small seed set found via database
search, forward-and-backward chase from each seed, screen new
papers for relevance, repeat with the new relevant set as next
seed, continue until saturation (each iteration adds few new
relevant papers). The methodology is documented as the
**bidirectional snowball** in systematic-review literature [5].

For a gap-finder skill, snowballing is the right framing when
the gap is bounded but the author doesn't yet have the seeds.
The skill can name "snowball from <recent review paper> using
forward citation chasing" as a concrete strategy.

### MeSH-vs-keyword and the precision-recall trade-off

The MeSH-vs-keyword question is methodologically important for
gap-finder's suggestions. MeSH terms are more precise (they
catch the relevant indexed papers without false positives) but
less complete (they catch only papers that have been indexed,
which excludes recent un-indexed papers and some preprints).
Keyword searches are the opposite: more recall, more noise,
better for emerging literature.

The practical recommendation for a gap-finder skill: when
suggesting a search, name both the MeSH-term-anchored version
*and* the keyword-anchored version when both make sense. The
author can run either or both depending on whether they want
precision or recall.

### LLM-assisted search tools

A separate class of tools is the LLM-driven literature-search
assistants: **Elicit**, **Consensus**, **Scite**, **Undermind**,
**Scholarcy**, **Research Rabbit**, **Inciteful**, and others.
These vary substantially in quality and trustworthiness:

- **Scite** is the most-cited for *finding contradicting and
  supporting evidence* and has the largest classified-citation
  dataset (≈1.2B citation classifications as of 2024 [TODO
  verify current scale]). Its citation-intent classifier is
  the most rigorous in the space.
- **Elicit** and **Consensus** offer LLM-generated summaries of
  search results. Quality varies; both have been documented to
  produce confidently wrong summaries in cases where the
  underlying papers actually conflict.
- **Undermind** [TODO verify current product status] aims to be
  a deeper-search tool with iterative LLM-driven refinement.
- The general failure mode across LLM-driven tools is the same
  as scriptorium guards against: confidently wrong summaries,
  inverted causal claims, and over-confident "no evidence for X"
  statements based on shallow search.

For gap-finder's direction-suggestion output, naming these
tools as options is appropriate when the gap is bounded; the
caveat is that **the tool's output still needs human
verification**. The skill should not delegate the gap-direction
suggestion to a recommendation that the author run an LLM-
driven search tool blindly.

### Forward-looking: what the search-strategy literature still
doesn't tell us

Several questions in the literature-search-methodology space are
unresolved:

- **How does LLM-assisted search affect the coverage of
  systematic reviews?** Early evidence suggests mixed
  results — better discovery on some topics, worse on others;
  the long-term answer is unclear.
- **What is the right way to evaluate LLM-driven literature
  tools?** The metrics that work for traditional database
  search (recall, precision, F1) don't capture the failure
  modes specific to generative tools (hallucinated citations,
  confidently wrong summaries).
- **How do tools handle preprints and other grey literature?**
  Coverage varies dramatically; the gap-finder skill should
  caveat this when suggesting tools.

For scriptorium, the operational implication is that the
literature-search-strategy advice gap-finder gives should
**caveat tool-specific limitations** and **never claim that
running a particular search will close a particular gap**. The
author runs the search; the search produces results; the author
evaluates and decides.

## How this informs scriptorium

For `gap-finder` specifically:

1. **Output is a search strategy, not a citation list.** Per
   [[declared-work-scope]] and the no-invention rule shared
   with `citation-audit`, the skill produces *search terms,
   field operators, citation-chase directions, and tool
   recommendations* — never *cite this paper*. The author runs
   the search.

2. **Structured search-string drafts.** When the gap is
   well-bounded (a missing population, a methodological gap,
   a counterargument gap), the skill produces a draft search
   string with the right structure for the relevant database.
   PubMed for biomedical; APA PsycInfo for psychology; IEEE
   Xplore for engineering; etc. The author copies and pastes.

3. **Citation-chasing direction when the seeds exist.** When
   the manuscript already cites work on the gap's topic, the
   skill suggests forward citation chasing from a specific
   cited paper as a concrete next step. This is more
   actionable than "search the literature".

4. **Snowballing when the seeds are missing.** When the gap is
   bounded but the manuscript doesn't yet have the seed
   citations, the skill names a likely seed (a landmark review
   or method paper) and suggests bidirectional snowballing
   from it.

5. **Name tools, caveat limitations.** When LLM-driven search
   tools (Elicit, Consensus, Scite, etc.) are a reasonable
   option, the skill names them with explicit "still requires
   human verification" framing. Never recommends them as a
   substitute for verifying the literature the author would
   end up citing.

6. **MeSH-anchored AND keyword-anchored options.** When
   suggesting a PubMed search, the skill provides both
   versions: the MeSH-anchored search for precision and the
   keyword-anchored search for recall in emerging literature.

7. **Honest about uncertainty.** When the skill isn't sure the
   suggested strategy will close the gap (because the gap is
   poorly bounded or the field is sparse), it says so. "This
   search may not return much; the field is sparse" is more
   useful than confident strategies that go nowhere.

## Implementation priority for scriptorium

**Verdict:** Direct grounding for the `gap-finder` skill (v0.3
candidate, currently `needs-grounding` until this note and
[[research-gap-detection]] both land). This note covers the
*direction-suggestion* side of gap-finder; the sister note
covers the *detection* side. Both are required.

**Why useful context anyway:**

- Search-strategy methodology is useful framing for any future
  scriptorium skill that needs to point an author at "go look
  up X". The PICO / PCC framing, the database-controlled-
  vocabulary advice, and the citation-chasing strategies are
  reusable across skills.

- The LLM-assisted-search-tool landscape is moving fast and the
  knowledge note will need updating periodically. Worth being
  explicit in the note that the tool list is a snapshot, not a
  permanent recommendation.

- A future `literature-finder` skill (not in current roadmap,
  speculative) could do automated structured search against
  PubMed / Semantic Scholar APIs and surface results to the
  author. This note's framework would be the design anchor.
  Speculative; not v0.3 work.

**Condition that would flip the implementation priority:** if a
maintained, API-accessible bibliographic search service emerges
with strong precision and citation-intent classification (an
extension of Scite or Semantic Scholar with author-side use), a
gap-finder variant could call out to it directly rather than
producing search-string drafts for the author to run manually.
That's a v0.5+ question.

## Cross-references

- [[research-gap-detection]] — the detection side of
  gap-finder; this note covers the direction-suggestion side.
  Both required.
- [[citation-claim-alignment]] — the parallel "audit existing
  citations" skill. Gap-finder's no-invention rule mirrors
  citation-audit's; this note operationalises what the skill
  suggests instead of inventing.
- [[hallucination-in-llm-citations]] — the underlying failure
  mode this note's "never invent citations" rule defends
  against. Gap-finder's specific variant is hallucinated
  *future* literature, which is harder to detect because the
  fake citation hasn't entered the manuscript yet.
- [[reference-managers]] — adjacent territory. Reference
  managers (Zotero, Mendeley, Paperpile, EndNote) are the tools
  authors use to manage what the gap-finder skill points them
  toward. Gap-finder's search-strategy output should be
  pasteable into the author's reference manager workflow.
- [[ai-agentic-scientific-writing]] — the GeneAgent
  generate-verify-modify pattern; the underlying defence
  pattern for grounded suggestion.
- [[declared-work-scope]] — the convention. Gap-finder's
  suggestions are bounded by declared work; the search
  strategies are anchored to gaps that exist in declared prose.

## References

[1] Booth, A., Sutton, A., & Papaioannou, D. (2016).
*Systematic Approaches to a Successful Literature Review* (2nd
ed.). SAGE Publications. ISBN: 9781473912458. (Comprehensive
reference for literature-search methodology; the
PICOS-structured approach to query construction.)

[2] Aromataris, E., & Riitano, D. (2014). Constructing a search
strategy and searching for evidence. *American Journal of
Nursing*, 114(5), 49-56. DOI: 10.1097/01.NAJ.0000446779.99522.f6.
PMID: 24759479. (Accessible introduction to PICO-structured
boolean-query construction.)

[3] Higgins, J. P. T., Thomas, J., Chandler, J., Cumpston, M.,
Li, T., Page, M. J., & Welch, V. A. (eds.). (2022). *Cochrane
Handbook for Systematic Reviews of Interventions* (version
6.3). Cochrane. <https://training.cochrane.org/handbook>.
Chapter 4 ("Searching for studies"). (The canonical
search-strategy reference for systematic reviews.)

[4] Greenhalgh, T., & Peacock, R. (2005). Effectiveness and
efficiency of search methods in systematic reviews of complex
evidence: audit of primary sources. *BMJ*, 331(7524), 1064-1065.
DOI: 10.1136/bmj.38636.593461.68. PMID: 16230312. (The landmark
demonstration that citation chasing finds papers database search
misses.)

[5] Wohlin, C. (2014). Guidelines for snowballing in systematic
literature studies and a replication in software engineering.
*Proceedings of the 18th International Conference on Evaluation
and Assessment in Software Engineering (EASE)*, Article 38.
DOI: 10.1145/2601248.2601268. (Formalisation of snowballing as a
standalone systematic-review methodology.)

[6] Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco,
O. H. (2017). Optimal database combinations for literature
searches in systematic reviews: a prospective exploratory
study. *Systematic Reviews*, 6, 245.
DOI: 10.1186/s13643-017-0644-y. PMID: 29208034. (Cross-database
coverage analysis; relevant for tool recommendations across
different fields.)

[7] Nicholson, J. M., Mordaunt, M., Lopez, P., Uppala, A.,
Rosati, D., Rodrigues, N. P., Grabitz, P., & Rife, S. C. (2021).
Scite: A smart citation index that displays the context of
citations and classifies their intent using deep learning.
*Quantitative Science Studies*, 2(3), 882-898.
DOI: 10.1162/qss_a_00146. (Scite's citation-intent
classification methodology.)

[8] Else, H. (2023). Abstracts written by ChatGPT fool
scientists. *Nature*, 613(7944), 423.
DOI: 10.1038/d41586-023-00056-7. PMID: 36635510. (Documents
the LLM-summary failure mode that gap-finder's
"name tools with caveats" recommendation guards against.)

[9] van Dis, E. A. M., Bollen, J., Zuidema, W., van Rooij, R.,
& Bockting, C. L. (2023). ChatGPT: five priorities for
research. *Nature*, 614(7947), 224-226.
DOI: 10.1038/d41586-023-00288-7. PMID: 36737653. (The
much-cited Nature commentary on LLM use in research, including
the limitations of LLM-driven literature search.)
