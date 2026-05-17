# init

Conversationally bootstrap `MANUSCRIPT_STATE.yaml` for a new or existing
manuscript directory. The conversational counterpart to the CLI's
`scriptorium init <dir>`: the CLI writes a blank-with-comments
template; this skill fills it in with the author's actual intent.

**Category:** utility
**Modifies the manuscript?** No.
**Modifies `MANUSCRIPT_STATE.yaml`?** Yes — only on explicit author
confirmation, only after schema validation passes.

## Why a separate skill (and not just a richer CLI command)

The schema has twelve top-level keys. About a third can be inferred
from the filesystem (title, target type, bibliography paths,
sections). The rest are subjective and benefit from conversational
elicitation: `core_claims`, `known_weaknesses`, `terminology`,
`style.tone`, `style.audience`. A click-prompt walkthrough in the CLI
would be tedious and produce worse output than an author editing the
template directly. A skill that *converses* — surfaces inferred
values, asks about the rest two-at-a-time, validates before writing —
produces better state.

The split is principled: the CLI scaffolds the file; the skill fills
it in. They share the name `init` (matching Claude Code's `/init`
convention) so authors have one verb to remember regardless of
surface.

## What it does

1. **Discover** — locates the manuscript directory and checks for an
   existing `MANUSCRIPT_STATE.yaml`. Reads the bundled JSON Schema.
2. **Infer** — proposes what can be inferred from the filesystem:
   title (from the main file's H1), target type (from section names
   / boilerplate), source format (from predominant file extensions),
   bibliography paths and format (from glob), sections array (from
   sub-files). Every inferred value is offered as a confirmable
   proposal, never as a silent decision.
3. **Elicit** — asks about subjective fields one or two at a time:
   `core_claims`, `known_weaknesses`, `terminology.preferred` /
   `forbidden`, `style.tone`, `style.voice`, `style.audience`,
   `constraints.max_word_count`, `document_phase`. Existing values
   are shown first; the author chooses to update, add to, or leave.
4. **Confirm** — shows the full proposed YAML as a diff against the
   existing file (or template). Validates against the schema. If
   validation fails, surfaces the errors as conversational prompts,
   never as raw `jsonschema` dumps.
5. **Write** — only on explicit author confirmation. Preserves
   template comments for fields left empty so they can be filled in
   later without re-reading the schema.
6. **Suggest next steps** — based on `document_phase.current`, points
   the author at relevant follow-up skills. Suggestions only; never
   auto-invocation.

## What it does not do

- **Write fields not in the schema.** The schema is the source of truth.
- **Silently overwrite existing values.** Existing content is shown
  before any change is proposed.
- **Write the file before validation passes.** Validation precedes
  write.
- **Auto-invoke the v0.1 leaf skills** when the conversation ends.
  `citation-audit`, `reviewer-simulation`, `argumentative-flow` —
  the author invokes those, not this skill.
- **Ask a wall of questions.** Two at a time, max.
- **Replace the CLI's `scriptorium init`.** That command scaffolds
  the file; this skill fills it in. Run the CLI first when starting
  from a clean directory.

## Inputs

- **Manuscript directory** — defaults to the user's current working
  directory; ask if ambiguous.
- **Existing `MANUSCRIPT_STATE.yaml`** (optional) — if present, read
  it and fill missing fields rather than starting over.
- **The bundled JSON Schema** —
  `schemas/manuscript-state.schema.json` from the scriptorium
  install. Read at runtime so the skill stays in sync with schema
  evolution.
- **Directory listing** (optional) — for filesystem inference.
- **First page of the main manuscript file** (optional) — improves
  target-type and title inference.

## Using it

### Inside Claude Code

```text
/scriptorium:init
```

The skill detects the current working directory by default and walks
through discovery → inference → elicitation → confirmation → write.

### Outside Claude Code (Codex, Gemini, Hermes, ChatGPT, …)

```bash
scriptorium prompt-pack --output prompts.md
```

Drop the prompt pack into your agent's context, then ask it to run
`init` on your manuscript directory. The platform-neutral prompt
asks you to paste the existing `MANUSCRIPT_STATE.yaml` (if any),
the schema, a directory listing, and (optionally) the first page of
the main file — substitutes for the file-system access the Claude
Code version has natively.

Or use this single skill's prompt directly:

```bash
cat ~/.claude/plugins/scriptorium/skills/init/prompt.md
```

See [`examples/conversation.md`](examples/conversation.md) for a
worked end-to-end example.

## Conversation pattern

The skill never produces a wall-of-questions form. The conversation
shape is roughly:

```text
init: I see a manuscript directory with `paper.qmd`, `references.bib`,
      and a `sections/` subdir. Looks like a Quarto manuscript. The
      main file's H1 is "Single-cell transcriptomic profiling of
      CD8+ T cell exhaustion in pancreatic ductal adenocarcinoma".
      Should I use that as the title?

author: yes

init: Good. Setting target_type=manuscript, source_format=quarto,
      bibliography.paths=[references.bib], format=bibtex.
      
      The `sections/` directory has six files (00-abstract.md through
      05-supplementary.md). Including them in sections[]?

author: yes, but skip 05-supplementary for now

init: Done. Now the subjective fields — these can't be inferred.
      What is this paper arguing? List the load-bearing claims —
      the things a reader who only reads the abstract should walk
      away believing.

author: [...]
```

…and so on, two prompts at a time, until the author either runs out
of fields or chooses to skip the rest.

## Grounding

This skill is grounded in:

- `schemas/manuscript-state.schema.json` — the canonical field set
  and enum values the elicitation steers toward. The skill reads it
  at runtime so it stays in sync as the schema evolves.
- [`common-critiques-taxonomy`](../../knowledge/peer-review/common-critiques-taxonomy.md)
  — informs *why* certain fields matter for downstream skills.
  `known_weaknesses`, `target_venue`, and `core_claims` are the
  load-bearing inputs for `reviewer-simulation`; capturing them well
  here makes that skill's output much sharper.

This skill is a utility, not an evidence-grounded critique or
transformation. The grounding is intentionally light.

## Composition with other skills

After `init` writes the state file, the natural next moves depend on
`document_phase.current`:

| Phase | Suggested next step |
|---|---|
| `outline`, `draft` | No leaf skill helps much yet. Come back when full draft sections exist. |
| `review`, `revision` | `citation-audit` (existing references) and `reviewer-simulation` (pressure-test). |
| `submission` | `argumentative-flow` on the discussion section catches structural issues a final reader will notice. |

The skill *suggests* these — the author invokes them.

## Design notes

- **Schema is the source of truth.** Hard-coding the field list in
  the prompt would drift as the schema evolves. The skill reads
  `schemas/manuscript-state.schema.json` at runtime to enumerate
  available fields and their enum values.
- **Inference is opt-in.** Every inferred value appears as a
  question, never as a silent decision. The author can always say
  "no, the title is different."
- **Existing values are first-class.** When the file already has
  partial content, the skill never replaces silently. Show, ask,
  update.
- **Conversation pacing.** Two prompts at a time, max. A wall of
  questions produces worse answers than a slow walk.
- **Validation precedes write.** A broken file is never produced;
  validation errors become conversational prompts.

## See also

- [`scriptorium init`](../../docs/src/content/docs/reference/cli.md)
  — the CLI subcommand that scaffolds the blank template. Run it
  first when starting from a clean directory; the `init` skill then
  fills in the elicited values.
- GitHub issue [#28](https://github.com/seandavi/scriptorium/issues/28)
  — the canonical tracking issue.
