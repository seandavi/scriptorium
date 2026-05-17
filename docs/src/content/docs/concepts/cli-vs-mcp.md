---
title: CLI vs MCP server
description: Why scriptorium ships as a CLI today and where an MCP server fits later.
sidebar:
  order: 20
---

Scriptorium ships as a Python CLI plus a Claude Code plugin. A [Model Context Protocol](https://modelcontextprotocol.io/) server is a plausible alternative — or, more likely, a complement. This page explains the choice and the tradeoffs.

## The two surfaces

### CLI (current default)

- `scriptorium install` / `validate` / `prompt-pack` / `list` / `init` — direct invocation.
- Skills are markdown files under `~/.claude/plugins/scriptorium/`.
- Composes naturally with shell pipelines, git hooks, CI workflows.
- Works in non-Claude environments via per-skill `prompt.md` files (see [`scriptorium prompt-pack`](/reference/cli/)).
- No daemon, no persistent process, no protocol surface.

### MCP server (future)

- Skills and state become MCP resources and tools.
- Any MCP-aware client (Claude Code, Codex, Cursor, Zed, etc.) auto-discovers and uses them.
- Persistent process, localhost network surface.
- The server can hold session state across multiple skill invocations — a natural home for `MANUSCRIPT_STATE.yaml` if it ever grows dynamic.
- Research-tooling integration (PubMed, OpenAlex, Crossref) is a natural MCP-server responsibility — caching, rate-limit awareness, API-key management — that fits awkwardly into per-skill code.

## Tradeoffs

| Concern | CLI | MCP server |
|---|---|---|
| Install complexity | Low | Medium — server lifecycle, process supervision |
| Discovery | Manual or via docs | Automatic by any MCP client |
| Cross-client portability | Via `prompt.md` per skill | Native, protocol-driven |
| Session state | Filesystem only | Possible in the server process |
| Network surface | None | Localhost (or remote, if exposed) |
| Caching for external APIs | Per-skill, or via a package | Natural — sits between client and API |
| Versioning | `pip` / `uv` | Server protocol versions + tool versions |
| Failure modes | Process exit | Hung process, dropped connection, version drift |

The MCP version isn't strictly better — it adds a protocol surface and a process to supervise. The reasons to pay that cost are auto-discovery across clients and a natural home for stateful, API-bound work that doesn't fit into per-skill scripts.

## Direction for each release

### v0.1 — CLI + Claude Code plugin only

The plugin model already gives Claude Code users automatic discovery (`/help` lists `scriptorium:*` skills). Other agents reach scriptorium via the prompt-pack flow, which is good-enough for v0.1 and avoids committing to a protocol surface before there's user pull for it.

### v0.2+ — MCP server complementing the CLI (not replacing)

Plausible scope for an MCP server:

- Host API-fronting tools that benefit from caching and rate limiting — PubMed lookup, Crossref DOI resolution, retraction-check (see [the research-tooling discussion](https://github.com/seandavi/scriptorium/issues/19)).
- Surface bundled skills as MCP tools for clients that aren't Claude Code (Codex, Cursor, Zed). The skill manifests already declare their inputs and grounding; mapping that to MCP tool schemas is mostly mechanical.
- Coordinate cross-skill workflows where one skill's output is another's input — easier to manage in a single process than across CLI invocations.

Markdown skills stay file-based regardless. The MCP server is an *additional* surface, not a replacement for the plugin model.

### Open question for v0.2 planning

Does scriptorium's skill bundle become an MCP-server resource set, or stay primarily a Claude Code plugin with MCP layered underneath? The current bet is "plugin remains primary; MCP layers underneath." That's reversible if cross-client demand turns out higher than expected.

## Related

- [Reference — CLI commands](/reference/cli/) — the surface that exists today.
- [How-to — Install](/how-to/install/) — the plugin install paths.
- [GitHub issue #19](https://github.com/seandavi/scriptorium/issues/19) — the research-tooling discussion that's the most natural fit for an MCP server.
- [GitHub issue #20](https://github.com/seandavi/scriptorium/issues/20) — the canonical tracking issue for this page.
