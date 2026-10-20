# Citation–claim alignment: verifying that a cited source supports its claim

*Last updated: 2026-10-20*

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
built a complete citation network for the belief that β-amyloid is
produced by and injures skeletal muscle in inclusion-body myositis.
From 242 papers containing statements about the claim and
675 citations addressing it, he constructed a directed graph with
**220,609 citation paths** through the PubMed-indexed literature
(220,553 of them supporting the claim).

Greenberg's three named distortion patterns:

1. **Citation bias** — papers that refute or weaken the belief are
   disproportionately *un-cited* relative to their evidence weight.
   In the β-amyloid network, the six primary-data papers that
   weakened or refuted the claim received only 6% of the 214
   citations to primary data (P=0.01).
2. **Amplification** — papers that contain no original data about the
   claim nevertheless cite the canonical papers and are in turn cited
   as support, expanding the *apparent* authority of the claim
   without adding evidence.
3. **Invention** — citation conversion of a hypothesis into a stated
   fact ("citation transmutation"). A paper presenting an unsupported
   claim becomes, three citations later, the source for the claim
   being treated as established.

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
- **Eichorn & Yankauer (1987)** — *Am J Public Health* survey of
  three public-health journals, 150 references audited [^2]. 31%
  of references had citation errors, one in ten of them major
  (reference not locatable); 30% of references differed from authors'
  use of them, with half of those major (i.e.
  the cited paper was *not* in fact related to the author's
  contention). PMID: 3079520.
- **Evans, Nadjari & Burchell (1990)**, *JAMA* — "Quotational and
  reference accuracy in surgical journals: a continuing peer review
  problem" [^3]. Fifty references from one issue of each of three
  surgical journals yielded 13 major and 41 minor citation errors and
  37 major quotation errors; the authors wrote that the data support
  the hypothesis that "authors do not check their references or may
  not even read them."

These studies together establish the methodological template still in
use: select a sample of in-text citations, retrieve each cited
reference, classify whether the cited source supports the in-text
statement, tally. (A "Smith & Banks 1991 *BMJ*" citation-accuracy
paper named in the original brief could not be located; see the
research-gap note at the end of this document.)

### Computational approaches

- **scite.ai** [^4] — operationalises citation–claim alignment at
  scale. Its Smart Citations classifier uses deep learning to label
  each citing statement as **supporting**, **contrasting**, or
  **mentioning**. From manual annotations across publication domains,
  the scite team estimates the average distribution of citation
  statements as ~92.6% mentioning, ~6.5% supporting, ~0.8%
  contrasting (Nicholson et al. 2021, *Quantitative Science Studies*).
  The numbers themselves
  are informative: the vast majority of citations in the literature
  are neither support nor contradiction; they are *mention*. This
  raises a calibration question for any audit — what counts as a
  "miscitation" when the modal citation is mention-not-support?
- **Semantic Scholar** — provides a "highly cited" indicator and
  citation-influence scores, but does not classify stance. Useful
  for triage; not a substitute for stance classification.
- **Citation-intent research corpora** — academic work on
  citation-intent classification has produced multiple labelled
  corpora (e.g. ACL-ARC, SciCite) used to train classifiers. These
  label *intent* (background / method / result comparison), not
  support versus contrast. Quality varies: the SciCite paper's best
  model reached a macro-F1 of 84.0 on SciCite and 67.9 on ACL-ARC
  (Cohan et al. 2019 [^8]) — well short of ceiling, and lowest on
  the rare classes.

### Manual claim–citation alignment protocols

Reference-accuracy surveys, and editors and reviewers who spot-check
cited material — a measure the quotation-error meta-analysis
explicitly recommends [^5] — apply a manual protocol of the same
form: select claims in the abstract and discussion that depend on
cited support, retrieve each reference, judge whether the cited
source materially supports the claim. The Cochrane methodology review
of reference-accuracy surveys (Wager & Middleton 2008 [^6], see
[[citation-accuracy-evidence]]) pooled 66 such surveys and reports a
median quotation-error rate per journal of ~20%. The surveys used
somewhat different criteria, so this shows how widely the protocol
has been applied, not that it is reproducible across reviewers.

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
*Complex Systems* [^7] modelled the distribution of *identical
misprints* in citations across many papers, inferring that authors
copied citations from one another without consulting the source;
their estimate was that only about 20% of citers read the original.
The implication is that detected
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
  consult its supporting/contrasting labels as weak, low-recall
  corroboration only — not as a second opinion that sets the prior.
  scite's contrasting class has a recall of 0.451 [^4], so a missing
  "contrasting" label is not evidence of support, and a scite label
  should never override the skill's own reading of the cited source
  (see the LLM limits below).
- **Greenberg-style network audits** are out of scope for a
  per-manuscript skill. They are appropriate for a future
  `citation-network-audit` operating on a corpus.

LLM limits — be honest:

- Without full text, the skill is verifying support against the
  *abstract*, which is a much weaker test than the full paper. The
  output should say so.
- Automated stance classification is not perfectly reliable. scite's
  deployed SciBERT classifier, evaluated on a 9,708-statement
  holdout set, reported F-scores of 0.973 for mentioning, 0.648 for
  supporting, and 0.590 for contrasting (precision 0.852 for
  contrasting, recall 0.451) [^4] — the rare, decision-relevant
  classes are exactly where it is weakest. An LLM prompt has no
  published benchmark of its own here and should not be assumed to
  do better.
- The conservative-edit posture (DESIGN.md) means `citation-audit`
  *never* modifies citations — it only flags. Replacement
  recommendations should be human-authored.

## Implementation priority for scriptorium

**Verdict:** Yes (v0.1).

**Skill:** `citation-audit` (critique phase), scoped to the
per-manuscript four-step protocol above with a gradient
classification and an explicit abstract-only / metadata-only marker.
Required data: the manuscript, its bibliography (identifier-resolved),
and cited abstracts or full texts where available.

**Maybe later:** a corpus-level `citation-network-audit` in
Greenberg's style. Condition that would flip it to Yes: a user corpus
of many citing papers on one claim, with full texts available, and a
demonstrated need beyond the per-manuscript audit.

The 2026-10 refresh did not change either verdict. Note that the
four-step protocol is the reference-accuracy / editorial protocol, not
Greenberg's network method; Greenberg supplies the distortion
categories the audit flags.

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
    PMID: 19622839.

[^2]: Eichorn P, Yankauer A. Do authors check their references? A
    survey of accuracy of references in three public health journals.
    *American Journal of Public Health*. 1987; 77(8):1011–1012.
    DOI: 10.2105/ajph.77.8.1011. PMID: 3079520.

[^3]: Evans JT, Nadjari HI, Burchell SA. Quotational and reference
    accuracy in surgical journals: a continuing peer review problem.
    *JAMA*. 1990; 263(10):1353–1354. DOI: 10.1001/jama.1990.03440100059009.
    PMID: 2304213.

[^4]: Nicholson JM, Mordaunt M, Lopez P, Uppala A, Rosati D, Rodrigues
    NP, Grabitz P, Rife SC. scite: A smart citation index that
    displays the context of citations and classifies their intent
    using deep learning. *Quantitative Science Studies*. 2021;
    2(3):882–898. DOI: 10.1162/qss_a_00146.

[^5]: Jergas H, Baethge C. Quotation accuracy in medical journal
    articles — a systematic review and meta-analysis. *PeerJ*. 2015;
    3:e1364. DOI: 10.7717/peerj.1364. PMID: 26528420.

[^6]: Wager E, Middleton P. Technical editing of research reports in
    biomedical journals. *Cochrane Database of Systematic Reviews*.
    2008;(4):MR000002. DOI: 10.1002/14651858.MR000002.pub3.
    PMID: 18843753.

[^7]: Simkin MV, Roychowdhury VP. Read before you cite! *Complex
    Systems*. 2003; 14:269–274. arXiv: cond-mat/0212043.

[^8]: Cohan A, Ammar W, van Zuylen M, Cady F. Structural scaffolds for
    citation intent classification in scientific publications.
    *NAACL 2019*. arXiv: 1904.01608.

**Research gap:** A "Smith & Banks 1991 *BMJ*" citation-accuracy
paper appears in some bibliographies and was sketched here, but it
could not be located in CrossRef, PubMed, or Google Scholar searches
during the May 2026 knowledge-layer sweep, nor in a repeat web search
during the October 2026 refresh. The closest foundational
work in this vein is de Lacey, Record & Wade (1985) *BMJ* and
Eichorn & Yankauer (1987) *AJPH* (entry [^2] above) — both are
methodologically primary for this skill's grounding and the Smith &
Banks reference is not load-bearing. The claim has been left here
as a gap rather than fabricated. *What would verify it: locating the
exact Smith & Banks 1991 paper (or confirming the citation was a
secondary-source misattribution).*
