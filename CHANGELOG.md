# Changelog

All notable changes to scriptorium are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the project uses [PEP 440](https://peps.python.org/pep-0440/) /
[Semantic Versioning](https://semver.org/) for version numbers. Pre-1.0
releases are exploratory: the shape of skills, CLI surface, and shared
state schema may change between versions.

## [Unreleased]

### Added

- `scriptorium:venue-fit` skill (v0.2). Tiered venue
  recommendation (`Likely fit` / `Stretch` / `Probably
  premature`) with per-axis fit reasoning across scope,
  audience, methodological, novelty, significance, and
  open-access/cost/indexing (when constraints are declared).
  Handles three author states — decided (`target_venue` set,
  assesses + offers alternatives), considering
  (`candidate_venues` non-empty, tiers each + suggests
  additions), undecided (open recommendation, may write back to
  `candidate_venues` with explicit consent). Includes opt-in
  preprint mode that surfaces server recommendations
  (bioRxiv/medRxiv/arXiv/ChemRxiv/SSRN/OSF) and a strategic-
  choice sub-section on pre vs post-publication peer review
  (PCI, Review Commons, F1000Research, eLife's post-2022
  reviewed-preprint model). Predatory-venue refusal is
  load-bearing — the output always includes a `## Predatory
  signals detected` section whether or not flags fired (silence
  is indistinguishable from "didn't check"); per-journal
  judgments only, never per-publisher; defers to authoritative
  human-curated sources (Think.Check.Submit, DOAJ, OASPA,
  Cabell's, COPE). Optional bias-managed pub-history
  calibration — history shifts which tier candidates fall into,
  never sources the recommendation list. Outputs qualitative
  tiers only (no per-venue acceptance probabilities; Bornmann
  κ ≈ 0.17 makes that indefensible). Closes #82.

- Three new knowledge notes anchor the skill:
  `knowledge/peer-review/venue-selection.md` (multi-axis
  journal-fit literature: Misra & Agarwal 2017, Solomon & Björk
  2012, Calcagno et al. 2012 on submission trajectories),
  `knowledge/peer-review/predatory-publishing.md` (Beall's
  history, Cabell's, Think.Check.Submit, per-journal-not-per-
  publisher principle with MDPI and Hindawi-Wiley case studies),
  and `knowledge/peer-review/preprint-landscape.md` (preprint
  ecosystem, pre/post-pub review platforms, funder requirements
  driving preprint adoption).

- `MANUSCRIPT_STATE.yaml` schema: new
  `project.candidate_venues` field (array of strings, optional).
  Models the actual author workflow — many authors draft before
  deciding on a venue. Empty `target_venue` + empty
  `candidate_venues` = undecided; populated `candidate_venues`
  alone = considering; populated `target_venue` = decided.
  Backward-compatible with existing `target_venue` consumers
  (`desk-rejection-risk` etc.); `init` updated to elicit the
  right field based on author state, with explicit support for
  "drafting before deciding" as a first-class workflow rather
  than a missing step.

- New convention note `knowledge/conventions/declared-work-scope.md`
  documenting scriptorium's project-wide scope: *we operate on prose
  the author has written or scaffolding the author has declared; we
  do not produce prose from blankness.* Grounded in Hayes' 2012
  writing-process model (proposer / translator / transcriber /
  evaluator — scriptorium occupies the translator and evaluator
  roles, never the proposer), the AI-writing-failure-modes literature
  (hallucinated citations and voice loss are blank-slate generation
  failures the scope structurally defends against), and the existing
  end-to-end-generation survey (Sakana AI Scientist as the negative
  exemplar, GeneAgent's verify-before-emit pattern as the positive
  one). The convention sits alongside `guidance-level.md` as a
  sister structural commitment; alignment across docs and intro
  skills is tracked in #80.

- `scriptorium:desk-rejection-risk` skill. Author-side pre-submission
  audit that flags triggers likely to result in desk rejection before
  peer review: scope/audience mismatch, format and length issues,
  missing or weak required sections, weak significance framing, and
  presentation patterns editors triage on. Outputs a structured
  markdown report with a qualitative risk band
  (`low / moderate / high`) and per-category severity flags;
  `cannot-assess` is a first-class flag so silence on a category
  never reads as "no risk there". The skill refuses to run without
  `project.target_venue` — desk rejection is venue-conditional and a
  generic audit produces platitudes. Grounded in
  `knowledge/peer-review/editorial-decision-making.md` (70–90%
  desk-rejection rates at top journals; Bornmann's
  inter-reviewer-agreement κ ≈ 0.17 motivating why editorial
  discretion at triage is load-bearing),
  `knowledge/scientific-writing/significance-positioning.md` (Day &
  Gastel pattern; Lin et al. 2022 *PNAS* novel-plus-conventional
  finding; NIH Simplified Review Framework Factor 1), and
  `knowledge/peer-review/common-critiques-taxonomy.md` (Bordage 2001
  *Acad Med* top-10 reject reasons as the editor-detectable subset).
  Same author-side-only, ICMJE/NIH/Elsevier/Nature-policy posture as
  `reviewer-simulation`; pairs with it (`desk-rejection-risk` first
  to clear the desk; `reviewer-simulation` second to pressure-test
  the science). Same `meta.guidance_level` framing adaptation as the
  other conversation-bearing skills; structured output unchanged
  across levels. Mirrored in the platform-neutral `prompt.md`.

- `scriptorium:terminology-normalization` (new v0.3 skill) detects
  terminology drift across the manuscript and enforces the
  `terminology.preferred` / `terminology.forbidden` /
  `terminology.synonyms` lists declared in `MANUSCRIPT_STATE.yaml`.
  Reports inconsistencies with exact occurrence locations and
  suggests concrete one-pass normalizations. Categorised as
  **normalization** in DESIGN.md's taxonomy — the skill *may*
  surface concrete edits but does **not** auto-apply them; the
  author applies the edits or invokes a follow-up. Operational
  protocol reads `bibliography.paths` files BEFORE flagging tokens,
  so cited author names and paper titles are never false-positively
  flagged as drift (the load-bearing failure mode named in the
  issue spec). Inflection differences (cell/cells, gene/genes) are
  ignored by default; quoted contexts and term-as-subject passages
  are excluded from forbidden-term enforcement. Pairs with
  `argumentative-flow` as the first verification pass that a
  transformation preserved declared terminology. Grounded in
  `knowledge/critique-techniques/internal-consistency.md` (drift as
  an internal-consistency failure; surface candidate-synonym
  clusters as questions, not decisions) and
  `knowledge/scientific-writing/style-guides.md` (preferred-term
  enforcement as a venue-dependent style-guide function — project
  state, not the skill, decides what's preferred). Same guidance
  mirrored in the platform-neutral `prompt.md`. Closes #74.

- `scriptorium:citation-audit` now documents an **Optional tooling:
  `quartobot resolve`** section. When
  [quartobot](https://github.com/seandavi/quartobot) is on PATH, it
  resolves persistent-ID cite keys (`@pmid:`, `@doi:`) to canonical
  CSL JSON via NCBI E-utilities / Crossref. The note records the
  observed Paperpile-shaped bibliography pattern: title/author search
  first to identify each key, then `quartobot resolve` to attach
  canonical PMIDs and DOIs. The hard rules (no invented persistent
  IDs; CSL metadata is not full-text verification) still apply. Same
  guidance mirrored in the platform-neutral `prompt.md`.

### Changed

- `scriptorium:argumentative-flow` now performs an **active
  ESL-aware preservation check** for hedging and stance markers.
  Previously the skill listed "do not smooth out ESL hedging" as a
  passive non-goal; the v0.2 enhancement promotes it to an active
  inventory step in the operational protocol (alongside cite keys,
  numbers, and declared terminology) and an explicit sub-section in
  the preservation report enumerating hedges retained verbatim,
  modified (with a logical-coherence justification), or dropped.
  Hedging joins citations / statistics / declared terminology as a
  fourth preserved category in the hard preservation contract. The
  guidance-level interaction is load-bearing: at `full` the
  preservation report surfaces in one or two sentences that
  ESL-aware preservation ran (citing Swales/Hyland); at
  `terse`/`standard` the audit fires silently and the table
  speaks for itself — no lecturing. Grounded in
  `knowledge/scientific-writing/esl-writers-swales-hyland.md`. Same
  logic mirrored in `prompt.md` for the platform-neutral path.
  Closes #75.

- `scriptorium:tour` and `scriptorium:explain` now make the
  evidence-base posture an explicit, visible part of their output —
  not a footnote. Tour's turn-1 paragraph names that each skill
  grounds in published research synthesised under `knowledge/`,
  with the project's credibility model stated plainly; the
  manuscript-drafter walk-through in turn 2 names the load-bearing
  papers behind each leaf skill (Greenberg 2009 *BMJ* for
  citation-distortion, Bornmann's inter-reviewer agreement κ ≈ 0.17
  for the multi-lens reviewer design, Gopen & Swan reader-expectation
  theory for argumentative-flow). Explain's system-overview template
  gains an `## Evidence base` section; the per-skill template's
  `## How it's grounded` section now leads with "this skill grounds
  in published research — behaviours trace back to papers, not LLM
  intuition alone" and names anchor citations where they exist.
  `knowledge/README.md` added to explain's default `Sources` list.
  Same framing mirrored in both `prompt.md` files for the
  platform-neutral path.

- Plugin manifest (`.claude-plugin/plugin.json`) and the
  marketplace entry (`.claude-plugin/marketplace.json`) no longer
  declare a `version` field. Per the Claude Code plugin docs, while
  scriptorium is actively pre-1.0, omitting `version` lets the
  marketplace mechanism treat every commit on `main` as a new
  version (SHA-based) — so `/plugin update scriptorium@scriptorium`
  picks up changes without requiring a manual version bump. Two new
  regression tests in `tests/test_marketplace.py` keep both files
  in sync; update them deliberately when cutting a real release.

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

- `scriptorium:tour` skill. Conversational onboarding for new
  users: three or four turns, greets, asks what the user is
  working on, walks them through the relevant subset of
  scriptorium, shows a concrete `MANUSCRIPT_STATE.yaml` excerpt,
  ends with one concrete next command (usually
  `/scriptorium:init <dir>`). Strictly read-only; never
  auto-invokes another skill. Designed as the single entry point
  to point new users at instead of linking them to documentation.
  README.md and INSTALL.md updated to surface
  `/scriptorium:tour` as the recommended first step after install.

- `scriptorium:explain` skill. Read-only meta-skill that
  synthesises a one-screenful overview of scriptorium (no arg), a
  named skill (`/scriptorium:explain citation-audit`), a
  `MANUSCRIPT_STATE.yaml` field
  (`/scriptorium:explain meta.guidance_level`), or a knowledge note
  by slug. Reads the plugin tree only; consumes no manuscript
  content. `tour` and `explain` are complementary — `tour` is
  interactive and ends with a next move; `explain` is a reference
  lookup. Users at the `full` guidance level are nudged toward
  `explain` from the leaf skills.

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
