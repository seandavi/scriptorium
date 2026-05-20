---
title: First run
description: Install scriptorium, scaffold a state file, validate it, and run your first skill. A concrete walkthrough from zero to one shaped output.
sidebar:
  order: 15
---

import { Aside } from '@astrojs/starlight/components';

A concrete walkthrough from installing scriptorium to seeing your
first shaped output. Assumes you have a manuscript directory with
some prose already written; if you don't, the conceptual
walk-through is [Start here](/concepts/start-here/) instead.

The whole flow takes ten to fifteen minutes the first time. Most of
that is choosing what to put in `MANUSCRIPT_STATE.yaml`.

## 1. Install scriptorium

Follow [Install](/how-to/install/) for the full set of paths.
The short version for Claude Code:

```text
/plugin marketplace add seandavi/scriptorium
/plugin install scriptorium@scriptorium
```

You'll also want the Python CLI for the steps below. From a
checkout of the repo or a `pip` install:

```bash
uv tool install agentic-scriptorium
# or
pip install agentic-scriptorium
```

Verify the CLI:

```bash
scriptorium --help
```

You should see subcommands including `init`, `validate`, `list`,
and `prompt-pack`.

## 2. Scaffold `MANUSCRIPT_STATE.yaml`

From the root of your manuscript directory:

```bash
scriptorium init ./my-paper
```

This writes a starter `MANUSCRIPT_STATE.yaml` with every top-level
key present and commented. The file is the [shared editorial
state](/reference/manuscript-state-schema/) every skill reads;
without it, no other skill has the declared scaffolding it needs.

The file is local to your repo. Nothing in scriptorium uploads or
syncs it. Whether to commit it (private fork; private remote;
`.gitignore`) is your call.

<Aside type="note" title="Two ways to populate the file">
You can edit `MANUSCRIPT_STATE.yaml` directly, or run the
conversational bootstrap inside Claude Code:

```text
/scriptorium:init
```

The conversational version infers what it can from the filesystem
(title, sections, bibliography paths) and asks you about the
subjective fields (`core_claims`, `known_weaknesses`,
`terminology`, `audience`). On first use it sets
`meta.guidance_level: full` by default so the workflow gets
explained as you go.
</Aside>

## 3. Populate the file

The fields scriptorium most needs to do useful work:

- **`project.title`** — what the paper is called.
- **`project.target_type`** — `manuscript`, `grant`, `review`, or
  `thesis-chapter`.
- **`project.target_venue`** — the journal or funder you're
  targeting. Several skills (`desk-rejection-risk`, `venue-fit`,
  `author-contribution-audit`) refuse to run without one.
- **`document_phase.current`** — one of `outline` / `draft` /
  `review` / `revision` / `submission` / `post-submission` /
  `accepted`. See [workflow stage](/concepts/workflow-stage/) for
  the per-stage table.
- **`core_claims`** — the load-bearing arguments the paper is
  making. Two to four entries. The grain that works: *"X is
  required for Y in Z"* (specific) rather than *"we characterise
  X"* (vague).
- **`known_weaknesses`** — limitations you have already chosen to
  acknowledge. Reviewer-simulation will *not* flag these as fresh
  fatal critiques (it reads the field as calibration input, not
  disclosure target).
- **`terminology.preferred`** / **`terminology.forbidden`** /
  **`terminology.synonyms`** — your declared terminology
  choices. `terminology-normalization` and the transformation
  skills enforce these.

A worked example for an imaginary biomedical paper lives at
[`templates/MANUSCRIPT_STATE.example.yaml`](https://github.com/seandavi/scriptorium/blob/main/templates/MANUSCRIPT_STATE.example.yaml).
Drop a copy anywhere as a reference:

```bash
scriptorium init --example /tmp/example
```

A minimal version sufficient to run most skills looks like:

```yaml
meta:
  guidance_level: standard

project:
  title: "Single-cell profiling of CD8+ T cell exhaustion in PDAC"
  target_type: manuscript
  target_venue: "Nature Cancer"

document_phase:
  current: revision

core_claims:
  - "PDAC tumor-infiltrating CD8+ T cells exhibit a distinct
     exhaustion trajectory characterized by early loss of
     effector cytokine production."
  - "A four-gene signature (TOX, PDCD1, HAVCR2, LAG3) predicts
     non-response to anti-PD-1 monotherapy with AUC=0.82."

known_weaknesses:
  - "Validation cohort (n=44) is underpowered for subgroup
     analysis by tumor stage."
  - "No functional ex vivo killing assays — exhaustion is defined
     transcriptionally, not functionally."

terminology:
  preferred:
    - "tumor-infiltrating lymphocytes (TILs)"
    - "anti-PD-1"
  forbidden:
    - "novel"
    - "groundbreaking"

bibliography:
  paths:
    - "references.bib"
  format: bibtex
```

## 4. Validate the file

```bash
scriptorium validate MANUSCRIPT_STATE.yaml
```

The validator checks the file against the JSON Schema. It catches
typos in enum values (e.g. `guidance_level: medium` — not a valid
enum value; `terse` / `standard` / `full` are), missing required
keys, and structural mistakes. If validation passes you're ready
to run skills.

## 5. Run your first skill

Pick a skill based on where your manuscript is. Three good first
runs:

### If your manuscript has citations: `citation-audit`

Inside Claude Code, in the manuscript repo:

```text
/scriptorium:citation-audit
```

The skill reads your prose and bibliography and emits a table —
one row per citation-bearing claim. For each row: the claim, the
citation, an assessment of fit (strong / weak / partial /
unsupported / causal overreach), and a recommendation.

The skill never adds a citation. Recommendations point at
specific search strategies (the right database, the right time
horizon) for you to act on; the author chooses what to actually
cite. A full worked output lives in the
[case study](/concepts/case-study/#step-1-citation-audit--claim-by-claim-assessment).

### If your manuscript has declared terminology: `terminology-normalization`

```text
/scriptorium:terminology-normalization
```

The skill reads your `terminology.preferred` / `forbidden` /
`synonyms` lists and walks the manuscript looking for drift. It
reports occurrences and suggests normalisations. It does not
modify the manuscript without your consent.

### If your manuscript is early-draft and you want a pressure-test: `gap-finder`

```text
/scriptorium:gap-finder
```

Reads your prose and emits an anchored taxonomy of gaps — claims
under-supported, premises missing, counterarguments not
addressed, internal-consistency mismatches. Each finding is
anchored to a specific passage. The skill refuses cleanly on
empty sections — it does not draft prose to fill gaps.

A shaped output looks like (abbreviated):

```text
### Premise gaps

- Section 4.2, paragraph 2: The claim "this generalises to other
  surgical procedures" assumes the cohort included multiple
  procedures. The methods describe only Roux-en-Y; either narrow
  the claim or note that generalisation is hypothetical.

### Counter-argument gaps

- Discussion, paragraph 3: The alternative hypothesis that the
  duration effect reflects HbA1c rather than disease duration is
  not addressed. Either show it's not confounded (sensitivity
  analysis) or acknowledge as a limitation.

### Search strategies (if you want to fill these)

- For Roux-en-Y vs sleeve-gastrectomy generalisation: PubMed
  "bariatric procedure type" AND "T2D remission" AND outcomes
  (2015-2024).
```

## 6. Pick a guidance level based on what you want

`meta.guidance_level` controls how much detail each skill
surfaces per invocation. The field is the author's filter; pick
the level that matches the bandwidth you have to act on
findings.

- **Early-stage draft, want the most-important-things-first** —
  set `terse`. Surfaces a small handful of high-priority
  findings, not the full list.
- **Mid-revision, want the focused complete list** — leave at
  `standard` (the default).
- **Pre-submission pressure-test, want every finding with
  rationale** — set `full`. Adds per-finding grounding to the
  standard output.

The structured shape of each skill's output does not change with
guidance level; what changes is how many findings are surfaced
and how much rationale wraps each one.

For the full treatment, including the safety framing this dial
exists to support, see [Guidance level](/concepts/guidance-level/).

## 7. What to do with the output

Two things to keep in mind when reading skill output:

**It's a report, not a rewrite.** Critique skills
(`citation-audit`, `reviewer-simulation`, `gap-finder`,
`desk-rejection-risk`, `figure-text-alignment`,
`reporting-guideline-fit`, `reporting-guideline-compliance`,
`author-contribution-audit`, `venue-fit`,
`outlier-sentence-detector`) modify nothing. The output is for
you to read, decide on, and act on by editing the manuscript
yourself.

Transformation skills (`argumentative-flow`, `compression`) do
modify prose, but only present the modification as a diff under
the [preservation contract](/concepts/glossary/#preservation-contract).
You accept or reject the diff; nothing is silently applied to
your manuscript file.

**The findings are anchored, not aggregated.** No skill produces
an overall quality score. No letter grade. No aggregate
"writing-quality" number. The output is one finding per claim,
one finding per anchor — each one independently actionable. The
mental shift the first-time user usually has to make is that the
skill does not tell you whether the paper is good; it surfaces
things to consider.

<Aside type="note" title="The author owns every edit">
Scriptorium's posture is *the author retains responsibility for
their writing*. Skills emit findings; the author chooses what to
act on. There is no auto-apply for any skill that touches
manuscript prose.
</Aside>

## Where to go next

- **The conceptual map** — [Start here](/concepts/start-here/).
- **A shaped example** — [Case study](/concepts/case-study/)
  walks `citation-audit`, `reviewer-simulation`, and
  `argumentative-flow` through a realistic discussion paragraph.
- **The skill catalog** — [Skills reference](/reference/skills/)
  for every shipped skill, categorised, with lifecycle stage and
  grounding pointers.
- **The state file** — [Schema reference](/reference/manuscript-state-schema/)
  for every field in `MANUSCRIPT_STATE.yaml`.
