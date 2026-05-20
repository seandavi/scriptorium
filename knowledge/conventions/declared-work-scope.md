# Declared-work scope: where scriptorium does and does not operate

*Last updated: 2026-05-20*

## Synthesis

Scriptorium is scoped to operate on **declared work** — prose the
author has written, or scaffolding the author has committed to in
`MANUSCRIPT_STATE.yaml` (claims, weaknesses, audience, tone, target
venue, terminology). It does not synthesise prose from a blank page,
and it does not act as a thinking partner during the pre-declaration
phase of research (forming hypotheses, choosing a research question,
brainstorming what to study).

The "phase ≥ draft" cut some projects use is a *proxy* for this
principle. Phase works most of the time because by draft phase the
author has declared enough — there's prose to critique, there's
state filled in. But phase misses the harder cases: a draft
manuscript with an empty Related Work section is in `draft` phase
yet asking a skill to fill that section is a blank-slate generation.
Conversely, a `revision`-phase author asking "do my claims need
stronger limitations framing?" is in scope even if the limitations
text isn't yet written — what matters is that `known_weaknesses` is
declared. The phase axis is too coarse; the declared-work axis is
the actual principle.

This note documents the convention so every skill grounds in the
same rule and so a contributor proposing a new skill knows where
the line is.

## The principle, stated

> **Scriptorium operates on prose the author has written or
> scaffolding the author has declared. It does not produce prose
> from blankness.**

Two corollaries follow:

1. **Generation is not forbidden, but it must be a transformation
   of declared inputs.** A v0.4 `specific-aims` skill that turns
   declared significance + hypotheses + methods into aims prose is
   in scope — the generation is bounded by what the author has
   already committed to. A hypothetical skill that helps an author
   "figure out what to study" is *not* in scope — there is nothing
   declared to ground it.
2. **Refusal is the right behaviour at the boundary.** When a user
   asks a skill to operate on prose that doesn't exist (an empty
   section, a missing chapter), the skill refuses cleanly and points
   the user at the pre-declaration work that needs to happen first.
   It does not silently degrade into best-effort blank-slate
   generation.

## Why this is the right cut — supporting evidence

### Cognitive process: Hayes' 2012 writing model

The [[hayes-flower-writing-model]] note documents Hayes' 2012
revision of the canonical cognitive-process model of writing. The
revised architecture splits writing into four sub-processes:
**proposer** (generates content), **translator** (turns proposals
into language), **transcriber** (orthography), and **evaluator**
(reviewer role), under a control structure that arbitrates between
them.

Scriptorium's declared-work scope maps cleanly onto this:

- **Proposer** — out of scope. Generating content from nothing is
  precisely the activity that requires partnership, intuition, and
  domain knowledge the author owns. Scriptorium does not propose.
- **Translator** — in scope when proposals are declared. Turning a
  declared core claim into a sharper sentence is translation, not
  proposing. `argumentative-flow` lives here.
- **Transcriber** — trivially in scope; orthography-level work is
  what most editors already do.
- **Evaluator** — clearly in scope. `citation-audit`,
  `reviewer-simulation`, `desk-rejection-risk`, and gap-finder are
  all evaluator-role skills.

The proposer/translator split is the cleanest expression of where
scriptorium lives. Hayes' revised model treats *working memory as
the bottleneck* on the writer; scriptorium's discipline is to
absorb the translator and evaluator load so the author's working
memory stays available for proposing. Stepping into the proposer
role would defeat that purpose.

### Failure modes: blank-slate generation in scholarly writing

The [[ai-writing-failure-modes]] note collects the canonical
failure modes of LLM scholarly writing. The two most cited —
**hallucinated references** and **authorial-voice loss / lexical
homogenisation** — are both failure modes of blank-slate
generation. They do not happen (or happen much less) when the model
is operating on declared inputs:

- Hallucinated citations require the model to *invent* sources to
  back unbacked claims. A skill that audits declared citations
  against bibliographic metadata can't hallucinate; a skill that
  generates prose from blankness must.
- Lexical homogenisation happens when an LLM smooths an author's
  distinctive prose into a centre-of-distribution voice. This is a
  generation-side failure mode; a skill operating on declared text
  has the author's voice as input and can preserve it.

The declared-work scope is the project's structural defence
against these failure modes. Each skill's specific guard — "no
invented citations" for `citation-audit`, "preserve hedging and
stance markers" for `argumentative-flow`, "never claim full-text
verification of papers you haven't seen" — is the same principle
applied to that skill's surface.

### Negative exemplar: end-to-end generation systems

The [[ai-agentic-scientific-writing]] note surveys the existing
end-to-end-generation landscape (Sakana AI Scientist, AutoBA, etc.).
The independent evaluation by Beel et al. (arXiv:2502.14297) on
the original AI Scientist found:

- 42% of experiments failed due to coding errors.
- Literature reviews used simplistic keyword search and
  misclassified established concepts (micro-batching for SGD) as
  novel.
- Generated papers had a median of **5 citations**.
- Outputs contained structural errors including missing figures and
  placeholder text like "Conclusions Here".

These are the failure modes of blank-slate generative scholarly
writing in their fully expressed form. Scriptorium's declared-work
scope is the project's positioning *against* this trajectory.
The thesis is not that generation is impossible; it is that
generation grounded in author-declared scaffolding is a different
class of problem from end-to-end generation, and scriptorium is
sized for the former.

### Positive exemplar: GeneAgent's verify-before-emit pattern

The same survey note documents GeneAgent's design: generate →
check against domain database → modify → summarise. This is the
*grounded* version of generation: every generation step verifies
against an authoritative source before its output is emitted.
Scriptorium's declared-work scope is the manuscript-writing
analogue — every skill verifies against the author's declared
state before its output is emitted.

## How a skill cashes this out

Each skill applies the principle to its own surface. The
manifestations vary, but the shape is consistent:

| Skill | Declared inputs | What it refuses to invent |
|---|---|---|
| `init` | (none yet; this is where declarations are set up) | — |
| `tour` | None; pure orientation | Anything beyond what's in the plugin tree |
| `citation-audit` | Manuscript prose + bibliography | New citations to back unbacked claims |
| `reviewer-simulation` | Manuscript + `core_claims` + `known_weaknesses` + `target_venue` | Critiques of work not in the manuscript |
| `argumentative-flow` | Manuscript section + terminology + tone preferences | New claims; new citations; voice changes |
| `desk-rejection-risk` | Manuscript + `target_venue` | Generic advice; runs only with a declared venue |
| `terminology-normalization` | Manuscript + `terminology.*` lists | Stylistic flattening beyond declared preferences |
| `explain` | Plugin tree only | Anything outside the tree |
| `gap-finder` (proposed) | Manuscript + state | Prose to fill the gap; citations to fill it |

The pattern: every skill names what it consumes from the
author's declarations, and every skill names what it refuses to
synthesise from blankness.

## Refusal behaviour at the boundary

When a user asks a skill to operate beyond its declared-work
boundary, the skill should:

1. **Name the refusal explicitly.** "I can't draft the section
   because there's nothing there yet to ground against" is better
   than degrading into a best-effort attempt.
2. **Point at the pre-declaration work that needs to happen
   first.** "Sketch a stub for the section — even a few sentences
   declaring what claims it will make — and I can identify gaps
   against that stub." The author owns the proposer step.
3. **Not lecture.** The boundary is structural, not pedagogical.
   One clear sentence is enough; no need to explain the
   declared-work principle every time it fires.

This refusal pattern is the same shape as the per-skill failure
guards (`citation-audit`'s "no invented citations", etc.). It is
the principle at a different scope.

## When this convention may need to evolve

This is the v0.1–v0.3 scope. It is a defensible cut for now and
will be revisited as the project matures. Plausible reasons to
revisit:

- **A future v0.5+ "ideation" skill** with sufficient guardrails
  (declared topic area, declared methods constraints, declared
  audience) might be in scope as a *bounded* proposer-side
  contribution. The principle would not change — the inputs would
  shift — but the rules for what "declared" means at the proposer
  surface would need their own grounding work.
- **Composition with external generative tools** (a scriptorium
  pipeline that calls out to a domain-specific generator, then
  audits its output against the declared state) is a future
  question. The declared-work scope says scriptorium itself does
  not generate; it does not say scriptorium can't *audit* an
  external generator's output.
- **Author-side configuration of the boundary** (a power user who
  declares "I am explicitly inviting blank-slate help here") would
  need to be explicit and per-invocation; the project's default
  posture should remain refusal at the boundary.

These are not v0.1 decisions. The current convention is: declared
work or nothing, with refusal as the boundary behaviour.

## Implementation priority for scriptorium

**Verdict:** Documented convention. Already implicit in every
v0.1 skill; explicit grounding here so future skills can be
audited against it and so contributors know where the line is.

**How a skill adopts it:**

1. Add `knowledge/conventions/declared-work-scope.md` to the
   skill's `grounding:` list in `SKILL.md`.
2. The skill's "Inputs" section should explicitly enumerate the
   declared work it consumes (manuscript prose, specific
   `MANUSCRIPT_STATE.yaml` fields, bibliography paths).
3. The skill's "What this skill does NOT do" section should name
   the specific blank-slate behaviours it refuses — using language
   from this convention if useful.
4. If the skill could plausibly be asked to operate beyond the
   boundary (an empty section, a missing chapter), its operational
   protocol should include the refusal behaviour above.

**What this is not:** This is not a verbosity rule or a refusal
template. It is the project's structural commitment about where
scriptorium operates. Skills should *embody* the principle, not
*recite* it.

## Cross-references

- [[hayes-flower-writing-model]] — cognitive-process model;
  the proposer/translator/evaluator distinction underlying this
  convention.
- [[ai-writing-failure-modes]] — the failure-mode literature
  the declared-work scope is the structural defence against.
- [[ai-agentic-scientific-writing]] — end-to-end generation
  survey; the negative exemplar this scope positions against.
- [[guidance-level]] — the sister convention controlling *how
  much* scriptorium teaches at each level. Declared-work-scope
  controls *where* scriptorium operates; guidance-level controls
  *how* it talks when it does.
