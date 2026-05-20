# Visualization and figure design in scientific manuscripts

*Last updated: 2026-05-17*

## Synthesis

Figure design has its own foundational literature, parallel to the
sentence-level writing literature scriptorium already engages with.
Tufte's *The Visual Display of Quantitative Information* (1983;
2nd ed. 2001) [1] is the canonical statement of the design
principles — maximise data-ink, minimise chartjunk, small multiples,
data density, narrative integration with text. Wilkinson's *The
Grammar of Graphics* (1999; 2nd ed. 2005) [2] is the formal-system
counterpart: a generative grammar for statistical graphics that
underlies ggplot2 and virtually every modern visualisation
framework. *PLOS Computational Biology*'s "Ten Simple Rules for
Better Figures" (Rougier, Droettboom, Bourne 2014) [3] and Rolandi,
Cheng & Pérez-Kriz's *Advanced Materials* guide (2011) [4] are the
practitioner-oriented translations of those principles into
scientific-figure practice.

The under-researched problem in this space is **figure-text
alignment**: does the figure caption actually describe what the
figure shows, and does the body-text discussion of the figure
match what the figure displays? Anecdotal evidence — visible in
any thorough peer review — is strong that misalignment is common
(wrong axis units called out, wrong panel referenced, claims about
patterns the figure does not actually exhibit). Formal corpus
studies of figure-text alignment in scientific articles are rare;
the closest adjacent literature is image-forensics work on
duplication and manipulation (Bik et al. 2016; see
[[forensic-methodology]]), which addresses figure *integrity* rather
than figure-text *consistency*.

For scriptorium specifically, this opens a candidate skill —
`figure-text-alignment` — that is technically interesting but
limited by current LLM capability to actually read scientific
figures. Multimodal models can parse simple charts and extract
axes and labels; they struggle with complex multi-panel figures,
specialised plots (volcano plots, dimensional-reduction
projections, Manhattan plots, gel images), and panel-level
sub-references. The skill is worth scoping as v0.3 with explicit
LLM-capability honesty: catch the cheap misalignments
(panel-numbering, axis-unit mismatches, figure-counter drift) and
route the harder ones to human review.

## Evidence and frameworks

### Tufte and the data-ink tradition

Tufte's *The Visual Display of Quantitative Information* [1]
introduced and codified the design principles that now define
serious quantitative graphics:

- **Data-ink ratio.** Maximise the proportion of ink/pixels devoted
  to data; minimise non-data ink (heavy gridlines, redundant scale
  labels, decorative shading).
- **Chartjunk.** Decoration that adds no information actively
  degrades the figure.
- **Small multiples.** Arrays of similar small figures support
  comparison across conditions without imposing scale-switching
  cost on the reader.
- **Graphical integrity.** The visual representation must be
  proportional to the data; broken axes, truncated zero, and
  area-vs-length encoding errors mislead readers.
- **Narrative integration.** The figure exists to support a claim
  in the text; figures and text together are the unit of
  argument, not separate artefacts.

Tufte's later books — *Envisioning Information* (1990), *Visual
Explanations* (1997), *Beautiful Evidence* (2006) — extend the
framework but the 1983/2001 volume is the operational reference.

### Wilkinson's grammar of graphics

Wilkinson's *Grammar of Graphics* [2] is a different kind of
contribution: a formal generative grammar for statistical graphics.
Any graphic is decomposed into:

- **Data** — variables and observations.
- **Aesthetics** — mappings from variables to visual channels
  (position, colour, size, shape).
- **Geometries** — the marks (points, lines, bars).
- **Statistics** — transformations of the data (binning, smoothing,
  summary statistics).
- **Scales** — mappings from data range to display range.
- **Coordinate system** — Cartesian, polar, etc.
- **Facets** — partitioning into small multiples.

The grammar is the intellectual substrate of ggplot2 (Wickham
2016), Vega-Lite, Altair, and virtually every modern declarative
plotting framework. For scriptorium, the grammar is useful because
it gives a structured vocabulary for describing what a figure
*should* contain. A figure-text alignment skill that knows what
the data, aesthetic mappings, and statistics of a figure are has
specific things to check the text against; one that treats the
figure as an opaque pixel array does not.

### Practitioner translations

**Rougier, Droettboom & Bourne (2014).** [3] The most cited
practical guide for scientific figures, in *PLOS Computational
Biology*'s Ten Simple Rules series. The ten rules: know your
message; know your audience; identify the right type of plot;
captions are not optional; do not trust the defaults; use colour
effectively; do not mislead the reader; avoid chartjunk; message
trumps beauty; get the right tool. All ten map cleanly onto
checkable properties of a figure-plus-caption pair, which is part
of the reason the paper has the citation traction it does.

**Rolandi, Cheng & Pérez-Kriz (2011).** [4] An *Advanced Materials*
brief guide co-authored by a scientist, a graphic designer, and a
cognitive psychologist. The contribution is the cognitive-design
overlay: figures should support the reader's cognitive task, not
just display the data. Cognitive-load framing (see
[[hayes-flower-writing-model]]) applies in the visual modality —
unnecessary distinctions in colour, irrelevant panels, distant
legend-to-data placement, all add extraneous load.

**Stephen Few, *Information Dashboard Design* (2nd ed. 2013).** [5]
The dashboard-design literature is adjacent but increasingly
relevant as scientific figures move into interactive and
dashboard-style forms (Shiny apps, IIIF viewers, paper-companion
explorables). Few's emphasis on pre-attentive processing and
at-a-glance comprehension is operationally translatable.

### Figure-text alignment

This is the under-studied area. The peer-review literature
([[critique-quality-evidence]]) consistently identifies figure-text
misalignment as a high-frequency reviewer concern:

- Caption references the wrong panel ("Figure 2A shows X" when the
  X is in Figure 2B).
- Axis units in the body text disagree with axis units in the figure.
- Sample sizes claimed in text differ from those visible in the
  figure (numbers in bars, n= labels in caption).
- Discussion of a "trend" or "pattern" that is not visible in the
  cited figure.
- Figure counter drift — Figure 4 in the file is referenced as
  Figure 5 in the text after a mid-revision insertion.
- Colour-blindness violations (red/green encoding) when the caption
  asserts accessibility compliance.

Quantitative corpus work on figure-text misalignment specifically
is sparse. The closest adjacent corpus work is in image-forensics
([[forensic-methodology]]), which catalogues duplication and
manipulation but not text-misalignment, and in caption-quality
studies (largely informal commentary). No formal figure-text-
alignment corpus or prevalence study was located during this sweep;
the absence is itself worth noting — practitioners assert these
errors are common but, to our knowledge, no peer-reviewed prevalence
estimate exists.

### Image forensics overlap

Bik et al. (2016) [6] — already detailed in
[[forensic-methodology]] — established that ~3.8% of biomedical
papers contain inappropriately duplicated images. Most of those
issues are *integrity* failures (panel re-use, contrast
manipulation) rather than *alignment* failures (caption-figure
mismatch). The two failure modes are conceptually separable:
- **Integrity**: the figure does not honestly represent the
  underlying data.
- **Alignment**: the figure and the surrounding text disagree.

Scriptorium's natural focus is alignment, not integrity, because
alignment is text-tractable and integrity requires image processing.

## How this informs scriptorium

A `figure-text-alignment` skill is a v0.3 candidate, with explicit
limits on what it can deliver.

**What is tractable for an LLM-only skill:**

- **Cross-reference consistency.** Does every `Figure N` reference
  in the body text correspond to a figure with caption "Figure N"?
  Does every figure-with-caption have at least one body-text
  reference? This is deterministic string-matching, not LLM
  judgement.
- **Panel-letter consistency.** Does "Figure 3B" in the text match
  a panel labelled "B" in Figure 3's caption?
- **Axis-unit and sample-size cross-check.** If the caption says
  "n=24" and the body text says "twenty patients", flag the
  discrepancy. Same for units (μg vs. mg, log-fold-change vs.
  fold-change).
- **Counter drift.** If figures are reordered, ensure body-text
  references are updated.

**What is partially tractable with multimodal LLMs:**

- **Axis label match.** If the LLM can read the figure, does the
  axis label match the variable the caption and body text describe?
- **Plot-type match.** If the caption says "boxplot" and the figure
  is a barplot, flag it.
- **Colour-channel description.** If the caption asserts colour
  coding by category and the figure uses gradient colour, flag it.

Multimodal capability is improving but is unreliable for: complex
multi-panel figures, specialised scientific plot types (volcano
plots, MA plots, Manhattan plots, k-mer spectra, gel/Western
images), figures with embedded annotations and arrows, and any
figure where extraction of panel-level data points is required.
The skill must default to *flagging* rather than asserting, and
must produce inspectable output where the LLM's reading of the
figure is exposed alongside its claim.

**What is not tractable:**

- **Image integrity** (duplication, manipulation). Belongs to
  Proofig / ImageTwin / human inspection; scriptorium should not
  pretend to do this.
- **Pattern-claim verification** (is the trend the author describes
  actually visible?). Requires quantitative inspection of the
  underlying data, not just the rendered figure.
- **Statistical-claim verification from figures** (is the p-value
  in the figure consistent with the rendered effect size?).
  Requires the underlying data.

**Preservation contract.** A figure-text-alignment skill that
*modifies* text to fix references must respect the preservation
constraints in [[semantic-preservation]] — particularly
statistic-string preservation. A skill that "fixes" "Figure 4" to
"Figure 5" must not also silently change "n=24" to "n=20" because
the LLM thinks they should match.

**Reporting.** The skill's output should be a structured list of
candidate inconsistencies, each with:
- Location in body text (paragraph, sentence).
- Location in figure asset (panel, caption line).
- Type of inconsistency (counter drift, axis-unit mismatch, etc.).
- Confidence (high for deterministic checks, low for LLM-vision
  claims).
- Suggested fix (without auto-applying it).

## Implementation priority for scriptorium

**Verdict:** **Maybe later** — `figure-text-alignment` is plausibly
v0.3 but should not ship before its capability limits are honest.

**Condition that would flip to Yes:**

- Multimodal LLM capability on scientific figures becomes
  demonstrably reliable for the bounded sub-tasks listed above
  (axis-label match, plot-type match, panel-letter check).
- Author demand surfaces — the skill is most valuable to
  high-volume authors and to groups with many trainees producing
  draft manuscripts.
- The deterministic sub-skills (cross-reference consistency,
  panel-letter consistency, counter drift, axis-unit cross-check)
  are independently valuable and could ship earlier as a
  text-only first cut.

**If Yes (anticipated scope):**

- **Skill name**: `figure-text-alignment`
- **Phase**: v0.3 (after the conservative-edit posture and
  preservation reporting are well-established).
- **Scope**:
  - **Sub-skill A (text-only, deterministic)**: cross-reference
    consistency, panel-letter consistency, counter drift,
    axis-unit/sample-size cross-check. Shippable earlier, possibly
    in v0.2.
  - **Sub-skill B (multimodal)**: axis-label match, plot-type
    match, colour-channel description, gated behind a
    `multimodal_enabled` flag in MANUSCRIPT_STATE. Outputs are
    surfaced as low-confidence flags requiring human review.
- **Required data**:
  - Figure assets (PDF / PNG / SVG referenced from the manuscript).
  - Captions in machine-readable form.
  - `MANUSCRIPT_STATE.figure_index` listing every figure with its
    file path and caption.
  - For Sub-skill B, multimodal-capable model access.

**Honest limits:**

- Sub-skill B will produce false positives on specialised plot
  types (volcano plots, etc.). The skill must reserve flagging
  language for unambiguous cases.
- Image integrity is **out of scope** and must be named as such;
  the skill should explicitly cite Proofig / ImageTwin and direct
  authors to those tools (see [[forensic-methodology]]).
- The skill must not silently rewrite captions; misalignments
  surface as candidates for human resolution.

## Open questions / weak evidence

- Formal corpus data on figure-text misalignment prevalence is
  sparse. Anecdotal evidence is strong but a peer-reviewed
  estimate of "what fraction of submissions have misaligned
  figure references" appears to be missing. *What would close
  this gap: a corpus study analogous to Bik et al. (2016) for
  image duplication, but targeting caption-vs-body and
  axis-label-vs-body alignment.*
- Multimodal LLM accuracy on scientific figures is improving
  rapidly but is not benchmarked specifically for the
  text-alignment task scriptorium would deploy. Internal
  evaluation is required before any Sub-skill B claims.
- The boundary between figure-text alignment and
  pattern-claim-verification is fuzzy. A claim that "Group A is
  higher than Group B" requires either trust in the rendered
  figure or independent access to the data; the latter is out of
  scope.

## References

1. Tufte ER. *The Visual Display of Quantitative Information*.
   2nd ed. Graphics Press; 2001. ISBN 9781930824133.
2. Wilkinson L. *The Grammar of Graphics*. 2nd ed. Springer; 2005.
   ISBN 9780387245447. doi:10.1007/0-387-28695-0.
3. Rougier NP, Droettboom M, Bourne PE. Ten simple rules for
   better figures. *PLoS Computational Biology*. 2014;
   10(9):e1003833. doi:10.1371/journal.pcbi.1003833.
4. Rolandi M, Cheng K, Pérez-Kriz S. A brief guide to designing
   effective figures for the scientific paper. *Advanced Materials*.
   2011;23(38):4343–4346. doi:10.1002/adma.201102518. PMID:
   21960472.
5. Few S. *Information Dashboard Design: Displaying Data for
   At-a-Glance Monitoring*. 2nd ed. Analytics Press; 2013. ISBN
   9781938377006.
6. Bik EM, Casadevall A, Fang FC. The prevalence of inappropriate
   image duplication in biomedical research publications. *mBio*.
   2016;7(3):e00809-16. doi:10.1128/mBio.00809-16. PMID: 27273827.
