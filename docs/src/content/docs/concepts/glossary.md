---
title: Glossary
description: Single-source definitions for every term used across the scriptorium docs.
sidebar:
  order: 50
---

A one-page reference for terminology used across the scriptorium
docs. Each entry is two to four sentences and links to the
relevant concept page or knowledge note for the longer treatment.
This page exists so the rest of the docs can link to a single
definition; cross-references should point here rather than
duplicating definitions inline.

## Argumentative flow

The logical and structural coherence of a section's prose —
whether each paragraph's topic position connects to prior context,
whether the stress position carries new information, whether the
argument arc is visible to the reader. The `argumentative-flow`
skill operates on this property of a section under a
[preservation contract](#preservation-contract).

See: [skills reference — `argumentative-flow`](/reference/skills/).

## Core claim

A load-bearing assertion the manuscript is arguing — what a
reader of the abstract should walk away believing. Declared in
`MANUSCRIPT_STATE.yaml` under `core_claims`. Critique skills test
whether the prose actually supports each declared claim;
transformation skills must preserve declared claims verbatim
(none added, none dropped).

See: [Schema reference](/reference/manuscript-state-schema/),
[Start here — what scriptorium operates on](/concepts/start-here/#what-it-operates-on).

## Declared work / declared-work scope

What scriptorium operates on: prose the author has already
written, or scaffolding the author has committed to in
`MANUSCRIPT_STATE.yaml` (claims, weaknesses, terminology,
audience, target venue). Scriptorium does not produce prose from
blankness; the proposer role (Hayes 2012) stays with the author.

See: [Declared-work scope](/concepts/declared-work-scope/),
[`knowledge/conventions/declared-work-scope`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/declared-work-scope.md).

## Design memo

A standalone architectural decision record kept under
`docs/design/` (and rendered into the site by the docs
preprocessor). Memos document why a design choice was made — what
alternatives were considered, what evidence drove the decision,
what would prompt revisiting. They are the longer-form companion
to the knowledge layer.

## EQUATOR Network

The international network that maintains reporting-guideline
checklists for health research — CONSORT (RCTs), STROBE
(observational), PRISMA (systematic reviews), ARRIVE (animal
research), TRIPOD / TRIPOD+AI (prediction models), STARD
(diagnostic accuracy), CARE (case reports), COREQ (qualitative),
CHEERS (economic evaluations), and their AI extensions
(CONSORT-AI, SPIRIT-AI). `reporting-guideline-fit` infers which
checklist applies to a manuscript;
`reporting-guideline-compliance` runs the checklist against the
prose.

See: <https://www.equator-network.org/>.

## Guidance level

The author's dial over how much detail and how many findings
scriptorium surfaces per skill invocation. Schema enum at
`meta.guidance_level`: `terse` (small handful, big-picture only),
`standard` (focused list — the default), `full` (every finding
above threshold, with rationale). Set the level to match the
bandwidth you have for revisions, not the level that feels
rigorous.

See: [Guidance level](/concepts/guidance-level/),
[`knowledge/conventions/guidance-level`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/guidance-level.md).

## Knowledge note

A standalone evidence-grounded document under `knowledge/` that
documents what the literature says about some aspect of scholarly
writing or peer review. Each skill's `manifest.yaml` lists the
knowledge notes its design decisions ground in. The full
structure of a knowledge note is documented in the
[knowledge layer README](https://github.com/seandavi/scriptorium/blob/main/knowledge/README.md).

See: [Knowledge layer](/concepts/knowledge/).

## `MANUSCRIPT_STATE.yaml`

The shared editorial-state file every scriptorium project
carries. Lives at the root of the manuscript repository. Records
what the manuscript is arguing (`core_claims`), the limitations
already acknowledged (`known_weaknesses`),
`terminology.preferred` / `forbidden` / `synonyms`, `style`
(tone, voice, audience), `constraints`, the `target_venue`, the
`document_phase`, and `meta.guidance_level`. Every skill reads
it; only `init` writes it. It is a local file; nothing in
scriptorium uploads or syncs it.

See: [Schema reference](/reference/manuscript-state-schema/),
the [worked example](https://github.com/seandavi/scriptorium/blob/main/templates/MANUSCRIPT_STATE.example.yaml).

## Preservation contract

The explicit list of properties a transformation skill
(`argumentative-flow`, `compression`) is required to preserve
verbatim when it modifies prose: every citation key, every
numerical value / p-value / confidence interval / unit, the
declared `terminology.preferred` / `forbidden` / `synonyms`
lists, declared `core_claims`, and the author's hedging strength
and stance markers. Any shift in hedging is reported as a
per-edit note rather than absorbed silently. The contract is
what scriptorium guarantees; sentence-level "voice preservation"
is explicitly not.

See: [Landing — voice preservation, the honest version](https://github.com/seandavi/scriptorium#voice-preservation-the-honest-version),
[`semantic-preservation`](https://github.com/seandavi/scriptorium/blob/main/knowledge/editing/semantic-preservation.md).

## Reviewer simulation lens

One of four attentional perspectives `reviewer-simulation` applies
to a manuscript: methodological skeptic, domain expert,
translational/clinical, statistical. Each lens emits the same
six-section structure (Major Critiques, Minor Critiques, Fatal
Concerns, Enthusiasm Drivers, Suggested Revisions, Acceptance
Risk). The term is *lens*, not *persona*. A lens is an attentional
focus on what a reader of that disposition would notice; a persona
implies impersonating a specific reviewer, which the skill does
not do.

See: [skills reference — `reviewer-simulation`](/reference/skills/),
[Case study](/concepts/case-study/) for example output.

## Skill

A single-responsibility unit of scriptorium functionality.
Implemented as a directory under `skills/` containing
`manifest.yaml` (machine-readable metadata), `SKILL.md` (the
prompt for Claude Code), `prompt.md` (the platform-neutral
prompt), `README.md` (the human-readable contract), and
`examples/`. Skills do not auto-invoke; the author chooses which
one to run and when.

See: [Skills reference](/reference/skills/) for the catalog.

## Skill category

One of six categorical labels in a skill's `manifest.yaml`:

- **critique** — assesses prose; does not modify the manuscript.
  Emits structured findings.
- **validation** — checks against an external standard (reporting
  guideline, authorship policy); does not modify.
- **normalization** — enforces declared style and terminology;
  suggests edits, never auto-applies.
- **transformation** — modifies prose under a
  [preservation contract](#preservation-contract).
- **meta** — orientation or explanation; no manuscript modification.
- **utility / onboarding** — bootstrap; modifies only
  `MANUSCRIPT_STATE.yaml` (currently only `init`).

The category determines what the skill can produce and the
guarantees that come with that production.

See: [Skills reference — categorisation axes](/reference/skills/#categorisation-axes).

## Workflow stage

Where in the writing process scriptorium fits. The
`document_phase.current` field in `MANUSCRIPT_STATE.yaml` records
the stage (`outline` / `draft` / `review` / `revision` /
`submission` / `post-submission` / `accepted`). Scriptorium
occupies the *translator* and *evaluator* roles in Hayes' 2012
cognitive-process model — most useful at `draft` through
`submission`. The author owns the *proposer* role; outline and
ideation are out of scope.

See: [Workflow stage](/concepts/workflow-stage/).

## Related

- [Start here](/concepts/start-here/) — the conceptual map.
- [Declared-work scope](/concepts/declared-work-scope/) —
  what scriptorium operates on.
- [Guidance level](/concepts/guidance-level/) — the author's
  dial.
- [Workflow stage](/concepts/workflow-stage/) — where in the
  writing process scriptorium fits.
- [Skills reference](/reference/skills/) — the catalog.
- [Schema reference](/reference/manuscript-state-schema/) —
  every field in `MANUSCRIPT_STATE.yaml`.
