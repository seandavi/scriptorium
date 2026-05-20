# Critique Quality: What Makes Review Feedback Actually Useful

*Last updated: 2026-05-17*

## Synthesis

"Does peer review work?" has a more discouraging empirical answer than most researchers assume. The Cochrane systematic review on the value of peer review for biomedical journals (Jefferson et al., updated through several editions) concluded that "little empirical evidence is available to support the use of editorial peer review as a mechanism to ensure quality of biomedical research" and that "the practice of peer review is based on faith in its effects, rather than on facts" [1]. That is — review *exists*, review *is widely defended*, but the controlled evidence that the process improves what gets published is thin.

The evidence that does exist points to two narrower, more defensible claims. First, peer review *does* improve manuscripts on specific dimensions, particularly around limitations, conclusions, and reporting (Goodman, Berlin et al. 1994 at *Annals of Internal Medicine*: 33 of 34 quality items improved post-review, with the largest gains in "discussion of study limitations, generalizations, use of confidence intervals, and the tone of conclusions") [2]. Second, peer reviewers — even trained ones — detect only a fraction of major errors. Schroter et al. (2008) inserted nine major methodological errors into manuscripts sent to 607 BMJ reviewers; reviewers detected an average of 2.58 of 9 at baseline, and even with formal training detection rose only modestly and with no durable improvement [3].

What does this mean for scriptorium? Two things. (1) The benchmark a simulated reviewer should be compared against is not "perfect review" — it is "real human reviewers, who miss most major errors." A simulation that surfaces methodological concerns the author would otherwise have missed adds value even if it is not exhaustive. (2) The dimensions on which peer review has *demonstrable* effect — limitations, generalizability, tone of conclusions, reporting quality — are exactly the dimensions on which structured AI critique can plausibly contribute, because they are the dimensions for which checklists, reporting guidelines (CONSORT, STROBE, ARRIVE), and the EQUATOR framework have made expectations explicit [4].

Open peer review is the area where critique-quality evidence is most encouraging and most consistent: the BMJ randomized trial of open peer review (Walsh et al. 1999) and several subsequent F1000Research / eLife / Royal Society Open Science studies found that reviewers writing signed, publishable reviews produce more constructive and substantive comments, with no detectable loss in critical content [5]. This generalizes a design principle for scriptorium: making critique *inspectable and revisable* produces better critique, in humans and likely in agents.

## Evidence

**Does peer review catch real flaws? Mostly no.**

- Schroter S, Black N, Evans S, Godlee F, Osorio L, Smith R. What errors do peer reviewers detect, and does training improve their ability to detect them? *J R Soc Med* 101(10): 507–514 (2008). RCT-style design with 607 BMJ reviewers and three test papers each containing 9 major + 5 minor inserted errors. Baseline detection: 2.58/9 (~29%) major errors. Training increased this only modestly; gains diminished by Paper 3. Even when reviewers recommended rejection, biased randomization was the only error detected by >60% of them; many other errors were missed by the majority [3].
- Jefferson T et al. (Cochrane). "Editorial peer review for improving the quality of reports of biomedical studies." Multiple updates. Headline: insufficient empirical evidence to conclude that peer review improves quality, but also insufficient to conclude it does not. Most studies are methodologically weak [1].

**Does peer review improve manuscripts? Yes, on specific axes.**

- Goodman SN, Berlin J, Fletcher SW, Fletcher RH. Manuscript quality before and after peer review and editing at *Annals of Internal Medicine*. *Ann Intern Med* 121(1): 11–21 (1994). 111 manuscripts assessed pre- and post-review on a 34-item quality instrument; 33/34 items improved. Largest improvements in discussion of limitations, generalizations, use of confidence intervals, and tone of conclusions. Manuscripts in the bottom 50% pre-review showed 2-3× larger improvements [2].
- Cobo et al. (2007, BMJ) — statistical reviewers improve reporting in biomedical articles, RCT design. Adding a methodological/statistical reviewer led to measurable reporting-quality gains.

**Open review changes critique quality.**

- Walsh E, Rooney M, Appleby L, Wilkinson G. Open peer review: a randomised controlled trial. *Br J Psychiatry* 176: 47–51 (2000). Reviewers who signed their reviews were more courteous, somewhat more constructive, and no less critical than blinded reviewers. Some declined to review when asked to sign (a real selection effect).
- van Rooyen, Godlee, Evans, Black, Smith (1999, BMJ). Open peer review RCT: signed reviews took slightly longer and were not lower quality; recommendations did not differ systematically.
- F1000Research's post-publication open model has produced datasets that allow meta-analysis of open vs. closed review tone. Bornmann, Wolf & Daniel (2012, *Scientometrics*) "Closed versus open reviewing of journal manuscripts: how far do comments differ in language use?" finds open review comments use more constructive and explanatory language [5].

**Reviewer training has small, short-lived effects.**

- Schroter S, Black N, Evans S, Carpenter J, Godlee F, Smith R. Effects of training on quality of peer review: randomized controlled trial. *BMJ* 328: 673 (2004). PMID: 14996698. Two training interventions (face-to-face workshop, self-taught package) produced statistically detectable but small improvements in review quality that decayed within months [6].
- This null-ish finding has been replicated in subsequent reviewer-training studies. The disappointing-but-honest implication: reviewer skill is largely tacit, accumulated through extensive practice, and not easily acquired from short training.

**EQUATOR / reporting-guideline frameworks make critique tractable.**

- The EQUATOR Network maintains the canonical inventory of reporting guidelines (CONSORT for RCTs, STROBE for observational studies, PRISMA for systematic reviews, ARRIVE for animal studies, STARD for diagnostic accuracy, CARE for case reports, SPIRIT for protocols). These guidelines turn "is this reported well?" into a checklist of specific items reviewers can flag [4]. Adherence audits routinely find median compliance of 50–70% even in top journals, leaving substantial room for actionable critique.

## Design principles for scriptorium's reviewer-simulation

Translating the evidence into concrete design guidance:

1. **Anchor critiques to specific manuscript passages and specific reporting items.** Schroter et al. (2008) demonstrates that even motivated human reviewers miss most inserted errors. The remedy is not to demand the impossible (catch everything); it is to structure the search systematically. EQUATOR's checklist-driven model is the design template: each persona walks through the relevant reporting-guideline items and flags absences or weaknesses, citing the manuscript passage.

2. **Optimize for the dimensions where review has demonstrable effect.** Goodman et al. (1994) is the strongest evidence for *where* peer review improves manuscripts: limitations, generalizations, conclusions, reporting. Scriptorium's simulated review should over-index on these dimensions because they are (a) demonstrably improvable by good critique and (b) tractable to assess from manuscript text alone.

3. **Constructive form matters.** Open-review evidence (Walsh 2000, van Rooyen 1999, Bornmann 2012) shows that the *form* of a critique affects whether authors act on it. Practical pattern, supported by multiple guides: name the issue, point to the passage, explain why it matters, and (where possible) suggest a remedy. Pure complaint is consistently less effective than the four-part pattern.

4. **Explicit non-findings are part of a good review.** Because reviewers miss most errors (Schroter et al.), a review that says "I checked statistical analysis and have no concerns" carries more information than silence. Scriptorium personas should explicitly note which critique families they checked and found unproblematic — this is also the mechanism by which simulated review becomes auditable.

5. **Volume is not quality.** Bornmann, Weymuth & Daniel (2010, see [[common-critiques-taxonomy]]) found that *concentration of negative comments in fatal-flaw categories* — not total count — predicts downstream outcomes. Scriptorium should not reward verbosity; the prioritization signal lives in critique family, not critique count.

6. **Make the simulation inspectable like an open review.** The empirical advantage of open review (more constructive, no loss of substance) maps onto scriptorium's "inspectable transformations" design principle directly. Every simulated critique is logged, attributable to a persona, anchored in text. This is open review as agentic protocol.

## How this informs scriptorium

- Build personas around the dimensions peer review provably improves (limitations, generalizability, conclusions, reporting quality), not the dimensions on which human reviewers under-perform (deep design-error detection). The simulation should be honest about what it can and cannot do.
- Use reporting-guideline checklists (CONSORT, STROBE, ARRIVE etc.) as scaffolding for the methodological skeptic and statistical reviewer personas. The `MANUSCRIPT_STATE.yaml` could declare the relevant guideline; scriptorium then runs the checklist against the manuscript.
- Output format should follow the four-part open-review pattern: issue, passage reference, justification, suggested remedy. Critiques that don't fit this shape should be flagged as low-quality by the skill itself.
- Track explicit non-findings. Reviewer simulation should produce both "concerns" and "checked-no-concerns" sections; the latter is what distinguishes a structured review from a complaint generator.

## Open questions / weak evidence

- **Almost no RCT-quality evidence for AI-vs-no-AI authorial benefit.** Liang et al. (2026) is the closest analog (AI assistance to *reviewers*, not authors); the author-side experiment is open. Scriptorium's own usage data could fill this gap.
- **Are checklist-grounded critiques actually more actionable than free-form ones?** Plausible from the EQUATOR rationale but not directly tested. A small in-house experiment within scriptorium's user base would be feasible and informative.
- **The "constructive vs. destructive" literature is mostly normative.** There are commentary papers and training guides; rigorous experimental comparisons of critique styles' effect on author behavior are surprisingly thin. Sridhar's "Constructive Peer Review Made Practical: A Guide to the EMPATHY Framework" (*Journal of Marketing*, 2025; doi:10.1177/00222429241312127) is one attempt to formalize this; it is a guide/framework paper rather than a controlled empirical study, so the framework should be treated as a structured proposal, not an empirically validated intervention.
- **Generalization across fields.** Most strong evidence is from biomedicine (BMJ, *Annals*, Cochrane). Whether the same critique-quality patterns hold in CS, humanities, or qualitative social science is under-studied.
- **What does "useful critique" mean from the author's perspective?** "Author satisfaction" and "manuscript improvement" are different outcomes; the literature mostly measures one or the other, rarely both with the same design.

## References

1. Jefferson T, Rudin M, Brodney Folse S, Davidoff F. Editorial peer review for improving the quality of reports of biomedical studies. *Cochrane Database Syst Rev* (2007, multiple updates). DOI: [10.1002/14651858.MR000016.pub3](https://doi.org/10.1002/14651858.MR000016.pub3). See also the summary "Little evidence for effectiveness of scientific peer review," PMC1125118.
2. Goodman SN, Berlin J, Fletcher SW, Fletcher RH. Manuscript quality before and after peer review and editing at *Annals of Internal Medicine*. *Ann Intern Med* 121(1): 11–21 (1994). DOI: [10.7326/0003-4819-121-1-199407010-00003](https://doi.org/10.7326/0003-4819-121-1-199407010-00003). PMID: 8198342.
3. Schroter S, Black N, Evans S, Godlee F, Osorio L, Smith R. What errors do peer reviewers detect, and does training improve their ability to detect them? *J R Soc Med* 101(10): 507–514 (2008). DOI: [10.1258/jrsm.2008.080062](https://doi.org/10.1258/jrsm.2008.080062). PMID: 18840867.
4. EQUATOR Network. Reporting guidelines for health research. https://www.equator-network.org/reporting-guidelines/. CONSORT 2025: https://www.equator-network.org/reporting-guidelines/consort/.
5. Bornmann L, Wolf M, Daniel HD. Closed versus open reviewing of journal manuscripts: how far do comments differ in language use? *Scientometrics* 91(3): 843–856 (2012). DOI: [10.1007/s11192-011-0569-5](https://doi.org/10.1007/s11192-011-0569-5). See also Walsh E, Rooney M, Appleby L, Wilkinson G. *Br J Psychiatry* 176: 47–51 (2000), and van Rooyen S et al. *BMJ* 318: 23–27 (1999) for the BMJ open-review RCT.
6. Schroter S, Black N, Evans S, Carpenter J, Godlee F, Smith R. Effects of training on quality of peer review: randomized controlled trial. *BMJ* 328: 673 (2004). DOI: [10.1136/bmj.38023.700775.AE](https://doi.org/10.1136/bmj.38023.700775.AE). PMID: 14996698.

See also: [[reviewer-archetypes-evidence]], [[common-critiques-taxonomy]], [[ai-peer-review-research]].
