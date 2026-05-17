# Logical-fallacy detection in scientific writing

*Last updated: 2026-05-17*

## Synthesis

A *fallacy* is an error in reasoning that produces an argument whose
conclusion does not in fact follow from its premises, even though the
inference may look plausible. Logicians distinguish **formal** fallacies
— invalid by virtue of their syntactic structure (e.g. affirming the
consequent) — from **informal** fallacies, whose problems lie in the
content, context, or pragmatic use of the argument (e.g. appeal to
authority, false dichotomy, hasty generalization). Scientific
manuscripts overwhelmingly fail in informal ways: a paper's syntactic
logic is rarely the issue; its inferential warrants almost always are.

Two empirical bodies of work matter here. First, the "spin" literature
(Boutron et al. 2010 [^1] and follow-ons) documents that
*interpretive* fallacies — overstating effects, conflating significance
with importance, attributing causation from correlation — appear in
roughly half of RCT discussion sections even when the underlying
analysis is competently executed. Second, the methodological-critique
literature (Kerr 1998 on HARKing [^2]; Nuzzo 2014 on p-value
misunderstanding [^3]; the 2016 ASA statement on p-values) documents
that several specific fallacies have become so endemic that they are
better treated as reportable patterns than as occasional lapses.

For scriptorium, the practical implication is that fallacy detection
is *pattern matching against a small canonical list*, not an attempt
at general-purpose logical analysis. The list is short — perhaps
twelve to twenty patterns account for the vast majority of in-science
inferential errors — and each pattern has both a definition and a
canonical surface form an LLM can flag. See
[[argument-mapping]] for the structural underpinnings and
[[citation-claim-alignment]] for the closely related problem of
overclaim through citation.

## Techniques and tools

### The canonical taxonomies

- **Bo Bennett, *Logically Fallacious*** (2012 / 2021 Academic Edition,
  ISBN 9781456607524 [hardback]) [^4]. The book and the companion site
  https://www.logicallyfallacious.com/ document ~300 fallacies with
  definition, example, and logical form. The site is the most
  comprehensive open inventory; the book imposes a usable taxonomy.
- **Wikipedia "List of fallacies"** — a community-maintained inventory
  organised by formal / informal / pragmatic categories; useful as a
  cross-check, less rigorous than Bennett.
- **Walton, Reed & Macagno** *Argumentation Schemes* (see
  [[argument-mapping]]) — frames each "fallacy" as a *scheme misuse*
  paired with a known critical-question audit. This is the most
  productive frame for pattern detection because it forces the
  fallacy to point at a missing answer.

### The high-frequency in-science fallacies

The patterns below are the ones that surface most often in biomedical
peer review and post-publication critique. Each has a recognizable
surface form an automated check can match against.

1. **Post hoc ergo propter hoc / correlation as causation.** Inferring
   that A causes B from the observation that A precedes B, or from a
   correlation in observational data. The default fallback in
   observational epidemiology and increasingly in single-cell /
   association studies. Surface form: "X was associated with Y,
   suggesting that X drives / causes / leads to Y."

2. **Affirming the consequent.** Formal fallacy: from "if H then D" and
   "D" inferring "H." In science, frequently dressed as "our model
   predicted this pattern; we observed this pattern; therefore our
   model is correct." Without an alternative-hypothesis check, this
   is a fallacy.

3. **False dichotomy.** Presenting two options as exhaustive when more
   exist. Common in discussion sections: "either X mechanism or Y
   mechanism."

4. **Hasty generalisation.** Drawing a population-level conclusion from
   a small or non-representative sample. Surface form: small-N or
   single-site studies that conclude "this is true of [broad
   population]."

5. **Appeal to authority.** Citing a senior researcher or major journal
   as warrant rather than the underlying data. Walton's critical
   questions for "argument from expert opinion" make the audit
   concrete (see [[argument-mapping]]). Note: in science, citation of
   established results is *not* an automatic appeal-to-authority
   fallacy — the test is whether the citation does inferential work
   the cited evidence can support.

6. **Base-rate neglect.** Ignoring prior probability when interpreting
   a positive test result or association. Endemic in diagnostic
   accuracy reporting, screening papers, and rare-disease research.
   Nuzzo (2014) [^3] gives the canonical worked example: a p<0.05
   result on a low-prior hypothesis still has high posterior
   probability of being a false positive.

7. **p-hacking as reasoning.** Inferring an effect by exploiting
   analytic flexibility — multiple outcomes, multiple subgroups,
   multiple covariate adjustments — until p < 0.05 [^3]. The cognitive
   move that makes this a fallacy (and not merely a procedural error)
   is *treating the surviving result as if it had been pre-specified*.

8. **HARKing — Hypothesizing After the Results are Known.** Kerr 1998
   [^2] defined HARKing as "presenting a post hoc hypothesis (i.e.,
   one based on or informed by one's results) in one's research report
   as if it were, in fact, an a priori hypothesis." Kerr's survey
   found HARKing widely practiced and widely viewed as inappropriate.
   HARKing is the upstream cause of many spurious "novel" findings
   and is detectable from internal evidence — see
   [[internal-consistency]] and Yarkoni 2019 [^5].

9. **Overgeneralisation from a model organism / model system.**
   Inferring human relevance from cells in a dish, a single mouse
   strain, or a single cohort.

10. **Equivocation / shifting definitions.** Using a key term in one
    sense in the methods and a different sense in the conclusion.
    Particularly common with terms like "significant," "validated,"
    "associated."

11. **Composition / division.** Inferring properties of the whole from
    parts, or vice versa. Surface form: aggregating subgroup effects
    into a population-level claim without test for heterogeneity.

12. **Survivorship / selection bias as reasoning.** Drawing a
    conclusion from a sample defined by an outcome rather than by
    enrolment, then interpreting the sample as representative.

### Spin as a special class

Boutron et al. (2010) [^1] analysed 72 RCTs with nonsignificant primary
outcomes published in December 2006 and found spin — the systematic
distortion of interpretation to favour the experimental treatment — in
**18.0%** of titles, **37.5%** of abstract Results sections, **58.3%**
of abstract Conclusions, and **50.0%** of main-text Conclusions. The
detailed spin taxonomy (focus on within-group analyses, focus on
secondary outcomes, focus on subgroup analyses, downplay of
nonsignificance) is in effect a catalogue of *interpretive* fallacies
specific to clinical trials. Yavchitz et al. (2012) showed that this
spin propagates linearly into press releases and news coverage. See
[[citation-overreach-research]] for the full citation chain.

### Cognitive-bias literature

Kahneman's *Thinking, Fast and Slow* (2011) and the broader
heuristics-and-biases programme are the substrate behind several of the
above patterns: anchoring (the first number reported sets the frame),
availability (vivid examples dominate inference), and confirmation
bias (researchers preferentially see evidence consistent with their
hypothesis). Mlodinow's *The Drunkard's Walk* (2008) is the canonical
popularisation of base-rate neglect. The substantive evidence base for
"researchers exhibit the same biases as anyone else" is robust enough
that scriptorium should treat this as background, not a finding to be
debated.

## How this informs scriptorium

- **`reviewer-simulation`** can be primed with the 12-pattern list
  above as an explicit checklist. Each persona walks the conclusions
  section against the list and reports either "no instance flagged"
  or "instance flagged at [passage], pattern: [name], reason: [why]."
- **`argumentative-flow`** can detect surface forms of correlation→
  cause and overgeneralisation through targeted prompts; high-recall,
  modest-precision is the realistic operating point.
- **A future `spin-audit`** could implement the Boutron taxonomy on
  abstract Conclusions sections; this is a narrow, high-value target
  because spin is both prevalent and identifiable from text alone.
- Make the patterns *named*, not vibes: every flagged fallacy should
  cite the pattern by name (and ideally a Bennett / Walton reference)
  so the author can argue back if the LLM is wrong.

### LLM limits — be honest

- LLMs detect surface forms reliably but cannot reliably distinguish
  between a *valid* appeal to expertise (a domain-appropriate citation
  doing real work) and a *fallacious* appeal to authority. This is a
  warrant-validity question, not a textual one.
- HARKing detection from a single manuscript is partial at best (see
  [[internal-consistency]]); full detection requires preregistration
  comparison.
- Base-rate fallacies require numerical reasoning the model often
  hallucinates. For prevalence/PPV calculations the skill should call
  out to a script (see [[statistical-inconsistency]]) rather than
  recompute in-band.

## Limits and caveats

- The fallacy list above is *prescriptive*, not exhaustive. Several
  authors (notably Boudry) have argued that the fallacy-theoretic
  frame itself is overused — that what looks like an appeal-to-
  authority is often a legitimate appeal to consensus, and that
  fallacy spotting can substitute for engagement with substance.
- Distinguishing a fallacy from a *defeasible-but-permissible*
  inference requires context. Scriptorium critiques should always
  flag with hedging ("possible appeal to authority — does the cited
  paper actually support the claim?") rather than verdict ("appeal
  to authority").
- The "spin" taxonomy is well-established for RCTs and less well-
  developed for observational studies, basic-science papers, and
  computational methods papers. Adapting it to those genres remains
  ongoing methodological work.

## References

[^1]: Boutron I, Dutton S, Ravaud P, Altman DG. Reporting and
    Interpretation of Randomized Controlled Trials With Statistically
    Nonsignificant Results for Primary Outcomes. *JAMA*. 2010;
    303(20):2058–2064. DOI: 10.1001/jama.2010.651. PMID: 20501928.

[^2]: Kerr NL. HARKing: Hypothesizing After the Results are Known.
    *Personality and Social Psychology Review*. 1998; 2(3):196–217.
    DOI: 10.1207/s15327957pspr0203_4. Definition: "presenting a post
    hoc hypothesis (i.e., one based on or informed by one's results)
    in one's research report as if it were, in fact, an a priori
    hypothesis." Note: the original prompt referenced DOI suffix
    `0204_1`; the correct DOI suffix is `0203_4` (verified).

[^3]: Nuzzo R. Scientific method: statistical errors. *Nature*. 2014;
    506(7487):150–152. DOI: 10.1038/506150a.

[^4]: Bennett B. *Logically Fallacious: The Ultimate Collection of
    Over 300 Logical Fallacies (Academic Edition)*. eBookIt.com,
    2012; expanded 2021. ISBN 9781456607524 (Academic Edition
    hardback). Companion site: https://www.logicallyfallacious.com/.

[^5]: Yarkoni T. The generalizability crisis. *Behavioral and Brain
    Sciences*. 2019 (published online 2020); 45:e1.
    DOI: 10.1017/S0140525X20001685.
