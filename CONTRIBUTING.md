# Contributing to scriptorium

Thanks for considering a contribution. This file covers the workflow, code
quality bar, and the conventions that keep the project coherent.

## TL;DR

```bash
git clone https://github.com/seandavi/scriptorium
cd scriptorium
uv sync --extra dev
pre-commit install
```

That's it. From there, work happens through issues and pull requests.

## Workflow

All non-trivial changes go through a GitHub issue and a pull request, even
if you have direct push access. Two reasons:

1. **Traceability.** The issue captures the *why*; the PR captures the
   *what*. Together they document the project's design history.
2. **Copilot review.** Every PR gets an automated review from Copilot
   before merge. Catches the cheap stuff before a human looks.

The standard cycle:

```
file issue → branch from main → commit → open PR → request Copilot → merge
```

Branch naming: `topic-shortname` (e.g. `citation-audit-skill`, `schema-credit-field`).
PR titles match the issue title; PR body includes "Closes #N".

## Code quality

The project uses, in roughly this order of importance:

- **ruff** for linting and formatting (one tool, both jobs).
- **pyrefly** as the primary type checker (Rust-based, fast).
- **mypy** as a secondary type checker for edge cases pyrefly doesn't
  yet handle. Both run in CI; both must pass.
- **yamllint** on all YAML files (including `MANUSCRIPT_STATE.yaml`
  examples).
- **markdownlint** on top-level markdown. Knowledge-layer docs
  (`knowledge/`) are excluded because they use academic patterns
  (long lines, footnote-style references) markdownlint flags as
  problems.
- **pytest** for tests. Coverage is reported but not strictly enforced
  at v0.1.

The pre-commit config (`.pre-commit-config.yaml`) runs all of the above
locally before each commit. Installing it (`pre-commit install`) is
strongly recommended.

## Skill contributions

Skills live under `skills/<skill-name>/` and ship with:

- `SKILL.md` — Claude Code format with frontmatter (`name`, `description`).
- `prompt.md` — platform-neutral prompt body (no Claude-specific syntax).
- `manifest.yaml` — declares supported platforms, required tools, and
  knowledge-layer dependencies.
- `README.md` — human-facing skill documentation.
- `examples/` — input/output examples.

**Every skill must declare its grounding in the knowledge layer.** The
`README.md` includes a "Grounding" section listing the knowledge docs the
skill draws on (e.g. `[[citation-claim-alignment]]`, `[[reader-expectation-approach]]`).
This keeps skill design accountable to evidence rather than vibes.

See `DESIGN.md` for the full design philosophy and what *not* to do.

## Knowledge layer contributions

`knowledge/` is the evidence base scriptorium's skills ground in. New
knowledge documents follow the template at the top of every existing
doc: Synthesis, Evidence and frameworks, How this informs scriptorium,
Implementation priority, Open questions, References.

**Citation requirements:** real DOIs, PMIDs, ISBNs, or arXiv IDs.
Never fabricate. Mark unverifiable items as `[TODO verify]`.

The `Implementation priority` section is load-bearing — it states
whether a finding becomes a skill (and if so, in what phase) or
remains framing-only context.

## Skill citation discipline

Scriptorium is **citation-resolver-agnostic**. Manuscripts authored in
BibTeX, CSL-JSON, Pandoc-style cite keys, raw DOI-as-URL, or any other
system all work — the skills operate on the resolved citation set, not
on a particular resolver's encoding.

That has two consequences for skill authors:

1. **In skill bodies, cite external work using plain markdown.** Use
   `[Greenberg 2009 BMJ](https://doi.org/10.1136/bmj.b2680)` or
   `DOI: [10.1136/bmj.b2680](https://doi.org/10.1136/bmj.b2680)` —
   forms that render correctly anywhere a Markdown file is read
   (GitHub, Starlight, Claude Code, plain editors). Do **not** use
   manubot / quartobot cite-key syntax (`@doi:...`, `@pmid:...`,
   `[@doi:...]`) in `SKILL.md`, `prompt.md`, or skill `README.md` —
   those formats require a specific build pipeline to resolve, and
   skills are meant to load anywhere a plain Markdown reader can read
   them.

2. **Internal wiki-links stay.** `[[knowledge-doc-name]]` references
   into the `knowledge/` tree are scriptorium-internal cross-links,
   not citations. They are not affected by this discipline.

Knowledge-layer documents (`knowledge/**/*.md`, `knowledge/**/*.qmd`)
are scriptorium-internal evidence base, not skill bodies, and **may**
use manubot / quartobot cite keys — the docs site has a quartobot
preprocess step (see the *Docs site* section above) that resolves
those keys at build time. The constraint above applies specifically
to skill bodies that ship outside the docs build.

Rationale: scriptorium's value proposition is that any author with
any toolchain can adopt it. Tying skill prose to a particular
resolver's syntax silently couples scriptorium to that resolver and
breaks the promise.

## Filing issues

For **new skill proposals**, use the *Skill proposal* issue template
(GitHub will surface it when you open a new issue). The template
enforces grounding — every proposed skill must either cite existing
`knowledge/` notes or propose new ones with a summary of what they
would synthesise. Proposals without grounding get labelled
`needs-grounding` and held until the evidence base catches up.

For everything else (bugs, infrastructure, schema changes, knowledge
additions), open a blank issue and label appropriately.

Useful labels:

- `infrastructure` — repo setup, tooling, CI, packaging.
- `skill` — proposed new skill or change to existing one (the
  template applies this automatically).
- `needs-grounding` — skill proposal whose knowledge notes don't
  yet exist; held until they do.
- `knowledge-layer` — research-doc additions or revisions.
- `schema` — changes to `manuscript-state.schema.json` or other schemas.
- `documentation` — docs site, READMEs, design docs.
- `enhancement` — feature requests.
- `bug` — broken behavior.
- `v0.2`, `v0.3`, `v0.4` — roadmap targeting (milestones cover this too).

Filing a "documentation idea" issue is encouraged whenever you notice
a gap during implementation. Documentation debt compounds.

## Docs site

The Astro/Starlight docs site lives under `docs/`. It pulls top-level
prose (`README.md`, `DESIGN.md`, `docs/roadmap.md`) and the entire
`knowledge/` tree into the site at build time, so most contributions
don't need to touch the site directly — edit the source, rerun
`just preprocess`, and the site updates.

The workflow:

```bash
cd docs
just install       # one-time: npm install (~30s)
just dev           # local dev server with hot reload
just build         # production build (also runs in CI)
just clean         # blow away node_modules + generated content
```

`just preprocess` does four things: (1) copies `DESIGN.md` and
`docs/roadmap.md` into the site; (2) mirrors `knowledge/*.md` under
`concepts/knowledge/`, rewriting `[[wikilinks]]` to Starlight URLs;
(3) renders any `knowledge/*.qmd` files via the [quartobot][quartobot]
pre-render hook (resolves `@pmid:` / `@doi:` cite keys to CSL JSON
through manubot) followed by `quarto render` (citeproc); (4) renders
any `.qmd` files under `docs/qmd/` via Quarto. Generated content —
`references.json` and Quarto's build dirs — is gitignored; the source
of truth stays at the repo root.

Requirements for docs work: Node 22+, npm, `uv` (used by the preprocess
script + to install quartobot), and `just` (1.x). Quarto and
[quartobot][quartobot] are required if you touch any `.qmd` source files
(one knowledge doc, `knowledge/citations/citation-accuracy-evidence.qmd`,
uses the pipeline today). The preprocess script errors out cleanly when
they are needed but missing:

```bash
# Quarto: see https://quarto.org/docs/get-started/
uv tool install quartobot
```

[quartobot]: https://github.com/quartobot/quartobot

The docs site builds in CI on every PR via the `docs-build` job and
deploys to GitHub Pages on every push to `main` via the `docs-deploy`
workflow.

### Enabling GitHub Pages (one-time, repo-admin)

The deploy workflow assumes Pages is enabled with **Source: GitHub Actions**.
To enable: Settings → Pages → Build and deployment → Source → "GitHub
Actions". Once enabled, every push to `main` deploys to
`https://seandavi.github.io/scriptorium/` within ~2 minutes.

## License

The project is dual-licensed by category:

- **Code** (everything under `src/`, tests, schemas, scripts,
  configuration) — [MIT](LICENSE).
- **Prose** (the `docs/` site, the `knowledge/` evidence base, the
  top-level `.md` files, per-skill `README.md`s) — [CC BY 4.0](LICENSE-DOCS).

By contributing code you agree it is released under the MIT license;
by contributing prose you agree it is released under CC BY 4.0.
