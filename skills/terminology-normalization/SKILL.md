---
name: terminology-normalization
description: Detect terminology drift across a manuscript and enforce the preferred / forbidden / synonyms lists declared in MANUSCRIPT_STATE.yaml. Reports inconsistencies with exact occurrence locations and suggests normalizations. Does NOT modify the manuscript without explicit author consent.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/conventions/declared-work-scope.md
  - knowledge/critique-techniques/internal-consistency.md
  - knowledge/scientific-writing/style-guides.md
---

# Terminology normalization

You are running scriptorium's **terminology-normalization** skill. Your
job is to detect terminology drift in a manuscript and enforce the
`terminology.preferred` / `terminology.forbidden` / `terminology.synonyms`
lists declared in `MANUSCRIPT_STATE.yaml`. This is a **normalization**
skill: you may *suggest* concrete one-pass edits, but you must **not**
apply them without the author's explicit consent.

## Critical constraints — read before doing anything else

1. **Never modify the manuscript without explicit author consent.** The
   default output is a markdown report that surfaces drift, names the
   suggested normalization, and lets the author apply it (or invoke a
   follow-up edit pass). Auto-applying terminology rewrites is the
   exact failure mode this skill exists to avoid — see DESIGN.md's
   conservative-edit posture.
2. **Read the bibliography first.** Author names, paper titles, and
   other bibliographic metadata frequently contain tokens that look
   like forbidden terms or like variants of preferred terms but are
   *not* manuscript prose. Read every file in
   `MANUSCRIPT_STATE.yaml#bibliography.paths` before scanning the
   manuscript so tokens appearing in author / title / journal /
   container metadata are excluded from flagging. This is a
   load-bearing failure mode in the issue spec: missing this step
   produces false positives that erode trust in the entire skill.
3. **Ignore inflection by default.** "cell" vs. "cells", "gene" vs.
   "genes", "method" vs. "methods" — these are not drift; they are
   English morphology. Flag stem-level variation only (e.g.
   "cohort" vs. "cohorts" is *not* drift; "cohort" vs. "subjects"
   *is*, given preferred terms are declared).
4. **Respect quoted contexts and term-as-subject contexts.** A
   forbidden term inside `"quotes"` or in a passage critiquing or
   defining the term itself is not an enforcement target. A sentence
   like *we deliberately avoid the term "subjects"* is the author
   doing exactly what the skill would want; do not flag it as a
   violation.
5. **Surface, don't decide.** Undeclared near-variants — clusters of
   tokens the author has not yet expressed a preference about —
   are surfaced as a question: *should one of these be promoted to
   `terminology.preferred`, or are they intentionally distinct?* The
   skill does not pick a winner.

## Invocation discipline — when to invoke, when not

**Invoke when:**

- `MANUSCRIPT_STATE.yaml#terminology` declares preferences AND the
  document is in `draft`, `revision`, or `submission` phase.
- The user explicitly asks for a terminology check.
- `argumentative-flow` has just run and the author wants to confirm
  that the transformation preserved declared terms.

**Do not invoke when:**

- `terminology.preferred`, `terminology.forbidden`, and
  `terminology.synonyms` are all empty — there is nothing to enforce.
- The document is in `outline` phase — terminology is not yet stable;
  flagging drift here is noise.
- As a silent side-effect of another skill. The output is a report
  for the author, not a precondition for another transformation.

## Inputs you should expect

- **Manuscript text** — file path(s) or pasted prose. Full prose,
  including sections. If the manuscript is multi-file (e.g. Quarto
  includes declared under `sections`), read each file.
- **`MANUSCRIPT_STATE.yaml`** — usually at the manuscript's root. The
  `terminology.preferred`, `terminology.forbidden`,
  `terminology.synonyms`, and `bibliography.paths` fields are
  load-bearing.
- **Bibliography file(s)** — referenced by
  `MANUSCRIPT_STATE.yaml#bibliography.paths`. Read these *before*
  flagging any token in the manuscript (see constraint 2 above).

If `MANUSCRIPT_STATE.yaml` is missing or its terminology lists are
empty, stop. Tell the author the skill has nothing to enforce against
and suggest they declare terminology preferences first (e.g. via
`scriptorium:init`).

## Conversational style

Read `meta.guidance_level` from `MANUSCRIPT_STATE.yaml` (default
`standard` if absent). Adapt framing — not the structured output —
per [[guidance-level]]:

- `terse` — open with a one-line "running terminology normalization";
  emit the markdown report; no closing summary.
- `standard` — open with a sentence naming the manuscript and the
  declared terminology counts (e.g. "5 preferred terms, 3 forbidden,
  2 synonym mappings"); close with a one-line summary of the
  findings.
- `full` — open with what this skill produces (preferred-term drift,
  forbidden-term occurrences, undeclared variants, suggested
  normalizations) and how to read it (which sections are
  enforcement, which are questions for the author); close with
  which findings to act on first and which are informational. If
  running for the first time in this session, also offer
  `/scriptorium:explain terminology-normalization` so the author
  can learn the skill's design before reading its output.

Run the signal-based check-in once if appropriate (see the
convention note). The structured output itself is unchanged across
levels — what changes is only the framing around it. The
no-auto-apply posture is **never** relaxed based on guidance level.

## Operational protocol

Work in this order. The order matters — step 1 before step 3 is the
guard against the false-positives-on-cited-names failure mode.

1. **Read `MANUSCRIPT_STATE.yaml`.** Extract:
   - `terminology.preferred` — terms the manuscript should use.
   - `terminology.forbidden` — terms the manuscript should not use.
   - `terminology.synonyms` — map of variant → preferred term.
   - `bibliography.paths` — files to load before flagging.
   - `meta.guidance_level` — framing only; see above.
   - `document_phase.current` — if `outline`, decline the run.
2. **Read the bibliography file(s).** Build a set of tokens that
   appear in author names, titles, journal names, and other
   bibliographic metadata. Tokens in this set are excluded from
   flagging, even if they match a forbidden term or a non-preferred
   variant. Note in the output how many bibliographic tokens were
   excluded — the count is part of the audit trail.
3. **Read the manuscript prose.** Tokenize at the stem level
   (ignore inflection differences) and identify quoted regions and
   term-as-subject passages so they can be excluded.
4. **Detect preferred-term drift.** For each preferred term, search
   for declared synonyms (per `terminology.synonyms`) and any
   undeclared near-variants. Report each variant's location and
   count.
5. **Detect forbidden-term occurrences.** For each forbidden term,
   list each occurrence with the surrounding sentence. Exclude
   bibliographic tokens, quoted contexts, and term-as-subject
   passages.
6. **Detect undeclared variants.** Cluster repeated near-variants
   the author has not declared a preference for. Surface each
   cluster as a question — *promote one to preferred, add a synonym
   mapping, or leave as-is?*
7. **Propose normalizations.** For each preferred-term drift and
   each forbidden-term occurrence, write a concrete one-pass edit
   the author can apply (e.g. "Replace `subjects` with `participants`
   in 4 locations: introduction L12, methods L34, results L56,
   discussion L78"). Do not apply any edit.
8. **Emit the report.** Use the section headings below verbatim so
   downstream skills and future orchestrators can consume the
   output by structure.

## Output format

Emit a markdown document with exactly these section headings, in this
order:

```markdown
# Terminology normalization

## Summary

- Preferred terms declared: N
- Forbidden terms declared: N
- Synonym mappings declared: N
- Bibliographic tokens excluded from flagging: N
- Preferred-term drift: N variants found across M locations
- Forbidden-term occurrences: N
- Undeclared variants surfaced for author decision: N

## Preferred-term drift

(One subsection per preferred term that has detected drift. Omit
preferred terms with zero drift. For each: the preferred term, the
undeclared variant(s) found, occurrence count, and the locations.)

### `<preferred-term>`

| Variant found | Count | Locations |
|---|---|---|
| `<variant>` | N | section:line, section:line, … |

## Forbidden-term occurrences

(One row per occurrence. Quoted contexts and term-as-subject
passages are excluded — note the exclusion count separately.)

| Forbidden term | Location | Surrounding sentence |
|---|---|---|
| `<term>` | section:line | "…sentence containing the term…" |

(If any occurrences were excluded due to quoted context or
term-as-subject framing, note the count and the rationale below the
table.)

## Undeclared variants

(Clusters of repeated near-variants the author has not declared a
preference for. Each cluster is a question for the author, not an
enforcement finding.)

### Cluster <N>: <variant-a> / <variant-b> / …

- Occurrences: <variant-a> (N), <variant-b> (N), …
- Locations: …
- Question: promote one to `terminology.preferred`, add a synonym
  mapping in `terminology.synonyms`, or leave as deliberate
  variation?

## Suggested normalization

(Concrete one-pass edits the author can apply. Grouped by preferred
term and forbidden term. Each edit is "find / replace" with line
references. The skill does not apply these — the author does, or
invokes a follow-up edit pass.)

### Preferred-term drift fixes

- Replace `<variant>` with `<preferred>` in N locations:
  section:line, section:line, …

### Forbidden-term removals

- Remove or rephrase `<forbidden>` in N locations: section:line, …
  (Suggested replacement, if a `synonyms` mapping covers it:
  `<preferred>`.)

## What this skill did NOT check

(Honest list. Always include the items below; add specifics from
the current run where relevant.)

- Whether a flagged variant is in fact a different concept (e.g.
  "cell" and "cell-line" are distinct; the skill flags candidate
  drift but the author confirms).
- US/UK English spelling variation, unless explicitly declared as
  preferred / forbidden in the state file. Variety is a venue
  decision, not a drift question.
- Acronym expansion and first-use enforcement — out of scope for
  v0.3; covered separately when that utility lands.
- Bibliography normalization (author-name format, journal
  abbreviations, etc.) — separate utility. This skill only reads
  the bibliography to *exclude* its tokens from flagging.
- Stylistic-tone change. Deliberate prose variation (e.g. "stark
  contrast" used for emphasis) is preserved; this skill does not
  propose stylistic rewrites.
- Quoted passages and passages where a term is the subject of
  discussion. These are excluded from forbidden-term enforcement.
```

## What "good output" looks like

- **Bibliography-aware.** The Summary names the count of
  bibliographic tokens excluded. An audit that flags "Smith" because
  Smith is a cited author has failed at step 2.
- **Inflection-blind.** "cells" and "cell" do not appear in the
  drift table. Stem-level variants only.
- **Specific, location-anchored.** Never "the manuscript uses
  multiple variants." Always "introduction L12, L18; methods L34."
- **Surfaces undeclared variants as questions.** The author owns
  the terminology; the skill does not invent preferences.
- **Suggests, does not apply.** Every proposed edit is presented as
  text the author can paste into an edit pass; the manuscript is
  unchanged on disk.
- **Honest about exclusions.** Quoted contexts and term-as-subject
  passages are listed by count so the author can verify the
  exclusion was correct.

## What you must not do

- Modify the manuscript or the bibliography.
- Promote an undeclared variant to preferred without author
  consent — even a "you probably want X" recommendation that
  silently presupposes the answer.
- Flag tokens that appear only in bibliographic metadata.
- Flag inflection differences (cell/cells, gene/genes,
  method/methods) as drift.
- Flag forbidden terms inside quoted passages or in passages where
  the term is the subject of discussion.
- Propose stylistic rewrites beyond what the declared terminology
  lists license.
- Auto-apply suggested normalizations as a follow-up step.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [[internal-consistency]] — terminology drift is a class of
  internal-consistency failure. The note frames detection
  methodology: identify candidate synonym clusters, ask the author
  to choose, replace. The MANUSCRIPT_STATE terminology block is
  named there as the design pattern this skill consumes. The
  surfaces-as-questions-not-decisions posture for undeclared
  variants comes directly from that note's recommendation that the
  consistency check "flag candidate-synonym clusters for the author
  to resolve."
- [[style-guides]] — preferred-term enforcement is a style-guide
  function. The note covers conventions across AMA (medicine), CSE
  (general science), APA (psychology / social science), Chicago,
  ACS, and IEEE, and is explicit that style is **venue-dependent,
  not correct/incorrect**. This grounds two design choices: (a) the
  preferred-terms list is project-specific and read from the state
  file rather than imposed by the skill, and (b) US/UK English
  variation is out of scope by default — the venue, not the skill,
  decides.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.
