---
title: Declared-work scope
description: What scriptorium operates on, why that cut is structural rather than stylistic, and how each shipped skill respects it.
sidebar:
  order: 11
---

import { Aside } from '@astrojs/starlight/components';

Scriptorium operates on prose the author has already written, or on
scaffolding the author has committed to in `MANUSCRIPT_STATE.yaml`.
By default it does not produce prose from a blank page. This page is
the why-and-where of that default, and the table at the bottom shows
how each shipped skill respects it.

The boundary is a default the author controls. Each skill declares
its boundary refusals as **scope guards** with `default: refuse`, and
the author can override a scope guard for one run or for the project.
The accuracy guards that sit alongside them, such as never citing
from model memory, cannot be overridden.
[Author authority](/concepts/author-authority/) covers the mechanism.

The fuller, evidence-grounded version of this principle lives in
[`knowledge/conventions/declared-work-scope`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/declared-work-scope.md).
This page is the author-facing summary.

## The scope cut

Scriptorium reads two kinds of input:

1. **Declared prose.** Sentences, paragraphs, sections you have
   already written — even rough or unfinished. A methods section in
   draft. A discussion paragraph that doesn't yet flow. An abstract
   stub.
2. **Declared scaffolding.** Anything you have committed to in
   `MANUSCRIPT_STATE.yaml` — the `core_claims` you are arguing, the
   `known_weaknesses` you have already chosen to acknowledge,
   `terminology.preferred` / `terminology.forbidden`, the
   `target_venue`, the `audience`, the `tone`, the `voice`.

Both count as *declared work*. A skill grounds its output against
one or both. It does not synthesise output from nothing.

The mirror default: scriptorium does not draft sections from a
blank page. It does not propose what the paper should be arguing.
It does not invent claims for the author to defend. A skill steps
outside this only when the author overrides the scope guard that
holds it.

<Aside type="note" title="Generation isn't out of scope — blank-slate generation is, by default">
A future skill that takes declared significance + declared
hypotheses + declared methods and turns them into specific-aims
prose would still be in scope, because the inputs are declared
scaffolding. (For NIH applications it would also carry the
`nih-application-prose` policy guard; see the
[roadmap](/roadmap/).) A skill that helps an author "figure out
what to study" is not in scope by default, because there is nothing
declared to ground against. The principle is *declared inputs*, not
*read-only*.
</Aside>

## Why this cut

Two reasons, one cognitive and one empirical.

### Cognitive: Hayes 2012

The Hayes-Flower cognitive-process model of writing, in its 2012
revision, splits the writing process into four sub-processes —
**proposer**, **translator**, **transcriber**, and **evaluator** —
arbitrated by a control structure that decides which one to engage
next. The model is the canonical psychological account of what
writers actually do.

Scriptorium's scope maps cleanly onto Hayes' processes:

- **Proposer** — generating content from nothing — is out of scope.
  This is the activity that requires intuition, domain knowledge,
  and the author's own judgement.
- **Translator** — turning declared proposals into language — is in
  scope. `argumentative-flow` lives here.
- **Transcriber** — orthography — is trivially in scope.
- **Evaluator** — assessing what's been written — is in scope.
  `citation-audit`, `reviewer-simulation`, `gap-finder`, and
  `desk-rejection-risk` are all evaluator-role skills.

Hayes' updated model treats working memory as the writer's
bottleneck. The discipline scriptorium adopts is to absorb the
translator and evaluator load so the author's working memory stays
available for the proposer role. Stepping into the proposer role
would defeat the purpose.

For the full grounding see
[`hayes-flower-writing-model`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/hayes-flower-writing-model.md)
in the knowledge layer, and the
[workflow-stage page](/concepts/workflow-stage/) for the practical
implications.

### Empirical: the failure modes of blank-slate generation

The two most-cited failure modes of LLM scholarly writing —
hallucinated citations and authorial-voice loss — are both
failure modes of blank-slate generation. They happen much less, or
do not happen at all, when the model is operating on declared
inputs.

- A skill that audits the author's declared citations against
  bibliographic metadata cannot hallucinate references. A skill
  that generates prose from blankness will, eventually, hallucinate
  references to back unbacked claims.
- A skill that operates on the author's existing prose has the
  author's voice as input and can preserve it. A skill that
  generates from blankness produces centre-of-distribution prose
  by construction.

Scriptorium's declared-work scope is the structural defence
against these failure modes. The per-skill guards — "no invented
citations" for `citation-audit`, "preserve hedging and stance
markers" for `argumentative-flow`, "never claim verification of
papers you haven't seen" for any skill that touches references —
are the same principle expressed at each skill's surface.

The deeper grounding for the failure-mode evidence is
[`ai-writing-failure-modes`](https://github.com/seandavi/scriptorium/blob/main/knowledge/prior-art/ai-writing-failure-modes.md).

## What "declared" means in practice

The bar for "declared" is much lower than the bar for "finished":

- A draft sentence — even if you plan to rewrite it.
- A stated `core_claim` in `MANUSCRIPT_STATE.yaml`.
- A `known_weakness` listed in `MANUSCRIPT_STATE.yaml`, even before
  the limitations paragraph is written.
- A paragraph stub that names what it will argue but not yet how.
- A methods section that's complete in structure but still rough in
  prose.
- A `target_venue` declared in `project.target_venue`, even before
  a draft exists for that venue's format.

In all of these cases, scriptorium has something to ground against
and can run. The trigger for the default refusal is not "this prose
is rough," it is "there is no prose here yet."

## What's out of scope by default

What the skills decline unless the author overrides the scope guard
involved:

- **Draft an empty section.** Asking a skill to fill in an empty
  Related Work section is a blank-slate generation request
  (`generation-from-blankness`). By default the skill declines and
  points at the pre-declaration work that needs to happen first.
- **Write a discussion from a results table.** The discussion is
  proposer work — it requires the author's reading of what the
  results mean. A skill cannot ground discussion prose against a
  table alone.
- **Propose new aims, claims, or hypotheses.** Adding to
  `core_claims` based on what would "round out" the paper is
  proposer work the author owns (`pre-declaration-ideation`).
- **Generate a literature review from a topic name.** Even if a
  bibliography is supplied, choosing what to engage with — and how
  — is proposer work.

One related refusal is not a scope guard and no override changes it:

- **Invent a citation to support a claim.** This is the canonical
  hallucination case, and `no-parametric-citations` is an accuracy
  guard: no skill names a citation from model memory. By default
  `citation-audit` and `gap-finder` surface missing support and
  suggest search strategies, and the author chooses what to cite.
  An author who overrides their `citation-recommendations` scope
  guard gets named papers, but only works the skill resolved against
  Crossref or PubMed in that session.

When a skill is asked to operate beyond its declared-work boundary,
the [refusal pattern](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/declared-work-scope.md#refusal-behaviour-at-the-boundary)
is to name the refusal clearly, point at the pre-declaration work,
say how to override (answer in this run, or add an entry under
`meta.overrides`), and not lecture. One sentence is enough.

## The phase axis is a proxy

`MANUSCRIPT_STATE.yaml` has a `document_phase.current` field that
takes values `outline` / `draft` / `review` / `revision` /
`submission` / `post-submission` / `accepted`. Several skills
decline by default on `outline` (the `outline-phase` scope guard)
for the same reason this page describes: outline-phase manuscripts often have empty sections,
and operating on an empty section is blank-slate generation.

The phase axis is a *proxy* for the declared-work principle. It
catches the common cases. It misses edge cases — a `draft`-phase
manuscript with an empty Related Work section is still asking for
blank-slate generation; a `revision`-phase author asking about
limitations framing is in scope even before the limitations
paragraph is written. The phase axis is too coarse to be the
actual rule; the declared-work axis is.

For the operational rule each skill follows on the phase axis, see
the [skills reference](/reference/skills/) and the
[workflow-stage page](/concepts/workflow-stage/).

## How this shows up in skills

The table is the operational expression of this page. Every shipped
skill names what it consumes from the author's declarations and
what it declines to synthesise by default. Rows are alphabetical.
Which of these are overridable scope guards and which are fixed
accuracy guards is listed per skill in the
[guard table](/concepts/author-authority/#guards-by-skill).

| Skill | Declared inputs | What it won't invent by default |
|---|---|---|
| `argumentative-flow` | Manuscript section + `terminology.*` + `style.tone` / `style.voice` + declared `core_claims` | New claims; new citations; voice changes outside declared style |
| `author-contribution-audit` | Author Contributions section + `project.target_venue` (optional) | Authorship adjudication; CRediT roles not derivable from declared text |
| `citation-audit` | Manuscript prose + bibliography | New citations; full-text claims about papers not supplied |
| `compression` | Manuscript section + `constraints.max_word_count` + declared `core_claims` | Cuts to declared claims; cuts to citations or statistics |
| `desk-rejection-risk` | Manuscript + `project.target_venue` | Generic advice (declines without a declared venue) |
| `explain` | Plugin tree only | Anything outside the plugin tree |
| `figure-text-alignment` | Manuscript prose + figure captions | Image content (text-only by default); fabricated panel descriptions |
| `gap-finder` | Manuscript prose + declared `core_claims` + `known_weaknesses` | Prose to fill the gap; citations to fill it |
| `init` | Filesystem + author Q&A | Fields beyond what the schema declares |
| `outlier-sentence-detector` | Manuscript prose only | Universal quality thresholds; the calibration is per-manuscript |
| `reporting-guideline-compliance` | Manuscript + inferred reporting guideline | Prose to fill missing checklist items |
| `reporting-guideline-fit` | Manuscript methods + abstract | Authoritative declaration of the guideline; the author confirms |
| `reviewer-simulation` | Manuscript + `core_claims` + `known_weaknesses` + `project.target_venue` | Critiques of work not in the manuscript |
| `terminology-normalization` | Manuscript + `terminology.*` lists | Stylistic flattening beyond the declared lists |
| `tour` | Plugin tree only | Anything beyond what's in the plugin tree |
| `venue-fit` | `project.target_type` + manuscript metadata + (optional) `pub_history` | Predatory venues; venue assessment without `target_type` |

The pattern that repeats: the *declared inputs* column is what the
skill grounds against; the *won't invent* column is what the skill
does not produce by default because it has no declared ground to
anchor against.

## Related

- [Start here](/concepts/start-here/) — the conceptual map this
  page is one branch of.
- [Workflow stage](/concepts/workflow-stage/) — the practical
  expression of the proposer/translator/evaluator split.
- [Guidance level](/concepts/guidance-level/) — the sister
  convention controlling *how* scriptorium talks; this page
  controls *where* it operates.
- [Author authority](/concepts/author-authority/) — how the
  author overrides this page's scope guards, and which guards
  stay fixed.
- [`knowledge/conventions/declared-work-scope`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/declared-work-scope.md)
  — the full, evidence-grounded note.
- [`hayes-flower-writing-model`](https://github.com/seandavi/scriptorium/blob/main/knowledge/scientific-writing/hayes-flower-writing-model.md)
  — the cognitive-process model this scope cut grounds in.
- [`ai-writing-failure-modes`](https://github.com/seandavi/scriptorium/blob/main/knowledge/prior-art/ai-writing-failure-modes.md)
  — the empirical evidence the scope cut defends against.
