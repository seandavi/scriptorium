# Editorial decision-making and desk rejection

*Last updated: 2026-05-17*

## Synthesis

The peer-review process most authors imagine — careful reading by
two or three experts, weighed by an editor against a clear standard —
is not what most submissions experience. At high-impact journals,
the modal outcome is **desk rejection**: a 1–3 day editorial decision
made without external review at all. Reported rates run from roughly
30% at mid-tier journals to 70–90% at *Nature*, *Cell*, *NEJM*, and
similar [1,4]. The decision is made by an editor or associate editor
reading the cover letter and abstract, sometimes glancing at the
figures, and applying a small number of triage heuristics: scope fit,
methodological adequacy detectable from the abstract, novelty, and
language quality.

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
predictors. The bottom line: reviewer recommendations are noisy
inputs to an editorial decision that is itself partly judgement.

### Desk-rejection rates and triage criteria

Quantitative data is uneven, but the order of magnitude is
consistent across reports:

- *Nature*, *Cell*, *Science*: desk-rejection rates 70–80%+; overall
  acceptance under 8% [4].
- *NEJM*, *Lancet*: desk-rejection ~90%, overall acceptance ~5%.
- Mid-tier subject-specific journals: desk-rejection 30–60%.
- Open-access mega-journals (*PLOS ONE*, *Scientific Reports*):
  much lower desk-rejection (~20–30%), with most filtering
  happening at peer review.

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

### Editors and associate editors

The "editor's introduction" papers in journals like *eLife* and
*Annual Reviews* describe the assignment-to-AE step: a handling
editor reads the abstract, identifies an associate editor (AE)
with topical fit, and either triages or hands off. AE selection
is itself a high-leverage decision — AEs choose reviewers, weight
their reports, and write the decision letter.

Lauer's writings at NIH [TODO verify primary source] describe the
study-section analogue: a designated discussant pre-reads and
anchors the conversation; the panel then debates and scores. The
parallel matters: in both peer review and grant review, the
person who introduces the work to the deciding body has
disproportionate influence on outcome. This is why
[[reviewer-archetypes-grants]] applies as much to journal AEs as
to grant reviewers — the AE is functionally the first reviewer.

### Open / transparent decision-making

Several journals have experimented with transparency to test
whether visibility changes review quality or outcome:

- ***eLife***: publishes a decision letter (a consolidated set of
  reviewer-and-editor points) with every accepted paper. eLife's
  2022+ "publish-then-review" model further restructured the
  process: editorial decisions to send out for review are
  publishable as preprints regardless of eventual recommendation.
  Empirical evaluations [6] show modest effects on quality with no
  acceptance-rate inflation.
- ***BMJ***: publishes signed reviews and the full prepublication
  history. Randomized trials at BMJ [3] found that open identities
  and open reports did not significantly change review quality or
  acceptance rates.
- ***PLOS***: opt-in publication of peer-review history; modest
  uptake.

The pattern: making decisions visible does not, on average,
change them much. The constraint on review quality is *time and
expertise*, not opacity.

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
saves 6+ weeks of round-trip; catching a reviewer-style critique
saves perhaps 2 weeks on a second round. The desk-rejection audit
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
     ethics statements)?

2. **Use `MANUSCRIPT_STATE.target_venue` aggressively.** A
   desk-rejection-risk audit is incoherent without a target.
   Skills should refuse to run (or run with a warning) if
   `target_venue` is empty.

3. **Honest reporting.** The skill should distinguish
   *desk-rejection signals* (editorial triage heuristics) from
   *reviewer concerns* (peer-review-stage critique). These map
   to different stages of the decision pipeline and should be
   reported separately.

4. **Conservative-edit posture applies.** The audit reports risk
   signals; it does not rewrite the abstract or cover letter
   unsolicited. If the user then asks for a rewrite, that's a
   separate transformation skill invocation.

## Implementation priority for scriptorium

**Verdict:** Yes — **v0.2 skill** `desk-rejection-risk` (or
explicit output mode of `reviewer-simulation`).

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
  public statistics. The 70–80% figures for *Nature*/*Cell* are
  consistent across multiple sources but are not authoritative.
- Field-to-field heterogeneity is large: ML conference venues
  don't really have "desk rejection" — every submission goes to
  review under tight deadlines. The audit needs discipline
  awareness ([[discipline-conventions]]).
- Editor weighting of reviewer recommendations is poorly
  characterised in the literature. The Bornmann review [1]
  summarises what little is known.
- The Lauer / study-section literature is real but mostly
  blog-and-talk format rather than peer-reviewed primary sources;
  primary citations would strengthen this document.

## References

[1] Bornmann, L., & Daniel, H.-D. (2010). The state of the
art of editorial peer review: A literature survey on the
manuscript review process and the assessment of the contribution
of editorial peer review. (Bornmann has a body of peer-review-
process review work; the originally cited 10.3102/0034654309338847
points to a *Review of Educational Research* meta-review.) [TODO
verify which Bornmann review is most appropriate as the canonical
citation here — the body of work spans 2008–2015.]

[2] Smith, R. (2006). Peer review: a flawed process at the heart
of science and journals. *Journal of the Royal Society of
Medicine*, 99(4), 178–182. DOI: 10.1177/014107680609900414. PMID:
16574968.

[3] van Rooyen, S., Godlee, F., Evans, S., Black, N., & Smith, R.
(1999). Effect of open peer review on quality of reviews and on
reviewers' recommendations: a randomised trial. *BMJ*, 318(7175),
23–27. DOI: 10.1136/bmj.318.7175.23. (Foundational BMJ open-review
randomised trial.)

[4] Manusights and trade-press compilations of desk-rejection
rates by journal (2024–2026). Specific journal acceptance and
desk-rejection rates as cited in the synthesis above are drawn
from journal-reported statistics and aggregated reviews. [TODO
verify against primary publisher disclosures for each named
journal.]

[5] International Committee of Medical Journal Editors. ICMJE
Recommendations on editor and reviewer responsibilities.
https://www.icmje.org.

[6] eLife. (2022). Peer Review: Final results from a trial at
eLife. https://elifesciences.org/inside-elife/e8fa8f7a/
peer-review-final-results-from-a-trial-at-elife. (Internal
evaluation of eLife's published-decision-letter model.)

[7] Lauer, M. (NIH OER). Blog posts on study-section dynamics at
https://nexus.od.nih.gov/all/category/peer-review/. [TODO
identify primary peer-reviewed citation for grant-review
analogue.]
