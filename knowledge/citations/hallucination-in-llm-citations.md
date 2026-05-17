# Hallucination in LLM-generated citations

*Last updated: 2026-05-17*

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
real *and* correctly cited. Retrieval-augmented generation (RAG) and
function-call grounding substantially reduce fabrication, but do not
eliminate it — and they introduce a subtler failure mode (citation of
real papers that do not support the claim).

The implication for scriptorium is structural, not merely cautionary:
*no skill should generate citations from the model's parametric
knowledge.* Critique skills may flag citations that look suspect;
transformation skills may rearrange citations the author has already
placed; only an explicit retrieval-grounded skill, with verifiable
bibliography intake, may *add* a citation, and even then only by
proposing additions to the author for confirmation.

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
education, and other domains. The fabrication rate is model-dependent,
prompt-dependent, and domain-dependent, but does not drop to zero in
any unconstrained generative setup yet evaluated.

**The "fictional DOI" pattern.** A recurring sub-phenomenon: the model
emits DOI strings that follow CrossRef structural conventions
(prefix/journal-code/year-format) but resolve to nothing or to an
unrelated paper. Walters & Wilder report this explicitly; it is
consistent with token-level generation that has learned the *shape*
of a DOI without storing the *index* that maps DOIs to papers. Naive
copy-paste of LLM-generated DOIs into bibliography managers is the
most common downstream failure mode this produces.

**Retrieval-augmented generation (RAG).** RAG pipelines retrieve
candidate documents before generation, then condition on retrieved
content. Reported fabrication-rate reductions in recent literature:
40%+ reduction in domain-specific RAG (MEGA-RAG); SELF-RAG with
explicit citation/critique loops reports hallucination rates in the
~6% range; Hyper-RAG reports ~12% accuracy improvement.[^3] These are
substantial gains, but recent work also documents a residual failure
mode: **citation hallucination in RAG** — the model cites a real
paper from the retrieved context but the cited content does not
support the claim. This is the same overreach problem as in human
authors (see [[citation-overreach-research]]), now mechanized.

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

**Reviewer-simulation does not need to fabricate citations.** The
reviewer-simulation skill produces critiques of the manuscript, not
new bibliographic claims. Personas should be instructed to identify
*types* of missing support ("a recent meta-analysis would strengthen
this claim") rather than *specific* citations, to avoid laundering
fabricated references through the reviewer voice.

## Open questions / weak evidence

- Fabrication base rates are model-version-dependent and drift as
  models update. The Walters & Wilder and Bhattacharyya numbers are
  early-2023 snapshots; current models likely fabricate less in
  unconstrained generation, but the rate has not dropped to zero in
  any evaluation we have located.
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

[^3]: Retrieval-augmented generation reductions are summarized across
    multiple recent papers, including SELF-RAG (Asai et al. 2024)
    and Hyper-RAG. Numbers cited are reported values; methodology and
    benchmarks vary, so cross-paper comparisons are indicative
    rather than authoritative. `[TODO verify]` specific DOIs.
