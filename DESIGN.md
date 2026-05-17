# DESIGN

The design rationale for `scriptorium`: an agentic operating system for
scholarly writing.

## The thesis

AI changes the operating model of scholarly writing in the same way it
changes the operating model of research institutions more broadly. The
question isn't whether AI generates prose — that's table stakes — but
how it composes with the rest of the editorial workflow: shared state,
inspectable transformations, structured outputs, conservative edits,
versioned revisions. Scriptorium is that operating model, shipped as
code.

The medieval scriptorium had:

- A coordinated workspace (the room itself)
- Shared conventions (paleographic, structural, citational)
- Multiple specialized roles (copyist, illuminator, glossator, corrector)
- An inspectable artifact at every stage (the in-progress manuscript)

The agentic scriptorium has:

- A coordinated workspace (the manuscript repo, with `MANUSCRIPT_STATE.yaml`)
- Shared conventions (the schema; the structured-output discipline; preservation rules)
- Multiple specialized capabilities (citation-audit, reviewer-simulation, argumentative-flow, …)
- An inspectable artifact at every stage (semantic diffs, structured critiques, checkpointed revisions)

## Design philosophy

The system separates four kinds of operations:

| Category | What it does | Example skills |
|---|---|---|
| **Generation** | Produces new prose | (Phase 2: specific-aims, discussion-drafting) |
| **Critique** | Assesses existing prose without modifying it | citation-audit, reviewer-simulation |
| **Validation** | Checks for structural / factual / consistency issues | (Phase 3: figure-text-alignment, statistics-consistency) |
| **Normalization** | Applies style, terminology, journal conventions | (Phase 3: terminology-normalization, journal-style-conversion) |
| **Transformation** | Modifies prose to improve specific properties | argumentative-flow, (Phase 2: compression, redundancy-removal) |

And prefers:

- **Inspectable transformations.** Every edit is reviewable. No hidden rewrites.
- **Structured outputs.** Skills emit predictable section headers so downstream skills can consume them.
- **Semantic diffs.** When prose changes, the change is justified and minimized.
- **Checkpointing.** Long workflows checkpoint between stages; nothing is irreversible.

And avoids:

- **Giant prompts.** Each skill has one responsibility.
- **Unconstrained rewriting.** Transformative skills preserve citations, statistics, and terminology by default.
- **Hidden state.** Everything load-bearing lives in `MANUSCRIPT_STATE.yaml` or in explicit skill arguments.
- **Citation hallucination.** Critique skills don't invent citations; transformation skills don't add them.

## The shared-state contract

Every project that uses scriptorium maintains a `MANUSCRIPT_STATE.yaml`
file at its root. The schema is defined in `schemas/manuscript-state.schema.json`.
The file declares:

- Project metadata (title, target type, target venue)
- Document phase (draft, review, revision, submission)
- Core claims (what the manuscript is arguing)
- Known weaknesses (limitations the authors have already acknowledged)
- Terminology (preferred + forbidden words)
- Style (tone, voice)
- Constraints (preserve_citations, preserve_statistics, avoid_hype)

Every skill reads this file. Critique skills use it to ground their
assessment. Transformation skills use it to bound their edits. The
file is the gravity well that keeps the workflow coherent across
sessions and across skills.

A skill that doesn't read `MANUSCRIPT_STATE.yaml` is doing something
local — fine for utilities, but it isn't part of the OS.

## Skill granularity

One skill = one responsibility.

Good:

- `citation-audit` (audit citations)
- `argumentative-flow` (improve logical flow)
- `compression` (reduce length without losing meaning)

Bad:

- `improve-paper` (does what? touches what? touches everything?)
- `make-it-better` (no contract; no inspectability)

Granularity matters because composition matters. An orchestrator
calling 5 narrow skills produces an inspectable trace; an orchestrator
calling 1 wide skill produces a black box.

## Conservative-edit posture

Transformation skills default to:

- Preserving every citation
- Preserving every quantitative statement
- Preserving terminology declared in `MANUSCRIPT_STATE.yaml`
- Minimizing rewrite surface area
- Explaining each modification

This is uncomfortable for skills like `argumentative-flow` that want
to move things around — but the discomfort is the point. A scriptorium
copyist who silently improved the author's prose was not a copyist;
they were a problem. The same applies here.

Skills that need to make aggressive changes should be invoked
explicitly, named loudly in their description, and emit a clear
"Remaining Weaknesses" section so the author sees what they didn't
fix.

## Invocation discipline

Skills come in two flavors:

- **Auto-invocable** — the model may suggest these when their
  description matches the user's intent. Reserved for read-only
  critique skills where over-invocation costs nothing.
- **Explicit-only** — must be invoked by name (`/scriptorium:<name>`).
  Reserved for transformative skills where surprise rewrites are
  unwanted.

A skill's description declares which mode it intends. There's no
automatic enforcement — the discipline is in the description language
and in user habit.

## Defensive design choices

Several of scriptorium's design choices are *responses* to documented
failure modes of AI writing assistance. The choices look conservative
because the failure modes are real.

### Hallucinated citations

LLMs reliably invent references with plausible authors, journals, and
DOIs ([Walters & Wilder 2023 *Sci Reports*][walters-wilder-2023];
[Bhattacharyya et al. 2023 *Cureus*][bhattacharyya-2023]). Scriptorium's
critique skills (`citation-audit`, `reviewer-simulation`) **must not
generate, suggest, or add citations** under any circumstances. They can
only assess existing ones. This is hardcoded by convention and by
`MANUSCRIPT_STATE.yaml`'s `constraints.preserve_citations: true`
default. See [`knowledge/citations/hallucination-in-llm-citations.md`](knowledge/citations/hallucination-in-llm-citations.md).

### Authorial-voice loss / "ChatGPT smell"

[Kobak et al. 2024][kobak-2024] documented the lexical fingerprint of
LLM-edited scientific writing — over-use of "delve," "intricate,"
"underscore," and similar markers. Scriptorium's conservative-edit
posture (preserve source language, transformations are minimal and
inspectable, never auto-invoked) is the design defense against this.
We don't claim to eliminate the smell, only to minimize and surface it.
See [`knowledge/prior-art/ai-writing-failure-modes.md`](knowledge/prior-art/ai-writing-failure-modes.md).

### Automation complacency

[Parasuraman & Manzey 2010][parasuraman-2010] established that users
over-rely on automated decision aids, missing what the aid missed.
Scriptorium's structured outputs include explicit **"What this skill
did NOT check"** sections, forcing the user to engage with the limits
rather than treating the output as comprehensive.

### Suggestion-acceptance bias

Buschek, Jakesch, and colleagues' CHI work shows users accept LLM
suggestions even when they would have written differently — biasing
the resulting prose toward the model's stylistic defaults. Scriptorium
transformative skills are **explicit-invocation only** (never
auto-invoked) and emit inspectable diffs so the user can reject as
easily as accept.

### Author skill degradation

This is the failure mode scriptorium does **not** defend against.
Over-reliance on AI writing assistance plausibly atrophies the
underlying skill, but the evidence is too early to design around. We
flag this honestly as a known limit rather than pretend the
conservative-edit posture solves it. Author retains responsibility for
their writing.

[walters-wilder-2023]: https://doi.org/10.1038/s41598-023-41032-5
[bhattacharyya-2023]: https://doi.org/10.7759/cureus.39238
[kobak-2024]: https://arxiv.org/abs/2406.07016
[parasuraman-2010]: https://doi.org/10.1177/0018720810376055

## Scope

Scriptorium's evidence base is most thoroughly grounded in **biomedical
and clinical reporting standards** — EQUATOR Network guidelines,
CONSORT, STROBE, PRISMA, ARRIVE, STARD, TRIPOD+AI, CONSORT-AI/SPIRIT-AI.
This is where the reporting-guideline density is highest, where the
LLM-hallucination evidence is most thoroughly studied, and where the
audience overlap is greatest with the project's authors and
contributors.

Extensions to other fields — physics (PRL "Letters" format), CS/ML
(NeurIPS norms, no-theorems-vs-theorems papers), qualitative social
science, mathematics (theorem-proof structure), economics (alphabetical
authorship), humanities (argument-driven, not IMRaD) — are welcome
but not yet evidenced. PRs adding discipline-specific knowledge
layers and skill variants are explicitly invited; see
[`knowledge/scientific-writing/discipline-conventions.md`](knowledge/scientific-writing/discipline-conventions.md)
for the landscape.

For v0.1–v0.3, default behavior assumes biomedical/clinical conventions.
This is stated, not silent — so readers in other fields encounter the
bias as explicit scope rather than hidden assumption.

## Roadmap

### v0.1 (this release): the leaves

Three skills, schema, Venice example. Goal: prove the shared-state +
structured-output pattern works on a real manuscript. If the three
skills don't compose usefully on the Venice paper, the design is
wrong and we revisit before building more.

- `citation-audit` (critique)
- `reviewer-simulation` (critique)
- `argumentative-flow` (transformation)

### v0.2 (next): coordination

If v0.1 holds up, add the first orchestrator. The orchestrator's
sole job is to sequence the leaves intelligently for a given
document phase.

- `manuscript-pipeline` (orchestrator)
- `revision-summary` (utility)

### v0.3: more leaves

Once the orchestrator pattern works, add high-leverage additional
leaves driven by what we needed and didn't have.

Likely candidates: `compression`, `redundancy-removal`,
`statistics-consistency`, `terminology-normalization`. Order
determined by which gap bites first.

### v0.4: drafting

Generation skills are harder than critique skills — they're the most
opinionated and the most likely to produce off-key prose. Defer until
the critique/validation/normalization layers are mature enough to
catch generation mistakes.

Likely candidates: `specific-aims`, `results-narrative`,
`discussion-drafting`.

### v0.5+: knowledge layer + platform adapters

Once skill content stabilizes:

- A `knowledge/` directory of reusable editorial heuristics (journal
  styles, grant-program patterns, reviewer-archetype tells) that
  individual skills reference explicitly.
- Adapters that compile SKILL.md down to platform-neutral prompts for
  Codex / Gemini / ChatGPT / Hermes / etc.

## Naming

The project is `scriptorium`. Repo name on GitHub will be
`seandavi/scriptorium`. PyPI package name, if published, will be
something more disambiguated (e.g., `agentic-scriptorium`) because
the bare PyPI name is taken — but the project itself is `scriptorium`
everywhere it appears in narrative.

The tagline is *an agentic scriptorium for scholarly writing*. Use it
in talks, posts, papers. The repo name does the search/install work;
the tagline does the brand work.

## Non-goals

- **Replacing pandoc/Quarto/LaTeX.** Scriptorium produces structured
  outputs about prose; it does not produce final-formatted documents.
- **Replacing a reference manager.** Citation audit works with whatever
  bibliography the manuscript already uses.
- **Replacing peer review.** Reviewer simulation is a sparring partner,
  not a substitute for real reviewers.
- **Generating manuscripts from scratch.** This is intentionally not a
  v0.1 goal. The harder design questions are about coordination, not
  generation.

## Why this is open source

The thesis — that AI changes the operating model of research
institutions — is more credible when the operating model itself is
inspectable. A closed-source agentic scriptorium would be a black-box
peer-review-as-a-service play; an open one is documentation of what
the new operating model actually looks like, available to anyone who
wants to fork it.

Practically: the scholarly-writing audience is small enough that
network effects come from openness, not from lock-in.
