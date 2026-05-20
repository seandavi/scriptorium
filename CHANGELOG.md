# Changelog

All notable changes to scriptorium are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project uses [PEP 440](https://peps.python.org/pep-0440/) /
[Semantic Versioning](https://semver.org/) for version numbers. Pre-1.0
releases are exploratory: the shape of skills, CLI surface, and shared
state schema may change between versions.

## [Unreleased]

### Added

- Self-hosted Claude Code plugin marketplace at
  `.claude-plugin/marketplace.json`. Users can now install scriptorium
  with `/plugin marketplace add seandavi/scriptorium` followed by
  `/plugin install scriptorium@scriptorium`, with no Python toolchain
  required. The existing `scriptorium install` CLI paths (dev-link,
  copy) remain available for users who also want the Python CLI.
  README.md and INSTALL.md updated; `tests/test_marketplace.py`
  validates the manifest shape and that declared plugin sources
  resolve.

- `meta.guidance_level` field on `MANUSCRIPT_STATE.yaml` (enum:
  `terse | standard | full`, default `standard`). Persisted
  user-side preference for how much framing each skill should add
  around its structured work. The `full` level is designed to teach
  the workflow as the author uses it — upfront orientation,
  per-field rationale, end-of-phase recaps. Set by
  `scriptorium:init`; honored by every conversation-bearing skill.
  The convention is documented at
  `knowledge/conventions/guidance-level.md` and grounded into
  every adapting skill's frontmatter, with a signal-based
  once-per-session check-in protocol so the level can be
  recalibrated without nagging.

- `scriptorium:explain` skill. Read-only meta-skill that
  synthesises a one-screenful tour of scriptorium (no arg), a named
  skill (`/scriptorium:explain citation-audit`), a
  `MANUSCRIPT_STATE.yaml` field
  (`/scriptorium:explain meta.guidance_level`), or a knowledge note
  by slug. Reads the plugin tree only; consumes no manuscript
  content. Users at the `full` guidance level are nudged toward
  this skill from the leaf skills.

- `scriptorium:init` now opens with a short orientation turn and
  elicits `meta.guidance_level` as its first question (with the
  three options explained). Each subjective field
  (`core_claims`, `known_weaknesses`, `terminology.*`,
  `style.tone`, `style.audience`, `document_phase.current`) now
  carries a 2-3 sentence "why this matters / how to think about
  answering" preface. Init itself always runs at the `full` level
  regardless of saved preference, because that's where the
  preference is set.

### Fixed

- Knowledge layer is now packaged with the plugin. Wheel installs,
  sdist, and `scriptorium install` (copy mode) previously did not
  ship `knowledge/`, leaving skill `grounding:` references
  unresolvable in CLI installs. The full knowledge tree now ships
  alongside `schemas/`, `skills/`, and `templates/`. Marketplace
  installs already shipped knowledge (they clone the whole repo),
  so behaviour there is unchanged.

## [0.1.0.dev0] - 2026-05-19

The first published dev pre-release. This is the "skills usable end-to-end
on real manuscripts; everything else still earning its way in" cut.

### Added

#### Skills

Four bundled skills, each shipped as a Claude Code skill
(`scriptorium:<name>`) and as a platform-neutral `prompt.md` you can paste
into any LLM:

- **`init`** — conversational pass that populates a fresh
  `MANUSCRIPT_STATE.yaml` (core claims, known weaknesses, terminology,
  audience, tone) and routes to the right next skill for the manuscript's
  current phase. Pairs with the `scriptorium init` CLI subcommand, which
  scaffolds the file.
- **`citation-audit`** — for each scientific claim, identify citation
  support, evaluate evidence strength, and flag overreach. Outputs a
  structured claim / citation / assessment / recommendation table.
  Inspectable; never modifies prose.
- **`reviewer-simulation`** — simulates four reviewer lenses
  (methodological skeptic, domain expert, translational reviewer,
  statistical reviewer). Outputs Major/Minor Critiques, Fatal Concerns,
  Enthusiasm Drivers, Suggested Revisions, Acceptance Risk. Deliberately
  uses *lenses*, not "personas", grounded in the low inter-reviewer
  agreement literature (Bornmann κ≈0.17).
- **`argumentative-flow`** — improves logical and argumentative coherence
  while preserving citations, statistics, and terminology. Outputs
  Structural Diagnosis / Logical Gaps / Proposed Outline / Revised Text /
  Remaining Weaknesses.

#### CLI

A single `scriptorium` console script (Click-based) with six subcommands:

- `scriptorium install` — install the Claude Code plugin into
  `~/.claude/plugins/scriptorium/`. Supports `--mode dev-link` (symlink,
  edits propagate) and the default copy install.
- `scriptorium init` — scaffold `MANUSCRIPT_STATE.yaml` in a manuscript
  directory; `--example` drops a fully-populated reference instead.
- `scriptorium validate` — JSON Schema validation of a
  `MANUSCRIPT_STATE.yaml` against `schemas/manuscript-state.schema.json`.
- `scriptorium prompt-pack` — bundle all skills into a single
  platform-neutral markdown prompt pack for use with non-Claude agents.
- `scriptorium list` — list bundled skills with one-line summaries.
- `scriptorium trace` — extract skill invocations from Claude Code
  transcripts as structured records conforming to
  `schemas/trace.schema.json`. Supports three consent tiers
  (`structured-only`, `output-text`, `manuscript-chunk`) and filters by
  skill, project, and time range. Useful for self-inspection and (later)
  eval-loop work. **No transcript content leaves the local machine** —
  the subcommand only writes to stdout or to a file you choose.

#### Schemas

- `schemas/manuscript-state.schema.json` — JSON Schema Draft 2020-12 for
  `MANUSCRIPT_STATE.yaml`, the single source of editorial truth every
  skill reads. Covers project metadata, document phase, core claims,
  known weaknesses, audience, tone, terminology, and source-format hints.
- `schemas/trace.schema.json` — JSON Schema Draft 2020-12 for trace
  records. Uses conditional `if`/`then` subschemas to enforce that
  `structured-only` traces cannot contain skill output text or manuscript
  chunks, and `output-text` traces cannot contain manuscript chunks.

#### Knowledge layer

Curated, peer-reviewed evidence base under `knowledge/`. Visible to the
agent at skill-runtime; powers the citations in each skill's grounding.
v0.1.0.dev0 ships:

- `knowledge/citations/` — citation-accuracy evidence (drives
  `citation-audit`).
- `knowledge/peer-review/` — peer-review reliability and review-quality
  literature (drives `reviewer-simulation`).
- `knowledge/scientific-writing/`, `knowledge/editing/`,
  `knowledge/critique-techniques/`, `knowledge/grants/`,
  `knowledge/prior-art/`, `knowledge/reproducibility/` — supporting
  evidence for the leaf skills.
- `knowledge/author-roles/` — career-stage behavioral evidence and EAL
  academic-writing literature; supports future personalization skills.

A Quarto-based build pipeline (via [quartobot](https://github.com/seandavi/quartobot))
resolves `@pmid:` / `@doi:` cite keys in `knowledge/**/*.qmd` before
citeproc renders the docs site.

#### Documentation

- Astro/Starlight documentation site under `docs/` with concept pages
  (skills, schema, CLI vs MCP tradeoffs, trace schema, etc.).
- `DESIGN.md` — design philosophy, scope, and roadmap.
- `INSTALL.md` — install paths for Claude Code, other agents, and manual
  use.
- `CONTRIBUTING.md` — contribution guide.
- Per-skill `README.md` files documenting inputs, outputs, and grounding.

#### Examples and templates

- `templates/MANUSCRIPT_STATE.yaml` — minimal starter scaffold (what
  `scriptorium init` drops).
- `templates/MANUSCRIPT_STATE.example.yaml` — fully populated reference
  manuscript exercising every field in the schema (what `scriptorium
  init --example` drops).

#### Companion tools (external, recommended)

Not bundled; useful neighbors:

- [Semantic Scholar MCP](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)
  and [PubMed MCP](https://github.com/JackKuo666/PubMed-MCP-Server) for
  bibliographic lookup during citation audit.
- [quartobot](https://github.com/seandavi/quartobot) for Quarto-based
  scholarly writing.

### Infrastructure

- `pyproject.toml` with hatchling build, `force-include` of `schemas/`,
  `templates/`, `skills/`, and `.claude-plugin/` into the wheel so the
  CLI can locate them via `importlib.resources`.
- CI on every PR: ruff (lint + format), pyrefly + mypy (typecheck),
  pytest on Python 3.10–3.13, yamllint, markdownlint, JSON Schema
  validation of example state files, full docs build.
- GitHub Pages deploy workflow for the docs site.

### Licensing

Dual-licensed by category:

- Code (`src/`, tests, schemas, scripts, configuration): [MIT](LICENSE).
- Documentation and knowledge layer (`docs/`, `knowledge/`, top-level
  prose, per-skill `README.md`): [CC BY 4.0](LICENSE-DOCS).

### Known limitations of v0.1.0.dev0

- No orchestrator — skills are invoked one at a time by the user.
- No drafting skills — generation is out of scope at this layer.
- No Codex / Gemini / Hermes adapters beyond the platform-neutral
  prompt-pack export.
- No persona / authorial-voice personalization in-band (the
  `knowledge/author-roles/` evidence base is in place, but the
  personalization skills themselves are not).
- The `trace` subcommand captures Claude Code transcript structure only;
  thinking-block text is not persisted to the transcript by Claude Code,
  so it cannot be recovered.

[Unreleased]: https://github.com/seandavi/scriptorium/compare/v0.1.0.dev0...HEAD
[0.1.0.dev0]: https://github.com/seandavi/scriptorium/releases/tag/v0.1.0.dev0
