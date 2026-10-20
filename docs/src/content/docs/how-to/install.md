---
title: Install
description: Install scriptorium for use with Claude Code, other agents, or no agent at all.
sidebar:
  order: 10
---

Several install paths depending on the agent you use.

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

## npx skills (any supported agent)

The [`skills` CLI](https://github.com/vercel-labs/skills) installs scriptorium's skills into the skills directory of Claude Code, Codex, Cursor and the other agents it supports. It needs Node.js (for `npx`) and no Python. If you use Claude Code, the plugin install above is still the recommended path.

Install all skills (the CLI asks which skills and agents you want):

```bash
npx skills add seandavi/scriptorium
```

Install one skill, or a few, with `--skill`. `--list` shows what is available without installing anything:

```bash
npx skills add seandavi/scriptorium --skill citation-audit
npx skills add seandavi/scriptorium --skill init --skill explain --skill tour
npx skills add seandavi/scriptorium --list
```

Pick agents with `-a` (`-a '*'` for every supported agent), and add `-y` to skip the prompts:

```bash
npx skills add seandavi/scriptorium -a claude-code codex -y
```

By default skills go into the current project (for Claude Code, `.claude/skills/`). `-g` installs them for your user instead, so every project sees them:

```bash
npx skills add seandavi/scriptorium -g
```

When you install for more than one agent, the CLI keeps one copy under `.agents/skills/` and symlinks it into each agent's directory. `--copy` writes a separate copy into each agent's directory instead.

Update and remove:

```bash
npx skills update
npx skills remove citation-audit
```

`npx skills list` shows what is installed. The CLI records each skill's source in `skills-lock.json` in the project.

Each skill is installed on its own, without the rest of the repo. `init`, `explain` and `tour` carry the files they read most (the state schema, the example state file, the knowledge-layer README and the two `knowledge/conventions/` notes) under their own `assets/` directory. What the plugin and CLI add on top:

- **The `scriptorium` CLI** — `scriptorium validate`, `scriptorium init` and `scriptorium prompt-pack`. Without it, `init` checks `MANUSCRIPT_STATE.yaml` against its bundled schema in-conversation, which is best-effort; `scriptorium validate` is the authoritative check. Install it with `uv pip install agentic-scriptorium`.
- **The full knowledge layer, locally.** A plugin install or a checkout has every note under `knowledge/` and every skill's `SKILL.md`. A standalone `explain` fetches any note or skill it does not bundle from GitHub `main`, which may be newer than your installed copy, and needs network access to do so.

## Other agents (Codex, Gemini, Hermes, ChatGPT, …)

Each skill ships with a platform-neutral `prompt.md` you can paste into any LLM directly. The CLI's `prompt-pack` subcommand emits these prompts in a shape your agent can use.

### Per-skill files (default)

```bash
scriptorium prompt-pack --output prompts/
```

This writes one `.md` per shipped skill into `prompts/` plus a `README.md` manifest listing each skill, its category, and a one-line description:

```text
prompts/
  README.md
  citation-audit.md
  reviewer-simulation.md
  argumentative-flow.md
  ...
```

Paste the specific prompt you want into your agent's context — most non-Claude-Code users only need one skill at a time, not all of them.

If you'd like the filenames to carry the project namespace (useful when you're dropping skills from multiple sources into the same directory), add `--prefix scriptorium-`:

```bash
scriptorium prompt-pack --prefix scriptorium- --output prompts/
# writes prompts/scriptorium-citation-audit.md, etc.
```

### Single concatenated file

If you want every skill prompt in one document — for archival, for an agent that loads its whole system prompt from a single file, or just to scan everything at once — use `--single-file`:

```bash
scriptorium prompt-pack --single-file --output scriptorium-prompts.md
```

## Without any agent — manual use

Every skill's `prompt.md` is human-readable and can be used as a checklist. The skills double as editorial guidance.

## Requirements

- **Claude Code path:** Claude Code installed and on PATH.
- **npx skills path:** Node.js, for `npx`.
- **Prompt-pack path:** Python 3.10+ to run the CLI (or just read the individual `prompt.md` files directly with no tooling).
- **State validation:** the CLI bundles `jsonschema` and `pyyaml` for `scriptorium validate`.

## Uninstall

```bash
rm -rf ~/.claude/plugins/scriptorium
```

For the live-linked install, this removes the symlink only; the source repo is untouched.
