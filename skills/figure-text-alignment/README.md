# figure-text-alignment

Audit text-only alignment between figure captions and the body-text
sentences that reference them. For every figure, classify the
caption ↔ body-text-reference pair as
`aligned / partially aligned / misaligned / cannot determine`, and
flag pattern-level issues (orphan figure, phantom figure, panel
mismatch, axis/units divergence, direction divergence).

**Category:** critique
**Modifies the manuscript?** No.
**Reads figure images?** No, ever — this is the **text-only** subset.
The multimodal counterpart (sub-skill B) is explicitly deferred.
**Invocation:** explicit. Safe to suggest when a manuscript has at
least one figure with a caption and at least one body-text reference,
and is in `draft` / `revision` / `submission` phase.

## Scope: text-only

This is the v0.3 text-only sub-skill of figure-text alignment, per
[issue #14](https://github.com/seandavi/scriptorium/issues/14). It
checks alignment between two textual surfaces:

1. The **figure caption** — what the caption claims the figure shows.
2. The **body-text figure references** — sentences in the manuscript
   that say "Figure N shows X" or "as illustrated in Fig. N".

It does **not** look at the figure file itself. That is the job of
sub-skill B (multimodal), which is deferred until LLM-vision
reliability for scientific figures is validated against a
known-mismatch test set. The two failure modes are conceptually
separable — text-only catches caption/body-text disagreement, which
is a documented manuscript failure mode in its own right, while
multimodal would catch caption/image disagreement.

## What it does

For each (figure, body-text reference) pair, the four-step protocol
(mirroring [`citation-audit`](../citation-audit/README.md)):

1. **Extract** the caption's claim about the figure.
2. **Extract** the body-text reference's claim about the figure.
3. **Compare** on three axes: subject, direction/pattern, panel-and-axis
   specifics.
4. **Classify** the alignment.

Beyond per-pair alignment, it flags pattern-level issues:

- **Orphan figure** — figure exists but is never referenced in body text.
- **Phantom figure** — body text references "Figure N" but no Figure N
  caption exists.
- **Panel mismatch** — caption describes panels A/B/C; body text
  references a panel letter the caption does not define.
- **Axis / units divergence** — caption names units / scaling that the
  body text discusses in incompatible terms.
- **Direction divergence** — caption says one direction (decrease /
  downregulation); body text asserts the opposite for the same
  comparison.

The output is a structured markdown report with consistent section
headings so future orchestrators (the v0.2+ `manuscript-pipeline`
skill) can consume it.

## What it does not do

- **Read figure images.** Sub-skill B is the right skill for that and
  is deferred — see *Scope: text-only* above.
- **Verify axis labels rendered in the figure**, statistical
  annotations on the figure, or whether described trends are actually
  visible. All require reading the image.
- **Image integrity** (duplication, manipulation, splicing) — out of
  scope and out of scriptorium. Use Proofig, ImageTwin, or human
  inspection (see
  [`forensic-methodology`](../../knowledge/critique-techniques/forensic-methodology.md)
  for the boundary).
- **Modify the manuscript** or suggest specific rewrites. Flags
  misalignments; the author decides what to change.
- **Score the manuscript** on a quality scale. Audit is descriptive.
- **Operate on outline-phase manuscripts.** Figures are not yet
  stable; the skill declines cleanly.

## Inputs

- **Manuscript text** — file path(s) or pasted prose. Full prose,
  including figure captions and body-text references. For multi-file
  projects (e.g. Quarto with `sections` declared), every section file
  is read.
- **`MANUSCRIPT_STATE.yaml`** *(optional but recommended)* —
  `document_phase.current` (refuses on outline),
  `meta.guidance_level` (framing), `core_claims` (context). Figure
  locations are not declared in the schema; the skill discovers them
  from the manuscript text.

## Using it

### Inside Claude Code

```text
/scriptorium:figure-text-alignment
```

Then point Claude at the manuscript file(s) and ensure
`MANUSCRIPT_STATE.yaml` is reachable from the project root.

### Outside Claude Code (Codex, Gemini, Hermes, ChatGPT, …)

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to run
`figure-text-alignment` on your manuscript.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/figure-text-alignment/prompt.md
```

## Output structure

```markdown
# Figure-text alignment (text-only)

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

## Pattern flags
### Orphan figures
### Phantom figure references
### Panel mismatches
### Axis / units divergences
### Direction divergences

## What this skill did NOT check
```

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`visualization-figures`](../../knowledge/scientific-writing/visualization-figures.md)
  — primary grounding. Names figure-text alignment as a documented
  manuscript failure mode (wrong panel referenced, axis-unit
  mismatch, trends not visible in the cited figure, figure-counter
  drift). Anchors the text-only / multimodal split this skill
  embodies.
- [`internal-consistency`](../../knowledge/critique-techniques/internal-consistency.md)
  — frames figure-text alignment as a class of internal-consistency
  failure and provides the structured-output discipline.
- [`forensic-methodology`](../../knowledge/critique-techniques/forensic-methodology.md)
  — used here for the boundary statement. Image integrity is a
  different problem with different methodology and is emphatically
  out of scope.
- [`guidance-level`](../../knowledge/conventions/guidance-level.md)
  — scriptorium-wide convention for how much framing the skill adds.
- [`declared-work-scope`](../../knowledge/conventions/declared-work-scope.md)
  — scriptorium-wide convention. The skill operates on declared
  captions and declared body-text references; it does not generate
  captions or invent figure references.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Gradient over binary.** The most common real-world finding is the
  caption-and-body-text-mostly-agree-but-disagree-on-one-panel case;
  forcing yes/no answers loses load-bearing nuance.
- **Patterns over enumeration.** Twelve references to a single
  phantom figure are one pattern-flag row, not twelve.
- **Honest about the deferred multimodal sub-skill.** The "did NOT
  check" section names the deferral by name so authors do not
  mistake the text-only audit for a complete figure-text-alignment
  pass. Sub-skill B will ship when LLM-vision reliability on
  scientific figures is validated against a known-mismatch test set.

## See also

- [`citation-audit`](../citation-audit/README.md) — sibling critique
  skill, also operating on a four-step gradient classification.
  Figure-text alignment uses the same protocol pattern applied to a
  different text-vs-text comparison.
- [`terminology-normalization`](../terminology-normalization/README.md)
  — another internal-consistency-class skill, grounded in the same
  `internal-consistency` knowledge note.
- GitHub issue [#14](https://github.com/seandavi/scriptorium/issues/14)
  — the canonical tracking issue. Names the text-only / multimodal
  split this skill implements.
