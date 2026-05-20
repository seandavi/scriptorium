# Reporting guidelines (EQUATOR Network)

*Last updated: 2026-05-17*

## Synthesis

Reporting guidelines are checklists that specify, study design by study
design, what information a paper *must* report to be evaluable. They are not
style advice; they are minimum-information standards, analogous to MIAME for
microarrays or DICOM for imaging. The EQUATOR Network
(equator-network.org), an international consortium founded in 2008, maintains
the canonical registry — currently more than 600 guidelines across study
designs and reporting domains.

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

## Evidence and frameworks

### CONSORT 2010 — randomized controlled trials

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

### ARRIVE 2.0 — animal research

Percie du Sert N, Hurst V, Ahluwalia A, *et al.* The ARRIVE guidelines 2.0:
Updated guidelines for reporting animal research. *PLoS Biol*. 2020;
18(7):e3000410. DOI: 10.1371/journal.pbio.3000410. [4]

ARRIVE 2.0 reorganized the 2010 original into two priority tiers: the
"Essential 10" (the absolute minimum, including study design, sample size,
inclusion/exclusion criteria, randomization, blinding, outcome measures,
statistical methods, experimental animals, experimental procedures, and
results) and a Recommended Set covering ethics, housing, contextual detail.
Adoption by funders (Wellcome, NIH NC3Rs) has driven uptake.

### STARD 2015 — diagnostic accuracy

Bossuyt PM, Reitsma JB, Bruns DE, *et al.* STARD 2015: an updated list of
essential items for reporting diagnostic accuracy studies. *BMJ*.
2015;351:h5527. DOI: 10.1136/bmj.h5527. [5]

A 30-item checklist for studies estimating the accuracy of a diagnostic
test against a reference standard. Co-published in *BMJ*, *Radiology*, and
*Clinical Chemistry* in October 2015. A STARD-AI extension was published in
2025 (Sounderajah V, *et al. Nat Med*. 2025; DOI: 10.1038/s41591-025-03953-8)
to address artificial-intelligence-based diagnostic tools.

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
machine learning methods. *BMJ*. 2024;385:q824. DOI: 10.1136/bmj.q824. [7]
(The full statement: *BMJ* 2024;385:e078378.)

TRIPOD+AI expanded the checklist to 27 items and unified reporting for
regression-based and ML-based models. It places new emphasis on
trustworthiness, fairness, and reproducibility — including reporting of
training/validation/test splits, hyperparameter selection, and fairness
across demographic subgroups.

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
  the statistics items of the relevant guideline (CONSORT items 7a, 12;
  STROBE item 12; TRIPOD items 8, 9). Inconsistencies between methods and
  results in *those specific items* are higher-severity than free-text
  arithmetic mismatches.
- **`sample-size-validation`** (planned). Should detect whether sample-size
  justification is present (CONSORT 7a; ARRIVE Essential 10 item 2; STROBE
  item 10) and whether the justification names the assumed effect size,
  power, and alpha. The skill should not invent these — only flag absence.
- **`reporting-guideline-compliance`** (proposed new skill). A direct mapping from
  manuscript sections to checklist items. Output: per-item status (present /
  partial / missing / not-applicable) with a span pointer for each
  "present" claim. This is a critique skill, not transformative.
- **`journal-style-conversion`** (planned). Reporting guidelines are part
  of journal style. A conversion skill should know which guideline each
  target journal requires and check that the manuscript complies before
  reformatting citations or section titles.
- **`reviewer-simulation`** (current). The simulator should consult the
  applicable guideline as a baseline of reviewer concerns — many real
  reviewer comments are paraphrases of checklist items the manuscript
  didn't satisfy.

A practical design note: the manuscript-state schema should be able to
record which reporting guideline(s) apply, so skills don't have to
re-detect. Adding an optional `reporting_guidelines: [CONSORT-AI, TRIPOD+AI]`
field to `MANUSCRIPT_STATE.yaml` would let any skill consume the answer.

## Open questions / weak evidence

- Adoption rates vary widely. Studies of CONSORT compliance show 50–70%
  reporting completeness in journals that require it (e.g., Turner et al.
  *Trials* 2012); compliance for newer guidelines is lower.
- Whether guideline compliance improves *outcomes* (reduced research waste,
  more accurate meta-analyses) is plausible but not directly established by
  RCT-grade evidence — the natural experiment is hard to run.
- The AI extensions are very new. CONSORT-AI / SPIRIT-AI / TRIPOD+AI have
  been adopted by *Nature Medicine*, *BMJ*, and *Lancet Digital Health* but
  field-wide uptake is still patchy.
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
   or machine learning methods. *BMJ*. 2024;385:q824. (Full statement:
   *BMJ* 2024;385:e078378.) [TODO verify exact DOI of full statement]
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
    Research. https://www.equator-network.org/ (accessed 2026-05-17).
