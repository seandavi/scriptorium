---
title: MANUSCRIPT_STATE.yaml schema
description: The JSON Schema for the shared editorial state file every scriptorium project carries.
sidebar:
  order: 20
---

Every project that uses scriptorium maintains a `MANUSCRIPT_STATE.yaml` file at its root. Every skill reads it. The file is the gravity well that keeps the workflow coherent across sessions and across skills.

## Authoritative source

The canonical schema is [`schemas/manuscript-state.schema.json`](https://github.com/seandavi/scriptorium/blob/main/schemas/manuscript-state.schema.json) in the repo. Validate any file against it with:

```bash
scriptorium validate MANUSCRIPT_STATE.yaml
```

## Top-level keys

| Key | Required | Purpose |
|---|---|---|
| `project` | yes | Title, target type (manuscript / grant / review / …), target venue. |
| `document_phase` | yes | Where the document is in its lifecycle: outline → draft → review → revision → submission → post-submission → accepted. |
| `core_claims` | no | What the document is arguing. Critique skills test whether the prose supports each claim; transformation skills preserve them. |
| `known_weaknesses` | no | Limitations the authors already plan to acknowledge. Reviewer-simulation will not flag these as fatal. |
| `terminology` | no | `preferred` / `forbidden` lists and `synonyms` for normalization passes. |
| `style` | no | `tone[]`, `voice` (active / passive / mixed), `audience`. |
| `constraints` | no | `preserve_citations`, `preserve_statistics`, `avoid_hype`, `max_word_count`. |
| `bibliography` | no | Paths to `.bib` / `.json` / `.yaml` bibliography files and primary `format`. |
| `sections` | no | Optional explicit section manifest for multi-file projects (e.g. Quarto includes). |

## Scaffolding a new file

```bash
scriptorium init my-manuscript/
```

Writes a starter `MANUSCRIPT_STATE.yaml` with all top-level keys present and commented. Edit it to match your project, then `scriptorium validate` it.

## Design context

See [Design — the shared-state contract](/concepts/design/) for why this file exists and what skills are required to do with it.
