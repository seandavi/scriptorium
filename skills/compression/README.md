# compression

Propose page-limit-driven length reductions on a manuscript section
while preserving every citation, every declared statistic, every
declared core claim, and every declared terminology choice.

**Category:** transformation
**Modifies the manuscript?** No — the skill *suggests* edits. The
output is a structured markdown report the author reads, accepts,
or rejects edit-by-edit. The manuscript on disk is unchanged.
**Invocation:** explicit. Never proactive, never as a follow-up to
another skill without the user re-asking. Refuses to run without a
declared or supplied length target.

## Why "transformation" that suggests but does not apply

`compression` is a sibling to `argumentative-flow`. Both are
transformation skills; both inherit the same preservation contract
(citations, statistics, terminology, voice, claim set, hedging);
both ship per-edit output the author can audit. They differ on two
axes:

- **Editorial level.** Per [`copyediting-vs-developmental`](../../knowledge/editing/copyediting-vs-developmental.md),
  compression sits at *line editing* (sentence-level tightening,
  paragraph merges). `argumentative-flow` sits at *developmental
  editing* (structural reorganization, claims hierarchy). Different
  level, same posture.
- **Apply vs. suggest.** `argumentative-flow` produces a revised
  section the author can accept or reject as a block.
  `compression` produces a list of independent per-edit suggestions,
  each one reviewable on its own. This is the
  `terminology-normalization` posture — suggest, don't apply — at a
  different surface.

The combination matters: the author can run `compression`, accept
half the proposed edits, then run `argumentative-flow` on the
result to check that the cuts did not damage flow.

## What it does

- **Measures the gap.** Counts words, characters, and lines of the
  source section. Computes the gap to the declared length target.
- **Inventories preservation surfaces.** Cite keys, numbers,
  declared `core_claims` asserted in the section, declared
  preferred / forbidden terminology, hedging and stance markers.
- **Proposes edits in three categories.** Cheap (filler, redundant
  phrasing, hedging stacks, discourse-marker boilerplate),
  structural (paragraph merges, parenthetical moves,
  subordinate-clause tightening), and boundary (looks like
  compression but approaches germane-load — surfaced in "Edits NOT
  proposed" with the reason).
- **Verifies preservation per edit.** Each proposed edit lists the
  citations, numbers, claims, terms, and hedges that survive. The
  preservation report aggregates the per-edit checks.
- **Names what it did not do.** Compressions that risked losing a
  load-bearing nuance are surfaced in "Edits NOT proposed" so the
  author sees the considered-but-rejected set.

## What it does not do

- **Apply any edit.** Proposed edits are text the author copies into
  the manuscript (or rejects). The skill writes nothing to the
  manuscript on disk.
- **Remove or rename citations.** Even when the sentence carrying a
  citation is cut, the citation must re-attach to the surviving
  sentence with the same claim, or the cut is not proposed.
- **Round, re-express, or substitute numbers.** A compression that
  swaps "53%" for "majority" is a semantic edit, not a length edit.
- **Re-scope or weaken declared `core_claims`.** Read
  `MANUSCRIPT_STATE.yaml#core_claims`; preserve every one.
- **Merge distinct claims into one.** Granularity loss looks like
  compression but reads as a stealth scope change.
- **Introduce AI-writing tells.** Em-dash overuse, rule-of-three
  ("clear, concise, and compelling"), inflated symbolism ("plays a
  key role in"), elevated synonyms ("utilise" for "use"). The
  compressed text should read more like the source author, not less.
- **Smooth out hedging.** Hedging *stacks* ("may potentially
  possibly") are the legitimate target — reduce to a single hedge.
  Removing the hedge entirely is forbidden.
- **Restructure the section.** Paragraph reordering, claims
  hierarchy changes, narrative-framework shifts — these are
  `argumentative-flow`'s territory.
- **Compress the whole manuscript at once.** Single-section scope is
  what makes the per-edit diff reviewable.
- **Run without a length target.** Target-less compression is an
  opinion about the author's prose, not a service.

## Hard preservation constraints

| Constraint | What it means |
|---|---|
| Cite keys | Every cite key in source appears in output, unchanged |
| Numbers | Every quantitative statement preserved verbatim |
| Core claims | Every declared `core_claim` preserved |
| Claim granularity | Distinct claims may not be merged |
| Terminology | `MANUSCRIPT_STATE.yaml#terminology` honored |
| Voice | Active / passive as source has it |
| Tone | `style.tone` targets respected |
| Hedging | Stance markers preserved; only hedging stacks reducible |

If preservation conflicts with a proposed length reduction,
**preservation wins**. The conflict goes into "Edits NOT proposed"
rather than violating silently.

The BERTScore antonymy problem
([`semantic-preservation`](../../knowledge/editing/semantic-preservation.md))
means embedding similarity is **not** a safe automated guard against
meaning flips. The skill reads each proposed edit against the source
for semantic preservation; it does not delegate that check to a
similarity metric.

## Inputs

- **Section text** — a single named section (introduction, abstract,
  results, discussion, methods, or a named subsection).
- **`MANUSCRIPT_STATE.yaml`** — declares `core_claims`, `terminology`,
  `style.voice`, `style.tone`, and `constraints.max_word_count`.
- **Bibliography entries** — for cite keys in the section, so the
  pass can verify each is preserved across proposed edits.
- **Length target** — read from
  `MANUSCRIPT_STATE.yaml#constraints.max_word_count` by default;
  the user may supply a different target at invocation. The skill
  refuses to run without a target.

## Output structure

```markdown
# Compression

## Summary
| Measure | Source | Target | Proposed-after |

## Proposed edits
### Edit <N> — <one-line label>
- Source / Proposed / Words saved / Rationale / Preservation check

## Preservation report
| Item | Source count | Proposed-output count | Status |
### Hedging stacks reduced vs. hedges retained vs. hedges dropped

## Edits NOT proposed
### <one-line label> (lines L–L)
- Why it looked like a candidate / Why no edit was proposed

## What this skill did NOT check
```

## Why "suggest, don't apply"

Compression is one step closer to copyediting than
`argumentative-flow` is, but the conservative-edit posture is the
same. Einsohn's *Copyeditor's Handbook*
([`copyediting-vs-developmental`](../../knowledge/editing/copyediting-vs-developmental.md))
is explicit: copyeditors do not have license to rewrite a text line
by line. Scriptorium's restraint is the editorial profession's
restraint, ported into agent design — surface the suggested edit,
let the author apply it.

The per-edit format also makes the suggest-don't-apply posture
*useful*. An author who runs compression on a 5,000-word discussion
that needs to fit 4,500 can accept the cheap reductions wholesale,
review the structural ones, and skip the boundary cases. A
block-format revised section forces the author into accept-all or
reject-all; a per-edit list lets them mix.

## Why a length target is required

Compression without a target is an opinion about the author's prose:
"this could be tighter." That opinion may even be correct, but it's
not what `compression` is for. The skill's value is enforcing a
declared external constraint — a journal's word limit, a grant's
page limit, an abstract's character limit — and proposing the
edits that close the gap. Target-less compression invites the
skill into stylistic-rewrite territory, which is the failure mode
the preservation contract exists to prevent.

The `MANUSCRIPT_STATE.yaml#constraints.max_word_count` field is the
declared target; the user may supply a stricter target at
invocation. If neither is set, the skill asks before doing anything.

## Using it

### Inside Claude Code

```text
/scriptorium:compression
```

Then point Claude at the section file and ensure
`MANUSCRIPT_STATE.yaml` is reachable from the project root with
`constraints.max_word_count` declared (or supply a target at
invocation).

### Outside Claude Code

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to run
`compression` on a specific section against a specific target.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/compression/prompt.md
```

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`narrative-frameworks`](../../knowledge/scientific-writing/narrative-frameworks.md)
  — Schimel's OCAR/LDR; the section-level framing for which
  paragraphs carry the resolution vs. which carry scaffolding the
  author may want to compress.
- [`semantic-preservation`](../../knowledge/editing/semantic-preservation.md)
  — Nida's formal-equivalence framing; BERTScore antonymy problem.
  Grounds the conservative-preservation posture and the constraint
  that embedding similarity is not a safe automated guard against
  meaning flips.
- [`copyediting-vs-developmental`](../../knowledge/editing/copyediting-vs-developmental.md)
  — Mossop's twelve revision parameters and the editing-level
  gradient. Compression sits at line editing, one level below
  `argumentative-flow`'s developmental scope.
- [`revision-research`](../../knowledge/editing/revision-research.md)
  — Sommers 1980. Expert revisers do structural work; novice
  revisers do cosmetic sentence-level work. Every proposed
  compression edit must net-reduce length and have a documented
  reason.
- [`reader-expectation-approach`](../../knowledge/scientific-writing/reader-expectation-approach.md)
  — Gopen & Swan's topic/stress position and subject-verb proximity.
  A 30-word subject phrase is often compressible *and* more readable
  when tightened.
- [`hayes-flower-writing-model`](../../knowledge/scientific-writing/hayes-flower-writing-model.md)
  — Sweller's extraneous-vs-germane load distinction. Compression
  is justified when it removes extraneous load; not when it removes
  germane scaffolding the reader needs.
- [`esl-writers-swales-hyland`](../../knowledge/scientific-writing/esl-writers-swales-hyland.md)
  — hedging and stance patterns vary legitimately across linguistic
  backgrounds. Compression must not "smooth out" deliberate hedging;
  only hedging *stacks* are legitimate targets.
- [`ai-writing-failure-modes`](../../knowledge/prior-art/ai-writing-failure-modes.md)
  — Kobak 2024 on the lexical fingerprint of LLM-edited prose. The
  forbidden-transforms list draws directly from the patterns this
  note documents.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Inventory before proposing edits.** The operational protocol's
  step 3 extracts cite keys, numbers, declared `core_claims`,
  declared terminology, and hedging markers *before* any edit is
  proposed. The preservation report at the end verifies against this
  inventory. The inventory exists so violations are caught
  mechanically rather than relying on the model's recall.
- **Per-edit format.** Each proposed edit is independent and
  reviewable on its own — author can accept, reject, or modify edit
  by edit. This is the `terminology-normalization` posture (suggest,
  don't apply) at a different surface.
- **"Edits NOT proposed" is non-empty for any real section.** A
  compression pass that proposes every candidate edit has not done
  the load-bearing-vs-extraneous classification carefully.
  Honest passes leave compression on the table the author may still
  want to make.
- **Target is required.** A target-less compression is an opinion
  about the author's prose; with a target, it's a service. The
  skill refuses to run without one.
- **Single-section scope.** Reviewable per-edit diffs require small
  surface area. A "compress the whole manuscript" mode is implicitly
  declined — splitting into per-section passes is the design.

## See also

- [`argumentative-flow`](../argumentative-flow/README.md) — the
  developmental-editing sibling. Both inherit the same preservation
  contract; `argumentative-flow` restructures, `compression` reduces.
  Pair them: compress first, then run `argumentative-flow` on the
  shorter section to check the cuts did not damage flow.
- [`terminology-normalization`](../terminology-normalization/README.md)
  — the normalization-category skill whose suggest-don't-apply
  posture `compression` shares.
- [`desk-rejection-risk`](../desk-rejection-risk/README.md) — the
  critique skill that flags word-limit violations as a desk-rejection
  trigger. Useful upstream of `compression` to confirm the target
  the author should be reducing toward.
