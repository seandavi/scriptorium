# Predatory publishing: detection, taxonomy, and the moving landscape

*Last updated: 2026-05-20*

## Synthesis

"Predatory publishing" names the business model in which a venue
charges article-processing fees while providing little or no
editorial work, peer review, or indexing in return. The term
became broadly current with Jeffrey Beall's blog **Scholarly Open
Access**, which from 2008 until its abrupt removal in 2017
maintained the most-cited list of "potential, possible, or
probable" predatory journals and publishers [1]. Beall's list was
controversial in detail — accused of methodology issues, OA bias,
and individual misclassifications — but the underlying phenomenon
it documented is well-attested across the OA literature [2, 3].
Roughly two thirds of self-styled OA journals in the early 2010s
were estimated to be either definitively predatory or operating
without the quality controls a legitimate journal would maintain
[2]; that fraction has shifted as the legitimate OA infrastructure
matured, but the predatory landscape has matured too, and detection
remains an active problem.

Several patterns dominate the predatory operating model:

- **Pay-to-publish with no real peer review.** Submissions are
  accepted with no substantive revision or external review, often
  within days. The fee is the product.
- **Fabricated editorial boards.** Editorial lists frequently
  include real scholars who never agreed to serve, sometimes with
  affiliations the listed scholar never held.
- **Fake or misleading metrics.** Journals invent impact factor
  analogues ("Universal Impact Factor", "Global Impact Factor"),
  cite themselves to inflate Google Scholar h-index, or claim
  indexing in databases they're not in [4].
- **Hijacked journals.** Established journal titles are cloned at
  look-alike URLs to harvest fees from authors searching for the
  legitimate journal [5].
- **Aggressive solicitation.** Mass-emailed calls for papers
  targeting researchers who have published nearby, often with
  flattering personalisation lifted from public CVs.

For an automated tool like scriptorium, the consequence is twofold.
First, **the predatory layer cannot be ignored** — any venue
recommendation that doesn't filter for it is incomplete and
exposes the author to a real cost. Second, **detection is hard
in-band** and depends on community-maintained authoritative
sources. A tool that pretends to verify predatory status from
training-data knowledge alone will fail; the correct posture is to
apply published heuristics, defer to authoritative checklists
(Think.Check.Submit, COPE, DOAJ membership, Cabell's Predatory
Reports where the author has access), and refuse to recommend
anything the heuristics flag.

## Evidence and frameworks

### Beall's list: history and what it left behind

Beall's blog [1] ran from 2008 to January 2017, at which point it
was taken down without public explanation. Speculation centred on
legal pressure from listed publishers; Beall himself later wrote
about the experience in *Biochemia Medica* [6]. The blog's
specific recommendations are no longer available at the original
URL but are archived; the methodology Beall used has been
critiqued in detail [7, 8].

The most durable contribution of Beall's work was not the list
itself but the **publication of detection heuristics**. The
criteria Beall published (lack of editorial board, missing peer-
review process, fake metrics, unprofessional websites, predatory
solicitation language) became the reference taxonomy for
subsequent work. The criteria themselves are not in serious
dispute even when individual judgments using them were. A modern
detection effort still uses Beall's framework, just with more
maintained data sources.

### Successor resources

Several community and commercial resources have filled the gap
since 2017:

**Cabell's Predatory Reports** [9] is the commercial successor most
research libraries subscribe to. It maintains both a "Journal
Whitelist" (positively reviewed venues) and "Journal Blacklist"
(predatory or otherwise problematic venues), with documented
criteria for each listing. Access requires an institutional
subscription, which limits its reach for unaffiliated researchers
but makes it the most authoritative single source where access is
available.

**Think.Check.Submit** [10] is the community-maintained checklist
many editorial guides now point at. It does not maintain a list of
journals; it provides a structured checklist of questions an
author can answer about any specific venue before submitting. The
checklist covers editorial board verification, peer-review process
transparency, indexing claims, society affiliation, and contact
information consistency. Think.Check.Submit is the right resource
to recommend to authors as the **process** they should follow,
even when an automated tool has not flagged a specific concern.

**COPE (Committee on Publication Ethics)** [11] maintains a
membership-based set of publishing-ethics standards. COPE
membership is a positive signal but not a certification —
predatory publishers have applied for and even achieved COPE
listings before being removed, and many legitimate journals are
not COPE members because of cost or institutional structure.

**DOAJ (Directory of Open Access Journals)** [12] maintains a
curated list of OA journals meeting transparency and quality
criteria. DOAJ inclusion is a moderately strong positive signal;
DOAJ removal (the journal was once listed and then excluded) is a
strong negative signal worth surfacing if visible. The DOAJ Seal
indicator marks journals meeting additional rigor criteria.

**OASPA (Open Access Scholarly Publishers Association)** [13]
membership requires meeting publishing-practice standards
including peer-review documentation and editorial-board
transparency. OASPA membership is a positive signal for OA
publishers similar to DOAJ inclusion for journals.

For an automated venue-fit recommendation, the right posture is to
use these resources as soft signals — DOAJ inclusion is a positive
heuristic, Cabell's flagging is a negative heuristic — but not to
treat any single source as definitive. Predatory designation is
contested in detail and an automated tool should defer to
authoritative human-curated sources rather than rendering its own
judgments.

### Per-journal, not per-publisher: the MDPI nuance

A common error in informal predatory-detection lists is treating
entire publishers as predatory based on the worst journals in
their portfolio. The most cited contemporary case is **MDPI**, a
Basel-headquartered OA publisher with several hundred journals
spanning quality levels. MDPI as a publisher has been
controversial for years — high APCs, aggressive solicitation, fast
turnaround, and self-citation patterns drew scrutiny [14, 15] —
but the publisher includes journals that have built solid
reputations in their fields (*Sensors*, *Cells*, *International
Journal of Molecular Sciences*, *Cancers*) alongside journals
that have raised serious quality concerns. Treating MDPI as a
single entity is wrong in both directions: it would flag
legitimate venues and it would miss problems in specific journals
within the portfolio.

The principle: **predatory assessment must be per-journal, not
per-publisher**. The same publisher can host both a venue with
rigorous review and a venue with predatory characteristics. The
relevant question is always about the specific journal under
consideration, with the publisher as one signal among several.

### The Hindawi-Wiley case: when legitimate publishers degrade

In 2023-2024, Wiley closed 19 Hindawi-acquired journals after
documented manipulation by paper mills [16, 17]. Hindawi had been
a long-standing OA publisher acquired by Wiley in 2021;
subsequent investigation found that several of its journals had
been heavily compromised by special-issue submission patterns
correlating with paper-mill operations. The case is significant
for venue-fit work because it demonstrates that **legitimacy is
not permanent**: a journal can move from defensible to compromised
within a few years, especially in the OA-special-issue model where
revenue scales with publication volume and editorial oversight can
lag.

Practical consequence: a venue-fit recommendation based on
training-data knowledge of a journal's status from before the
events in question is potentially stale. The skill must caveat
that its knowledge has a date stamp and that authors should verify
current status via Think.Check.Submit or DOAJ at submission time.

### Hijacked journals

A distinct subcategory worth naming: **hijacked journals**, where
a predatory operation creates a look-alike domain or even a full
clone of a legitimate journal's website to intercept submissions
and fees [5]. The legitimate journal still exists at its real URL;
authors searching the journal name and clicking the wrong result
end up paying APCs to the hijacked version, which provides no
actual publication or indexing.

Detection requires URL verification rather than name verification.
A skill recommending venues should provide the verified URL for
each recommendation and flag any case where multiple URLs are
associated with a single journal name (a common signal of
hijacking in progress).

## How this informs scriptorium

For `venue-fit` specifically:

1. **Predatory refusal is a load-bearing posture, not an aside.**
   No recommendation list includes a flagged venue. The skill
   maintains a `## Predatory signals detected` section in its
   output even when no candidates were flagged, stating
   explicitly that the check was applied — silence here is
   indistinguishable from "we didn't check", which is the wrong
   inference for the author to draw.

2. **Use per-journal, not per-publisher, judgments.** The skill
   does not flag a publisher as predatory; it flags a specific
   journal as predatory if the heuristics fire. MDPI and similar
   mixed-portfolio publishers require per-journal assessment.

3. **Defer to authoritative human-curated resources where they
   exist.** Think.Check.Submit, DOAJ, OASPA, and Cabell's are
   the references. The skill applies published Beall-style
   heuristics and, when uncertain, says so and points the author
   at the authoritative source rather than guessing.

4. **Caveat staleness.** Training-data knowledge of a venue's
   status is potentially out of date. The skill's recommendation
   output names this explicitly: "venue status assessed from
   training data through [model knowledge cutoff date]; verify
   current status via Think.Check.Submit at submission."

5. **Hijacked-journal protection via URL verification.** When
   recommending a venue, the skill provides a verified URL and
   flags multiple-URL situations. The recommendation includes the
   verified URL even when the author hasn't asked, because the
   missing-URL failure mode is silent.

6. **Refuse cleanly at the boundary.** When the author asks
   whether a specific journal is predatory, the skill answers
   based on the heuristics it can apply. When the heuristics are
   inconclusive, it says so, names the heuristics it checked, and
   points the author at Think.Check.Submit for the remaining
   verification steps. It does not invent a verdict.

## Implementation priority for scriptorium

**Verdict:** Direct grounding for the `venue-fit` skill (v0.2).
The predatory-publishing dimension is first-class, not an aside.
Without this grounding the skill would be incomplete — the most
expensive misfit failure mode for an author is publishing in a
predatory venue, and not flagging that is worse than not
recommending at all.

**Why useful context anyway:**

- The per-journal-not-per-publisher principle applies to any
  future scriptorium work that assesses venues (e.g., a
  hypothetical preprint-server fit skill would face the same
  question about preprint-server moderation rigor varying within
  a publisher).

- The staleness caveat — "training-data knowledge has a date
  stamp; verify current status" — is the same shape as the
  citation-audit caveat about CSL metadata not standing in for
  full-text verification. It's a principle: an LLM-driven tool
  must be honest about what its training data can and can't
  attest to about the current world.

- The "use authoritative human-curated sources" pattern is
  duplicated across multiple knowledge notes in this layer
  ([[predatory-publishing]] for venues, [[citation-claim-
  alignment]] for full-text verification, [[reporting-
  guidelines]] for checklists). Worth being explicit that this
  is a project-wide pattern: scriptorium is the assistant on the
  edge of the workflow; authoritative sources of truth remain
  external.

**Condition that would flip this:** if a maintained, machine-
queryable predatory-detection API emerges (Cabell's API access at
scale, a successor to Beall's list with API endpoints), the skill
could shift from heuristic-based flagging to API-driven flagging.
That's a future capability, not a v0.2 dependency.

## Cross-references

- [[venue-selection]] — venue-fit's primary grounding; predatory
  refusal is the layer applied across every recommendation that
  note produces.
- [[editorial-decision-making]] — desk-rejection rates and editor
  triage; predatory venues are by construction not in this
  framework.
- [[reference-managers]] — adjacent territory; reference managers
  face the parallel "is this citation real" problem that
  predatory journals create downstream of acceptance there.
- [[declared-work-scope]] — the convention. Predatory venue
  refusal is consistent with the principle: scriptorium operates
  on declared work and refuses to recommend venues that would
  exploit that work.

## References

[1] Beall, J. (2008-2017). *Scholarly Open Access*. Blog.
Original URL no longer active (removed 2017-01-15); archived at
the Internet Archive and Wayback Machine.

[2] Shen, C., & Björk, B.-C. (2015). 'Predatory' open access: a
longitudinal study of article volumes and market characteristics.
*BMC Medicine*, 13, 230. DOI: 10.1186/s12916-015-0469-2.
PMID: 26423063. (The empirical estimate of predatory OA scale in
the early-to-mid 2010s.)

[3] Kakamad, F. H., Mohammed, S. H., Najar, K. A., Qadr, G. A.,
Ahmed, J. O., Mohammed, K. K., Salih, R. Q., Hassan, M. N., Mikael,
T. M., Kakamad, S. H., Baba, H. O., Salih, A. M., Othman, S., &
Ahmed, M. S. (2019). Kscien's list; a new strategy to discourage
predatory journals and publishers. *International Journal of
Surgery Open*, 17, 5-7. DOI: 10.1016/j.ijso.2019.01.002. [TODO
verify exact volume/page; the Kscien list itself is the more
durable reference here than the methodology paper.]

[4] Jalalian, M., & Mahboobi, H. (2014). Hijacked journals and
predatory publishers: Is there a need to re-think how to assess
the quality of academic research? *Walailak Journal of Science and
Technology*, 11(5), 389-394. (Early documentation of the
"hijacked journals" pattern.)

[5] Dadkhah, M., Maliszewski, T., & Teixeira da Silva, J. A.
(2016). Hijacked journals, hijacked web-sites, journal phishing,
misleading metrics, and predatory publishing: actual and potential
threats to academic integrity and publishing ethics. *Forensic
Science, Medicine, and Pathology*, 12(3), 353-362.
DOI: 10.1007/s12024-016-9785-x. PMID: 27342770. (More extensive
taxonomy of hijacking and metric-faking patterns.)

[6] Beall, J. (2017). What I learned from predatory publishers.
*Biochemia Medica*, 27(2), 273-278.
DOI: 10.11613/BM.2017.029. PMID: 28694718. (Beall's own post-shut-
down reflection on the methodology and the pressures.)

[7] Olivarez, J. D., Bales, S., Sare, L., & vanDuinkerken, W.
(2018). Format aside: Applying Beall's criteria to assess the
predatory nature of both OA and non-OA library and information
science journals. *College & Research Libraries*, 79(1), 52-67.
DOI: 10.5860/crl.79.1.52. (Independent application of Beall's
criteria to non-OA journals — finds the criteria flag
problematic non-OA venues too, suggesting the criteria are about
quality, not OA-ness per se.)

[8] Berger, M., & Cirasella, J. (2015). Beyond Beall's list:
Better understanding predatory publishers. *College & Research
Libraries News*, 76(3), 132-135. DOI: 10.5860/crln.76.3.9277.
(Critique of Beall's methodology and the OA-vs-predatory
conflation; widely cited.)

[9] Cabell's International. (Ongoing.) *Predatory Reports*
(formerly *Cabell's Blacklist*). <https://www2.cabells.com>.
Subscription required. (Commercial successor to Beall's list;
the most authoritative single source where access is available.)

[10] Think.Check.Submit. (Ongoing.) *Choose the right journal for
your research*. <https://thinkchecksubmit.org>. (Community-
maintained checklist; the recommended process resource for
authors. Funded jointly by COPE, DOAJ, OASPA, and others.)

[11] Committee on Publication Ethics (COPE). (Ongoing.) *COPE
Core Practices*. <https://publicationethics.org>. (Membership-
based publishing ethics standards.)

[12] Directory of Open Access Journals (DOAJ). (Ongoing.)
<https://doaj.org>. (Curated OA journal directory; DOAJ Seal
indicates additional rigor criteria.)

[13] Open Access Scholarly Publishers Association (OASPA).
(Ongoing.) <https://oaspa.org>. (Membership organisation for OA
publishers; membership criteria publicly listed.)

[14] Crosetto, P. (2021). Is MDPI a predatory publisher? *Blog
post*. <https://paolocrosetto.wordpress.com/2021/04/12/
is-mdpi-a-predatory-publisher/>. (Influential informal analysis
of MDPI's growth and self-citation patterns. Conclusion:
publisher-level designation is wrong, but specific concerns about
specific journals within the portfolio are real. The reference is
a blog post rather than a peer-reviewed paper; cited here because
it is the most widely-referenced contemporary discussion of the
MDPI question.)

[15] Petrou, C. (2022). Guest Post — MDPI's Remarkable Growth.
*The Scholarly Kitchen*. <https://scholarlykitchen.sspnet.org/
2020/08/10/guest-post-mdpis-remarkable-growth/>. [TODO verify
date; the URL slug suggests 2020 not 2022.] (Industry-side
analysis of MDPI's growth and the structural questions it raised
about the OA-special-issue model.)

[16] Else, H. (2024). Paper-mill detector put to the test in
biggest-ever publishing-fraud sweep. *Nature*, 627, 261-262.
DOI: 10.1038/d41586-024-00580-0. (Coverage of the Wiley-Hindawi
shutdown and the paper-mill detection work behind it.)

[17] Brainard, J. (2023). Fake scientific papers are alarmingly
common. *Science*, 380(6645), 568-569.
DOI: 10.1126/science.adi9617. (Broader context on paper-mill
operations and their effect on OA-venue integrity.)
