# Statistical inconsistency: forensic detection of reporting errors

*Last updated: 2026-10-20*

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

The 2024–2026 literature refines this picture in two ways. First, the
regex-extraction step is a known weak point. Statcheck recognises only
APA-formatted results and misses many tests reported in other styles
[^10] [^11]. That argues for LLM-assisted *extraction* feeding
deterministic *recomputation*, which is the split this note already
recommends. Second, frontier LLMs used as end-to-end paper verifiers
remain unreliable on errors that matter. On a benchmark of 91 errors
serious enough to prompt errata or retraction, no model exceeded 21.1%
recall or 6.1% precision [^17]. LLMs do better on narrowly *objective*
errors such as formulas, calculations and tables, where expert-confirmed
precision was 83% [^18]. Taken together, this is evidence for the
extract-then-recompute architecture, not against it. The 2026 INSPECT-SR
tool [^16] also brings statistical-inconsistency checks into mainstream
evidence-synthesis practice.

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
web interfaces exist at several URLs.

**Validity: contested.** The original note said that "a validation study
(Schmidt 2017) found … high accuracy". That misstated the source and is
corrected here. Schmidt's 2017 preprint is a *critique* [^10]. The
validity evidence runs as follows:

- Nuijten et al.'s 2017 validity preprint [^9] reported sensitivity
  between 85.3% and 100% and specificity between 96.0% and 100%,
  "depending on the assumptions and settings". Overall accuracy was
  96.2–99.9%.
- Schmidt [^10] reanalysed the same 49-paper benchmark including the
  tests Statcheck never recognised: about 39% of all tests (435 of
  1,120). On that basis he reported sensitivity of .52 and precision of
  60.4%.
- Böschen [^11] fed Statcheck 187 test strings in varied reporting
  styles. He concluded that it misses any result deviating even slightly
  from APA style, and argued that more flexible approaches (JATSdecoder,
  LLMs) are needed.
- Nuijten replied [^12] that Statcheck "does exactly what it is designed
  to do": it checks APA-reported NHST results.

*Interpretation.* Both sides agree on the facts. Statcheck is highly
accurate on what it parses, and it parses only APA-formatted results.
For scriptorium, a "no inconsistencies found" result therefore needs the
denominator stated: how many results were found and checked. Silence is
not clearance.

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
github.com/QuentinAndre/pysprite. R implementation: the `rsprite2`
package on CRAN [^19].

### DEBIT (Heathers & Brown)

DEBIT — Descriptive Binary Inconsistency Test — applies the same logic
to binary data. For binary observations, the standard deviation is a
direct function of the mean and N; reported SDs incompatible with the
reported proportion are detectable. Implementation in `scrutiny`:
https://lhdjung.github.io/scrutiny/reference/debit.html. The `scrutiny`
package description cites the method as Heathers and Brown (2019),
https://osf.io/5vb3u/ [^7].

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
(suspicious dissimilarity). Among unretracted trials, **15.2%
(763/5,015) had trial p-values within 0.05 of 0 or 1, against 10%
expected**, an excess of about 5 percentage points. Among trials that
had already been retracted, the figure was 43% (31/72) [^5]. (The
earlier "approximately 6% of trials" wording did not match the abstract
and has been corrected.)

The Carlisle methodology is *not* a per-trial fabrication detector —
the author was explicit that individual flagged trials could have
benign explanations — but it is a corpus-level red flag that has led to
multiple high-profile retractions and to ongoing scrutiny of specific
researchers' bodies of work. The method has been re-examined and
partially critiqued in follow-up work by Bolland and colleagues.
Their simulations found that baseline p-values computed from *rounded*
summary statistics are not uniformly distributed, whereas randomisation
method, non-normality and correlation between baseline variables had
no important effect [^13]. Continuous baseline variables gave uniform
distributions but categorical variables did not [^14]. The same group
later published empirically generated reference proportions to use in
place of the uniform expectation when summary statistics are rounded
[^15]. (These replace an unidentified "Bolland et al. 2017 preprint"
citation.)

### INSPECT-SR (2026): trustworthiness checks in evidence synthesis

Wilkinson et al. published INSPECT-SR in *BMJ* in September 2026 [^16],
updating a 2025 medRxiv preprint [^16]. It is a consensus tool for deciding
whether a randomised trial is trustworthy enough to include in a
systematic review. It contains **21 checks across four domains**:
post-publication notices; conduct, governance and transparency; text and
figures; and results in the study. The guidance notes that some checks
require the ability "to perform and interpret some basic statistical
tests". Its author group includes the GRIM, SPRITE and `scrutiny`
developers (Brown, Heathers, Jung). INSPECT-SR is the first
consensus-developed instrument in this list. It shows the forensic
checks in this note moving from sleuthing practice into standard
systematic-review method. *(The individual checks were not itemised in
the source pages we could access. Which checks correspond to
GRIM-, baseline- or Carlisle-style tests is unverified.)*

### LLMs as error detectors (2025–2026)

Two 2025 preprints give the first quantitative evidence on LLMs as
end-to-end paper checkers:

- **SPOT** (Son et al. 2025) [^17] paired 83 published papers with 91
  errors serious enough to prompt errata or retraction. The best model
  (o3) reached at most 21.1% recall and 6.1% precision, and the other
  models scored near zero. Across eight runs, models "rarely rediscover
  the same errors".
- **Bianchi et al. 2025** [^18] built a GPT-5 "Paper Correctness
  Checker" restricted to *objective* errors (formulas, derivations,
  calculations, figures, tables) in AI-conference papers. Experts
  confirmed 263 of 316 flagged items, a precision of 83.2%.

*Interpretation.* LLMs are useful at finding *candidate* objective
inconsistencies and poor at reliably finding the errors that matter
most. Neither study tests recall on statistical-test recomputation
specifically. Neither licenses dropping deterministic recomputation.

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
  failure mode and produces confident-but-wrong critique. The
  Statcheck coverage critique [^10] [^11] makes LLM extraction the
  natural replacement for regex extraction. It does not make the LLM a
  suitable *recomputer*; the SPOT results [^17] argue against
  end-to-end LLM verification.
- **Skill output**: structured tuples of `(reported_statistic,
  recomputed_statistic, discrepancy_magnitude, gross_flag)` — the
  same schema Statcheck emits. The report should also state coverage:
  how many results were extracted, how many were checkable, and which
  were not checked and why. Without that, a clean result is
  uninterpretable [^10].
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

## Implementation priority for scriptorium

**Verdict:** Yes, as a planned skill. `statistics-consistency` (DESIGN.md
Phase 3) has not shipped. No current skill is grounded in this note.

**If Yes:**

- *Scope*: Statcheck-equivalent p-value recomputation, plus GRIM,
  GRIMMER and DEBIT on extracted (mean, SD, N, granularity) tuples.
- *Architecture*: LLM extraction feeds deterministic recomputation, and
  the report states coverage.
- *Required data*: none beyond the manuscript text. The recomputation
  libraries (`statcheck`, `scrutiny`, `rsprite2`) are open source.
- *Out of scope*: SPRITE as a verdict (it is heuristic) and
  Carlisle-style corpus analysis.
- *Evidence change since 2026-05*: the Statcheck validity dispute and
  the LLM-verifier benchmarks strengthen the case for this architecture
  rather than changing the verdict.

## Limits and caveats

- Statcheck's effective scope is **APA-style NHST reporting** —
  largely psychology, partially clinical-trials-with-APA-conventions,
  not most basic-science. Adapting to other reporting styles
  (e.g. `chi^2(2) = 5.7` rendered in LaTeX) requires parser work.
  Independent critiques put the share of unrecognised tests high
  enough to matter: about 39% of tests in Schmidt's reanalysis [^10].
- GRIM/GRIMMER require granular data; they do not apply to
  continuous-variable means. Many biomedical means are continuous
  and out of scope.
- SPRITE is heuristic; "no plausible distribution found" can also
  mean "the search was too short." Output should be treated as
  hypothesis-generating, not verdict-generating.
- The Carlisle method has been productively critiqued for
  assumption sensitivity, notably to rounding of summary statistics
  [^13]. Treat outputs as flags for human investigation, not as fraud
  determinations.
- Statcheck reports inconsistencies, not fraud. Most inconsistencies
  are transcription errors; some are rounding; only a small
  fraction reflect malfeasance. Tone of any scriptorium-generated
  critique must mirror this.
- LLM-as-verifier evidence is so far mostly preprints [^17] [^18], from
  AI and ML papers rather than biomedical statistics. Treat it as
  directional.

## References

[^1]: Nuijten MB, Hartgerink CHJ, van Assen MALM, Epskamp S, Wicherts
    JM. The prevalence of statistical reporting errors in psychology
    (1985–2013). *Behavior Research Methods*. 2016; 48(4):1205–1226.
    DOI: 10.3758/s13428-015-0664-2. PMID: 26497820.

[^2]: Brown NJL, Heathers JAJ. The GRIM Test: A Simple Technique
    Detects Numerous Anomalies in the Reporting of Results in
    Psychology. *Social Psychological and Personality Science*. 2017;
    8(4):363–369. DOI: 10.1177/1948550616673876. (Preprint with the
    260/71/36/16 counts: *PeerJ Preprints* 2016;4:e2064v1, DOI:
    10.7287/peerj.preprints.2064v1.)

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

[^7]: Jung L. scrutiny: Error Detection in Science (R package; v0.6.1
    on CRAN, 2025-12-02). https://github.com/lhdjung/scrutiny;
    https://cran.r-project.org/package=scrutiny. Implements GRIM,
    GRIMMER and DEBIT. SPRITE is in the separate `rsprite2` package
    [^19]; the earlier claim that `scrutiny` bundles SPRITE has been
    corrected. The CRAN description cites DEBIT as Heathers and Brown
    (2019), https://osf.io/5vb3u/.

[^8]: Ritchie SJ. *Science Fictions: How Fraud, Bias, Negligence, and
    Hype Undermine the Search for Truth*. Metropolitan Books, 2020.
    ISBN 9781250222695 (US hardcover); 9781847925657 (UK Bodley Head);
    9781847925664 (UK paperback).

[^9]: Nuijten MB, van Assen MALM, Hartgerink CHJ, Epskamp S, Wicherts
    JM. The validity of the tool "statcheck" in discovering statistical
    reporting inconsistencies. *PsyArXiv* (preprint). 2017. DOI:
    10.31234/osf.io/tcxaj.

[^10]: Schmidt T. Statcheck does not work: All the numbers. Reply to
    Nuijten et al. (2017). *PsyArXiv* (preprint). 2017. DOI:
    10.31234/osf.io/hr6qy.

[^11]: Böschen I. statcheck is flawed by design and no valid spell
    checker for statistical results. *arXiv*. 2024; arXiv:2408.07948.

[^12]: Nuijten MB. Statcheck does what it is designed to do: a reply to
    Böschen (2024). *PsyArXiv* (preprint). 2025. DOI:
    10.31234/osf.io/xyfjz.

[^13]: Bolland MJ, Gamble GD, Avenell A, Grey A. Rounding, but not
    randomization method, non-normality, or correlation, affected
    baseline P-value distributions in randomized trials. *J Clin
    Epidemiol*. 2019;110:50–62. DOI: 10.1016/j.jclinepi.2019.03.001.
    PMID: 30858019. (Corrigendum: *J Clin Epidemiol* 2020;126:226, DOI:
    10.1016/j.jclinepi.2020.05.017.)

[^14]: Bolland MJ, Gamble GD, Avenell A, Grey A, Lumley T. Baseline P
    value distributions in randomized trials were uniform for
    continuous but not categorical variables. *J Clin Epidemiol*.
    2019;112:67–76. DOI: 10.1016/j.jclinepi.2019.05.006. PMID: 31125614.

[^15]: Bolland MJ, Gamble GD, Grey A, Avenell A. Empirically generated
    reference proportions for baseline p values from rounded summary
    statistics. *Anaesthesia*. 2020;75(12):1685–1687. DOI:
    10.1111/anae.15165. PMID: 32524590.

[^16]: Wilkinson J, Bero L, Heal C, *et al.* INSPECT-SR tool for
    assessing trustworthiness of randomised controlled trials. *BMJ*.
    2026;394:e100611. DOI: 10.1136/bmj-2026-100611. PMID: 42785807.
    Guidance: https://inspect-sr.com/. Preprint: Wilkinson J, Heal C,
    Flemyng E, *et al.* INSPECT-SR: a tool for assessing trustworthiness
    of randomised controlled trials. *medRxiv*. 2025. DOI:
    10.1101/2025.09.03.25334905.

[^17]: Son G, Hong J, Fan H, Nam H, Ko H, *et al.* When AI Co-Scientists
    Fail: SPOT — a Benchmark for Automated Verification of Scientific
    Research. *arXiv*. 2025; arXiv:2505.11855.

[^18]: Bianchi F, Kwon Y, Izzo Z, Zhang L, Zou J. To Err Is Human:
    Systematic Quantification of Errors in Published AI Papers via LLM
    Analysis. *arXiv*. 2025; arXiv:2512.05925.

[^19]: Wallrich L. rsprite2: Identify Distributions that Match Reported
    Sample Parameters (SPRITE) (R package; v0.2.1 on CRAN, 2023).
    https://cran.r-project.org/package=rsprite2.
