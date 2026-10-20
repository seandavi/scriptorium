# Hallucination in LLM-generated citations

*Last updated: 2026-10-20*

## Synthesis

LLMs trained to predict the next token will, when prompted to produce
citations, generate strings that *look like* citations. Whether those
strings correspond to real papers, real DOIs, and real claims is a
separate question — and the empirical answer, across the most-studied
models, is "often not." This is not a bug to be patched. It is a
predictable property of how generative models compose plausible
surface forms from training data, and it persists even when the
underlying world-knowledge has improved.

The base rates are now well-quantified. For unconstrained
free-generation tasks, GPT-3.5 fabricated roughly half its
citations; GPT-4 dropped that to roughly a fifth; specialized
biomedical prompts with GPT-3.5 produced ~47% fabricated and ~46%
authentic-but-inaccurate references, leaving **7%** that were both
real *and* correctly cited. Newer models have not closed the gap: in
June 2025, GPT-4o still fabricated 19.9% of the citations in
generated mental-health literature reviews, with fabrication rising
to 28–29% on less-studied topics.[^5] Retrieval-augmented generation
(RAG) and function-call grounding reduce fabrication, but do not
eliminate it — and they introduce a subtler failure mode (citation of
real papers that do not support the claim).

Since 2025 the question has moved from "how often do models
fabricate when asked?" to "how much fabrication has reached the
published record?" The answer is: measurably, and rising. Audits of
millions of papers find non-existent references rising sharply after
2023,[^6][^7] and about 1% of papers accepted at NeurIPS 2025
contained at least one fabricated citation that had passed 3–5
expert reviewers.[^8] Many of these fabrications carry real-looking
identifiers that resolve to a *different* paper,[^8] so a check that
only asks "does this DOI resolve?" will pass them.

The implication for scriptorium is structural, not merely cautionary:
*no skill should generate citations from the model's parametric
knowledge.* Critique skills may flag citations that look suspect;
transformation skills may rearrange citations the author has already
placed; only an explicit retrieval-grounded skill, with verifiable
bibliography intake, may *add* a citation, and even then only by
proposing additions to the author for confirmation. And because
authors' own manuscripts now arrive carrying LLM-generated references
from their drafting tools, `citation-audit` must verify that each
identifier resolves to the work the reference string describes, not
merely that it resolves.

## Evidence

**Walters & Wilder (2023), *Scientific Reports* 13:14045** — the
clearest cross-model quantification. The authors prompted GPT-3.5 and
GPT-4 to write short literature reviews on 42 multidisciplinary
topics, producing 84 papers and 636 citations. They then searched
databases to determine which citations referred to real works.

- **GPT-3.5:** 55% of citations were fabricated.
- **GPT-4:** 18% of citations were fabricated.
- Among real (non-fabricated) citations: **43%** of GPT-3.5 citations
  and **24%** of GPT-4 citations contained substantive errors (wrong
  authors, wrong title, wrong journal, wrong year, etc.).

The improvement from GPT-3.5 to GPT-4 is substantial but does not
approach acceptable accuracy. Combining fabrication and error rates,
fewer than two in three GPT-4 citations were both real and correctly
described.[^1]

**Bhattacharyya et al. (2023), *Cureus*** — focused on medical
content. Prompted GPT-3.5 (April 2023) to generate 30 short biomedical
papers with at least three references each, producing 115 citations.
Results: **47%** fabricated, **46%** authentic but inaccurate, **7%**
authentic and accurate. Among the real references, **87%** contained
at least one of seven error types (incorrect PMID, author name,
article title, date, journal title, volume, page numbers).[^2]

These two papers are the most-cited base-rate studies, but the
general finding has been replicated across legal contexts (the
widely reported court sanctions for fabricated case law), economics,
education, and other domains. In medicine, Chelli et al. (2024) asked
GPT-3.5, GPT-4, and Bard to reproduce the reference lists of 11
systematic reviews and found hallucination rates of 39.6%, 28.6%, and
91.4% respectively.[^4] Linardon et al. (2025) prompted GPT-4o for six
literature reviews (176 citations): 19.9% were fabricated, 45.4% of
the real citations contained errors, and fabrication was 6% for major
depressive disorder but 28–29% for less-studied disorders, reaching
46% for specialized prompts on binge eating disorder.[^5] The
fabrication rate is model-dependent, prompt-dependent, and
domain-dependent — and, per Linardon et al., worst exactly where
authors are least able to spot it (niche, specialized topics) — but
does not drop to zero in any unconstrained generative setup yet
evaluated.

**The "fictional DOI" pattern.** A recurring sub-phenomenon: the
model emits identifiers (DOIs, arXiv IDs, PMIDs) that look valid but
resolve to nothing or to an unrelated paper. The evidence for it is
now direct. Bhattacharyya et al. found an incorrect PMID in 93% of
generated papers.[^2] Walters & Wilder did not examine DOIs, but found
that when ChatGPT attached links to real works, about one-third of
those links were inaccurate.[^1] In Linardon et al.'s GPT-4o study,
the most frequent error in real citations was an "incorrect or
invalid" DOI.[^5] In published NeurIPS 2025 papers, "Identifier
Hijacking" — a valid identifier pointing to a different work — was
the primary failure mode in 4% of fabricated citations and a
secondary characteristic in 29%, typically layered on top of a fully
fabricated reference "to create a veneer of plausibility and false
verifiability."[^8] *Researcher inference:* this is consistent with
token-level generation that has learned the *shape* of an identifier
without storing the index that maps identifiers to papers. Naive
copy-paste of LLM-generated identifiers into bibliography managers is
the most common downstream failure mode this produces, and a
resolve-only check cannot catch it.

**Prevalence in the published literature (2025–2026).** Four
independent lines of evidence now measure fabricated references in
papers that were actually posted or published:

- **Biomedical literature.** Topaz et al. (*The Lancet*, 2026; a
  peer-reviewed research letter) built an automated
  reference-verification system and ran it over PubMed Central's
  open-access subset from 1 January 2023 to 18 February 2026, about
  2.5 million papers. Among 97.1 million verified references they
  identified 4,046 fabricated references in 2,810 papers; the rate
  grew more than 12-fold since 2023, with the sharpest increase from
  mid-2024.[^6] *Nature*'s report on the study describes this as
  "nearly 3,000 biomedical-science papers that contain fake
  references" and says "rates of fabricated citations have climbed
  steeply since 2023."[^6] Topaz told Retraction Watch that 91% of
  the affected papers had only one or two fabricated references.[^6]
- **Cross-repository.** Zhao et al. (arXiv preprint, May 2026)
  audited 111 million references across 2.5 million papers in arXiv,
  bioRxiv, SSRN, and PubMed Central and estimate, conservatively,
  146,932 hallucinated citations in 2025 alone. Hallucinated
  references were more common in fields with rapid AI uptake, in
  papers with linguistic signs of AI-assisted writing, and among
  small and early-career author teams; "preprint moderation and
  journal publication processes capture only a fraction of these
  errors."[^7]
- **Peer-reviewed conference papers.** At NeurIPS 2025, 100
  fabricated citations appeared in 53 accepted papers (about 1% of
  accepted papers). Every one showed compound failure modes, and 92%
  of affected papers had only one or two fabricated references —
  the signature of light AI use, not wholesale generation.[^8] In ACL,
  NAACL, and EMNLP papers from 2024–2025, nearly 300 papers carried
  at least one hallucinated citation, half of them at EMNLP 2025.[^9]
- **Venue response.** ICLR 2026 ran an automated reference checker on
  every submission, had flagged references checked by at least three
  humans, and desk-rejected every paper with a confirmed hallucinated
  reference. The organisers note the checker "had a significant false
  positive rate" — for example on non-English titles that authors had
  translated.[^10]

Two implications follow. First, light-touch AI use is the dominant
pattern, so fabricated references will usually be a small minority
inside an otherwise real bibliography. Second, writing tools now
generate bibliographies directly: OpenAI's Prism, launched January
2026, was demonstrated finding literature and "automating the process
of writing the bibliography," with OpenAI's own caveat that this does
not absolve "the scientist of the responsibility to verify that their
references are correct."[^11] See [[ai-writing-tools-survey]] and
[[ai-peer-review-research]].

**Retrieval-augmented generation (RAG).** RAG pipelines retrieve
candidate documents before generation, then condition on retrieved
content. Methods such as Self-RAG, which trains the model to decide
when to retrieve and to critique whether its output is supported by
the retrieved passages, report gains in factuality and citation
accuracy for long-form generation over ChatGPT and conventional RAG
baselines.[^3] These are substantial gains, but RAG also has a
residual failure mode: **citation hallucination in RAG** — the model
cites a real paper from the retrieved context but the cited content
does not support the claim. This is the same overreach problem as in
human authors (see [[citation-overreach-research]]), now mechanized.
The NeurIPS taxonomy's "Semantic Hallucination" category, a real or
plausible reference attached to content it does not support, is the
published-literature version of this failure.[^8]

**Why models fabricate.** Generative LLMs learn to produce
high-probability token sequences. Bibliographic strings have
strong surface regularities (author lastname, year, journal,
volume:pages) that the model can reproduce as patterns regardless of
whether any specific paper instance exists. Unless the model is
constrained to emit only tokens from a verified bibliography, it
will compose plausible-looking citations whenever asked. This is a
property of the architecture, not a deficiency of training data, and
it is why bigger models reduce but do not eliminate the problem.

## How this informs scriptorium

The hallucination evidence is the load-bearing rationale for several
scriptorium design choices.

**Generation skills must not invent citations.** Per
[[DESIGN]] §"Conservative-edit posture": "Critique skills don't
invent citations; transformation skills don't add them." This is not
a stylistic preference; it is the only defensible posture given the
base rates above.

**`citation-audit` reads citations, does not propose them.** Even
when the skill identifies a claim that lacks a supporting citation
(or rests on overreach), its output is a *flag for the author*, not
a *proposed reference string*. The author resolves the gap from their
own reference manager or a retrieval system they trust.

**`citation-audit` must check identifier-to-metadata agreement, not
just resolution.** Fabricated references survive review through
compound failure modes that defeat several checks at once, and about
a third of the NeurIPS 2025 fabrications carried a real identifier
pointing to a different work (Identifier Hijacking: 4% as the primary
mode, 29% as a secondary one).[^8]
A DOI, PMID, or arXiv ID that resolves is not evidence the reference
is real: the audit should compare the resolved record's title, first
author, year, and venue against the reference string and flag any
mismatch. Fabrications are usually one or two items in an otherwise
genuine bibliography — 92% of affected NeurIPS 2025 papers[^8] and
91% of affected papers in the Lancet audit[^6] — so the audit must
check every entry rather than sample.

**`argumentative-flow` and other transformation skills must respect
`preserve_citations: true`.** The schema constraint
`preserve_citations: true` in `MANUSCRIPT_STATE.yaml` is enforced as
a contract: every citation present in the input must appear in the
output, in the same form, attached to a claim it could plausibly have
been attached to in the input. The contract prevents the LLM from
"helpfully" substituting a fabricated citation for an inconvenient
one during a rewrite.

**Bibliography intake, not bibliography generation.** Scriptorium
assumes the manuscript arrives with an existing bibliography (BibTeX,
CSL-JSON, or similar; see [[csl-and-bibliographic-standards]]). The
system reads and operates on that bibliography. It does not synthesize
one. If a future generation skill — e.g., `related-work-suggester` —
proposes additions, it must do so via an explicit retrieval-grounded
pathway (e.g., a CrossRef or Semantic Scholar query) and surface the
proposed additions to the author for confirmation before any
manuscript edit.

**`gap-finder` names gaps, not papers, unless it has retrieved them.**
The Linardon et al. result — fabrication highest on niche,
specialized topics[^5] — is exactly the territory a gap-finding skill
works in. Any specific work `gap-finder` names must come from a
retrieval call whose result has been checked against Crossref or
PubMed metadata in the same session; otherwise it should describe
the *kind* of literature to search for.

**Reviewer-simulation does not need to fabricate citations.** The
reviewer-simulation skill produces critiques of the manuscript, not
new bibliographic claims. Personas should be instructed to identify
*types* of missing support ("a recent meta-analysis would strengthen
this claim") rather than *specific* citations, to avoid laundering
fabricated references through the reviewer voice.

## Implementation priority for scriptorium

**Verdict:** Yes — this note grounds `citation-audit` and `gap-finder`
(both existing). (Section added 2026-10-20; the note previously lacked
one.)

**If Yes:**
- **`citation-audit`** — material change from the 2025–2026
  evidence: verify that each identifier's resolved metadata (title,
  first author, year, venue) matches the reference string, and report
  "identifier resolves to a different work" as its own finding class,
  distinct from "identifier does not resolve" and "no identifier."
  Audit every entry: in both the NeurIPS 2025 and Lancet audits, 9 in
  10 affected papers had only one or two fabricated references.[^6][^8]
  Keep the existing posture of flagging, never proposing replacement
  references.
- **`gap-finder`** — minor change: no named works without same-session
  retrieval and metadata verification; otherwise describe the search
  to run.
- **Required data:** network access to Crossref, PubMed E-utilities,
  and arXiv metadata at audit time. The ICLR 2026 experience[^10]
  warns that automated checkers have a real false-positive rate
  (translated titles, books, grey literature), so findings should be
  phrased as "could not verify" with the evidence shown, not as
  "fabricated."

## Open questions / weak evidence

- Fabrication base rates are model-version-dependent and drift as
  models update. The Walters & Wilder and Bhattacharyya numbers are
  early-2023 snapshots. The June 2025 GPT-4o figure (19.9%)[^5] shows
  newer models still fabricate in unconstrained generation; no
  evaluation we have located shows a rate of zero.
- Prevalence estimates in the published literature depend on the
  verifier. The Lancet audit[^6] and the Zhao et al. preprint[^7] use
  different corpora and pipelines; their absolute counts are not
  directly comparable, and both will miss some real-but-unindexed
  works (false positives) and some hijacked identifiers (false
  negatives).
- The interaction between RAG quality and citation overreach is
  underexplored. RAG that retrieves accurately can still produce
  citations that overreach the retrieved content — closer to human
  spin than to fabrication.
- Whether scriptorium should ship an *optional* retrieval-grounded
  citation-suggester (Phase 2+) is an open design question. The
  current default is the safer "audit-only" posture.

## References

[^1]: Walters WH, Wilder EI. Fabrication and errors in the
    bibliographic citations generated by ChatGPT. *Scientific
    Reports*. 2023;13:14045. doi:10.1038/s41598-023-41032-5.
    PMID: 37679503.

[^2]: Bhattacharyya M, Miller VM, Bhattacharyya D, Miller LE. High
    rates of fabricated and inaccurate references in ChatGPT-generated
    medical content. *Cureus*. 2023;15(5):e39238.
    doi:10.7759/cureus.39238. PMID: 37337480.

[^3]: Asai A, et al. Self-RAG: Learning to Retrieve, Generate, and
    Critique through Self-Reflection. arXiv:2310.11511 (2023);
    ICLR 2024 (https://openreview.net/forum?id=hSyW5go0v8). The
    previous version of this note also quoted figures for MEGA-RAG
    (40%+ reduction), SELF-RAG (~6% hallucination), and Hyper-RAG
    (~12% improvement). None of those figures could be traced to a
    checked source in the October 2026 refresh (the Self-RAG abstract
    reports no such number), so they have been removed. Skills should
    not cite [^3] as a specific empirical number.

[^4]: Chelli M, Descamps J, Lavoué V, et al. Hallucination Rates and
    Reference Accuracy of ChatGPT and Bard for Systematic Reviews:
    Comparative Analysis. *Journal of Medical Internet Research*.
    2024;26:e53164. doi:10.2196/53164. PMID: 38776130.

[^5]: Linardon J, Jarman HK, McClure Z, Anderson C, Liu C, Messer M.
    Influence of Topic Familiarity and Prompt Specificity on Citation
    Fabrication in Mental Health Research Using Large Language Models:
    Experimental Study. *JMIR Mental Health*. 2025;12:e80371.
    doi:10.2196/80371. PMID: 41223407.

[^6]: Topaz M, Roguin N, Gupta P, Zhang Z, Peltonen L-M. Fabricated
    citations: an audit across 2·5 million biomedical papers. *The
    Lancet*. 2026;407(10541):1779–1781.
    doi:10.1016/S0140-6736(26)00603-3. PMID: 42107362. A research
    letter (Correspondence section), not a full Article. *The Lancet*
    later published a Department of Error notice linked to it
    (2026;408:218; doi:10.1016/S0140-6736(26)01339-5); its content
    was not checked, and the letter's full text returned HTTP 403 to
    the refresh's fetcher. Counts (4,046 fabricated references in
    2,810 papers among 97.1 million verified references; 1 January
    2023 – 18 February 2026; more than 12-fold growth) are from:
    Columbia University School of Nursing. "Nearly 3,000 peer-reviewed
    medical papers have fake citations, a Columbia Nursing AI-assisted
    audit finds." Press release, 2026-05-07.
    https://www.eurekalert.org/news-releases/1127364 . The 91% figure
    is Topaz quoted in: Retraction Watch. "One in 277 PubMed-indexed
    papers in 2026 shows fabricated references, says analysis."
    2026-05-07.
    https://retractionwatch.com/2026/05/07/one-in-277-pubmed-indexed-papers-in-2026-shows-fabricated-references-says-analysis/ .
    "Nearly 3,000" and "climbed steeply since 2023" are quoted from:
    Naddaf M. Surge in fake citations uncovered by audit of 2.5
    million biomedical-science papers. *Nature*. 2026;653:658–659.
    doi:10.1038/d41586-026-00748-w.

[^7]: Zhao Z, Wang Y, Stuart T, De Vaan M, Ginsparg P, Yin Y. LLM
    hallucinations in the wild: Large-scale evidence from
    non-existent citations. arXiv:2605.07723 (2026). (Preprint.)

[^8]: Ansari MS, et al. Compound Deception in Elite Peer Review: A
    Failure Mode Taxonomy of 100 Fabricated Citations at NeurIPS 2025.
    arXiv:2602.05930 (2026). (Preprint.)

[^9]: Sakai Y, Kamigaito H, Watanabe T. HalluCitation Matters:
    Revealing the Impact of Hallucinated References with 300
    Hallucinated Papers in ACL Conferences. arXiv:2601.18724 (2026).
    (Preprint.)

[^10]: ICLR 2026 Program Chairs. A Retrospective on the ICLR 2026
    Review Process. ICLR blog, 2026-03-31.
    https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/

[^11]: Bonifacic I. OpenAI releases Prism, a Claude Code-like app for
    scientific research. *Engadget*, 2026-01-27.
    https://www.engadget.com/ai/openai-releases-prism-a-claude-code-like-app-for-scientific-research-180000454.html
