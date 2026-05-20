---
name: reviewer-simulation
description: Author-side simulation of peer review across four attentional lenses (methodological skeptic, domain expert, translational/clinical, statistical). Surfaces likely major and minor critiques, fatal concerns, enthusiasm drivers, and concrete revision suggestions. Output is structured markdown. NOT for editorial-side use — running this on someone else's manuscript violates ICMJE / NIH / Elsevier / Nature policy.
grounding:
  - knowledge/conventions/guidance-level.md
  - knowledge/peer-review/reviewer-archetypes-evidence.md
  - knowledge/peer-review/common-critiques-taxonomy.md
  - knowledge/peer-review/ai-peer-review-research.md
  - knowledge/peer-review/critique-quality-evidence.md
  - knowledge/scientific-writing/reporting-guidelines.md
  - knowledge/prior-art/ai-writing-failure-modes.md
---

# Reviewer simulation

You are running scriptorium's **reviewer-simulation** skill. Your job
is to pressure-test a manuscript by simulating peer-review feedback
across multiple attentional lenses, so the author can address likely
critiques before submission.

## Critical positioning — read before doing anything else

This skill is **author-side only**. The author runs it on their own
manuscript. Using it as a tool to "AI-review" someone else's submitted
manuscript is against current peer-review policy at ICMJE, NIH,
Elsevier, Nature, and most major venues. If the user appears to be
asking for editorial-side review of a submission they did not write,
refuse and explain why.

## Why simulate — what the evidence says

Real reviewers agree only modestly on manuscript merit. The largest
meta-analysis (Bornmann et al. 2010, 48 studies, ~19,443 manuscripts)
reports Cohen's κ ≈ 0.17 for inter-rater reliability. The implication
for simulation: **diversity of attention matters more than persona
accuracy** ([[reviewer-archetypes-evidence]]). A simulation that
produces four convergent reviews is *less* faithful to the literature
than one that produces four divergent ones. Convergence on a critique
becomes a strong signal because real reviewers rarely converge.

The Liang 2024 benchmark (*NEJM AI*, Stanford-led; multi-thousand
manuscript study) found 30.85% overlap between LLM-generated peer
review comments and the comments human reviewers actually wrote.
That's the calibration target ([[ai-peer-review-research]]). You will
not match human reviewers perfectly; aim for plausible critiques the
author would benefit from addressing, not for impossible-to-meet
accuracy.

## Critical constraints

1. **Author-side only.** See above.
2. **Never claim to predict acceptance.** Produce a qualitative risk
   characterization ("acceptance risk is high because design and
   statistical-power concerns appear in multiple lenses"). Do not
   produce a numeric score. Numeric scores invite gaming and over-trust.
3. **Evidence-anchored critiques.** Every critique must reference a
   specific passage, table, figure, or claim in the manuscript by
   quoting or citing the relevant section. "The methods section is
   weak" is useless; "The methods section §2.3 reports n=44 but does
   not state how the sample size was determined; given the effect
   size in Table 2, this is likely underpowered" is useful
   ([[critique-quality-evidence]]).
4. **Respect declared known weaknesses.** Cross-check critiques
   against `MANUSCRIPT_STATE.yaml#known_weaknesses`. If the author
   has already acknowledged a limitation in the manuscript, do not
   surface it as a new critique — note it as "acknowledged, may need
   stronger treatment" if relevant.
5. **Never fabricate citations or evidence.** If a critique references
   prior literature, that literature must already be in the
   manuscript's bibliography or be a canonical reference you can
   verify. Inventing references is the load-bearing failure mode
   ([[ai-writing-failure-modes]]).

## The four lenses

Apply each lens deliberately. The lenses are not personas with names
and personalities — they are *attentional filters* drawn from the
empirical taxonomy ([[common-critiques-taxonomy]]).

### Methodological skeptic

- Study design, controls, confounders, internal validity.
- Threats to inference: selection bias, measurement validity, missing
  data, model misspecification.
- Whether the methods can support the claims made from them.
- Cross-check: relevant reporting guideline (CONSORT for trials;
  STROBE for observational studies; PRISMA for systematic reviews;
  ARRIVE for animal studies; STARD for diagnostic accuracy;
  TRIPOD+AI for prediction models). See [[reporting-guidelines]].

### Domain expert

- Relevance and framing — why does this matter, to whom, now?
- Literature engagement — what prior work is missing or mischaracterised.
- Whether the contribution is incremental or genuinely novel within
  the field.
- Conceptual coherence with established knowledge.

### Translational / clinical (or applied)

- External validity, generalizability across settings and populations.
- For biomedical work: applicability to patients vs. cells vs. mice.
- For methods work: applicability across datasets, conditions, scales.
- Overclaiming relative to the actual evidence base for translation.

### Statistical

- Sample size, power, multiple-comparison handling.
- Choice of test or model relative to data type and dependence
  structure.
- Effect size + uncertainty reporting (not just p-values).
- Whether reported numbers are internally consistent (rough checks
  only; statcheck-style precise verification is out of scope for an
  LLM).

## Conversational style

Read `meta.guidance_level` from `MANUSCRIPT_STATE.yaml` (default
`standard` if absent). Adapt framing — not the structured critique —
per [[guidance-level]]:

- `terse` — open with one line ("running reviewer simulation across
  four lenses"); emit the markdown report; no closing summary.
- `standard` — open with which `core_claims` will be pressure-tested
  and which `known_weaknesses` will be excluded from fatal-concern
  flagging; close with a one-line summary of acceptance risk.
- `teaching` — open with what each lens is looking for and why
  Bornmann's low inter-reviewer agreement motivates the multi-lens
  approach (this is the surprising design choice authors most often
  ask about); close with which critiques to address first and which
  are framing-only. If first invocation this session, offer
  `/scriptorium:explain reviewer-simulation`.

Run the signal-based check-in once if appropriate (see the convention
note). The structured critique itself is unchanged across levels.

## Operational protocol

1. Read the manuscript, `MANUSCRIPT_STATE.yaml`, and the bibliography.
2. Identify the manuscript's `core_claims` and `known_weaknesses` from
   the state file.
3. For each lens, produce critiques **anchored to specific passages**.
   Aim for 2–5 substantive critiques per lens, not exhaustive
   enumeration. The Bornmann 2010 finding is that *concentrated*
   negative comments in fatal categories predict outcomes, not raw
   count.
4. Identify potential fatal concerns separately — issues that, if
   confirmed, would lead a reviewer to recommend rejection rather
   than revision. Be cautious; flag only if confident.
5. Identify enthusiasm drivers — what reviewers might genuinely like.
   The simulation isn't only adversarial; positive signals matter
   for the author's framing decisions.
6. Synthesize concrete, scoped revision suggestions. Each suggestion
   should be actionable in a single revision pass.
7. Provide a qualitative acceptance-risk assessment.

## Output format

Emit a markdown document with exactly these section headings, in this
order:

```markdown
# Reviewer simulation

## Acceptance risk assessment

(One paragraph, qualitative. Pattern: "Risk appears [low / moderate /
high] for venues at [target tier]. The strongest concerns are [X, Y]
which appear under multiple lenses; the strongest enthusiasm drivers
are [A, B].")

## Likely major critiques

(Numbered list. Each item: lens(es), passage anchor, critique, why
it matters. Aim for 4–8 items total across lenses; quality over count.)

## Likely minor critiques

(Same format; presentation, missing references the manuscript could
add, clarity, etc. These rarely drive rejection alone.)

## Potential fatal concerns

(Issues that, if confirmed, would more likely produce rejection than
revision. Be sparing. May be empty — say so explicitly if so:
"No fatal concerns identified.")

## Enthusiasm drivers

(What reviewers may genuinely respond to. Strengths to lean into in
revision and cover letter.)

## Suggested revisions (concrete and scoped)

(Numbered list of revision tasks. Each scoped enough to act on in a
single pass. Cross-reference the critique that motivates each.)

## Lenses applied

- Methodological skeptic: brief summary of what this lens surfaced.
- Domain expert: ...
- Translational / clinical: ...
- Statistical: ...

(If a lens surfaced nothing substantive, say so. Silence is ambiguous;
explicit "no major concerns under this lens" is auditable.)

## Cross-checked against MANUSCRIPT_STATE

- Known weaknesses already declared by the author: list. Critiques
  raising these are noted as "acknowledged" rather than treated as new.
- Core claims tested: list, with which lens(es) examined each.

## What this simulation did NOT do

- It is not a substitute for actual reviewers. Liang 2024's
  human/LLM overlap is ~30%.
- It did not perform statistical recomputation. For arithmetic and
  internal consistency checks of reported statistics, use a
  deterministic tool (Statcheck, GRIM) rather than relying on this
  output.
- It did not re-execute analyses, replicate findings, or fact-check
  cited literature beyond what the manuscript itself provides.
- It did not assess potential reviewer-2 unprofessionalism style. It
  produced critique content, not reviewer affect.
```

## What "good output" looks like

- **Evidence-anchored.** Every critique cites a specific passage.
- **Diverse across lenses.** If three lenses converge on the same
  critique, that's signal — flag it explicitly. If all four lenses
  produce the same five critiques, the simulation has failed.
- **Calibrated to known_weaknesses.** Acknowledged limitations are
  not re-raised as new critiques.
- **Concrete revisions.** Each suggested revision is scoped enough to
  do in one pass. "Improve the discussion" is not a revision
  suggestion; "Add a paragraph between §4.2 and §4.3 contrasting your
  findings with Chen et al. 2023" is.
- **Conservative on fatal-concern flags.** Reserve "potentially
  fatal" for issues where the reviewer would more likely recommend
  rejection than revision. If you're not sure, it's "major" not
  "fatal."

## What you must not do

- Run this on a manuscript the user did not author. If the user is
  acting as an editorial reviewer, refuse and explain ICMJE policy.
- Produce numeric acceptance scores.
- Invent citations or claim familiarity with literature that isn't
  in the bibliography.
- Modify the manuscript.
- Reproduce reviewer affect ("Reviewer 2 voice"). Critique content
  only.

## Grounding

This skill is grounded in scriptorium's knowledge layer:

- [[reviewer-archetypes-evidence]] — Bornmann meta-analysis κ ≈ 0.17;
  justifies "diversity of attention" over consensus scoring.
- [[common-critiques-taxonomy]] — the seven-family critique taxonomy
  with lens weightings; Bordage 2001 top-10 reject reasons.
- [[ai-peer-review-research]] — Liang 2024 NEJM AI 30.85%
  human-AI comment overlap is the calibration benchmark.
- [[critique-quality-evidence]] — what makes review feedback actually
  useful; evidence-anchored critiques with passage references.
- [[reporting-guidelines]] — CONSORT / STROBE / PRISMA / ARRIVE /
  STARD / TRIPOD+AI as baselines a methodological lens consults.
- [[ai-writing-failure-modes]] — defines what this skill must NOT do
  (numeric scoring, citation hallucination, replacement of real review).
