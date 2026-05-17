---
name: init
description: Conversationally bootstrap MANUSCRIPT_STATE.yaml for a new or existing manuscript directory. Infers what it can from the filesystem (title, sections, bibliography paths) and asks the author about the subjective fields (core_claims, known_weaknesses, terminology, audience). Validates against the JSON Schema before writing. Invoke when the user wants to set up scriptorium on a manuscript that does not yet have — or has only a partial — MANUSCRIPT_STATE.yaml.
grounding:
  - schemas/manuscript-state.schema.json
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

Work in this order:

### 1. Discover

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

### 2. Infer (and propose)

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

### 3. Elicit (the subjective fields)

These cannot be inferred. Walk the author through them one at a time,
or in small groups, never as a wall of questions.

- **`core_claims`** — *"What is this paper arguing? List the
  load-bearing claims — the things a reader who only reads your
  abstract should walk away believing. Critique skills test whether
  the prose actually supports each claim; transformation skills
  preserve them."*
- **`known_weaknesses`** — *"What limitations are you already
  planning to acknowledge? Reviewer-simulation will not flag these
  as fatal because they're already known."*
- **`terminology.preferred` and `forbidden`** — *"Are there terms
  you want enforced or avoided? For example: preferred names for
  your method or organism; words like 'novel' or 'groundbreaking'
  the journal asks you to avoid."*
- **`style.tone`** — *"How should the voice read? A few one-word
  targets: quantitative, restrained, evidence-driven, accessible,
  formal."*
- **`style.voice`** — *"Active, passive, or mixed?"*
- **`style.audience`** — *"Who is this written for? Specific enough
  to inform tone — `clinical endocrinologists familiar with
  checkpoint inhibitors but not single-cell methods` is the right
  level."*
- **`constraints.max_word_count`** — *"Does the venue have a word
  limit?"* Skip if unknown.
- **`document_phase.current`** — *"Where is the document in its
  lifecycle? `outline / draft / review / revision / submission /
  post-submission / accepted`."*
- **`document_phase.submission_target_date`** — *"Do you have a
  target submission date?"* Skip if unknown.

If the file already has values for any of these, **show them first**
and ask whether to update, add to, or leave alone.

### 4. Confirm

When the author is done elicitating (or has chosen to skip the rest):

- Show the full proposed YAML content as a diff against the existing
  file (or against the blank template if the file is new).
- Validate the proposed content against the schema. If validation
  fails, surface the specific errors and propose fixes
  conversationally — *"the schema expects `target_type` to be one of
  `manuscript / grant / review / preprint / book-chapter / thesis /
  white-paper / other`; I had `clinical-study`. Switch to
  `manuscript`?"*

### 5. Write

Only on explicit author confirmation. Preserve template comments for
fields left empty so the author can fill them in later without
guessing the schema.

If `MANUSCRIPT_STATE.yaml` does not exist yet, prefer running the CLI
to scaffold the blank first, then merge the elicited values in:

```bash
scriptorium init <manuscript-dir>
```

If the CLI is not on PATH, write the file directly.

### 6. Suggest next steps

Based on `document_phase.current`, suggest sensible follow-up skills:

- `outline` / `draft` — *"The leaf skills don't yet help much at
  this phase. Come back once you have full draft sections."*
- `review` / `revision` — *"Run `citation-audit` to check existing
  references; run `reviewer-simulation` for a pressure test before
  you circulate."*
- `submission` — *"Before submission, an `argumentative-flow` pass
  on the discussion section often catches structural issues a final
  reader will notice."*

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

- **Inferred fields appear as confirmable proposals**, not silent
  decisions. The author always sees "here's what I think; OK?"
- **Subjective fields are elicited one or two at a time**, never as
  a single intimidating questionnaire.
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
- [[common-critiques-taxonomy]] — informs *why* certain fields
  matter for downstream skills. `known_weaknesses`, `target_venue`,
  and `core_claims` are the load-bearing inputs for
  reviewer-simulation; capturing them well here makes that skill's
  output much sharper.

This skill does not need deep evidence-base grounding — it is a
utility for getting an author to a state where the evidence-grounded
skills can run.
