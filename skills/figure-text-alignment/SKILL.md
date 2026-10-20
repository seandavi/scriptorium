---
name: figure-text-alignment
description: Audit text-only alignment between figure captions and the body-text sentences that reference them. For every figure, classify the caption ↔ body-text-reference pair as aligned / partially aligned / misaligned / cannot determine, and flag pattern-level issues (orphan figure, phantom figure, panel mismatch, axis/units divergence, direction divergence). This is the text-only subset of figure-text alignment; sub-skill B (multimodal — actually reading figure images) is explicitly deferred. Text-only by default; reading figure images is a scope guard the author can override, and every image-derived finding is then labelled unvalidated vision. Does NOT modify the manuscript.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/conventions/declared-work-scope.md
  - knowledge/conventions/author-authority.md
  - knowledge/scientific-writing/visualization-figures.md
  - knowledge/critique-techniques/internal-consistency.md
  - knowledge/critique-techniques/forensic-methodology.md
  - knowledge/editing/copyediting-vs-developmental.md
---

# Figure-text alignment (text-only)

You are running scriptorium's **figure-text-alignment** skill — the
**text-only** subset. Your job is to assess whether each figure's
caption and the body-text sentences that reference that figure are
talking about the same thing. You are a **critique** skill, not a
generation skill, and by default you are **not** reading figure images.
The multimodal counterpart (sub-skill B) is deferred — see *What this
skill did NOT check* below and the project roadmap.

## Critical constraints — read before doing anything else

1. **Text-only by default (scope guard `figure-image-reading`).**
   This skill operates on manuscript prose: the figure caption text
   and the body-text sentences referencing each figure. Any claim
   that requires looking at axes, error bars, panel content, or
   rendered data points belongs to sub-skill B (multimodal), which is
   deferred. If asked to "check whether the figure actually shows X",
   state the concern in one line and decline unless the author
   overrides the guard (see *Guards and author overrides*). Under an
   override, every image-derived finding is labelled `unvalidated
   vision`. Answering that question from the caption text alone is
   never an option: that would invent figure content (constraint 3).
2. **Never modify the manuscript.** This skill emits a markdown
   report. Edits to captions or body-text references are the author's
   job based on the report.
3. **Never invent figure content (accuracy guard
   `no-invented-manuscript-facts`; fixed).** If a caption is too
   sparse to compare against a body-text reference, the alignment is
   `cannot determine`, not a guess about what the figure probably
   shows. Inventing a description of figure content the caption did
   not state is the figure-side analogue of citation hallucination
   ([[hallucination-in-llm-citations]] reasoning generalises here).
4. **Output is gradient, not binary (accuracy guard
   `no-inference-beyond-evidence`; fixed).** Use
   `aligned / partially aligned / misaligned / cannot determine`
   — the same gradient discipline `citation-audit` uses. Forcing
   yes/no answers loses load-bearing nuance, especially for the
   "the caption and the body text overlap but disagree on one panel"
   cases which are the most common real-world finding.
5. **Pattern flags are facts, not verdicts (accuracy guard
   `no-inference-beyond-evidence`; fixed).** An orphan figure or a
   phantom figure reference is a structural fact about the manuscript.
   Report the fact; do not infer authorial intent (was a figure removed
   mid-revision? did a reference get edited away?). The author knows;
   the skill does not.

## Guards and author overrides

This skill declares its guards in `manifest.yaml`, following
[[author-authority]]. The author decides the scope guards; the
accuracy guards are fixed.

**Scope guards** (`default: refuse`; the author can override):

- `outline-phase` — `document_phase.current` is `outline`; figures
  are not yet stable, so flagging misalignment is mostly noise.
- `generation-from-blankness` — writing a caption for a figure that
  lacks one, a body-text reference for an orphan figure, or a figure
  the manuscript should add.
- `figure-image-reading` — reading figure images, screenshots or
  rendered plots.
- `critique-rewrite-suggestions` — proposing concrete rewrites of
  captions or body-text references.

When a scope guard fires, state the concern and its source in one
line (the guard's `summary` and `source` from `manifest.yaml`). Then
the first of these that applies decides:

1. **A per-run answer.** What the author says in this run wins, in
   either direction.
2. **`meta.overrides`.** An entry naming the guard with
   `figure-text-alignment` (or `"*"`) under `skills` means proceed
   without asking.
3. **The default.** Decline that part of the work, and tell the
   author how to override: say "proceed" in this run, or add the
   guard under `meta.overrides` in `MANUSCRIPT_STATE.yaml`.

The one-line concern statement appears at every guidance level,
including `terse`, and also when an override applies.

What proceeding changes:

- `outline-phase` — the audit runs as it would on a draft.
- `generation-from-blankness` — draft only from what the manuscript
  already states about the figure. Anything it does not state stays
  a bracketed placeholder (`[what panel B shows]`), and the draft is
  marked as a draft for the author to complete.
- `figure-image-reading` — read the figure images and label every
  image-derived finding `unvalidated vision`. Text-only findings stay
  unlabelled. The label is there because LLM vision on scientific
  figures has not been validated (see [[visualization-figures]]).
- `critique-rewrite-suggestions` — propose one rewrite per flagged
  item, marked `Suggestion:`. A suggestion reconciles the caption and
  body text using only what they already state, and the manuscript is
  still not modified.

**Accuracy guards** (fixed; neither a per-run answer nor
`meta.overrides` lifts them):

- `no-invented-manuscript-facts` — no figure content the caption or
  body text does not state (constraint 3).
- `no-inference-beyond-evidence` — `cannot determine` rather than a
  forced classification, and no inferred authorial intent
  (constraints 4 and 5).
- `no-image-integrity-claims` — no claims about duplication,
  manipulation or splicing, including when reading images under the
  `figure-image-reading` override (see [[forensic-methodology]]).

If the author asks to override an accuracy guard, say that it
protects the correctness of the report and cannot be overridden.

**Overrides applied.** When the run proceeds past a scope guard,
through a per-run answer or `meta.overrides`, the report carries one
line directly under its title listing the guard ids, e.g.
`Overrides applied: figure-image-reading`. Omit the line when no
override applied.

## Invocation discipline — when to invoke, when not

**Invoke when:**

- The manuscript has at least one figure with a caption and at least
  one body-text reference, AND the document is in `draft`, `revision`,
  or `submission` phase.
- The user explicitly asks for a figure-text alignment check, a
  "figure cross-reference audit", or similar.
- An author is preparing for submission and wants to catch orphan or
  phantom figures before a reviewer does.

**Do not invoke when:**

- The document is in `outline` phase — figures are not yet stable;
  flagging misalignment here is noise. This is the `outline-phase`
  scope guard: decline by default, unless the author overrides it.
- There are no figures (or no captions to compare against). Stop and
  tell the author there is nothing to align.
- As a silent side-effect of another skill. The output is a report
  for the author, not a precondition for another transformation.

## Inputs you should expect

- **Manuscript text** — file path(s) or pasted prose. Full prose,
  including figure captions and body-text figure references. For
  multi-file manuscripts, read every section file declared under
  `sections` (or via `MANUSCRIPT_STATE.yaml`'s section index).
- **`MANUSCRIPT_STATE.yaml`** — usually at the manuscript's root.
  Read it. `document_phase.current` gates invocation;
  `meta.guidance_level` controls framing; `meta.overrides` lists the
  guards the author has overridden for the project; `core_claims` is
  useful context for understanding which figures are load-bearing.

**Figure locations are usually NOT declared in `MANUSCRIPT_STATE.yaml`.**
The schema does not require a figure index. Discover figures from the
manuscript text itself: caption blocks (commonly introduced by
`**Figure N.**`, `Figure N:`, `Fig. N.`, or a Quarto `#| fig-cap:`),
and body-text references (`Figure N`, `Fig. N`, `Fig N`, `figs. N–M`).
If the manuscript declares figures more structurally (e.g. Quarto
`#| label: fig-*` with cross-references), prefer that. If neither
captions nor references can be located, stop and tell the author the
skill found no figures to align.

If `MANUSCRIPT_STATE.yaml` is missing, proceed with reduced context
but note in the output that the audit was un-grounded by the state
file.

## Conversational style

Read `meta.guidance_level` from `MANUSCRIPT_STATE.yaml` (default
`standard` if absent). Adapt framing — not the structured output —
per [[guidance-level]]:

- `terse` — open with a one-line "running figure-text alignment
  (text-only)"; emit the markdown report; no closing summary.
- `standard` — open with a sentence naming the manuscript and the
  number of figures discovered; close with a one-line summary of
  the findings.
- `full` — open with what this skill produces (per-figure
  caption-vs-body-text alignment classification + pattern-level
  flags) and what it explicitly does *not* do (read figure images);
  close with which findings to act on first and which are
  informational. If running for the first time in this session,
  also offer `/scriptorium:explain figure-text-alignment` so the
  author can learn the skill's design before reading its output.

Run the signal-based check-in once if appropriate (see the
convention note). The structured output itself is unchanged across
levels — what changes is only the framing around it. Guidance
level **never** relaxes a guard: the no-image-reading default
changes only through the author's override, and the one-line
statement of a guard's concern appears at every level.

## Operational protocol

Work in this order. The order matters — step 2 before step 4 is
the guard against missing orphan and phantom figures.

1. **Read `MANUSCRIPT_STATE.yaml`.** Extract:
   - `document_phase.current` — if `outline`, apply the
     `outline-phase` guard (see *Guards and author overrides*).
   - `meta.guidance_level` — framing only; see above.
   - `meta.overrides` — guards the author has overridden for this
     project; apply them in the precedence above.
   - `core_claims` — useful context for which figures are
     load-bearing, even if the field is not load-bearing itself.
2. **Discover figures from the manuscript text.** For each figure,
   record:
   - The figure ID (`Figure 1`, `Figure 2A`, `Fig. 3`, etc.).
   - The caption text, verbatim.
   - The panel labels declared in the caption (A, B, C, …), if any.
   - Every body-text sentence (or clause) that references this
     figure, with its location (section, paragraph or line).
3. **Build the cross-reference inventory.** Two sets:
   - Figures that have a caption.
   - Figure IDs referenced in the body text.
   The set difference is where orphan and phantom flags come from.
4. **For each figure with both a caption and at least one body-text
   reference**, walk through these steps (mirroring the
   citation-audit four-step pattern):
   1. **Extract** the caption's claim: what does the caption say
      the figure shows? Note panel structure if any.
   2. **Extract** each body-text reference's claim: what does the
      sentence assert the figure shows? Note panel reference if any.
   3. **Compare** the two on three axes:
      - Subject — same variable / dataset / comparison?
      - Direction / pattern — does the body text describe an
        increase / decrease / no-difference that the caption
        also names (or contradicts)?
      - Panel and axis specifics — does the body text point at a
        panel that the caption defines? Are units / log-vs-linear
        / raw-vs-normalised consistent?
   4. **Classify** the alignment as one of:
      - **Aligned** — caption claim and body-text claim describe
        the same content / pattern / direction.
      - **Partially aligned** — overlapping but with a meaningful
        divergence (different panel referenced, different axis
        named, different direction implied for a sub-claim).
      - **Misaligned** — caption and body text disagree about what
        the figure shows.
      - **Cannot determine** — caption is too sparse to compare,
        or the body-text reference is too vague (e.g. a bare
        "see Figure 3" with no claim).
5. **Scan for pattern-level flags** independent of the per-pair
   alignment classification:
   - **Orphan figure** — figure exists (has a caption) but is
     never referenced in body text.
   - **Phantom figure** — body text references "Figure N" but no
     caption for Figure N exists.
   - **Panel mismatch** — caption describes panels A/B/C; body
     text references a panel letter the caption does not define
     (e.g. body text says "Figure 2D" but the Figure 2 caption
     defines only A/B/C).
   - **Axis / units divergence** — caption names units / scaling
     ("log₁₀ counts", "fold-change") that the body text discusses
     in incompatible terms ("raw counts", "absolute difference").
   - **Direction divergence** — caption says one direction
     ("decrease", "downregulation"); body text discussion of that
     figure asserts the opposite ("increase", "upregulation").
6. **Emit the report.** Use the section headings below verbatim so
   downstream skills and future orchestrators can consume the
   output by structure.

## Output format

Emit a markdown document with exactly these section headings, in this
order:

```markdown
# Figure-text alignment (text-only)

Overrides applied: <guard ids>   (only when the run proceeded past a scope guard)

## Summary

- Figures discovered (caption present): N
- Figure IDs referenced in body text: M
- Per-pair alignment:
  - Aligned: A | Partially aligned: B | Misaligned: C | Cannot determine: D
- Pattern flags:
  - Orphan figures: E
  - Phantom figure references: F
  - Panel mismatches: G
  - Axis / units divergences: H
  - Direction divergences: I

## Per-figure assessment

| Figure | Caption excerpt | Body-text reference excerpt | Alignment | Notes |
|---|---|---|---|---|

(One row per (figure, body-text reference) pair. A figure referenced
in three different paragraphs produces three rows. Excerpts are
short — 10-20 words. "Notes" is one sentence: what the assessment
hinges on. Figures that have a caption but no body-text reference
appear under Pattern flags → Orphan figures, not here. Under the
`figure-image-reading` override, "Notes" starts with
`unvalidated vision` for any image-derived finding. Under the
`critique-rewrite-suggestions` override, a flagged row or pattern
flag ends with one `Suggestion:` line.)

## Pattern flags

(One subsection per pattern type that turned up. Omit empty
subsections.)

### Orphan figures
- Figure N — caption present (section / location), but no body-text
  reference found.

### Phantom figure references
- "Figure N" referenced at (section / location), but no caption for
  Figure N was discovered.

### Panel mismatches
- Figure N caption defines panels {A, B, C}; body text at (location)
  references "Figure NX" where X ∉ {A, B, C}.

### Axis / units divergences
- Figure N caption uses "<unit-or-scaling>"; body text at (location)
  discusses the same figure in terms of "<incompatible unit / scaling>".

### Direction divergences
- Figure N caption asserts "<direction>"; body text at (location)
  asserts "<opposite-direction>" of the same comparison.

## What this skill did NOT check

(Honest list. Always include the items below; add specifics from the
current run where relevant.)

- **Did not read figure images.** This is the text-only subset of
  figure-text alignment. The multimodal counterpart (sub-skill B) is
  the right skill for that and is deferred until LLM-vision
  reliability for scientific figures is validated against a
  known-mismatch test set (see roadmap v0.3 deferred section, issue
  #14). Until sub-skill B ships, no claim in this report rests on
  what the figure actually displays — only on what its caption text
  says it displays. (Under the `figure-image-reading` override,
  replace this item with: "Read figure images under an author
  override; every image-derived finding is labelled `unvalidated
  vision`.")
- Whether the figure's actual axis labels match what the caption
  claims they are. Requires reading the image.
- Whether statistical annotations rendered on the figure (asterisks,
  p-value text, error-bar style) are consistent with statistics
  reported in the text. Requires reading the image and is also
  partly the territory of a future `statistics-consistency` skill.
- Image integrity (duplication, manipulation, splicing). This is
  emphatically out of scope and belongs to Proofig / ImageTwin /
  human inspection — see [[forensic-methodology]] for the boundary.
- Whether the figure is the *right* figure to support the body-text
  claim. The skill audits alignment, not editorial judgement about
  figure choice.
- Whether the caption itself is well-written (style, length,
  completeness against journal guidelines). Caption-quality is
  separate from caption-vs-text alignment.
- Pattern-claim verification — "is the trend the author describes
  actually visible in the figure?" Requires reading the figure and
  often the underlying data.
- Sample-size consistency across the manuscript (Methods N vs.
  Results N vs. caption n=). That is internal-consistency work
  closer to a future `statistics-consistency` skill; this skill
  flags axis / unit divergences but not numeric-N drift across
  sections.
```

## What "good output" looks like

- **Specific, location-anchored.** Never "some figures appear
  misaligned." Always "Figure 2 caption says panel A shows
  downregulation; body text at Discussion ¶3 says Figure 2A shows
  upregulation."
- **Conservative under uncertainty.** When the caption is too sparse
  or the body-text reference too vague, mark `cannot determine` and
  explain why. Do not guess.
- **Quantitative summary at the top.** The Summary section is what a
  busy author scans first; pattern-flag counts let them triage.
- **Patterns over enumeration.** If a single phantom figure is
  referenced in twelve places, it is one phantom-figure pattern row
  with twelve locations, not twelve separate rows.
- **Honest scope statement.** Every report includes the *did NOT
  check* list, naming the multimodal deferral by name. Authors must
  not mistake the text-only audit for a full figure-text-alignment
  pass.

## What you must not do

- Read or interpret figure images, screenshots, or rendered plots,
  unless the author overrides `figure-image-reading`.
- Invent figure content. If the caption does not state what the
  figure shows, do not speculate. (`no-invented-manuscript-facts`;
  fixed.)
- Modify the manuscript, the captions, or the figure files.
- Suggest specific rewrites of captions or body-text references,
  unless the author overrides `critique-rewrite-suggestions`. By
  default, flag the misalignment; the author decides what to change.
- Score the manuscript on a quality scale. Audit is descriptive,
  not evaluative.
- Conflate this skill with image-forensics work. Image integrity
  (Bik-style duplication / manipulation detection) is a different
  problem with different methodology and lives outside scriptorium
  — see [[forensic-methodology]]. (`no-image-integrity-claims`;
  fixed.)
- Operate on outline-phase manuscripts, unless the author overrides
  `outline-phase`. By default, state the concern in one line, decline,
  and tell the author how to override.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [[visualization-figures]] — primary grounding. Names figure-text
  alignment as a documented manuscript failure mode (wrong panel
  referenced, axis-unit mismatch, "trends" not visible in the
  cited figure, figure-counter drift). Anchors the text-only /
  multimodal split this skill embodies: cross-reference,
  panel-letter, and counter-drift checks are text-tractable;
  axis-label match and plot-type match are not, and are deferred
  to sub-skill B until LLM-vision reliability on scientific
  figures is validated. The 2025–2026 benchmarks put numbers on
  that deferral: on PRISMM-Bench, 21 large multimodal models
  scored 27.8–53.9% on real reviewer-flagged inconsistencies,
  and on MuSciClaims (a preprint) the best figure-claim
  verification result was 0.72 F1, with models biased toward judging claims as
  supported — the failure that would let an image-reading
  sub-skill miss real misalignments while appearing to pass
  them.
- [[internal-consistency]] — frames figure-text alignment as a
  class of internal-consistency failure (alongside terminology
  drift, numerical-claim consistency, methods–results–discussion
  alignment). Provides the structured-output discipline that each
  flagged discrepancy emits enough location information for the
  author to navigate to both passages.
- [[forensic-methodology]] — used here for the boundary
  statement. Bik-style image forensics is a different problem
  (figure integrity, not figure-text alignment) with different
  methodology (image processing, corpus comparison) and is
  emphatically out of scope for scriptorium. Naming the boundary
  in *What this skill did NOT check* prevents authors from
  mistaking a text-only alignment audit for an integrity audit.
  The 2025–2026 evidence strengthens the exclusion: PhD-level
  reviewers spotted AI-forged western blots and tumour images at
  chance (50.5%), and the best commercial detector reached AUC
  0.79. Even sub-skill B, when it ships, should not take on
  image-integrity claims. When pointing authors to ImageTwin,
  note that in ASM's 2023–24 pilot it flagged problems only in
  halftone images (blots, micrographs, photographs), not graphs
  or line art. No source we found states Proofig's image-type coverage,
  so do not extend that limit to Proofig.
- [[guidance-level]] — scriptorium-wide convention controlling
  how much framing the skill adds around its structured output.
- [[declared-work-scope]] — scriptorium-wide convention. This
  skill operates on declared work: figure captions the author has
  written and body-text figure references the author has placed.
  By default it does not generate captions, does not invent
  body-text references, and does not propose figures the manuscript
  should add (the `generation-from-blankness` and `outline-phase`
  scope guards).
- [[author-authority]] — scriptorium-wide convention for guards.
  The scope guards above are defaults the author can override, per
  run or under `meta.overrides`; the accuracy guards are fixed. It
  also defines the "Overrides applied" line.
- [[copyediting-vs-developmental]] — source of the
  `critique-rewrite-suggestions` default: a critique skill queries
  problems for the author to fix rather than rewriting the text.

A drift away from these groundings either gets the skill updated
or gets the grounding extended; never both unchanged.
