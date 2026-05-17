# The reproducibility crisis as the framing context for scriptorium

*Last updated: 2026-05-17*

## Synthesis

The reproducibility crisis is not a vague rhetorical backdrop;
it is a documented, decade-long, multi-field empirical finding that
**a substantial fraction of published findings do not replicate**.
The headline numbers — ~36% replication rate in psychology [1],
~62% in social-science experiments published in *Nature* and
*Science* [2], ~46% in preclinical cancer biology [3] — are
field-specific but mutually corroborating. The crisis is real, the
causes are now reasonably well understood (low statistical power,
selective reporting, p-hacking, under-specified methods, weak
incentives for replication and for transparency), and the reform
agenda has consolidated around concrete instruments: pre-registration,
registered reports, data sharing, code sharing, and the TOP
Guidelines [4, 5, 6].

For scriptorium, the connection is direct and load-bearing.
The system's most distinctive design choices —
`preserve_citations: true`, `preserve_statistics: true`,
`avoid_hype: true`, structured citation auditing, the
conservative-edit posture in [[semantic-preservation]] — are not
productivity features. They are **a response to specific documented
failure modes in the literature**: citation overreach (see
[[citation-overreach-research]]), citation distortion (Greenberg
2009 in [[forensic-methodology]]), statistical inconsistency (see
[[statistical-inconsistency]]), and the LLM-era amplification of
all of the above through hallucination (see
[[hallucination-in-llm-citations]]). Framed this way, scriptorium is
**reproducibility infrastructure at the manuscript layer** —
pre-submission, author-side, before the document enters the
literature.

Making this framing explicit in the JOSS paper and in DESIGN.md
strengthens scriptorium's thesis considerably. It elevates the
project from "writing tool" to "first-pass quality-assurance layer
for the post-reproducibility-crisis manuscript". This is also the
honest framing of what scriptorium can and cannot do.

## Evidence and frameworks

### Empirical replication studies

**Open Science Collaboration (2015).** [1] The landmark psychology
replication project. One hundred experimental and correlational
studies from three top psychology journals were replicated using
high-powered designs and original materials when available.
Headline result: 97% of original studies reported statistically
significant findings; only 36% of replications did. Replication
effect sizes were on average about half of original effect sizes.
The study was deliberately not designed to estimate "the true
replication rate of psychology" — that was the press headline, not
the paper's claim — but the magnitude of the gap between original
and replication results was striking enough to galvanise the field.

**Camerer et al. (2018).** [2] A targeted replication of 21
experimental social-science studies published in *Nature* and
*Science* (2010–2015). Pre-registered, average ~5× original sample
size. Sixty-two per cent of effects replicated in the same direction
and at statistical significance; replication effect sizes averaged
~50% of original. The pattern — fewer significant replications, and
smaller effects when they do replicate — is consistent with the
psychology project and is now the canonical signature of selective
reporting and publication bias.

**Errington et al. (2021), Reproducibility Project: Cancer Biology.** [3]
A coordinated attempt to repeat 193 experiments from 53 high-impact
cancer-biology papers. After significant attrition, 50 experiments
from 23 papers were ultimately completed. For positive effects, the
median replication effect size was 85% smaller than the original; on
combined positive and null effects, success rate was 46%. Beyond the
quantitative findings, the *qualitative* finding was that none of the
target experiments could be replicated from the methods sections
alone — clarifications from original authors were required in every
case, and roughly two-thirds required protocol modifications. The
methods-section opacity finding is in some ways the more actionable
result: it implicates writing practice directly, not just analysis
practice.

### Causes and the reform agenda

**Ioannidis (2005).** [7] The most-cited theoretical analysis of why
most published findings should be expected to be false. Ioannidis
combined Bayesian reasoning with field-level estimates of pre-study
odds, sample sizes, bias parameters, and the number of competing
teams to argue that the *positive predictive value* of a published
finding is often well below 50%. The argument is normative rather
than empirical — a derivation, not a measurement — but it predicts
exactly the replication-rate signal subsequently observed and remains
the dominant theoretical frame. Already cited in
[[hallucination-in-llm-citations]] as the prior-art warning that the
literature is unreliable even before LLMs got their hands on it.

**Munafò et al. (2017), "A manifesto for reproducible science."** [4]
The consolidation document for the reproducibility-reform movement.
Identifies failure modes at four levels — methods, reporting and
dissemination, reproducibility, and evaluation/incentives — and
specifies countermeasures at each: pre-registration, multi-arm
replication, registered reports, open data, open code, reporting
checklists, and incentive structures. The manifesto is the most
cited single reference for the modern reform programme.

**Nosek et al. (2015), TOP Guidelines.** [5] The *Transparency and
Openness Promotion* guidelines were developed by a working group
hosted at the Center for Open Science. Eight transparency standards
(citation, data, materials, code, design, research materials,
analytic methods, replication, registration) each defined at three
levels (encouragement, requirement, verification). The TOP framework
gives journals a vocabulary for "how transparent do we require
authors to be?" and has been adopted by over a thousand journals.
For scriptorium, TOP is the *external* schema against which a
manuscript's transparency can be assessed; reporting-guideline
adherence (EQUATOR; see [[reporting-guidelines]]) is the *internal*
equivalent.

### The post-crisis reform infrastructure

The reform agenda is no longer aspirational. It has institutional
form:

- **Registered reports** — pre-acceptance based on methods, not
  results. Now offered by ~300 journals.
- **Pre-registration** at the Open Science Framework, AsPredicted,
  ClinicalTrials.gov, and similar repositories. EU CTR 536/2014
  requires pre-registration for clinical trials in EU member states.
- **Open data and open code** mandates, increasingly required by
  funders (NIH 2023 data-sharing policy, NSF, Wellcome Trust,
  European Research Council).
- **Reporting checklists** (CONSORT, STROBE, ARRIVE, MIAME, MDAR;
  see [[reporting-guidelines]]) — the field-specific implementations
  of "what must a methods section actually contain".
- **Post-publication forensics** (image, statistics, text, network;
  see [[forensic-methodology]]) — the catch-the-rest-after-publication
  layer.

The reform agenda is now mature enough that *failure to comply* is
the anomaly rather than the norm at well-managed journals. The gap
is between the high-end journals and the long tail.

## How this informs scriptorium

The reproducibility crisis is the *raison d'être* of scriptorium's
most distinctive design choices. Making the link explicit elevates
the project's framing.

**Preservation constraints as anti-fabrication infrastructure.** The
`preserve_citations: true` and `preserve_statistics: true` defaults
in MANUSCRIPT_STATE are direct responses to: (a) LLM citation
hallucination ([[hallucination-in-llm-citations]]); (b) the
documented incidence of statistical inconsistency in published
literature ([[statistical-inconsistency]]); (c) citation overreach
in author practice ([[citation-overreach-research]]). The defaults
are not stylistic; they are post-crisis hygiene.

**Citation audit as Crossref/Retraction-Watch integration.** The
`citation-audit` skill (current) should explicitly check candidate
references against Crossref's retracted indicator
([[forensic-methodology]]). This is one of the cheapest, highest-
yield reforms a manuscript-layer tool can offer: prevent the
manuscript from citing already-retracted work. The deterministic
nature of the check — DOI in, retracted-flag out — makes it ideal
for an LLM-orchestrated skill, since no judgement is required.

**Reporting-guideline integration ([[reporting-guidelines]]).** TOP
and the field-specific reporting guidelines are the structural
backbone of pre-submission reproducibility. Scriptorium's
`reporting-checklist` skill should be field-aware (CONSORT for RCTs,
STROBE for observational, ARRIVE for animal, etc.). The skill's
output is a *gap list*, not a verdict.

**Methods-section opacity as a first-class concern.** Errington et
al.'s finding [3] that *no* cancer-biology paper could be replicated
from its methods section alone is a writing-practice indictment, not
just a statistics indictment. A future `methods-completeness` skill
that checks for protocol parameters known to matter (reagent
identifiers via RRIDs, software version pins, model identifiers,
randomisation procedures) is implied by the post-crisis evidence
and would be a high-value v0.3 candidate.

**`avoid_hype` is an empirical, not an aesthetic, default.** The
post-crisis consensus is that overclaiming and hedge-removal are
specific failure modes of the literature, not idiosyncratic
preferences. The `avoid_hype` constraint should be defended as
literature-supported, with [[citation-overreach-research]] and
Ioannidis [7] as the supporting evidence.

## Implementation priority for scriptorium

**Verdict:** **No new skill — high-value framing for DESIGN.md and
the JOSS paper.**

**Why useful context anyway:**

- The JOSS paper's thesis section should open with the
  reproducibility crisis as the motivation, citing Open Science
  Collaboration 2015, Camerer 2018, Errington 2021, Munafò 2017, and
  Ioannidis 2005. This anchors scriptorium as **a response to
  documented field-wide problems, not a productivity tool**.
- DESIGN.md should label each preservation constraint with its
  evidentiary basis: `preserve_citations` ← LLM hallucination +
  citation-distortion literature; `preserve_statistics` ← statistical
  inconsistency literature; `avoid_hype` ← citation-overreach +
  Ioannidis. The defaults are then visibly load-bearing.
- This framing also defines what scriptorium *does not* do:
  registered reports, pre-registration, replication coordination,
  open-data infrastructure, post-publication forensics. Naming what
  is out of scope is part of the honest pitch.

**Maybe-later flip conditions for new skills.** Three skills are
implied by the post-crisis evidence and become more plausible if
demand pulls:

1. `retraction-check` extension to `citation-audit` — already cheap
   and high-yield; arguably this is v0.2 not v0.3 (currently in
   citation-audit scope).
2. `reporting-guideline-gap` skill keyed to manuscript type — v0.3
   candidate (covered in [[reporting-guidelines]]).
3. `methods-completeness` skill (RRID coverage, software-version
   pins, model-identifier check) — v0.3+ candidate if author demand
   surfaces; non-trivial scope.

## Open questions / weak evidence

- The replication rates across fields vary widely; using "the
  reproducibility crisis" as a singular phenomenon obscures real
  cross-field heterogeneity. Scriptorium's framing should
  acknowledge the variation, not collapse it.
- Empirical evidence on what fraction of replication failures are
  due to *methods-section opacity* (vs. true non-replicability) is
  limited. Errington 2021's qualitative finding [3] is the strongest
  single data point and is suggestive rather than decisive.
- Whether a manuscript-layer tool actually moves the needle on
  pre-submission quality is itself an unaddressed empirical
  question. Scriptorium should be honest that the impact case is
  largely theoretical until evaluated.

## References

1. Open Science Collaboration. Estimating the reproducibility of
   psychological science. *Science*. 2015;349(6251):aac4716.
   doi:10.1126/science.aac4716. PMID: 26315443.
2. Camerer CF, Dreber A, Holzmeister F, et al. Evaluating the
   replicability of social science experiments in *Nature* and
   *Science* between 2010 and 2015. *Nature Human Behaviour*.
   2018;2:637–644. doi:10.1038/s41562-018-0399-z.
3. Errington TM, Denis A, Perfito N, Iorns E, Nosek BA. Investigating
   the replicability of preclinical cancer biology. *eLife*.
   2021;10:e71601. doi:10.7554/eLife.71601. See also companion
   meta-paper: Errington TM et al. Reproducibility in Cancer Biology:
   What have we learned? *eLife*. 2021;10:e75830.
   doi:10.7554/eLife.75830, and the project overview Errington TM
   et al., *eLife*. 2021;10:e67995. doi:10.7554/eLife.67995.
4. Munafò MR, Nosek BA, Bishop DVM, et al. A manifesto for
   reproducible science. *Nature Human Behaviour*. 2017;1:0021.
   doi:10.1038/s41562-016-0021.
5. Nosek BA, Alter G, Banks GC, et al. Promoting an open research
   culture. *Science*. 2015;348(6242):1422–1425.
   doi:10.1126/science.aab2374. PMID: 26113702.
6. Center for Open Science. TOP Guidelines.
   https://www.cos.io/initiatives/top-guidelines (accessed
   2026-05-17).
7. Ioannidis JPA. Why most published research findings are false.
   *PLoS Medicine*. 2005;2(8):e124.
   doi:10.1371/journal.pmed.0020124. PMID: 16060722.
