# Citation overreach: spin, amplification, and primary-vs-review cascades

*Last updated: 2026-05-17*

## Synthesis

Citation accuracy (see [[citation-accuracy-evidence]]) is necessary
but not sufficient. A separate, well-documented failure mode is
*overreach*: the cited source exists and is technically related, but
the in-text claim is stronger, broader, or more mechanistic than the
source actually supports. Overreach is harder to detect than
miscitation because every individual citation may pass a spot-check;
the problem only surfaces in aggregate, where the chain of citations
collectively converts a hedged hypothesis into stated fact.

Three threads of evidence frame this problem. First, **spin in
primary reports** — Boutron and colleagues showed that even within a
single RCT report with statistically nonsignificant results, authors
routinely emphasize positive findings; that spin then propagates into
press releases and news coverage (Yavchitz et al.). Second, **citation
distortion as a network phenomenon** — Greenberg's *BMJ* 2009 paper
remains the clearest demonstration that a literature can establish
"unfounded authority" through citation bias, amplification, and
invention. Third, the **review-citing-review cascade** — the working
practice in which authors cite reviews rather than the primary
literature, accelerating loss of the original claim's hedging,
caveats, and effect sizes.

For `citation-audit`, the practical lesson is: do not treat a citation
as a yes/no support flag. Treat it as a question about *what kind* of
support is offered (primary data, secondary synthesis, opinion) and
*how strong* the claim relative to that support.

## Evidence

**Boutron et al. (2010), *JAMA* 303(20):2058–2064** — analyzed 72
RCTs with statistically nonsignificant primary outcomes published in
2006. Spin (defined as reporting that distorts the interpretation of
results to favor the intervention) appeared in **18.0%** of titles,
**37.5%** of abstract Results sections, and **58.3%** of abstract
Conclusions. In **23.6%** of abstracts the conclusion focused only on
treatment effectiveness despite a nonsignificant primary outcome.
In the main text, spin appeared in **29.2%** of Results, **43.1%** of
Discussion, and **50.0%** of Conclusion sections. The headline finding
is that interpretation, not data, is where overreach lives.[^1]

**Yavchitz et al. (2012), *PLOS Medicine* 9(9):e1001308** — followed
70 RCTs from publication into press release and news coverage. Spin
in the press release was strongly predicted by spin in the abstract
conclusion (RR 5.6, 95% CI 2.8–11.1, p<0.001). **51%** of news items
covering these RCTs reproduced the same spin. The findings of RCTs
were *overestimated* in **27%** of press releases. The chain
abstract → press release → news systematically amplifies overreach;
each step adds confidence and removes caveats.[^2]

**Greenberg (2009), *BMJ* 339:b2680** — the landmark citation-network
analysis. Greenberg constructed a "claim-specific citation network"
of all PubMed papers addressing whether β-amyloid is abnormally
present in inclusion body myositis muscle: 242 papers containing
relevant statements, 675 citations, **220,609 citation paths**.
Greenberg documented three distortion mechanisms:

- **Citation bias** — papers supporting the claim received **94%** of
  citations; papers weakening or refuting it received only **6%**,
  despite equal publication timing (p=0.01).
- **Amplification** — citation of papers that contain no primary
  data, expanding the apparent evidence base without adding evidence.
- **Invention** — including *citation transmutation* (hypothesis
  converted to fact through citation alone), *citation diversion*
  (citing real content while altering its meaning), and *dead-end
  citations* (citing a paper that contains no relevant evidence).

Greenberg's framing: "Citation is both an impartial scholarly method
and a powerful form of social communication. Through distortions …
citation can be used to generate information cascades." Eight of nine
NIH-funded proposals on the same topic examined in the paper showed
citation bias or invention — overreach reaches grant review, not just
manuscripts.[^3]

**Ioannidis (2005), *PLOS Medicine* 2(8):e124** — provides the
broader context. If a substantial fraction of individual research
findings are false, then citation chains that amplify them are not
neutral information transmission but active error propagation.
Ioannidis's argument does not directly measure citation behavior, but
it raises the prior probability that any single citation, if treated
as definitive, is more likely than naive readers assume to be
defending a false or fragile finding.[^4]

**Review-citing-review (no single canonical paper)** — practitioner
literature in evidence-based medicine, particularly Greenhalgh's
"How to read a paper" series, consistently warns that researchers
cite reviews where they should cite primary sources. This is partially
captured in the Pavlovic finding (see [[citation-accuracy-evidence]])
that review articles attract higher inaccuracy rates and that
citation chains account for ~20–24% of errors. The mechanism: each
review summarizes the previous review's summary; effect sizes
flatten, caveats drop, hedging language disappears, and the original
primary finding is no longer directly inspectable from any single
citation in the chain.

## How this informs scriptorium

`citation-audit` should distinguish three failure modes and emit them
as separate output sections:

1. **Quotation mismatch.** The cited source does not contain the
   claim. Handled by [[citation-accuracy-evidence]].
2. **Overreach.** The cited source contains a *weaker* version of the
   claim (e.g., a hypothesis the manuscript treats as a finding; an
   effect size described as larger than the source reports; a
   speculative discussion-section sentence treated as a result).
3. **Review-only mechanistic support.** A mechanistic, quantitative,
   or causal claim is supported only by a review citation, not a
   primary source. The recommendation is *flag for verification*,
   never *insert a primary citation* — the latter would replicate the
   LLM hallucination pattern documented in
   [[hallucination-in-llm-citations]].

For `reviewer-simulation`, an "evidence skeptic" reviewer persona
should be parameterized to mirror Greenberg's distortion categories:
prompted to look for amplification (citation density without primary
data), invention (citation diversion / transmutation), and bias
(claim-supporting citations dominating over null or refuting ones).

For `MANUSCRIPT_STATE.yaml`, the `avoid_hype: true` constraint is the
state-level analog of Boutron's spin findings — a transformation
skill operating under this constraint should refuse to harden hedged
language and should surface (not silently fix) hedged-vs-asserted
mismatches between abstract conclusions and main-text results.

## Open questions / weak evidence

- Detecting overreach automatically requires reading the cited source,
  which scriptorium does not do natively. A useful intermediate
  posture is *suspect-flag with rationale* rather than
  *verified-correct/incorrect*.
- The "review-citing-review" cascade is well-described qualitatively
  but poorly quantified outside biomedicine. The proportion of
  citation chains that actually distort the underlying claim
  (vs. faithfully summarize it) is not known.
- Greenberg's analysis is one case study (β-amyloid / IBM). The
  generalization that *all* claim-specific networks contain comparable
  distortion is plausible but not established.

## References

[^1]: Boutron I, Dutton S, Ravaud P, Altman DG. Reporting and
    interpretation of randomized controlled trials with statistically
    nonsignificant results for primary outcomes. *JAMA*.
    2010;303(20):2058–2064. doi:10.1001/jama.2010.651.
    PMID: 20501928.

[^2]: Yavchitz A, Boutron I, Bafeta A, et al. Misrepresentation of
    randomized controlled trials in press releases and news coverage:
    a cohort study. *PLOS Medicine*. 2012;9(9):e1001308.
    doi:10.1371/journal.pmed.1001308. PMID: 22984354.

[^3]: Greenberg SA. How citation distortions create unfounded
    authority: analysis of a citation network. *BMJ*.
    2009;339:b2680. doi:10.1136/bmj.b2680. PMID: 19622839.

[^4]: Ioannidis JPA. Why most published research findings are false.
    *PLOS Medicine*. 2005;2(8):e124.
    doi:10.1371/journal.pmed.0020124. PMID: 16060722.
