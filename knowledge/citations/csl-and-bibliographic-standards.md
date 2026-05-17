# CSL and bibliographic standards

*Last updated: 2026-05-17*

## Synthesis

Scriptorium does not generate bibliographies; it operates on
bibliographies the author has already curated. This design choice
rests on hallucination evidence (see
[[hallucination-in-llm-citations]]) and on the practical observation
that the scholarly identifier ecosystem already does this work well.
The relevant standards split into three layers: a **style layer** (how
citations are rendered) — Citation Style Language (CSL); a **storage
layer** (how references are stored) — BibTeX/BibLaTeX, CSL-JSON,
RIS; and an **identifier layer** (how works, authors, organizations,
and funders are pinpointed) — DOI / CrossRef / DataCite, ORCID, ROR,
the Open Funder Registry, and CURIE prefixes coordinated by the
Bioregistry.

Each layer is independently mature. CSL governs nearly every modern
reference manager (Zotero, Mendeley, Paperpile, and most academic
word-processor integrations). Persistent identifier coverage is now
high enough that "the bibliography exists in machine-readable form
with stable identifiers" is a reasonable assumption for any
contemporary manuscript. Manubot's reliance on Bioregistry CURIE
prefixes — currently spanning 1,677 identifier types — illustrates the
practical reach of this infrastructure beyond pure DOI/ORCID lookups.

Scriptorium's job is to read whatever bibliography the manuscript
ships with, treat it as authoritative, and never silently introduce
references that are not in it. That posture only works because the
existing standards are good enough to make "the author's bibliography"
a stable artifact to anchor against.

## Evidence

**Citation Style Language (CSL).** Originally conceived by Bruce
D'Arcus in 2006 for OpenOffice citation rendering, formalized as an
XML-based specification. Early CSL adoption was driven by Simon
Kornblith's Zotero integration; Mendeley followed and (with Columbia
University Libraries) obtained an Alfred P. Sloan Foundation grant to
build the CSL style editor. Mendeley and Elsevier have donated to the
CSL project since 2014.[^1]

The current specification (CSL 1.0.2) defines:

- A style language (XML) describing how to render citations and
  bibliographies for a given journal or discipline.
- A data interchange format (**CSL-JSON**) for individual references.
- A locale mechanism for language- and region-specific conventions.

The CSL Style Repository hosts thousands of journal- and
discipline-specific styles, maintained by community contributions.
Zotero, Mendeley, Paperpile, Pandoc (via citeproc), and several
journal submission systems consume CSL natively. This makes CSL the
de facto interoperability standard for "what should this citation
look like in this venue."

**BibTeX / BibLaTeX.** The older LaTeX-native ecosystem remains
dominant in physics, mathematics, computer science, and statistics.
BibTeX's `@article{...}` syntax is well-understood and stable.
BibLaTeX is the modern successor with richer entry types and Unicode
support. Most reference managers can export to BibTeX, and most
manuscript workflows in LaTeX-heavy fields use BibTeX as the
canonical bibliography format. Scriptorium should accept BibTeX/
BibLaTeX as a first-class input.

**DOIs and CrossRef.** The Digital Object Identifier system, operated
for scholarly content primarily by CrossRef and DataCite, is the most
widely deployed persistent identifier for academic works. CrossRef
holds metadata for over 140 million scholarly works (current
estimate; `[TODO verify]` exact figure) and exposes structured
metadata via a public REST API. CrossRef's metadata records
increasingly carry references *to* other works, ORCID author
identifiers, and ROR institutional identifiers — turning the citation
graph itself into queryable infrastructure.[^2]

**DataCite.** Mirrors CrossRef for datasets, software, and other
research outputs. Particularly important in data-citation contexts;
DataCite's metadata schema is closely aligned with CrossRef's to
support interoperability.

**ORCID.** Persistent identifier for individual researchers. ORCID
records can be tied to publications, peer reviews, grants, and
affiliations. The ORCID/CrossRef auto-update system propagates
publication records to ORCID profiles automatically when an article
is registered with CrossRef. This makes ORCID a reasonable
disambiguator for "who is the author" in contexts where lastname-only
attribution is ambiguous.[^3]

**ROR.** The Research Organization Registry, launched in 2019, is
jointly run by California Digital Library, CrossRef, DataCite, and
(formerly) ORCID. ROR provides CC0-licensed open identifiers for
research organizations, replacing the historically fragmented
landscape of institutional identifiers. ROR is now the de facto
standard for affiliation identification in CrossRef metadata.[^4]

**Open Funder Registry (FundRef).** CrossRef's funder identifier
service. The registry contains over 15,000 funder entries; CrossRef
holds funding metadata on more than 1.7 million works. This matters
for `MANUSCRIPT_STATE.yaml` declaring grant numbers and funder
identifiers consistently.

**Bioregistry and CURIE prefixes.** The Bioregistry is a meta-registry
that catalogs identifier prefixes across biology, biomedicine, and
adjacent fields. CURIEs (Compact URIs) take the form `prefix:identifier`
(e.g., `doi:10.1136/bmj.b2680`, `clinicaltrials:NCT04280705`,
`pmid:19622839`). Bioregistry currently catalogs **1,677 prefixes**
(as referenced by manubot). Manubot — the open scholarly-publishing
tool — initially used Identifiers.org for ~700 prefixes, then migrated
to Bioregistry for both broader coverage and more rigorous validation
(open contribution model; better regex patterns; resolution of
namespace inconsistencies).[^5][^6]

This matters for scriptorium because it means a manuscript's
"citations" need not all be DOI-based. A reference to
`clinicaltrials:NCT04280705` or `arXiv:2401.01234` is a fully
machine-resolvable citation under existing standards, and scriptorium
should treat such references as first-class.

## How this informs scriptorium

**Bibliography is input, not output.** Scriptorium reads BibTeX,
CSL-JSON, or in-manuscript citation keys (Pandoc-style
`[@doi:10.1136/bmj.b2680]` or `\cite{...}`) and treats the resulting
reference set as the canonical "what citations exist in this
manuscript." Any skill operating on the manuscript can ask: *is this
in-text citation present in the bibliography?* That is a syntactic
check, not a generative act.

**Citation audit operates on the citation set, not on free-text
references.** Because CSL/BibTeX entries carry stable identifiers,
`citation-audit` does not have to parse rendered prose to figure out
*which* paper a citation refers to. It can ask the structured
question: "in-text citation `[Smith 2019]` resolves to bibliography
entry `smith2019`, which has DOI `10.1234/abcd`. Does the manuscript's
claim accompanying this citation match what we know about that DOI?"

**No skill writes new bibliography entries.** Even when
`reviewer-simulation` recommends "consider adding a recent
meta-analysis," the recommendation does not propose specific bibtex
keys, DOIs, or author strings. Adding bibliography entries is the
author's act, using their reference manager and the
identifier-resolution services above.

**MANUSCRIPT_STATE bibliography pointer.** The state schema includes
a `bibliography` field pointing to the canonical bibliography file
(e.g., `bibliography: refs.bib`). Skills resolve in-text citations
against this file. If the field is absent, citation-aware skills can
still operate on in-text citation keys but should emit a warning that
the bibliography link is missing.

**Manubot pattern as design influence.** Manubot's three-stage
pipeline (Pandoc parses citation keys → manubot-cite filter retrieves
metadata via CrossRef / Bioregistry → citeproc renders styled output)
is a clean separation of concerns that scriptorium should mirror in
spirit: identifier resolution, metadata retrieval, and rendering are
three different jobs, and conflating them is where errors enter.

## Open questions / weak evidence

- Coverage of non-biomedical fields by Bioregistry is uneven;
  scriptorium should not assume every domain has a comparable
  identifier catalog.
- Some venues still demand plain-text references with no identifiers
  (older journals, certain humanities outlets). Scriptorium degrades
  gracefully to "citation key only" in those cases but loses the
  ability to do identifier-level verification.
- The interaction between CSL styles and journal-specific
  pre-submission validation is messier than the standards suggest;
  journals' production pipelines often diverge from their published
  style guides.

## References

[^1]: Citation Style Language. About. https://citationstyles.org/about/

[^2]: CrossRef. Public REST API and infrastructure documentation.
    https://crossref.org/

[^3]: ORCID. Public-facing documentation.
    https://orcid.org/ . CrossRef–ORCID auto-update:
    https://www.crossref.org/community/orcid/

[^4]: Research Organization Registry (ROR). About page.
    https://ror.org/about/

[^5]: Hoyt CT, Balk M, Callahan TJ, et al. Unifying the identification
    of biomedical entities with the Bioregistry. *Scientific Data*.
    2022;9:714. doi:10.1038/s41597-022-01807-3.

[^6]: Manubot. Usage documentation, citation prefix support.
    https://github.com/manubot/rootstock/blob/main/USAGE.md
