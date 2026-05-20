# explain — synthesize a tour of scriptorium

Read-only meta-skill. With no argument it summarises scriptorium
itself; with an argument it drills into a named skill, a
`MANUSCRIPT_STATE.yaml` field, or a knowledge note. Reads the plugin
tree (`skills/`, `schemas/`, `knowledge/`); consumes no manuscript
content.

## Files

- `SKILL.md` — Claude Code skill (with frontmatter, full
  operational protocol, output templates).
- `prompt.md` — platform-neutral version for use with any LLM that
  has access to the plugin tree.
- `manifest.yaml` — machine-readable metadata.

## When to invoke

- `/scriptorium:explain` — whole-system overview.
- `/scriptorium:explain <skill>` — explain that skill.
- `/scriptorium:explain <field>` — explain that
  `MANUSCRIPT_STATE.yaml` field.
- `/scriptorium:explain <note>` — summarise a `knowledge/` note.

A leaf skill running at the `full` guidance level will sometimes
suggest the explain skill before its first invocation in a session
("want a tour of citation-audit before you run it?"). That's the
intended path for new users learning the workflow.

## What it explicitly will not do

- Read or summarise the user's manuscript.
- Auto-invoke another skill after explaining.
- Produce a multi-screen explanation by default.
