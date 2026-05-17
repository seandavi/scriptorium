---
title: Install
description: Install scriptorium for use with Claude Code, other agents, or no agent at all.
sidebar:
  order: 10
---

Three install paths depending on the agent you use.

## Claude Code (recommended)

Scriptorium ships as a Claude Code plugin. Two ways to install:

### Live-linked (personal / development use)

```bash
git clone https://github.com/seandavi/scriptorium ~/Documents/git/scriptorium
cd ~/Documents/git/scriptorium
uv sync
uv run scriptorium install --mode dev-link
```

This symlinks the source repo into `~/.claude/plugins/scriptorium/`. Edits to the source propagate immediately. Best for the maintainer or anyone iterating on skills.

### Copy-installed (clean / shared use)

```bash
uv tool install agentic-scriptorium       # once published to PyPI
scriptorium install --mode copy
```

This copies the plugin into `~/.claude/plugins/scriptorium/`. Updates require re-running the install command. Cleaner for users who don't plan to edit the skills.

### Verifying

Restart Claude Code, then in any session:

```text
/help
```

You should see entries like `scriptorium:citation-audit`, `scriptorium:reviewer-simulation`, `scriptorium:argumentative-flow` once the first skill PRs land.

## Other agents (Codex, Gemini, Hermes, ChatGPT, …)

Each skill ships with a platform-neutral `prompt.md` you can paste into any LLM directly. Bundle all skills into one prompt pack:

```bash
scriptorium prompt-pack --output scriptorium-prompts.md
```

Drop the resulting markdown into your agent's context, then invoke skills by name.

## Without any agent — manual use

Every skill's `prompt.md` is human-readable and can be used as a checklist. The skills double as editorial guidance.

## Requirements

- **Claude Code path:** Claude Code installed and on PATH.
- **Prompt-pack path:** Python 3.10+ to run the CLI (or just read the individual `prompt.md` files directly with no tooling).
- **State validation:** the CLI bundles `jsonschema` and `pyyaml` for `scriptorium validate`.

## Uninstall

```bash
rm -rf ~/.claude/plugins/scriptorium
```

For the live-linked install, this removes the symlink only; the source repo is untouched.
