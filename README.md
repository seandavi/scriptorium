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

The medieval scriptorium had an operating model. The agentic one is
just now being built.

## Install

### Claude Code (recommended)

```bash
# Personal use (live-link the dev copy)
./scripts/dev-link.sh

# Or install a copy to your Claude plugins dir
./scripts/install-claude.sh
```

Restart Claude Code; the skills appear as `scriptorium:citation-audit`,
`scriptorium:reviewer-simulation`, `scriptorium:argumentative-flow`.

### Other agents (Codex, Gemini, Hermes, ChatGPT, …)

Each skill ships with a platform-neutral `prompt.md` you can paste into
any LLM directly. To get all skills concatenated into a single
prompt-pack file:

```bash
./scripts/prompt-pack.py > scriptorium-prompts.md
```

See [INSTALL.md](INSTALL.md) for per-platform recipes.

## Quick start

```bash
# 1. Initialize editorial state for your manuscript
cp templates/manuscript-state.template.yaml \
   /path/to/your/manuscript/MANUSCRIPT_STATE.yaml

# 2. Edit the file — fill in title, core claims, terminology, etc.

# 3. Validate it
python scripts/validate-state.py /path/to/your/manuscript/MANUSCRIPT_STATE.yaml

# 4. In Claude Code, inside the manuscript repo:
/scriptorium:citation-audit
/scriptorium:reviewer-simulation
/scriptorium:argumentative-flow
```

A populated example for the Venice 2026 spatial hackathon manuscript
lives at [`examples/venice-paper/MANUSCRIPT_STATE.yaml`](examples/venice-paper/MANUSCRIPT_STATE.yaml).

## What's in the box (v0.1)

| Skill | Phase | What it does |
|---|---|---|
| `citation-audit` | leaf | For each scientific claim: identify citation support, evaluate evidence strength, flag overreach. Outputs a structured claim/citation/assessment/recommendation table. No text modification. |
| `reviewer-simulation` | leaf | Simulates four reviewer personas (methodological skeptic, domain expert, translational reviewer, statistical reviewer). Outputs Major/Minor Critiques, Fatal Concerns, Enthusiasm Drivers, Suggested Revisions, Acceptance Risk. |
| `argumentative-flow` | transformative | Improves logical and argumentative coherence while preserving citations, statistics, and terminology. Outputs Structural Diagnosis / Logical Gaps / Proposed Outline / Revised Text / Remaining Weaknesses. |

Deliberately not in v0.1 (see [DESIGN.md](DESIGN.md) for the build
order): orchestrators, drafting skills, knowledge layer, Codex/Gemini
adapters. These earn their way in once the v0.1 skills have been used
on real manuscripts.

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

v0.1 in flight. Three leaf skills + shared state schema + Venice
example. Orchestrators, additional skills, and platform adapters
follow once the leaves prove out on real manuscripts.

## License

Dual-licensed by category:

- **Code** — source under `src/`, tests, schemas, scripts, and configuration files — is [MIT](LICENSE).
- **Documentation and knowledge layer** — the `docs/` site, the `knowledge/` evidence base, top-level prose files (`README.md`, `DESIGN.md`, `INSTALL.md`, `CONTRIBUTING.md`), and per-skill `README.md` files — is [CC BY 4.0](LICENSE-DOCS).
