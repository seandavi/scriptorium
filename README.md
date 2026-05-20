# scriptorium

> Single-responsibility AI skills that work on prose the author has
> written. Each skill reads a shared editorial state file and is
> grounded in a curated, peer-reviewed evidence base.

Scriptorium is a collection of focused AI skills — citation audit,
reviewer simulation, argumentative-flow analysis, terminology
normalization, page-limit compression, and ten more — that coordinate
around a single editorial-state file
([`MANUSCRIPT_STATE.yaml`](schemas/manuscript-state.schema.json)). It
is built for authors revising their own manuscripts and grants who
want structured, anchored critique on prose they have already
written.

**Documentation site:** <https://seandavi.github.io/scriptorium/>
(includes a [worked case study](https://seandavi.github.io/scriptorium/concepts/case-study/)
showing real reviewer-simulation output and a before/after argumentative-flow run).

## What scriptorium does

- **Reads prose the author has already declared** and emits structured,
  anchored findings — one finding per claim, one per section, one
  per figure-text mismatch. No overall quality score. No letter grade.
- **Grounds every design decision in a curated knowledge layer**
  (fifty-plus notes on citation accuracy, hallucination evidence,
  reviewer-archetype research, reporting guidelines, the AI-writing
  failure-mode literature). Each skill's `manifest.yaml` cites the
  knowledge notes its design comes from.
- **Preserves what the author owns.** Critique skills modify nothing.
  Transformation skills operate under an explicit preservation
  contract (citations, statistics, declared terminology, declared
  core claims, hedging style — see [voice preservation](#voice-preservation-the-honest-version)).
- **Refuses to invent.** No skill adds a citation. No skill drafts a
  section from a blank page. The
  [`declared-work-scope`](knowledge/conventions/declared-work-scope.md)
  convention is enforced across every conversation-bearing skill.

## What scriptorium will not do

These are explicit non-goals, grounded in the
[roadmap](docs/roadmap.md#explicit-non-goals) and the knowledge layer.
Naming them up front is the point — a pre-submission tool earns trust
by being concrete about its limits.

- **No blank-slate prose generation.** Scriptorium does not draft
  sections from nothing. The proposer role (Hayes 2012) is the
  author's; scriptorium occupies the translator and evaluator roles.
  See [`declared-work-scope`](knowledge/conventions/declared-work-scope.md).
- **No autonomous reviewing.** `reviewer-simulation` and
  `desk-rejection-risk` are author-side only. Editorial-side use
  violates ICMJE, NIH, and major-publisher peer-review policy, and
  the skills refuse to run on a manuscript the user did not author.
- **No overall writing-quality score.** No letter grade, no
  Flesch-Kincaid, no aggregate number. Those systematically misrate
  scientific prose and would be theater rather than information.
- **No image-forensics or sleuth replacement.** Bik-style figure
  integrity review, tortured-phrase detection, and statistical
  forensics (Carlisle, Statcheck, GRIM, SPRITE) require domain
  experts. Scriptorium is a pre-submission first pass.
- **No reference-manager replacement.** Citation audit works with
  the bibliography Zotero, Mendeley, Paperpile, or BibTeX already
  produced; scriptorium does not manage references itself.
- **No discipline-specific defaults outside biomedical / clinical at
  v0.1–v0.3.** The evidence base is biomedical-coded. Physics,
  CS/ML, mathematics, qualitative social science, and humanities
  defaults need per-discipline knowledge layers that don't exist
  yet — PRs welcome.
- **No native `.docx` round-trip.** Scriptorium operates on
  markdown-converted prose; tracked changes and Word field codes
  are not preserved through the conversion.
- **No skill-degradation defence.** Whether extended AI use atrophies
  the author's underlying skill is plausible but under-evidenced.
  The author retains responsibility for their writing.

## Where scriptorium fits in the writing workflow

The seven lifecycle stages in `MANUSCRIPT_STATE.yaml` (`outline` →
`draft` → `review` → `revision` → `submission` → `post-submission` →
`accepted`) map onto four roles in
[Hayes' 2012 cognitive-process model](knowledge/scientific-writing/hayes-flower-writing-model.md):
**proposer, translator, evaluator, transcriber**. Scriptorium occupies
the *translator* and *evaluator* roles when the author has already
proposed. It does not propose for the author.

| Lifecycle stage | Typical scriptorium skills |
|---|---|
| **`outline`** (proposer phase — author-owned) | `init`, `tour`, `explain`, `venue-fit`. No critique skills — outline-phase prose isn't yet declared. |
| **`draft`** | `citation-audit`, `gap-finder`, `figure-text-alignment`, `reporting-guideline-fit`, `terminology-normalization`, `argumentative-flow` (per section). |
| **`review` · `revision`** | All of the above plus `reviewer-simulation`, `author-contribution-audit`, `reporting-guideline-compliance`. |
| **`submission`** | All of the above plus `desk-rejection-risk`, `compression`. |

The [skill reference](https://seandavi.github.io/scriptorium/reference/skills/)
lists every shipped skill by category and lifecycle stage.

## Voice preservation, the honest version

A common (correct) fear about AI editing tools is that they will
flatten the author's voice. Scriptorium's posture on this is split
into two claims — one that is enforced, one that is not.

**Enforced (the preservation contract).** Transformation skills
(`argumentative-flow`, `compression`) operate under an explicit
preservation contract:

- Every citation key in the source is preserved; none are added.
- Every numerical value, p-value, confidence interval, and unit is
  preserved verbatim.
- Whatever the author declares in `terminology.preferred` /
  `terminology.forbidden` / `terminology.synonyms` is respected.
- The author's hedging strength (over-cautious vs assertive) is
  honoured — any shift is reported as a per-edit note rather than
  absorbed silently.
- Declared `core_claims` are preserved; no claim is added, no
  declared claim is dropped.

Critique skills (`citation-audit`, `reviewer-simulation`,
`gap-finder`, `desk-rejection-risk`, `figure-text-alignment`,
`reporting-guideline-compliance`, `author-contribution-audit`,
`venue-fit`, `reporting-guideline-fit`) rewrite nothing at all.

**Not promised (sentence-level voice preservation).** Scriptorium
does not claim that running a transformation skill leaves your
prose "sounding like you" at the sentence level. The evidence is
the Kobak et al. 2024 lexical-fingerprint work: LLM-edited prose
is detectable at corpus scale, and correcting it at sentence scale
is not reliable. The conservative-edit posture above minimizes the
surface area of changes; it does not promise that nothing about
the author's distinctive voice shifts. See
[`ai-writing-failure-modes`](knowledge/prior-art/ai-writing-failure-modes.md)
for the evidence we're calibrating against.

The defence is structural: the author reviews each per-edit diff
and chooses what to accept.

## Light, standard, full — author chooses

Critique can be paralyzing if it arrives all at once and presents
as authoritative. `meta.guidance_level` in `MANUSCRIPT_STATE.yaml`
lets the author dial in how much framing scriptorium adds around
its work:

- **`terse`** — questions and confirmations only. No prose between
  turns. For authors on their second-or-later project.
- **`standard`** (default) — one-line "why" before non-obvious
  questions. For returning users who appreciate anchoring without
  a lecture.
- **`full`** — upfront orientation, 2–3 sentence rationale before
  each elicited field, end-of-phase recap. For first-time users
  who want to learn the workflow as they go.

The structured output of each skill — the citation-audit table, the
four reviewer-lens sections, the argumentative-flow diff — does not
change with guidance level. What changes is the framing around the
structured work. See
[`guidance-level`](knowledge/conventions/guidance-level.md).

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
<https://github.com/seandavi/scriptorium>. Append `@v0.2.0` or any
ref to pin.)

Once installed, run:

```text
/scriptorium:tour
```

A short conversational walk-through — three or four turns — that
orients you to scriptorium and ends with one concrete next command.
It writes nothing and invokes no other skill; it's the single entry
point we recommend pointing new users at instead of linking them
to documentation.

Updates: `/plugin marketplace update` then
`/plugin update scriptorium@scriptorium`.

If you also want the Python CLI (`scriptorium init`,
`scriptorium validate`, `scriptorium trace`), or you want a
live-linked dev install, see [INSTALL.md](INSTALL.md).

### Other agents (Codex, Gemini, Hermes, ChatGPT, …)

Each skill ships with a platform-neutral `prompt.md` you can paste
into any LLM directly. To get all skills concatenated into a single
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

`MANUSCRIPT_STATE.yaml` is a local file in your repository. It is
not uploaded to scriptorium and is not shared unless you commit it
to a shared branch. Whether to commit it is your call.

A fully-populated reference manuscript lives at
[`templates/MANUSCRIPT_STATE.example.yaml`](templates/MANUSCRIPT_STATE.example.yaml)
(an imaginary biomedical paper that exercises every field in the
schema). Use `scriptorium init --example /tmp/example` to drop a
copy anywhere as a learning aid.

A worked case study showing the full citation-audit /
reviewer-simulation / argumentative-flow run on a realistic
discussion paragraph (constructed for the walk-through, not real)
lives at
[`docs/src/content/docs/concepts/case-study.md`](docs/src/content/docs/concepts/case-study.md).

## What ships today

Fourteen skills across critique, validation, normalization,
transformation, meta, and utility categories. The full list,
organised by category and lifecycle stage, is the
[skills reference page](https://seandavi.github.io/scriptorium/reference/skills/).
A short summary:

- **Critique** — `citation-audit`, `reviewer-simulation`,
  `gap-finder`, `figure-text-alignment`, `desk-rejection-risk`,
  `venue-fit`, `author-contribution-audit`, `reporting-guideline-fit`.
- **Validation** — `reporting-guideline-compliance`.
- **Normalization** — `terminology-normalization`.
- **Transformation** — `argumentative-flow`, `compression`.
- **Meta / utility** — `tour`, `explain`, `init`.

The `scriptorium` CLI exposes six subcommands: `install`, `init`,
`validate`, `prompt-pack`, `list`, and `trace`. See
`scriptorium --help`.

Deliberately *not* shipped (see [DESIGN.md](DESIGN.md) and the
[roadmap](docs/roadmap.md) for build order): the
`manuscript-pipeline` orchestrator (held until the leaves have been
exercised on more real manuscripts); blank-slate drafting skills
(structurally out of scope); Codex/Gemini installer scripts.

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
  documents before citeproc renders them. Used inside the
  scriptorium docs build for the `knowledge/` evidence base; useful
  standalone for any Quarto-based scholarly writing.

These are external projects, not bundled with scriptorium. Install
them separately following each project's own instructions.

## Design principles

The system separates:

- **generation** (write new prose — out of scope at v0.1–v0.3)
- **critique** (assess existing prose; emit structured findings)
- **validation** (check against an external standard)
- **normalization** (enforce declared style and terminology)
- **transformation** (modify prose under a preservation contract)

And prefers:

- inspectable transformations over opaque rewrites
- structured outputs over freeform rambles
- semantic diffs over surface rewrites
- explicit checkpointing over hidden state

See [DESIGN.md](DESIGN.md) for the full design philosophy and the
[roadmap](docs/roadmap.md) for what ships when.

## Status

v0.2 shipped (CHANGELOG: [`[0.2.0]`](CHANGELOG.md#020---2026-05-20)).
Fourteen skills, fifty-plus knowledge notes, the consolidated
`scriptorium` CLI (six subcommands), the shared-state schema, the
trace schema, the Venice example. 114 tests. Pre-1.0 shape: the
skill catalog is growing; CLI surface and schema may still adjust.

## License

Dual-licensed by category:

- **Code** — source under `src/`, tests, schemas, scripts, and
  configuration files — is [MIT](LICENSE).
- **Documentation and knowledge layer** — the `docs/` site, the
  `knowledge/` evidence base, top-level prose files (`README.md`,
  `DESIGN.md`, `INSTALL.md`, `CONTRIBUTING.md`), and per-skill
  `README.md` files — is [CC BY 4.0](LICENSE-DOCS).
