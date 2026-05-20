---
title: Start here — the mental model
description: A single-page conceptual orientation to scriptorium. What it operates on, what it does, what it won't do, and where to read next.
sidebar:
  order: 10
---

This page is the conceptual orientation. It does not install
anything, run anything, or assume you've made any decisions yet. It
exists so that by the end of one read you have the mental model the
rest of the docs assume.

If you want to do something concrete instead, jump to the
[first-run walkthrough](/how-to/first-run/).

## What scriptorium is

Scriptorium is a collection of focused AI skills that work on prose
the author has already written. Each skill is single-purpose
(audit citations, simulate reviewers, compress to a length limit,
normalize terminology) and reads the same shared editorial state
file (`MANUSCRIPT_STATE.yaml`). Every skill is grounded in a curated
evidence base — the [knowledge layer](/concepts/knowledge/) — and
each skill's `manifest.yaml` lists the specific knowledge notes its
behaviour is grounded in.

## What it operates on

Scriptorium operates on **declared work** — prose the author has
already written, or scaffolding the author has committed to in
`MANUSCRIPT_STATE.yaml` (claims, weaknesses, terminology, target
venue, audience). It does not produce prose from blankness.

This is a structural commitment, not a stylistic preference. The
full rationale lives in
[declared-work scope](/concepts/declared-work-scope/) — that page
is the answer to the most common reasonable fear about AI writing
tools, which is *the model will write the paper for me*.

The short version: scriptorium reads what you have written and
emits structured findings about it. The author retains the
proposer role.

## What it does to that prose

Three verbs cover what every shipped skill does. The
[skills reference](/reference/skills/) is the full catalog; the
list below is the conceptual shape.

**Critique** — assess existing prose, emit structured findings,
modify nothing. The output is a report the author reads.

- `citation-audit` — claim-by-claim assessment of how well the
  existing citations support the existing claims.
- `reviewer-simulation` — four-lens pressure test (methodological
  skeptic, domain expert, translational/clinical, statistical) of
  what would land if you submitted as-is.
- `gap-finder` — anchored list of premises missing, counterarguments
  not addressed, related work not engaged.

**Validate** — check the manuscript against an external standard
(a reporting guideline, an authorship policy, a venue's
requirements), modify nothing.

- `reporting-guideline-compliance` — run a CONSORT / STROBE /
  PRISMA / ARRIVE / TRIPOD checklist against the manuscript.
- `reporting-guideline-fit` — infer which checklist applies to the
  study before the checklist itself runs.
- `desk-rejection-risk` — pre-submission audit against the editor's
  triage checklist.

**Transform** — modify prose under an explicit preservation
contract. Citations, statistics, declared terminology, declared
core claims, and the author's hedging stance are preserved verbatim.
Every modification is presented as a diff for the author to accept
or reject.

- `argumentative-flow` — restructure a section for logical and
  argumentative coherence under the preservation contract.
- `compression` — reduce a section to a declared length target
  under the same preservation contract.
- `terminology-normalization` — enforce the `terminology.preferred`
  / `terminology.forbidden` / `terminology.synonyms` lists declared
  in `MANUSCRIPT_STATE.yaml`.

## What it doesn't do

These are explicit non-goals, not aspirations for later versions.
The full list lives in the [roadmap's non-goals
section](https://github.com/seandavi/scriptorium/blob/main/docs/roadmap.md#explicit-non-goals);
the three that matter for the mental model:

- **No blank-slate prose generation.** No skill drafts a section
  from nothing. The proposer role
  ([Hayes 2012](/concepts/workflow-stage/)) is the author's.
- **No autonomous reviewing.** `reviewer-simulation` and
  `desk-rejection-risk` are author-side only. Editorial-side use
  on someone else's manuscript violates ICMJE, NIH, and major-
  publisher policy, and the skills refuse to run that way.
- **No overall quality score.** No letter grade, no Flesch-Kincaid,
  no aggregate writing-quality number. Skills emit anchored
  findings, not aggregates.

## The dial

Critique can be paralyzing if it arrives all at once. The
[`guidance-level`](/concepts/guidance-level/) field in
`MANUSCRIPT_STATE.yaml` is the author's control over how much
detail and how many findings each skill surfaces per invocation.

Three values: `terse`, `standard`, `full`. The default is
`standard`. Pick the level that matches the bandwidth you have to
act on findings, not the level that feels rigorous. The
[guidance-level page](/concepts/guidance-level/) makes the safety
framing explicit — it's the answer to the second reasonable fear
about AI writing tools, which is *getting back a pile of critique
I can't process*.

## Where in the writing process

Scriptorium fits the *revise* and *pre-submission* stretches of the
writing process. It does not fit the outline-and-first-draft
stretch — there is no declared prose to operate on yet.

The full mapping uses Hayes' 2012 cognitive-process model of
writing and is laid out in
[workflow stage](/concepts/workflow-stage/). The two-sentence
version: scriptorium occupies the *translator* and *evaluator*
roles when the author has already proposed. It does not propose
for the author.

The `document_phase` field in `MANUSCRIPT_STATE.yaml` signals
which stage you're in (`outline` / `draft` / `review` /
`revision` / `submission` / `post-submission` / `accepted`).
Several skills refuse to run on `outline` because there's nothing
declared to ground against — that's the [declared-work
scope](/concepts/declared-work-scope/) principle expressed at the
phase axis.

## How this shows up in skills

Every skill named on this page is a real shipped skill — read its
entry on the [skills reference](/reference/skills/) for the
operational details (inputs, outputs, refusal behaviours, grounding
notes). The reference page is the source of truth; this page is the
map.

Three skills are worth picking out as illustrations of the mental
model:

- `init` (utility) — the only skill that writes anything outside
  the manuscript: it scaffolds `MANUSCRIPT_STATE.yaml`. Without
  this file no other skill has the declared state it needs.
- `citation-audit` (critique) — the prototypical critique skill.
  Reads declared prose plus the bibliography, emits a table, never
  invents a citation.
- `argumentative-flow` (transformation) — the prototypical
  transformation skill. Reads a declared section, emits revised
  prose plus a preservation diff showing exactly what changed and
  what was preserved verbatim.

## Where to go next

- **I want to run something concrete now** —
  [First-run walkthrough](/how-to/first-run/). Six steps from
  install to first output.
- **I want to see real shaped output before I install anything** —
  [Case study](/concepts/case-study/). A realistic discussion
  paragraph walked through `citation-audit`,
  `reviewer-simulation`, and `argumentative-flow`.
- **I want the catalog of every shipped skill** —
  [Skills reference](/reference/skills/). Categorised, with
  lifecycle stage and grounding pointers.

If you want to read the conceptual basis in more depth first, the
three deeper concept pages are:

- [Declared-work scope](/concepts/declared-work-scope/) — what
  scriptorium operates on and what it refuses.
- [Guidance level](/concepts/guidance-level/) — the author's dial
  over surface area of critique.
- [Workflow stage](/concepts/workflow-stage/) — where scriptorium
  fits in the writing process.

And the cross-cutting reference:

- [Glossary](/concepts/glossary/) — single-source definitions for
  every term the docs use.
