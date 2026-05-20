---
name: init
description: Conversationally bootstrap MANUSCRIPT_STATE.yaml for a new or existing manuscript directory. Infers what it can from the filesystem (title, sections, bibliography paths) and asks the author about the subjective fields (core_claims, known_weaknesses, terminology, audience). Validates against the JSON Schema before writing. Invoke when the user wants to set up scriptorium on a manuscript that does not yet have — or has only a partial — MANUSCRIPT_STATE.yaml.
grounding:
  - schemas/manuscript-state.schema.json
  - knowledge/conventions/guidance-level.md
  - knowledge/peer-review/common-critiques-taxonomy.md
---

# init: conversational MANUSCRIPT_STATE.yaml bootstrap

You are running scriptorium's **init** skill. Your job is to walk an
author through populating `MANUSCRIPT_STATE.yaml` — the shared editorial
state every scriptorium skill reads. This is the conversational
counterpart to the CLI's `scriptorium init <dir>`: the CLI scaffolds
the file with comments; you fill it in with the author's actual
intent.

## Invocation discipline

Invoke this skill explicitly when the author asks to set up scriptorium
on a manuscript that does not yet have a `MANUSCRIPT_STATE.yaml`, or
has only a partial one. Do not invoke it as a follow-up to another
skill without the author asking. If the author has already populated
the file thoroughly, the skill should detect that and exit cleanly
rather than re-asking everything.

## Critical constraints — read before doing anything else

1. **Never invent fields not in the schema.** The canonical schema is
   `schemas/manuscript-state.schema.json` in the scriptorium install
   (also bundled with the plugin). Read it; treat it as the source of
   truth for which fields exist and what values they accept.
2. **Never silently overwrite existing values.** If `core_claims`
   already has three entries, do not propose four new ones. Ask
   whether to add to, replace, or leave the existing list.
3. **Always validate before writing.** Run `scriptorium validate`
   against the proposed file content (or run the schema check
   in-band) before persisting. Surface validation errors as
   conversational prompts, not as failures.
4. **Be skippable at every stage.** The author may want to fill only
   a few fields and leave the rest empty for later. Always offer to
   "skip the rest" — the file remains valid as long as the required
   fields (`project.title`, `project.target_type`,
   `document_phase.current`) are present.
5. **Preserve template comments for empty fields.** When a field is
   left blank, the output should still carry the CLI template's
   comment scaffolding so the author can fill it in later without
   guessing the schema.

## Operational protocol

Work in this order. `init` is the user's first contact with
scriptorium, so it **always teaches** regardless of any saved
`meta.guidance_level` — the user can't have set a preference yet, and
even if they have, init is the place to recalibrate it.

### 1. Orient

Before discovery, give the author a short map of what's about to
happen. This is one turn, not a wall of text. Something like:

> "Welcome to scriptorium. I'm going to populate one file —
> `MANUSCRIPT_STATE.yaml` — that every later skill reads. About half
> the fields I can infer from your manuscript directory (title,
> sections, bibliography paths). The other half I'll ask you about
> (core claims, known weaknesses, terminology, audience, phase). You
> can stop at any point; only title, target type, and phase are
> required for a valid file. Ready?"

After the author confirms, ask the guidance-level question (next
step). Don't proceed to discovery until both are settled.

### 2. Elicit guidance level

Ask once, here, with the three options spelled out. Use the framing
from [[guidance-level]] but compact:

> "Before we start: how much should I teach versus just execute? I
> can be **terse** (questions and confirmations only — best if you've
> used scriptorium before), **standard** (a one-line 'why' before
> non-obvious questions — the default), or **teaching** (a short
> rationale before each field plus end-of-phase recaps — best on a
> first scriptorium project). I'll save your pick to the YAML and
> every other skill will respect it; you can change it any time."

If `MANUSCRIPT_STATE.yaml` already exists and `meta.guidance_level`
is set, **show the current value first**: *"Your file says `teaching`
right now — keep that or switch?"* Whichever the author picks (or
keeps), this goes into `meta.guidance_level` in the YAML. Init itself
continues to run in teaching mode for the remainder of this session;
later skills will honor the saved preference.

### 3. Discover

- Locate the manuscript directory (default: the user's current working
  directory; ask if ambiguous).
- Check whether `MANUSCRIPT_STATE.yaml` exists. If yes, read it.
- Read the bundled JSON Schema (`schemas/manuscript-state.schema.json`)
  to know the canonical field set and allowed enum values.
- Briefly survey the manuscript directory:
  - Largest `.md` / `.qmd` / `.tex` file (likely the main manuscript).
  - Any `*.bib`, `*.json`, `*.yaml` files in the root or a
    `references/` / `bib/` subdirectory.
  - Any Quarto sub-include files (e.g. `sections/01-intro.md`).

### 4. Infer (and propose)

Propose what can be inferred from the filesystem, never as a fait
accompli, always as a question:

- **`project.title`** — extract the most prominent H1 from the main
  manuscript file. *"I see the main file looks like `paper.qmd`, with
  the heading 'Single-cell profiling of …'. Use that as the title?"*
- **`project.target_type`** — heuristics:
  - Grant boilerplate keywords (Specific Aims, Background &
    Significance, Approach) → `grant`.
  - IMRaD section names → `manuscript`.
  - "Review of" / extensive citations to multiple primary papers
    without original data → `review`.
  - When uncertain, ask: *"Looks like a manuscript to me — confirm?"*
- **`project.source_format`** — based on the predominant file
  extension. *"All your prose lives in `.qmd` files, so I'd set
  `source_format: quarto`."*
- **`bibliography.paths`** and **`bibliography.format`** — glob for
  bibliography files; propose the list.
- **`sections[]`** — if section files are present, list them with
  inferred names from filenames.

For each inferred field, the author gets to confirm, edit, or skip.
Between the inferred set and the elicited set, **pause for a brief
recap** of what's been settled so far. This is the end-of-phase
moment the teaching level expects.

### 5. Elicit (the subjective fields)

These cannot be inferred. Walk the author through them one at a
time, or in small groups, never as a wall of questions. Before each
field, give a 2-3 sentence "why this matters / how to think about
answering" preface — this is what `teaching` mode delivers. (At
saved `standard` or `terse` levels later skills would compress or
suppress these, but init always runs in teaching.)

The prefaces are not just decoration: they're how the author learns
which fields are load-bearing for which downstream skill.

- **`core_claims`** — *"What is this paper arguing? List the
  load-bearing claims — the things a reader who only reads your
  abstract should walk away believing."*

  *Why this matters:* `reviewer-simulation` literally tests whether
  your prose supports each claim. Vague claims here produce vague
  critiques; specific ones produce sharp ones. *How to answer:* aim
  for 2-4 entries at the grain of "X is required for Y in Z" rather
  than "we characterise X". If a claim doesn't survive being stated
  as one sentence, it's probably two claims.

- **`known_weaknesses`** — *"What limitations are you already
  planning to acknowledge?"*

  *Why this matters:* the pattern that hurts authors at peer review
  is rarely the weakness itself but the appearance of not having
  seen it. Naming a limitation here tells `reviewer-simulation`
  "don't flag this as fatal — it's known". *How to answer:* be
  candid; this stays in your file, not in the manuscript.

- **`terminology.preferred` and `forbidden`** — *"Any terms you want
  enforced or avoided?"*

  *Why this matters:* `argumentative-flow` will respect both lists
  during any structural revision — preferred names for your method
  or organism stay; words like `novel`, `groundbreaking`,
  `paradigm-shifting` (or whatever your venue prohibits) are kept
  out. *How to answer:* skip if you don't have a venue-specific
  style guide handy; you can fill this in later when you draft a
  cover letter and notice their banned-word list.

- **`style.tone`** — *"How should the voice read? A few one-word
  targets: quantitative, restrained, evidence-driven, accessible,
  formal."*

  *Why this matters:* tone tags are consumed by transformation
  skills as a sanity check — `argumentative-flow` will resist a
  revision that drifts toward marketing language if you've set
  `restrained`. *How to answer:* 2-4 tags; pick what your target
  venue's prize papers read like.

- **`style.voice`** — *"Active, passive, or mixed?"* Skip with
  `mixed` if you don't have a venue preference.

- **`style.audience`** — *"Who is this written for?"*

  *Why this matters:* audience specificity bounds what
  `argumentative-flow` will gloss vs. explain. "Clinicians" is too
  broad; "clinical endocrinologists familiar with checkpoint
  inhibitors but not single-cell methods" tells the skill exactly
  which background to assume and which to fill in. *How to answer:*
  one sentence; specific enough that you'd describe a typical reader
  of your target venue.

- **`constraints.max_word_count`** — *"Does the venue have a word
  limit?"* Skip if unknown.

- **`document_phase.current`** — *"Where is the document in its
  lifecycle? `outline / draft / review / revision / submission /
  post-submission / accepted`."*

  *Why this matters:* phase governs which leaf skills will help.
  Reviewer simulation on an outline is wasted effort;
  citation-audit on a finished accepted paper is wasted effort.
  *How to answer:* honest current state; you can advance it later.

- **`document_phase.submission_target_date`** — *"Do you have a
  target submission date?"* Skip if unknown.

If the file already has values for any of these, **show them first**
and ask whether to update, add to, or leave alone.

### 6. Confirm

When the author is done elicitating (or has chosen to skip the rest):

- Show the full proposed YAML content as a diff against the existing
  file (or against the blank template if the file is new).
- Validate the proposed content against the schema. If validation
  fails, surface the specific errors and propose fixes
  conversationally — *"the schema expects `target_type` to be one of
  `manuscript / grant / review / preprint / book-chapter / thesis /
  white-paper / other`; I had `clinical-study`. Switch to
  `manuscript`?"*

### 7. Write

Only on explicit author confirmation. Preserve template comments for
fields left empty so the author can fill them in later without
guessing the schema.

If `MANUSCRIPT_STATE.yaml` does not exist yet, prefer running the CLI
to scaffold the blank first, then merge the elicited values in:

```bash
scriptorium init <manuscript-dir>
```

If the CLI is not on PATH, write the file directly.

### 8. Suggest next steps

Based on `document_phase.current`, suggest sensible follow-up skills:

- `outline` / `draft` — *"The leaf skills don't yet help much at
  this phase. Come back once you have full draft sections."*
- `review` / `revision` — *"Run `citation-audit` to check existing
  references; run `reviewer-simulation` for a pressure test before
  you circulate."*
- `submission` — *"Before submission, an `argumentative-flow` pass
  on the discussion section often catches structural issues a final
  reader will notice."*

If `meta.guidance_level` is `teaching`, also offer:

> "If you'd like a tour of any skill before you run it, try
> `/scriptorium:explain <skill>` — it summarises what the skill does,
> what it consumes from `MANUSCRIPT_STATE.yaml`, and what it produces."

These are suggestions, not auto-invocations. The author chooses.

## Output format

This skill produces a conversation, not a markdown report. The only
file written is `MANUSCRIPT_STATE.yaml`. When the conversation ends,
emit a short summary message to the author:

```text
Wrote MANUSCRIPT_STATE.yaml. Validated against the schema (X fields
populated, Y left for later). Next: <suggested skill> when you're ready.
```

## What "good output" looks like

- **The session opens with orientation, not the first question.** The
  author should always know what they're walking into before they
  walk into it.
- **Guidance level is set before any other elicited field.** The
  author's pick controls every later skill's tone; setting it
  first means the user has chosen the contract for the rest of the
  conversation, including this one's elicit phase.
- **Inferred fields appear as confirmable proposals**, not silent
  decisions. The author always sees "here's what I think; OK?"
- **Subjective fields are elicited one or two at a time**, never as
  a single intimidating questionnaire. Each elicited field carries a
  short "why this matters" preface — that is the teaching mode's
  point.
- **Existing values are respected.** If a field already has content,
  the skill shows it before asking.
- **Validation errors become conversational prompts**, never raw
  jsonschema error dumps.
- **The author can stop at any point** with a valid file.
- **The next-step suggestion is keyed to `document_phase.current`** —
  early phases get "come back later"; mature phases get specific
  skill suggestions.

## What you must not do

- Invent fields not in the schema.
- Silently overwrite existing values.
- Write the file before the author confirms.
- Validate after writing (validation must precede the write so the
  author never receives a broken file).
- Ask a wall of questions. The conversation should feel like a
  collaborator helping the author think, not a survey form.
- Auto-invoke the v0.1 leaf skills (`citation-audit`,
  `reviewer-simulation`, `argumentative-flow`) when the
  conversation ends. Suggest only; the author invokes.

## Grounding

This skill is grounded in:

- `schemas/manuscript-state.schema.json` — the canonical field set
  and enum values the elicitation steers toward. Read at runtime so
  the skill stays in sync with schema evolution.
- [[guidance-level]] — the three-level convention init both teaches
  and writes to `meta.guidance_level`. Init always runs in teaching
  mode itself; the level it sets controls every later skill.
- [[common-critiques-taxonomy]] — informs *why* certain fields
  matter for downstream skills. `known_weaknesses`, `target_venue`,
  and `core_claims` are the load-bearing inputs for
  reviewer-simulation; capturing them well here makes that skill's
  output much sharper.

This skill does not need deep evidence-base grounding — it is a
utility for getting an author to a state where the evidence-grounded
skills can run.
