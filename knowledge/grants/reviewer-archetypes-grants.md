# Reviewer archetypes for grant review

*Last updated: 2026-05-17*

## Synthesis

Grant review is structurally different from manuscript review, and a
grant-reviewer simulation skill should not be a re-skinned
manuscript-reviewer simulation. The differences are not stylistic.
They are: **fewer reviewers per artifact** (typically 1–3 primary
reviewers for a grant, vs. 2–4 for a manuscript), **panel
deliberation rather than independent recommendations** (study
sections discuss; manuscript reviewers do not), **anchored scoring
distributions** (study-section reviewers calibrate against the
section's recent score distribution), **selection pressure from
triage** (~50% of grant applications are streamlined without
discussion; manuscripts are rarely silently desk-rejected after
review begins), and **explicit criterion-based scoring** (NIH and NSF
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

For scriptorium, the practical implication is that the planned
`reviewer-simulation` skill should expose grant-specific personas
distinct from manuscript-specific ones, and that the orchestrator
must select personas based on `target_type` in
`MANUSCRIPT_STATE.yaml` (grant proposal vs manuscript).

## Evidence

### NIH study-section dynamics

**Composition.** A typical NIH study section meeting reviews 50–100
applications across 1.5–2 days. Each application is assigned to
2–3 primary reviewers (one designated primary, one or two
secondary/tertiary). Roughly **50% of applications are
streamlined** ("triaged") and not discussed at the meeting; they
receive written critiques and individual reviewer scores but no
priority/percentile score. Streamlining is based on reviewer
pre-meeting scores; any single reviewer can request a streamlined
application be discussed.[^1]

**Discussion.** For each discussed application, ~15–20 minutes are
typically allotted. The discussion is anchored by the primary
reviewers' pre-meeting scores. After discussion, every voting
member of the study section assigns a final overall impact score.
The reported priority score is the mean of these scores; the
percentile is computed across the current and recent meetings of
the same study section.

**Five-criterion scoring (regulatory).** Significance, Investigator,
Innovation, Approach, Environment. Each is scored 1–9. Under the
Simplified Framework (effective 2025): Factor 1 (Importance =
Significance + Innovation), Factor 2 (Rigor & Feasibility =
Approach), Factor 3 (Expertise & Resources = Investigator +
Environment, evaluated as sufficient/not sufficient).

**Empirical reviewer reliability.** Pier et al. (2018) showed
essentially no inter-rater agreement on the same applications when
reviewers worked independently; see [[grant-writing-evidence]]. The
panel discussion *may* improve calibration somewhat, but the
underlying noise is high.

**Anchoring and panel effects.** Social-pressure effects in panel
deliberation have been documented. One PMC-indexed study,
*Laughter and the Chair* (Hosseini et al., 2019), examined social
pressures during grant peer-review meetings and identified
identifiable patterns of conformity, anchoring to the chair, and
deference to the primary reviewer. `[TODO verify]` full citation.[^2]

### NSF panel dynamics

**Criteria.** Two merit-review criteria: **Intellectual Merit** and
**Broader Impacts**. Both apply to every proposal. NSF reviewers are
asked to consider five elements per criterion: potential to advance
knowledge / benefit society; creative or transformative concepts;
soundness of plan; mechanism for assessing success; qualifications
of the team; adequacy of resources.[^3]

**Format.** NSF panel review combines individual ad hoc reviews with
a panel meeting. Reviewers produce written reviews; the panel
discusses and groups proposals into "Highly Competitive," "Competitive,"
"Recommend for Funding," etc. The panel does not assign numerical
scores in the NIH style; recommendations are categorical, and the
final funding decision rests with the program director.

**Broader Impacts** is a load-bearing criterion that frequently
trips up applicants accustomed to NIH framing. Examples of
acceptable Broader Impacts: STEM education, public engagement,
workforce development, infrastructure improvement, partnerships,
under-served-population research. The criterion is *not* optional
window-dressing — it is one of two merit criteria, and a weak
Broader Impacts section can sink an otherwise-strong proposal.

### HHMI Investigator Program

HHMI Investigator review is structurally different from both NIH
and NSF. The selection is **person-focused** rather than
project-focused: candidates are evaluated on their own scientific
trajectory, with applicants required to submit their five most
significant publications from the past 5–7 years. Eligibility
requires tenured or tenure-track position (assistant professor or
higher), 5–15 years post-training, an active national peer-reviewed
research grant (e.g., R01), and ≥75% research effort.[^4]

The HHMI review process: review by Scientific Review Board members
(distinguished scientists), semifinalist video presentations,
virtual symposium with Q&A. The artifact reviewers evaluate is
*the scientist*, not *the proposal*.

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
   anything? Why now?
2. **NIH Rigor reviewer** — focuses on Approach. Asks: is the design
   feasible with the preliminary data? Are pitfalls identified? Are
   alternative strategies plausible? Does the timeline work?
3. **NIH Expertise reviewer** — issues sufficient / not-sufficient
   verdict on Investigator and Environment.
4. **Triage-prone reviewer** — reads only the Specific Aims page,
   abstract, and first two paragraphs of the Approach. Asks: would I
   bring this back from streamlining?
5. **NSF Intellectual Merit reviewer** — broader, more
   research-direction-focused than NIH; less emphasis on
   preliminary data.
6. **NSF Broader Impacts reviewer** — focused entirely on Broader
   Impacts plan; many applicants underdevelop this and lose
   competitiveness.
7. **HHMI-style person reviewer** — evaluates the candidate's
   scientific trajectory and most-significant-papers package.

These personas mirror the empirical structure of the review process,
not just stylistic variation.

**Triage-aware critique.** The triage-prone persona is particularly
important because it mirrors the highest-leverage failure mode:
~50% of applications are streamlined. The aims page must carry
disproportionate signal for the application to escape streamlining.
A `specific-aims-critique` skill should be runnable in
"streamlined-or-not?" mode that simulates this reviewer.

**Funder-type routing.** `MANUSCRIPT_STATE.yaml` should declare not
only `target_type: grant` but also `target_funder: NIH | NSF | HHMI |
foundation:<name>`. The reviewer-simulation skill should select
persona sets based on this declaration. The criteria, idiom, and
review dynamics differ enough that a single generic grant-reviewer
persona would mislead authors targeting non-NIH funders.

**Panel dynamics are out of scope (for now).** Reviewer-simulation
on a single document cannot reproduce panel deliberation, anchoring,
or chair effects. The skill should be honest about this: it
simulates individual reviewers, not the panel-level outcome. The
Pier et al. finding of low inter-rater agreement makes this
limitation more honest, not less — even simulating the panel would
be modeling a noisy process whose outputs are mostly stochastic.

**Conservative-edit posture in grant contexts.** Grant text density
is higher than manuscript text density: every sentence in the aims
page does rhetorical work, every figure caption signals
sophistication, every preliminary-data callout shapes the
*Approach* score. Transformation skills operating on grant text
should default to even tighter preservation constraints than for
manuscripts.

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

## References

[^1]: NIH Center for Scientific Review. First-Level Peer Review.
    https://public.csr.nih.gov/ForApplicants/InitialReviewResultsAndAppeals/applicationduringafterreview .
    NIAID. NIH Peer Review Process and Triage.
    https://www.niaid.nih.gov/grants-contracts/peer-review .

[^2]: Hosseini M, Eckmann P, Bierer BE. Laughter and the chair:
    Social pressures influencing scoring during grant peer review
    meetings. *PMC6445833* (2019). `[TODO verify]` exact journal /
    DOI from PMC entry.

[^3]: NSF. How We Make Funding Decisions — Merit Review.
    https://www.nsf.gov/funding/merit-review . NSF Proposal & Award
    Policies & Procedures Guide (PAPPG), current edition.

[^4]: HHMI. Investigator Program Announcement (2024).
    https://www.hhmi.org/sites/default/files/programs/investigator/investigator2024-program-announcement.pdf .
    HHMI. Becoming an HHMI Scientist.
    https://www.hhmi.org/programs .
