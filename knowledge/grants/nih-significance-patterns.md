# NIH significance patterns: what funded grants look like

*Last updated: 2026-05-17*

## Synthesis

NIH grant applications — particularly R01s — have a recognizable
structural anatomy that has crystallized over decades of practitioner
experience and is reinforced by the agency's own review criteria.
The most studied single artifact is the **Specific Aims page**: a
one-page document that, by near-unanimous practitioner consensus,
determines a substantial portion of the application's fate before
reviewers read anything else. Empirical work on how reviewers
allocate criterion scores (Eblen et al. 2016) supports this
practitioner intuition: among the five regulatory criteria, the
*Approach* criterion correlates most strongly with the overall
impact score and the funding outcome — but Significance and
Innovation also carry meaningful predictive weight.

The 2024 transition to the NIH Simplified Review Framework
restructured how these criteria are scored without removing them.
Reviewers now assess three factors: **Importance of the Research**
(Significance + Innovation, scored 1–9), **Rigor and Feasibility**
(Approach, scored 1–9), and **Expertise and Resources**
(Investigator + Environment, evaluated as sufficient/not sufficient
rather than numerically scored). The five regulatory criteria persist;
their packaging into factors changes the rhetorical work the
Specific Aims page must do.

For scriptorium grant skills, this means two things. First, the
Specific Aims page is the right unit of focus — it is structured,
short, high-leverage, and follows a near-canonical four-paragraph
shape. Second, "what makes a good aims page" is a mix of *practitioner
wisdom* (well-documented across multiple workbooks but mostly
non-empirical) and *empirical findings* (criterion-score
correlations, percentile-funding relationships). The two should be
labeled distinctly.

## Evidence

**Eblen et al. (2016), *PLOS ONE* 11(6):e0155060.** Analyzed the
relationship of the five criterion scores (Significance, Investigator,
Innovation, Approach, Environment) to the Overall Impact score and to
funding outcomes for **over 123,700 competing R01 applications** for
fiscal years 2010–2013. The headline finding: **Approach was the
strongest single predictor** of the Overall Impact score across
applications, with Significance and Innovation also showing
substantial predictive weight, while Environment and Investigator
were weaker predictors at the margin. This corroborates the
practitioner adage that a fundable aims page must convey not just
that the science matters (Significance) and is novel (Innovation),
but that the work *can be done as proposed* (Approach).[^1]

**NIH Simplified Peer Review Framework (NOT-OD-24-010, effective
January 2025).** Reorganizes the five criteria into three factors:

- **Factor 1: Importance of the Research** — combines Significance
  and Innovation. Scored 1–9.
- **Factor 2: Rigor and Feasibility** — Approach. Scored 1–9.
- **Factor 3: Expertise and Resources** — combines Investigator and
  Environment. Evaluated as sufficient / not sufficient.

The scale remains 1 (exceptional) to 9 (poor), with 5 as average.
Overall Impact remains a separate 1–9 score that reviewers assign
holistically.[^2]

**NIH Specific Aims structural conventions.** Practitioner
literature converges on a four-paragraph aims page:

1. **Hook / significance opener.** Establishes the problem and its
   scientific or clinical importance. Usually 3–5 sentences ending
   with the gap.
2. **Gap and rationale.** Articulates what is not known, why the
   gap matters, and what the field's working hypothesis is.
3. **Premise and central hypothesis.** Names the long-term goal, the
   immediate objective, and the central hypothesis the proposal
   tests, anchored in the applicant's own preliminary data.
4. **Aims block + impact close.** Two or three specific aims (often
   bulleted), each a 2–4 sentence description of approach and
   expected result. Closes with a sentence on how the work advances
   the field.[^3]

Practitioner sources (NIAID's draft-specific-aims guidance, NINDS's
writing-specific-aims page, the Russell & Morrison *Workbook*) all
prescribe variants of this structure. The convergence is striking
and suggests that *form has won*: applicants who deviate substantially
from this shape pay a legibility cost with reviewers who have
internalized the convention.

**Russell & Morrison, *The Grant Application Writer's Workbook* (NIH
version; Grant Writers' Seminars & Workshops).** The dominant
practitioner workbook for NIH grant writing. Provides a step-by-step
"bulleted outline" approach to the Specific Aims page: significance
of the problem → gap in knowledge → long-term goal → objective →
central hypothesis → rationale → specific aims → expected outcomes →
impact. The workbook is regularly updated to track NIH form changes
(current edition updated January 2026 for FORMS-I).[^4]

**Lauer et al. (2016), *eLife* 5:e13323.** "NIH peer review percentile
scores are poorly predictive of grant productivity." Analyzed
**102,740 funded grants**; among grants with percentile scores of 20
or better, percentile rank had AUC ≈ 0.54 for predicting
above-median citation productivity — essentially equivalent to chance.
The implication: *within the funded range*, peer review cannot
reliably discriminate which grants will be most productive. The
predictive validity of peer review for funding outcomes is real but
constrained; once an application is good enough to be discussed, the
noise floor is high.[^5]

**Eblen et al. extension on triage.** Combining the above with the
NIH triage process: typically ~50% of applications are streamlined
(not discussed) and receive no priority score. Among the discussed
applications, percentile rank predicts funding well at the
percentile-payline boundary but predicts productivity weakly within
the funded range. Practitioner implication: the aims page's job is
not to optimize for being "the best" — it is to get *out of the
streamlined bottom half* with enough strength to land at or below
the percentile payline.

## How this informs scriptorium

**The aims page is a structured artifact, not free prose.** A future
`specific-aims` skill (planned for v0.4 in the [[DESIGN]] roadmap)
should treat the aims page as a structured document with named
slots: hook, gap, premise, hypothesis, aims-list, impact close.
Critique and transformation skills on the aims page should target
specific slots rather than the page as a whole.

**Criterion-aware critique.** A `grant-reviewer-simulation` skill
should be able to assume reviewer personas that map to the
Simplified Framework factors: an "Importance of the Research"
reviewer focused on whether Significance and Innovation are clearly
articulated; a "Rigor and Feasibility" reviewer focused on Approach
specifics, pitfalls, and alternative strategies; an "Expertise and
Resources" reviewer who issues a sufficient/not-sufficient verdict.
See [[reviewer-archetypes-grants]] for the persona structure.

**Conservative-edit posture is even more important in grant
contexts.** Grant text is highly purpose-built: every sentence in the
aims page is doing rhetorical work. The cost of an unauthorized
rewrite is higher than for a manuscript discussion section, because
the aims page is the document reviewers cite when arguing for or
against funding. `MANUSCRIPT_STATE.yaml` for a grant project should
default to strict preservation constraints; transformation skills
should require explicit invocation.

**Practitioner wisdom is labeled.** Scriptorium should be clear in
its outputs that structural recommendations on the aims page (the
four-paragraph shape, the bulleted aims with expected outcomes, the
impact close) come from practitioner consensus, not from peer-reviewed
empirical evidence on what wins. The empirical evidence is on
criterion-score correlations, not on rhetorical conventions.

## Open questions / weak evidence

- The four-paragraph aims-page convention is well-documented in
  workbooks and institutional guidance but, as far as we have
  located, no large-N empirical study compares aims-page structure
  against funding outcomes. The convention may be a coordination
  equilibrium more than a causal advantage.
- The relative weighting of the criteria varies by study section and
  by program officer culture. Generalizations across NIH institutes
  should be hedged.
- The Simplified Framework is too recent (effective 2025) for outcome
  data; how the factor-based packaging changes review behavior is an
  open empirical question.

## References

[^1]: Eblen MK, Wagner RM, RoyChowdhury D, Patel KC, Pearson K. How
    criterion scores predict the Overall Impact score and funding
    outcomes for National Institutes of Health peer-reviewed
    applications. *PLOS ONE*. 2016;11(6):e0155060.
    doi:10.1371/journal.pone.0155060. PMID: 27249058.

[^2]: NIH. NOT-OD-24-010: Simplified Review Framework for NIH
    Research Project Grant Applications. 2023.
    https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-010.html

[^3]: NIAID. Draft Specific Aims (practitioner guidance).
    https://www.niaid.nih.gov/grants-contracts/draft-specific-aims .
    NINDS. Writing Specific Aims.
    https://www.ninds.nih.gov/funding/preparing-your-application/preparing-research-plan/writing-specific-aims

[^4]: Russell SW, Morrison DC. *The Grant Application Writer's
    Workbook: National Institutes of Health Version*. Grant Writers'
    Seminars & Workshops, LLC. Current edition: January 2026
    (FORMS-I update). https://www.grantcentral.com/workbooks/national-institutes-of-health/

[^5]: Lauer MS, Danthi NS, Kaltman J, Wu C. NIH peer review percentile
    scores are poorly predictive of grant productivity. *eLife*.
    2016;5:e13323. doi:10.7554/eLife.13323. PMID: 26880623.
