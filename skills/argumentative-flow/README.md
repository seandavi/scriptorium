# argumentative-flow

Improve a manuscript section's logical and argumentative coherence
while preserving every citation, statistic, and declared terminology
choice.

**Category:** transformation
**Modifies the manuscript?** Yes — this is the v0.1 transformative
skill. The other two v0.1 skills are critique-only.
**Invocation:** explicit-only. Never proactive, never as a follow-up
to another skill without the user re-asking.

## Why "transformation" is a load-bearing category

Critique skills are safe by construction — they describe; they do not
edit. Transformation skills are not. Every transformation skill needs:

- An **explicit invocation discipline** so the author's voice and
  argument structure are never rewritten without consent.
- **Hard preservation constraints** so the things that must not
  change (citations, numbers, terminology) cannot change.
- **Reviewable output** — a diff against the source, plus a
  preservation report — so the author can audit the change.

argumentative-flow sets that pattern for the project. Future
transformation skills (compression, redundancy-removal,
terminology-normalization) inherit it.

## What it does

- **Paragraph order** within the section.
- **Sentence order** within paragraphs (Gopen & Swan: topic position,
  stress position, old-info-then-new).
- **Transitions** — connective tissue between paragraphs.
- **Claims hierarchy** — paragraph-leading sentence should state the
  paragraph's claim.
- **Argument progression** — Toulmin: claim → data → warrant.

## What it does not do

- **Add or remove citations.** Citations are inviolate.
- **Change numbers, statistics, or quantitative statements.**
- **Substitute terminology** not licensed by `MANUSCRIPT_STATE.yaml`.
- **Embellish style.** No added metaphors, no added hedging beyond
  what's already present, no replacement of plain words with elevated
  synonyms.
- **Add or remove claims.** Reorder, re-emphasize, reframe — yes.
  Add or cut — no. If a claim genuinely should be cut, the pass
  recommends cutting it in the Remaining weaknesses section; the
  author decides.
- **Rewrite the methods section.** Different problem; different skill
  (not in v0.1).
- **Compress length.** Different skill (v0.2 candidate).
- **"Smooth out" ESL hedging or stance patterns** — they vary
  legitimately across linguistic backgrounds and are often
  deliberate.
- **Transform the whole manuscript at once.** Single-section scope is
  what makes the diff reviewable.

## Hard preservation constraints

| Constraint | What it means |
|---|---|
| Cite keys | Every cite key in the source appears in the output, unchanged |
| Numbers | Every quantitative statement preserved verbatim |
| Terminology | `MANUSCRIPT_STATE.yaml#terminology` honored (preferred / forbidden / synonyms) |
| Voice | Active or passive as the source has it |
| Tone | `style.tone` targets respected |
| Claim set | No added, removed, or weakened claims |

If preservation conflicts with a proposed improvement, **preservation
wins**. The pass surfaces the conflict in Remaining weaknesses rather
than silently violating.

The BERTScore antonymy problem ([`semantic-preservation`](../../knowledge/editing/semantic-preservation.md))
means embedding similarity is **not** a safe automated guard against
meaning flips. The skill reads the revised text against the source for
semantic preservation; it does not delegate that check to an
automated similarity metric.

## Inputs

- **Section text** — a single named section (introduction,
  discussion, methods, abstract, or a named subsection).
- **`MANUSCRIPT_STATE.yaml`** — declares `terminology`, `style.voice`,
  `style.tone`, and `constraints.preserve_*` flags.
- **Bibliography entries** — for cite keys appearing in the section,
  so the pass can verify each is preserved.

## Output structure

```markdown
# Argumentative-flow pass

## Section scope
## Structural diagnosis
## Logical gaps
## Proposed outline
## Revised text
## Diff against source
## Preservation report
| Item | Source count | Output count | Status |
## Remaining weaknesses
```

See [`examples/`](examples/) for a worked example.

## Why "smallest viable edits"

Sommers 1980 ([`revision-research`](../../knowledge/editing/revision-research.md))
documents an empirical contrast: novice revisers do cosmetic
sentence-level work, treating revision as polishing. Expert revisers
do structural work, treating revision as resolving the gap between
intention and execution. The skill aims for the expert pattern. A
revision that changes every sentence has likely overreached — small
changes serving structural goals are the target.

## Using it

### Inside Claude Code

```text
/scriptorium:argumentative-flow
```

Then point Claude at the section file (introduction, discussion,
etc.) and ensure `MANUSCRIPT_STATE.yaml` is reachable from the
project root.

### Outside Claude Code

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, ask it to run
`argumentative-flow` on a specific section.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/argumentative-flow/prompt.md
```

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`reader-expectation-approach`](../../knowledge/scientific-writing/reader-expectation-approach.md)
  — Gopen & Swan's topic and stress positions; old-info-then-new.
  Mechanism-level grounding for sentence- and paragraph-level work.
- [`narrative-frameworks`](../../knowledge/scientific-writing/narrative-frameworks.md)
  — Schimel's OCAR/LDR; Heard; Whitesides. Framework-level grounding
  for section-level structural work.
- [`argument-mapping`](../../knowledge/critique-techniques/argument-mapping.md)
  — Toulmin's claim / data / warrant. Used to diagnose logical gaps
  inside structural reorganization.
- [`semantic-preservation`](../../knowledge/editing/semantic-preservation.md)
  — Nida's formal/dynamic equivalence; BERTScore antonymy problem.
  Grounds the constraint that embedding similarity is not safe as
  the only preservation check.
- [`revision-research`](../../knowledge/editing/revision-research.md)
  — Sommers 1980. The empirical case for *small* changes serving
  *structural* goals.
- [`esl-writers-swales-hyland`](../../knowledge/scientific-writing/esl-writers-swales-hyland.md)
  — hedging and stance patterns vary legitimately. The skill must
  not "smooth out" deliberate ESL hedging.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Inventory before transforming.** The first operational step
  extracts the list of cite keys, the list of numbers, and the list
  of declared terminology terms. The preservation report at the end
  verifies against this inventory. The inventory exists so violations
  can be caught mechanically rather than relying on the model's
  recall of what was originally there.
- **Single-section scope.** Reviewable diffs require small surface
  area. A "transform the whole manuscript" mode is implicitly
  declined — splitting into per-section passes is the design.
- **Explicit-only invocation, hard-coded.** The description does not
  telegraph "automatically use this when…". The constraint lives in
  prompt text, manifest metadata, and README.
- **Recommend, do not cut.** Claims the pass thinks should be removed
  are surfaced as recommendations in Remaining weaknesses. The
  author makes the cut.

## See also

- [`citation-audit`](../citation-audit/README.md) — the v0.1 critique
  skill that flags citation problems argumentative-flow's preservation
  constraints exist to *not* introduce.
- [`reviewer-simulation`](../reviewer-simulation/README.md) — the v0.1
  critique skill that surfaces structural concerns; running it before
  an argumentative-flow pass helps identify which section most
  benefits from restructuring.
- GitHub issue [#7](https://github.com/seandavi/scriptorium/issues/7)
  — the canonical tracking issue.
