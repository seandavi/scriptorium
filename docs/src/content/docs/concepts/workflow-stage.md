---
title: Workflow stage
description: Where scriptorium fits in the writing process. Hayes 2012 framing; the lifecycle stages each shipped skill is invokable at.
sidebar:
  order: 13
---

import { Aside } from '@astrojs/starlight/components';

Scriptorium fits the *revise* and *pre-submission* stretches of the
writing process. It does not fit the outline-and-first-draft
stretch — there is nothing declared yet to operate on. This page
explains why, using the same cognitive-process model that grounds
[declared-work scope](/concepts/declared-work-scope/), and gives
the skill-by-stage table at the bottom.

## Hayes 2012 in one paragraph

The Hayes-Flower cognitive-process model of writing, in its 2012
revision, splits writing into four sub-processes — **proposer**
(generates content), **translator** (turns proposals into
language), **transcriber** (orthography), and **evaluator** (the
reviewer role) — under a control structure that decides which one
to engage when. The processes are recursive, not linear: writers
drop out of translating to re-plan, drop out of reviewing to
re-translate. The "plan, write, edit" pipeline taught to
undergraduates is a pedagogical fiction; experienced writers move
between the processes constantly.

For the full grounding see
[`hayes-flower-writing-model`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/hayes-flower-writing-model.md)
in the knowledge layer.

## The two stages scriptorium fits

The author always owns the **proposer** role. Generating content
from nothing requires intuition, domain knowledge, and the
author's own judgement. Scriptorium does not propose for the
author.

What scriptorium does occupy is the **translator** and **evaluator**
roles, on declared inputs:

- **Translator work — declared claims into sharper prose.**
  `argumentative-flow` reads a section the author has written and
  restructures it under a preservation contract. `compression`
  reads the same section and reduces it to a declared length
  target under the same contract. Neither invents claims; both
  transform declared work into clearer prose.
- **Evaluator work — declared prose pressure-tested.**
  `citation-audit`, `reviewer-simulation`, `gap-finder`,
  `figure-text-alignment`, `desk-rejection-risk`,
  `reporting-guideline-fit`, `reporting-guideline-compliance`,
  `venue-fit`, and `author-contribution-audit` all read declared
  prose and emit structured findings about it. None of them
  rewrites the prose.

Practically, this puts scriptorium in two stretches of the
writing process:

1. **Revise.** The author has draft prose and wants it
   pressure-tested or tightened. Most scriptorium skills land
   here.
2. **Pre-submission.** The author is preparing to submit and wants
   compliance, fit, and reviewer-anticipation checks.

## Out of scope: outline, ideation, blank-page drafting

The phase the author owns alone:

- **Outline.** Choosing what to write, what to argue, what to
  include. No skill helps with this — there is no declared work
  yet for skills to ground against. Several skills explicitly
  refuse to run at `document_phase.current: outline` (see the
  table below).
- **Idea generation.** Choosing the research question, the
  hypothesis, the methodological approach. The
  [declared-work scope](/concepts/declared-work-scope/) page is
  the longer treatment of why.
- **First drafting from blankness.** Writing the first version of
  a section that does not yet exist. A skill cannot operate on a
  section that does not yet have prose; the
  [refusal pattern](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/declared-work-scope.md#refusal-behaviour-at-the-boundary)
  is to name this clearly and point at the pre-declaration work.

<Aside type="note" title="The order of work matters here">
The author proposes; scriptorium reads what was proposed. Working
the other way — letting scriptorium propose, then accepting or
rejecting — collapses the proposer / translator / evaluator
distinction Hayes' 2012 model rests on. The author retains the
proposer role for the same reason a peer reviewer does not draft
the paper they review.
</Aside>

## `document_phase.current` signals the stage

`MANUSCRIPT_STATE.yaml` has a `document_phase.current` field that
records where the document is in its lifecycle. The seven valid
values, in order:

| Phase | Meaning | Most relevant scriptorium skills |
|---|---|---|
| `outline` | Idea-and-structure stage. Most prose not yet written. | `init`, `tour`, `explain`, `venue-fit` (if `target_venue` is declared). No critique skills — outline-phase prose isn't yet declared. |
| `draft` | First-pass prose exists for most sections. | `citation-audit`, `gap-finder`, `figure-text-alignment`, `reporting-guideline-fit`, `terminology-normalization`, `argumentative-flow` (per section). |
| `review` | Prose is settled enough for internal-team or co-author review. | All `draft`-phase skills, plus `reviewer-simulation`, `outlier-sentence-detector`, `compression` (if length-bounded). |
| `revision` | Responding to internal or external review. | All `review`-phase skills, plus `author-contribution-audit`, `reporting-guideline-compliance`. |
| `submission` | Preparing to submit to the target venue. | All `revision`-phase skills, plus `desk-rejection-risk`, `compression` (against the venue's word limit). |
| `post-submission` | Awaiting decision. | `explain`, `tour` only. Other skills are runnable but most work is done. |
| `accepted` | Manuscript accepted. | `explain`, `tour` only. |

The phase axis is a coarse proxy for the
[declared-work principle](/concepts/declared-work-scope/#the-phase-axis-is-a-proxy)
— it catches the common cases but misses edge cases. A
`draft`-phase manuscript with an empty Related Work section is
still asking for blank-slate generation; a `revision`-phase
author asking about limitations framing is in scope even before
the limitations paragraph is written. Skills enforce the
declared-work principle directly; the phase axis is the
first-line filter.

## How this shows up in skills

The table below maps each shipped skill to the lifecycle stages
at which it is invokable. *Invokable* means the skill will run
and produce useful output; outside the marked stages the skill
either refuses cleanly or returns thin output because the
declared state it needs is not yet present.

The table is generated from each skill's
`manifest.yaml#lifecycle_phases` at docs-build time — adding or
removing a skill, or changing the declared phases, regenerates it
without manual edits.

<!-- GENERATED:workflow-stage-table:start -->
| Skill | Outline | Draft | Review | Revision | Submission |
|---|---|---|---|---|---|
| `argumentative-flow` | — | yes | yes | yes | — |
| `author-contribution-audit` | — | — | yes | yes | yes |
| `citation-audit` | — | yes | yes | yes | yes |
| `compression` | — | — | — | yes | yes |
| `desk-rejection-risk` | — | — | — | yes | yes |
| `explain` | yes | yes | yes | yes | yes |
| `figure-text-alignment` | — | yes | yes | yes | — |
| `gap-finder` | — | yes | yes | yes | — |
| `init` | yes | yes | yes | yes | yes |
| `outlier-sentence-detector` | — | yes | yes | yes | yes |
| `reporting-guideline-compliance` | — | — | yes | yes | yes |
| `reporting-guideline-fit` | — | yes | yes | yes | — |
| `reviewer-simulation` | — | — | yes | yes | yes |
| `terminology-normalization` | — | yes | yes | yes | — |
| `tour` | yes | yes | yes | yes | yes |
| `venue-fit` | — | — | yes | yes | yes |
<!-- GENERATED:workflow-stage-table:end -->

The source of truth for each skill's refusal behaviour is its
`manifest.yaml` and `SKILL.md` in the
[skills directory](https://github.com/seandavi/scriptorium/tree/main/skills);
the [skills reference](/reference/skills/) is the rendered catalog.

Notes on the patterns:

- **Skills that refuse on `outline` phase** —
  `author-contribution-audit`, `figure-text-alignment`,
  `gap-finder`, `reporting-guideline-compliance`,
  `reporting-guideline-fit`, `venue-fit`. All of these need
  declared prose or a declared `target_venue` to ground against;
  on outline they would have to invent.
- **Skills runnable in any phase** — `explain`, `init`, `tour`.
  These do not need declared manuscript prose; they operate on
  the plugin tree (`tour`, `explain`) or on the
  `MANUSCRIPT_STATE.yaml` itself (`init`).
- **Skills most useful late** — `desk-rejection-risk`,
  `reporting-guideline-compliance`, `author-contribution-audit`.
  All three pressure-test against external standards (editor
  triage, EQUATOR checklists, ICMJE/CRediT) the manuscript will
  meet at submission. They run earlier but the findings are less
  actionable when the declared state is still moving.

## Related

- [Start here](/concepts/start-here/) — the conceptual map this
  page is one branch of.
- [Declared-work scope](/concepts/declared-work-scope/) — the
  structural principle the phase axis is a proxy for.
- [Skills reference](/reference/skills/) — the full catalog with
  per-skill operational details.
- [`hayes-flower-writing-model`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/hayes-flower-writing-model.md)
  — the cognitive-process model this page grounds in.
