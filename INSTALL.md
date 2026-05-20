# INSTALL

Several install paths depending on the agent you use.

## Claude Code (recommended)

Scriptorium ships as a Claude Code plugin via a self-hosted plugin
marketplace at `seandavi/scriptorium`. Pick one of three paths:

Scriptorium is pre-release (`0.1.0.dev0`). The marketplace install
path uses Claude Code's built-in plugin system and needs no Python.
The CLI install paths go through a source checkout. A PyPI
publication will land at v0.1 release.

### Plugin marketplace from GitHub (easiest, no Python required)

Inside Claude Code:

```text
/plugin marketplace add seandavi/scriptorium
/plugin install scriptorium@scriptorium
```

The `seandavi/scriptorium` argument is the `owner/repo` shorthand
for <https://github.com/seandavi/scriptorium>. Claude Code clones
the repo to its plugin cache, reads `.claude-plugin/marketplace.json`,
and installs the `scriptorium` plugin from it. The skills appear as
`scriptorium:init`, `scriptorium:citation-audit`, etc.

To pin to a specific tag or commit, append `@ref` to the shorthand:

```text
/plugin marketplace add seandavi/scriptorium@v0.1.0
```

The non-interactive equivalent (from a shell) is:

```bash
claude plugin marketplace add seandavi/scriptorium
claude plugin install scriptorium@scriptorium
```

Updates: `/plugin marketplace update scriptorium` refreshes the
marketplace; `/plugin update scriptorium@scriptorium` updates the
installed plugin. Uninstall: `/plugin uninstall scriptorium@scriptorium`.

This path does not install the `scriptorium` Python CLI. If you also
want the CLI (for `scriptorium validate`, `scriptorium init`,
`scriptorium trace`, `scriptorium prompt-pack`), combine this path
with `uv pip install agentic-scriptorium` once v0.1 publishes, or
use one of the CLI install paths below.

### Live-linked (personal / development use)

```bash
git clone https://github.com/seandavi/scriptorium ~/Documents/git/scriptorium
cd ~/Documents/git/scriptorium
uv pip install -e .
scriptorium install --mode dev-link
```

This symlinks the source repo into `~/.claude/plugins/scriptorium/`.
Edits to the source propagate immediately. Best for the maintainer
or anyone iterating on skills. Skips the marketplace mechanism, so
`/plugin update` will not touch this install — pulling the repo
updates the plugin directly.

### Copy-installed (clean / shared use, no marketplace)

```bash
git clone https://github.com/seandavi/scriptorium /tmp/scriptorium
cd /tmp/scriptorium
uv pip install .
scriptorium install
```

This copies the bundled plugin into `~/.claude/plugins/scriptorium/`.
Updates require re-running `scriptorium install`. Cleaner for users
who want the Python CLI but not the marketplace mechanism. Once v0.1
publishes to PyPI, the clone step will become optional
(`uv pip install agentic-scriptorium`, then `scriptorium install`).

### Verifying

Restart Claude Code, then in any session:

```text
/help
```

You should see entries like `scriptorium:tour`, `scriptorium:init`,
`scriptorium:citation-audit`, `scriptorium:reviewer-simulation`,
`scriptorium:argumentative-flow`, `scriptorium:explain`.

Then run:

```text
/scriptorium:tour
```

A short three-or-four-turn walk-through that orients you to
scriptorium and ends with one concrete next command. No file
writes, no skill invocation. The recommended first step for any
new user.

## Other agents (Codex, Gemini, Hermes, ChatGPT, …)

Each skill ships with a platform-neutral `prompt.md` you can paste
into any LLM directly. Three ways to use this:

### Manual single-skill use

```bash
cat skills/citation-audit/prompt.md | pbcopy
# Paste into your agent of choice with the manuscript text + MANUSCRIPT_STATE.yaml
```

### Bundle all skills into a prompt pack

```bash
scriptorium prompt-pack -o scriptorium-prompts.md
```

Produces a single markdown document containing all skills as separate
prompts, with clear delimiters. Drop the whole file into your agent's
context, then invoke skills by name.

### Per-platform integration

Platform-specific adapters are not in v0.1. If you write one for
Codex / Gemini / Hermes / etc., a PR is welcome.

## Without any agent — manual use

Every skill's `prompt.md` is human-readable and can be used as a
checklist. The skills double as editorial guidance.

## Requirements

- **A manuscript or scaffolding to work on.** Scriptorium operates
  on declared work — prose you've written or state you've committed
  to in `MANUSCRIPT_STATE.yaml`. It does not produce prose from
  blankness; pre-draft ideation and "help me figure out what to
  study" sit outside its scope (see
  [`knowledge/conventions/declared-work-scope.md`](knowledge/conventions/declared-work-scope.md)).
- **Claude Code path:** Claude Code installed and on PATH.
- **CLI path:** Python 3.10+. Install with `uv pip install -e .` from
  a source checkout (or `uv pip install agentic-scriptorium` once
  v0.1 is published). The CLI's dependencies (`click`, `pyyaml`,
  `jsonschema`) come along automatically.
- **Manual / no-agent path:** No tooling — the `prompt.md` files
  under `skills/` are human-readable.

## Uninstall

For a marketplace install:

```text
/plugin uninstall scriptorium@scriptorium
/plugin marketplace remove scriptorium
```

For a CLI install (dev-link or copy):

```bash
rm -rf ~/.claude/plugins/scriptorium
uv pip uninstall agentic-scriptorium  # if you no longer want the CLI either
```

For the live-linked install, removing the plugin directory removes
the symlink only; the source repo is untouched.
