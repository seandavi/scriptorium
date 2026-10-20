# CRediT, ICMJE, and the authorship landscape

*Last updated: 2026-10-20*

## Synthesis

Authorship in modern science is increasingly contested, increasingly
formalised, and increasingly machine-readable. Two complementary
artefacts dominate the landscape: **ICMJE's four authorship
criteria** (substantial contribution, drafting, approval,
accountability), which define *who can be an author*; and the
**Contributor Roles Taxonomy (CRediT)**, which describes *what each
contributor actually did*, mapping contributions onto 14 standardised
roles. The empirical literature on ghost and gift authorship shows
the older "author list" model has been quietly failing for decades:
roughly one in five high-impact biomedical papers in 2008 reported
either honorary or ghost authorship [3]. A 2024 meta-analysis of 19
health-science surveys puts the figure higher when contributions are
checked against ICMJE criteria rather than self-assessed: 51% of
publications had honorary authorship on that measure [8]. The
combination of CRediT metadata plus explicit ICMJE compliance is the
field's response.

The 2023 ICMJE update making LLMs ineligible for authorship [5] is
relevant for scriptorium beyond the obvious "don't list ChatGPT as a
co-author" — it implies that any AI-assisted scholarly tool must be
disclosable, attributable, and ultimately reducible to a human's
accountability. The same May 2023 update asked authors to disclose
AI use in the cover letter and in the submitted work [5]. A January
2024 amendment added that authors who used AI to conduct the study
should give the tool, version and prompts in the Methods [10]. The
January 2026 update did not introduce these rules; it consolidated
ICMJE's AI guidance into a dedicated top-level Section V covering
authors, reviewers and editors [5]. The current text also warns that
nondisclosure of AI use "may be construed as misconduct in some
circumstances" [5]; when that sentence was first added could not be
established. Scriptorium's design is consistent with this: skills
are explicitly invoked, outputs are reviewed by humans, and the
underlying manuscript remains a human-accountable artefact.

For the build itself: this is a **schema-level addition, not a new
skill**. `MANUSCRIPT_STATE.yaml` should grow a `contributors:` field
aligned to CRediT roles. Several v0.x skills can then consume it
without a dedicated authorship skill being justified. (Superseded in
practice. Scriptorium shipped a dedicated `author-contribution-audit`
skill that reads the manuscript's Author Contributions prose, and the
schema deliberately omits `contributors:`. See *Implementation
priority*.)

## Evidence and frameworks

### CRediT: the 14 roles

The Contributor Roles Taxonomy was developed through a workshop
process beginning in 2012, formalised by Brand et al. in 2015 [1],
and adopted by CASRAI and (later) NISO. It became an ANSI/NISO
standard, Z39.104-2022, approved by ANSI on 14 January 2022 [4].
CRediT is widely referenced in publisher submission workflows (the
earlier "more than 150 publishers" figure could not be verified and
has been dropped). In 2026 Crossref added CRediT support to its
metadata schema (Schema 5.5), so roles can now travel with the DOI
record [7].

The 14 roles are:

1. Conceptualization
2. Data curation
3. Formal analysis
4. Funding acquisition
5. Investigation
6. Methodology
7. Project administration
8. Resources
9. Software
10. Supervision
11. Validation
12. Visualization
13. Writing — original draft
14. Writing — review & editing

Each contributor can hold multiple roles, and roles can be marked
"lead", "equal", or "supporting". The point is to disaggregate
"author" into "what did this person actually contribute", which is
where the older author-list model breaks down for large
collaborations.

The 2015 Brand et al. paper [1] frames CRediT as "moving beyond
authorship" toward an "attribution" model — useful background for
why the taxonomy looks the way it does. Allen, O'Connell and Kiermer
[6] describe how publishers began implementing it in the shift from
authorship to contributorship.

The role list itself has not changed. The CRediT Standing Committee
says that "current resource constraints make further revisions of
CRediT a challenge at this time". Meanwhile it is publishing
illustrative examples of the roles and prioritising implementation
of the existing version in scholarly metadata schemas such as
Crossref's [4, 7]. Crossref's Schema 5.5 allows multiple roles per
contributor and a flag for the corresponding author. Before 5.5, a
contributor could carry only one Crossref contributor role [7].

### ICMJE: the four criteria

The International Committee of Medical Journal Editors specifies
four conditions, *all of which must be met*, for someone to be
listed as an author:

1. Substantial contributions to the conception or design of the
   work, or the acquisition, analysis, or interpretation of data.
2. Drafting the work or reviewing it critically for important
   intellectual content.
3. Final approval of the version to be published.
4. Agreement to be accountable for all aspects of the work in
   ensuring that questions related to the accuracy or integrity of
   any part of the work are appropriately investigated and resolved.

Contributors who do not meet all four criteria should be listed in
the acknowledgements with their specific contributions described.
The current ICMJE text gives, as "examples of activities that alone
(without other contributions) do not qualify a contributor for
authorship", "acquisition of funding; general supervision of a
research group or general administrative support; and writing
assistance, technical editing, language editing, and proofreading"
[2]. These are a common source of dispute. (Corrected in the
2026-10 refresh: the earlier version listed "data acquisition"
here. ICMJE's list does not, because acquisition of data counts
toward criterion 1. Data collection alone still does not make
someone an author: ICMJE's own examples of acknowledgement wording
include contributors who "collected data", since they do not meet
the other three criteria [2].)

### Ghost, gift, and honorary authorship

Wislar et al.'s 2011 BMJ cross-sectional survey [3] is the
canonical empirical study. Across six leading general medical
journals in 2008:

- **Honorary authorship** (named author who did not meet ICMJE
  criteria): 17.6%.
- **Ghost authorship** (substantive contributor not named as
  author): 7.9%.
- **Either or both:** 21.0%.

This was an improvement over the 1996 baseline (29.2%), but the
absolute rate remains substantial. The literature distinguishes:

- **Gift authorship** — author added as a favour (mentor, senior
  colleague, collaborator on a different project).
- **Honorary authorship** — author added in deference to position
  or to confer credibility (department chair, funding-source
  representative).
- **Ghost authorship** — substantive contributor (often a
  professional medical writer, industry employee, or student)
  omitted from the byline.

Meursinge Reynders et al.'s 2024 systematic review and
meta-analysis [8] pooled 19 surveys in the health sciences, all
rated as low methodological quality. Prevalence depended on how
researchers were asked:

- 26% perceived honorary co-authors when given no authorship
  criteria.
- 18% did so when referred to the ICMJE criteria.
- 51% of publications had honorary authorship when researchers
  declared their co-authors' contributions and these were then
  compared with ICMJE criteria.

In the same surveys, 10% of researchers reported being approached
to add an honorary author, and 16% admitted adding one [8]. The gap
between 18% and 51% is the operational point (researcher
inference). Authors under-recognise honorary authorship until their
contributions are written down and checked against the criteria.
That is the check a contributions audit performs.

The CRediT taxonomy is partly a response: explicit role assignment
makes it harder to add an honorary author with no plausible
contribution, and harder to omit a ghost author who did the
heavy lifting.

### Authorship order by field

Order conventions vary substantially across disciplines (see
[[discipline-conventions]]):

- **Biomedicine and life sciences**: first author = lead
  contributor (often graduate student/postdoc); last author =
  senior responsible PI / corresponding author. Middle authors
  ordered approximately by contribution. Equal-contribution
  markers (†, *, "these authors contributed equally") are common
  for first-author shared positions.
- **Mathematics, theoretical physics, economics**: alphabetical by
  surname. Deviation from alphabetical is sometimes meaningful and
  sometimes a journal style.
- **Computer science / ML**: contribution-based, no consistent
  field convention; lead author is typically first, advisor often
  last but not always.
- **Particle physics ("hyperauthorship")**: hundreds-to-thousands
  of authors listed alphabetically by collaboration convention;
  byline is unreadable as a contribution signal.

A scriptorium audit that assumes "last author = senior PI"
silently mislabels mathematics and economics submissions.

### AI and authorship policy

ICMJE's 2023 update [5] is explicit: chatbots and LLMs **cannot
be listed as authors** because they cannot satisfy the
accountability criterion. Nature, Science, JAMA, and the Cell
Press journals have issued aligned statements; the consensus is
robust. The January 2026 ICMJE update moves the AI guidance into a
new top-level Section V, "Use of Artificial Intelligence in
Publishing", with subsections for authors, reviewers and editors
[5]. Most of the disclosure rules below predate it; the date each
first appeared is given where it could be established. Required
disclosure now reads:

- **AI used for writing, editing, proofreading** → describe in
  acknowledgements.
- **AI used for data collection, analysis, or figure generation**
  → describe in methods. Since a January 2024 amendment, authors
  who used AI to conduct the study should give enough detail to
  allow replication, "including the tool used, version, and prompts
  where applicable" [10]. The January 2026 Section V keeps this
  wording [5].
- **Cover letter** must mention AI use, in addition to the
  disclosure in the manuscript itself. This dates from the May 2023
  update [5].
- **AI as author or source.** Authors should not list AI as an
  author or co-author, nor cite AI as an author. "Referencing
  AI-generated material as the primary source is not acceptable"
  [5].
- **Consequences.** "Nondisclosure of AI use may require corrective
  action and may be construed as misconduct in some circumstances"
  [5]. This sentence is in the current Section V text; the date it
  was first added could not be verified, because icmje.org blocked
  automated fetching.
- **Peer-reviewer confidentiality**: reviewers "must adhere to the
  journal's stated policy on the use of AI or request permission
  from the journal" before using AI in a review. Confidentiality
  "may prohibit the uploading of the manuscript to software or
  other AI technologies where confidentiality cannot be assured
  unless such use of AI is explicitly permitted by journals" [5].
  (Reworded in the 2026-10 refresh. The earlier text said uploading
  was acceptable if the LLM was "contractually non-retaining", which
  is not ICMJE's test. The test is the journal's policy and its
  explicit permission.)

This last constraint is operationally relevant for
`reviewer-simulation`: a user running the skill on their own
unsubmitted manuscript is fine; a user running it on a manuscript
they are peer-reviewing is not.

## How this informs scriptorium

1. **Add `contributors:` to `MANUSCRIPT_STATE.yaml`.** Structure:
   a list of `{name, orcid?, roles: [CRediT role string]}`
   objects. This unblocks several downstream skills without
   requiring a new authorship-specific skill in v0.1.
   (Not adopted. See *Implementation priority*. If it is revisited,
   align it with Crossref Schema 5.5, which already models multiple
   CRediT roles and a corresponding-author flag [7].)

2. **Skills that consume `contributors:`**
   - `reviewer-simulation` can flag authorship-policy issues
     (missing contribution statement, last author shown as
     non-contributor, AI listed as author).
   - A future `submission-readiness` audit can check ICMJE
     compliance pre-submission.
   - `revision-summary` can attribute changes to specific
     contributors when journals require it.

3. **AI-disclosure language as a skill output.** Scriptorium
   itself is an AI-assisted tool. Outputs of transformation
   skills should be invoke-traceable enough that users can write
   honest acknowledgements ("Scriptorium's `argumentative-flow`
   skill was used to review the discussion section; all edits
   were reviewed by the authors"). This is a `MANUSCRIPT_STATE`
   /skill-log discipline, not a new skill. Under the ICMJE text
   (cover-letter disclosure since May 2023 [5]) the same record
   should also support a cover-letter disclosure. Where AI was used
   to conduct the study, as opposed to writing assistance, the
   Methods should name the tool, version and prompts (since January
   2024 [10]; retained in the January 2026 Section V [5]).

4. **Discipline-specific authorship-order norms.** A scope warning
   in the schema documentation: contribution-order interpretation
   is biomedical-default; in math/economics, alphabetical order is
   not informative.

## Implementation priority for scriptorium

**Verdict:** Yes (v0.1 schema augmentation) and No (no dedicated
authorship skill).

**Reconsidered 2026-10-20 — superseded by what shipped.** Scriptorium
now has a dedicated `author-contribution-audit` skill. It audits the
manuscript's Author Contributions section against the ICMJE criteria
and CRediT roles, and it deliberately does **not** add
`contributors:` to `MANUSCRIPT_STATE.yaml`. Declared prose stays in
the manuscript. The current verdict is therefore **Yes — dedicated
skill (shipped); No — schema field**. The original reasoning below is
kept for the record. The refreshed evidence supports the dedicated
skill. Self-assessed honorary authorship (18%) understates the
criteria-checked rate (51%) [8], which is exactly the gap a
contributions audit closes. Three changes are pending for the skills
pass:

- **Non-author activities.** The skill's list of activities that
  alone do not justify authorship should match the current ICMJE
  list (funding acquisition; general supervision or administrative
  support; writing assistance, technical and language editing,
  proofreading), which does not name data acquisition. A
  contributor who only collected data still fails criteria 2–4 [2].
- **AI disclosure.** The skill's AI checks should cover the ICMJE
  AI rules as now consolidated in Section V (January 2026) [5]: the
  cover-letter plus in-manuscript disclosure (May 2023 [5]); tool,
  version and prompts in the Methods (January 2024 [10]); no AI
  cited as an author or as a primary source; and the misconduct
  warning for nondisclosure (in the current text; date added not
  verified). The skill should present these as established ICMJE
  requirements, not as new in 2026.
- **CRediT metadata.** It may note that CRediT roles can now be
  deposited with Crossref metadata (Schema 5.5) [7].

**Yes — schema:** Add `contributors:` to
`MANUSCRIPT_STATE.yaml` in v0.1 or v0.2. Minimal effort, high
downstream leverage. Required data: a list of `{name, orcid?,
roles: [string]}` items; roles drawn from the 14 CRediT
categories; optional `equal_contribution` and `corresponding`
booleans. Document the field in the schema, with a note that
biomedical authorship-order conventions inform `roles` but other
disciplines may use the field differently.

**No — dedicated skill:** A standalone `authorship-audit` skill
is not justified in v0.1–v0.3. The cost of building it is
disproportionate to how often a user will invoke it. Embed
ICMJE-compliance checks in `reviewer-simulation` and (future)
`submission-readiness` instead.

**If Maybe later:** if a non-trivial fraction of users start
submitting to high-stakes biomedical venues where authorship
disputes are a known failure mode, promote to a
`authorship-and-contribution-audit` skill. Trigger: a user reports
that an authorship issue was caught at submission that scriptorium
could have flagged.

## Open questions / weak evidence

- CRediT adoption is uneven: many adopting publishers require role
  metadata at submission but don't publish it visibly, so its
  audit value depends on whether downstream readers can see it.
  A 2025 scoping review of 45 papers found that CRediT promotes
  transparency. It also found barriers: limited applicability across
  research types, ethical concerns, conflicts among contributors,
  low awareness, inconsistent implementation and ambiguous role
  definitions [9]. Crossref Schema 5.5 [7] addresses visibility,
  but uptake by publishers is not yet measured.
- The Wislar et al. data are 15+ years old. More recent surveys
  exist but are heterogeneous. The 2024 meta-analysis [8] pools them
  but rates every included survey as low methodological quality, so
  the field-wide trend is still unclear.
- AI authorship policy is evolving fast. The ICMJE position is
  robust, but specifics (do you need to disclose grammar
  checkers? citation managers? Paperpal?) are inconsistent across
  journals. The January 2026 ICMJE text [5] sets the floor for
  ICMJE-following journals, but it does not settle the
  grammar-checker question.
- The dating of individual ICMJE AI rules rests on secondary and
  search-index copies, because icmje.org blocked automated fetching:
  the May 2023 cover-letter rule on search-index copies of ICMJE's
  May 2023 update, the January 2024 tool/version/prompts sentence on
  a dated journal blog post [10]. When the misconduct sentence was
  added is unknown.
- The claim that Nature, Science, JAMA and Cell Press issued
  aligned AI-authorship statements was not re-checked journal by
  journal in the 2026-10 refresh.
- ORCID integration with CRediT is improving but is not yet
  universal; some publishers require ORCIDs for all authors,
  others only the corresponding author.

## References

[1] Brand, A., Allen, L., Altman, M., Hlava, M., & Scott, J.
(2015). Beyond authorship: attribution, contribution,
collaboration, and credit. *Learned Publishing*, 28(2), 151–155.
DOI: 10.1087/20150211.

[2] International Committee of Medical Journal Editors. *Defining
the Role of Authors and Contributors*.
<https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html>.

[3] Wislar, J. S., Flanagin, A., Fontanarosa, P. B., & DeAngelis,
C. D. (2011). Honorary and ghost authorship in high impact
biomedical journals: a cross sectional survey. *BMJ*, 343, d6128.
DOI: 10.1136/bmj.d6128. PMID: 22028479.

[4] CRediT — Contributor Roles Taxonomy.
https://credit.niso.org/. (Hosted by NISO since 2022.) Standard:
ANSI/NISO Z39.104-2022, approved by ANSI on 14 January 2022
(<https://www.niso.org/standards-committees/credit>). Standing
Committee updates: <https://credit.niso.org/category/updates/>.

[5] International Committee of Medical Journal Editors. (2023).
*ICMJE Recommendations*, updated May 2023. AI / chatbot
authorship guidance.
https://www.icmje.org/news-and-editorials/updated_recommendations_may2023.html
and <https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html>.
Superseded in part by the January 2026 update, which adds Section V,
"Use of Artificial Intelligence in Publishing" (A. Use of AI by
authors; B. Use of AI by reviewers; C. Editors' role):
<https://www.icmje.org/news-and-editorials/updated_recommendations_jan2026.html>
and <https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-reviewers.html>.
(The icmje.org pages blocked automated fetching during the 2026-10
refresh. The quotations were checked against search-index copies of
the January 2026 Recommendations, including ICMJE's annotated PDF.
Corrected in the 2026-10 audit: the earlier wording presented the
cover-letter rule and the tool/version/prompts sentence as new in
January 2026. They date from May 2023 and January 2024 [10]
respectively; January 2026 consolidated them into Section V.)

[6] Allen, L., O'Connell, A., & Kiermer, V. (2019). How can we
ensure visibility and diversity in research contributions? How
the Contributor Role Taxonomy (CRediT) is helping the shift from
authorship to contributorship. *Learned Publishing*, 32(1),
71–74. DOI: 10.1002/leap.1210.

[7] Crossref. (2026). Schema 5.5 now available: adding CRediT, new
record types for blogs and posters, and more. *Crossref blog*.
<https://www.crossref.org/blog/schema-5.5-now-available-adding-credit-new-record-types-for-blogs-and-posters-and-more/>.
See also the CRediT site post "Crossref Schema 5.5 now available:
includes support for CRediT":
<https://credit.niso.org/updates/crossref-schema-5-5-now-available-includes-support-for-credit/>.

[8] Meursinge Reynders, R. A., ter Riet, G., Di Girolamo, N.,
Cavagnetto, D., & Malički, M. (2024). Honorary authorship is highly
prevalent in health sciences: systematic review and meta-analysis
of surveys. *Scientific Reports*, 14(1), 4385.
DOI: 10.1038/s41598-024-54909-w. PMID: 38388672.

[9] Godskesen, T., Helgesson, G., & Eriksson, S. (2026).
Implementation, barriers, and improvement strategies for CRediT: a
scoping review. *Accountability in Research*, 33(4), 2528953.
DOI: 10.1080/08989621.2025.2528953. PMID: 40658084. (Published
online 14 July 2025.)

[10] *Ochsner Journal*. (2024, 25 January). Additional AI
recommendations from the International Committee of Medical Journal
Editors. *Ochsner Journal blog*.
<https://ochsnerjournal.wordpress.com/2024/01/25/additional-ai-recommendations-from-the-international-committee-of-medical-journal-editors/>.
(Dated secondary record of the January 2024 ICMJE amendment, quoting
it verbatim: "Authors who used AI technology to conduct the study
should describe its use in the methods section in sufficient detail
to enable replication of the approach, including the tool used,
version, and prompts where applicable." The same post records the
January 2024 addition "Reviewers must request permission from the
journal prior to using AI technology to facilitate their review."
Cited because icmje.org blocked automated fetching.)
