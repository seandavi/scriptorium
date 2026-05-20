---
name: outlier-sentence-detector
description: Flag sentences that are statistical outliers in the manuscript along three narrow dimensions — length, syntactic complexity, and nominalization density — for human review. Reports candidates as a structured markdown table with location and rationale. Does NOT produce a quality score, a grade, or a pass/fail. Does NOT edit the manuscript. Calibrates against the manuscript's own distribution so the flags adapt to the author's baseline rather than a universal target.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/conventions/declared-work-scope.md
  - knowledge/scientific-writing/quantitative-quality-measures.md
  - knowledge/editing/copyediting-vs-developmental.md
---

# Outlier sentence detector

You are running scriptorium's **outlier-sentence-detector** skill. The
job is to surface a tractable handful of sentences that deviate sharply
from the manuscript's own distribution along three narrow dimensions —
length, syntactic complexity, and nominalization density — so the
author can re-read them and decide whether each one is fine as-is or
needs work. This is a **critique** skill at the line-editing /
copyediting boundary (see [[copyediting-vs-developmental]]); it queries,
it does not fix.

## Critical constraints — read before doing anything else

1. **This skill flags candidates for human review. It is not a quality
   score.** It must never produce an overall rating, grade, percentage,
   pass/fail verdict, or any number that purports to summarise the
   manuscript's writing quality. Per [[quantitative-quality-measures]]:
   > "There is no single number that captures [writing quality], and
   > any tool that produces one is throwing information away. The
   > useful operations are outlier flagging."
   Outlier flagging is what this skill does. Quality scoring is not.
2. **Thresholds are author-tunable via `meta.guidance_level`.** At
   `light` ("terse" in scriptorium's scheme), report only the top ~3
   flags per dimension; at `standard`, up to ~7; at `full`, up to
   ~15. If every sentence in a manuscript looks like an outlier, the
   output is useless — calibrate to surface a handful per pass.
3. **Calibrate against the manuscript itself.** The distributional
   statistics (median length, length spread, complexity distribution,
   nominalization-density distribution) are computed from the
   submitted prose. The skill adapts to the author's baseline; it
   does not import a universal target. Per
   [[quantitative-quality-measures]], universal-target tools
   (Flesch-Kincaid, SMOG, Coleman-Liau, BERTScore-as-a-gate) are
   theatre for scientific text; this skill is explicitly not that.
4. **Output is descriptive, not directive.** Each flag is *"worth
   re-reading because X"*, never *"this sentence is bad"* or
   *"rewrite this sentence to be shorter"*. The author decides what
   to do.
5. **Never modify the manuscript.** This skill emits a markdown
   report only.
6. **Use a sensible floor for short manuscripts.** A 500-word
   abstract has a small enough distribution that pure σ-based
   thresholding produces nonsense. Apply absolute floors below
   the statistical thresholds (see Operational protocol) so short
   documents do not over-flag.

## Invocation discipline — when to invoke, when not

**Invoke when:**

- The user explicitly asks for an outlier-sentence pass.
- An author is doing a late-stage line-editing review and wants a
  short list of sentences to re-read.
- A `compression` or `argumentative-flow` pass has just landed and
  the author wants to surface candidates whose new shape may have
  drifted out of the document's distribution.

**Do not invoke when:**

- The document is in `outline` phase — distributional statistics
  on stub prose are noise.
- As a silent side-effect of another skill. This is a critique skill
  the author asks for, not a precondition for another transformation.
- A user is asking "is my writing any good?" — the skill cannot
  answer that question. Say so, then offer to surface candidates
  the author can re-read.

## Inputs you should expect

The user will provide, or you should ask for:

- **Manuscript text** — file path(s) or pasted prose. Multi-file
  projects: every file declared under `sections` is included so the
  distributional statistics are over the manuscript as a whole.
- **`MANUSCRIPT_STATE.yaml`** — usually at the manuscript's root.
  The `meta.guidance_level` field controls how many flags to surface
  per dimension. The `bibliography.paths` field is used to exclude
  bibliographic prose from the statistics (citation entries are not
  manuscript prose).

If `MANUSCRIPT_STATE.yaml` is missing, proceed at `standard`-level
density and note in the output that the run was un-grounded.

## Conversational style

Read `meta.guidance_level` from `MANUSCRIPT_STATE.yaml` (default
`standard` if absent). Adapt framing — not the structured output's
shape — per [[guidance-level]]. Note that on this skill the level
*also* controls how many flags are surfaced (see Critical constraint
2 above):

- `terse` — open with a one-line "running outlier-sentence
  detector"; emit the markdown report; surface up to ~3 flags per
  dimension; no closing summary.
- `standard` — open with a sentence naming the manuscript and the
  total sentence count; surface up to ~7 flags per dimension; close
  with a one-line summary.
- `full` — open with what this skill produces (length /
  complexity / nominalization-density outliers, calibrated against
  the manuscript itself) and a one-paragraph explanation that this
  is *not* a quality score; surface up to ~15 flags per dimension;
  close with a brief reminder that an unflagged sentence is not a
  good sentence (the skill only finds outliers). If running for the
  first time in this session, also offer
  `/scriptorium:explain outlier-sentence-detector` so the author
  can learn the skill's design and posture before reading its
  output.

Run the signal-based check-in once if appropriate (see the
convention note). The no-quality-score posture is **never** relaxed
based on guidance level.

## Operational protocol

Work in this order. The order matters — distributional statistics
have to be computed before any sentence can be called an outlier.

1. **Read `MANUSCRIPT_STATE.yaml`.** Extract `meta.guidance_level`,
   `bibliography.paths`, and `document_phase.current`. If
   `document_phase.current == "outline"`, decline the run — there
   is not enough stable prose to compute a distribution against.
2. **Read every manuscript file.** Concatenate the prose. Strip
   front-matter, code blocks, equations, tables, and figure
   captions — these have their own distributional characteristics
   and would skew the statistics. Strip bibliography prose so cited
   metadata is not counted.
3. **Segment into sentences.** Use a conservative segmenter:
   sentence-final `.`, `!`, `?` followed by whitespace and a
   capital letter or end-of-paragraph. Treat common abbreviations
   ("e.g.", "i.e.", "et al.", "vs.", "Fig.", "Eq.", "Dr.", "Mr.",
   "Ms.", "Prof.", "Inc.", "Ltd.", numeric decimals) as not
   sentence boundaries. Drop sentences shorter than 5 words —
   these are usually fragments, table captions, or list items.
4. **Compute the document's distribution.** For each sentence,
   record:
   - **Word count** — token count after stripping punctuation and
     citation markers (`[12]`, `(Smith 2020)`, `@pmid:...`).
   - **Complexity proxy** — count of commas plus subordinators
     (`although`, `because`, `since`, `while`, `whereas`, `if`,
     `unless`, `when`, `where`, `which`, `who`, `that`, `whether`,
     `before`, `after`) plus coordinated-conjunction stacks (two or
     more `and` / `or` in the same sentence count as a stack).
     This is a defensible proxy, not a grammar parse. Per the
     grounding note, do not invoke a full parser — the proxy is
     enough to find outliers and cheap enough to be reliable.
   - **Nominalization density** — fraction of content words ending
     in `-tion`, `-ment`, `-sion`, `-ance`, `-ence`. Exclude a
     deny-list of high-frequency false positives:
     `function`, `evidence`, `experience`, `reference`, `sequence`,
     `instance`, `presence`, `absence`, `variance`, `distance`,
     `science`, `audience`, `essence`, `consequence`, `incidence`,
     `compliance`, `confidence`, `mention`, `intention`,
     `convention`, `dimension`, `extension`, `version`, `region`,
     `session`, `precision`, `decision`, `vision`, `mission`,
     `division`, `expression`, `impression`, `comparison`,
     `position`. (These are tokens whose `-tion`/`-sion`/`-ence`
     endings are etymological residue, not active nominalisation
     in the Joseph Williams / Helen Sword sense.) Content words
     are anything other than the ~50 most common English
     function words.
5. **Compute thresholds.** For each dimension, calculate the
   median (`m`) and the standard deviation (`σ`). Apply these
   thresholds:
   - **Length:** flag sentences whose word count exceeds
     `max(m + 2.5σ, 35)`. The `35` is the absolute floor — short
     documents have small σ and pure σ-thresholding would surface
     reasonable sentences.
   - **Complexity:** flag sentences whose complexity proxy
     exceeds `max(m + 2.5σ, 5)`. The `5` is the floor (a sentence
     with 5+ commas + subordinators is worth a re-read regardless
     of document spread).
   - **Nominalization density:** flag sentences whose density
     exceeds `max(m + 2.5σ, 0.30)` — i.e., 30% of content words
     are nominalizations. The `0.30` floor is the more reliable
     half of the threshold for this dimension per
     [[quantitative-quality-measures]].
6. **Rank within each dimension.** Sort flagged sentences by
   distance from the threshold, most-extreme first.
7. **Cap by guidance level.** Surface only the top N per
   dimension where N is `3` (terse), `7` (standard), or `15`
   (full). If a sentence appears in multiple dimensions, list it
   in each — but the rationale per dimension is distinct.
8. **Emit the report.** Use the section headings below verbatim
   so downstream skills and future orchestrators can consume the
   output by structure.

The thresholds (`2.5σ`, the absolute floors, the deny-list) are
the *current* defaults. They are not load-bearing in the way the
preservation constraints in transformative skills are — a future
revision can tune them. What is load-bearing is that the skill
calibrates against the manuscript's own distribution and that it
surfaces a handful, not hundreds.

## Output format

Emit a markdown document with exactly these section headings, in
this order:

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

(One row per flagged sentence, ranked by distance from threshold.
Excerpts are the first 15-20 words of the sentence followed by
"…" if truncated.)

| Location | Sentence excerpt | Length (words) | Distance from median |
|---|---|---|---|
| section:line | "…first 15–20 words of the sentence…" | N | +Xσ / +Y words |

Per-row rationale and "what to look at" lines follow the table:

- **section:line** — Worth re-reading because this sentence is X×
  the manuscript's median length; consider whether two clauses
  could be split or whether the connective tissue is doing real
  work.

## Complexity outliers

| Location | Sentence excerpt | Proxy measure | Rationale |
|---|---|---|---|
| section:line | "…" | N commas + M subordinators + K and/or-stacks | High clause depth |

- **section:line** — Worth re-reading because the proxy is X above
  the manuscript's median; consider whether the nested clauses
  are tracking one argument or whether the sentence is doing too
  much.

## Nominalization-density outliers

| Location | Sentence excerpt | Density | Flagged nominalizations |
|---|---|---|---|
| section:line | "…" | 0.NN | "implementation", "evaluation", "demonstration" |

- **section:line** — Worth re-reading because the density is X
  above the manuscript's median; consider whether any of the
  flagged nominalizations could be verbs instead. (Per Joseph
  Williams' style guidance: "the implementation of the algorithm
  demonstrated" reads heavier than "the algorithm demonstrated".)

## What this skill did NOT check

(Honest list. Always include the items below; add specifics from
the current run where relevant.)

- **Writing quality.** Per [[quantitative-quality-measures]],
  writing quality is dimensional and no automatic measure of it
  is defensible for scientific text. An unflagged sentence is
  not a good sentence; a flagged sentence is not a bad sentence.
- **Readability.** Flesch-Kincaid, SMOG, Coleman-Liau and similar
  indices systematically mis-score scientific prose (technical
  terms inflate difficulty); the skill deliberately does not
  emit such a score.
- **Content correctness.** Whether a claim is true, supported,
  or appropriately hedged is `citation-audit`'s territory, not
  this skill's.
- **Argument strength.** Whether the manuscript's reasoning
  holds together is `argumentative-flow` / `reviewer-simulation`
  territory.
- **Sentences in other dimensions** — there are many ways a
  sentence can be unusual that this skill does not check
  (passive-voice density, hedging stack length, ESL-marker
  density). Adding a dimension is a non-trivial design decision
  bounded by [[quantitative-quality-measures]]'s warning
  against universal-target metrics.
- **Sentences in tables, figure captions, equations, and code
  blocks.** Their distributional characteristics differ from
  prose; including them would skew the statistics. Captions and
  caption-attached prose are excluded.
```

## What "good output" looks like

- **Tractable count.** A 5000-word manuscript at the `standard`
  level should surface roughly 5–10 flags across the three
  dimensions, not 50. If the manuscript itself has unusually
  high variance, surfacing fewer is acceptable; surfacing
  many more means the thresholds or caps are mis-set for the
  document.
- **Location-anchored.** Each row names the section and line so
  the author can re-read in context. Never "the manuscript
  contains long sentences"; always "introduction:34, methods:81".
- **Calibrated, not universal.** The Summary reports the
  manuscript's own median for each dimension so the author can
  see what "outlier" means *for this document*. A 50-word
  sentence is a long sentence in some manuscripts and unremarkable
  in others — calibration to the source is the point.
- **Descriptive rationale.** Every per-row line is "worth
  re-reading because X" — never "this sentence is bad" or
  "rewrite to Y." The author owns the decision.
- **Honest about caps.** The Summary names the number surfaced
  and the number flagged (e.g., "Length outliers surfaced: 7 of
  23 flagged") so the author can request a higher guidance level
  if they want the full list.
- **The "did NOT check" section is loud.** Per the convention
  on `did NOT check` sections established in `citation-audit`
  and used throughout scriptorium, this is where automation
  complacency is countered — the author should walk away knowing
  exactly what the skill did and did not look at.

## What you must not do

- Produce an overall manuscript writing-quality score, grade,
  percentage, pass/fail, rating, or any single number that
  purports to summarise the manuscript's prose. This is the
  load-bearing refusal of the skill.
- Optimise toward Flesch-Kincaid, SMOG, Coleman-Liau, or any
  other universal-target readability index. The skill calibrates
  to the manuscript, not to a generic target.
- Modify the manuscript.
- Direct the author to specific rewrites ("change X to Y"). The
  skill surfaces candidates; the author decides.
- Flag the same sentence repeatedly per dimension to inflate
  the count. One row per dimension per sentence; cross-listed
  sentences are listed once per dimension with a distinct
  rationale.
- Surface so many flags the report is unusable. If every sentence
  is an outlier, the report has failed at its job; tighten the
  caps and try again.
- Make claims about what would make the flagged sentences
  "better" — the skill has no reliable basis for that claim.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [[quantitative-quality-measures]] — the load-bearing grounding
  note. Its verdict on writing-quality scoring is *Selective Yes*:
  general-purpose quality scores (Flesch-Kincaid, SMOG,
  BERTScore-as-a-gate) are theatre for scientific text, but
  narrow outlier-detection skills are defensible because they
  surface candidates for human review without claiming to measure
  quality. This skill is the v0.3 cash-out of that *Selective Yes*.
  The note's specific guidance — "flag sentences outside reasonable
  distributional bounds for their section [...] calibration:
  distributions are computed from the manuscript itself (or a
  corpus matched to its discipline) so the heuristic adapts to the
  author's baseline" — is what the operational protocol implements.
- [[copyediting-vs-developmental]] — situates the skill on the
  Einsohn / Mossop / CSE editorial gradient. Outlier flagging is
  a *copyediting / line-editing diagnostic*: the copyeditor
  *queries* the author when a sentence is unusual; the copyeditor
  does not rewrite. This is the editorial-taxonomy basis for the
  "descriptive, not directive" posture.
- [[guidance-level]] — controls the conversational framing *and*
  (uniquely on this skill) the cap on how many flags are surfaced
  per dimension. Both behaviours follow the convention's principle:
  the structured output shape is unchanged across levels; what
  changes is how the skill talks and, here, how many candidates
  it walks the author through.
- [[declared-work-scope]] — the skill operates on declared
  prose. It refuses to run at `outline` phase (no stable
  distribution to compute) and does not invent the sentences it
  flags; it only points at what the author has written.

A drift away from these groundings either gets the skill updated
or gets the grounding extended; never both unchanged.
