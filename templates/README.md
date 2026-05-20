# templates/

Reference and starter material for `MANUSCRIPT_STATE.yaml`, the shared
editorial state file every scriptorium skill reads.

## Files

- **`MANUSCRIPT_STATE.yaml`** — starter template. Sparsely populated,
  with commented-out fields and inline guidance on what each one
  controls. This is what `scriptorium init` drops into a new manuscript
  directory.
- **`MANUSCRIPT_STATE.example.yaml`** — fully-populated worked example
  for an imaginary biomedical manuscript. Every field that the schema
  permits is filled in with realistic content. Use as a reference for
  what each field can hold, not as a template to copy wholesale.

## Using these files

The most common path is to let the CLI scaffold the starter for you:

```bash
scriptorium init /path/to/your/manuscript
```

That drops the starter `MANUSCRIPT_STATE.yaml` into the target directory.
Edit it directly, or use the conversational bootstrap inside Claude Code:

```text
/scriptorium:init
```

To drop a copy of the worked example anywhere as a learning aid:

```bash
scriptorium init --example /tmp/example
```

Validate the result at any time:

```bash
scriptorium validate /path/to/your/manuscript/MANUSCRIPT_STATE.yaml
```

## Schema reference

The authoritative schema lives at
[`schemas/manuscript-state.schema.json`](../schemas/manuscript-state.schema.json).
A field-by-field reference page is rendered at
[`/reference/manuscript-state-schema/`](https://seandavi.github.io/scriptorium/reference/manuscript-state-schema/)
on the documentation site.
