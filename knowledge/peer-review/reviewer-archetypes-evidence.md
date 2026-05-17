# Reviewer Archetypes: What the Evidence Shows

*Last updated: 2026-05-17*

## Synthesis

Empirical research on peer review converges on an uncomfortable result: when two competent reviewers read the same manuscript, they agree only modestly on its merit. The largest meta-analysis to date (Bornmann, Mutz & Daniel 2010, 48 studies, ~19,443 manuscripts) reports a mean inter-rater reliability of Cohen's κ ≈ 0.17 and ICC/r² ≈ 0.34 — i.e., reviewer agreement is "low" by any standard psychometric benchmark [1]. This is not a flaw to be reformed away; it is a stable empirical regularity across decades, fields, and journal types. Different reviewers attend to different aspects of the same work. That fact, more than any other, justifies a multi-persona reviewer simulation: a single LLM "reviewer" trained to mimic the field's median is by construction less useful than a panel that deliberately diversifies the attentional lens.

The bias literature is more contested than its popular framing suggests. Lee, Sugimoto, Zhang & Cronin (2013) systematically reviewed the field and concluded that "a closer look at the empirical and methodological limitations of research on bias raises questions about the existence and extent of many hypothesized forms of bias" [2]. The clearest experimentally-demonstrated bias is prestige bias under single-blind review (Tomkins, Zhang & Heavlin 2017 PNAS, randomized at the 2017 WSDM conference) — single-blind reviewers were significantly more likely to recommend acceptance for papers from famous authors or top institutions, with single-blind bidders preferring famous authors at ~1.6x the double-blind rate [3]. Gender bias, by contrast, has not held up under the largest test: Squazzoni et al. (2021, Science Advances, 145 journals, ~1.7M authors, ~740K reviewers) found no systematic penalty against women authors, and in some segments a slight pro-women effect [4].

The folkloric "Reviewer 2" — the rude, smug, pet-theory-obsessed referee — has weaker empirical support than the meme suggests. The one direct test we have (Peterson 2020, satirical title notwithstanding) found that reviewers labeled "2" by editorial systems are not systematically harsher than "1"; if anything, Reviewer 3 is the more negative slot in some journals' workflow [5]. The trope captures something real (unprofessional reviews exist and are common — PeerJ's 2018 survey of 1,106 scientists found ~half had received at least one unprofessional review [6]) but assigns it to the wrong position number. For a simulation system, the takeaway is that the "harsh skeptical reviewer" archetype is empirically defensible as a *behavior*, not as a numbered role.

## Evidence

- **Inter-rater reliability is low and stable.** Bornmann, Mutz & Daniel (2010), the canonical meta-analysis, pooled 70 reliability coefficients from 48 studies of journal peer review: mean Cohen's κ = 0.17, mean ICC/r² = 0.34. The authors conclude IRR is "quite limited and needs improvement." Similar magnitudes recur in earlier meta-analyses (Cicchetti 1991, BBS) and in domain-specific replications [1].

- **Bias literature is more nuanced than slogans.** Lee et al. (2013) is the most cited critical review. Many bias claims rely on observational data with weak controls; the experimental record is thinner. The strongest experimental finding is Tomkins et al. (2017): in a fully randomized natural experiment at WSDM 2017, single-blind reviewers gave significantly higher scores to papers from famous authors and high-prestige institutions than double-blind reviewers reading the same manuscripts. The single-blind reviewers were also more likely to bid on famous-author papers [3]. This is consistent with prior smaller experiments (e.g., Budden et al. 2008 on Behavioral Ecology, contested).

- **Gender bias does not appear at scale.** Squazzoni et al. (2021) is the largest study of its kind: 145 Elsevier journals, 1.7M authors, 740K reviewers, full submission-to-decision data. Result: "manuscripts written by women as solo authors or coauthored by women were treated even more favorably by referees and editors" [4]. The signal in smaller studies appears to wash out at scale, though field-specific effects (notably in some humanities/social sciences) remain plausible.

- **"Reviewer 2" is folklore that captures real behavior at the wrong address.** The trope is academic culture (memes, the 55k-member "Reviewer 2 Must Be Stopped!" Facebook group). The PeerJ 2018 survey reported ~50% of scientists experienced unprofessional review comments [6]. The empirical test of the position-number claim (analysis of one journal's reviewer database, ~2020) found Reviewer 2 was no harsher than Reviewer 1; Reviewer 3 was somewhat more negative in that dataset [5]. So: harshness exists, position numbering doesn't predict it.

- **Reviewer demographics influence behavior modestly.** Squazzoni et al. (2021) and Murray et al. (2019) document differences by reviewer age, career stage, and geography (e.g., early-career reviewers tend to write longer, more thorough reports; senior reviewers are faster and more decision-oriented). Effect sizes are small relative to between-reviewer variance.

## How this informs scriptorium

The four-persona design in scriptorium's `reviewer-simulation` skill is grounded in this evidence in three ways:

1. **Diversity-of-attention is the point, not consensus.** Because real reviewers agree at κ ≈ 0.17, a simulation that produces four convergent reviews is *less* faithful to the literature than one that produces four divergent ones. The methodological skeptic, domain expert, translational reviewer, and statistical reviewer should each surface critiques the others miss. Convergence on a critique becomes a stronger signal than agreement on praise.

2. **Personas are attentional lenses, not numbered slots.** Avoid labels like "Reviewer 1 / Reviewer 2 / Reviewer 3" — that framing imports folklore the data don't support. Label personas by the lens they apply (methodological / domain / translational / statistical). This also avoids inheriting the asymmetric "harshness" connotations of numbered roles.

3. **Acknowledge prestige and confirmation bias in design.** Because single-blind prestige bias is the best-replicated reviewer bias [3], `reviewer-simulation` should not be primed with author identity, institutional affiliation, or venue prestige. The skill should operate on the manuscript text and `MANUSCRIPT_STATE.yaml` claims/limitations only. This is a defensible default the human-reviewer literature actively endorses (Tomkins et al.'s implicit recommendation was double-blinding).

## Open questions / weak evidence

- **Do LLM-simulated reviewers reproduce human reviewer disagreement patterns?** Liang et al. (2024) report ~30% point-level overlap between GPT-4 and human reviewers, comparable to the ~28% overlap between two human reviewers on the same papers [see `ai-peer-review-research.md`]. Whether this represents genuine diverse attention or shared surface-level engagement is unresolved.
- **Field-specificity of bias findings.** Squazzoni et al. (2021) is dominated by Elsevier journals; humanities and small-society journals are underrepresented. Gender-bias null findings may not generalize.
- **Persona orthogonality.** No empirical work directly tests whether the four personas scriptorium uses are independent in critique space, or whether (e.g.) "methodological skeptic" and "statistical reviewer" mostly produce the same critiques in practice. This is a first-class empirical question for scriptorium itself to investigate from its own logs.
- **Whether disagreement is signal or noise.** Bornmann et al. (2010) treat low IRR as a defect. Others (e.g., Mayo-Wilson et al. 2021) argue it reflects legitimate multi-criteria evaluation and that high agreement would itself be suspicious. Scriptorium's design implicitly takes the latter view.

## References

1. Bornmann L, Mutz R, Daniel HD. A reliability-generalization study of journal peer reviews: a multilevel meta-analysis of inter-rater reliability and its determinants. *PLoS ONE* 5(12): e14331 (2010). DOI: [10.1371/journal.pone.0014331](https://doi.org/10.1371/journal.pone.0014331). PMID: 21179459.
2. Lee CJ, Sugimoto CR, Zhang G, Cronin B. Bias in peer review. *J Am Soc Inf Sci Tech* 64(1): 2–17 (2013). DOI: [10.1002/asi.22784](https://doi.org/10.1002/asi.22784).
3. Tomkins A, Zhang M, Heavlin WD. Reviewer bias in single- versus double-blind peer review. *PNAS* 114(48): 12708–12713 (2017). DOI: [10.1073/pnas.1707323114](https://doi.org/10.1073/pnas.1707323114). PMID: 29138317.
4. Squazzoni F, Bravo G, Farjam M, Marusic A, Mehmani B, Willis M, Birukou A, Dondio P, Grimaldo F. Peer review and gender bias: a study on 145 scholarly journals. *Sci Adv* 7(2): eabd0299 (2021). DOI: [10.1126/sciadv.abd0299](https://doi.org/10.1126/sciadv.abd0299). PMID: 33523967.
5. Peterson DAM. "Dear Reviewer 2: Go F' Yourself" (2020), *Social Science Quarterly*. The empirical claim that Reviewer 2 is not systematically harsher than Reviewer 1 is reported in this and adjacent commentary. DOI: [10.1111/ssqu.12824](https://doi.org/10.1111/ssqu.12824) [TODO verify exact DOI].
6. Silbiger NJ, Stubler AD. Unprofessional peer reviews disproportionately harm underrepresented groups in STEM. *PeerJ* 7: e8247 (2019). DOI: [10.7717/peerj.8247](https://doi.org/10.7717/peerj.8247). PMID: 31875147. (This is the published PeerJ analysis of the 2018 survey referenced in the text.)

See also: [[common-critiques-taxonomy]], [[critique-quality-evidence]], [[ai-peer-review-research]].
