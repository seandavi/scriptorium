---
title: CLI commands
description: Reference for the `scriptorium` command-line tool.
sidebar:
  order: 10
---

The `scriptorium` CLI exposes five subcommands.

```text
$ scriptorium --help
Usage: scriptorium [OPTIONS] COMMAND [ARGS]...

  Scriptorium: agentic operating system for scholarly writing.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  init         Scaffold a starter MANUSCRIPT_STATE.yaml in a manuscript dir.
  install      Install scriptorium into the Claude Code plugins directory.
  list         List bundled skills with descriptions and grounding refs.
  prompt-pack  Concatenate bundled skill prompts into one platform-neutral file.
  validate     Validate a MANUSCRIPT_STATE.yaml file against the JSON Schema.
```

## `scriptorium install`

Install scriptorium into the Claude Code plugins directory.

```text
Usage: scriptorium install [OPTIONS]

Options:
  --mode [dev-link|copy]  dev-link symlinks the source repo; copy installs
                          from package data. [default: copy]
  --target PATH           Install target (default: ~/.claude/plugins/scriptorium).
  --force                 Overwrite an existing install.
```

Use `--mode dev-link` when working from a clone (`uv sync` + dev-link). Use `--mode copy` when installing from a published wheel.

## `scriptorium validate <path>`

Validate a `MANUSCRIPT_STATE.yaml` file against the JSON Schema (Draft 2020-12). Prints per-field errors and exits non-zero on failure.

```bash
scriptorium validate MANUSCRIPT_STATE.yaml
```

## `scriptorium prompt-pack`

Concatenate all bundled skill prompts into one platform-neutral markdown file. Drop the result into any LLM's context to use scriptorium skills outside Claude Code.

```text
Usage: scriptorium prompt-pack [OPTIONS]

Options:
  -o, --output PATH  Write the prompt pack to a file instead of stdout.
```

## `scriptorium list`

List bundled skills with descriptions and grounding references (the knowledge documents each skill grounds in).

## `scriptorium init <manuscript-dir>`

Scaffold a starter `MANUSCRIPT_STATE.yaml` in a directory. Refuses to overwrite without `--force`.

```text
Usage: scriptorium init [OPTIONS] MANUSCRIPT_DIR

Options:
  --force  Overwrite an existing MANUSCRIPT_STATE.yaml.
```

A conversational counterpart — the `init` *skill* — is planned for v0.2 ([issue #28](https://github.com/seandavi/scriptorium/issues/28)). It walks an author through populating the file rather than copying a template.

## Related

- [`MANUSCRIPT_STATE.yaml` schema](/reference/manuscript-state-schema/) — the JSON Schema the validator enforces.
