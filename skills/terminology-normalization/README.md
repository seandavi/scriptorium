# terminology-normalization

Detect terminology drift across a manuscript and enforce the
preferred / forbidden / synonyms lists declared in
`MANUSCRIPT_STATE.yaml`. Reports inconsistencies with exact
occurrence locations and suggests concrete normalizations.

**Category:** normalization
**Modifies the manuscript?** No, not without explicit author
consent. The skill emits a report with suggested edits; the
author applies them or invokes a follow-up edit pass.
**Invocation:** explicit. Safe to suggest when terminology
preferences are declared and the document is in
`draft` / `revision` / `submission` phase, or as a verification
pass after `argumentative-flow`.

## What it does

- **Preferred-term drift detection.** For each term declared in
  `terminology.preferred`, finds declared synonyms (from
  `terminology.synonyms`) and undeclared near-variants in the
  prose, reporting locations and counts.
- **Forbidden-term enforcement.** For each term in
  `terminology.forbidden`, lists each occurrence with the
  surrounding sentence. Quoted contexts and term-as-subject
  passages are excluded.
- **Undeclared-variant surfacing.** Clusters of repeated
  near-variants the author has not declared a preference for are
  surfaced as questions — promote one to preferred, add a synonym
  mapping, or leave as deliberate variation. The skill does not
  pick a winner.
- **Concrete normalization suggestions.** One-pass find/replace
  edits the author can apply. The skill does not apply them.

## What it does not do

- **Modify the manuscript.** No auto-applied edits. The author
  applies suggestions, or invokes a follow-up edit pass.
- **Flag bibliographic tokens.** Author names, paper titles,
  journals, and other bibliography metadata are read first and
  excluded from flagging.
- **Flag inflection differences.** "cell" / "cells", "gene" /
  "genes" are not drift. Stem-level variants only.
- **Flag quoted passages or term-as-subject passages.** A
  forbidden term inside `"quotes"` or in a sentence critiquing or
  defining the term is not a violation.
- **Enforce US/UK English variation** unless explicitly declared
  in the state file. Variety is a venue decision.
- **Expand acronyms or enforce first-use** — out of scope; a
  separate utility for v0.3+.
- **Normalize the bibliography itself** — separate utility. This
  skill reads the bibliography only to exclude its tokens from
  flagging.
- **Propose stylistic rewrites** beyond what the terminology
  lists license. Stylistic variation is preserved.

## Inputs

- **Manuscript text** — file path(s) or pasted prose. For
  multi-file projects, every file declared under `sections` is
  read.
- **`MANUSCRIPT_STATE.yaml`** — the
  `terminology.preferred / forbidden / synonyms` and
  `bibliography.paths` fields are load-bearing.
- **Bibliography file(s)** — as listed in
  `MANUSCRIPT_STATE.yaml#bibliography.paths`. Read **before**
  scanning the manuscript so cited author names and titles are
  never false-positively flagged.

## Using it

### Inside Claude Code

```text
/scriptorium:terminology-normalization
```

Then point Claude at the manuscript file(s) and ensure
`MANUSCRIPT_STATE.yaml` is reachable from the project root.

### Outside Claude Code (Codex, Gemini, Hermes, ChatGPT, …)

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to
run `terminology-normalization` on your manuscript.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/terminology-normalization/prompt.md
```

## Output structure

```markdown
# Terminology normalization

## Summary
- Preferred terms declared: N
- Forbidden terms declared: N
- Synonym mappings declared: N
- Bibliographic tokens excluded from flagging: N
- Preferred-term drift: N variants across M locations
- Forbidden-term occurrences: N
- Undeclared variants surfaced for author decision: N

## Preferred-term drift
### `<preferred-term>`
| Variant found | Count | Locations |

## Forbidden-term occurrences
| Forbidden term | Location | Surrounding sentence |

## Undeclared variants
### Cluster <N>: <variant-a> / <variant-b> / …

## Suggested normalization
### Preferred-term drift fixes
### Forbidden-term removals

## What this skill did NOT check
```

## Why "bibliography first"

The most credibility-eroding failure mode for a terminology check
is flagging a cited author's name as a forbidden term, or flagging
a word in a paper title as a non-preferred variant. The
operational protocol's step 2 — read every file in
`bibliography.paths` before tokenizing the manuscript — is the
guard. The Summary section names the count of bibliographic
tokens excluded so the audit trail is visible.

## Why "suggest, don't apply"

Normalization skills sit one step closer to transformation than
critique skills do. The conservative-edit posture in
[DESIGN.md](../../DESIGN.md) is explicit: transformative work
preserves declared terminology and minimises rewrite surface,
and even then transformation runs only on explicit invocation.
The same logic applies here — surfacing a suggested edit lets the
author decide; auto-applying does not. Authors who want the edit
pass invoke it explicitly.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`internal-consistency`](../../knowledge/critique-techniques/internal-consistency.md)
  — terminology drift is a class of internal-consistency failure.
  The note explicitly names the
  `MANUSCRIPT_STATE.yaml#terminology` block as the design pattern
  this skill consumes and recommends that consistency checks
  "flag candidate-synonym clusters for the author to resolve" —
  which is exactly what the **Undeclared variants** section does.
- [`style-guides`](../../knowledge/scientific-writing/style-guides.md)
  — preferred-term enforcement is a style-guide function. The
  note covers conventions across AMA, CSE, APA, Chicago, ACS, and
  IEEE, and is explicit that style is **venue-dependent**, not
  correct/incorrect. This grounds two design choices: (a) the
  preferred-terms list is project-specific and read from the
  state file rather than imposed by the skill, and (b) US/UK
  English variation is out of scope by default — the venue, not
  the skill, decides.

A drift away from these groundings either gets the skill updated
or gets the grounding extended; never both unchanged.

## Design notes

- **Bibliography-first read order.** The operational protocol's
  step 2 is non-negotiable. It exists because the false-positive
  failure mode — flagging cited author names as drift — is the
  one most likely to make an author dismiss the skill as broken.
- **Suggest, do not apply.** Normalization is a category that
  *may* propose concrete edits, but the act of applying them
  belongs to the author or to an explicit follow-up edit pass.
  This is the same posture `argumentative-flow` adopts at the
  paragraph level; here it applies at the token level.
- **Surface undeclared variants as questions.** The skill does
  not invent terminology preferences. Asking — rather than
  guessing — is what makes the output trustworthy.
- **Pairs with `argumentative-flow`.** Running
  `terminology-normalization` after `argumentative-flow` is the
  first check that the transformation skill did not drift
  terminology silently. This pairing is part of why this skill
  was prioritised for v0.3.

## See also

- [`citation-audit`](../citation-audit/README.md) — critique
  skill that audits in-text citation use; this skill audits
  in-text terminology use.
- [`argumentative-flow`](../argumentative-flow/README.md) — the
  transformation skill whose preservation contract includes
  honoring `MANUSCRIPT_STATE.yaml#terminology`; this skill is the
  natural verification pass after a flow run.
- GitHub issue [#74](https://github.com/seandavi/scriptorium/issues/74)
  — the canonical tracking issue.
