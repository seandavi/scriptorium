# Preprint landscape: servers, post-publication review, and the moving boundary

*Last updated: 2026-05-20*

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

**arXiv** (Cornell, founded 1991 by Paul Ginsparg) is the original
and the model. Initially physics, expanded to mathematics, computer
science, quantitative biology, economics, statistics, and several
others. arXiv applies endorsement-based moderation (new authors
must be endorsed by an existing author) and minimal subject-area
screening; the time-stamp is the durable contribution. By 2024,
arXiv hosted roughly 2.5 million papers across categories [5,
TODO verify exact current count]. The CS subfields have built an
entire publication culture around arXiv-first posting; physics and
math have done so for longer.

**bioRxiv** and **medRxiv** are operated by Cold Spring Harbor
Laboratory Press. bioRxiv (launched 2013) covers preclinical and
basic biology; medRxiv (launched 2019, joint with BMJ and Yale)
covers clinical research. Both apply a screening process focused
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
Elsevier in 2016) is the social sciences and economics preprint
server with substantial uptake in finance, law, and accounting
but increasingly contested governance after the Elsevier
acquisition [8].

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
journal's preprint policy**.

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
shift. eLife eliminated the accept/reject decision in late 2022;
under the current model, eLife reviews any preprint the editors
select for review and publishes the resulting Public Reviews
alongside the preprint as a "reviewed preprint", with no final
acceptance gate. The author can revise; eLife continues to
review revisions; the preprint and its review record are the
publication. This is the most aggressive existing implementation
of the post-publication-review model at a high-impact journal.

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
  preprints directly for review.

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
open repository for funded research. **NIH's 2025 Public Access
Policy** [16] requires deposit of accepted manuscripts in PubMed
Central upon publication. **Wellcome Trust** requires open access
at publication, with preprint deposit accepted as compliance for
some cases. **Howard Hughes Medical Institute (HHMI)** has been
particularly strong on preprint encouragement [17].

For an automated venue-fit recommendation, funder-driven
constraints are hard filters: a Wellcome-funded researcher
recommended to submit to a subscription journal without an OA
option is recommended to violate their funder agreement. The skill
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
  uniform.

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
   so the author sees the trade-offs.

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
   journal without an OA option is a wrong recommendation.

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
emphasis accordingly.

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

[3] Polka, J. K., Penfold, N. C., Sever, R., Inglis, J. R., Pinto,
N., & Whyte, S. (2024). State of preprinting in the life sciences.
*Annual Review of Biomedical Data Science*. [TODO verify volume
and pages; the citation is from a Polka et al. recent review of
biomedical preprinting state-of-the-art. The ASAPbio website at
asapbio.org has primary documentation if the formal citation needs
adjustment.] (Survey of the biomedical preprint landscape.)

[4] Maggio, L. A., Artino, A. R., Picho, K., & Driessen, E. W.
(2020). Are you sure you want to do that? Fostering the
responsible use of preprints. *Medical Education*, 54(7), 631-634.
DOI: 10.1111/medu.14181. PMID: 32249938. (Editorial caution about
the clinical-medicine specifics of preprint risk.)

[5] arXiv. (Ongoing.) About arXiv. <https://arxiv.org/about>.
(Primary source for arXiv submission counts, moderation policy,
and history.)

[6] Cold Spring Harbor Laboratory Press. (Ongoing.) About
medRxiv. <https://www.medrxiv.org/about-medrxiv>. (medRxiv
screening criteria, particularly the clinical-screen layer.)

[7] Brierley, L., Nanni, F., Polka, J. K., Dey, G., Pálfy, M.,
Fraser, N., & Coates, J. A. (2022). Tracking changes between
preprint posting and journal publication during a pandemic.
*PLoS Biology*, 20(2), e3001285.
DOI: 10.1371/journal.pbio.3001285. PMID: 35104289. (The
preprint-to-published-version drift during COVID-19 — concrete
evidence of preprint version-control risks.)

[8] Tay, A. (2017). The future of SSRN — bought by Elsevier in
2016. Blog post archive. [TODO verify primary documentation; the
SSRN-Elsevier acquisition controversy is well-documented across
scholarly-communication-Twitter from 2016-2017 but the
peer-reviewed analysis is thinner.] (Documents the controversy
around governance changes after the Elsevier acquisition.)

[9] Peer Community In (PCI). (Ongoing.) <https://peercommunityin.
org>. (Community-run discipline-specific preprint recommendation
system; founding paper is Casadevall & Fang 2014 on the
peer-review economy, but PCI itself was founded 2016 by Dominique
Bourgeon, Thomas Guillemaud, and Denis Bourguet at INRAE.)

[10] Bourguet, D., Guillemaud, T., & Bourgeon, D. (2017). Peer
Community In: a recommendation process for preprints. *PCI
Documentation*. <https://peercommunityin.org>. [TODO verify a
formal citation for the PCI design paper; the documentation site
is the primary source but a peer-reviewed account of PCI's
methodology would be the stronger reference.]

[11] Review Commons. (Ongoing.) <https://reviewcommons.org>.
(Refereed-preprint service operated by ASAPbio and EMBO Press;
the journal-independent peer-review model.)

[12] F1000Research. (Ongoing.) <https://f1000research.com>.
(Post-publication peer-review platform operated by Taylor &
Francis since 2020.) Founding paper: Tracz, V., & Lawrence, R.
(2016). Towards an open science publishing platform. *F1000Research*,
5, 130. DOI: 10.12688/f1000research.7968.1.

[13] Eisen, M. B. (2022). Peer review without journals: A new
era for eLife. *eLife*. [TODO verify exact citation; eLife
announced the model change in October 2022 via an editorial.] The
model change is documented at the eLife website and in
contemporary scholarly-communication coverage.

[14] SHERPA/RoMEO (now Open Policy Finder, operated by JISC).
(Ongoing.) <https://openpolicyfinder.jisc.ac.uk/>. (Publisher
preprint and self-archiving policy database. The authoritative
reference for journal-by-journal preprint policy.)

[15] cOAlition S. (Ongoing.) Plan S Principles and Implementation.
<https://www.coalition-s.org>. (The cOAlition S funder consortium
open-access requirements that drive preprint adoption among
funded researchers in Europe.)

[16] National Institutes of Health (NIH). (2024). 2024 NIH Public
Access Policy. <https://publicaccess.nih.gov>. (NIH's 2025-effective
public-access policy requiring deposit in PubMed Central upon
publication.)

[17] Howard Hughes Medical Institute (HHMI). (Ongoing.) HHMI
Open Access Policy. <https://www.hhmi.org/about/policies/
open-access>. (HHMI's preprint and OA requirements; one of the
most prescriptive funder-side policies.)

[18] Fu, D. Y., & Hughey, J. J. (2019). Releasing a preprint is
associated with more attention and citations for the peer-
reviewed article. *eLife*, 8, e52646.
DOI: 10.7554/eLife.52646. PMID: 31808742. (Empirical evidence on
preprint-citation relationship.)

[19] Wang, J., Lai, J., Yang, X., Lin, Z., Liang, S., Lin, Z.,
Zhao, Z., Tian, Y., Wei, X., Lin, J., & Wei, S. (2024). Effect
of preprint posting on subsequent article citations: A bibliometric
analysis. *Journal of the Medical Library Association*, 112(1),
57-66. DOI: 10.5195/jmla.2024.1684. PMID: 38486838. [TODO verify;
preprint-citation effect studies are now numerous; this is a
representative recent analysis. The Fu & Hughey study above is the
more-cited foundational reference.]
