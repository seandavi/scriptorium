# Discipline conventions beyond biomedicine

*Last updated: 2026-05-17*

## Synthesis

Scriptorium's knowledge base is biomedical-coded. IMRaD structure,
reporting guidelines like CONSORT and STROBE, first-author/last-author
anchors, and significance-positioning in the NIH style
([[nih-significance-patterns]]) are conventions of the life sciences
and medicine. Other disciplines write differently — sometimes
radically so. A physics PRL, a NeurIPS conference paper, a
single-author mathematics theorem-proof paper, an economics working
paper, and a humanities monograph chapter are different genres with
different success criteria. A tool that silently assumes biomedical
norms will produce confidently wrong critique on any of them.

The defensible move is not to build per-discipline skill variants
(high effort, uncertain value, ongoing maintenance) but to **state
the project's scope explicitly in `DESIGN.md` and in each skill's
description**. Swales' 2004 *Research Genres* [1] gives the
cross-disciplinary framework: genres vary along dimensions of
*structure*, *citation practice*, *audience model*, and *epistemic
norms*, and the variation is large enough that a single editing tool
cannot pretend neutrality. Saying so up front is more honest — and
more useful — than pretending otherwise.

## Evidence and frameworks

### Physics: PRL Letters and arXiv preprint norms

*Physical Review Letters* enforces a strict 4.5-printed-page limit
(approximately 3500 words) and explicitly forbids the standard
IMRaD section structure. A PRL is a single continuous argument, with
methods compressed into the body or relegated to supplementary
material. The implicit reader is assumed to know the field's prior
work and notation; introductions are typically a single paragraph.

The dominant submission norm in physics is to post to arXiv at or
before journal submission. The result is that the *preprint* is the
canonical version for the community; journal publication serves as
post-hoc validation. Scriptorium skills that assume "submission" is
a singular event will model this poorly.

### Computer science / machine learning

NeurIPS, ICML, ICLR, and related venues use **8–10 page main
paper + supplementary appendix** as the canonical format, with
double-blind peer review handled in 6–8 week conference cycles. The
8-page constraint is real and load-bearing: it forces a writing
style with dense figures, compressed related work, and methods
deferred to the appendix.

Specific conventions:
- Authorship is typically contribution-based, with no alphabetical
  convention.
- Code and data release are increasingly mandatory for camera-ready
  acceptance.
- Supplementary material has expanded rapidly; some papers' appendices
  now exceed the main paper in length.
- The "related work" section serves a different function than a
  biomedical introduction: it is closer to a positioning argument
  than a literature review.

A scriptorium audit calibrated for "is the introduction sufficiently
contextualised" will misfire on an ICML submission whose
introduction is intentionally compressed.

### Mathematics: theorem-proof-corollary

Mathematics papers are organised around the
**definition–theorem–proof–corollary–remark** structure rather than
IMRaD. Krantz's *A Primer of Mathematical Writing* [2] is the
standard reference for the genre. Key features:

- Figures are rare; the work happens in notation.
- Citation practice is sparser and more targeted; "see Smith
  (2018), Theorem 3.2" rather than a paragraph of context.
- Single- or few-author papers dominate; **alphabetical authorship
  is the default** outside biomedical/medical-statistics
  collaborations.
- Significance-positioning ([[significance-positioning]]) looks
  different: results are positioned relative to a known open
  problem or a structural place in a theory, not relative to
  population health.

A reviewer-simulation skill that probes for "what's the clinical
relevance" of a result in algebraic topology is not just
unhelpful — it is misframed.

### Economics

Economics papers are typically **long** (40–80 pages including
appendices), with extensive identification-strategy discussion,
robustness tables, and theoretical appendices. **Alphabetical
authorship by surname** is the field's default convention; deviations
are read as informative (a non-alphabetical order signals contribution
order). Working papers are first-class objects; journal publication
often comes years after the working paper has circulated.

John Cochrane's "Writing Tips for PhD Students" [3] is the most
widely cited internal guide and is worth reading just to see how
different the field's prose norms are: it explicitly tells students
that "you are primarily a writer", emphasises the one-paragraph
contribution statement, and advises against travelogue-style
methods sections.

### Humanities and qualitative social sciences

Humanities scholarship is **argument-driven** rather than IMRaD,
typically organised around an interpretive thesis defended through
close engagement with primary and secondary sources. The
epistemology is fundamentally different: claims are not validated by
replication or effect sizes but by the persuasiveness of the
argument and the depth of the engagement with prior scholarship.

Qualitative social science (ethnography, critical theory,
interpretive policy analysis) shares this orientation. Citation
practice is denser and more conversational ("as Foucault notes…").
Reporting guidelines analogous to CONSORT or PRISMA largely do not
apply, though there are emerging quality standards for some
qualitative subfields (e.g., COREQ, SRQR).

A `reviewer-simulation` calibrated on biomedical reviewer archetypes
([[reviewer-archetypes-evidence]]) will not approximate a humanities
reviewer. The epistemic dispositions are not the same.

### Engineering

Engineering bifurcates roughly into **design / system papers**
(novel artifact, characterisation, performance evaluation) and
**applied papers** (methodology applied to a problem). Journal
conventions vary by subfield (IEEE Transactions style is its own
universe). The genre is closer to ML than to biomedicine — figure-
and table-dense, with methods often embedded in implementation
details rather than separated.

### The cross-disciplinary frame

Swales' 2004 *Research Genres* [1] argues that genres differ along
at least the following dimensions, all of which matter for editing:

- **Structural conventions** (IMRaD vs. argument-essay vs.
  theorem-proof).
- **Citation density and integration style** (cf.
  [[esl-writers-swales-hyland]] on integral vs. non-integral
  citations).
- **Author–reader relationship** (presumed shared knowledge,
  formality, use of "we").
- **Evidence types** (experimental data, mathematical proof,
  archival sources, computational benchmarks).
- **Authorship conventions** (alphabetical, contribution-order,
  first-last anchored).

Treating all five of these as biomedical defaults is a scope
choice — scriptorium should be honest about it.

## How this informs scriptorium

1. **Add an explicit scope statement to `DESIGN.md`.** Something
   like: "Scriptorium's knowledge layer is calibrated for biomedical
   and life-sciences manuscripts. Skills will run on physics, CS,
   mathematics, economics, and humanities texts, but the heuristics
   embedded in critique skills assume biomedical conventions. Users
   working outside that scope should treat the output as advisory,
   not authoritative." This is a low-effort/high-value addition.

2. **Encode discipline in `MANUSCRIPT_STATE.yaml`.** The schema
   already has `target_venue`; add (or document) a discipline /
   field hint that skills can use to dial down or qualify their
   feedback. Even a single string ("biomedical" | "ml" |
   "physics" | "math" | "economics" | "humanities" | "engineering"
   | "other") is enough to let skills emit *"this check assumes
   biomedical conventions and may not apply to your field"*
   warnings.

3. **Don't build per-discipline skill variants in v0.1–v0.3.** The
   incremental value of `argumentative-flow-physics` over a
   well-scoped general `argumentative-flow` is small. The cost of
   maintaining five variants is high.

4. **Reviewer-simulation needs disciplinary calibration if it is
   to generalise.** The biomedical reviewer archetypes
   ([[reviewer-archetypes-evidence]]) are not portable.
   Cross-disciplinary calibration is a v0.4+ problem.

## Implementation priority for scriptorium

**Verdict:** No new skill in v0.1–v0.3. The implementation
priority is a **documentation change**: a scope statement in
`DESIGN.md` and a one-line scope note in each critique skill's
description.

**If Yes (later):** in v0.5+ ("knowledge layer + platform adapters"
phase in `DESIGN.md`), if scriptorium gains traction outside
biomedicine, add discipline-specific knowledge files under
`knowledge/disciplines/{physics,ml,math,economics,humanities}.md`
that individual skills reference explicitly. Required data: a
discipline hint in `MANUSCRIPT_STATE.yaml` and discipline-tagged
reviewer archetypes.

**Why useful context anyway:** This document scopes
scriptorium's claims. The biggest reputational risk for an
agentic editing tool is overconfident wrong output on a manuscript
type it wasn't designed for. Naming the scope is cheap defence.

**Condition that flips to Yes:** a non-biomedical user community
emerges and complains that scriptorium's biomedical defaults are
miscalibrated for their work. That's the trigger for
`knowledge/disciplines/` content, not before.

## Open questions / weak evidence

- The discipline boundaries are fuzzy. Computational biology shares
  ML conventions; biostatistics shares economics conventions;
  digital humanities shares CS conventions. A flat discipline tag
  in `MANUSCRIPT_STATE.yaml` will mislabel boundary cases.
- "Biomedical conventions" themselves vary — basic-science papers
  in *Cell* read differently than clinical trials in *NEJM*. A
  one-axis discipline scope is a simplification.
- Conference-vs-journal is sometimes a bigger split than
  field-vs-field. NeurIPS papers and biomedical papers differ less
  along some dimensions than NeurIPS and *Journal of Machine
  Learning Research* papers.

## References

[1] Swales, J. M. (2004). *Research Genres: Explorations and
Applications*. Cambridge University Press. ISBN 9780521533348
(paperback; hardback ISBN 9780521825603). [TODO verify hardback
ISBN.]

[2] Krantz, S. G. (2017). *A Primer of Mathematical Writing*,
Second Edition. American Mathematical Society. ISBN
9781470436582. (The originally referenced ISBN 9781470414597
appears not to correspond to the published second edition.)

[3] Cochrane, J. H. (2005, updated). *Writing Tips for PhD
Students*. Available at
https://www.johnhcochrane.com/research-all/writing-tips-for-phd-studentsnbsp
(no DOI; widely cited in economics-graduate-training materials).

[4] *Physical Review Letters* author guidelines. American Physical
Society. https://journals.aps.org/prl/authors. (Style and length
norms as of 2024–2026.)

[5] International Committee of Medical Journal Editors. ICMJE
Recommendations. https://www.icmje.org. (Provided as the
biomedical reference point against which other-discipline
conventions are contrasted.)
