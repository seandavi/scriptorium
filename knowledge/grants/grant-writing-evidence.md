# Grant writing evidence: what's actually known about what wins

*Last updated: 2026-10-20*

## Synthesis

A scriptorium grant skill should not pretend that the evidence base
for "what wins a grant" is anywhere as clean as the evidence base for
"what wins a published paper." The grant literature splits into three
strata, each with different epistemic status. First, **the empirical
peer-review-quality literature** — studies of inter-reviewer
agreement, predictive validity of scores, institutional bias —
provides strong evidence that grant review is noisier and less
discriminating than reviewers themselves believe. Second, **the
funding-outcomes data** — NIH RePORT statistics, success-rate trends,
early-stage-investigator (ESI) funding rates — establishes the
structural difficulty of funding and the importance of resubmission.
Third, **practitioner
wisdom** — Russell & Morrison, Robert Porter's RD-specialist
materials, agency-specific writing guides — codifies craft norms that
have not, for the most part, been subjected to large-N empirical
testing.

Two findings from the empirical literature should anchor any honest
grant skill. Pier et al. (2018) showed that two reviewers evaluating
the same NIH application produce ratings about as similar to each
other as ratings of two *different* applications — that is, almost
no agreement. Fang, Bowen & Casadevall (2016) showed that within the
funded range, percentile scores barely predict subsequent citation
productivity (AUC ≈ 0.54). The implication is uncomfortable: peer
review can usually identify clearly weak applications and clearly
strong ones, but discrimination among the middle is closer to luck
than to skill. A 2026 registered report on 134,991 reviews at four
Norwegian funders puts reliability higher — moderate, with ICCs of
0.50–0.65 — but agrees that most disagreement is specific to the
application, not to the reviewer.[^11]

This does not mean "grant writing doesn't matter." It means *the
signal-to-noise ratio is low*, and writing exists to maximize the
signal applicants can control — clarity, structural fit to review
criteria, demonstrated feasibility, anticipation of reviewer
objections — while accepting that outcomes will retain a stochastic
component beyond any author's control.

Since 2025 the funding context has tightened and the rules around AI
have changed. NIH R01-equivalent success rates fell from 18.7% in
FY2024 to 13.0% in FY2025.[^8] The person-based ESI funding rate fell
from 29.8% (FY2023) to 18.9% (FY2025).[^9] NIH institutes no longer
rely on paylines when deciding what to fund.[^14] NIH will not treat
applications "substantially developed by AI" as the applicants'
original ideas, and it limits each PI to six applications per
calendar year.[^13] A 2026 *PNAS* study found that LLM involvement in
NIH and NSF proposals rose sharply from 2023, and that higher LLM
involvement was associated with proposals that sit closer to
recently funded work.[^12] For a writing tool, that last finding is a
direct caution: AI-assisted positioning may make proposals less
distinctive.

## Evidence and frameworks

**Pier et al. (2018), *PNAS* 115(12):2952–2957.** "Low agreement
among reviewers evaluating the same NIH grant applications." A
controlled experiment replicating NIH review in four constructed
study sections (8–12 reviewers each): the authors analyzed 83 primary
ratings and critiques from 43 reviewers of the same group of 25 R01
applications. Sixteen applications had been funded on first
submission; for the other nine, which were funded only after
resubmission, the study used the initial unfunded version. Each
application had 2–4 primary reviewers. Headline finding: **two
randomly selected ratings for the same application were on average
just as similar to each other as two randomly selected ratings for
different applications.** The outcome of review depended more on
*which reviewer* evaluated the grant than on the grant itself. The
authors are explicit: this is a fundamental challenge to the validity
of grant peer review as currently practiced.[^1]

**Fang, Bowen & Casadevall (2016), *eLife* 5:e13323.** A re-analysis
of NIH R01 grants funded 1980–2008: within funded grants with
percentile scores of 20 or better (102,740 grants analyzed),
percentile rank was a poor predictor of
citation productivity. AUC = 0.54 (95% CI 0.53–0.54) for "above
median citation productivity." An AUC of 0.5 is random chance.
Within the funded range, scores barely beat coin-flip prediction of
which grants will be most productive.[^2]

**Lauer & Nakamura (2015), *NEJM* 373(20):1893–1895.** "Reviewing
peer review at the NIH." A perspective by the heads of NIH's Office
of Extramural Research and Center for Scientific Review on how NIH
evaluates its own peer review. We use it for a distinction that is
our framing rather than a quotation (not re-checked against the
article text in this refresh): peer review must discriminate at the
funding boundary even if it cannot discriminate within the funded
pool. The *decision-quality* question is different from the
*predictive-validity* question.[^3]

**Eblen et al. (2016).** See [[nih-significance-patterns]] for full
detail. The 123,700-application analysis (FY2010–2013, legacy
five-criterion scoring) found that "the Approach and, to a lesser
extent, the Significance criterion scores were the main predictors"
of Overall Impact and funding. This is the empirical backbone for the
practitioner adage that an aims page must *demonstrate feasibility*,
not merely *assert importance*. Under the Simplified Review Framework,
NIH's 2025 scoring guidance tells reviewers that the Importance
(Factor 1) score sets a ceiling on Overall Impact, so the two must now
be read together; see [[nih-significance-patterns]].

**Reliability across funders: Hesselberg et al. (2026), *PLOS One*
21(9):e0356108.** A registered report analyzing 134,991 reviews from
four Norwegian research funders with a cross-classified regression
model. Inter-rater reliability was "moderate across funders: average
ICCs ranged from 0.50 to 0.65." Only 3.1% of disagreement came from
stable reviewer tendencies, against 24.1% at the application level
and 55.2% residual. In-depth review roles (reviewers with more
responsibility for an application) were associated with slightly
lower disagreement; reviews by subject-matter experts were associated
with modestly *higher* disagreement. The authors conclude that gains
"are more likely to come from clearer criteria, more structured
review formats, and reducing application-level ambiguity", and that
these are expected to be incremental.[^11] Researcher inference: the
application-level share is the part an author can act on, by making
the proposal less ambiguous to read.

**Halo effect and institutional prestige bias.** Multiple studies
document that reviewers' impressions are influenced by institutional
prestige and by prior recognition. A 2024 *eLife* meta-research paper
(Hultgren, Patras & Hicks) examined the Beckman Young Investigator
award after the Beckman Foundation asked applicants, from 2020, to
blind the technical proposal in the initial letter of intent. Comparing
award years 2021–2024 with 2017–2020, the distribution of applicants
invited to submit a full application "shifted from those affiliated
with institutions regarded as more prestigious to those outside of
this group", and the shift carried through to final awards. The
authors "did not find evidence of a shift in the distribution of
applicants with respect to gender."[^4] In computer science, the
evidence is mixed and method-sensitive. A natural experiment at ICLR
(which moved from single- to double-blind review) tested whether
double-blind review reduces prestige bias.[^7] An observational study
of computer-systems conferences found that, depending on the prestige
metric and analysis choices, the same data "can lead to contradictory
conclusions with high statistical significance".[^5] NIH cites "the
potential for reputational bias to affect peer review outcomes" as a
reason for the Simplified Review Framework, and says the binary
Factor 3 rating is meant to limit the influence of general scientific
reputation.[^15]

**Success rates and ESI dynamics.** NIH reported the following for
FY2025 against FY2024: R01-equivalent applications rose 12.1% (37,478
to 42,022), competing R01-equivalent awards fell 21.8% (7,000 to
5,471), and the R01-equivalent success rate fell from 18.7% to 13.0%
(it was 21.6% in FY2023). NIH links the drop to fewer awards, more
applications, and more awards being forward-funded.[^8] For ESIs,
NIH reported a person-based funding rate of 29.8% in FY2023, 26.1% in
FY2024, and 18.9% in FY2025, with 1,587, 1,423, and 1,144 ESI
R01-equivalent awardees. NIH links the FY2025 drop in part to a
requirement, from June 2025, to use 50% of remaining competing
research project grant funds for full-year (multiyear) funded
awards.[^9] These are NIH-wide figures. The May 2026 version of this
note attributed a ~30% → ~18% ESI decline to institute-level
sources. That figure appears to match these NIH-wide person-based
rates rather than an institute-specific figure (researcher
inference: the numbers match, but the original source of the old
figure was not traced). Institutes have historically used
preferential paylines for ESIs.[^6] Since the January 2026 Council
round, NIH's Unified Funding Strategy says institutes "will not rely
on funding paylines". Career stage is now one consideration among
several, under the tenet "Consider investigator career stage and
promote sustainability of the biomedical research workforce."[^14]
*Resubmission outcomes* are uneven. NCI's grant FAQ says: "Some who
were not discussed on first submission, are funded on resubmission.
Some who were discussed on first submission, do worse on
resubmission. There is really no way of saying what the 'chances'
are." Reviewers "can identify new issues/weaknesses."[^10] There is
no reliable a priori prediction of resubmission outcome from initial
score alone.

**The "perfect score → fund" simplification.** Practitioner narrative
sometimes treats funding as deterministic in scores: "if your
percentile is below the payline, you're funded." The actual decision
process is messier. Program staff have substantial discretion;
priority scores feed into institute-level decisions that incorporate
portfolio balance, ESI policies, programmatic priorities, and
post-review changes (e.g., budget adjustments, just-in-time
documentation). Scriptorium should not promise score thresholds as
funding promises. Since January 2026 this is NIH's stated policy
rather than an informal reality: institutes do not rely on paylines,
and they weigh "peer review information in its entirety" alongside
"health priorities, scientific opportunities, the workforce,
availability of funds, and the wider research portfolio."[^14] Under
the emergency review modifications in force through the January 2027
Council round, only about the top third of applications is discussed,
and a "competitive but not discussed" middle third is also considered
for funding.[^16]

**AI in applications and its observed effects.** NOT-OD-25-132
(effective for the September 25, 2025 receipt date) says: "NIH will
not consider applications that are either substantially developed by
AI, or contain sections substantially developed by AI, to be original
ideas of applicants." It warns that "AI use may result in plagiarism,
fabricated citations, or other kinds of research misconduct", says
NIH uses AI-detection technology, and allows post-award referral to
the Office of Research Integrity. The same notice caps each PI at six
new, renewal, resubmission, or revision applications per calendar
year.[^13] Qian et al. (2026, *PNAS*) combined confidential NIH and
NSF submissions from two US R1 universities with all publicly
released NIH and NSF awards. They found that LLM use "rises sharply
beginning in 2023" with a bimodal split between minimal and
substantive use. Higher LLM involvement "is consistently associated
with lower semantic distinctiveness, positioning projects closer to
recently funded work within the same agency." At NIH, LLM use was
positively associated with proposal success and early publication
output; the productivity gains were "concentrated in nonhit papers".
No comparable associations appeared at NSF.[^12] The study is
observational: it cannot show that LLM use causes success, and the
success association may reflect which applicants adopted LLMs.

**Practitioner wisdom (label clearly).** The dominant practitioner
sources are:

- **Russell & Morrison, *Grant Application Writer's Workbook*** —
  step-by-step prescriptive workbook. Practitioner consensus, not
  empirical study.
- **Robert Porter (RD Specialist materials)** — widely-referenced
  practitioner writing on Approach sections, reviewer psychology,
  and resubmission strategy. Drawn from experience as a research
  development professional; not empirical research.
- **Friedman, *Career Development Awards*** — guidance on K-series
  awards. [TODO verify: no book or guide by this author and title
  was located in the October 2026 refresh; keep unverified until a
  bibliographic record is found, or remove.]
- **Agency-specific guides** (NIAID, NINDS, NIDDK practitioner pages;
  NSF program officer essays).

These are valuable as craft guides but should not be cited as
evidence-based in the same register as Pier, Fang et al., or Eblen.

## How this informs scriptorium

**Honesty about noise.** Any grant skill — `specific-aims`,
`grant-reviewer-simulation`, `aims-page-critique` — should produce
outputs that acknowledge the empirical finding that grant outcomes
are noisier than reviewers themselves believe. This is not
defeatism; it is calibration. Outputs should help authors maximize
controllable signal, not promise outcome guarantees.

**Approach over Significance — revised.** Eblen's finding that
Approach was the strongest single predictor of Overall Impact still
justifies a rigorous "Approach scrutinizer" persona in
`grant-reviewer-simulation`: a reviewer who probes feasibility,
preliminary data, pitfalls, alternative strategies, statistical
power, and timeline. But under NIH's 2025 scoring guidance a weak
Importance (Factor 1) score caps Overall Impact however strong the
approach is (see [[nih-significance-patterns]]). For NIH targets,
aims-page critique should check the importance slots first. It should
then treat the approach sentences (typically the 2–4 sentence
descriptions under each aim) as the next-highest-leverage content,
not as a substitute for a convincing gap.

**Reduce ambiguity, not just weaknesses.** Hesselberg et al. place
most reviewer disagreement at the application level.[^11] A critique
skill can help by flagging passages that two careful readers could
reasonably read differently: an undefined scope, an aim with two
possible interpretations, an unstated success criterion. This is
researcher inference from the variance decomposition. No study has
tested it as an intervention.

**Bias-aware critique.** Scriptorium should resist amplifying the
institutional-prestige bias that empirical work has documented.
A `grant-reviewer-simulation` persona should not be encouraged to
react more favorably to "investigator at MIT" framing than to
"investigator at [less-recognized institution]" framing — the bias
is documented as a *real-world reviewer behavior*, but reproducing
it in scriptorium critiques would compound the problem rather than
help the author counteract it.

**Resubmission posture.** A `resubmission-strategy` skill (future)
should be empirical-evidence-aware: the FAQ-level finding that
resubmission outcomes are unpredictable from initial score alone
means the skill cannot recommend resubmission strategy based on
score; it must focus on substantive responses to specific reviewer
critiques. With paylines gone and released scores possibly replaced
by categories (see [[nih-significance-patterns]]), the written
critiques are the most stable input such a skill will have.

**AI-originality policy and distinctiveness.** For NIH targets,
generated aims or significance prose runs into NOT-OD-25-132.[^13]
Separately, the Qian et al. finding suggests a quieter risk: text
shaped with LLM help drifts toward what was recently funded.[^12]
Grant skills should keep the author's own wording and positioning as
the default and flag convergent, generic positioning rather than
introduce it. Both points are researcher inference about skill
design; neither source evaluates writing tools.

**Practitioner-wisdom labeling in outputs.** When a critique skill
draws on practitioner conventions (the four-paragraph aims page,
the bulleted-aims pattern, the "long-term goal → objective → central
hypothesis" cadence), the output should signal that the
recommendation is drawn from craft tradition, not from peer-reviewed
evidence. The DESIGN.md principle of inspectability extends to
provenance.

## Implementation priority for scriptorium

**Verdict:** No — framing-only. This note does not become a skill by
itself.

**If No:** It is the calibration layer for every grant-facing skill
(v0.4 `specific-aims`, `aims-significance-coherence`, and the grant
personas of `reviewer-simulation`). It sets what those skills may and
may not claim: no funding probabilities, no payline language,
practitioner conventions labeled as such, and an explicit statement
of review noise. The October 2026 refresh adds two constraints those
skills inherit: NIH's AI-originality policy (NOT-OD-25-132) and the
observed link between LLM use and less distinctive proposals.

## Open questions / weak evidence

- Pier et al. used a constructed experimental setting (offline
  re-rating of previously-reviewed grants). The extent to which
  *real-time study-section dynamics* — discussion, anchoring, primary
  reviewer influence — restores or worsens inter-rater consistency
  is partially studied (see [[reviewer-archetypes-grants]]) but not
  fully resolved.
- Most peer-review evidence is from NIH. NSF, DOE, NSF-style agencies,
  and private foundations have less-studied review dynamics; the
  Pier/Fang findings should not be extrapolated wholesale.
- Pier et al. (no agreement among individual NIH reviewers) and
  Hesselberg et al. (moderate ICCs at Norwegian funders) are not
  directly comparable: different funders, scales, reviewer roles, and
  reliability statistics. Neither settles how reliable NIH review is
  under the Simplified Review Framework.
- Practitioner-wisdom interventions (e.g., "follow the four-paragraph
  aims structure") have not been subjected to randomized comparison
  against alternatives. The craft norms may or may not be causally
  helpful; we know only that successful applicants tend to follow
  them.
- Qian et al. is observational. Whether LLM-assisted writing causes
  higher NIH success, or whether early adopters differ in other ways,
  is open. So is how NIH's AI policy changed applicant behaviour after
  September 2025.

## References

[^1]: Pier EL, Brauer M, Filut A, et al. Low agreement among
    reviewers evaluating the same NIH grant applications. *PNAS*.
    2018;115(12):2952–2957. doi:10.1073/pnas.1714379115.
    PMID: 29507248.

[^2]: Fang FC, Bowen A, Casadevall A. NIH peer review percentile
    scores are poorly predictive of grant productivity. *eLife*.
    2016;5:e13323. doi:10.7554/eLife.13323. PMID: 26880623.

[^3]: Lauer MS, Nakamura R. Reviewing peer review at the NIH. *N Engl
    J Med*. 2015;373(20):1893–1895. doi:10.1056/NEJMp1507427.

[^4]: Hultgren AE, Patras NMF, Hicks J. Blinding reduces institutional
    prestige bias during initial review of applications for a young
    investigator award. *eLife*. 2024;13:e92339.
    doi:10.7554/eLife.92339.

[^5]: Frachtenberg E, McConville KS. Metrics and methods in the
    evaluation of prestige bias in peer review: A case study in
    computer systems conferences. *PLOS ONE*. 2022;17(2):e0264131.
    doi:10.1371/journal.pone.0264131.

[^6]: NIH RePORT. Success rates statistics.
    https://report.nih.gov/funding/nih-budget-and-spending-data-past-fiscal-years/success-rates .
    Institute-specific ESI paylines are published on each institute's
    funding page (e.g., NHLBI, NIDDK, NCI, NINDS); recent trend data
    aggregated by practitioner trackers including the WriteDIT NIH
    Paylines & Resources page (https://writedit.wordpress.com/nih-paylines-resources/).
    Superseded in part: since the January 2026 Council round NIH
    institutes no longer rely on paylines (see [^14]); use the
    NIH-wide FY2025 figures in [^8] and [^9] for current rates.

[^7]: Sun M, Barry Danfa J, Teplitskiy M. Does double-blind peer
    review reduce bias? Evidence from a top computer science
    conference. *J Assoc Inf Sci Technol*. 2022;73(6):811–819.
    doi:10.1002/asi.24582.

[^8]: NIH Extramural Nexus. Fiscal Year 2025 By the Numbers:
    Extramural Grant Investments in Research. March 12, 2026.
    https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/03/fiscal-year-2025-by-the-numbers-extramural-grant-investments-in-research

[^9]: NIH Extramural Nexus. NIH Support for Early Stage Investigators
    in FYs 2024 and 2025. February 10, 2026.
    https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/02/nih-support-for-early-stage-investigators-in-fys-2024-and-2025

[^10]: National Cancer Institute, Division of Cancer Biology. Getting
    a Grant from NCI: FAQs.
    https://www.cancer.gov/about-nci/organization/dcb/funding/resources/faqs
    (accessed 2026-10-20).

[^11]: Hesselberg J-O, Ulleberg P, Sørensen Ø, Fostervold KI,
    Ingvaldsen SH, Svege I. Why do reviewers disagree? Evidence from
    four funders and 134,000 reviews. *PLOS One*. 2026;21(9):e0356108.
    doi:10.1371/journal.pone.0356108.

[^12]: Qian Y, Wen Z, Furnas AC, Bai Y, Shao E, Wang D. The rise of
    large language models and the direction and impact of US federal
    research funding. *PNAS*. 2026;123(33):e2601439123.
    doi:10.1073/pnas.2601439123. Preprint: arXiv:2601.15485.

[^13]: NIH. NOT-OD-25-132: Supporting Fairness and Originality in NIH
    Research Applications. Released July 17, 2025.
    https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html

[^14]: NIH Extramural Nexus. Implementing a Unified NIH Funding
    Strategy to Guide Consistent and Clearer Award Decisions.
    November 21, 2025.
    https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/implementing-a-unified-nih-funding-strategy-to-guide-consistent-and-clearer-award-decisions

[^15]: NIH. Simplified Peer Review Framework.
    https://grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework
    (accessed 2026-10-20).

[^16]: Reed B (CSR). Emergency Modifications to NIH Peer Review. NIH
    Extramural Nexus, November 24, 2025 (editor's note 9/16/26:
    extended through the January 2027 Council round, NOT-OD-26-114).
    https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/emergency-modifications-to-nih-peer-review
