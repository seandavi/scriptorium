# Internal consistency: detecting contradictions and drift within a single manuscript

*Last updated: 2026-05-17*

## Synthesis

Internal consistency checking is the audit of a manuscript against
itself: does Table 1's N match the methods N? Does the abstract's
percentage match Figure 2? Does the conclusion match the hypothesis
the introduction announced? Does the limitations section concede X
while the discussion claims not-X? These are not deep
domain-knowledge questions — they are *bookkeeping* questions, and
they are exactly the kind of error a careful author makes regularly
because manuscripts are written nonlinearly across many sessions, with
numbers and definitions migrating as the analysis evolves.

The empirical evidence that internal-consistency errors are common is
indirect but converging. Schroter et al. (2008) found that reviewers
detect roughly 29% of inserted major errors at baseline (see
[[critique-quality-evidence]]); a meaningful share of those undetected
errors are within-manuscript inconsistencies that should have been
catchable from text alone. The statistical-consistency literature
(Nuijten et al. 2016 — see [[statistical-inconsistency]]) found that
half of NHST-using psychology papers contained at least one
statistically inconsistent p-value, an even more specific form of
internal inconsistency. And the spin literature (Boutron 2010 — see
[[logical-fallacy-detection]]) documents that abstract Conclusions
routinely contradict abstract Results in interpretation, if not in
number.

For scriptorium this category is unusually tractable: the questions
have right answers (the number is either equal or not), the textual
locations are well-defined (abstract vs. methods vs. results vs.
discussion), and modern LLMs can perform the cross-section matching
reliably *when the comparison is textual*. Where the comparison
requires recomputation — e.g. is this percentage compatible with this
N? — the skill should call out to a script. See
[[statistical-inconsistency]] for the numerical-recomputation tools
and the honest LLM-limitation framing.

## Techniques and tools

### Terminology drift

The same concept named multiple ways within a single manuscript is a
common drift pattern: "the model" / "our method" / "the classifier"
referring to the same artifact; "patients" / "subjects" /
"participants" used interchangeably; "AUROC" / "AUC" / "C-statistic"
referring to the same quantity. The audit is simple in principle:
identify candidate synonyms, cluster them, ask the author to choose a
preferred term and replace.

The scriptorium design pattern for this is the
**MANUSCRIPT_STATE.yaml** terminology block, which declares preferred
and forbidden terms. A `terminology-normalization` skill (Phase 3 per
DESIGN.md) consumes the block. Where the preferred term has not yet
been declared, the consistency check can flag candidate-synonym
clusters for the author to resolve.

### Numerical-claim consistency

The most common errors:

- **Sample size drift**: Methods says N=312; Table 1 says N=308; the
  abstract says "more than 300." The audit is to extract each N
  mention and compare. Discrepancies often reflect legitimate exclusion
  (e.g. dropouts) but should be explained explicitly.
- **Percentage / proportion mismatch**: a percentage in the abstract
  cannot be derived from any N in the methods. This is where
  techniques like **GRIM** ([[statistical-inconsistency]]) become
  diagnostic — a reported mean of 4.31 on an N=14 integer scale is
  *mathematically impossible*.
- **Effect-size mismatch**: the abstract reports an odds ratio that
  differs from the Results table.
- **Confidence-interval / p-value internal inconsistency**: covered
  in detail by Statcheck — see [[statistical-inconsistency]].

LLMs can extract numerical claims reliably; comparison is the easy
part. The work is in defining the *equivalence class* — does "more
than 300" match N=312? — and in deciding whether a small numerical
difference is a genuine discrepancy or a rounding artifact.

### Figure-text alignment

Does the figure show what the text describes? Failure modes:

- Text describes a trend in one direction; figure shows the
  opposite.
- Text claims significance for a comparison the figure does not in
  fact show.
- Figure legend names panels A–D but the text refers to panels A–E.
- The figure shows three groups; the text discusses two.

Vision-capable LLMs can partially perform this audit, but it remains
in scope as a *future* skill (DESIGN.md flags `figure-text-alignment`
as Phase 3). Pre-vision tooling is restricted to checking textual
figure-references against figure-legend text — which catches the
panel-label and group-count failure modes, but not the more substantive
"the trend in the image is opposite to the text" failure.

### Methods–results–discussion alignment

A standard internal-consistency audit walks each *claim* in the
discussion section and asks: which result in the Results section
supports this? Does the methods section actually permit that result?
A simple structured prompt — "for each discussion claim, identify the
results passage that supports it" — surfaces orphan claims (no
supporting result) and orphan results (no discussion).

This is closely related to argument mapping ([[argument-mapping]])
applied to the manuscript as a whole rather than to individual
paragraphs. The Toulmin decomposition is the same — claim, data,
warrant — but the *data* in this context is the results section, and
the *warrant* is the methodological premise the methods section
established.

### Self-contradiction detection

Failure modes:

- Limitations section: "we did not assess long-term outcomes."
  Conclusion: "supports use as a long-term strategy."
- Methods: "exploratory analysis."
  Discussion: language treating the finding as confirmatory.
- Introduction: pre-specified primary hypothesis was X.
  Results: the reported primary outcome is Y.

The introduction–results mismatch is the textual fingerprint of
HARKing (Kerr 1998; see [[logical-fallacy-detection]]). Yarkoni (2019)
[^1] argues that even when the hypothesis literally matches, the
*verbal* hypothesis is often broader than the *statistical*
hypothesis the analysis actually tests — a more subtle but equally
detectable mismatch.

### Hypothesis–results consistency and HARKing fingerprints

Detecting HARKing from a single manuscript is partial:

- **What's detectable**: introduction hypothesis vs. reported primary
  outcome (mismatch is a smell); confidence of language in
  introduction vs. open-ended exploratory language in methods.
- **What's not**: post-hoc rephrasing that aligns the introduction to
  the data. Full HARKing detection requires preregistration
  comparison.

Where preregistration exists (OSF, ClinicalTrials.gov), a future
audit skill can compare. Where it doesn't, the skill can only flag
*plausible* HARKing — language patterns consistent with a post-hoc
narrative re-fit.

### Tools that operationalise internal consistency

- **SciScore** [^2] — automated assessment against MDAR / ARRIVE /
  CONSORT-derived rigor criteria, scanning the methods section for
  declared elements (blinding, randomization, RRIDs). SciScore is
  closer to a *reporting-completeness* audit than a self-consistency
  audit, but the two overlap on items like "the methods declares
  randomization; the results table reports the post-randomization
  groups."
- **Penelope.ai** [^3] — pre-submission manuscript-quality checker
  used by several journals (BMJ Open and others); applies a
  customisable battery of 30+ checks. Like SciScore, primarily
  presence-of-element rather than consistency-of-element.
- **Statcheck** [^4] — discussed in detail at
  [[statistical-inconsistency]]; detects internal inconsistencies
  between p-values and their test statistics + degrees of freedom.
- **scrutiny** (R package, github.com/lhdjung/scrutiny) [^5] —
  bundles GRIM, GRIMMER, DEBIT, SPRITE for downstream use; relevant
  here because GRIM-class checks are internal-consistency checks at
  the level of the reported summary statistics.

Outside these specific tools, internal-consistency auditing remains
largely manual — and that gap is one of the more obvious places where
a structured LLM critique can usefully contribute.

## How this informs scriptorium

- **A future `internal-consistency` critique skill** is a high-value
  Phase 3 target. The audit is structured (cross-section comparison),
  well-defined (right answers exist), and within current LLM
  capability for the textual cases.
- The structured-output discipline is critical here: each flagged
  discrepancy should emit `{location_a, location_b, claim_a, claim_b,
  discrepancy_type}` so the author can navigate to both passages
  immediately.
- `reviewer-simulation` should include a "structural reviewer"
  persona whose remit is internal consistency — the bookkeeping
  reviewer that academic peer review rarely supplies but that
  routinely catches genuine errors.
- The MANUSCRIPT_STATE.yaml *core claims* declaration is the
  natural anchor for self-contradiction detection: each declared
  claim is checked against limitations, methods, and results.

LLM limits — be honest:

- Numerical consistency requires *recomputation*, not just textual
  comparison. The skill should call out to a Python script (or
  Statcheck / GRIM / SPRITE) for verification rather than asking
  the LLM to reason about whether a percentage is compatible with
  an N. LLM arithmetic is notoriously unreliable on this exact task.
- Figure–text alignment for the substantive content (trend
  direction, panel meaning) requires vision capability and remains
  partial even with it.
- Plausible-HARKing detection generates false positives — a
  legitimate exploratory paper with frank language about
  exploration may trip the same heuristics.

## Limits and caveats

- Internal consistency is a *necessary* but profoundly *insufficient*
  condition for a manuscript being correct. A paper can be perfectly
  internally consistent and still be wrong.
- Self-consistency audits punish honest hedging: a discussion that
  raises a counterargument and refutes it can look like
  self-contradiction to a naive pattern-matcher. The skill must
  distinguish *argued* tension from *unintended* contradiction.
- The HARKing-fingerprint heuristic is contested — defensible
  exploratory science can look HARKed by these textual signals, and
  flagging it as such risks chilling exploratory work. Hedged
  language ("results consistent with") is preferable to verdict.

## References

[^1]: Yarkoni T. The generalizability crisis. *Behavioral and Brain
    Sciences*. 2019 (online); 45:e1. DOI: 10.1017/S0140525X20001685.
    Argues that the verbal-vs-statistical hypothesis mismatch is a
    pervasive form of internal inconsistency even when literal
    hypothesis statements are preserved.

[^2]: Menke J, Roelandse M, Ozyurt B, Martone M, Bandrowski A. The Rigor
    and Transparency Index Quality Metric for Assessing Biological and
    Psychological Research Articles. *iScience*. 2020; 23(11):101698.
    DOI: 10.1016/j.isci.2020.101698. SciScore product page:
    https://sciscore.com/.

[^3]: Penelope.ai — automated pre-submission manuscript checking.
    https://www.penelope.ai/. No primary methods paper located in
    accessible sources; described in journal editorial workflow
    documentation. [TODO verify a peer-reviewed methods reference if
    one exists.]

[^4]: Nuijten MB, Hartgerink CHJ, van Assen MALM, Epskamp S, Wicherts
    JM. The prevalence of statistical reporting errors in psychology
    (1985–2013). *Behavior Research Methods*. 2016; 48(4):1205–1226.
    DOI: 10.3758/s13428-015-0664-2. PMID: 26497820.

[^5]: Jung LH. scrutiny: Error detection in science (R package).
    https://github.com/lhdjung/scrutiny. Bundles GRIM, GRIMMER, DEBIT,
    SPRITE implementations.
