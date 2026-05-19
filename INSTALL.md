# INSTALL

Three install paths depending on the agent you use.

## Claude Code (recommended)

Scriptorium ships as a Claude Code plugin. Two ways to install:

Scriptorium is pre-release (`0.1.0.dev0`). Both install paths
currently go through a source checkout; a PyPI publication will
land at v0.1 release.

### Live-linked (personal / development use)

```bash
git clone https://github.com/seandavi/scriptorium ~/Documents/git/scriptorium
cd ~/Documents/git/scriptorium
uv pip install -e .
scriptorium install --mode dev-link
```

This symlinks the source repo into `~/.claude/plugins/scriptorium/`.
Edits to the source propagate immediately. Best for the maintainer
or anyone iterating on skills.

### Copy-installed (clean / shared use)

```bash
git clone https://github.com/seandavi/scriptorium /tmp/scriptorium
cd /tmp/scriptorium
uv pip install .
scriptorium install
```

This copies the bundled plugin into `~/.claude/plugins/scriptorium/`.
Updates require re-running `scriptorium install`. Cleaner for users
who don't plan to edit the skills. Once v0.1 publishes to PyPI, the
clone step will become optional (`uv pip install agentic-scriptorium`,
then `scriptorium install`).

### Verifying

Restart Claude Code, then in any session:

```
/help
```

You should see entries like `scriptorium:init`,
`scriptorium:citation-audit`, `scriptorium:reviewer-simulation`,
`scriptorium:argumentative-flow`.

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

- **Claude Code path:** Claude Code installed and on PATH.
- **CLI path:** Python 3.10+. Install with `uv pip install -e .` from
  a source checkout (or `uv pip install agentic-scriptorium` once
  v0.1 is published). The CLI's dependencies (`click`, `pyyaml`,
  `jsonschema`) come along automatically.
- **Manual / no-agent path:** No tooling — the `prompt.md` files
  under `skills/` are human-readable.

## Uninstall

```bash
rm -rf ~/.claude/plugins/scriptorium
uv pip uninstall agentic-scriptorium  # if you no longer want the CLI either
```

For the live-linked install, removing the plugin directory removes
the symlink only; the source repo is untouched.
