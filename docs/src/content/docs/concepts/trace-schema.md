---
title: Trace schema
description: The canonical record format for telemetry and eval data, with tiered consent baked in at the schema level.
sidebar:
  order: 30
---

The trace schema defines what a single record of "this skill ran on this manuscript artifact and the user did these things with the output" looks like. Every telemetry capture surface (transcript-mining, hooks, an eventual submission API) produces records of this shape, so aggregation across surfaces is by construction rather than retrofit.

The schema lives at `schemas/trace.schema.json` in the scriptorium repository and is JSON Schema Draft 2020-12.

## Why a schema first

Without a contract written down, each capture surface encodes its own assumptions, and by the time you want to aggregate across them every record is slightly differently shaped. The schema is the discipline that prevents that drift — the same discipline `MANUSCRIPT_STATE.yaml` enforces for editorial state.

It also forces the privacy story to be explicit. The unpublished research manuscripts these traces describe are sensitive data, and the consent question — "what is the user actually opting into?" — has to be answerable at the record level, not retrofitted later. The schema makes it answerable.

## What a trace record represents

One skill invocation on one manuscript artifact, plus whatever follow-on signal is observable from that capture surface. Concretely:

- **Identity:** when the record was emitted, which scriptorium version emitted it, which schema version it conforms to.
- **Provenance:** which capture surface produced the record (a Claude Code transcript, a hook, an SDK runner, manual).
- **Skill identity:** which skill ran, at what version, on what invocation surface (Claude Code, Gemini CLI, SDK).
- **Model identity:** provider, model name, whether extended thinking was used, whether the thinking text itself is captured.
- **Manuscript metadata:** discipline, target venue tier, section, word / citation / claim counts, language self-report. Content-free by default.
- **Skill output structure:** suggestion and finding counts by category. The freeform output text itself is gated behind a higher consent tier.
- **User actions:** acceptance / rejection / ignored counts, plus optional free-text feedback.
- **Timing:** when the skill was invoked and completed.

## Tiered consent

The schema bakes three consent tiers into every record, with the user choosing per-submission. The default is the lowest tier.

### Tier 1 — `structured-only`

Counts, metadata, identifiers. No manuscript text, no skill output text, no thinking. This is the default and the only tier safe under institutional policies that prohibit cloud telemetry on research data.

A tier-1 record tells you that *citation-audit ran on a 1,240-word discussion section in a biomedical manuscript and produced 7 strong / 5 moderate suggestions, of which the user accepted 6 and rejected 4*. It does not tell you anything about the manuscript content or the specific suggestions.

### Tier 2 — `output-text`

Tier 1, plus the skill's actual output text. Useful for mining what kinds of suggestions get accepted vs rejected. Still no manuscript content.

A tier-2 record adds the citation-audit output table to a tier-1 record. The manuscript text the skill ran on remains unrecorded.

### Tier 3 — `manuscript-chunk`

Tier 2, plus the manuscript chunk the skill ran on. Highest fidelity, highest privacy cost. Needed for some kinds of evaluation but explicitly not required for most.

A tier-3 record adds the discussion section text to a tier-2 record.

### Enforcement

The schema *enforces* the tier rather than describing it. A record declaring `consent_tier: structured-only` that also carries `skill_output.text` or `manuscript_chunk` fails validation. This is encoded with JSON Schema conditional subschemas (`if`/`then`), so any consumer — the CLI, an HTTP API, a third-party tool — gets the same enforcement automatically.

## Example records

A minimal tier-1 record:

```json
{
  "trace_schema_version": 1,
  "submission_id": "5f1d7c8e-3a2b-4c5d-9e8f-1234567890ab",
  "submitted_at": "2026-05-17T14:32:11Z",
  "scriptorium_version": "0.2.0",
  "consent_tier": "structured-only",
  "provenance": {
    "source": "claude-code-transcript",
    "session_id": "b497916e-600b-46cd-96d9-576a5fe929cf"
  },
  "skill": {
    "name": "citation-audit",
    "invocation_surface": "claude-code"
  },
  "model": {
    "provider": "anthropic",
    "name": "claude-opus-4-7",
    "thinking_used": true,
    "thinking_text_captured": false
  },
  "manuscript": {
    "discipline": "biomedical",
    "section": "discussion",
    "word_count": 1240,
    "citation_count": 18
  },
  "skill_output": {
    "suggestion_counts": {"strong": 7, "moderate": 5, "weak": 2}
  }
}
```

A tier-2 record adds the freeform skill output text:

```json
{
  "trace_schema_version": 1,
  "submission_id": "5f1d7c8e-3a2b-4c5d-9e8f-1234567890ab",
  "submitted_at": "2026-05-17T14:32:11Z",
  "scriptorium_version": "0.2.0",
  "consent_tier": "output-text",
  "provenance": {"source": "claude-code-transcript", "session_id": "b497916e-..."},
  "skill": {"name": "citation-audit", "invocation_surface": "claude-code"},
  "model": {"provider": "anthropic", "name": "claude-opus-4-7"},
  "skill_output": {
    "suggestion_counts": {"strong": 7, "moderate": 5, "weak": 2},
    "text": "# Citation audit\n\n## Claim/citation alignment\n..."
  }
}
```

A tier-3 record adds the manuscript chunk:

```json
{
  "trace_schema_version": 1,
  "submission_id": "...",
  "consent_tier": "manuscript-chunk",
  "skill_output": {"text": "...", "suggestion_counts": {"strong": 7}},
  "manuscript_chunk": "Recent advances in spatial transcriptomics have enabled..."
}
```

## What this schema is NOT

- **Not a personal-data schema.** Names, affiliations, ORCID, emails do not appear here. If telemetry ever needs them, that is a separate schema with its own consent flow.
- **Not a manuscript schema.** Manuscript content lives in `MANUSCRIPT_STATE.yaml` and (for tier-3 only) in the `manuscript_chunk` field. The schema does not attempt to describe the manuscript itself.
- **Not a transport schema.** Records can live as JSONL on disk, as POST bodies to a future submission API, as rows in a database — the schema fixes the record shape, not the transport.

## How thinking is handled

Extended-thinking content is recorded *if it is capturable on the source surface*, and the record makes that explicit. Specifically:

- For `provenance.source = claude-code-transcript`: Claude Code transcripts persist thinking-block structure (type and cryptographic signature) but *not* the thinking text itself. So records extracted from transcripts have `thinking_used: true` when thinking happened but `thinking_text_captured: false` always.
- For `provenance.source = sdk-runner`: a wrapper around the Anthropic SDK can capture thinking text from the streaming response. Records from that source can have `thinking_text_captured: true`.
- For `provenance.source = claude-code-hook`: hooks fire after a tool call but do not have access to thinking content. `thinking_text_captured: false`.

This is documented at the record level rather than left implicit so consumers cannot mistake structural absence of thinking for substantive absence.

## Schema evolution

The `trace_schema_version` field is `const: 1` for now. Schema changes follow the standard discipline:

- **Additive change** (new optional field): no version bump; document the addition in the changelog.
- **Field removal or semantic change**: version bump. Older records remain identifiable by their `trace_schema_version` value and can be migrated explicitly.
- **Tier semantics change**: version bump and a migration note. Tier semantics are the load-bearing privacy contract; changing them is a privacy-affecting change.

## Related

- [Issue #47](https://github.com/seandavi/scriptorium/issues/47) — the design issue this schema closes.
- [Issue #48](https://github.com/seandavi/scriptorium/issues/48) — the `scriptorium trace` subcommand that emits records of this shape from Claude Code transcripts.
- [Issue #49](https://github.com/seandavi/scriptorium/issues/49) — the telemetry-hook-with-consent-flow design, which will produce records of the same shape from a live PostToolUse hook.
