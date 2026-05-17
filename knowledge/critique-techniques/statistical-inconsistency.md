# Statistical inconsistency: forensic detection of reporting errors

*Last updated: 2026-05-17*

## Synthesis

Over the past decade an unusually productive research programme has
developed mathematical and computational techniques for detecting
internal inconsistencies in published statistics — errors that follow
purely from the algebra of the reported numbers, regardless of access
to the underlying data. These tools — Statcheck, GRIM, GRIMMER, SPRITE,
DEBIT, the Carlisle baseline-statistic method — share a common
methodological frame: they ask whether the reported summary statistics
are mathematically possible (or plausible) given each other and the
declared sample size. When the answer is no, something is wrong:
typically a transcription error, occasionally an analysis error,
sometimes evidence of fabrication.

Statcheck (Nuijten et al. 2016) [^1] is the most widely deployed and
most consequential of these tools. It established that **roughly half
of psychology papers using NHST contain at least one inconsistency
between a reported p-value and its test statistic + degrees of freedom,
and roughly one in eight contains an inconsistency large enough to
change a statistical conclusion**. GRIM (Brown & Heathers 2017) [^2]
extends the same approach to the relationship between a reported mean,
its sample size, and the granularity of the underlying scale.
GRIMMER [^3] extends GRIM to standard deviations. SPRITE [^4]
reconstructs candidate raw datasets compatible with reported summary
statistics, allowing visual inspection of whether the implied
distribution is plausible. DEBIT does the same for binary data.
Carlisle's anaesthesia-trial method [^5] tests whether the
distribution of baseline-comparison p-values across many trials follows
the uniform distribution expected from random sampling.

For scriptorium the lesson is uncomfortable but clear: most of these
checks require *numerical computation*, not language understanding.
An LLM asked to "verify whether F(2, 84) = 3.41 corresponds to
p = 0.038" will hallucinate confidently. The honest design is for
scriptorium skills to extract candidate statistics from a manuscript
and call out to Statcheck (or a re-implementation) rather than attempt
in-band verification. See [[internal-consistency]] for the broader
within-manuscript audit and [[forensic-methodology]] for the
post-publication sleuthing context.

## Techniques and tools

### Statcheck (Nuijten et al. 2016)

Statcheck [^1] extracts APA-style null-hypothesis-significance-test
reports from text — patterns like `t(48) = 2.13, p = .039` or
`F(2, 84) = 3.41, p = .03` — recomputes the p-value from the reported
test statistic and degrees of freedom, and flags discrepancies. The
software is the spell-checker analogue for statistics.

Headline empirical findings from the 250,000+ p-value audit across
eight major psychology journals 1985–2013:

- **~50%** of papers using NHST contained at least one reporting
  inconsistency between p, test statistic, and df.
- **~13%** of papers contained at least one *gross* inconsistency
  large enough to potentially change the statistical conclusion
  (e.g. a p < .05 result that recomputed to p > .05).
- Errors were not randomly distributed; they tended to be in
  directions favouring statistical significance — i.e. systematic
  bias, not just noise.

The R package is at https://github.com/MicheleNuijten/statcheck [^6];
web interfaces exist at several URLs. A validation study (Schmidt
2017) found that for clean APA-style reporting Statcheck achieves
high accuracy; precision drops on noisy or non-APA formats. A
follow-on validity study (Nuijten et al. 2017 OSF preprint) compared
Statcheck flags against manual reanalysis and found sensitivity and
specificity both above 95% for properly formatted results.

### GRIM (Brown & Heathers 2017)

GRIM — Granularity-Related Inconsistency of Means — exploits a
trivial mathematical fact: for N integer observations, the arithmetic
mean must be expressible as some integer numerator over N. A reported
mean of 4.31 on N=14 integer responses is therefore mathematically
impossible (the closest legal values are 4.286 and 4.357).

Brown & Heathers [^2] tested 260 recent psychology papers; **71 were
testable with GRIM**; of those, **about half (36/71) contained at
least one inconsistent mean** and **more than 20% (16/71) contained
multiple inconsistencies**. The test requires only the reported mean,
the sample size, the scale granularity (e.g. integer Likert items),
and the number of items per participant.

GRIM is implemented in the `scrutiny` R package
(github.com/lhdjung/scrutiny) [^7] and in `pysprite` and related
Python ports.

### GRIMMER (Anaya 2016)

GRIMMER extends GRIM to standard deviations and variances [^3]. The
key insight: for granular data, the variance is also constrained to a
finite set of values given the mean and sample size. The test
identifies impossible SDs given the reported mean, N, and granularity.
The PeerJ Preprint and implementation in `scrutiny` are the canonical
references; ability of the test to flag inconsistency depends on
sample size, granularity, decimal precision of the reported statistic,
and the size of the SD. GRIMMER is genuinely diagnostic in many real
papers and frequently flags errors GRIM alone misses.

### SPRITE (Heathers, Anaya, van der Zee, Brown 2018)

SPRITE — Sample Parameter Reconstruction via Iterative TEchniques [^4]
— attempts the inverse problem: given a reported mean, SD, and
sample size for granular data, reconstruct candidate raw datasets
compatible with those summary statistics. Visualising the candidate
distributions often makes implausibility obvious — e.g. the implied
distribution requires a bimodal cluster of extreme values that no
plausible response process would generate.

SPRITE is heuristic, not deterministic; it returns *plausible*
distributions rather than the actual data. Its value is in flagging
cases where *no* plausible distribution exists or where the only
distributions consistent with the summaries are bizarre. PeerJ
Preprint: DOI 10.7287/peerj.preprints.26968v1. Python implementation:
github.com/QuentinAndre/pysprite.

### DEBIT (Heathers & Brown)

DEBIT — Descriptive Binary Inconsistency Test — applies the same logic
to binary data. For binary observations, the standard deviation is a
direct function of the mean and N; reported SDs incompatible with the
reported proportion are detectable. Implementation in `scrutiny`:
https://lhdjung.github.io/scrutiny/reference/debit.html.

### Carlisle baseline-distribution method

Carlisle (2017) [^5] analysed **72,261 baseline-table means across
29,789 variables in 5,087 RCTs** in six anaesthetic journals plus
JAMA and NEJM. The method: for each trial, compute the Stouffer-Fisher
combined p-value across baseline variables for the test of similarity
between randomised arms. Under genuine random assignment, the
distribution of these p-values across many trials should be uniform.
Carlisle found that across every journal in the sample the distribution
showed substantial deviation — excess of trials with baseline
similarity p-values near 0 (suspicious similarity) *and* near 1
(suspicious dissimilarity). In approximately **6% of trials**, the
baseline-comparison statistics were either too similar or too
dissimilar to be plausibly random.

The Carlisle methodology is *not* a per-trial fabrication detector —
the author was explicit that individual flagged trials could have
benign explanations — but it is a corpus-level red flag that has led to
multiple high-profile retractions and to ongoing scrutiny of specific
researchers' bodies of work. The method has been re-examined and
partially critiqued in follow-up work (e.g. Bolland et al. 2017
preprint) which highlighted statistical-assumption sensitivities.

### Stuart Ritchie's *Science Fictions* (2020)

Ritchie [^8] provides the lay-readable synthesis of this tool family
in the context of the broader replication crisis (ISBN 9781250222695,
US hardcover; 9781847925657, UK). Particularly useful for explaining
why these forensic tools are *not* a substitute for replication, and
for situating Statcheck-class checks within the larger reform agenda.

## How this informs scriptorium

- **A future `statistics-consistency` skill** (DESIGN.md Phase 3) is
  the right home for this work. The realistic scope is *Statcheck-
  like* on the test-statistic/p-value pairs in the manuscript, plus
  flagging candidate (mean, N, granularity) tuples for downstream
  GRIM checks.
- **Critical implementation discipline**: the LLM does the
  *extraction* (find the statistical statements in the text); the
  *verification* is performed by a deterministic recomputation
  script. Letting the LLM do the arithmetic in-band is a known
  failure mode and produces confident-but-wrong critique.
- **Skill output**: structured tuples of `(reported_statistic,
  recomputed_statistic, discrepancy_magnitude, gross_flag)` — the
  same schema Statcheck emits.
- **Composition with other skills**: `internal-consistency` should
  treat Statcheck-class checks as one of its check families;
  `reviewer-simulation` should include a statistical reviewer
  persona that consumes the Statcheck output as their prior.

LLM limits — be honest and emphatic:

- **LLMs cannot reliably recompute p-values.** They will get the
  algebra wrong, particularly for F-tests and chi-square. Always
  call out to a script.
- **GRIM, GRIMMER, SPRITE require numerical computation** the LLM
  cannot reliably perform. The skill should extract the candidate
  tuples and hand off.
- **Carlisle-type baseline-distribution analysis** is corpus-level
  and out of scope for a per-manuscript critique skill. It belongs
  in a future forensic-audit skill operating on a researcher's body
  of work.
- Where the LLM is genuinely useful: locating where in a manuscript
  the relevant tuples appear, deciding whether a flagged
  inconsistency is consequential (does it change a conclusion?),
  and writing the critique sentence around the recomputed result.

## Limits and caveats

- Statcheck's effective scope is **APA-style NHST reporting** —
  largely psychology, partially clinical-trials-with-APA-conventions,
  not most basic-science. Adapting to other reporting styles
  (e.g. `chi^2(2) = 5.7` rendered in LaTeX) requires parser work.
- GRIM/GRIMMER require granular data; they do not apply to
  continuous-variable means. Many biomedical means are continuous
  and out of scope.
- SPRITE is heuristic; "no plausible distribution found" can also
  mean "the search was too short." Output should be treated as
  hypothesis-generating, not verdict-generating.
- The Carlisle method has been productively critiqued for
  assumption sensitivity. Treat outputs as flags for human
  investigation, not as fraud determinations.
- Statcheck reports inconsistencies, not fraud. Most inconsistencies
  are transcription errors; some are rounding; only a small
  fraction reflect malfeasance. Tone of any scriptorium-generated
  critique must mirror this.

## References

[^1]: Nuijten MB, Hartgerink CHJ, van Assen MALM, Epskamp S, Wicherts
    JM. The prevalence of statistical reporting errors in psychology
    (1985–2013). *Behavior Research Methods*. 2016; 48(4):1205–1226.
    DOI: 10.3758/s13428-015-0664-2. PMID: 26497820.

[^2]: Brown NJL, Heathers JAJ. The GRIM Test: A Simple Technique
    Detects Numerous Anomalies in the Reporting of Results in
    Psychology. *Social Psychological and Personality Science*. 2017;
    8(4):363–369. DOI: 10.1177/1948550616673876.

[^3]: Anaya J. The GRIMMER test: A method for testing the validity of
    reported measures of variability. *PeerJ Preprints*. 2016;
    4:e2400v1. DOI: 10.7287/peerj.preprints.2400v1.

[^4]: Heathers JAJ, Anaya J, van der Zee T, Brown NJL. Recovering data
    from summary statistics: Sample Parameter Reconstruction via
    Iterative TEchniques (SPRITE). *PeerJ Preprints*. 2018;
    6:e26968v1. DOI: 10.7287/peerj.preprints.26968v1.

[^5]: Carlisle JB. Data fabrication and other reasons for non-random
    sampling in 5087 randomised, controlled trials in anaesthetic and
    general medical journals. *Anaesthesia*. 2017; 72(8):944–952.
    DOI: 10.1111/anae.13938. PMID: 28580651.

[^6]: Nuijten MB. statcheck (R package).
    https://github.com/MicheleNuijten/statcheck. Also available on
    CRAN.

[^7]: Jung LH. scrutiny: Error Detection in Science (R package).
    https://github.com/lhdjung/scrutiny. Bundles GRIM, GRIMMER, DEBIT,
    SPRITE implementations.

[^8]: Ritchie SJ. *Science Fictions: How Fraud, Bias, Negligence, and
    Hype Undermine the Search for Truth*. Metropolitan Books, 2020.
    ISBN 9781250222695 (US hardcover); 9781847925657 (UK Bodley Head);
    9781847925664 (UK paperback).
