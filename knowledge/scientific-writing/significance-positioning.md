# Significance and positioning

*Last updated: 2026-10-20*

## Synthesis

"Significance" in scientific writing is two distinct things that share a
word. The first is **rhetorical positioning**: how the author frames why
the work matters, why now, and to whom. The second is **review-criterion
significance**: the specific question NIH or NSF reviewers are scored
against, distinct from rigor, innovation, and approach. A manuscript or
grant succeeds when its rhetorical positioning lands on the same point the
applicable review criterion measures — and fails, often invisibly, when the
two diverge.

The empirical literature on what reviewers actually weight is thinner than
the volume of advice on the topic suggests. Tahamtan et al.'s 2016 review
of citation predictors [1] is the cleanest synthesis we have, and
points to a small number of consistently strong factors (paper quality,
journal impact factor, number of authors, international collaboration,
field visibility) with much of the rest of the literature being noisy.
Empirical work on peer review (Teplitskiy et al. *PNAS* 2022 on novelty
[2]) finds that novelty, measured from reference-list combinations,
predicts acceptance, and that conventionality predicts it too. Editors
select for novelty even after accounting for reviewers'
recommendations.

For scriptorium, the practical implication is that the **positioning
section** of a manuscript or grant (the abstract, the significance
statement, the specific aims page, the closing paragraph of the
introduction) is where the highest-leverage editorial work happens.
`reviewer-simulation` (current) and a future `positioning-audit` skill
should focus disproportionate attention here.

Two 2025–2026 developments sharpen this. For NIH applications, the
2025 scoring guidance tells reviewers that the Importance factor
(Significance + Innovation) sets a ceiling on the overall impact score
[12]. Positioning is now the limiting factor on a grant's score, not
one input among several. Second, a 2026 *PNAS* study of NIH and NSF
proposals found that heavier LLM involvement is associated with lower
semantic distinctiveness, with proposals positioned closer to recently
funded work [15]. A writing tool that helps with positioning can push
toward sameness, which is the opposite of what positioning is for.

## Evidence and frameworks

### Day & Gastel: the classic procedural guide

Robert A. Day and Barbara Gastel's *How to Write and Publish a Scientific
Paper*, 8th edition (Greenwood, 2016; Cambridge University Press paperback,
2017; ISBN-13 978-1-4408-4280-1; Cambridge ISBN 978-1-316-64043-2) [3] is
the longest-running general-purpose manual for scientific publishing. Day's original
1979 edition has been continuously updated; Gastel joined as coauthor for
recent editions and is now first author. The book is practical and
procedural — title construction, abstract craft, author-instructions
reading, response-to-reviewers — rather than theoretical. It is the
default text in many graduate-level scientific writing courses outside
biomedicine.

Day & Gastel's framing of significance is conservative: state the problem,
state what you did, state what is new, state why it matters, in roughly
that order. The book does not propose a structural framework on the order
of OCAR ([[narrative-frameworks]]) but it disciplines authors on the small
craft moves (title weight-bearing, abstract structure, methods-as-recipe)
that determine whether positioning lands.

### Mewburn and the Thesis Whisperer tradition

Inger Mewburn, Director of Research Training at the Australian National
University, has written extensively under the "Thesis Whisperer" brand
(thesiswhisperer.com) on academic positioning, particularly for graduate
students and early-career researchers. The relevant book-length treatment
is *How to Be an Academic: The Thesis Whisperer Reveals All* (NewSouth
Publishing, 2017; ISBN-13 978-1-74223-507-3) [4].

Mewburn's contribution is sociological more than rhetorical: she frames
academic writing as a positioning practice within a community of practice,
where the writer is making claims not just about the work but about their
membership in a field. The Mewburn–Thomson 2013 paper on why academics
blog (*Studies in Higher Education* 38(8):1105–1119) [9] is part of this
lineage.

The practical takeaway for a writing system: significance claims read
differently depending on the writer's apparent positioning. A junior
author claiming "first demonstration" carries less weight than the same
claim from a senior author at a high-prestige institution. This is
neither fair nor avoidable; the editorial response is to make the
*evidence* for the claim do more work and rely less on author authority.

### What predicts citation impact (Tahamtan et al. 2016)

Tahamtan I, Safipour Afshar A, Ahamdzadeh K. Factors affecting number of
citations: a comprehensive review of the literature. *Scientometrics*.
2016;107(3):1195–1225. DOI: 10.1007/s11192-016-1889-2. [1]

This review synthesized 198 empirical studies on what predicts citation
counts. The three categories of factors:

1. **Paper-related** — quality, novelty/originality of subject, field
   characteristics, study type (review > original > letter), length,
   abstract characteristics, title characteristics.
2. **Journal-related** — impact factor, accessibility (open access),
   indexing, language (English dominant).
3. **Author-related** — number of authors, international collaboration,
   author seniority/h-index, institutional reputation.

The most consistent findings across studies: paper quality and journal
impact factor dominate; international collaboration and number of authors
contribute modestly; author demographics (age, gender, race) have weak and
inconsistent effects.

For editorial work, the actionable factors are: title clarity and
informativeness, abstract structure, choice of journal, and the inclusion
of a clear methodological signal in the abstract. The non-actionable
factors (institutional prestige, author seniority) bound the realistic
ceiling of editorial improvement.

### Empirical work on peer review and novelty

Wang J, Veugelers R, Stephan P. Bias against novelty in science: A
cautionary tale for users of bibliometric indicators. *Research Policy*.
2017;46(8):1416–1436. DOI: 10.1016/j.respol.2017.06.006. [5]

More directly germane:

Teplitskiy M, Peng H, Blasco A, Lakhani KR. Is novel research worth
doing? Evidence from peer review at 49 journals. *PNAS*.
2022;119(47):e2118046119. DOI: 10.1073/pnas.2118046119. PMID: 36395142. [2]

This study used 20,538 manuscripts submitted to *Cell* and *Cell
Reports* (2013–2018) and 6,785 manuscripts submitted in 2018 to 47
Institute of Physics Publishing journals. Novelty and conventionality
were measured from the atypicality of journal combinations in each
manuscript's reference list, not from how the manuscript describes
itself. Findings: (a) "higher novelty is consistently associated with
higher acceptance" — top-quintile novelty submissions were 6.5
percentage points more likely to be accepted than bottom-quintile
ones; (b) higher conventionality was also associated with acceptance
(+16.3% top-bottom quintile difference); (c) reviewer disagreement was
not systematically related to novelty or conventionality; and (d)
"editors select strongly for novelty even conditional on reviewers'
recommendations" (+7.0%). The authors conclude that journal peer
review "favors novel research that is well situated in the existing
literature."

The editorial implication: positioning that flags novelty *and* conventional
grounding does better than positioning that flags novelty alone. The
manuscript that opens with "Although the X approach is well established,
we show…" is making both moves simultaneously. This extends the
finding (researcher inference): the study measured what a manuscript
cites, not how it frames itself, and it did not isolate the abstract
or editorial-screening stage.

### NIH significance and the simplified review framework (2025)

As of January 25, 2025, NIH applications submitted under the Simplified
Review Framework score against three factors rather than the five legacy
criteria [6]:

- **Factor 1: Importance of the Research** (combining Significance and
  Innovation) — scored 1–9
- **Factor 2: Rigor and Feasibility** (Approach) — scored 1–9
- **Factor 3: Expertise and Resources** (Investigator, Environment) —
  rated for sufficiency, not scored

The legacy Significance criterion read: *"Does the project address an
important problem or a critical barrier to progress in the field? If the
aims of the project are achieved, how will scientific knowledge, technical
capability, and/or clinical practice be improved?"* Under the Simplified
Review Framework, reviewers instead "evaluate the importance of the
proposed research in the context of current scientific challenges and
opportunities". They "assess whether the application addresses an
important gap in knowledge in the field, would solve a critical problem,
or create a valuable conceptual or technical advance", and evaluate "the
rigor of the scientific background for the work (e.g., prior literature
and/or preliminary data)". The Innovation language adds that "a project
that is not applying novel concepts or approaches may be of critical
importance for the field." [6]

The reframing matters editorially. Under the old framework, an author
could be strong on Significance and weak on Innovation (or vice versa)
and get a mixed score. Under the new framework, both are bundled into
Factor 1. Our reading (researcher inference) is that an application that
nails one but not the other will score lower than one that ladders both
into a single positioning claim. NIH's scoring guidance (effective
October 2025 Council round) makes Factor 1 more consequential still: "a
project of moderate or limited importance (Factor 1) cannot be made more
impactful by a strong approach (Factor 2) and/or appropriate expertise
and resources (Factor 3)", and "Your Factor 1 score should set a limit
for the best possible overall impact score" [12]. Positioning sets the
upper bound for the application. See [[nih-significance-patterns]] for
the funding-side changes (no paylines from January 2026; proposed
score-free reporting) and NIH's 2025 policy that applications
"substantially developed by AI" are not considered original [16].

### NSF broader impacts criterion

NSF's Merit Review Criterion 2 ("Broader Impacts") was added in 1997 under
Director Neal Lane and has been the subject of substantial empirical and
philosophical analysis since [7, 8]. The criterion asks how the proposed
work will "benefit society and contribute to the achievement of specific,
desired societal outcomes." NSF's current examples, which it says are
illustrative rather than prescriptive, are STEM education, public
engagement, societal well-being, a globally competitive STEM workforce,
partnerships, national security, U.S. economic competitiveness, and
research and education infrastructure [7]. NSF's 2025 priorities
guidance tells investigators to "prioritize the first six broader impacts
goals" of the America COMPETES Reauthorization Act of 2010. It requires
that activities addressing the seventh goal (expanding participation of
women and underrepresented groups) be "open and available to all
Americans" [13]. In December 2025 the National Science Board recommended
that NSF "pursue renaming the 'Broader Impacts' criterion to 'Societal
Benefits'"; this is a recommendation, not adopted policy [14].

Holbrook (2005) [8] documents persistent community concerns:
ambiguity about how broader impacts are weighted relative to intellectual
merit; lack of evaluative consensus among reviewers; difficulty of
projecting societal impact from basic research. Bozeman & Boardman (2009)
[11] give a critical assessment of the criterion, which "has met with
resistance from the scientific community". A 2023 study (Woodson &
Boutilier, *Research Evaluation* 32(2)) compared NSF award abstracts with
project outcome reports from 2014–2017. It found "the number of broader
impacts proposed in the abstracts is significantly higher than the number
of broader impacts reported" in the outcome reports, a pattern common
across directorates and impact types except impacts serving advantaged
groups [10]. The authors caution that this does not show scientists are
"delinquent or disingenuous". Rather, it suggests many broader-impacts
statements are aspirational rather than operational. The NSB report's
own survey found that only 53% of NSF staff said it is clear how to
assess Broader Impacts, against 96% for Intellectual Merit [14].

For editorial work, the implication: broader-impacts language should be
*specific* (named partners, named programs, named metrics) rather than
*aspirational* ("will broadly benefit underrepresented groups"). The
specific form survives reviewer scrutiny better. Under NSF's current
priorities guidance, broadening-participation activities should also be
described as open to all participants, with any targeting framed by
non-protected characteristics such as institution type, geography,
socioeconomic status, or career stage [13].

### LLM use and the distinctiveness of positioning (2026)

Qian Y, Wen Z, Furnas AC, Bai Y, Shao E, Wang D. The rise of large
language models and the direction and impact of US federal research
funding. *PNAS*. 2026;123(33):e2601439123. DOI: 10.1073/pnas.2601439123. [15]

Using confidential NIH and NSF submissions from two US R1 universities
and all publicly released NIH and NSF awards, the authors found that
LLM use "rises sharply beginning in 2023" with a bimodal split between
minimal and substantive use. "Higher LLM involvement is consistently
associated with lower semantic distinctiveness, positioning projects
closer to recently funded work within the same agency." At NIH, LLM use
was positively associated with proposal success and early publication
output, with gains concentrated in non-hit papers; NSF showed no
comparable associations. The design is observational, so the success
association does not show that LLM use causes funding.

The editorial implication (researcher inference): a positioning critique
should check whether the claimed gap and contribution are specific to
this project or could describe any recent award in the area. Skills
should not introduce generic framing in the course of "improving"
significance prose.

## How this informs scriptorium

- **`reviewer-simulation`** (current). Should distinguish between the
  rhetorical-significance critique ("the framing doesn't make me care") and
  the criterion-significance critique ("under NIH simplified review, this
  doesn't ladder Factor 1 well"). Knowing the target venue and the
  applicable review criteria changes what the simulator says. For NIH
  grants, a weak Factor 1 critique should be presented as capping the
  overall assessment, per the 2025 scoring guidance [12].
- **`desk-rejection-risk`** (current). Its significance-framing category
  draws on this note. The novelty-plus-conventional-grounding check should
  be attributed to Teplitskiy et al. 2022 [2], and described as
  consistent with that study rather than shown by it. The study measured
  reference-list novelty and conventionality across the whole acceptance
  decision; it did not test abstract-level framing or the desk-screening
  stage.
- **`venue-fit`** (current). Uses the significance axis; nothing in this
  refresh changes how the axis is scored.
- **`terminology-normalization`** (current). Exempts significance claims
  proper from the promotional-register catalog. The NIH Innovation
  language — a project "not applying novel concepts or approaches may be
  of critical importance" [6] — is a reason not to push authors toward
  "novel" in grant prose.
- **`specific-aims-audit`** (planned, v0.4). NIH specific aims pages live or
  die on whether they articulate (i) a problem of acknowledged importance,
  (ii) a critical barrier, (iii) a tractable approach. The skill should
  test for each move explicitly. This is the most direct application of the
  Schimel OCAR + ABT diagnostic ([[narrative-frameworks]]) to the
  grant-writing domain. Under the 2025 scoring guidance, (i) and (ii)
  bound the score and should be tested first.
- **`positioning-audit`** (proposed). A read-only critique skill that
  evaluates the abstract, significance statement, and introduction-closer
  for: (i) whether the "why now" is clearly stated, (ii) whether novelty is
  paired with conventional grounding, (iii) whether the named beneficiaries
  of the work are specific, not aspirational, and (iv) whether the claimed
  gap is distinctive to this work rather than generic to the field [15].
  Outputs a per-element assessment with span pointers.
- **`broader-impacts-audit`** (proposed, NSF-specific). Checks whether
  broader-impacts statements name specific partners, programs, and
  measurable activities — rather than aspirational claims — and whether
  participation activities match NSF's current priorities guidance [13].
  Could share infrastructure with `positioning-audit`.

The deeper design implication: positioning is the part of the manuscript
where structured-output skills can have the highest leverage and the
lowest semantic risk. The positioning sections are short, opinionated, and
high-stakes. A scriptorium that focuses critique-skill density here
produces visible improvements that authors can actually adopt. It should
stay critique-first: Qian et al. [15] and NOT-OD-25-132 [16] both point
away from generating positioning prose for the author.

## Implementation priority for scriptorium

**Verdict:** Yes (current and v0.4) for the grounding role; Maybe later
for the stand-alone `positioning-audit` and `broader-impacts-audit`
skills.

**If Yes:** This note already grounds `desk-rejection-risk`,
`venue-fit`, and `terminology-normalization`, and is named as grounding
for the v0.4 `specific-aims` and `aims-significance-coherence` skills.
Required data: `project.target_venue` or `target_funder`, the abstract,
significance statement, and introduction-closer (manuscripts) or the
aims page (grants). The October 2026 refresh changes three things these
skills should reflect: the corrected novelty attribution and scope
(Teplitskiy et al. 2022), the Factor 1 ceiling, and NSF's current
Broader Impacts guidance.

**If Maybe later:** `positioning-audit` flips to Yes once
`desk-rejection-risk`'s significance-framing category proves too
coarse in use, or authors ask for positioning critique outside a
submission context. `broader-impacts-audit` flips to Yes when NSF
adopts final merit-review language (the "Societal Benefits" rename or
the Guidance on Financial Assistance), so the skill is not built on
wording that is about to change.

## Open questions / weak evidence

- The empirical literature on what reviewers weight is dominated by
  bibliometric proxies (citation counts) rather than direct measurement of
  reviewer decisions. The Teplitskiy et al. 2022 PNAS study [2] is unusual
  in using submission-level acceptance data across many journals; it is
  not yet replicated at scale, and its novelty measure is
  reference-based rather than rhetorical.
- Mewburn's positioning work is influential but pedagogical and qualitative
  rather than empirical. The claims about authority-effects on reviewer
  perception are plausible but not rigorously tested.
- NIH's Simplified Review Framework is new (effective January 2025) and
  there is not yet enough scoring data to tell whether the factor
  consolidation has changed what reviewers prioritize. The 2025 scoring
  guidance states the intended effect (Factor 1 as ceiling); whether
  reviewers apply it is unmeasured.
- "Significance" as a criterion is famously vague. The empirical evidence
  that improving significance framing improves outcomes is indirect —
  largely from comparing accepted vs. rejected manuscripts after the fact,
  which is confounded with quality.
- Qian et al. [15] show an association between LLM involvement and less
  distinctive positioning; whether editing tools that only critique (as
  opposed to generating text) have the same effect is unknown.

## References

1. Tahamtan I, Safipour Afshar A, Ahamdzadeh K. Factors affecting number
   of citations: a comprehensive review of the literature. *Scientometrics*.
   2016;107(3):1195–1225. DOI: 10.1007/s11192-016-1889-2.
2. Teplitskiy M, Peng H, Blasco A, Lakhani KR. Is novel research worth
   doing? Evidence from peer review at 49 journals. *PNAS*.
   2022;119(47):e2118046119. DOI: 10.1073/pnas.2118046119. PMID: 36395142.
3. Gastel B, Day RA. *How to Write and Publish a Scientific Paper*. 8th
   ed. Greenwood; 2016 (Cambridge University Press paperback, 2017).
   ISBN-13 978-1-4408-4280-1; Cambridge paperback ISBN-13
   978-1-316-64043-2.
4. Mewburn I. *How to Be an Academic: The Thesis Whisperer Reveals All*.
   NewSouth Publishing; 2017. ISBN-13 978-1-74223-507-3.
5. Wang J, Veugelers R, Stephan P. Bias against novelty in science: A
   cautionary tale for users of bibliometric indicators. *Research
   Policy*. 2017;46(8):1416–1436. DOI: 10.1016/j.respol.2017.06.006.
6. National Institutes of Health. Simplified Peer Review Framework.
   NOT-OD-24-010 and follow-on policy notices.
   https://grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review
   (accessed 2026-05-17; effective for applications submitted on or after
   January 25, 2025). Criterion text as quoted:
   https://grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework
   (accessed 2026-10-20).
7. National Science Foundation. *Merit Review Broader Impacts Criterion:
   Representative Activities*. NSF; ongoing.
   https://www.nsf.gov/funding/learn/broader-impacts
8. Holbrook JB. Assessing the science–society relation: The case of the
   US National Science Foundation's second merit review criterion.
   *Technology in Society*. 2005;27(4):437–451.
   DOI: 10.1016/j.techsoc.2005.08.001.
9. Mewburn I, Thomson P. Why do academics blog? An analysis of audiences,
   purposes and challenges. *Studies in Higher Education*.
   2013;38(8):1105–1119. DOI: 10.1080/03075079.2013.835624.
10. Woodson T, Boutilier S. From intent to impact—The decline of broader
    impacts throughout an NSF project life cycle. *Research Evaluation*.
    2023;32(2):348–355. DOI: 10.1093/reseval/rvac046.
11. Bozeman B, Boardman C. Broad impacts and narrow perspectives: Passing
    the buck on science and social impacts. *Social Epistemology*.
    2009;23(3–4):183–198. DOI: 10.1080/02691720903364019.
12. National Institutes of Health. Simplified Review Framework: Scoring
    Guidance. Released March 14, 2025; effective 2025/10 Council round.
    https://grants.nih.gov/sites/default/files/Simplified-Review-Scoring-Guidance.pdf
    (accessed 2026-10-20).
13. National Science Foundation. Updates on NSF Priorities.
    https://www.nsf.gov/updates-on-priorities (accessed 2026-10-20).
14. National Science Board. Merit review for a new era at NSF (release of
    *Merit Review for a Changing Landscape*). December 2025.
    https://www.nsf.gov/nsb/updates/merit-review-new-era-nsf . Policy
    recommendations and staff-survey figures as presented in: National
    Science Board. NSF Merit Review for a Changing Landscape (slides).
    February 25, 2026.
    https://nsf-gov-resources.nsf.gov/files/NSB-Merit-Review-Changing-Landscape-Feb25-2026.pdf
15. Qian Y, Wen Z, Furnas AC, Bai Y, Shao E, Wang D. The rise of large
    language models and the direction and impact of US federal research
    funding. *PNAS*. 2026;123(33):e2601439123.
    DOI: 10.1073/pnas.2601439123. Preprint: arXiv:2601.15485.
16. National Institutes of Health. NOT-OD-25-132: Supporting Fairness and
    Originality in NIH Research Applications. July 17, 2025.
    https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
