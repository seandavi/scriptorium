# scriptorium

> *An agentic scriptorium for scholarly writing.*

Scriptorium is an agentic operating system for scholarly writing.
It coordinates AI capabilities — citation audit, reviewer simulation,
structural analysis — around shared editorial state, so manuscripts,
grants, and reviews are improved as a workflow rather than a series of
one-shot prompts.

## Why this exists

A medieval scriptorium was a coordinated workspace where multiple
scribes copied, annotated, glossed, and corrected manuscripts under
shared conventions. The modern scholarly-writing process — drafting,
citing, reviewing, revising, publishing — has the same shape, but most
AI tools sit outside of it: they generate prose in isolation, lose
context between sessions, and offer no way to compose improvements.

Scriptorium puts the agentic-AI layer *inside* the workflow:

- A single source of editorial truth (`MANUSCRIPT_STATE.yaml`) that
  every skill reads.
- A collection of conservative, single-responsibility skills (citation
  audit, reviewer simulation, argumentative-flow analysis) that emit
  structured outputs another skill can consume.
- A discipline of inspectable transformations: semantic diffs over
  unconstrained rewriting; preserved citations and statistics by
  default; no hidden state.

**A deliberate scope.** Scriptorium operates on prose the author has
written or scaffolding the author has declared. It does not produce
prose from blankness — pre-draft ideation, "help me figure out what
to study", or section-from-scratch generation sit outside what
scriptorium does. That cut is structural, not aspirational: it's
what the existing skills already enforce (citation-audit refuses to
invent citations; argumentative-flow refuses to add claims; venue-fit
refuses to recommend without declared content), and it's what keeps
behaviours auditable rather than vibes-based. The full rationale,
grounded in Hayes' 2012 writing-process model and the AI-writing
failure-modes literature, lives in
[`knowledge/conventions/declared-work-scope.md`](knowledge/conventions/declared-work-scope.md).

The medieval scriptorium had an operating model. The agentic one is
just now being built.

## Install

### Claude Code (recommended)

Scriptorium hosts its own plugin marketplace at
[`seandavi/scriptorium`](https://github.com/seandavi/scriptorium).
Easiest install — no Python toolchain needed:

```text
/plugin marketplace add seandavi/scriptorium
/plugin install scriptorium@scriptorium
```

(`seandavi/scriptorium` is the GitHub `owner/repo` shorthand for
<https://github.com/seandavi/scriptorium>. Append `@v0.1.0` or any
ref to pin.) Skills appear as `scriptorium:tour`,
`scriptorium:init`, `scriptorium:citation-audit`,
`scriptorium:reviewer-simulation`, `scriptorium:argumentative-flow`,
`scriptorium:explain`.

Once installed, run:

```text
/scriptorium:tour
```

This is a short conversational walk-through — three or four turns —
that orients you to scriptorium and ends with one concrete next
command. It writes nothing and invokes no other skill; it's the
single entry point we recommend pointing new users at instead of
linking them to documentation.

Updates: `/plugin marketplace update` then
`/plugin update scriptorium@scriptorium`.

If you also want the Python CLI (`scriptorium init`,
`scriptorium validate`, `scriptorium trace`), or you want a
live-linked dev install, see [INSTALL.md](INSTALL.md).

### Other agents (Codex, Gemini, Hermes, ChatGPT, …)

Each skill ships with a platform-neutral `prompt.md` you can paste into
any LLM directly. To get all skills concatenated into a single
prompt-pack file:

```bash
scriptorium prompt-pack -o scriptorium-prompts.md
```

See [INSTALL.md](INSTALL.md) for per-platform recipes.

## Quick start

```bash
# 1. Scaffold editorial state for your manuscript
scriptorium init /path/to/your/manuscript

# 2. Populate it. Two ways:
#    a) Edit /path/to/your/manuscript/MANUSCRIPT_STATE.yaml directly.
#    b) In Claude Code inside the manuscript repo, run the conversational
#       bootstrap that walks you through core_claims, known_weaknesses,
#       terminology, audience, and tone:
#       /scriptorium:init

# 3. Validate the result
scriptorium validate /path/to/your/manuscript/MANUSCRIPT_STATE.yaml

# 4. Run the leaf skills in Claude Code, inside the manuscript repo:
/scriptorium:citation-audit
/scriptorium:reviewer-simulation
/scriptorium:argumentative-flow
```

A fully-populated reference manuscript lives at
[`templates/MANUSCRIPT_STATE.example.yaml`](templates/MANUSCRIPT_STATE.example.yaml)
(an imaginary biomedical paper that exercises every field in the
schema). Use `scriptorium init --example /tmp/example` to drop a copy
anywhere as a learning aid.

## What's in the box (v0.1)

Four bundled skills, exposed through both Claude Code and the
platform-neutral prompt-pack:

| Skill | Phase | What it does |
|---|---|---|
| `init` | bootstrap | Conversational pass that populates `MANUSCRIPT_STATE.yaml` (core claims, known weaknesses, terminology, audience, tone) and routes to the right next skill for the document phase. Pairs with the `scriptorium init` CLI subcommand, which scaffolds the file. |
| `citation-audit` | leaf | For each scientific claim: identify citation support, evaluate evidence strength, flag overreach. Outputs a structured claim/citation/assessment/recommendation table. No text modification. |
| `reviewer-simulation` | leaf | Simulates four reviewer personas (methodological skeptic, domain expert, translational reviewer, statistical reviewer). Outputs Major/Minor Critiques, Fatal Concerns, Enthusiasm Drivers, Suggested Revisions, Acceptance Risk. |
| `argumentative-flow` | transformative | Improves logical and argumentative coherence while preserving citations, statistics, and terminology. Outputs Structural Diagnosis / Logical Gaps / Proposed Outline / Revised Text / Remaining Weaknesses. |

The `scriptorium` CLI exposes six subcommands: `install`, `init`,
`validate`, `prompt-pack`, `list`, and `trace`. `scriptorium trace`
extracts skill invocations from Claude Code transcripts as structured
records conforming to `schemas/trace.schema.json` — useful for
self-inspection and (eventually) eval-loop work. See
`scriptorium --help` for the full surface.

Deliberately not in v0.1 (see [DESIGN.md](DESIGN.md) for the build
order): orchestrators, drafting skills, additional knowledge-layer
contributions beyond what skills currently cite, Codex/Gemini
adapters. These earn their way in once the v0.1 skills have been used
on real manuscripts.

## Companion tools

Scriptorium is the editorial layer; these tools are useful neighbors
for the rest of the scholarly-writing workflow:

- **[Semantic Scholar MCP](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)**
  and **[PubMed MCP](https://github.com/JackKuo666/PubMed-MCP-Server)**
  — bibliographic lookup and full-text retrieval as MCP servers,
  consumable by Claude Code (and any MCP-aware agent). Pair well with
  `scriptorium:citation-audit` when claims need to be checked against
  primary literature.
- **[quartobot](https://github.com/seandavi/quartobot)** — resolves
  persistent-identifier cite keys (`@pmid:`, `@doi:`) in Quarto
  documents before citeproc renders them. Used inside the scriptorium
  docs build for the `knowledge/` evidence base; useful standalone for
  any Quarto-based scholarly writing.

These are external projects, not bundled with scriptorium. Install
them separately following each project's own instructions.

## Design principles

The system separates:

- **generation** (write new prose)
- **critique** (assess existing prose)
- **validation** (check for structural / factual issues)
- **normalization** (terminology, style, journal conventions)

And prefers:

- inspectable transformations over opaque rewrites
- structured outputs over freeform rambles
- semantic diffs over surface rewrites
- explicit checkpointing over hidden state

See [DESIGN.md](DESIGN.md) for the full design philosophy and the
roadmap.

## Status

v0.1 in flight. Four bundled skills (`init`, `citation-audit`,
`reviewer-simulation`, `argumentative-flow`), the consolidated
`scriptorium` CLI (six subcommands, including `trace` for transcript
analysis), the shared state schema, the trace schema, and the Venice
example. Orchestrators, additional skills, and platform adapters
follow once the leaves prove out on real manuscripts.

## License

Dual-licensed by category:

- **Code** — source under `src/`, tests, schemas, scripts, and configuration files — is [MIT](LICENSE).
- **Documentation and knowledge layer** — the `docs/` site, the `knowledge/` evidence base, top-level prose files (`README.md`, `DESIGN.md`, `INSTALL.md`, `CONTRIBUTING.md`), and per-skill `README.md` files — is [CC BY 4.0](LICENSE-DOCS).
