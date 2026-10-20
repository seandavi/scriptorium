# Reporting guidelines (EQUATOR Network)

*Last updated: 2026-10-20*

## Synthesis

Reporting guidelines are checklists that specify, study design by study
design, what information a paper *must* report to be evaluable. They are not
style advice; they are minimum-information standards, analogous to MIAME for
microarrays or DICOM for imaging. The EQUATOR Network
(equator-network.org), an international consortium founded in 2008, maintains
the canonical registry. Its online library listed roughly 700 records
across study designs and reporting domains when checked on 2026-10-20 [10].
(That figure is a count of the library listing, not a number EQUATOR
publishes.)

For a scriptorium-style writing system, reporting guidelines are the
**validation contract**. Where narrative frameworks ([[narrative-frameworks]])
tell you whether a paper is *readable*, reporting guidelines tell you whether
it is *evaluable*. A trial paper that omits randomization details is not
recoverable by good prose. Several scriptorium skills planned for v0.3 — in
particular `statistics-consistency`, `sample-size-validation`, and a future
`reporting-guideline-compliance` skill — are grounded directly in these checklists.

The major reporting guidelines have been published with explanation-and-
elaboration companion documents that work as worked examples and are useful
as the substrate for LLM-driven compliance checks. Adoption by journals is
mixed: high-impact medical journals largely require CONSORT, PRISMA, and
STROBE in their author guidelines; specialty and methods journals are
patchier; AI-specific extensions are very new and not yet uniformly
required.

Two 2025–2026 developments matter most here. First, the two core trial
guidelines were revised: **CONSORT 2025** [11] replaces CONSORT 2010 and
renumbers the checklist, and **SPIRIT 2025** [12] does the same for trial
protocols. Any tool that cites CONSORT item numbers must therefore name
the version. Second, there is now direct validation evidence for
LLM-assisted adherence assessment. Zero-shot or lightly prompted LLMs
reach about 90% agreement with expert raters when assessing trial
reporting against CONSORT- and SPIRIT-based items [20, 21, 22].
AutoReporter, the only one of these studies to report chance-corrected
agreement, gives Cohen's κ of 0.70–0.77 [22]. On the 93-item TRIPOD
checklist the best models reach F1 ≈ 0.73–0.74 [23]. The authors
recommend these tools for semi-automated use with human checking, not
full automation.

## Evidence and frameworks

### CONSORT 2010 and CONSORT 2025 — randomized controlled trials

Schulz KF, Altman DG, Moher D (for the CONSORT Group). CONSORT 2010
Statement: updated guidelines for reporting parallel group randomised
trials. *BMJ*. 2010;340:c332. DOI: 10.1136/bmj.c332. [1]

CONSORT is a 25-item checklist plus a participant flow diagram. The check
covers trial design, randomization details, blinding, sample size
justification, primary and secondary outcomes, statistical methods, harms,
and limitations. It is required (or "strongly encouraged") by most major
clinical journals and by ICMJE-member journals.

The extensions are now numerous: cluster trials, non-inferiority/equivalence
trials, pragmatic trials, herbal interventions, and — most relevant for
modern manuscripts — CONSORT-AI (see below).

Hopewell S, Chan A-W, Collins GS, Hróbjartsson A, *et al.* CONSORT 2025
statement: updated guideline for reporting randomised trials. *BMJ*.
2025;389:e081123. DOI: 10.1136/bmj-2024-081123. [11]

CONSORT 2025 (published 14 April 2025, simultaneously in several journals)
is a **30-item checklist** plus a flow diagram. The developers "added seven
new checklist items, revised three items, deleted one item, and integrated
several items from key CONSORT extensions", and restructured the checklist
around a new **Open science** section [11]. That section covers trial
registration (item 2), access to the protocol and statistical analysis plan
(item 3), data sharing (item 4), and funding and conflicts of interest
(items 5a–b). Patient and public involvement is a new item (8). Harms items
from the CONSORT Harms extension are integrated (items 7, 15, 21a, 23a, 27).

**Item numbers shifted.** Sample-size determination was item 7a in
CONSORT 2010 and is **16a** in CONSORT 2025. Statistical methods were item
12 and are now **21a–d**, with missing-data handling (21c) as its own
sub-item. Sequence generation is **17a–b**. A tool that cites "CONSORT 7a"
or "CONSORT 17b" without naming the version will point at the wrong item.
A companion explanation-and-elaboration paper was published alongside the
statement (*BMJ* 2025;389:e081124).

### SPIRIT 2025 — trial protocols

Chan A-W, Boutron I, Hopewell S, Moher D, *et al.* SPIRIT 2025 statement:
updated guideline for protocols of randomised trials. *BMJ*.
2025;389:e081477. DOI: 10.1136/bmj-2024-081477. [12]

SPIRIT 2025 is a **34-item** minimum checklist for trial protocols plus a
schedule-of-enrolment diagram. The update added two new items, revised five,
and deleted or merged five. It also introduced a new open-science section,
put more emphasis on harms and on describing interventions and comparators,
and added a new patient-and-public-involvement item [12]. It is the
protocol-stage counterpart to CONSORT 2025. A manuscript that is a trial
protocol should be audited against SPIRIT 2025, not CONSORT.

### STROBE — observational studies

von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP (for
the STROBE Initiative). The Strengthening the Reporting of Observational
Studies in Epidemiology (STROBE) Statement: guidelines for reporting
observational studies. *PLoS Med*. 2007;4(10):e296. DOI:
10.1371/journal.pmed.0040296. [2]

A 22-item checklist for cohort, case-control, and cross-sectional studies
(18 items common; 4 design-specific). STROBE is the de facto standard for
epidemiological reporting and the foundation for several extensions
(STROBE-ME for molecular epidemiology, RECORD for routinely collected
health data, STROBE-Vet for veterinary studies).

### PRISMA 2020 — systematic reviews

Page MJ, McKenzie JE, Bossuyt PM, *et al.* The PRISMA 2020 statement: an
updated guideline for reporting systematic reviews. *BMJ*. 2021;372:n71.
DOI: 10.1136/bmj.n71. [3]

PRISMA 2020 replaced the 2009 statement (Moher et al., DOI:
10.1136/bmj.b2535). The 27-item checklist (with an expanded abstract
checklist and revised flow diagrams) addresses search strategy, study
selection, risk-of-bias assessment, certainty assessment, and synthesis
methods. PRISMA extensions exist for network meta-analyses, scoping reviews,
diagnostic test accuracy reviews, and individual participant data.

As of October 2026, PRISMA 2020 is still the current version. The official
PRISMA site lists two AI-related items as *under development*: a PRISMA
extension for systematic reviews of AI interventions, and a "partial update
of PRISMA 2020 to incorporate guidance on use of AI tools in the systematic
review process" [19]. It also lists updates of the network-meta-analysis,
scoping-review and protocol extensions as under development. No full
PRISMA successor has been published.

### ARRIVE 2.0 — animal research

Percie du Sert N, Hurst V, Ahluwalia A, *et al.* The ARRIVE guidelines 2.0:
Updated guidelines for reporting animal research. *PLoS Biol*. 2020;
18(7):e3000410. DOI: 10.1371/journal.pbio.3000410. [4]

ARRIVE 2.0 reorganized the 2010 original into two priority tiers: the
"Essential 10" (the absolute minimum, including study design, sample size,
inclusion/exclusion criteria, randomization, blinding, outcome measures,
statistical methods, experimental animals, experimental procedures, and
results) and a Recommended Set covering ethics, housing, contextual detail.

### STARD 2015 — diagnostic accuracy

Bossuyt PM, Reitsma JB, Bruns DE, *et al.* STARD 2015: an updated list of
essential items for reporting diagnostic accuracy studies. *BMJ*.
2015;351:h5527. DOI: 10.1136/bmj.h5527. [5]

A 30-item checklist for studies estimating the accuracy of a diagnostic
test against a reference standard. Co-published in *BMJ*, *Radiology*, and
*Clinical Chemistry* in October 2015. A STARD-AI extension was published in
2025 (Sounderajah V, *et al. Nat Med*. 2025;31(10):3283–3289; DOI:
10.1038/s41591-025-03953-8) [13] to address artificial-intelligence-based
diagnostic tools.

### TRIPOD and TRIPOD+AI — prediction models

Collins GS, Reitsma JB, Altman DG, Moons KGM. Transparent Reporting of a
multivariable prediction model for Individual Prognosis Or Diagnosis
(TRIPOD): the TRIPOD Statement. *BMJ*. 2015;350:g7594. DOI:
10.1136/bmj.g7594. [6]

TRIPOD covers the development, validation, or update of multivariable
prediction models. The 22-item checklist addresses outcomes, predictors,
sample size, missing data, model specification, performance, and
external validation.

Collins GS, Moons KGM, Dhiman P, *et al.* TRIPOD+AI statement: updated
guidance for reporting clinical prediction models that use regression or
machine learning methods. *BMJ*. 2024;385:e078378. DOI:
10.1136/bmj-2023-078378. [7]
(The earlier citation here, *BMJ* 2024;385:q824, is the accompanying
editorial by Cohen and Bossuyt, not the statement itself.)

TRIPOD+AI expanded the checklist to 27 items and unified reporting for
regression-based and ML-based models. It places new emphasis on
trustworthiness, fairness, and reproducibility — including reporting of
training/validation/test splits, hyperparameter selection, and fairness
across demographic subgroups.

### Generative-AI and LLM reporting guidelines (2025–2026)

LLM-specific guidance has arrived quickly since 2025:

- **TRIPOD-LLM** [14]: an extension of TRIPOD+AI for studies that develop,
  tune, prompt-engineer, or evaluate LLMs in biomedicine. It has 19 main
  items and 50 subitems. The format is modular, with 14 main items
  applicable across all study categories, and the authors describe it as a
  "living document".
- **REFINE** [15]: a 44-item, six-section checklist for foundation-model
  and LLM studies in medical research, including imaging AI. It was
  published ahead of print in February 2026.
- **CHART** [16]: the Chatbot Assessment Reporting Tool, for studies that
  evaluate generative-AI chatbots giving health advice. It was published in
  2025, jointly across several journals, with an explanation-and-elaboration
  paper in *BMJ*.
- **A reporting checklist for LLMs in behavioural science** [17]
  (*Nat Hum Behav*, 2026). This is the first such checklist outside
  biomedicine in this set.
- **GAMER** [18] is different from the others. It is not a study-design
  guideline but a nine-item checklist for disclosing how generative-AI
  tools were *used* in producing medical research. Its items cover a
  general declaration, tool specifications, prompting techniques, the
  tool's role, any new models developed, AI-assisted manuscript sections,
  content verification, data privacy, and impact on conclusions.

GAMER is directly relevant to scriptorium users. An author who used
scriptorium skills while drafting is the kind of author GAMER asks to
disclose.

### Evidence on LLM-assisted adherence assessment (2025–2026)

Four validation studies now bear directly on any skill that walks a
checklist with an LLM:

- **Wrightson et al. 2025** [20]: 113 sports-medicine trial reports, nine
  reporting questions. GPT-4 Turbo reached accuracy 90% (F1 0.89). Llama 2
  70B started at 64% and reached 83% after fine-tuning. GPT-4 Vision
  identified every participant-flow diagram but was only 57% accurate at
  detecting *missing details* in them.
- **Srinivasan et al. 2025** [21]: a zero-shot GPT-4o-mini pipeline matched
  experts on 91.7% of 2,210 item decisions (macro-F1 0.86 on the CONSORT-TM
  benchmark). Applied to 21,041 open-access RCTs, it found mean CONSORT
  compliance rising from 27.3% (1966–1990) to 57.0% (2010–2024). Critical
  items stayed rare: allocation concealment was reported in 16.1% of trials
  and external validity was discussed in 1.6%.
- **Chen et al. 2026, AutoReporter** [22]: a zero-shot, no-retrieval o3-mini
  prompt reached 90.1% accuracy on CONSORT (κ = 0.70) and 92.1% on SPIRIT
  (κ = 0.77). It matched or exceeded fine-tuned domain models without
  annotated training data.
- **Spiero et al. 2026** [23]: five LLMs scored the 93 TRIPOD items for 70
  manually scored prediction-model papers. Gemini-2.5-pro (F1 0.74) and
  GPT-5 (F1 0.73) performed best. Gemini-2.5-pro's supporting quotes were
  correct in 80–97% of cases. The authors conclude these models suit
  "semiautomated" rather than fully automated use.

*Interpretation (researcher inference).* These studies support the
`present / partial / missing / not-applicable` design with quoted anchors.
Agreement around 90%, with κ of 0.70–0.77 where it was reported [22], is
useful, but it means
roughly one item decision in ten will be wrong. Requiring a verbatim
quote per `present` row is the check that lets an author catch those
errors. All four studies evaluate *published* papers against established
checklists. None evaluates pre-submission drafts or the 2025 checklists.

### CONSORT-AI and SPIRIT-AI — AI-enabled trials

Liu X, Cruz Rivera S, Moher D, Calvert MJ, Denniston AK; SPIRIT-AI and
CONSORT-AI Working Group. Reporting guidelines for clinical trial reports
for interventions involving artificial intelligence: the CONSORT-AI
extension. *Nat Med*. 2020;26:1364–1374. DOI: 10.1038/s41591-020-1034-x. [8]

Cruz Rivera S, Liu X, Chan A-W, *et al.* Guidelines for clinical trial
protocols for interventions involving artificial intelligence: the
SPIRIT-AI extension. *Nat Med*. 2020;26:1351–1363. DOI:
10.1038/s41591-020-1037-7. [9]

These were the first international standards for trial reporting and
protocols of AI-based interventions. SPIRIT-AI covers protocols (before the
trial); CONSORT-AI covers final trial reports. Both add items for AI
intervention description, input data handling, error analysis, and
human/AI interaction.

CONSORT-AI and SPIRIT-AI were built on the 2010 and 2013 base checklists.
CONSORT 2025 and SPIRIT 2025 do not fold in AI-specific items [11, 12].
SPIRIT 2025 addresses the gap directly. Its developers say they will work
with extension leaders to align the extensions with SPIRIT 2025, and "In
the meantime, we recommend that the existing version of the relevant
SPIRIT extensions be used" [12]. SPIRIT-AI is among the extensions it
cites. An AI-intervention trial therefore needs both the 2025 base
checklist and the 2020 AI extension, with the version mismatch stated.
*(Researcher inference: applying the same approach to CONSORT-AI is by
analogy, and we found no published CONSORT-AI or SPIRIT-AI update as of
2026-10-20.)*

### Beyond these: the EQUATOR Network

The EQUATOR Network maintains the registry at equator-network.org. Other
relevant guidelines include:

- **CARE** — case reports (DOI: 10.7453/gahmj.2013.008)
- **SRQR** / **COREQ** — qualitative research synthesis and reporting
- **AGREE II** — practice guidelines
- **REMARK** — tumor marker studies
- **CHEERS 2022** — health economic evaluations (DOI: 10.1136/bmj-2021-067975)

For any given manuscript, the EQUATOR search tool returns the applicable
guidelines by study design. A scriptorium skill that auto-detects design
type from manuscript content could route to the right checklist
automatically; this is a candidate v0.3 capability.

## How this informs scriptorium

Reporting guidelines are the cleanest validation substrate available
because they are *enumerable*. Each guideline ships as a numbered checklist,
and each checklist item has a canonical answer pattern. This is ideal
ground for structured-output skills.

Direct connections:

- **`statistics-consistency`** (planned, v0.3). Should ground its checks in
  the statistics items of the relevant guideline: CONSORT 2010 items 7a and
  12, which are CONSORT 2025 items 16a and 21a–d; STROBE item 12; TRIPOD
  items 8 and 9. Inconsistencies between methods and results in *those
  specific items* are higher-severity than free-text arithmetic mismatches.
  See [[statistical-inconsistency]] for the deterministic-recomputation
  discipline.
- **`sample-size-validation`** (planned). Should detect whether sample-size
  justification is present and whether it names the assumed effect size,
  power, and alpha. The relevant items are CONSORT 2010 7a / CONSORT 2025
  16a, ARRIVE Essential 10 item 2, and STROBE item 10. The skill should not
  invent these values; it should only flag their absence.
- **`reporting-guideline-compliance`** (v0.3). A direct mapping from
  manuscript sections to checklist items. Output: per-item status (present /
  partial / missing / not-applicable) with a span pointer for each
  "present" claim. This is a critique skill, not transformative. Since
  April 2025 the default trial checklist should be **CONSORT 2025**, with
  CONSORT 2010 offered only when the author or venue requires it. Trial
  protocols should be audited against **SPIRIT 2025**. Item numbers must
  always carry the checklist version. The 2025–2026 validation studies
  [20–23] support checklist walking by LLM, but with an error rate of
  roughly one item in ten. Quoted anchors are therefore essential, not
  optional. Checks on figure-borne items, such as completeness of the flow
  diagram, are weaker still and should default to `partial` with a request
  to verify [20].
- **`reporting-guideline-fit`** (v0.2). The routing step should know the
  2025–2026 additions. Route trial protocols to SPIRIT 2025, trial reports
  to CONSORT 2025 (plus CONSORT-AI for AI interventions), LLM-evaluation
  studies to TRIPOD-LLM or REFINE, and chatbot health-advice studies to
  CHART. GAMER is an *additional* disclosure checklist that applies
  whenever generative AI was used in the research. It does not replace the
  design checklist.
- **`journal-style-conversion`** (planned). Reporting guidelines are part
  of journal style. A conversion skill should know which guideline each
  target journal requires and check that the manuscript complies before
  reformatting citations or section titles.
- **`reviewer-simulation`** (current). The simulator should consult the
  applicable guideline as a baseline of reviewer concerns — many real
  reviewer comments are paraphrases of checklist items the manuscript
  didn't satisfy. Srinivasan et al. [21] suggest where to start: allocation
  concealment and external-validity discussion are the most chronically
  under-reported CONSORT items.

A practical design note: the manuscript-state schema should be able to
record which reporting guideline(s) apply, so skills don't have to
re-detect. Adding an optional `reporting_guidelines: [CONSORT-AI, TRIPOD+AI]`
field to `MANUSCRIPT_STATE.yaml` would let any skill consume the answer.
Entries should carry a version, for example `CONSORT 2025` rather than
`CONSORT`.

## Implementation priority for scriptorium

**Verdict:** Yes. The current skills are `reporting-guideline-fit` (v0.2)
and `reporting-guideline-compliance` (v0.3), and `reviewer-simulation`
consumes the guideline as a baseline.

**If Yes:**

- *`reporting-guideline-compliance`*: update the default trial checklist
  from CONSORT 2010 to CONSORT 2025, and add SPIRIT 2025 for protocols.
  Version-qualify every item number. Keep quoted anchors mandatory, which
  the LLM-adherence evidence [20–23] now directly supports.
- *`reporting-guideline-fit`*: add routing for SPIRIT 2025, TRIPOD-LLM,
  REFINE and CHART. Surface GAMER as an add-on disclosure checklist when
  generative-AI use is declared.
- *Required data*: the checklist text for each named version. The CONSORT
  2025 and SPIRIT 2025 checklists are published open access [11, 12].
- *Not yet*: automated flow-diagram auditing. The one vision-model result
  (57% accuracy at detecting missing flow-diagram details [20]) is too
  weak to rely on.

## Open questions / weak evidence

- Adoption rates vary widely, and reporting remains incomplete even where
  CONSORT is endorsed. A Cochrane review found that endorsing journals
  reported trials more completely on 25 of 27 outcomes, five of them
  statistically significant. Allocation concealment, for example, was
  adequately reported in 45% of RCTs in endorsing journals and 22% in
  non-endorsing ones [24]. A large LLM-assisted audit put mean CONSORT
  compliance at 57% for 2010–2024 [21]. Compliance for newer guidelines is
  lower. (This replaces an earlier citation to "Turner et al. *Trials*
  2012", which we could not locate. The Turner et al. 2012 review appeared
  in the Cochrane Database of Systematic Reviews and in summary form in
  *Systematic Reviews*.)
- Whether guideline compliance improves *outcomes* (reduced research waste,
  more accurate meta-analyses) is plausible but not directly established by
  RCT-grade evidence — the natural experiment is hard to run.
- The AI extensions are very new. CONSORT-AI / SPIRIT-AI / TRIPOD+AI have
  been adopted by *Nature Medicine*, *BMJ*, and *Lancet Digital Health* but
  field-wide uptake is still patchy. The 2025–2026 wave of LLM guidelines
  (TRIPOD-LLM, REFINE, CHART, GAMER, and the behavioural-science checklist)
  overlaps in scope, and it is not yet clear which one journals will
  require.
- How CONSORT-AI and SPIRIT-AI fit with the 2025 base checklists is
  unresolved (see above).
- The LLM-adherence studies [20–23] all evaluate published papers against
  established checklists. Their performance on pre-submission drafts, on
  the renumbered 2025 checklists, and on non-English or non-biomedical
  manuscripts is untested.
- EQUATOR catalogs hundreds of guidelines; many overlap, many are dormant.
  Auto-detecting *which* guideline applies to a given manuscript is
  non-trivial. A naïve routing rule (e.g., design-type keyword match) will
  misroute prospectively-collected cohort studies that look like trials.

## References

1. Schulz KF, Altman DG, Moher D; CONSORT Group. CONSORT 2010 Statement:
   updated guidelines for reporting parallel group randomised trials.
   *BMJ*. 2010;340:c332. DOI: 10.1136/bmj.c332.
2. von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP;
   STROBE Initiative. The Strengthening the Reporting of Observational
   Studies in Epidemiology (STROBE) Statement: guidelines for reporting
   observational studies. *PLoS Med*. 2007;4(10):e296. DOI:
   10.1371/journal.pmed.0040296.
3. Page MJ, McKenzie JE, Bossuyt PM, *et al.* The PRISMA 2020 statement:
   an updated guideline for reporting systematic reviews. *BMJ*.
   2021;372:n71. DOI: 10.1136/bmj.n71.
4. Percie du Sert N, Hurst V, Ahluwalia A, *et al.* The ARRIVE guidelines
   2.0: Updated guidelines for reporting animal research. *PLoS Biol*.
   2020;18(7):e3000410. DOI: 10.1371/journal.pbio.3000410.
5. Bossuyt PM, Reitsma JB, Bruns DE, *et al.* STARD 2015: an updated list
   of essential items for reporting diagnostic accuracy studies. *BMJ*.
   2015;351:h5527. DOI: 10.1136/bmj.h5527.
6. Collins GS, Reitsma JB, Altman DG, Moons KGM. Transparent Reporting of
   a multivariable prediction model for Individual Prognosis Or Diagnosis
   (TRIPOD): the TRIPOD Statement. *BMJ*. 2015;350:g7594. DOI:
   10.1136/bmj.g7594.
7. Collins GS, Moons KGM, Dhiman P, *et al.* TRIPOD+AI statement: updated
   guidance for reporting clinical prediction models that use regression
   or machine learning methods. *BMJ*. 2024;385:e078378. DOI:
   10.1136/bmj-2023-078378. PMID: 38626948. (Correction: *BMJ*
   2024;385:q902. Accompanying editorial: Cohen JF, Bossuyt PM. *BMJ*
   2024;385:q824, DOI: 10.1136/bmj.q824.)
8. Liu X, Cruz Rivera S, Moher D, Calvert MJ, Denniston AK; SPIRIT-AI and
   CONSORT-AI Working Group. Reporting guidelines for clinical trial
   reports for interventions involving artificial intelligence: the
   CONSORT-AI extension. *Nat Med*. 2020;26:1364–1374. DOI:
   10.1038/s41591-020-1034-x.
9. Cruz Rivera S, Liu X, Chan A-W, *et al.* Guidelines for clinical trial
   protocols for interventions involving artificial intelligence: the
   SPIRIT-AI extension. *Nat Med*. 2020;26:1351–1363. DOI:
   10.1038/s41591-020-1037-7.
10. EQUATOR Network. Enhancing the QUAlity and Transparency Of health
    Research. https://www.equator-network.org/ (accessed 2026-10-20;
    library listing at https://www.equator-network.org/reporting-guidelines/).
11. Hopewell S, Chan A-W, Collins GS, Hróbjartsson A, *et al.* CONSORT 2025
    statement: updated guideline for reporting randomised trials. *BMJ*.
    2025;389:e081123. DOI: 10.1136/bmj-2024-081123. PMID: 40228833.
    Explanation and elaboration: *BMJ* 2025;389:e081124, DOI:
    10.1136/bmj-2024-081124.
12. Chan A-W, Boutron I, Hopewell S, Moher D, *et al.* SPIRIT 2025
    statement: updated guideline for protocols of randomised trials.
    *BMJ*. 2025;389:e081477. DOI: 10.1136/bmj-2024-081477. PMID: 40294953.
13. Sounderajah V, Guni A, Liu X, Collins GS, *et al.*; STARD-AI Steering
    Committee. The STARD-AI reporting guideline for diagnostic accuracy
    studies using artificial intelligence. *Nat Med*.
    2025;31(10):3283–3289. DOI: 10.1038/s41591-025-03953-8. PMID: 40954311.
14. Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, *et al.* The
    TRIPOD-LLM reporting guideline for studies using large language
    models. *Nat Med*. 2025;31(1):60–69. DOI: 10.1038/s41591-024-03425-5.
    PMID: 39779929.
15. Mese I, Akinci D'Antonoli T, Bluethgen C, Bressem K, *et al.* Reporting
    checklist for foundation and large language models in medical research
    (REFINE): an international consensus guideline. *Diagn Interv Radiol*.
    2026 (ahead of print). DOI: 10.4274/dir.2026.263812. PMID: 41742713.
16. CHART Collaborative. Reporting guidelines for chatbot health advice
    studies: explanation and elaboration for the Chatbot Assessment
    Reporting Tool (CHART). *BMJ*. 2025;390:e083305. DOI:
    10.1136/bmj-2024-083305. PMID: 40750271. (The CHART statement itself
    was co-published in several journals, including *BMJ Medicine* and
    *BMC Medicine*.)
17. Feuerriegel S, Barrie C, Crockett MJ, Globig LK, *et al.* A reporting
    checklist for large language models in behavioural science. *Nat Hum
    Behav*. 2026;10(7):1182–1186. DOI: 10.1038/s41562-026-02492-7.
    PMID: 42265331.
18. Luo X, Tham YC, *et al.*; GAMER Working Group. Reporting guideline for
    the use of Generative Artificial intelligence tools in MEdical
    Research: the GAMER Statement. *BMJ Evid Based Med*. 2025;30(6):390–400.
    DOI: 10.1136/bmjebm-2025-113825. PMID: 40360239.
19. PRISMA Executive. PRISMA extensions (including extensions under
    development). https://www.prisma-statement.org/extensions (accessed
    2026-10-20).
20. Wrightson JG, Blazey P, Moher D, *et al.* GPT for RCTs? Using AI to
    determine adherence to clinical trial reporting guidelines. *BMJ Open*.
    2025;15(3):e088735. DOI: 10.1136/bmjopen-2024-088735. PMID: 40107689.
21. Srinivasan A, Berkowitz J, Friedrich NA, *et al.* Large Language Model
    Analysis of Reporting Quality of Randomized Clinical Trial Articles: A
    Systematic Review. *JAMA Netw Open*. 2025;8(8):e2529418. DOI:
    10.1001/jamanetworkopen.2025.29418. PMID: 40875232.
22. Chen D, Li P, Khoshkish E, *et al.* AutoReporter: development of an
    artificial intelligence tool for automated assessment of research
    reporting guideline adherence. *J Am Med Inform Assoc*.
    2026;33(3):724–731. DOI: 10.1093/jamia/ocaf223. PMID: 41435508.
23. Spiero I, Leeuwenberg AM, Kamperman J, *et al.* Using large language
    models for automated assessment of reporting quality and completeness
    of prediction model studies. *J Clin Epidemiol*. 2026;196:112320. DOI:
    10.1016/j.jclinepi.2026.112320. PMID: 42134730.
24. Turner L, Shamseer L, Altman DG, *et al.* Consolidated standards of
    reporting trials (CONSORT) and the completeness of reporting of
    randomised controlled trials (RCTs) published in medical journals.
    *Cochrane Database Syst Rev*. 2012;11:MR000030. DOI:
    10.1002/14651858.MR000030.pub2. PMID: 23152285. Summary version:
    *Syst Rev*. 2012;1:60. DOI: 10.1186/2046-4053-1-60.
