# INSTALL

Three install paths depending on the agent you use.

## Claude Code (recommended)

Scriptorium ships as a Claude Code plugin. Two ways to install:

### Live-linked (personal / development use)

```bash
git clone https://github.com/seandavi/scriptorium ~/Documents/git/scriptorium
cd ~/Documents/git/scriptorium
./scripts/dev-link.sh
```

This symlinks the repo into `~/.claude/plugins/scriptorium/`. Edits
to the source propagate immediately. Best for the maintainer or
anyone iterating on skills.

### Copy-installed (clean / shared use)

```bash
git clone https://github.com/seandavi/scriptorium /tmp/scriptorium
cd /tmp/scriptorium
./scripts/install-claude.sh
```

This copies the plugin into `~/.claude/plugins/scriptorium/`. Updates
require re-running the install script. Cleaner for users who don't
plan to edit the skills.

### Verifying

Restart Claude Code, then in any session:

```
/help
```

You should see entries like `scriptorium:citation-audit`,
`scriptorium:reviewer-simulation`, `scriptorium:argumentative-flow`.

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
./scripts/prompt-pack.py > scriptorium-prompts.md
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
- **Prompt-pack path:** Python 3.10+ to run `prompt-pack.py` (or just
  read the individual `prompt.md` files directly with no tooling).
- **State validation:** Python 3.10+ with `jsonschema` and `pyyaml`
  if you want `scripts/validate-state.py` to lint your
  `MANUSCRIPT_STATE.yaml`. Install with `uv tool install jsonschema pyyaml`.

## Uninstall

```bash
rm -rf ~/.claude/plugins/scriptorium
```

For the live-linked install, this removes the symlink only; the source
repo is untouched.
