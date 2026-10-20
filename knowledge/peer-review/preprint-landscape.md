# Preprint landscape: servers, post-publication review, and the moving boundary

*Last updated: 2026-10-20*

## Synthesis

The preprint ecosystem has expanded from a narrow physics-and-CS
convention (arXiv, founded 1991) into a discipline-spanning
infrastructure with substantial — and still-evolving — overlap
with traditional journal publishing. By 2024, biomedical preprint
servers were hosting hundreds of thousands of papers annually;
COVID-19 (2020-2022) compressed roughly a decade of biomedical
preprint normalisation into two years [1, 2]. The current
landscape encompasses **archive-style preprint servers** that
provide minimal moderation and lasting time-stamped citation
(arXiv, bioRxiv, medRxiv, ChemRxiv, EarthArXiv, PsyArXiv, SSRN,
OSF Preprints), **post-publication peer-review platforms** that
add a refereed layer on top of preprints (PCI / Peer Community In,
Review Commons, F1000Research, eLife's post-2022 "reviewed
preprints" model), and **journal-policy variation** about preprints
that ranges from required pre-submission to outright prohibition
[3, 4].

Since 2025 the infrastructure itself has been reorganised, and
funders have started to expect or require preprints. bioRxiv and
medRxiv moved to an independent nonprofit, openRxiv, in March 2025
[22]. arXiv left Cornell to become an independent nonprofit in 2026
[5]. The Gates Foundation has expected funded manuscripts to be
posted as preprints since January 2025, "to the extent feasible" and
with an exception where the grantee judges a preprint inappropriate
[27]. HHMI has required initial and revised preprints on designated
servers since January 2026, for original research articles that are
major contributions from covered HHMI labs [26].
Under submission pressure, partly from AI-generated papers, arXiv
also tightened what it accepts. Since October 2025 its CS category
requires review and position papers to have passed peer review
first [21], and since October 2026 every submitter is limited to two
submissions per calendar month [20].

The decision an author faces is no longer just "where do I
submit?" but a multi-part one: *do I preprint? where? before, after,
or instead of journal submission? do I want pre- or post-
publication peer review? what does my target journal allow?* These
questions have substantively different answers across fields
(physics and CS have preprint cultures decades older than the
journal venues that aggregate them; clinical medicine still treats
preprinting cautiously because of patient-decision implications),
across career stages (preprinting carries different cost-benefit
calculations for trainees vs. established researchers), and across
funder requirements (NIH, Wellcome Trust, cOAlition S funders all
have specific preprint and open-access requirements that interact
with venue choice).

For an automated venue-fit recommendation, the consequence is that
the preprint layer cannot be a one-size answer. The author needs
to be asked whether preprints are in scope for them, and the
recommendation has to account for the chosen preprint server's
interaction with the recommended journal's preprint policy. The
landscape moves fast enough that the right grounding posture is to
maintain principles in this note and verify specifics at
invocation time.

## Evidence and frameworks

### The major preprint servers

**arXiv** was founded in 1991 by Paul Ginsparg, hosted at Cornell
for decades, and established as an independent nonprofit in 2026
[5]. It is the original and the model. Initially physics, expanded to mathematics, computer
science, quantitative biology, economics, statistics, and several
others. arXiv applies endorsement-based moderation (new authors
must be endorsed by an existing author) and minimal subject-area
screening; the time-stamp is the durable contribution. arXiv now
reports hosting more than three million articles in eight subject
areas [5]. Volume is rising fast: arXiv received 40,363 submissions
in September 2026, and submissions doubled in the two years before
that [20]. The CS subfields have built an
entire publication culture around arXiv-first posting; physics and
math have done so for longer.

Two 2025–2026 arXiv policy changes matter for venue advice:

- **CS review and position papers.** Since late October 2025 (arXiv
  blog post of 31 October 2025), review (survey) articles and
  position papers in arXiv's CS category must already be accepted
  at a journal or conference, after completed peer review, before
  arXiv will consider them. Workshop review is "not enough". arXiv
  cited an "unmanageable influx" of such papers, many of them
  "little more than annotated bibliographies", with generative AI
  adding to the flood. arXiv frames this as enforcing its existing
  rules on accepted content types rather than as a new policy [21].
- **Rate limits.** From 1 October 2026 each submitter may make at
  most two submissions per calendar month, across all categories.
  The separate cap of three active submissions at any time has
  applied since 2024. Rejected submissions count toward the monthly
  limit. arXiv calls this a "stopgap" while it works out best
  practice for authors using AI tools [20].

**bioRxiv** and **medRxiv** began as projects of Cold Spring Harbor
Laboratory; since March 2025 they have been overseen by openRxiv,
an independent nonprofit with researcher-led governance and initial
funding from the Chan Zuckerberg Initiative [22]. bioRxiv (launched
2013) covers preclinical and
basic biology; medRxiv (launched 2019, founded by CSHL, Yale and
BMJ [4, 6]) covers clinical research. Both apply a screening process focused
on excluding non-research content, plagiarism, and obvious
methodological problems. medRxiv adds a clinical-screen layer to
guard against papers that could mislead patient decisions [6].
COVID-19 made medRxiv a central piece of the public-health
information infrastructure and surfaced both the value (rapid
dissemination of preliminary findings) and the cost
(misinterpreted preprints driving public policy) of biomedical
preprinting [7].

**ChemRxiv** (founded 2017, jointly run by ACS, RSC, GDCh, CCS,
and CSJ) is the chemistry-discipline preprint server, with
moderation similar to bioRxiv's. **EarthArXiv** (2017, EarthRxiv
governance) covers Earth and planetary sciences. **PsyArXiv**
(2016, hosted on OSF) is the psychology preprint server with
broader social-sciences uptake. **SSRN** (1994, acquired by
Elsevier in May 2016 [8]) is the social sciences and economics preprint
server with substantial uptake in finance, law, and accounting.

**OSF Preprints** (Open Science Framework, Center for Open
Science) provides a multi-disciplinary preprint platform with
moderation per discipline. The OSF model is more meta-infrastructure
than single server; many discipline-specific preprint servers run
on OSF (PsyArXiv, SocArXiv, LawArXiv, others).

For an author choosing a preprint server, the relevant axes are:
**discipline scope** (does this server cover your field?),
**moderation rigor** (will format/scope problems be caught before
your paper is publicly time-stamped?), **license and reuse terms**
(CC-BY, CC-BY-NC, and variants — these matter downstream for
journal submission), **indexing** (Google Scholar yes for all
major servers; PubMed-relatedness varies), and **the target
journal's preprint policy**. A further axis is now **funder
designation**. For articles its policy covers, HHMI requires bioRxiv
(or medRxiv, ChemRxiv or arXiv for out-of-scope work) under CC BY 4.0
and says "other preprint servers should not be used" [26]. Where
Gates-funded authors preprint, the policy asks for a server
"recognized by the foundation or preapproved preprint server which
applies a sufficient level of scrutiny to submissions" [27]. For
funded authors, server choice can be a compliance question rather
than a preference.

### Pre-publication vs post-publication peer review

The pre/post-pub distinction is the second axis. Traditional
journal review is **pre-publication**: a manuscript is reviewed
before it appears in the venue. Post-publication review platforms
add an explicit layer on top of preprints in which the time-stamped
preprint is the durable record and review happens after public
posting. Several variants matter:

**PCI / Peer Community In** [9] is a community-run system in which
discipline-specific "Peer Communities" (PCI Evolutionary Biology,
PCI Ecology, PCI Neuroscience, others) recommend preprints based
on full peer review. The recommended preprint is a recognised
endorsement; no APC, no journal submission required. Many
mainstream journals accept PCI-recommended preprints as
fast-tracked submissions or accept them outright [10]. PCI is
strongest in ecology and evolutionary biology and is expanding.

**Review Commons** [11] is a refereed-preprint service that
provides journal-independent peer review on bioRxiv preprints,
with the resulting reviews portable to affiliated journals (EMBO
Press, eLife, others). The author receives reviews; the journals
receive reviews and decide independently whether to accept based
on the existing review record. The model is "review the science
once, decide at multiple journals" — the inefficiency of multiple
re-review cycles is reduced.

**F1000Research** [12] is a post-publication peer-review platform
where papers are published openly after editorial check (not peer
review), then reviewed openly by invited reviewers whose names and
reports are public. Articles can be revised in response to
reviews; the final status of an article is "approved" (1+
reviewer recommendations), "approved with reservations", or "not
approved", visible to readers. F1000Research has strong uptake in
clinical research, gene/genome papers, software/method papers,
and is the canonical reference for the post-pub review model.

**eLife's post-2022 model** [13] is the most consequential recent
shift. eLife announced in October 2022 that it would eliminate
accept/reject decisions after peer review [13];
under the current model, eLife reviews any preprint the editors
select for review and publishes the resulting Public Reviews
alongside the preprint as a "reviewed preprint", with no final
acceptance gate. The author can revise; eLife continues to
review revisions; the preprint and its review record are the
publication. This is the most aggressive existing implementation
of the post-publication-review model at a high-impact journal.
It has an indexing cost. Web of Science put eLife on hold in
October 2024. eLife now sends Web of Science only the papers
assessed as "solid" or better, about 93% of them, and is therefore
not eligible for a Journal Impact Factor. In Scopus, eLife moved to
the Preprints Collection. eLife reported in May 2025 that more than
100 funders and institutions still consider eLife papers in research
evaluation [23].

The pre/post-pub choice is not just a venue choice; it is a
strategic choice about **timing** (rapid dissemination vs.
embargo), **transparency** (named open reviews vs. blinded
journal reviews), **community signal** (a PCI recommendation
carries different weight than a journal acceptance, and the
weight varies by field), and **CV interpretation** (search and
tenure committees treat reviewed preprints inconsistently;
varies by field and institution).

### Journal preprint policies

Journal policies on preprints range from **required** to
**prohibited**, with most journals at "permitted with conditions"
in the middle. The variation matters because some authors have
been desk-rejected for either preprinting (some journals consider
this prior publication) or not preprinting (some funders or
journals now require open-access pre-submission posting). The
authoritative reference for journal-by-journal policies is
**SHERPA/RoMEO** [14] (now JISC's Open Policy Finder), which
aggregates publisher self-disclosed policies on preprint, accepted
manuscript, and published version self-archiving.

Common policy patterns:

- **Preprint-friendly** (most life sciences journals as of 2024):
  preprinting before submission is permitted with the requirement
  that the manuscript be appropriately cited in the published
  version and on the preprint server once accepted. Examples:
  *eLife*, *PLOS Biology*, *Nature* journals, *Cell Press*
  journals (with stipulations).

- **Preprint-required** (an emerging category): preprinting at a
  specified server is a precondition for submission or
  consideration. *eLife*'s post-2022 model is the clearest
  example; *EMBO Press* journals (some) accept bioRxiv-posted
  preprints directly for review. Funder policies now push the same
  way from the author side: HHMI requires preprints for covered
  original research articles from 2026 [26], and Gates has expected
  them, to the extent feasible and with grantee exceptions, since
  2025 [27].

- **Preprint-tolerant** (most clinical and applied-medicine
  journals as of 2024): preprinting is permitted but the journal
  treats it as a minor demerit in some cases, especially when the
  preprint received public attention before review.

- **Preprint-prohibited or hostile** (a shrinking but persistent
  category): some specialty journals, particularly in clinical
  surgery and some humanities subfields, treat preprinting as
  prior publication and decline to consider preprinted work. The
  list of such journals shifts; SHERPA/RoMEO is the reference.

For a venue-fit skill, the practical pattern is to check the
recommended journal's preprint policy against the author's
preprint preference and surface any incompatibility.

### Funder requirements

Funder requirements have been a strong recent driver of preprint
adoption. The **cOAlition S "Plan S"** [15] requires deposit in an
open repository for funded research. **NIH's 2024 Public Access
Policy** took effect on 1 July 2025, brought forward from 31
December 2025. It requires the Author Accepted Manuscript to be
submitted to PubMed Central upon acceptance and made publicly
available without embargo on the official date of publication [16].
Separately, in July 2025 NIH proposed five options for limiting
allowable publication costs. They ranged from disallowing all
publication costs to per-article caps of $2,000–$6,000 and an award
cap of 0.8% of direct costs or $20,000, whichever is greater, with
a proposed effective date of 1 January 2026 [24]. The most recent
dated status review found (March 2026) reported that no cap had been
finalised. A check of NIH's list of policy notices in October 2026
found no notice finalising one either [24].
**Wellcome Trust** funds APCs only for research articles in fully
open-access journals or platforms indexed in DOAJ, from 1 January
2025. It strongly encourages preprints, requires them during public
health emergencies, and accepts a CC BY preprint as compliant where
neither the Version of Record nor the Author Accepted Manuscript can
be made open access [25].
**Howard Hughes Medical Institute (HHMI)** has the most prescriptive
policy. For articles submitted from 1 January 2026, it requires
initial and revised preprints under CC BY 4.0 on a designated server
(bioRxiv preferred). The requirement covers named HHMI roles
(Investigators, Janelia group leaders, Freeman Hrabowski Scholars and
others listed in the policy), and only original research articles
that are major contributions from their labs: someone from the lab is
(co-)first, (co-)last or (co-)corresponding author. It "does not
apply to review articles, reviews of existing protocols and methods,
perspectives, commentaries" [26]. The initial preprint must go
up promptly after a journal sends the manuscript to review; HHMI
strongly recommends posting by journal submission. The revised
preprint must go up before journal publication. HHMI budgets can no
longer pay APCs at hybrid journals [17, 26].
**The Gates Foundation's** refreshed policy has applied to all
funded manuscripts since 1 January 2025. It states the foundation's
"expectation" that funded manuscripts are shared promptly as
preprints, "as soon as possible and to the extent feasible", "except
where the grantee determines that a preprint is not appropriate due
to ethical, safety or other legitimate concerns". It requires
immediate CC BY 4.0 availability, and states that the foundation
"will not pay article processing charges" [27]. Preprinting is
therefore a strong default for Gates grantees, not a hard
requirement.

For an automated venue-fit recommendation, funder-driven
constraints are hard filters: a Wellcome-funded researcher
recommended to submit to a subscription journal without an OA
option is recommended to violate their funder agreement. Hybrid
journals are now a funder issue too. Wellcome and HHMI no longer pay
hybrid APCs [25, 26], and Gates pays no APCs at all [27]. The skill
should ask about funder constraints up front when the manuscript's
financial scaffolding is non-trivial.

### What the landscape says about itself: known unknowns

The preprint landscape moves faster than peer-reviewed evidence
about the preprint landscape moves. Several questions are
actively unresolved as of late 2024 / early 2026:

- **Does preprinting affect citation rates and journal acceptance
  rates?** Multiple studies show modest positive effects on
  citation [18, 19], but the cleanest causal evidence is still
  thin and the publication-bias confound is real.

- **How do search and tenure committees weight preprints?**
  Cross-institutional variation is large; this is a CV-strategy
  question without a clean answer.

- **Will pre-publication review survive in fields that adopt
  reviewed-preprint models?** eLife's bet is that the answer is
  no; the broader journal ecosystem's response is in progress.

- **What is the right policy on AI-generated preprints?** Several
  servers have begun requiring disclosure; standards are not
  uniform. arXiv's responses so far are restrictions on content type
  and volume, not disclosure rules: the CS review/position-paper
  rule [21] and the 2026 rate limit [20].

For an automated tool, the operational consequence is that this
note should be treated as guidance to **principles** for
recommendation, with the **specifics** to be verified at
invocation time. The author should be pointed at SHERPA/RoMEO,
DOAJ, and the specific journal's instructions when the decision
is being made, not handed an authoritative answer from training
data alone.

## How this informs scriptorium

For `venue-fit` specifically:

1. **Preprints are an opt-in mode, asked once.** The skill asks
   whether preprint recommendations are in scope before producing
   them. Default depends on field (life sciences and CS / physics:
   default ask; clinical surgery, some humanities: default ask
   with caveat that this is field-uncommon). When in scope, the
   preprint section is its own tier (not interleaved with
   journals); when out of scope, it's suppressed entirely.

2. **Recommend specific preprint servers, not "preprint it
   somewhere".** Match the server to the manuscript's discipline
   (bioRxiv for life sciences, medRxiv for clinical, arXiv for
   physics/CS, ChemRxiv for chemistry, OSF for cross-discipline).
   Surface the per-server moderation rigor, license, and indexing
   so the author sees the trade-offs. Do not recommend arXiv CS for
   an unreviewed survey or position paper [21]. For HHMI-covered
   original research articles, restrict the choice to HHMI's
   designated servers [26].

3. **Surface the pre/post-pub review choice as a strategic
   decision.** Within the preprint section, name PCI, Review
   Commons, F1000Research, and eLife's reviewed-preprint model
   as the strategic alternatives to traditional review. The
   choice involves timing, transparency, community signal, and
   field convention — not a single "best" answer.

4. **Check journal preprint policy against preprint
   recommendation.** When recommending both a journal and a
   preprint server, verify (or caveat) that the journal accepts
   preprinted work from that server. Flag any incompatibility.

5. **Check funder constraints.** When the manuscript declares
   funder requirements (NIH, Wellcome, cOAlition S, etc.),
   filter the recommendation list against those requirements
   before tiering. A Wellcome paper recommended to a subscription
   journal without an OA option is a wrong recommendation. HHMI is
   the one funder here whose preprint rule is a requirement: for an
   original research article that is a major contribution from a
   covered HHMI lab ((co-)first, (co-)last or (co-)corresponding
   author), preprinting moves from opt-in to required; reviews,
   perspectives and commentaries are exempt [26]. A Gates-funded
   manuscript should get a strong prompt to preprint, not an
   enforced requirement, because the policy is an expectation "to
   the extent feasible" with grantee-determined exceptions [27].

6. **Caveat staleness, defer to SHERPA/RoMEO at decision time.**
   The skill names that its preprint-server and journal-policy
   knowledge has a date stamp and points the author at
   SHERPA/RoMEO for verification before submission. The
   verification step is part of the recommended action sequence,
   not an aside.

## Implementation priority for scriptorium

**Verdict:** Direct grounding for the `venue-fit` skill (v0.2);
preprints are an explicit mode within that skill, not a separate
skill. The same-skill decision is documented in issue #82.

**2026-10-20 refresh:** the verdict holds, but two behaviours need
updating in the skill (tracked for the skills pass). First, a
declared HHMI funder should turn the preprint mode from opt-in into
required, but only for original research articles that are major
contributions from a covered HHMI lab, and should restrict server
choice [26]. A declared Gates funder should trigger a strong prompt
to preprint, not a requirement, because Gates expects preprints "to
the extent feasible" and lets grantees decide a preprint is
inappropriate [27]. Second, the server-matching rule should exclude
arXiv CS for unreviewed review and position papers [21]. Funder APC
rules (Wellcome DOAJ-only, HHMI no hybrid, Gates none, NIH caps
proposed but not finalised as of October 2026) belong in the
hard-filter step [24–27].

**Why useful context anyway:**

- The opt-in preprint mode pattern (default ask, then proceed)
  is the right shape for any decision-support feature that
  bridges fields with different cultural defaults. Worth being
  explicit about as a project-wide pattern.

- A future v0.3 `preprint-policy-compliance` skill, if it
  emerges, would consume this note's framework. The
  per-journal-policy-axis content here could be extracted into a
  structured machine-queryable resource as a follow-up; for v0.2
  it stays as a knowledge note that the skill reads.

- The fast-moving-landscape framing — "principles in this note;
  specifics verified at invocation time" — is the right posture
  for several other areas where training-data knowledge ages
  faster than the discipline does (the AI-agentic-scientific-
  writing landscape, the predatory-publishing landscape, OA
  policy specifics). Worth being explicit that this is a
  general scriptorium pattern.

**Condition that would flip this:** if the reviewed-preprint
model (PCI, Review Commons, eLife post-2022, F1000Research)
becomes the dominant publication mode in any major field, the
venue-fit skill's whole shape would shift — the question becomes
"which review community / platform" rather than "which journal".
Worth re-reading this note in 18 months and updating the
emphasis accordingly. The 2025–2026 funder policies (the HHMI
requirement and the Gates expectation) move part of the
life-sciences author population toward that condition from the
funder side, without yet making it dominant.

## Cross-references

- [[venue-selection]] — primary grounding for `venue-fit`;
  preprint recommendation is the additional layer this note adds.
- [[predatory-publishing]] — same skill applies predatory
  refusal to preprint servers as well as journals (most preprint
  servers are not predatory in the usual sense, but the question
  is worth applying — the OA preprint ecosystem has predatory
  analogues).
- [[editorial-decision-making]] — preprint policies interact with
  journal triage; some editors look for preprint citation
  patterns in their desk-rejection heuristics.
- [[declared-work-scope]] — the convention. Preprint
  recommendation operates on declared work; the skill does not
  preprint anything on behalf of the author.

## References

[1] Fraser, N., Brierley, L., Dey, G., Polka, J. K., Pálfy, M.,
Nanni, F., & Coates, J. A. (2021). The evolving role of preprints
in the dissemination of COVID-19 research and their impact on the
science communication landscape. *PLoS Biology*, 19(4),
e3000959. DOI: 10.1371/journal.pbio.3000959. PMID: 33798194.
(The canonical assessment of how COVID-19 accelerated biomedical
preprinting and the implications.)

[2] Abdill, R. J., & Blekhman, R. (2019). Tracking the popularity
and outcomes of all bioRxiv preprints. *eLife*, 8, e45133.
DOI: 10.7554/eLife.45133. PMID: 31017570. (Empirical analysis of
bioRxiv preprint trajectories and journal publication outcomes.)

[3] Sever, R. (2026). The story behind the science: preprints of
pandemic potential — how bioRxiv and medRxiv brought preprints to
the life sciences. *mBio*, 17(2), e02989-25.
DOI: 10.1128/mbio.02989-25. (Replaces "Polka et al. 2024, *Annual
Review of Biomedical Data Science*", which could not be found in
Crossref or PubMed and appears not to exist. A first-hand account
of how the two servers brought preprints to the life sciences, by
their co-founder; the author's affiliations are openRxiv and Cold
Spring Harbor Laboratory.)

[4] Rawlinson, C., & Bloom, T. (2019). New preprint server for
medical research. *BMJ*, 365, l2301. DOI: 10.1136/bmj.l2301.
PMID: 31167753. (The BMJ editorial announcing medRxiv with Yale and
CSHL. Replaces "Maggio et al. 2020, *Medical Education* 54(7)",
whose DOI 10.1111/medu.14181 and PMID 32249938 resolve to unrelated
papers. A 2018 Maggio, Artino, Picho & Driessen paper with a similar
title exists — "Are you sure you want to do that? Fostering the
responsible conduct of medical education research", *Academic
Medicine* 93(4), 544–549, PMID 28678102 — but it is about medical
education research, not preprints.)

[5] arXiv. (Ongoing.) About arXiv. <https://arxiv.org/about>.
(Primary source for arXiv's history, moderation, governance and
size: "more than three million scholarly articles in eight subject
areas"; independent nonprofit since 2026.)

[6] openRxiv. (Ongoing.) About medRxiv.
<https://www.medrxiv.org/content/about-medrxiv>. (medRxiv's
founders, operator and screening criteria, including screening for
material that might pose a health risk. URL updated; the previous
`/about` path returns 404.)

[7] Brierley, L., Nanni, F., Polka, J. K., Dey, G., Pálfy, M.,
Fraser, N., & Coates, J. A. (2022). Tracking changes between
preprint posting and journal publication during a pandemic.
*PLoS Biology*, 20(2), e3001285.
DOI: 10.1371/journal.pbio.3001285. PMID: 35104285. (The
preprint-to-published-version drift during COVID-19 — concrete
evidence of preprint version-control risks. PMID corrected from
35104289, which is a different paper.)

[8] Elsevier. (2016, 17 May). Elsevier acquires the Social Science
Research Network (SSRN), the leading social science and humanities
repository and online community. Press release.
<https://www.prnewswire.com/news-releases/elsevier-acquires-the-social-science-research-network-ssrn-the-leading-social-science-and-humanities-repository-and-online-community-579752311.html>.
(Replaces an unverifiable blog-post pointer. Primary record of the
acquisition. The governance controversy that followed is not
sourced here.)

[9] Peer Community In (PCI). (Ongoing.)
<https://peercommunityin.org>. (Community-run discipline-specific
preprint recommendation system, created by INRAE researchers Denis
Bourguet, Benoit Facon and Thomas Guillemaud, the authors of [10].
Corrected in the 2026-10 refresh: the earlier entry named a
non-existent co-founder and attributed a "founding paper" to
Casadevall & Fang 2014.)

[10] Guillemaud, T., Facon, B., & Bourguet, D. (2019). Peer
Community In: a free process for the recommendation of unpublished
scientific papers based on peer review. In *ELPUB 2019 23rd
International Conference on Electronic Publishing*.
DOI: 10.4000/proceedings.elpub.2019.23. (Formal account of PCI's
design by its founders; replaces the documentation-site
placeholder.)

[11] Review Commons. (Ongoing.) <https://www.reviewcommons.org>.
(Journal-independent refereed-preprint platform for the life
sciences, developed with ASAPbio and implemented at EMBO; launched
in 2019. The journal-independent peer-review model.)

[12] F1000Research. (Ongoing.) <https://f1000research.com>.
(Post-publication peer-review platform operated by Taylor &
Francis since 2020.) Founding paper: Tracz, V., & Lawrence, R.
(2016). Towards an open science publishing platform. *F1000Research*,
5, 130. DOI: 10.12688/f1000research.7968.1.

[13] Eisen, M. B., Akhmanova, A., Behrens, T. E., Diedrichsen, J.,
Harper, D. M., Iordanova, M. D., Weigel, D., & Zaidi, M. (2022).
Peer review without gatekeeping. *eLife*, 11, e83889.
DOI: 10.7554/eLife.83889. PMID: 36263932. (The October 2022 eLife
editorial announcing the end of accept/reject decisions after peer
review.)

[14] SHERPA/RoMEO (now Open Policy Finder, operated by JISC).
(Ongoing.) <https://openpolicyfinder.jisc.ac.uk/>. (Publisher
preprint and self-archiving policy database. The authoritative
reference for journal-by-journal preprint policy.)

[15] cOAlition S. (Ongoing.) Plan S Principles and Implementation.
<https://www.coalition-s.org>. (The cOAlition S funder consortium
open-access requirements that drive preprint adoption among
funded researchers in Europe.)

[16] National Institutes of Health (NIH). (2024; effective 1 July
2025). 2024 NIH Public Access Policy. <https://publicaccess.nih.gov>.
Policy notice NOT-OD-25-047 (original effective date 31 December
2025; requirements):
<https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-047.html>.
See also NOT-OD-25-101, Notice of updated effective date for the
2024 NIH Public Access Policy:
<https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-101.html>.

[17] Howard Hughes Medical Institute (HHMI). (Ongoing.) Research
policies: publishing and sharing.
<https://www.hhmi.org/about/policies/publishing-sharing>. (Index
page for HHMI's Open Access to Publications Policy, effective
through 31 December 2025, and its Immediate Access to Research
Policy, effective 1 January 2026 [26].)

[18] Fu, D. Y., & Hughey, J. J. (2019). Releasing a preprint is
associated with more attention and citations for the peer-
reviewed article. *eLife*, 8, e52646.
DOI: 10.7554/eLife.52646. PMID: 31808742. (Empirical evidence on
preprint-citation relationship.)

[19] Fraser, N., Momeni, F., Mayr, P., & Peters, I. (2020). The
relationship between bioRxiv preprints, citations and altmetrics.
*Quantitative Science Studies*, 1(2), 618-638.
DOI: 10.1162/qss_a_00043. (Finds higher citation and altmetric
counts for bioRxiv-deposited articles, and says further research
is needed to establish causality. Replaces "Wang et al. 2024,
*JMLA* 112(1)", whose DOI is not registered and whose PMID
38486838 resolves to an unrelated retraction notice.)

[20] arXiv. (2026, 1 October). Fair moderation, equitable access,
and AI: arXiv's updated rate limit policy. *arXiv blog*.
<https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/>.

[21] arXiv. (2025, 31 October). Attention authors: updated practice
for review articles and position papers in arXiv CS category.
*arXiv blog*.
<https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/>.

[22] openRxiv. (2025, 11 March). Introducing openRxiv: a new
independent home for preprint sharing in the life sciences.
<https://openrxiv.org/introducing-openrxiv/>. News coverage:
Naddaf, M. (2025). Preprint sites bioRxiv and medRxiv launch new
era of independence. *Nature* (news).
DOI: 10.1038/d41586-025-00762-4.

[23] eLife. (2024, addendum 2025). Changes to eLife's indexing
status in Web of Science and Scopus.
<https://elifesciences.org/inside-elife/ae620829/changes-to-elife-s-indexing-status-in-web-of-science-and-scopus>.

[24] National Institutes of Health. (2025). NOT-OD-25-138: Request
for information on maximizing research funds by limiting allowable
publishing costs.
<https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-138.html>.
Status as of March 2026: Wood, E. (2026, 20 March). Guest post — All
the seats at the table: a summary and status review of the NIH APC
caps proposal. *The Scholarly Kitchen*.
<https://scholarlykitchen.sspnet.org/2026/03/20/guest-post-all-the-seats-at-the-table-a-summary-and-status-review-of-the-nih-apc-caps-proposal/>.
Re-checked 20 October 2026 against NIH's list of selected policy
notices, <https://grants.nih.gov/policy-and-compliance/notice-of-policy-changes>,
which lists no notice finalising publication-cost limits. The list
is described as "selected" notices, so absence there is strong but
not conclusive evidence that no cap has been finalised.

[25] Wellcome. (Ongoing.) Open access policy.
<https://wellcome.org/research-funding/guidance/ending-a-grant/open-access-guidance/open-access-policy>.
(APC rule effective 1 January 2025. The page showed no
last-updated date when re-checked in October 2026.)

[26] Howard Hughes Medical Institute. (2025; effective 1 January
2026). Immediate Access to Research Policy.
<https://hhmicdn.blob.core.windows.net/policies/Immediate-Access-to-Research.pdf>.
(Issue date 24 September 2025; the PDF shows "Last Updated:
08/05/2026", i.e. 5 August 2026. Applies to the HHMI roles listed in
the policy and to original research articles that are major
contributions from their labs, (co-)first, (co-)last or
(co-)corresponding author; it does not apply to review articles,
perspectives, commentaries and similar.)

[27] Gates Foundation. (Ongoing; refreshed policy effective 1
January 2025). Open Access Policy.
<https://openaccess.gatesfoundation.org/open-access-policy/>.
("It is the foundation's expectation that Funded Manuscripts shall be
shared promptly in the form of a preprint … except where the grantee
determines that a preprint is not appropriate due to ethical, safety
or other legitimate concerns." Re-checked 20 October 2026.)
