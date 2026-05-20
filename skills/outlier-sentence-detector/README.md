# outlier-sentence-detector

Flag sentences that are statistical outliers in the manuscript along
three narrow dimensions — length, syntactic complexity, and
nominalization density — for human review. Calibrates against the
manuscript's own distribution so flags adapt to the author's baseline
rather than a universal target.

**Category:** critique
**Modifies the manuscript?** No. The skill emits a report with
flagged candidates and per-row rationale; the author decides what
(if anything) to act on.
**Invocation:** explicit. This is a late-stage line-editing
diagnostic the author asks for, not a precondition for another skill.

## What it is — and what it explicitly is not

This skill **flags candidates for human review**. It is **not** a
writing-quality score. It never produces an overall rating, grade,
percentage, pass/fail, or any single number that purports to summarise
the manuscript's prose. Per the grounding note
[`quantitative-quality-measures`](../../knowledge/scientific-writing/quantitative-quality-measures.md):

> "There is no single number that captures [writing quality], and
> any tool that produces one is throwing information away. The useful
> operations are outlier flagging."

Outlier flagging is what this skill does. Quality scoring is not.

The grounding note's verdict is **Selective Yes**: general-purpose
writing-quality scores (Flesch-Kincaid, SMOG, Coleman-Liau,
BERTScore-as-a-gate) are theatre for scientific text — they
systematically mis-score correctly-used technical terminology as
"difficult" and penalise legitimate nominalisation. Narrow
outlier-detection skills are defensible because they surface
candidates for human review without claiming to measure quality.
This skill is the v0.3 cash-out of that *Selective Yes*.

## What it does

For each sentence in the manuscript, the skill computes three
properties and surfaces outliers in each dimension:

- **Length outliers.** Sentences whose word count is far from the
  manuscript's median (>2.5σ above the median, with an absolute
  floor of 35 words for short documents).
- **Complexity outliers.** Sentences with unusually high clause
  depth, measured by a defensible proxy: count of commas plus
  subordinators (`although`, `because`, `since`, `while`, `whereas`,
  `if`, `unless`, `when`, `where`, `which`, `who`, `that`,
  `whether`, `before`, `after`) plus coordinated-conjunction stacks.
  No full grammar parser; the proxy is cheap and enough to find
  outliers.
- **Nominalization-density outliers.** Sentences where a high
  fraction of content words are nominalizations (endings `-tion`,
  `-ment`, `-sion`, `-ance`, `-ence`), with a deny-list of
  high-frequency false positives (`function`, `evidence`,
  `experience`, `reference`, `sequence`, `instance`, `presence`,
  `absence`, `variance`, `distance`, …). Per the grounding note,
  nominalization density is one of the more reliable correlates
  of unclear scientific prose.

Each flag is **"worth re-reading because X"** — never "this
sentence is bad" or "rewrite to Y." The author decides.

## What it does not do

- **Produce a quality score.** No grade, no rating, no pass/fail,
  no single number. This is the load-bearing refusal of the skill.
- **Optimise toward Flesch-Kincaid or SMOG.** These indices
  systematically mis-score scientific prose; the skill calibrates
  against the manuscript itself, not against a universal target.
- **Edit the manuscript.** The output is a markdown report.
- **Direct specific rewrites.** Each flag is descriptive; the
  author owns the decision.
- **Flag inflated lists.** If every sentence is an outlier, the
  report has failed at its job. Guidance-level caps prevent this.
- **Run at `outline` phase.** Distributional statistics on stub
  prose are noise.
- **Check writing quality, readability, content correctness, or
  argument strength.** These are out of any single metric's reach
  for scientific text. Argument strength is `argumentative-flow` /
  `reviewer-simulation` territory; citation alignment is
  `citation-audit`'s.

## How many flags to expect

Tunable via `meta.guidance_level` in `MANUSCRIPT_STATE.yaml`:

| Guidance level | Per-dimension cap | Typical 5000-word manuscript |
|---|---|---|
| `terse` | 3 | ~3–6 flags total |
| `standard` (default) | 7 | ~5–10 flags total |
| `full` | 15 | up to ~30 flags total |

The Summary names "surfaced of flagged" (e.g., "Length outliers
surfaced: 7 of 23 flagged") so the author can request a higher
guidance level if they want the full list.

## Inputs

- **Manuscript text** — file path(s) or pasted prose. For
  multi-file projects, every file declared under `sections` is read.
- **`MANUSCRIPT_STATE.yaml`** *(optional but recommended)* — the
  `meta.guidance_level`, `bibliography.paths`, and
  `document_phase.current` fields are read. The skill proceeds at
  `standard` density if the state file is missing, noting the
  un-grounded run.

## Using it

### Inside Claude Code

```text
/scriptorium:outlier-sentence-detector
```

Then point Claude at the manuscript file(s) and ensure
`MANUSCRIPT_STATE.yaml` is reachable from the project root.

### Outside Claude Code (Codex, Gemini, Hermes, ChatGPT, …)

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to run
`outlier-sentence-detector` on your manuscript.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/outlier-sentence-detector/prompt.md
```

## Output structure

```markdown
# Outlier sentence detector

## Summary
- Sentences analysed: N
- Median sentence length: N words
- Median complexity proxy: N
- Median nominalization density: 0.NN
- Guidance level applied: terse | standard | full
- Length outliers surfaced: N (of M flagged)
- Complexity outliers surfaced: N (of M flagged)
- Nominalization-density outliers surfaced: N (of M flagged)

## Length outliers
| Location | Sentence excerpt | Length (words) | Distance from median |

## Complexity outliers
| Location | Sentence excerpt | Proxy measure | Rationale |

## Nominalization-density outliers
| Location | Sentence excerpt | Density | Flagged nominalizations |

## What this skill did NOT check
```

## Why "calibrate against the manuscript itself"

A 50-word sentence is a long sentence in some manuscripts and
unremarkable in others. Importing a universal target — "sentences
should be ≤25 words" — would reproduce the failure mode the
grounding note identifies in Flesch-Kincaid and SMOG: confidently
applying a calibration from one genre (military training pamphlets,
public-health flyers) to another (research papers read by domain
experts). The Summary reports the manuscript's own median per
dimension so the author sees what "outlier" means *for this
document*.

## Why "descriptive, not directive"

The skill sits at the copyediting / line-editing boundary on the
Einsohn / Mossop / CSE editorial gradient (see
[`copyediting-vs-developmental`](../../knowledge/editing/copyediting-vs-developmental.md)).
Einsohn's repeated injunction is that the copyeditor *queries* the
author when something is unusual — they do not silently fix it. The
skill follows the same posture: it points at sentences worth
re-reading and surfaces the dimension along which they are
unusual; what to do about them belongs to the author.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`quantitative-quality-measures`](../../knowledge/scientific-writing/quantitative-quality-measures.md)
  — the load-bearing note. Its **Selective Yes** verdict is exactly
  the design space this skill occupies: no general-purpose quality
  scoring, narrow outlier flagging is defensible. The note's
  recommended implementation — distributions computed from the
  manuscript itself, length / nesting depth / complexity as
  dimensions — is what the operational protocol implements.
- [`copyediting-vs-developmental`](../../knowledge/editing/copyediting-vs-developmental.md)
  — situates the skill on the editorial gradient. Outlier flagging
  is a copyediting / line-editing diagnostic; the descriptive
  (not directive) posture comes from Einsohn's "copyeditors query,
  they do not silently fix" principle.
- [`guidance-level`](../../knowledge/conventions/guidance-level.md)
  — controls framing *and* the per-dimension flag cap. Both
  behaviours follow the convention's principle that the structured
  output shape is unchanged across levels.
- [`declared-work-scope`](../../knowledge/conventions/declared-work-scope.md)
  — the skill operates on declared prose. It refuses to run at
  `outline` phase and does not invent the sentences it flags.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Calibrate locally, not universally.** Universal-target
  readability indices systematically fail on scientific text; the
  manuscript's own distribution is the only defensible reference.
- **Absolute floors prevent short-document nonsense.** A 500-word
  abstract has too small a distribution for pure σ-thresholding.
  Floors at 35 words (length), 5 (complexity proxy), and 0.30
  (nominalization density) prevent false-flagging on tight prose.
- **Cap by guidance level.** A tractable handful of flags is more
  useful than a comprehensive list. If every sentence is flagged,
  the report has failed; the caps make the output a workable
  re-reading list.
- **Three dimensions, not thirty.** Per the grounding note, adding
  dimensions is a non-trivial design decision — most measures
  available (lexical diversity, type-token ratio, hedging density)
  are noise for any specific judgement. The three chosen are
  defensible and bounded.
- **No full grammar parser.** The complexity proxy is intentionally
  cheap: commas + subordinators + coordinated-conjunction stacks.
  This is enough to find outliers and reliable across English
  variants and source formats.

## See also

- [`terminology-normalization`](../terminology-normalization/README.md)
  — covers the *other* half of GitHub issue
  [#15](https://github.com/seandavi/scriptorium/issues/15) (the
  terminology-drift detection originally proposed there is
  subsumed by `terminology-normalization`'s broader drift +
  preferred-term enforcement).
- [`argumentative-flow`](../argumentative-flow/README.md) — for
  the developmental-editing layer above this skill's line-editing
  surface.
- [`compression`](../compression/README.md) — sister skill at the
  line-editing layer that *proposes* length reductions; this
  skill *flags* length outliers. Running them together: this skill
  surfaces candidate sentences; the author then decides whether to
  invoke `compression` on a section the flags clustered in.
- GitHub issue [#15](https://github.com/seandavi/scriptorium/issues/15)
  — the canonical tracking issue. The terminology-drift half is
  closed by `terminology-normalization`'s shipping; this skill
  closes the outlier-sentence half.
