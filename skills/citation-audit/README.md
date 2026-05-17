# citation-audit

Audit a manuscript's existing citations for claim-support alignment,
primary-vs-review mismatch, causal overreach, and unsupported
assertions. Reports findings as structured markdown.

**Category:** critique
**Modifies the manuscript?** No.
**Adds citations?** No, ever. This is the skill's load-bearing constraint.

## What it does

For every in-text citation in a manuscript, citation-audit runs the
four-step journal-editorial protocol from [Greenberg
2009](https://doi.org/10.1136/bmj.b2680):

1. **Extract** the in-text claim the citation is attached to.
2. **Identify** the cited reference(s).
3. **Compare** the claim against what the cited reference supports.
4. **Classify** alignment as
   `supports / partially supports / does not support / cannot determine`.

Beyond per-citation alignment, it flags pattern-level smells:
unsupported assertions, causal overreach, primary-vs-review mismatch,
single-source load-bearing claims, and possible amplification or
invention (hedges lost between the primary source and the citing
sentence).

The output is a structured markdown report with consistent section
headings so future orchestrators (the v0.2 `manuscript-pipeline`
skill) can consume it.

## What it does not do

- **Add or suggest citations.** This is the LLM hallucination failure
  mode the skill exists in part to *not* introduce. If a claim has no
  citation, the audit flags it as unsupported; the author decides
  what to cite.
- **Modify the manuscript.** Audit is descriptive. Edits are the
  author's responsibility.
- **Verify full-text claim alignment** unless the cited papers' full
  texts are provided. With only bibliographic metadata, the audit
  says so explicitly.
- **Detect retractions** — that's a future v0.2 utility, not part of
  the v0.1 audit.
- **Score the manuscript.** Audit reports findings; it does not rank.

## Inputs

- **Manuscript text** — file path or pasted prose.
- **`MANUSCRIPT_STATE.yaml`** — usually at the manuscript root. The
  `core_claims`, `known_weaknesses`, and `bibliography.paths` fields
  are load-bearing.
- **Bibliography file(s)** — as listed in
  `MANUSCRIPT_STATE.yaml#bibliography.paths`.

Optionally:

- **Full text (or abstracts) of cited papers** — substantially
  improves the audit's confidence. Without them, the skill assesses
  from bibliographic metadata only.

## Using it

### Inside Claude Code

```text
/scriptorium:citation-audit
```

Then point Claude at the manuscript file (or paste a section) and
ensure `MANUSCRIPT_STATE.yaml` is reachable from the project root.

### Outside Claude Code (Codex, Gemini, Hermes, ChatGPT, …)

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to run
`citation-audit` on your manuscript.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/citation-audit/prompt.md
```

## Output structure

```markdown
# Citation audit

## Summary
- Claims examined: N
- Supports: A | Partially supports: B | Does not support: C |
  Cannot determine: D
- Unsupported assertions (no citation): E
- Patterns flagged: short list

## Per-claim assessment
| # | Claim (excerpt) | Cited refs | Alignment | Notes |

## Patterns
### Unsupported assertions
### Causal overreach
### Review-only support for mechanistic claims
### Single-source load-bearing claims
### Possible amplification / invention

## What this skill did NOT check
```

See [`examples/`](examples/) for a worked example showing each pattern.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`citation-claim-alignment`](../../knowledge/critique-techniques/citation-claim-alignment.md)
  — the operational four-step protocol; Greenberg 2009 BMJ distortion
  patterns; scite.ai's supporting / contrasting / mentioning
  classifier; manual journal-editorial protocols.
- [`citation-accuracy-evidence`](../../knowledge/citations/citation-accuracy-evidence.md)
  — error-prevalence baselines from de Lacey 1985 onward (~20% median
  quotation error rate across replications).
- [`citation-overreach-research`](../../knowledge/citations/citation-overreach-research.md)
  — Boutron 2010 JAMA on spin; the amplification and invention
  patterns that single-shot audit can detect.
- [`hallucination-in-llm-citations`](../../knowledge/citations/hallucination-in-llm-citations.md)
  — the failure mode this skill exists in part to *not* introduce.
  Documents why the hard constraint "never invent citations" is
  load-bearing rather than stylistic.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Gradient over binary.** The methodology this grounds in is
  explicitly gradient (scite's three-way classifier; the
  journal-editorial four-step). Forcing yes/no answers loses
  load-bearing nuance.
- **Patterns over enumeration.** If twelve review-only mechanistic
  citations appear, group as a pattern rather than twelve rows. The
  Summary section is what a busy author scans first.
- **Honest about what it cannot check.** The "What this skill did NOT
  check" section is required, not optional. LLMs cannot verify
  paywalled full-text content; the audit must say so.

## See also

- [`scriptorium validate`](../../docs/src/content/docs/reference/cli.md)
  — validate the `MANUSCRIPT_STATE.yaml` the audit reads.
- GitHub issue [#5](https://github.com/seandavi/scriptorium/issues/5)
  — the canonical tracking issue.
- GitHub issue [#19](https://github.com/seandavi/scriptorium/issues/19)
  — the v0.2+ direction where this skill picks up live PubMed /
  Crossref grounding for citation resolution.
