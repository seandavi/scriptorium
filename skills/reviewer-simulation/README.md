# reviewer-simulation

Author-side simulation of peer review across four attentional lenses.
Surfaces likely critiques, fatal concerns, enthusiasm drivers, and
concrete revision suggestions before the author submits.

**Category:** critique
**Modifies the manuscript?** No.
**Editorial-side use?** No — this is **author-side only**. See below.

## Author-side only — load-bearing policy note

Using this skill on a manuscript the user did *not* author —
specifically, using it as an aid in editorial review of someone
else's submission — violates current peer-review policy at ICMJE, NIH,
Elsevier, and Nature. The skill will refuse to run in that context.

The intended workflow is: the author runs the simulation on their own
draft to pressure-test it before submission, addresses critiques in
revision, and submits a stronger paper to actual reviewers.

## What it does

For each of four attentional lenses (methodological skeptic, domain
expert, translational/clinical, statistical), surfaces critiques
anchored to specific passages in the manuscript. The lenses are
*filters*, not personas — drawn from the empirical critique taxonomy
in [`common-critiques-taxonomy`](../../knowledge/peer-review/common-critiques-taxonomy.md).

Output sections:

- **Acceptance risk assessment** — qualitative, never numeric.
- **Likely major critiques** — 4–8 items across lenses, quality over count.
- **Likely minor critiques** — presentation, clarity, etc.
- **Potential fatal concerns** — sparing; may be empty.
- **Enthusiasm drivers** — what reviewers may genuinely like.
- **Suggested revisions** — concrete, scoped, one-pass-each.
- **Lenses applied** — what each lens surfaced.
- **Cross-checked against MANUSCRIPT_STATE** — acknowledged
  weaknesses are not re-raised as new critiques.
- **What this simulation did NOT do** — honest limits.

## What it does not do

- **Score the manuscript numerically.** Acceptance risk is
  qualitative. Numeric scores invite gaming and over-trust.
- **Replace real peer reviewers.** Liang 2024 (*NEJM AI*) benchmarked
  LLM-to-human reviewer comment overlap at ~30%. Useful pressure
  test, not a substitute.
- **Recompute statistics.** For arithmetic checks of reported
  numbers, use deterministic tools (Statcheck, GRIM); LLM arithmetic
  is unreliable.
- **Re-execute analyses or replicate findings.**
- **Fact-check cited literature** beyond what the manuscript provides.
- **Reproduce reviewer affect or "Reviewer 2 voice."** Critique
  content only.
- **Editorial-side review of submissions.**

## Inputs

- **Manuscript text** — file path or pasted prose.
- **`MANUSCRIPT_STATE.yaml`** — declares `core_claims`,
  `known_weaknesses`, and `target_venue` (which informs which lenses
  matter most for the destination).
- **Bibliography file(s)** — as listed in
  `MANUSCRIPT_STATE.yaml#bibliography.paths`.

## Why simulate at all

Real reviewers agree only modestly on manuscript merit. The largest
meta-analysis (Bornmann, Mutz & Daniel 2010, 48 studies, ~19,443
manuscripts) reports Cohen's κ ≈ 0.17. Implication: a simulation that
produces four convergent reviews is *less* faithful to the literature
than one that produces four divergent ones. Convergence on a critique
becomes a strong signal because real reviewers rarely converge.

The Liang 2024 *NEJM AI* benchmark — multi-thousand manuscript study
of GPT-4 reviewer comments — found 30.85% overlap with the comments
human reviewers actually wrote. The skill is calibrated to that
benchmark: aim for plausible, useful critiques the author would
benefit from addressing, not for impossible-to-meet accuracy.

## Using it

### Inside Claude Code

```text
/scriptorium:reviewer-simulation
```

Then point Claude at the manuscript file and ensure
`MANUSCRIPT_STATE.yaml` is reachable from the project root.

### Outside Claude Code

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to run
`reviewer-simulation` on your manuscript.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/reviewer-simulation/prompt.md
```

See [`examples/`](examples/) for a worked example.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [`reviewer-archetypes-evidence`](../../knowledge/peer-review/reviewer-archetypes-evidence.md)
  — Bornmann 2010 κ ≈ 0.17 inter-rater meta-analysis; justifies
  "diversity of attention" over consensus scoring; the "Reviewer 2"
  trope vs. the empirical record.
- [`common-critiques-taxonomy`](../../knowledge/peer-review/common-critiques-taxonomy.md)
  — Bordage 2001 top-10 reject reasons; the seven-family critique
  taxonomy mapped to the four lenses.
- [`ai-peer-review-research`](../../knowledge/peer-review/ai-peer-review-research.md)
  — Liang 2024 *NEJM AI* 30.85% human-AI comment overlap is the
  calibration benchmark.
- [`critique-quality-evidence`](../../knowledge/peer-review/critique-quality-evidence.md)
  — what makes a critique actually useful: passage-anchored
  evidence rather than generic statements.
- [`reporting-guidelines`](../../knowledge/scientific-writing/reporting-guidelines.md)
  — CONSORT / STROBE / PRISMA / ARRIVE / STARD / TRIPOD+AI as
  baselines a methodological lens consults.
- [`ai-writing-failure-modes`](../../knowledge/prior-art/ai-writing-failure-modes.md)
  — defines what this skill must NOT do (numeric scoring, citation
  hallucination, replacement of real review).

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Diversity over consensus.** The κ ≈ 0.17 finding is the reason
  for four lenses rather than one. Convergence on a critique across
  multiple lenses is treated as signal.
- **Concentrated negative comments matter more than raw count.**
  Bornmann, Weymuth & Daniel 2010 found that critique concentration
  in fatal categories (design, statistics, relevance) predicts
  downstream impact better than total comment count. The skill aims
  for 4–8 substantive critiques, not exhaustive enumeration.
- **Known weaknesses are first-class state.** Cross-checking against
  `MANUSCRIPT_STATE.yaml#known_weaknesses` prevents the noise of
  surfacing already-acknowledged limitations as fresh critiques.
- **Editorial policy is hard-coded into the prompt.** The skill
  refuses editorial-side use rather than relying on the operator's
  judgment.

## See also

- [`citation-audit`](../citation-audit/README.md) — the first v0.1
  critique skill; reviewer-simulation reads citation-audit-style
  output well as a companion input.
- GitHub issue [#6](https://github.com/seandavi/scriptorium/issues/6)
  — the canonical tracking issue.
