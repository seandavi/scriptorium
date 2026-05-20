# Design memos

Developer-facing design memos for scriptorium skills not yet built.
Provisional; reviewer-facing. **These memos do not reflect current
scriptorium behavior** — they capture the design questions, decision
points, and grounding gaps the project would need to resolve before
the named skill ships.

This directory is a repo-side developer artifact and is intentionally
excluded from the rendered documentation site. The site sidebar
(How-to / Reference / Concepts) covers the current shipped surface;
these memos cover what hasn't shipped yet.

## Why memos exist separately

Scriptorium's design discipline requires every skill to ground in
named evidence from [`knowledge/`](../../knowledge/). That discipline
makes it useful to write the design decisions before the code so the
rationale, the alternatives considered, and the open architectural
questions are preserved — even if the skill ultimately takes a
different shape or doesn't ship at all. A memo for a skill that
later supersedes its own design is more honest than a polished
SKILL.md backfilled after the fact.

The memos are reviewer-facing in posture: plain factual description
of what's already grounded, what's missing, what the architectural
decision points are, and what the open empirical questions are. They
are not pitches.

## Status vocabulary

Each memo declares one of:

- **design-staged** — design memo exists; grounding incomplete or
  architectural decisions unresolved. Not yet building.
- **building** — decisions made; the skill is in implementation.
- **built** — the skill has shipped. Memo is retained as historical
  context for why the design ended up where it did.
- **superseded** — the design captured in the memo was replaced by a
  different decision. Memo retained for accountability.

## Index

| Memo | Status | One-line summary | Last update |
|---|---|---|---|
| [`v0.3-statistics-consistency.md`](v0.3-statistics-consistency.md) | design-staged | Orchestrate external statistical-consistency tools (Statcheck, GRIM, SPRITE) from a scriptorium skill without doing LLM arithmetic. Deferred per issue [#13](https://github.com/seandavi/scriptorium/issues/13). | 2026-05-20 |
| [`v0.3-voice-profile.md`](v0.3-voice-profile.md) | design-staged | Extract a recognizable author voice profile from a 3–5 paper single-author corpus; surface stylistic features other skills can consume. Tracking issue [#43](https://github.com/seandavi/scriptorium/issues/43). | 2026-05-20 |
| [`v0.3-persona-calibration.md`](v0.3-persona-calibration.md) | design-staged | Checkpoint synthetic-feedback loops against the real author so a persona-driven loop does not optimize for the persona instead of the author. Tracking issue [#44](https://github.com/seandavi/scriptorium/issues/44). | 2026-05-20 |

For the bigger picture — what ships when, and which knowledge notes
ground which skills — see [`docs/roadmap.md`](../roadmap.md).
