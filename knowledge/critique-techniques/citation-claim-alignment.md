# Citation–claim alignment: verifying that a cited source supports its claim

*Last updated: 2026-05-17*

## Synthesis

The quotation-accuracy literature (see [[citation-accuracy-evidence]]
in `knowledge/citations/`) establishes that roughly one in five to one
in ten citations in biomedical literature contains a quotation error
serious enough to mislead a careful reader. Citation–claim alignment
is the methodological core of how that finding is generated and how
journal editors, sleuths, and emerging automated tools (notably
scite.ai) operationalise the question "does this citation actually
support what the sentence is claiming?" It is the load-bearing problem
for any automated citation audit, because bibliographic correctness
(does the reference exist? are the author names right?) is largely a
solved problem with reference managers and CrossRef, whereas
*semantic* correctness — does the cited paper say what the citing
sentence says it says? — remains overwhelmingly manual.

The technique is conceptually simple: extract the claim, retrieve the
cited reference, compare. In practice each step has known failure
modes: claims are ambiguously scoped, references are paywalled or
abstract-only, and "support" is gradient rather than binary. The
techniques below — Greenberg's citation-network methodology, scite's
classifier, journal-editorial-team protocols, the primary-vs-review
heuristic — give a layered approach. The strongest result is
Greenberg's *BMJ* 2009 paper [^1], which demonstrated by exhaustive
network analysis that an entire literature can establish "unfounded
authority" through citation bias, amplification, and invention even
when each individual citation might pass a casual spot-check.

For scriptorium, the practical takeaway is that `citation-audit`
should produce a *gradient* assessment — supports / partially supports
/ does not support / cannot determine without full text — rather than
a binary verdict. See [[hallucination-in-llm-citations]] for the
parallel risk that an LLM critique invents references; see
[[citation-overreach-research]] for the related problem of
*overreach*, where every individual citation may be technically
correct but the chain amplifies a hedged hypothesis into stated fact.

## Techniques and tools

### Greenberg 2009 — citation-distortion network analysis

Greenberg's *BMJ* 2009 paper "How citation distortions create
unfounded authority: analysis of a citation network" [^1] is the
methodological touchstone for understanding how systematically a
literature can drift away from its underlying evidence. Greenberg
built a complete citation network for the claim that β-amyloid
deposits in inclusion-body myositis muscle play a causal role in the
disease. From 242 papers containing statements about the claim and
675 supporting citations, he constructed a directed graph with
**220,609 citation paths** through the PubMed-indexed literature.

Greenberg's three named distortion patterns:

1. **Citation bias** — papers that refute or weaken the belief are
   disproportionately *un-cited* relative to their evidence weight.
   In the β-amyloid network, six papers presenting contradicting data
   attracted only ~6% of citations to the canonical set.
2. **Amplification** — papers that contain no original data about the
   claim nevertheless cite the canonical papers and are in turn cited
   as support, expanding the *apparent* authority of the claim
   without adding evidence.
3. **Invention** — citation conversion of a hypothesis into a stated
   fact. A paper presenting an unsupported claim becomes, three
   citations later, the source for the claim being treated as
   established.

Greenberg's method requires the full text of every citing paper, full
classification of each citation's stance toward the claim, and graph
analysis. This is post-publication, retrospective work, not a
within-manuscript audit. But the *types* of failure it names are
exactly the failure modes a single-manuscript audit should look for:
is this citation propagating an *invention*? Is the claim a citation-
chain amplification of something less certain?

### Earlier methodological work on citation accuracy

- **de Lacey, Record & Wade (1985)** — the foundational *BMJ*
  citation-accuracy study (see [[citation-accuracy-evidence]]).
- **Eichhorn & Yankauer (1987)** — *Am J Public Health* survey of
  three public-health journals, 150 references audited [^2]. 31%
  of references had citation errors (10% major); 30% of references
  differed from authors' use of them, with half of those major (i.e.
  the cited paper was *not* in fact related to the author's
  contention). PMID: 3079520.
- **Evans, Nadjari & Burchell (1990)**, *JAMA* — "Quotational and
  reference accuracy in surgical journals: a continuing peer review
  problem" [^3]. Documented surgical-journal quotation errors at
  rates that the authors interpreted as evidence many references were
  never read by the citing authors.

These studies together establish the methodological template still in
use: select a sample of in-text citations, retrieve each cited
reference, classify whether the cited source supports the in-text
statement, tally. *[TODO verify: Smith & Banks 1991 BMJ specifically
named in the brief — the citation-accuracy paper from that period in
BMJ is typically attributed to de Lacey 1985; I cannot confirm a 1991
Smith & Banks BMJ paper from accessible sources.]*

### Computational approaches

- **scite.ai** [^4] — operationalises citation–claim alignment at
  scale. Its Smart Citations classifier uses deep learning to label
  each citing statement as **supporting**, **contrasting**, or
  **mentioning**. Reported aggregate distribution in their corpus:
  ~92.6% mentioning, ~6.5% supporting, ~0.8% contrasting (Nicholson et
  al. 2021, *Quantitative Science Studies*). The numbers themselves
  are informative: the vast majority of citations in the literature
  are neither support nor contradiction; they are *mention*. This
  raises a calibration question for any audit — what counts as a
  "miscitation" when the modal citation is mention-not-support?
- **Semantic Scholar** — provides a "highly cited" indicator and
  citation-influence scores, but does not classify stance. Useful
  for triage; not a substitute for stance classification.
- **CitePrint** and related research prototypes — academic work on
  citation-intent classification has produced multiple labelled
  corpora (e.g. ACL-ARC, SciCite) used to train classifiers. Quality
  varies; agreement with human classification typically ~70–80%
  rather than near-ceiling.

### Manual claim–citation alignment protocols

Major journals' editorial teams (BMJ, JAMA, *Annals of Internal
Medicine*) apply a manual protocol of the same form: select claims in
the abstract and discussion that depend on cited support, retrieve
each reference, judge whether the cited source materially supports
the claim. The systematic-review literature on quotation-error
prevalence (Wager & Middleton 2007 / 2008 Cochrane methodology review,
see [[citation-accuracy-evidence]]) demonstrates this protocol's
reproducibility across reviewers; the median quotation error rate is
~20%.

The journal-editor protocol can be summarised in four steps:

1. **Extract** the in-text claim that the citation purportedly
   supports.
2. **Retrieve** the cited reference (full text where possible;
   abstract minimum).
3. **Compare** — does the cited source state, on its own evidence,
   what the citing sentence asserts?
4. **Classify** — fully supports / partially supports / does not
   support / not retrievable.

This is the protocol scriptorium's `citation-audit` should mirror, with
the explicit caveat that LLM access to full text is often blocked
behind paywalls. Where only abstract is accessible, the skill should
say so explicitly — "support assessed from abstract only" — rather
than implying full-text verification.

### The primary-vs-review heuristic

A common pattern flagged by Greenberg's invention category: a hedged
hypothesis is published in a primary paper; a review article cites the
primary paper but loses the hedge; a third paper cites *the review*
as if it established the claim. The mechanism is documented in
[[citation-overreach-research]] (see the spin and amplification
literatures).

The practical heuristic — when is review-only citation a smell, when is
it fine? — depends on the claim type:

- **Background context, definitional, or canonical-fact claim**:
  citing a review is appropriate and efficient.
- **Effect-size or mechanism claim that does inferential work in the
  current paper**: citing only the review is a smell; the primary
  source should be reachable. Discussion sections relying on
  review-only citations for load-bearing inferences are a frequent
  pattern in low-quality narrative reviews.

### "Drive-by citation" and citation copying

The phenomenon of citing without reading is documented indirectly
through quotation-error propagation: Simkin & Roychowdhury (2003)
*Complex Systems* used a methodology that detected the propagation of
*identical typographical errors* in citations across hundreds of
papers, inferring that authors copied citations from one another
without consulting the source. The implication is that detected
miscitations are not random — they cluster on citations that have been
propagated through copying.

## How this informs scriptorium

- **`citation-audit`** — the core scriptorium critique skill targeted
  by this knowledge. Implementation should:
  - Extract claim + paired citation as a (claim, ref) tuple.
  - Retrieve abstract via DOI / PubMed (CrossRef + NCBI E-utilities;
    no fabricated references — see [[hallucination-in-llm-citations]]).
  - Compare claim against retrieved abstract using a stance-
    classification prompt (supports / partially / does-not / cannot
    determine).
  - Emit structured output per (claim, ref) with a confidence flag
    and an explicit "abstract-only" marker when full text was
    inaccessible.
- **Cross-checks**: where scite.ai is available, the skill could
  cross-reference its supporting/contrasting classification as a
  second opinion (with their numbers as prior).
- **Greenberg-style network audits** are out of scope for a
  per-manuscript skill. They are appropriate for a future
  `citation-network-audit` operating on a corpus.

LLM limits — be honest:

- Without full text, the skill is verifying support against the
  *abstract*, which is a much weaker test than the full paper. The
  output should say so.
- LLM stance classification is not perfectly reliable; the
  scite.ai corpus shows ~70–85% agreement with human annotators
  depending on the dataset.
- The conservative-edit posture (DESIGN.md) means `citation-audit`
  *never* modifies citations — it only flags. Replacement
  recommendations should be human-authored.

## Limits and caveats

- Stance classification ("supports / mentions / contrasts") is a
  three-way collapse of a continuous question; reviewers often
  disagree on the boundary between "partially supports" and "does
  not support."
- A citation can be correct *as a citation* (the cited paper does
  contain the claim) but the cited paper itself can be wrong; this
  is a deeper problem (the literature itself is wrong) that
  citation-claim alignment cannot detect.
- Abstract-only assessment misses cases where the abstract supports
  the claim but the methods or limitations sections contradict it.
- "Drive-by citation" is largely undetectable from within a single
  manuscript; it requires cross-corpus comparison.

## References

[^1]: Greenberg SA. How citation distortions create unfounded
    authority: analysis of a citation network. *BMJ*. 2009;
    339:b2680. DOI: 10.1136/bmj.b2680. PMC: PMC2714656.

[^2]: Eichorn P, Yankauer A. Do authors check their references? A
    survey of accuracy of references in three public health journals.
    *American Journal of Public Health*. 1987; 77(8):1011–1012.
    PMID: 3079520.

[^3]: Evans JT, Nadjari HI, Burchell SA. Quotational and reference
    accuracy in surgical journals: a continuing peer review problem.
    *JAMA*. 1990; 263(10):1353–1354. DOI: 10.1001/jama.1990.03440100053007.

[^4]: Nicholson JM, Mordaunt M, Lopez P, Uppala A, Rosati D, Rodrigues
    NP, Grabitz P, Rife SC. scite: A smart citation index that
    displays the context of citations and classifies their intent
    using deep learning. *Quantitative Science Studies*. 2021;
    2(3):882–898. DOI: 10.1162/qss_a_00146.

**Research gap:** A "Smith & Banks 1991 *BMJ*" citation-accuracy
paper appears in some bibliographies and was sketched here, but it
could not be located in CrossRef, PubMed, or Google Scholar searches
during the May 2026 knowledge-layer sweep. The closest foundational
work in this vein is de Lacey, Record & Wade (1985) *BMJ* and
Eichorn & Yankauer (1987) *AJPH* (entry [^2] above) — both are
methodologically primary for this skill's grounding and the Smith &
Banks reference is not load-bearing. The claim has been left here
as a gap rather than fabricated. *What would verify it: locating the
exact Smith & Banks 1991 paper (or confirming the citation was a
secondary-source misattribution).*
