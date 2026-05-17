# CRediT, ICMJE, and the authorship landscape

*Last updated: 2026-05-17*

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
either honorary or ghost authorship [3]. The combination of CRediT
metadata plus explicit ICMJE compliance is the field's response.

The 2023 ICMJE update making LLMs ineligible for authorship [5] is
relevant for scriptorium beyond the obvious "don't list ChatGPT as a
co-author" — it implies that any AI-assisted scholarly tool must be
disclosable, attributable, and ultimately reducible to a human's
accountability. Scriptorium's design is consistent with this: skills
are explicitly invoked, outputs are reviewed by humans, and the
underlying manuscript remains a human-accountable artefact.

For the build itself: this is a **schema-level addition, not a new
skill**. `MANUSCRIPT_STATE.yaml` should grow a `contributors:` field
aligned to CRediT roles. Several v0.x skills can then consume it
without a dedicated authorship skill being justified.

## Evidence and frameworks

### CRediT: the 14 roles

The Contributor Roles Taxonomy was developed through a workshop
process beginning in 2012, formalised by Brand et al. in 2015 [1],
and adopted by CASRAI and (later) NISO. As of the mid-2020s, more
than 150 publishers reference CRediT in their submission workflows.

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
why the taxonomy looks the way it does.

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
The ICMJE explicitly notes that **funding, supervision, and
data-acquisition alone do not justify authorship** — a common
source of dispute.

### Ghost, gift, and honorary authorship

Wislar et al.'s 2011 BMJ cross-sectional survey [3] is the
canonical empirical study. Across six leading general medical
journals in 2008:

- **Honorary authorship** (named author who did not meet ICMJE
  criteria): 17.6%.
- **Ghost authorship** (substantive contributor not named as
  author): 7.9%.
- **Either or both:** 21.0%.

This was an improvement over the 1996 baseline (29.1%), but the
absolute rate remains substantial. The literature distinguishes:

- **Gift authorship** — author added as a favour (mentor, senior
  colleague, collaborator on a different project).
- **Honorary authorship** — author added in deference to position
  or to confer credibility (department chair, funding-source
  representative).
- **Ghost authorship** — substantive contributor (often a
  professional medical writer, industry employee, or student)
  omitted from the byline.

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
robust. Required disclosure varies:

- **AI used for writing, editing, proofreading** → describe in
  acknowledgements.
- **AI used for data collection, analysis, or figure generation**
  → describe in methods.
- **Cover letter** must mention AI use.
- **Peer-reviewer confidentiality**: uploading a manuscript to an
  LLM under review violates confidentiality unless the LLM is
  contractually non-retaining.

This last constraint is operationally relevant for
`reviewer-simulation`: a user running the skill on their own
unsubmitted manuscript is fine; a user running it on a manuscript
they are peer-reviewing is not.

## How this informs scriptorium

1. **Add `contributors:` to `MANUSCRIPT_STATE.yaml`.** Structure:
   a list of `{name, orcid?, roles: [CRediT role string]}`
   objects. This unblocks several downstream skills without
   requiring a new authorship-specific skill in v0.1.

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
   /skill-log discipline, not a new skill.

4. **Discipline-specific authorship-order norms.** A scope warning
   in the schema documentation: contribution-order interpretation
   is biomedical-default; in math/economics, alphabetical order is
   not informative.

## Implementation priority for scriptorium

**Verdict:** Yes (v0.1 schema augmentation) and No (no dedicated
authorship skill).

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
- The Wislar et al. data are 15+ years old. More recent surveys
  exist but are heterogeneous; the field-wide trend is unclear.
- AI authorship policy is evolving fast. The ICMJE position is
  robust, but specifics (do you need to disclose grammar
  checkers? citation managers? Paperpal?) are inconsistent across
  journals.
- ORCID integration with CRediT is improving but is not yet
  universal; some publishers require ORCIDs for all authors,
  others only the corresponding author.

## References

[1] Brand, A., Allen, L., Altman, M., Hlava, M., & Scott, J.
(2015). Beyond authorship: attribution, contribution,
collaboration, and credit. *Learned Publishing*, 28(2), 151–155.
DOI: 10.1087/20150211.

[2] International Committee of Medical Journal Editors. *Defining
the Role of Authors and Contributors*. https://www.icmje.org/
recommendations/browse/roles-and-responsibilities/
defining-the-role-of-authors-and-contributors.html.

[3] Wislar, J. S., Flanagin, A., Fontanarosa, P. B., & DeAngelis,
C. D. (2011). Honorary and ghost authorship in high impact
biomedical journals: a cross sectional survey. *BMJ*, 343, d6128.
DOI: 10.1136/bmj.d6128. PMID: 22028479.

[4] CRediT — Contributor Roles Taxonomy.
https://credit.niso.org/. (Hosted by NISO since 2022.)

[5] International Committee of Medical Journal Editors. (2023).
*ICMJE Recommendations*, updated May 2023. AI / chatbot
authorship guidance.
https://www.icmje.org/news-and-editorials/updated_recommendations_may2023.html
and https://www.icmje.org/recommendations/browse/
artificial-intelligence/ai-use-by-authors.html.

[6] Allen, L., O'Connell, A., & Kiermer, V. (2019). How can we
ensure visibility and diversity in research contributions? How
the Contributor Role Taxonomy (CRediT) is helping the shift from
authorship to contributorship. *Learned Publishing*, 32(1),
71–74. DOI: 10.1002/leap.1210.
