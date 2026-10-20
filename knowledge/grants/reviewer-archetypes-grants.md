# Reviewer archetypes for grant review

*Last updated: 2026-10-20*

## Synthesis

Grant review is structurally different from manuscript review, and a
grant-reviewer simulation skill should not be a re-skinned
manuscript-reviewer simulation. The differences are not stylistic.
They are: **few assigned reviewers per artifact** (NIH assigns three
or more reviewers, at least two of whom write full critiques; NSF now
requires at least two reviews per full proposal, vs. 2–4 for a
manuscript), **panel deliberation rather than independent
recommendations** (study sections discuss; manuscript reviewers do
not), **anchored scoring distributions** (study-section reviewers
calibrate against the section's recent score distribution),
**selection pressure from triage** (normally about the bottom half of
NIH applications is not discussed, and under emergency rules in force
through the January 2027 Council round only about the top third is
discussed; manuscripts are rarely silently desk-rejected after review
begins), and **explicit criterion-based scoring** (NIH and NSF
both require structured criterion ratings; manuscript reviewers
typically write free-form critiques).

These differences shape the personas that a useful reviewer-
simulation skill should expose. The manuscript-reviewer persona
toolkit — methodological skeptic, friendly champion, scope-creep
worrier — does not transfer directly. The grant-reviewer toolkit
needs personas that mirror the formal criterion structure (per
NIH Simplified Framework: Importance, Rigor and Feasibility,
Expertise and Resources), personas that mirror panel dynamics
(primary reviewer, discussant, triage-prone reviewer), and personas
that mirror funder-type variation (NIH study section, NSF panel,
HHMI advisory board, private foundation).

Review processes at both major US funders changed between mid-2025
and late 2026. NIH centralized all peer review in its Center for
Scientific Review, temporarily cut the share of applications
discussed, and proposed replacing released scores with competitiveness
categories. NSF cut its minimum review count to two (one of which may
be internal), let program officers skip panel discussion, and
reframed broadening-participation activities under Broader Impacts.
The National Science Board has also recommended renaming Broader
Impacts "Societal Benefits". Persona definitions should be dated and
tied to the funder's current published guidance, not to a
remembered process.

For scriptorium, the practical implication is that the planned
`reviewer-simulation` skill should expose grant-specific personas
distinct from manuscript-specific ones, and that the orchestrator
must select personas based on `target_type` in
`MANUSCRIPT_STATE.yaml` (grant proposal vs manuscript).

## Evidence and frameworks

### NIH study-section dynamics

**Composition.** A typical NIH study section meeting reviews 50–100
applications across 1.5–2 days (practitioner estimate; not stated in
the CSR pages cited here). CSR states that "each application is
assigned to three or more reviewers, and at least two of them
provide full written critiques"; NIAID describes CSR's assignment as
"primary and secondary reviewers plus at least one reader". In normal
operation, CSR study sections "do not review approximately the bottom
half of applications unless a reviewer asks to discuss a particular
application"; streamlined applications receive the assigned
reviewers' critiques and preliminary criterion scores but no overall
impact score. Streamlining is based on reviewer pre-meeting scores;
any single reviewer can request a streamlined application be
discussed.[^1]

**Emergency modifications (January 2026 through January 2027 Council
rounds).** After the 2025 lapse in appropriations, CSR changed the
discussion line: "The top third (30 to 35 percent) will be discussed
in the review meeting and considered for funding. The middle third
will be designated as 'competitive but not discussed' and considered
for funding. The lowest third will be designated as 'not competitive
and not discussed.'" Summary statements were reduced to a consensus
sentence, bullets on the main score-driving points, and the assigned
reviewers' critiques. NIH extended the modifications through the
January 2027 Council round, citing more than 40,000 applications for
that round.[^10]

**Centralization.** Effective with the August/October 2025 Council
round, all NIH peer review of grants, cooperative agreements, and
contracts is centralized within CSR, including review previously run
by individual institutes. NIH states that review criteria, including
the Simplified Review Framework, do not change.[^11]

**Discussion.** For each discussed application, ~15–20 minutes are
typically allotted (practitioner estimate). The discussion is
anchored by the assigned reviewers' pre-meeting scores. After
discussion, every voting member of the study section assigns a final
overall impact score. The reported priority score is the mean of
these scores; the percentile is computed across the current and
recent meetings of the same study section. In August 2026 NIH
proposed that numerical overall impact scores no longer be released
at all, with discussed applications reported as "Most Competitive"
(top 25%) or "Competitive" (26–50%). Critiques and criterion/factor
scores would still be released. This was a request for information,
not adopted policy, as of this update.[^14]

**Five-criterion scoring (regulatory).** Significance, Investigator,
Innovation, Approach, Environment. Each is scored 1–9. Under the
Simplified Framework (effective 2025): Factor 1 (Importance =
Significance + Innovation), Factor 2 (Rigor & Feasibility =
Approach), Factor 3 (Expertise & Resources = Investigator +
Environment, evaluated as sufficient/not sufficient). NIH's 2025
scoring guidance tells reviewers that the Factor 1 score sets a
ceiling on the overall impact score; see [[nih-significance-patterns]].

**Empirical reviewer reliability.** Pier et al. (2018) showed
essentially no inter-rater agreement on the same applications when
reviewers worked independently; see [[grant-writing-evidence]]. The
panel discussion *may* improve calibration somewhat, but the
underlying noise is high. A 2026 registered report covering 134,991
reviews at four Norwegian funders found moderate reliability (average
ICCs 0.50–0.65). Only 3.1% of disagreement came from stable reviewer
tendencies; reviewers in in-depth roles disagreed slightly less, and
subject-matter expert reviewers modestly more.[^12]

**Anchoring and panel effects.** Social-pressure effects in panel
deliberation have been documented. In four mock NIH study sections
of 8–12 oncology researchers reviewing the same 25 R01 applications,
Pier and colleagues identified "score calibration talk" — panelists
discussing scores rather than content — and found that only talk
initiated by *other* panelists correlated with assigned reviewers
changing their scores (Pier et al. 2017).[^16] The follow-up
*Laughter and the Chair* (Pier, Raclaw, Carnes, Ford & Kaatz, 2019)
examined the 15 cases of other-directed score calibration talk, five
of which were followed by an immediate, public score change. Score
change was more likely when shared laughter accompanied that talk
(OR = 16; 95% CI 1.09–234.25) and when the chair initiated it
(OR = 36; 95% CI 1.77–731.56). The authors note the small sample,
and the wide intervals reflect it. They warn that pressure from the
chair or from group laughter "could introduce bias in an R01's final
priority score".[^2]

**AI in NIH review.** NIH "prohibits NIH scientific peer reviewers
from using natural language processors, large language models, or
other generative Artificial Intelligence (AI) technologies for
analyzing and formulating peer review critiques for grant
applications", and states that uploading application content to
online generative AI tools violates peer-review confidentiality
(NOT-OD-23-149, 2023).[^13]

### NSF panel dynamics

**Criteria.** Two merit-review criteria: **Intellectual Merit** and
**Broader Impacts**. Both apply to every proposal. PAPPG 24-1
Chapter III.A lists five review elements that apply to both
criteria: (1) the potential to advance knowledge (Intellectual Merit)
or to benefit society and advance desired societal outcomes (Broader
Impacts); (2) the extent to which the activities "suggest and explore
creative, original, or potentially transformative concepts"; (3)
whether the plan is "well-reasoned, well-organized, and based on a
sound rationale", with "a mechanism to assess success"; (4) how well
qualified the individual, team, or organization is; and (5) whether
adequate resources are available.[^3]

**Format.** NSF review may be "conducted by *ad hoc* reviewers, a
panel of experts, or a combination of both"; the PAPPG describes
review by the program officer and "usually by three to ten other
persons outside NSF". The NSF Program Officer then "recommends to
the cognizant NSF Division Director whether the proposal should be
declined or recommended for award"; a Grants and Agreements Officer
makes the final award decision.[^3] Panels do not assign NIH-style
numerical scores. The categorical labels a panel uses vary by program
and are not specified in the PAPPG chapter cited here.

**December 2025 changes.** PAPPG 24-1 Supplement 1 (effective
December 8, 2025) states: "Full proposals, unless excepted, must be
reviewed by at least two reviewers, which can be conducted internally
by NSF staff."[^5] NSF Staff Memorandum OD 26-02 (December 1, 2025;
reproduced by the University of Utah) encourages program officers
"to triage all proposals where panel discussion is not needed to
make a funding recommendation". It allows an award recommendation
without panel discussion when ad hoc or individual reviews suffice,
removes panelists' ability to pull triaged proposals into discussion,
and says "most panel summaries should not exceed five sentences."[^6]
NSF deferred the planned PAPPG 26-1.[^5] On June 24, 2026 it published
a draft of the Guidance on Financial Assistance (GFA), which it says
"will replace the current" PAPPG, for a 60-day public comment period
that closed August 24, 2026.[^15] The merit-review criteria themselves
are unchanged in PAPPG 24-1 and its supplements.[^5]

**Broader Impacts** is a load-bearing criterion that frequently
trips up applicants accustomed to NIH framing. NSF's current list of
example outcomes — "include, but aren't limited to" — is STEM
education, public engagement, societal well-being, a globally
competitive STEM workforce, partnerships, national security, U.S.
economic competitiveness, and research and education
infrastructure.[^9] NSF's priorities guidance tells investigators to
"prioritize the first six broader impacts goals" of the America
COMPETES Reauthorization Act of 2010. Activities addressing the
seventh goal (expanding participation of women and underrepresented
groups) "must ensure that all outreach, recruitment, or participatory
activities in NSF projects are open and available to all Americans".
Participation may be expanded "based on non-protected
characteristics, including but not limited to institutional type,
geography, socioeconomic status, and career stage."[^7] The criterion
is *not* optional window-dressing — it is one of two merit criteria,
and a weak Broader Impacts section can sink an otherwise-strong
proposal. In December 2025 the National Science Board released
*Merit Review for a Changing Landscape*. Its first policy
recommendation is to "pursue renaming the 'Broader Impacts' criterion
to 'Societal Benefits'", while maintaining and refining both current
criteria. This is a recommendation, not adopted policy.[^8]

### HHMI Investigator Program

HHMI Investigator review is structurally different from both NIH
and NSF. The selection is **person-focused** rather than
project-focused — HHMI describes the program as supporting "people,
not projects" — so candidates are evaluated on their own scientific
trajectory.[^4] Eligibility for the next competition (applications
open September 28, 2027 and close March 7, 2028) is a tenured or
tenure-track (or equivalent) faculty position at an HHMI-eligible
institution with "a minimum of 7-years post-training lab head
experience, with no upper career-stage limit", and "an active,
nationally competitive, non-mentored grant of at least three years
in duration". Appointments are renewable seven-year terms.[^4] This
replaces the narrower 2024 eligibility window described in the May
2026 version of this note.

Because selection is person-focused, the artifact reviewers evaluate
is *the scientist*, not *the proposal*.

### Private foundations (general patterns)

Foundations vary widely. Templeton emphasizes large questions
(meaning, purpose, complexity). Howard Hughes emphasizes
investigator quality (above). Gates Foundation emphasizes
measurable health outcomes and equity. Wellcome Trust emphasizes
both science and societal impact. Common patterns: **smaller
review committees** (often 5–10 people, not 20–30), **less
anonymity** (committee members may be public), **explicit alignment
checks** with the foundation's strategic priorities.

## How this informs scriptorium

**Personas, not generic "reviewer."** The `reviewer-simulation` skill,
when invoked on a grant proposal (`target_type: grant` in
`MANUSCRIPT_STATE.yaml`), should expose grant-specific personas
distinct from the manuscript-reviewer set. A minimal grant-persona
catalog:

1. **NIH Importance reviewer** — focuses on Significance and
   Innovation. Asks: is the gap real? Does this paradigm-shift
   anything? Why now? Under the 2025 scoring guidance this persona's
   verdict caps the overall assessment.
2. **NIH Rigor reviewer** — focuses on Approach. Asks: is the design
   feasible with the preliminary data? Are pitfalls identified? Are
   alternative strategies plausible? Does the timeline work?
3. **NIH Expertise reviewer** — issues sufficient / not-sufficient
   verdict on Investigator and Environment.
4. **Triage-prone reviewer** — reads only the Specific Aims page,
   abstract, and first two paragraphs of the Approach. Asks: would I
   put this in the discussed group? Under the emergency rules that
   group is about the top third, with a "competitive but not
   discussed" band below it.
5. **NSF Intellectual Merit reviewer** — broader, more
   research-direction-focused than NIH; less emphasis on
   preliminary data.
6. **NSF Broader Impacts reviewer** — focused entirely on Broader
   Impacts plan; many applicants underdevelop this and lose
   competitiveness. Should check activities against NSF's current
   priorities guidance (open to all; non-protected characteristics
   for broadening participation) rather than pre-2025 templates.
7. **HHMI-style person reviewer** — evaluates the candidate's
   scientific trajectory.

These personas mirror the empirical structure of the review process,
not just stylistic variation.

**Triage-aware critique.** The triage-prone persona is particularly
important because it mirrors the highest-leverage failure mode:
in normal operation about half of NIH applications are not
discussed, and under the emergency rules about two-thirds are not.
The aims page must carry
disproportionate signal for the application to escape streamlining.
A `specific-aims-critique` skill should be runnable in
"streamlined-or-not?" mode that simulates this reviewer. With NSF
program officers now able to decide without panel discussion, the
same mode is relevant to NSF proposals.

**Funder-type routing.** `MANUSCRIPT_STATE.yaml` should declare not
only `target_type: grant` but also `target_funder: NIH | NSF | HHMI |
foundation:<name>`. The reviewer-simulation skill should select
persona sets based on this declaration. The criteria, idiom, and
review dynamics differ enough that a single generic grant-reviewer
persona would mislead authors targeting non-NIH funders. Because
these processes changed repeatedly in 2025–2026, persona text should
name the guidance it reflects and its date.

**Panel dynamics are out of scope (for now).** Reviewer-simulation
on a single document cannot reproduce panel deliberation, anchoring,
or chair effects. The skill should be honest about this: it
simulates individual reviewers, not the panel-level outcome. The
Pier et al. finding of low inter-rater agreement makes this
limitation more honest, not less — even simulating the panel would
be modeling a noisy process whose outputs are mostly stochastic.

**Author-side only, explicitly for grants.** NIH prohibits its
reviewers from using generative AI to analyze applications or write
critiques.[^13] `reviewer-simulation` on a grant must run only on the
user's own application. A request to simulate or draft a review of
an application the user has been assigned to review should be
refused. This matches the existing non-goal of no autonomous
reviewing; the NIH notice makes it a stated funder rule for grants.

**Conservative-edit posture in grant contexts.** Grant text density
is higher than manuscript text density: every sentence in the aims
page does rhetorical work, every figure caption signals
sophistication, every preliminary-data callout shapes the
*Approach* score. Transformation skills operating on grant text
should default to even tighter preservation constraints than for
manuscripts.

## Implementation priority for scriptorium

**Verdict:** Yes (v0.4) — grant persona set for `reviewer-simulation`
and the "streamlined-or-not?" mode.

**If Yes:** Skill: the grant-archetype variant of
`reviewer-simulation` (paired with v0.4 `aims-significance-coherence`).
Phase: v0.4. Scope: the seven personas above, routed on
`target_funder`, simulating individual reviewers only (no panel
outcome, no scores mapped to funding). Required data:
`project.target_type: grant`, `target_funder`, the aims page, and the
abstract or project summary. October 2026 changes to the scope: the
triage persona uses the funder's current discussion line; the NSF
Broader Impacts persona follows NSF's 2025 priorities guidance; and
the author-side-only refusal for grants cites NOT-OD-23-149.

## Open questions / weak evidence

- The empirical literature on whether panel discussion improves or
  degrades reviewer reliability (vs. independent rating) is mixed
  and small-N. Reviewer-simulation cannot honestly claim to model
  this dynamic; it can only model individual reviewer perspectives.
- Foundation review processes are heterogeneous and poorly
  documented in the empirical literature. Persona design for
  foundation reviewers should rely on the foundation's own published
  guidance rather than generalization.
- The Simplified Review Framework (2025+) is too new for outcome
  data. Whether the factor-based scoring changes reviewer behavior
  in measurable ways is unknown.
- Whether NIH's emergency one-third discussion line, and NSF's
  two-review minimum and optional panels, change review quality is
  unstudied. Both were introduced for workload reasons.
- Whether NSF adopts the "Societal Benefits" rename, and whether the
  final Guidance on Financial Assistance changes merit-review
  language, was unknown at this update.

## References

[^1]: NIH Center for Scientific Review. What happens to your
    application during and after review?
    https://public.csr.nih.gov/ForApplicants/InitialReviewResultsAndAppeals/applicationduringafterreview .
    NIAID. First-Level Peer Review.
    https://www.niaid.nih.gov/grants-contracts/peer-review
    (both accessed 2026-10-20).

[^2]: Pier EL, Raclaw J, Carnes M, Ford CE, Kaatz A. Laughter and
    the Chair: Social Pressures Influencing Scoring During Grant
    Peer Review Meetings. *Journal of General Internal Medicine*.
    2019;34(4):513–514. doi:10.1007/s11606-018-4751-9. PMID:
    30604119. PMC: PMC6445833.

[^3]: NSF. How We Make Funding Decisions — Merit Review.
    https://www.nsf.gov/funding/merit-review . NSF Proposal & Award
    Policies & Procedures Guide (PAPPG) 24-1, Chapter III: NSF
    Proposal Processing and Review.
    https://www.nsf.gov/policies/pappg/24-1/ch-3-proposal-processing-review

[^4]: HHMI. Mid-Career & Senior Faculty Program | HHMI Investigators
    (program snapshot and eligibility).
    https://www.hhmi.org/programs/investigators . HHMI. HHMI Announces
    Five Competitions for Scientists Across Career Stages.
    https://www.hhmi.org/news/hhmi-announces-five-competitions-scientists-across-career-stages .
    HHMI. Becoming an HHMI Scientist.
    https://www.hhmi.org/programs . (The 2024 program announcement
    PDF previously cited,
    https://www.hhmi.org/sites/default/files/programs/investigator/investigator2024-program-announcement.pdf ,
    now serves the program page.)

[^5]: NSF. Policy Notice: Implementation of Policy Changes to
    Proposal and Award Policies and Procedures Guide (PAPPG) 24-1,
    Supplement 1. Issued and effective December 8, 2025.
    https://www.nsf.gov/policies/document/pappg24-1-supplement-1

[^6]: NSF Office of the Director. Staff Memorandum OD 26-02: Updates
    to Merit Review Processes. December 1, 2025. Reproduced by
    University of Utah Office of the Vice President for Research,
    "Changes to NSF Peer Review Process".
    https://www.research.utah.edu/resources-opportunities/changes-to-nsf-peer-review-process/

[^7]: NSF. Updates on NSF Priorities (FAQ on broadening
    participation and Broader Impacts).
    https://www.nsf.gov/updates-on-priorities (accessed 2026-10-20).

[^8]: National Science Board. Merit review for a new era at NSF
    (release of *Merit Review for a Changing Landscape*). December
    2025. https://www.nsf.gov/nsb/updates/merit-review-new-era-nsf .
    Policy recommendations as presented: National Science Board. NSF
    Merit Review for a Changing Landscape (slides). February 25, 2026.
    https://nsf-gov-resources.nsf.gov/files/NSB-Merit-Review-Changing-Landscape-Feb25-2026.pdf

[^9]: NSF. Broader Impacts.
    https://www.nsf.gov/funding/learn/broader-impacts (accessed
    2026-10-20).

[^10]: Reed B (CSR). Emergency Modifications to NIH Peer Review. NIH
    Extramural Nexus, November 24, 2025.
    https://grants.nih.gov/news-events/nih-extramural-nexus-news/2025/11/emergency-modifications-to-nih-peer-review .
    NIH Extramural Nexus. Continuing Modified Peer Review Processes
    for the January 2027 Council Round. September 18, 2026
    (NOT-OD-26-114).
    https://grants.nih.gov/news-events/nih-extramural-nexus-news/2026/09/continuing-modified-peer-review-processes-for-the-january-2027-council-round

[^11]: NIH. NOT-OD-25-135: Notice to Applicants of Adjustments to
    Achieve Consistency in Peer Review Contacts and Processes. 2025.
    https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-135.html

[^12]: Hesselberg J-O, Ulleberg P, Sørensen Ø, Fostervold KI,
    Ingvaldsen SH, Svege I. Why do reviewers disagree? Evidence from
    four funders and 134,000 reviews. *PLOS One*. 2026;21(9):e0356108.
    doi:10.1371/journal.pone.0356108.

[^13]: NIH. NOT-OD-23-149: The Use of Generative Artificial
    Intelligence Technologies is Prohibited for the NIH Peer Review
    Process. 2023.
    https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html

[^14]: NIH. NOT-OD-26-088: Request for Information (RFI) on Proposed
    Changes to Reporting Outcomes from NIH Peer Review. Comments due
    October 13, 2026.
    https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-088.html

[^15]: NSF. Agency Information Collection Activities: Comment
    Request; National Science Foundation Proposal/Award
    Information—NSF Guidance on Financial Assistance. *Federal
    Register* 91 FR 38030, June 24, 2026. Document 2026-12725; docket
    NSF-2026-OTR-0001.
    https://www.federalregister.gov/documents/2026/06/24/2026-12725/agency-information-collection-activities-comment-request-national-science-foundation-proposalaward .
    NSF. Request for Public Comment on Draft NSF Guidance on Financial
    Assistance (GFA). NSF GovDelivery bulletin.
    https://content.govdelivery.com/accounts/USNSF/bulletins/41d5a00

[^16]: Pier EL, Raclaw J, Kaatz A, Brauer M, Carnes M, Nathan MJ,
    Ford CE. 'Your comments are meaner than your score': score
    calibration talk influences intra- and inter-panel variability
    during scientific grant peer review. *Research Evaluation*.
    2017;26(1):1–14. doi:10.1093/reseval/rvw025. PMID: 28458466.
