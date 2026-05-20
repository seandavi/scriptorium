# Venue selection: how researchers choose where to submit

*Last updated: 2026-05-20*

## Synthesis

Venue selection is the highest-stakes decision in the submission
workflow and the one most often made by intuition, lab tradition,
or career incentive rather than by deliberate fit assessment. The
cost of misfit is measurable in months — a desk rejection at one
of *Nature*'s family journals can cost 6–12 weeks before the author
even reaches external review. The published research on author
behaviour at submission is consistent: most authors over-aim, eat
desk rejection, then submit to the venue that was a defensible fit
all along [1, 2]. The pattern is not malice or incompetence; it is
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
the abstract sense [3].

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
across decades. Misra and Agarwal's 2017 *Journal of Korean Medical
Science* paper [4] is one of the more cited modern guides; it
frames journal selection around scope, audience, indexing, open
access, and time-to-publication as the load-bearing axes. Earlier
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
common desk-rejection pattern [1].

### Author-venue mismatch as a measurable phenomenon

The mismatch is documented empirically. Studies of submission
trajectories — papers that ultimately publish, but only after one
or more rejections — show that the modal "successful" submission
sequence is *higher-prestige journal → desk rejection or first-round
rejection → mid-tier journal → publication*, with months of latency
inserted by the first attempt [2]. The data on time-to-publication
for ultimately-accepted manuscripts is consistent: the mean cycle
time is 6–9 months from initial submission to final acceptance,
with rejection cycles accounting for most of the variance [TODO
verify with current cross-journal time-to-publication data; the
*PLOS Biology* and *Nature Communications* publisher reports are
the standard sources].

The decision pattern that produces this is rational from one
narrow perspective (try the higher-prestige venue first — the
expected value of a publication there outweighs the latency cost
if hit-rate is high enough) and irrational from another (most
authors over-estimate hit-rate, and the cumulative latency from
serial rejection eats into productivity). Realistic tiering — with
explicit "this is your defensible upper tier given the manuscript
as it currently reads" framing — is the intervention that lets
authors make this trade-off deliberately rather than by default.

### Solomon and Björk on open-access venue selection

Solomon and Björk's 2012 work on open-access journal selection [6]
adds a layer specific to the OA landscape: when authors choose
between equivalent venues on scope and audience, the deciding
factors become **article-processing-charge (APC) cost**, **license
terms** (CC-BY vs more restrictive), **indexing status**, and
**publication speed**. Their data shows that authors who are
self-funding APCs make systematically different choices than
authors on institutional OA agreements, and that the venue's
indexing (Scopus, Web of Science, PubMed) is treated as a hard
filter by many authors regardless of fit on other axes.

For a venue-fit skill, this means the recommendation must surface
the OA / cost / indexing axes alongside scope and audience — a
"perfect fit" venue that costs $11,400 in APCs is not a fit for
an author on a hard cap. The right behaviour is to let the author
declare their constraints (`open_access_required`, `max_apc_usd`,
`indexing_requirements`) and have the recommendation respect them
as hard filters rather than soft preferences.

### Career-stage interactions

Less well-documented but real in practice: career stage interacts
with venue choice in ways that change what counts as a defensible
recommendation. Early-career researchers benefit asymmetrically
from publications in well-respected specialty venues — first-author
papers in *J Biol Chem* or *J Neurosci* carry weight on faculty
search committees that *Nature* one-off coverage does not, because
field-recognised specialty publications signal a sustained
disciplinary commitment [TODO verify against any published
analysis of CV-tier signaling; this is widely-held in informal
mentorship literature but the formal-evidence base is thinner than
the topic deserves]. Established researchers can afford the higher
expected latency of prestige-tier attempts because the marginal
publication is less career-defining.

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
author tells the editor *why this venue*. Editors read cover
letters before manuscripts at most journals [1]; a cover letter
that articulates scope fit, audience fit, and significance fit
explicitly survives triage at a higher rate than one that names
the work without naming the fit. For a venue-fit skill, this
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
   Maps to the empirical pattern that authors over-aim. Naming
   each tier explicitly — including the venues the manuscript
   doesn't yet support — saves the author from the most expensive
   misfit pattern (high-prestige attempt that desk-rejects).

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
   Solomon-Björk's evidence says these dominate fit on equivalent
   scope/audience. If the author declares constraints, the skill
   filters before tiering rather than recommending and then
   apologising.

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
  selection.
- [[common-critiques-taxonomy]] — what reviewers at any venue tend
  to flag; informs the methodological-fit axis.
- [[declared-work-scope]] — the project-wide convention. Venue-fit
  operates on declared work and refuses to invent claims about the
  manuscript to make it fit a venue.

## References

[1] Bordage, G. (2001). Reasons reviewers reject and accept
manuscripts: the strengths and weaknesses in medical education
reports. *Academic Medicine*, 76(9), 889–896.
DOI: 10.1097/00001888-200109000-00010. PMID: 11553504. (Top-10
reject reasons — the source data for the per-axis assessment
framework here. The reasons cluster around scope/audience
mismatch, methodology, significance framing, and presentation, in
that order of frequency.)

[2] Calcagno, V., Demoinet, E., Gollner, K., Guidi, L., Ruths,
D., & de Mazancourt, C. (2012). Flows of research manuscripts
among scientific journals reveal hidden submission patterns.
*Science*, 338(6110), 1065–1069. DOI: 10.1126/science.1227833.
PMID: 23065906. (Empirical submission trajectories; demonstrates
the over-aim-then-cascade pattern at scale.)

[3] Lin, Y., Frey, C. B., & Wu, L. (2022). Remote collaboration
fuses fewer breakthrough ideas. *Nature*, 622, 87–94.
DOI: 10.1038/s41586-023-06767-1. [TODO verify: confirm this is
the correct Lin et al. 2022 PNAS / Nature reference for the
novel-plus-conventional finding cited in `editorial-decision-
making.md`. The cross-reference suggests so, but the citation
metadata should be checked against the actual paper.]

[4] Misra, D. P., & Agarwal, V. (2017). Selecting the right
journal: a comprehensive guide for authors. *Journal of Korean
Medical Science*, 32(7), 1064–1070.
DOI: 10.3346/jkms.2017.32.7.1064. PMID: 28581262. (Modern
editorial-guidance synthesis; the scope/audience/indexing/OA/
speed framework cited in the synthesis.)

[5] Day, R. A., & Gastel, B. (2016). *How to Write and Publish a
Scientific Paper* (8th ed.). Cambridge University Press. ISBN:
9781316640432. (The canonical writing-and-publishing manual;
chapter on journal selection is brief but the principle of
"aim at the journal whose readers are the audience for your
contribution" is the foundational framing.)

[6] Solomon, D. J., & Björk, B.-C. (2012). A study of open
access journals using article processing charges. *Journal of
the American Society for Information Science and Technology*,
63(8), 1485–1495. DOI: 10.1002/asi.22673. (Open-access venue
selection; the APC / license / indexing trade-off documentation.)

[7] Think.Check.Submit. (Ongoing.) Checklist for choosing
journals. <https://thinkchecksubmit.org/>. (Community-maintained
practical checklist; primary reference for the "what to verify
before submitting" question. Sister resource to
[[predatory-publishing]].)
