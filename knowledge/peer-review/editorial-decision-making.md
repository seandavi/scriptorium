# Editorial decision-making and desk rejection

*Last updated: 2026-10-20*

## Synthesis

The peer-review process most authors imagine — careful reading by
two or three experts, weighed by an editor against a clear standard —
is not what most submissions experience. At high-impact journals,
the modal outcome is **desk rejection**: an editorial-stage decision
made within days or weeks, without the paper being sent for full
peer review. The journals that
publish their own figures make this concrete. In 2025 *Science* sent
15.0% of its research submissions for external review and accepted
5.3%, with a median of 8 days to first decision [9]. *Nature* states
that about 8% of submissions are accepted and that "most submissions
are declined without being sent out for peer review" [4]. *NEJM*
reports publishing about 5% of original research submissions [10].
Comparable primary figures for mid-tier and mega-journals are scarce.
The decision is made by an editor or associate editor
reading the cover letter and abstract, sometimes glancing at the
figures, and applying a small number of triage heuristics: scope fit,
methodological adequacy detectable from the abstract, novelty, and
language quality. "Not peer reviewed" does not always mean
editor-only triage, though. At *Science*, editors summarily rejected
28.1% of submissions in a five-year dataset and sent 69.5% to the
Board of Reviewing Editors (BoRE), outside experts who give rapid
advice; editors then declined 75% of those after BoRE advice [12].
So most *Science* submissions that never reach full peer review are
still declined with outside scientific input. A large 2026 analysis of editorial triage
(110,303 submissions to *Science* and *Science Advances*) also finds
selection associated with factors the manuscript cannot change —
institutional prestige, team size, topic and country — and these
associations are stronger at the editorial stage than at peer
review [12].

For scriptorium, this matters because the value proposition includes
*catching what would trigger desk rejection before submission*. That
is a concrete, testable claim — much sharper than "improving the
manuscript" — and it is the most asymmetric intervention an
agentic editor can offer: a single weekend of pre-submission audit
can save months of round-trip latency. Operationalising it means
building (or budgeting in `reviewer-simulation`) a **desk-rejection
risk audit** that probes a small number of high-leverage triage
signals.

## Evidence and frameworks

### How editorial decisions actually get made

Smith's 2006 JRSM essay [2] is the most-cited polemic on peer
review's empirical weaknesses, and the most useful concise account
of the editorial side. Smith — then editor of BMJ for 13 years —
argues that peer review is "a flawed process at the heart of
science and journals", that the evidence base for peer review's
effectiveness is thin, and that editors retain substantial weighting
authority even when reviews are formally the basis of decision.

Bornmann's broader review of peer-review research [1] surveys
studies of inter-reviewer agreement (consistently low), editor
weighting of reviewer recommendations (variable), and decision
predictors. His meta-analysis with Mutz and Daniel pooled 70
reliability coefficients from 48 studies of journal peer review and
found low inter-rater reliability (mean ICC/r² = .34, mean Cohen's
kappa = .17) [8]. The bottom line: reviewer recommendations are noisy
inputs to an editorial decision that is itself partly judgement.

### Desk-rejection rates and triage criteria

Quantitative data is uneven. Most journals do not publish how many
submissions they decline before review; the figures below are the
ones journals disclose themselves:

- ***Science*** (2025, research articles, reports and research
  resources): 15,088 submissions; 15.0% externally reviewed; 5.3%
  accepted; median 8 days from submission to first decision [9]. In
  other words, about 85% of submissions were not sent to full peer
  review. That is not the same as editor-only triage. In Zhang et
  al.'s five-year *Science* data, editors summarily rejected 28.1%
  of 68,047 submissions and sent 69.5% to the Board of Reviewing
  Editors, then declined 75% of those after BoRE ratings and advice
  [12]. (The 2025 figures could only be read through trade-press and
  search-index copies of the *Science* page; see [9].)
- ***Nature***: "only about 8% of submitted manuscripts will be
  accepted for publication. Most submissions are declined without
  being sent out for peer review." Authors are "usually informed
  within a week" if the paper is not being considered [4].
- ***NEJM***: about 5% of original research submissions are
  published [10]. NEJM does not disaggregate desk rejection from
  later rejection in this statement.
- Mid-tier subject journals and open-access mega-journals (*PLOS
  ONE*, *Scientific Reports*) are widely described as desk-rejecting
  far less, with most filtering at peer review. We did not find
  primary, journal-disclosed figures for them, so this note no
  longer gives percentages for these tiers.

*Nature* also publishes the criteria its editors apply before
review: results that "seem novel, arresting (illuminating,
unexpected or surprising)", with "both immediate and far-reaching
implications". It states that "the judgement about which papers will
interest a broad readership is made by *Nature*'s editors, not its
referees", and that the initial decision "is not a reflection on the
technical validity of the work" [4]. This is direct evidence that
significance calibration is an editor-stage gate, separate from
technical soundness.

The dominant triage criteria reported by editors:

1. **Scope mismatch.** The paper is competent but wrong for the
   venue (basic-science result at a clinical journal; method
   paper at an applications journal).
2. **Insufficient novelty or significance.** Detected from the
   abstract — "we extend X to a new dataset" rarely survives
   triage at a flagship journal.
3. **Methodological inadequacy detectable from the abstract.**
   Small N, no controls, missing reporting-guideline elements
   ([[reporting-guidelines]]) flagged at a glance.
4. **Language quality.** Severe ESL issues (see
   [[esl-writers-swales-hyland]]) are read by editors as a
   competence signal even when the science is sound — an
   uncomfortable reality that drives the EAL editing market.
5. **Cover letter and significance positioning.** A cover letter
   that fails to articulate why the work matters here, now, for
   this venue is itself a desk-reject trigger; see
   [[significance-positioning]] and [[nih-significance-patterns]].

### Who gets past the desk: selection beyond the manuscript

Zhang et al. (2026) released deidentified data on 110,303
submissions over five years at *Science* and *Science Advances*
and analysed the editorial-review and peer-review stages
separately [12]. They report "strong selective effects associated
with higher institutional prestige, larger team size, and certain
topics and countries"; a small but significant advantage for
corresponding authors who are men at *Science*; and a significant
disadvantage for authors based in China. These associations "are
generally stronger in editorial review than in peer review, even as
final editorial decisions correlate strongly with reviewer advice"
[12].

Two consequences follow (researcher inference). First, desk-stage
outcomes are not a pure function of manuscript quality, so a
pre-submission audit can lower risk but cannot remove it. Second,
the editorial stage is where most of the non-manuscript variance
enters, which strengthens the case for treating desk triage as its
own problem rather than as early peer review.

### Editors and associate editors

The "editor's introduction" papers in journals like *eLife* and
*Annual Reviews* describe the assignment-to-AE step: a handling
editor reads the abstract, identifies an associate editor (AE)
with topical fit, and either triages or hands off. AE selection
is itself a high-leverage decision — AEs choose reviewers, weight
their reports, and write the decision letter.

NIH study sections are the grant-review analogue. A small number of
assigned reviewers (usually three) review each application in
detail and report to the panel; panel members' individual scores
are anchored to the scores those assigned reviewers declare
publicly [7]. In constructed NIH-style panels, discussion made
reviewers within a panel agree more but made different panels agree
less, and "score calibration talk" played a pivotal role in that
variability [11]. The parallel matters: in both peer review and
grant review, the person who introduces the work to the deciding
body has disproportionate influence on outcome (researcher
inference from [7, 11]; the journal-AE side of the analogy is not
directly measured). This is why
[[reviewer-archetypes-grants]] applies as much to journal AEs as
to grant reviewers — the AE is functionally the first reviewer.

### Open / transparent decision-making

Several journals have experimented with transparency to test
whether visibility changes review quality or outcome:

- ***eLife***: from 2023 eLife stopped making accept/reject
  decisions after peer review. Papers it sends for review are
  published as Reviewed Preprints with public reviews and an eLife
  Assessment [13]. An earlier opt-in trial (submissions in 2018,
  final outcomes reported in 2019) let 313 authors choose a process
  in which eLife committed to publish any paper it sent for in-depth
  review; 20.8% of trial papers were accepted against 14.9% in the
  regular process, and median time to acceptance was 175 days
  against 138 [6]. So the trial did raise the final acceptance rate,
  even though more trial papers were rejected before review. The
  model has had an indexing cost: Web of Science put eLife on hold in
  October 2024, and eLife now provides only a partial feed (papers
  assessed as "solid" or better), which makes it ineligible for a
  Journal Impact Factor [15].
- ***BMJ***: publishes signed reviews and the full prepublication
  history. In the 1999 BMJ randomised trial [3], asking reviewers
  to have their identity revealed to authors had no significant
  effect on review quality, the publication recommendation, or the
  time taken to review, but it made reviewers more likely to decline
  to review (35% v 23%).
- ***Nature***: for manuscripts submitted from 16 June 2025, every
  paper published as a research article carries its peer-review file
  (reviewer reports and author responses). Reviewers stay anonymous
  unless they choose to be named. This replaced the opt-in
  transparent review *Nature* had offered since 2020, so the share
  of *Nature* papers with a public review file grows over time
  rather than switching over at once [14].
- ***PLOS***: opt-in publication of peer-review history; modest
  uptake.

The pattern: making review visible has not, on the trial evidence,
changed review quality much. The constraint on review quality is
*time and expertise*, not opacity. Transparency now reaches the
author side too: under *Nature*'s 2025 policy, reviewer reports on
newly submitted papers that are accepted become public. Changing the
decision rule itself, as eLife did, changes outcomes and has
consequences for indexing.

### Why this matters for scriptorium

The value proposition implicit in
"`reviewer-simulation` as a sparring partner before submission"
is two distinct services:

1. **Reviewer-style critique** — simulated reviewer reports of
   the kind the work would receive *if it survives triage*.
2. **Desk-rejection risk audit** — a pre-triage check that flags
   the small number of high-leverage signals editors actually
   use to triage.

These are different products. The second is potentially much more
asymmetric: catching a scope mismatch before submitting to *Nature*
saves a desk-rejection cycle (*Nature* says authors are "usually
informed within a week" [4]) plus the reformatting and fresh queue
at the next venue; catching a reviewer-style critique saves perhaps
2 weeks on a second round. (Corrected in the 2026-10 audit: the
earlier "6+ weeks of round-trip" figure was unsourced and conflicted
with *Nature*'s own turnaround statement.) The desk-rejection audit
should be cheap, fast, and focused on a small triage checklist —
not a comprehensive review.

## How this informs scriptorium

1. **Build a `desk-rejection-risk` audit, either as its own v0.2
   skill or as a flagged output mode of `reviewer-simulation`.**
   The checklist is short:
   - Does the abstract (and cover letter, if present) articulate
     a finding that fits the target venue's scope?
   - Are reporting-guideline elements ([[reporting-guidelines]])
     present in the abstract for the relevant study type?
   - Are language-quality issues likely to trigger an editor's
     "send back for English editing" reflex?
   - Does the significance positioning
     ([[significance-positioning]]) match the venue's calibration
     (clinical relevance for *NEJM*; mechanistic insight for
     *Nature*; method novelty for ML venues)?
   - Are any policy-compliance issues likely to be caught at
     triage (ICMJE authorship; AI-disclosure; data-sharing;
     ethics statements)? The ICMJE Recommendations ask authors to
     describe AI use in both the cover letter and the manuscript
     (since the May 2023 update), and, when AI was used to conduct
     the study, to give the tool, version and prompts in the Methods
     (added in January 2024 [16]). The January 2026 update
     consolidated the AI guidance into a top-level Section V
     covering authors, reviewers and editors [5]. These are
     established requirements, not new 2026 ones.

2. **Use `MANUSCRIPT_STATE.target_venue` aggressively.** A
   desk-rejection-risk audit is incoherent without a target.
   Skills should refuse to run (or run with a warning) if
   `target_venue` is empty.

3. **Honest reporting.** The skill should distinguish
   *desk-rejection signals* (editorial triage heuristics) from
   *reviewer concerns* (peer-review-stage critique). These map
   to different stages of the decision pipeline and should be
   reported separately. It should also say that desk outcomes
   carry selection the manuscript cannot change (institution,
   team size, country, topic) [12], so a clean audit lowers risk
   rather than guaranteeing review.

4. **Conservative-edit posture applies.** The audit reports risk
   signals; it does not rewrite the abstract or cover letter
   unsolicited. If the user then asks for a rewrite, that's a
   separate transformation skill invocation.

## Implementation priority for scriptorium

**Verdict:** Yes — **v0.2 skill** `desk-rejection-risk` (or
explicit output mode of `reviewer-simulation`).

**Status (2026-10-20 refresh):** the skill now exists as
`skills/desk-rejection-risk/`. The verdict holds, and the refreshed
evidence strengthens it: journal-disclosed figures confirm that
most submissions to the top general journals are not sent to full
peer review [4, 9], and the editorial stage is where selection
is strongest [12]. Three things in the skill's grounding prose now
need to change. First, the rate figures it quotes from the previous
version of this note (*Cell*/*Lancet* figures; "30–60%" for mid-tier
journals) are no longer supported here. *Science*'s 85% figure [9]
should not be relied on until someone reads science.org directly,
because the only copies available to this refresh were trade-press
and search-index copies. Second, at *Science* that 85% includes a
Board of Reviewing Editors consultation for most papers [12], so the
skill should not describe the gate it simulates as an editor
skimming the abstract alone. Third, its policy-compliance category
should check the ICMJE AI-disclosure requirements: cover letter plus
manuscript (May 2023), and tool, version and prompts in the Methods
(January 2024 [16]), now consolidated in Section V (January 2026)
[5]. The skill should present these as established ICMJE
requirements, not new 2026 rules. Tracked for the skills pass, not
edited here.

**Skill spec:**
- Name: `desk-rejection-risk` (preferred) *or*
  `reviewer-simulation` with a `--mode=desk-triage` flag.
- Phase: v0.2 (next, alongside the first orchestrator).
- Scope: read `MANUSCRIPT_STATE.yaml`, the abstract, the cover
  letter (if present), and the figure captions. Do *not* read
  the full body. Emit a structured triage report with a small
  number of high-signal risk flags.
- Required data:
  - `project.target_venue` (mandatory; refuse to run without).
  - `project.target_type` (informs which checklist applies).
  - `core_claims` (for scope-fit assessment).
  - `known_weaknesses` (so triage doesn't flag what authors
    already acknowledge).
  - `contributors:` (if implemented per
    [[credit-taxonomy-authorship]]) for policy-compliance
    checks.
  - Venue-specific scope/significance rules from
    `knowledge/grants/` and `knowledge/scientific-writing/`.
- Output: a structured markdown report with sections
  `scope_fit`, `methodological_signals`,
  `significance_calibration`, `policy_compliance`,
  `language_quality`, each with severity flags (`high`,
  `medium`, `low`, `none`) and one-paragraph rationale.

**Why v0.2, not v0.1:** the v0.1 release prioritises proving the
skill composition pattern works. `desk-rejection-risk` is most
useful once `reviewer-simulation` is mature enough to share
infrastructure (venue calibration data, archetype prompts), which
v0.2 is the natural moment for.

**Operational note:** this is the skill that turns scriptorium's
value proposition from "a useful editing tool" into "a
weekend-of-time-for-months-of-round-trip-latency" trade. Sean
should treat it as load-bearing for the project's external
narrative.

## Open questions / weak evidence

- Desk-rejection rates are reported variably; many journals do
  not disaggregate triage from peer-review rejection in their
  public statistics. *Science* is the exception, publishing its
  external-review rate [9]. The earlier "70–80%" figures for
  *Nature*/*Cell* and "~90%" for *NEJM*/*Lancet* came from trade-press
  compilations and have been dropped. *Science*'s 85% not-reviewed
  figure and *Nature*'s "most submissions" statement are the
  defensible replacements; we found no primary figure for *Cell* or
  *The Lancet*. The *Science* figure is stated by the journal but
  was not read on the journal's own page in this refresh (see [9]),
  and it counts Board of Reviewing Editors declines as well as
  summary rejections [12].
- Field-to-field heterogeneity is large: ML conference venues
  don't really have "desk rejection" — every submission goes to
  review under tight deadlines. The audit needs discipline
  awareness ([[discipline-conventions]]).
- Editor weighting of reviewer recommendations is poorly
  characterised in the literature. The Bornmann review [1]
  summarises what little is known. The *Science*/*Science Advances*
  data [12] are the first large release that separates editorial and
  peer-review stages, but they come from two journals in one
  publisher family, and one author is a deputy editor at *Science
  Advances* (declared in the paper).
- The study-section analogy now rests on peer-reviewed work [7, 11],
  but that work uses constructed NIH-style panels and a small number
  of reviewers. No equivalent study measures how much a journal AE's
  first framing drives the outcome.
- The PLOS "modest uptake" statement above is unsourced.

## References

[1] Bornmann, L. (2011). Scientific peer review. *Annual Review of
Information Science and Technology*, 45(1), 197–245.
DOI: 10.1002/aris.2011.1440450112. (The canonical Bornmann review
of peer-review research. The previous entry pointed at DOI
10.3102/0034654309338847, which does not resolve.)

[2] Smith, R. (2006). Peer review: a flawed process at the heart
of science and journals. *Journal of the Royal Society of
Medicine*, 99(4), 178–182. DOI: 10.1177/014107680609900414. PMID:
16574968.

[3] van Rooyen, S., Godlee, F., Evans, S., Black, N., & Smith, R.
(1999). Effect of open peer review on quality of reviews and on
reviewers' recommendations: a randomised trial. *BMJ*, 318(7175),
23–27. DOI: 10.1136/bmj.318.7175.23. PMID: 9872878. (Foundational
BMJ open-review randomised trial.)

[4] *Nature*. (Ongoing.) Editorial criteria and processes.
<https://www.nature.com/nature/for-authors/editorial-criteria-and-processes>.
(Primary source for *Nature*'s ~8% acceptance figure, the statement
that most submissions are declined without review, and the
criteria for sending a paper out. Replaces the earlier
trade-press compilation.)

[5] International Committee of Medical Journal Editors. *ICMJE
Recommendations* (updated January 2026), including the new Section
V, "Use of Artificial Intelligence in Publishing".
<https://www.icmje.org/recommendations/>. (Section V consolidates
AI guidance that ICMJE first added in May 2023 (AI not an author;
disclosure in the cover letter and the submitted work) and extended
in January 2024 (tool, version and prompts; see [16]). icmje.org
blocked automated fetching during the 2026-10 refresh and audit, so
the May 2023 dating rests on search-index copies of ICMJE's May 2023
update and annotated PDF.)

[6] eLife. (2019). Peer review: final results from a trial at eLife.
<https://elifesciences.org/inside-elife/e8fa8f7a/peer-review-final-results-from-a-trial-at-elife>.
(Final outcomes of eLife's 2018 opt-in trial in which eLife
committed to publish any paper sent for in-depth review, using a
cut-off of one year after the trial closed. Not an evaluation of
published decision letters, as the earlier description said.)

[7] Pier, E. L., Raclaw, J., Carnes, M., Ford, C. E., & Kaatz, A.
(2019). Laughter and the chair: social pressures influencing
scoring during grant peer review meetings. *Journal of General
Internal Medicine*, 34(4), 513–514. DOI: 10.1007/s11606-018-4751-9.
PMID: 30604119. (Replaces the earlier pointer to NIH OER blog posts.
States that panelists' scores are anchored to those declared by the
assigned reviewers.)

[8] Bornmann, L., Mutz, R., & Daniel, H.-D. (2010). A
reliability-generalization study of journal peer reviews: a
multilevel meta-analysis of inter-rater reliability and its
determinants. *PLoS ONE*, 5(12), e14331.
DOI: 10.1371/journal.pone.0014331. PMID: 21179459.

[9] *Science* / AAAS. (Updated semi-annually; 2025 data.) Journal
metrics. <https://www.science.org/content/page/journal-metrics>.
(Submissions, external-review rate, acceptance rate and median
turnaround for the *Science* family of journals. The page blocked
automated fetching during the 2026-10 refresh, its independent
re-check and the evidence audit. The only copies of the 2025 figures
found were trade-press copies (Manusights blog posts) and
search-index summaries, the same class of source this refresh
dropped for the older desk-rejection rates. Treat the 85%
not-reviewed figure as stated by the journal but unverified here; it
needs a manual read of science.org before the skills pass relies on
it.)

[10] Massachusetts Medical Society. (Ongoing.) About NEJM.
<https://www.nejm.org/about-nejm/about-nejm>. ("About 5% of original
research submissions achieve publication by NEJM." The page blocked
automated fetching during the 2026-10 refresh, so the quotation was
checked through a search index's copy of the page.)

[11] Pier, E. L., Raclaw, J., Kaatz, A., Brauer, M., Carnes, M.,
Nathan, M. J., & Ford, C. E. (2017). 'Your comments are meaner than
your score': score calibration talk influences intra- and
inter-panel variability during scientific grant peer review.
*Research Evaluation*, 26(1), 1–14. DOI: 10.1093/reseval/rvw025.
PMID: 28458466.

[12] Zhang, S., LaBerge, N., McElhiney, Q., Larremore, D. B., &
Clauset, A. (2026). Editorial and peer review dynamics at elite
general science journals. *Science Advances*, 12(29), eaec0494.
DOI: 10.1126/sciadv.aec0494. PMID: 42455887. (Competing interest
declared in the paper: A. Clauset is a Deputy Editor at *Science
Advances*. Source for the *Science* triage breakdown: "Editors at
*Science* summarily rejected 28.1% of the 68,047 submissions … and
sent 69.5% to external experts on the BoRE. Given BoRE ratings and
advice, editors declined 75% of those manuscripts". The BoRE is "a
set of outside experts who would provide rapid advice to the editors
on whether and to whom to send a manuscript for formal peer review".
Checked against the open-access full text, PMC13371883.)

[13] Eisen, M. B., Akhmanova, A., Behrens, T. E., Diedrichsen, J.,
Harper, D. M., Iordanova, M. D., Weigel, D., & Zaidi, M. (2022).
Peer review without gatekeeping. *eLife*, 11, e83889.
DOI: 10.7554/eLife.83889. PMID: 36263932.

[14] *Nature*. (2025). Transparent peer review to be extended to all
of *Nature*'s research papers. *Nature*, 642(8068), 542.
DOI: 10.1038/d41586-025-01880-9. See also the Springer Nature press
release of 19 June 2025:
<https://www.springernature.com/gp/group/media/press-releases/transparent-peer-review-now-standard-for-nature/27788498>.

[15] eLife. (2024, addendum 2025). Changes to eLife's indexing
status in Web of Science and Scopus.
<https://elifesciences.org/inside-elife/ae620829/changes-to-elife-s-indexing-status-in-web-of-science-and-scopus>.

[16] *Ochsner Journal*. (2024, 25 January). Additional AI
recommendations from the International Committee of Medical Journal
Editors. *Ochsner Journal blog*.
<https://ochsnerjournal.wordpress.com/2024/01/25/additional-ai-recommendations-from-the-international-committee-of-medical-journal-editors/>.
(Dated secondary record of the January 2024 ICMJE amendment, quoting
it verbatim: "Authors who used AI technology to conduct the study
should describe its use in the methods section in sufficient detail
to enable replication of the approach, including the tool used,
version, and prompts where applicable." Cited because icmje.org
blocked automated fetching.)
