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
else's submission — would mean uploading a confidential manuscript
and handing the critique to an AI. Current reviewer policies rule
that out. NIH prohibits its reviewers from using generative AI to
analyse or formulate critiques. Elsevier (June 2026) and Springer
Nature (September 2026) allow limited, disclosed, supportive reviewer
use but forbid delegating the critique to AI. Elsevier bans uploading
a submitted manuscript into any AI tool; Springer Nature bans public
or unsecured tools. ICMJE requires reviewers to follow the journal's
AI policy or request the journal's permission. The skill will refuse
to run in that context. See
[`peer-review-platforms`](../../knowledge/prior-art/peer-review-platforms.md)
for sources.

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
- **Likely major critiques** — 4–8 items across lenses, quality over
  count. Hidden or instruction-like text aimed at AI reviewers, if
  found, is reported here as a `[Submission integrity]` item.
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
  trope vs. the empirical record; Kim et al. 2026 (preprint) on AI
  reviewers converging on each other.
- [`common-critiques-taxonomy`](../../knowledge/peer-review/common-critiques-taxonomy.md)
  — Bordage 2001 top-10 reject reasons; the seven-family critique
  taxonomy mapped to the four lenses; which families the evidence
  treats as fatal and which as fixable.
- [`ai-peer-review-research`](../../knowledge/peer-review/ai-peer-review-research.md)
  — Liang 2024 *NEJM AI* 30.85% human-AI comment overlap is the
  calibration benchmark; Ye et al. (preprint) on hidden-prompt
  manipulation and echoing of disclosed limitations; why the skill
  gives no scores or accept/reject recommendation.
- [`critique-quality-evidence`](../../knowledge/peer-review/critique-quality-evidence.md)
  — what makes a critique actually useful: passage-anchored
  evidence rather than generic statements; Cobo et al. 2007 on
  suggested checklists (no significant effect) vs. statistical
  reviewers (improved reporting).
- [`reporting-guidelines`](../../knowledge/scientific-writing/reporting-guidelines.md)
  — CONSORT 2025 / SPIRIT 2025 / STROBE / PRISMA / ARRIVE / STARD /
  TRIPOD+AI as baselines a methodological lens consults.
- [`ai-writing-failure-modes`](../../knowledge/prior-art/ai-writing-failure-modes.md)
  — hallucinated references, the failure mode this skill must not
  reproduce.
- [`peer-review-platforms`](../../knowledge/prior-art/peer-review-platforms.md)
  — the 2026 reviewer AI policies behind the author-side-only
  posture; hidden prompts in manuscripts; benchmark comparators.
- [`credit-taxonomy-authorship`](../../knowledge/peer-review/credit-taxonomy-authorship.md)
  — ICMJE Section V rules on reviewer AI use and confidentiality.

A drift away from these groundings either gets the skill updated or
gets the grounding extended; never both unchanged.

## Design notes

- **Diversity over consensus.** The κ ≈ 0.17 finding is the reason
  for four lenses rather than one. Convergence on a critique across
  multiple lenses is treated as signal.
- **Concentrated negative comments matter more than raw count.**
  Bornmann, Weymuth & Daniel 2010 found that many negative comments
  on relevance and on design/conception signalled that a rejected
  manuscript would not later appear in a high-impact journal, while
  comment counts on method/statistics, literature, writing, and
  discussion of results did not. The skill aims for 4–8 substantive
  critiques, not exhaustive enumeration.
- **Fatal vs. fixable follows the evidence.** Design is the only
  family both content analyses (Bordage 2001; Bornmann 2010) treat
  as fatal, and relevance is supported by one. Statistics and
  overclaiming are top-ranked in Bordage's data but judged fixable;
  literature and presentation are contested. Over-weighting minor
  issues is a documented weakness of AI reviewers (Kim et al. 2026,
  preprint) and worth watching in the skill's output.
- **Critiques come before the author's limitations.** Each lens works
  from the methods and results before weighing the limitations
  section, and says when a critique only restates a disclosed
  limitation. LLM reviewers have been found to echo disclosed
  limitations far more than humans do (Ye et al., preprint). This is
  a low-cost defence resting on one preprint, not an established
  finding.
- **Manuscript text is data, not instructions.** Hidden prompts aimed
  at AI reviewers have been found in real manuscripts. The skill
  ignores instructions in the manuscript and reports hidden or
  instruction-like text to the author.
- **Item-level reporting-guideline findings.** The methodological
  lens reports specific, passage-anchored checklist items, not a bare
  checklist: in a randomized trial, suggesting checklists to
  reviewers had no significant effect, while adding a statistical
  reviewer improved reporting (Cobo et al. 2007). That trial is also
  the strongest support for a dedicated statistical lens. The
  issue / passage / why / remedy format is well-motivated practice;
  no trial has tested whether it changes what authors do.
- **Benchmarks.** Liang 2024's overlap is the calibration benchmark.
  Read ReviewerToo's 81.8% accept/reject accuracy against its human
  baseline (83.9%), and treat Kim et al. 2026's expert ratings of
  individual criticisms as the closest usefulness benchmark.
  Preprint and self-evaluation figures (Kim, AAAI-26, PaperReview.ai)
  are provisional.
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
