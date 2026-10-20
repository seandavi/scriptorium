---
title: MANUSCRIPT_STATE.yaml schema
description: The JSON Schema for the shared editorial state file every scriptorium project carries.
sidebar:
  order: 20
---

Every project that uses scriptorium maintains a `MANUSCRIPT_STATE.yaml` file at its root. Every skill reads it. The file is the gravity well that keeps the workflow coherent across sessions and across skills.

## File scope and visibility

`MANUSCRIPT_STATE.yaml` is a *local file in your repository*. It is not uploaded to scriptorium, is not synced to any service, and is not shared with anyone unless you commit it to a shared branch. Whether you commit it at all is your call — a private fork, a private git remote, or `.gitignore`-ing the file are all reasonable choices.

The file exists so every skill can read the same declared state without you re-typing it each time. Skills like `reviewer-simulation` use the calibration fields (`known_weaknesses`, `core_claims`) to *refrain* from flagging items you have already chosen to acknowledge — the fields are inputs to the skill's calibration, not disclosure targets for anyone else.

## Authoritative source

The canonical schema is [`schemas/manuscript-state.schema.json`](https://github.com/seandavi/scriptorium/blob/main/schemas/manuscript-state.schema.json) in the repo. Validate any file against it with:

```bash
scriptorium validate MANUSCRIPT_STATE.yaml
```

## Top-level keys

| Key | Required | Purpose |
|---|---|---|
| `meta` | no | Scriptorium-side preferences, not properties of the manuscript: `guidance_level` (see [Guidance level](/concepts/guidance-level/)) and `overrides` (see [below](#metaoverrides)). |
| `project` | yes | Title, target type (manuscript / grant / review / …), target venue. |
| `document_phase` | yes | Where the document is in its lifecycle: outline → draft → review → revision → submission → post-submission → accepted. |
| `core_claims` | no | What the document is arguing. Critique skills test whether the prose supports each claim; transformation skills preserve them. |
| `known_weaknesses` | no | Limitations the authors have already chosen to acknowledge. Reviewer-simulation will not flag these as fatal. Naming under review — see [note below](#a-note-on-known_weaknesses). |
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

## `meta.overrides`

Guards the author has chosen to override for this project. Each skill
declares its guards in `manifest.yaml`; only `policy` and `scope`
guards can be overridden. [Author authority](/concepts/author-authority/)
explains the guard kinds, the precedence and the "Overrides applied"
line.

```yaml
meta:
  overrides:
    - guard: citation-recommendations
      skills: [citation-audit, gap-finder]
      note: "Name verified papers for unsupported claims; I decide what to cite."
    - guard: outline-phase
      skills: ["*"]
```

`overrides` is an array. Each entry is an object with these keys and
no others:

| Key | Required | Type | Meaning |
|---|---|---|---|
| `guard` | yes | string, kebab-case | A guard id declared under `guards:` in a skill's `manifest.yaml`. |
| `skills` | yes | non-empty array of unique strings | Skill names the override applies to, each kebab-case, or `"*"` for every skill that declares the guard. |
| `note` | no | string | Free text for the author's own record. Skills don't interpret it. |

A per-run answer from the author takes precedence over these entries,
and the skill still states the guard's concern in one line.

Beyond the schema, `scriptorium validate` checks each entry against the
guards the bundled skills declare. It rejects:

- a guard id no bundled skill declares;
- a guard of kind `accuracy`;
- a skill listed in `skills` that does not declare the guard.

## A note on `known_weaknesses`

The field's name is under review. Its *function* is calibration: it records limitations the author has already chosen to acknowledge so that downstream skills (most importantly `reviewer-simulation` and `desk-rejection-risk`) do not surface them as fresh fatal critiques the author would have to defend against. The field is a way of saying *"I know about these; don't make me re-litigate them."*

The current name reads to some authors as adversarial — particularly to first authors who reasonably feel that documenting "weaknesses" of their own paper in a file is the wrong default. The proposed replacement is **`acknowledged_limitations`**, which keeps the calibration semantics and removes the adversarial framing. The rename is tracked in [issue #62](https://github.com/seandavi/scriptorium/issues/62) and is scheduled for a dedicated schema-migration PR (it touches the schema, all templates, ~15 skill files, and a test fixture, so it lands as its own change rather than buried in a documentation PR).

Until the rename ships, both names refer to the same field; the migration PR will add a transitional alias rather than a breaking change.

## Design context

See [Design — the shared-state contract](/concepts/design/) for why this file exists and what skills are required to do with it.
