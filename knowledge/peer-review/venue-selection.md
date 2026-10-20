# Venue selection: how researchers choose where to submit

*Last updated: 2026-10-20*

## Synthesis

Venue selection is the highest-stakes decision in the submission
workflow and the one most often made by intuition, lab tradition,
or career incentive rather than by deliberate fit assessment. The
cost of misfit is measurable. A desk rejection at a top journal
often arrives within about a week [3, 8]. But each failed attempt
adds reformatting and a fresh queue, and a rejection after review
comes later: at *Science* in 2025 the median time to a first
post-review decision was 64 days [8]. The best large-scale data on
submission trajectories complicate the folk story that "most authors
over-aim". In a survey covering 923 biology journals, about 75% of
published articles had been submitted first to the journal that
published them. High-impact journals published proportionally more
articles resubmitted from elsewhere, and those resubmissions were
cited more than first-intent submissions [2]. The pattern that does hold is
that venue choice is rarely taught explicitly and the signals
authors get (impact factor, lab reputation, "where my advisor
publishes") are weakly correlated with fit.

A venue-fit framework requires answering several distinct
questions, not just one. **Scope fit** asks whether the manuscript's
topic falls inside what the journal publishes. **Audience fit**
asks whether the readership the journal serves is the audience
the author wants to reach. **Methodological fit** asks whether the
methods used are ones the journal's reviewers know how to evaluate
fairly. **Novelty fit** asks whether the contribution is in the
tier the journal expects (incremental advances, mechanistic
syntheses, paradigm-shifting findings — these aren't synonymous
across venues). **Significance fit** asks whether the work as
framed meets the editor's expected bar for *significance to that
journal's audience* — a separate question from significance in
the abstract sense. *Nature*, for example, says that "the judgement
about which papers will interest a broad readership is made by
*Nature*'s editors, not its referees", and that this initial
judgement "is not a reflection on the technical validity of the
work" [3].

For scriptorium, the practical consequence is that venue-fit
assessment must be multi-axis. A skill that returns "submit to *X*"
without naming the axes on which the assessment was made (and where
it caveats) is a black-box recommendation that the author can't
audit or override. The right output shape is tiered with explicit
per-axis reasoning, so the author sees the fit being assessed and
can disagree with any specific axis.

## Evidence and frameworks

### Journal-fit frameworks in the editorial guides

The journal-selection question has been treated extensively in the
editorial-guidance literature, with consistent recommendations
across decades. Bahadoran et al.'s 2020 guide [4] is a
representative modern example. It notes that "submitting to an
inappropriate journal is one of the most common reasons for fast
rejection". It groups the factors into the journal's characteristics
(prestige, performance, publishing model, acceptance possibility,
specialty), the manuscript's characteristics (relevance to the
journal's aim and scope, novelty, soundness of methods, potential
impact), and the authors' own priorities and limitations. Earlier
work by Day & Gastel [5] establishes the same shape with different
vocabulary: aim at the journal whose readers are the audience for
your contribution, not the journal whose reputation is the audience
for your CV.

The convergence across editorial guides is striking and worth
naming: **scope fit dominates everything else**. A manuscript on
clinical metabolomics submitted to a structural biology journal
will be desk-rejected regardless of quality; a methodologically
weak paper in-scope at a specialty journal will get a revision
chance. Authors who internalise scope-fit-first avoid the most
common desk-rejection pattern [4].

Once a paper is in scope, the reasons reviewers give for rejecting
it are mostly about methods and presentation. In Bordage's content
analysis of reviewer comments on 151 manuscripts submitted to a
medical-education conference, the most frequent reasons for
rejection were inappropriate or incomplete statistics,
overinterpretation of results, inappropriate or suboptimal
instrumentation, and samples that were too small or biased [1].
That is the evidence behind treating methodological fit as its own
axis, separate from scope (the generalisation from one
medical-education venue to journals at large is researcher
inference).

### Author-venue mismatch as a measurable phenomenon

The mismatch is documented empirically, but it is smaller than the
folk story suggests. Calcagno et al. surveyed the submission
histories of articles published in 2006–2008 across 923 biology
journals. About 75% of published articles had gone first to the
journal that published them; the remaining quarter arrived after a
rejection elsewhere [2]. High-impact journals published
proportionally more of these resubmissions, and resubmissions
received significantly more citations than first-intent submissions
[2]. So the "higher-prestige journal → rejection → lower-tier
journal" cascade is real but describes a minority of published
papers. The data cannot see papers that were never published.

Turnaround data are journal-specific. The *Science* family publishes
its medians. For *Science* in 2025 these were 8 days to a first
decision, 64 days to a first post-review decision, and 184 days from
submission to acceptance [8]. We did not verify a current
cross-journal figure for total cycle time, so this note no longer
states one. Each rejection adds its own round of these delays.

The decision pattern that produces this is rational from one
narrow perspective (try the higher-prestige venue first — the
expected value of a publication there outweighs the latency cost
if hit-rate is high enough) and irrational from another (most
authors over-estimate hit-rate, and the cumulative latency from
serial rejection eats into productivity). Realistic tiering — with
explicit "this is your defensible upper tier given the manuscript
as it currently reads" framing — is the intervention that lets
authors make this trade-off deliberately rather than by default.
(The claim that most authors over-estimate hit-rate is researcher
inference; [2] measures where papers end up, not authors'
expectations.)

### Solomon and Björk on open-access venue selection

Solomon and Björk surveyed 1,038 authors who had recently published
in 74 APC-charging open-access journals; 429 (41%), from 69 of the
journals, completed the survey [12]. "Fit, quality, and speed of
publication were the most important factors in the authors' choice
of a journal"; open access itself "was less important but a
significant factor for many authors". Sources of APC funding
differed widely across disciplines, and journals with impact
factors charged higher APCs [12]. Their companion study of 1,370
APC-charging journals in DOAJ found an average APC of about US$906
in 2010, ranging from $8 to $3,900. Journals with high impact
factors from major international publishers charged the most [6].

For a venue-fit skill, this means the recommendation must surface
the OA / cost / indexing axes alongside scope and audience — a
"perfect fit" venue with a high APC is not a fit for
an author on a hard cap. The right behaviour is to let the author
declare their constraints (`open_access_required`, `max_apc_usd`,
`indexing_requirements`) and have the recommendation respect them
as hard filters rather than soft preferences.

Since 2025 these constraints increasingly come from funders rather
than from author budgets. Wellcome funds APCs only in fully
open-access journals indexed in DOAJ. HHMI no longer pays hybrid
APCs. Gates pays no APCs. NIH has proposed limits on allowable
publication costs; the most recent dated status review (March 2026)
found none finalised, and an October 2026 check of NIH's policy
notices found no final notice either. The sources are in
[[preprint-landscape]]. Indexing status can also change
because of a journal's model, not its quality: after Web of Science
put eLife on hold in 2024, eLife became a partially indexed journal
that is not eligible for a Journal Impact Factor [11]. An
`indexing_requirements: [JIF]` constraint would now exclude it.

### Career-stage interactions

Less well-documented but real in practice: career stage interacts
with venue choice in ways that change what counts as a defensible
recommendation. Early-career researchers benefit asymmetrically
from publications in well-respected specialty venues — first-author
papers in *J Biol Chem* or *J Neurosci* carry weight on faculty
search committees that *Nature* one-off coverage does not, because
field-recognised specialty publications signal a sustained
disciplinary commitment. This is widely held in informal mentorship
advice. The 2026-10 refresh did not find a published analysis of CV
tier-signalling in faculty hiring, so treat it as practitioner
judgement rather than evidence. Established researchers can afford the higher
expected latency of prestige-tier attempts because the marginal
publication is less career-defining.

Author characteristics also affect outcomes directly at elite
venues. At *Science* and *Science Advances*, editorial-stage
decisions show selection associated with institutional prestige,
team size, topic and country, and these associations are stronger
at the editorial stage than at peer review [9]. This is a reason to
calibrate the "Stretch" tier against the author's context, not only
the manuscript (researcher inference). It is equally a reason never
to present that calibration as a judgement of the work's merit.

A venue-fit skill that ignores career stage produces the same
recommendation for a PhD student and a department chair, which is
the wrong recommendation for at least one of them. Pub history
(when provided) is the proxy for career stage that's safe to use
— see the cautions in
[[journal-selection-bias-and-pub-history]] (proposed; not yet
written).

### The cover letter as a fit-signal channel

A frequently-underemphasised point in the editorial-guidance
literature: the cover letter is the channel through which the
author tells the editor *why this venue*. Editorial guides treat
journal choice and the cover letter together for this reason [10].
In practitioner experience, a cover letter that articulates scope
fit, audience fit, and significance fit explicitly survives triage
more often than one that names the work without naming the fit.
This is not measured in the sources checked here. For a venue-fit
skill, this
matters because the recommendation's reasoning *is* what the
author will (re)use in the cover letter — recommendations that
spell out fit reasoning give the author a draft cover-letter
argument as a side effect.

## How this informs scriptorium

For the `venue-fit` skill specifically:

1. **Multi-axis assessment.** The skill must name and assess on
   each load-bearing axis (scope, audience, methodological,
   novelty, significance, OA/cost/indexing if the author declared
   constraints). A single-axis recommendation ("good fit" without
   decomposition) is a black box. The author needs to see the per-
   axis assessment to override on any single axis they disagree
   with.

2. **Tiered output: likely fit / stretch / probably premature.**
   Maps to the empirical pattern that a sizeable minority of papers
   reach their final venue only after a rejection elsewhere [2].
   Naming each tier explicitly — including the venues the manuscript
   doesn't yet support — lets the author choose a stretch attempt
   deliberately rather than by default. The skill should not tell
   authors that "most authors over-aim"; the evidence does not
   support that wording.

3. **Per-venue specifics, not generic categories.** A
   recommendation that says "submit to a specialty endocrinology
   journal" is not actionable; "submit to *Journal of
   Endocrinology* (Society for Endocrinology, IF ≈ 4.2, accepts
   methodology papers with clinical translation, recent
   single-cell papers include [example])" is. The skill grounds
   recommendations in specific recent papers from the venue when
   possible, because that's what a careful submitter actually
   does — read what the venue published recently to test fit
   before committing.

4. **Surface the cover-letter argument as a side effect.** The
   "why this venue" reasoning the skill emits per-tier is exactly
   what the cover letter needs. Calling this out in the skill's
   output ("the reasoning above is your draft cover-letter
   argument") is a useful UX nudge.

5. **OA / cost / indexing as hard filters when declared.**
   Solomon and Björk's survey puts fit, quality and speed first and
   OA second [12]. Cost and indexing still become hard limits when
   the author or the funder imposes them. If the author declares
   constraints, the skill filters before tiering rather than
   recommending and then apologising. Funder APC rules (Wellcome,
   HHMI, Gates, proposed NIH caps) are constraints of this kind.
   Before submission the author should still run the venue through
   the Think.Check.Submit checklist [7].

6. **Career stage via pub history is calibration only, never
   anchor.** See the bias-management discussion in the venue-fit
   skill spec. The list comes from manuscript fit; the tiering
   reflects feasibility given the author's track record. Never
   the other way around.

## Implementation priority for scriptorium

**Verdict:** Direct grounding for the `venue-fit` skill (v0.2).
This note is the primary evidence base; predatory publishing and
preprints get their own notes
([[predatory-publishing]], [[preprint-landscape]]).

**2026-10-20 refresh:** the verdict holds. The tiered output is
still the right shape, but its stated rationale changes. Calcagno et
al. show that about three-quarters of published papers went to
their final venue first [2]. Skill copy that says authors
characteristically over-aim should be softened. Funder APC rules and
JIF eligibility (eLife) are new inputs to the hard-filter step
[11]. Tracked for the skills pass.

**Why useful context anyway:**

- The multi-axis assessment shape this note recommends is the
  right output shape for any venue-fit skill, not just
  scriptorium's. Documenting the framework here lets future
  forks / re-implementations preserve the property even if the
  surrounding skill code changes.

- The "tiered with explicit per-axis caveats" pattern composes
  naturally with `desk-rejection-risk` (which takes a *declared*
  venue and assesses risk against it). The venue-fit skill
  recommends; desk-rejection-risk pressure-tests the
  recommendation. The two are a natural pair.

- Cover-letter argument as a side effect points toward a future
  v0.3 `cover-letter-draft` skill that takes the venue-fit
  reasoning and produces a structured first draft. That skill is
  pure transformation of declared work — the venue, the
  reasoning, and the manuscript are all declared — so it sits
  inside the [[declared-work-scope]] cleanly.

**Condition that would flip the implementation priority:** if
real-use feedback shows authors ignore the tiered output and just
read the "Likely fit" section, the framework may need to
restructure around the "decision support" function rather than the
"exhaustive assessment" function. Worth measuring once the skill
has been used on a few real submissions.

## Cross-references

- [[editorial-decision-making]] — desk-rejection rates and the
  patterns editors triage on. Closely paired; venue-fit
  recommends, editorial-decision-making informs what the editor
  at the recommended venue is likely to do.
- [[significance-positioning]] — the significance-framing axis of
  venue fit. Stretch venues require significance framing this
  note's literature underwrites.
- [[predatory-publishing]] — the refusal layer of venue-fit. No
  recommendation list includes a flagged venue.
- [[preprint-landscape]] — the preprint dimension of venue
  selection, and the funder APC and preprint rules.
- [[common-critiques-taxonomy]] — what reviewers at any venue tend
  to flag; informs the methodological-fit axis.
- [[declared-work-scope]] — the project-wide convention. Venue-fit
  operates on declared work and refuses to invent claims about the
  manuscript to make it fit a venue.

## References

[1] Bordage, G. (2001). Reasons reviewers reject and accept
manuscripts: the strengths and weaknesses in medical education
reports. *Academic Medicine*, 76(9), 889–896.
DOI: 10.1097/00001888-200109000-00010. PMID: 11553504. (Reviewers'
reasons for rejecting and accepting medical-education manuscripts;
background for the per-axis assessment framework. The earlier
annotation's claim about the order of frequency of reason clusters
was not re-verified in the 2026-10 refresh and has been dropped.
The paper analyses reviewer comments, not editor triage, so it is
no longer cited for the scope-fit, over-aiming or cover-letter
claims it was previously attached to.)

[2] Calcagno, V., Demoinet, E., Gollner, K., Guidi, L., Ruths,
D., & de Mazancourt, C. (2012). Flows of research manuscripts
among scientific journals reveal hidden submission patterns.
*Science*, 338(6110), 1065–1069. DOI: 10.1126/science.1227833.
PMID: 23065906. (Empirical submission trajectories across 923
biology journals. About 75% of published articles were submitted
first to the publishing journal. Resubmissions were cited more. The
earlier annotation said the paper "demonstrates the
over-aim-then-cascade pattern at scale", which overstates it.)

[3] *Nature*. (Ongoing.) Editorial criteria and processes.
<https://www.nature.com/nature/for-authors/editorial-criteria-and-processes>.
(Replaces "Lin, Frey & Wu 2022". That DOI,
10.1038/s41586-023-06767-1, is Lin, Frey & Wu (2023), "Remote
collaboration fuses fewer breakthrough ideas", *Nature* 623,
987–991, which does not support the significance-fit claim it was
cited for.)

[4] Bahadoran, Z., Mirmiran, P., Kashfi, K., & Ghasemi, A. (2020).
Scientific publishing in biomedicine: how to choose a journal?
*International Journal of Endocrinology and Metabolism*, 19(1),
e108417. DOI: 10.5812/ijem.108417. PMID: 33815519. (Published online
25 November 2020; issue dated January 2021. Replaces "Misra
& Agarwal 2017, *J Korean Med Sci* 32(7):1064–1070". That DOI is not
registered, and PMID 28581262 is a different JKMS paper.)

[5] Day, R. A., & Gastel, B. (2016). *How to Write and Publish a
Scientific Paper* (8th ed.). Cambridge University Press. ISBN:
9781316640432. (The canonical writing-and-publishing manual;
chapter on journal selection is brief but the principle of
"aim at the journal whose readers are the audience for your
contribution" is the foundational framing.)

[6] Solomon, D. J., & Björk, B.-C. (2012). A study of open
access journals using article processing charges. *Journal of
the American Society for Information Science and Technology*,
63(8), 1485–1495. DOI: 10.1002/asi.22673. (APC levels across
1,370 DOAJ journals in 2010. Author-choice findings are in [12].)

[7] Think.Check.Submit. (Ongoing.) Checklist for choosing
journals. <https://thinkchecksubmit.org/>. (Community-maintained
practical checklist; primary reference for the "what to verify
before submitting" question. Sister resource to
[[predatory-publishing]].)

[8] *Science* / AAAS. (Updated semi-annually; 2025 data.) Journal
metrics. <https://www.science.org/content/page/journal-metrics>.
(The page blocked automated fetching during the 2026-10 refresh,
its independent re-check and the evidence audit. The only copies of
the 2025 figures found were trade-press copies (Manusights blog
posts) and search-index summaries, the same class of source this
refresh dropped for older desk-rejection rates. The turnaround
medians cited here, and the 85% not-externally-reviewed figure used
in [[editorial-decision-making]], need a manual read of science.org
before the skills pass relies on them.)

[9] Zhang, S., LaBerge, N., McElhiney, Q., Larremore, D. B., &
Clauset, A. (2026). Editorial and peer review dynamics at elite
general science journals. *Science Advances*, 12(29), eaec0494.
DOI: 10.1126/sciadv.aec0494. PMID: 42455887.

[10] Nicholas, D. (2019). How to choose a journal and write a
cover letter. *Saudi Journal of Anaesthesia*, 13(Suppl 1), S35–S41.
DOI: 10.4103/sja.SJA_691_18. PMID: 30930718.

[11] eLife. (2024, addendum 2025). Changes to eLife's indexing
status in Web of Science and Scopus.
<https://elifesciences.org/inside-elife/ae620829/changes-to-elife-s-indexing-status-in-web-of-science-and-scopus>.

[12] Solomon, D. J., & Björk, B.-C. (2012). Publication fees in
open access publishing: sources of funding and factors influencing
choice of journal. *Journal of the American Society for Information
Science and Technology*, 63(1), 98–107. DOI: 10.1002/asi.21660.
