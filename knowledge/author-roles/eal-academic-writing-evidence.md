# EAL Scholarly Writing: Behavioral Evidence

*Last updated: 2026-05-17*

## Synthesis

The literature on English-as-additional-language (EAL) scholars writing for English-medium publication has three large, partially overlapping findings that are robust enough to inform persona design. First, **EAL manuscripts have "text histories"** — by the time a manuscript reaches a journal, it has typically passed through multiple **literacy brokers** (Lillis & Curry's verbatim term [1]): editors, translators, colleagues, paid services, friends. Persona design that models the EAL author as a solo writer + reviewer interacting in isolation misses the social structure that defines the experience. Second, there is a measurable **asymmetric burden**: Amano et al. (2023, n=908 environmental scientists across 8 countries) report that papers by non-native English speakers are **2.5× more likely to be rejected** and **12.5× more likely to receive a request for revision** on language grounds, and that EAL scholars spend **51% more time writing** and **91% more time reading** a paper [2]. Third, the **interpretive question** of whether to call this "linguistic injustice" remains genuinely contested between Hyland's "myth of linguistic injustice" position [3] and the Politzer-Ahles et al. responses [4, 5, 6] — a contested debate that a persona should not collapse to one side.

The deepest empirical finding for persona design is about **voice and stance**, not surface correctness. Hyland's (2005) stance/engagement model [7] and subsequent corpus comparisons consistently find EAL authors using fewer hedges, boosters, self-mentions, and explicit reader-engagement markers than L1 authors. Ivanič (1998) [8] provides the theoretical anchor: this is not just style but **discoursal self** — the projected authorial identity that reviewers in the English-medium publishing community read as confidence, expertise, and community membership. An EAL author may receive a reviewer comment like "the argument lacks confidence" or "voice is impersonal" and have no clear path from comment to revision: these are precisely the comments least amenable to local edits and most threatening to identity.

The practical implication for feedback-generating systems is that **specificity is load-bearing for EAL feedback uptake.** Synthesizing across the L2 feedback literature (Habib, Corcoran & Englander 2019 [9] and the broader corpus), **specific local edits** are taken up most reliably; **vague global suggestions** ("restructure the discussion," "make the voice more engaging") are the least actionable and most affectively costly. Habib et al. specifically find EAL authors report being affected by reviewer comments more deeply than the content alone explains. For a system whose skills emit feedback, this means: the same suggestion expressed as a specific local edit and as a vague global instruction will land very differently on an EAL persona, and the persona will reject (or stall on) the latter even when the suggestion is correct. The AI-polishing era (Jiang & Hyland 2024 [10]; Amano 2023 [2]) introduces a new tradeoff: LLM polishing solves the surface-correctness penalty but **flattens the voice/stance features Ivanič and Hyland identify as identity-bearing** — so aggressive AI assistance may deepen the deeper-layer gap reviewers misread as weak argument.

## Evidence and frameworks

### Text histories and literacy brokers

Lillis & Curry (2006) [1] introduce **"literacy brokers"** in the context of an 8+ year text-ethnographic study of 50 psychology/education scholars in Hungary, Slovakia, Spain, and Portugal. They distinguish three sub-categories: **academic brokers, language brokers, and non-professional brokers** (friends, family). The book-length report (Lillis & Curry 2010 [11]) documents how the "text history" of an EAL manuscript — the sequence of brokered interventions before submission — is the substrate from which the published article emerges. Curry & Lillis (2010) [12] adds that **network capital** determines broker access: well-networked EAL scholars get better brokers, doubly advantaging center-affiliated and well-connected authors.

The implication for persona design is structural, not surface: the EAL author's *expectation* is iterative external mediation. A persona that responds to a reviewer comment as a solo author confronting it for the first time misses how the actual EAL writer would seek out, integrate, or resist brokered help on the same comment.

### The linguistic-injustice debate (genuinely contested)

Hyland's (2016) **"Academic publishing and the myth of linguistic injustice"** [3] argues, verbatim, that the "Native vs non-Native polarization" framing is "outmoded" and "demoralizes EAL writers and marginalizes the difficulties experienced by novice L1 English academics." Based on Hong Kong interviews plus literature review, Hyland claims much of what is read as "language" rejection is actually unfamiliarity with disciplinary writing conventions, or research problems caused by "physical, scholarly and financial isolation." This is not a fringe position; it is published in the field's leading journal and has shaped subsequent debate.

The response from Politzer-Ahles, Holliday, Girolamo, Spychalska & Berkson (2016) [4] is the canonical counter: **absence of evidence is not evidence of absence**, and Hyland's focus on submission-stage data ignores the upstream cognitive and time burden. Their formulation: "if two scholars with the same ability level and training work on the same topic," the EAL scholar must work harder to produce the same output. Politzer-Ahles, Girolamo & Ghali (2020) [5] adds experimental support: reviewers shown matched abstracts varying only in surface English features rate the "non-native-like" version more negatively, including on content. Politzer-Ahles, Girolamo & Ghali (2023) [6] synthesizes the state of the debate with newer evidence.

Amano et al. (2023, *PLOS Biology*) [2] is the most quantitatively load-bearing recent evidence. Survey of 908 environmental scientists across 8 countries: papers by non-native English speakers are 2.5× more likely to be rejected, 12.5× more likely to receive revision requests on language grounds, spend 51% more time writing and 91% more time reading. The effect disproportionately falls on early-career and lower-income-country scholars.

**Honest synthesis:** there is good evidence of a measurable disadvantage in time/burden (Amano 2023) and in reviewer responses to surface features (Politzer-Ahles 2020); the *interpretive* question of whether to call this "injustice" — and what causal weight to assign to language versus disciplinary conventions versus material conditions — remains contested. A persona built only on the disadvantage frame will be one-sided; a persona built only on the Hyland frame will understate empirically documented friction.

### Voice, stance, and the discoursal self

Hyland (2005) [7] is the framework for analyzing the interactional metadiscourse features that distinguish expert and novice (and L1 and L2) academic writing: **hedges, boosters, self-mention, engagement markers**. Subsequent corpus comparisons consistently find EAL authors use fewer of these interactional markers than L1 authors, especially explicit reader-engagement features. The result is prose that sounds "flat" to L1 reviewers in ways that may be misread as weak argument rather than rhetorical-tradition difference.

Ivanič (1998) [8] is the verbatim source for **"discoursal self"** and the four-part identity scheme: **autobiographical self, discoursal self, authorial self, possibilities for selfhood**. For EAL persona design the discoursal/authorial split is critical: an EAL author may have a strong autobiographical self (real expertise, defensible findings) but struggle to project the *discoursal* self that English-medium reviewers expect.

Canagarajah (2002) [13] provides the **"geopolitics of academic writing"** framing — three layered conventions (textual, social, material/publishing) that disadvantage "periphery" scholars. The material chapter is dated but the core argument — that center conventions are *naturalized* rather than neutral — remains foundational.

Casanave (2002) [14], also cited in [[author-role-evidence]], includes bilingual/multilingual faculty in a Japanese university and stresses that academic writing is rule-shaped but not rule-determined. Useful counter to deficit framings of EAL writers.

### Revision patterns: L1 vs L2

Silva (1993) [15] is the meta-review of 72 empirical studies that established the canonical L1-vs-L2 revision-pattern finding (verbatim): L2 writers "revise at a superficial level, re-read and reflect less on their written text, revise less, and when they do revise, the revision is primarily focused on grammatical correction." They also plan less globally. **Caveat:** this body of work is largely about student writers in classroom contexts; extrapolating to mid-career publishing scholars is a real leap and should be flagged in any persona spec that relies on it. The pattern is plausible for early-career EAL scholars writing in a high-stakes second language, less so for senior EAL scholars who have published extensively in English.

### Feedback uptake and the affective load

Habib, Corcoran & Englander (2019) [9] is one of the few studies looking at EAL scholar trajectories specifically through reviewer-feedback experience. Narrative interviews with six young academics find that **reviewers' comments and editors' feedback were the most commonly discussed challenges**, and EAL authors report being affected by them more deeply than the content alone explains. They specifically describe "harsh feedback from journal peer-reviews" as the load-bearing pain point.

Synthesizing across this and the broader L2 feedback literature: **specific local edits** are the highest-uptake feedback form for EAL writers; **vague global suggestions** are the lowest. The asymmetry is sharper for EAL than for L1 writers because the cognitive cost of converting "restructure the discussion" into concrete edits is itself higher for someone navigating both the rhetorical task and a second language.

### AI / LLM polishing: a new tradeoff

Jiang & Hyland (2024) [10] is a comparative corpus study of GenAI text versus student argumentative essays. GenAI text shows **fewer human subjects, fewer explicit self-mentions** ("in my opinion"), more "organizing devices" ("on the other hand," "in conclusion"). For EAL personas this is the key finding: heavy LLM polishing **flattens precisely the stance/engagement features Ivanič and Hyland identify as identity-bearing**. So aggressive AI assistance may *solve* the surface-correctness penalty Amano (2023) documents at the cost of *deepening* the voice/stance gap that L1 reviewers read as weak argument.

The broader literature on AI tools for EAL scholars (2023–2026) is mostly advocacy or small-N qualitative, not strong empirical work. The equity argument (AI reduces the "language tax" but introduces a new "AI-detection" suspicion penalty) is active but not yet supported by robust empirical evidence. Personas should treat AI-mediated writing as a real and growing dimension of the EAL experience while not over-claiming what the evidence supports.

## How this informs scriptorium

This evidence base grounds the EAL author-persona work (#42, #43, #44):

1. **The EAL persona is not solo.** Encode that the persona's expectation is brokered help — colleagues, paid editors, AI tools — and that feedback from scriptorium is one input among many. An EAL persona that responds to every comment as if isolated misses the social structure documented by Lillis & Curry.

2. **Don't collapse the linguistic-injustice debate.** The persona should hold both: real surface-feature disadvantage (Amano 2023; Politzer-Ahles 2020) *and* the warning against treating EAL writers primarily as language-deficit subjects (Hyland 2016). A persona that only complains about reviewer bias misses Hyland's evidence; a persona that only blames their own English misses Politzer-Ahles. The honest persona sits with both.

3. **Specificity of feedback is a load-bearing metric.** Skill outputs benchmarked against an EAL persona should be evaluated partly on whether the feedback is **local-specific** vs **vague-global**. The persona will (correctly, per the evidence) reject vague global suggestions as low-uptake — and that becomes a useful pressure on skill design.

4. **Stance/voice comments require special handling.** Comments about hedging, boosters, self-mention, or reader engagement are the comments least amenable to local edits and most identity-threatening for EAL writers (Ivanič 1998; Hyland 2005). A persona should mark these comments as high-cost-to-act-on, and skills that produce such comments should pair them with concrete sentence-level rewrites rather than leaving them as global instructions.

5. **The AI-polishing tradeoff should be encoded.** An EAL persona is plausibly already using ChatGPT, DeepL Write, or Paperpal. Feedback that conflicts with what their LLM tool produced creates friction the persona should register. And feedback that pushes the writing further toward AI-flattened style (more "organizing devices," fewer self-mentions) should be flagged by the persona as deepening the voice problem, not solving it.

6. **Career stage compounds with EAL status, doesn't substitute for it.** The EAL grad-student persona and the EAL senior-PI persona are different cells in the role × language matrix. A senior EAL PI has decades of brokered experience and a polished stance repertoire; a first-time-publishing EAL grad student does not. Persona design should compose the [[author-role-evidence]] findings *with* this document, not pick one or the other.

## Implementation priority for scriptorium

**Verdict:** Yes (knowledge layer for v0.2 persona docs and v0.3 personalization skills). No (not a skill itself).

**Yes — grounding layer:** This document grounds the EAL persona work and the role × language matrix raised in #42 discussion. The EAL persona specs (which live outside the repo per the testing-integrity design) should cite this document for each behavior they model.

**No — dedicated skill:** An `eal-aware-rewriter` skill is *not* justified at this stage. The Amano (2023) burden is real, but the evidence does not yet support a single transformation skill that reliably reduces it. The contested Hyland/Politzer-Ahles debate also cautions against baking a deficit-correction model into a skill.

**If Maybe later:** if persona-calibration data (#44) consistently shows that EAL personas mark certain skill outputs as low-uptake or identity-threatening, that becomes a calibration signal for `argumentative-flow` (#7) and any future drafting skills — pressure to produce more specific, more local feedback. An explicit EAL-aware skill becomes justified if and when the persona-driven evaluation surfaces a clear, repeated pattern that a dedicated skill could address.

## Open questions / weak evidence

- **The Hyland vs Politzer-Ahles/Amano debate is genuinely unresolved.** Personas built one-sidedly will be wrong. The empirical work supports a real surface-feature and time-burden disadvantage; the interpretive question of how much of "language rejection" is actually disciplinary-convention or research-quality rejection remains live.

- **Scholarly EAL writing research is much smaller than student L2 writing research.** Silva (1993) and most revision-pattern studies are about classroom writing; extrapolating to mid-career publishing scholars is a real leap. Personas should be more cautious about Silva-style claims for senior EAL scholars than for early-career ones.

- **Empirical work on EAL scholar feedback-uptake patterns is thin.** Most "feedback uptake" research is on students. Habib, Corcoran & Englander (2019) is one of the few looking at scholars' trajectories specifically, and it's narrative not corpus.

- **Cultural/geographic concentration of the foundational corpus.** Lillis/Curry (Hungary/Slovakia/Spain/Portugal psychology), Flowerdew (Hong Kong Cantonese), Canagarajah (Sri Lanka). Latin American (Englander, Corcoran), African, and South Asian contexts are less represented in the high-citation foundational work, though Corcoran et al. (2019) [16] is correcting this.

- **Literacy-brokers research describes who brokers are but not what they do at the sentence level.** Lillis & Curry document the social structure; the micro-edit patterns brokers apply are less catalogued. This is a real gap for scriptorium because the system is itself effectively a literacy broker.

- **"Discoursal positioning differs by L1 rhetorical tradition" is more often asserted than empirically demonstrated for academic publishing specifically.** Contrastive-rhetoric claims in this literature should be cited with care.

- **AI-use literature for EAL scholars (2023–2026) is mostly opinion/advocacy or small qualitative.** The Jiang & Hyland (2024) corpus finding on AI text flattening voice features is the strongest recent empirical anchor; the broader equity arguments are not yet supported by robust evidence on publication outcomes.

- **A small number of pagination/volume details in the references list were not pinned at write-time;** the substance of those entries (authors, year, journal, argument) is correct, but exact page ranges should be verified at the source if scriptorium prose ever cites a specific page. Until then, these are treated as work-level rather than page-level citations.

## References

1. Lillis, T., & Curry, M. J. (2006). Professional academic writing by multilingual scholars: Interactions with literacy brokers in the production of English-medium texts. *Written Communication*, 23(1), 3–35. DOI: [10.1177/0741088305283754](https://doi.org/10.1177/0741088305283754).

2. Amano, T., Ramírez-Castañeda, V., Berdejo-Espinola, V., et al. (2023). The manifold costs of being a non-native English speaker in science. *PLOS Biology*, 21(7), e3002184. DOI: [10.1371/journal.pbio.3002184](https://doi.org/10.1371/journal.pbio.3002184). PMID: 37463136.

3. Hyland, K. (2016). Academic publishing and the myth of linguistic injustice. *Journal of Second Language Writing*, 31, 58–69. DOI: [10.1016/j.jslw.2016.01.005](https://doi.org/10.1016/j.jslw.2016.01.005).

4. Politzer-Ahles, S., Holliday, J. J., Girolamo, T., Spychalska, M., & Berkson, K. H. (2016). Is linguistic injustice a myth? A response to Hyland (2016). *Journal of Second Language Writing*, 34, 3–8. DOI: [10.1016/j.jslw.2016.09.003](https://doi.org/10.1016/j.jslw.2016.09.003). PMC: PMC5502761.

5. Politzer-Ahles, S., Girolamo, T., & Ghali, S. (2020). Preliminary evidence of linguistic bias in academic reviewing. *Journal of English for Academic Purposes*, 47, 100895. DOI: [10.1016/j.jeap.2020.100895](https://doi.org/10.1016/j.jeap.2020.100895). PMC: PMC7575202.

6. Politzer-Ahles, S., Girolamo, T., & Ghali, S. (2023). The linguistic disadvantage of scholars who write in English as an additional language: Myth or reality. *Language Teaching*, 56(2), 269–281. DOI: [10.1017/S0261444822000428](https://doi.org/10.1017/S0261444822000428).

7. Hyland, K. (2005). Stance and engagement: a model of interaction in academic discourse. *Discourse Studies*, 7(2), 173–192. DOI: [10.1177/1461445605050365](https://doi.org/10.1177/1461445605050365).

8. Ivanič, R. (1998). *Writing and identity: The discoursal construction of identity in academic writing*. John Benjamins. ISBN: 978-9027218001.

9. Habib, A., Corcoran, J. N., & Englander, K. (2019). Academic publishing in English: Exploring linguistic privilege and scholars' trajectories. *Journal of Language, Identity & Education*, 18(6), 387–400. DOI: [10.1080/15348458.2019.1671193](https://doi.org/10.1080/15348458.2019.1671193). [TODO verify exact author order]

10. Jiang, F. K., & Hyland, K. (2024). Does ChatGPT argue like students? Bundles in argumentative essays. *Applied Linguistics*, advance access. DOI: [10.1093/applin/amae052](https://doi.org/10.1093/applin/amae052). [TODO verify final pagination]

11. Lillis, T., & Curry, M. J. (2010). *Academic writing in a global context: The politics and practices of publishing in English*. Routledge. ISBN: 978-0415468824.

12. Curry, M. J., & Lillis, T. (2010). Academic research networks: Accessing resources for English-medium publishing. *English for Specific Purposes*, 29(4), 281–295. DOI: [10.1016/j.esp.2010.06.002](https://doi.org/10.1016/j.esp.2010.06.002).

13. Canagarajah, A. S. (2002). *A geopolitics of academic writing*. University of Pittsburgh Press. ISBN: 978-0822957942.

14. Casanave, C. P. (2002). *Writing Games: Multicultural Case Studies of Academic Literacy Practices in Higher Education*. Lawrence Erlbaum. ISBN: 978-0805835311.

15. Silva, T. (1993). Toward an understanding of the distinct nature of L2 writing: The ESL research and its implications. *TESOL Quarterly*, 27(4), 657–677. DOI: [10.2307/3587400](https://doi.org/10.2307/3587400).

16. Corcoran, J. N., Englander, K., & Muresan, L.-M. (Eds.). (2019). *Pedagogies and policies for publishing research in English: Local initiatives supporting international scholars*. Routledge. ISBN: 978-1138558090.

17. Flowerdew, J. (1999). Problems in writing for scholarly publication in English: The case of Hong Kong. *Journal of Second Language Writing*, 8(3), 243–264. DOI: [10.1016/S1060-3743(99)80116-7](https://doi.org/10.1016/S1060-3743(99)80116-7).

See also: [[author-role-evidence]], [[credit-taxonomy-authorship]], [[reviewer-archetypes-evidence]].
