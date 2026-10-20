---
title: Guidance level
description: The author's dial over how much detail and how many findings scriptorium surfaces per skill invocation. The defence against critique paralysis.
sidebar:
  order: 12
---

import { Aside } from '@astrojs/starlight/components';

`meta.guidance_level` is the field in `MANUSCRIPT_STATE.yaml` that
controls how much detail each skill surfaces around its work. It
takes one of three values:

```yaml
meta:
  guidance_level: terse      # or: standard, full
```

This page leads with the safety framing because that is the most
load-bearing thing about the field. The spec details come second.

## What this dial actually protects against

The thing scriptorium has to defend against is not "the author
wants too little critique." It is the opposite. The realistic
failure mode is that a skill returns thirty anchored findings and
the author closes the laptop. Critique without bandwidth to act on
it is paralysing.

The guidance-level dial is the author's control over the surface
area of critique. Set it to match the bandwidth you have for
revisions in this sitting, not the level that feels rigorous.

<Aside type="caution" title="More critique isn't more correctness">
Surfacing every observation a skill could make is not the same as
making the manuscript better. It is the same as giving the author
more work to triage. The skills are willing to find a lot;
`guidance_level` is the author's filter on what to surface. If
the level is wrong for your bandwidth, the result feels like an
interrogation rather than help.
</Aside>

## The three levels

The schema enum at `meta.guidance_level` has exactly three values.
The default when the field is unset is `standard`.

| Level | What gets surfaced | When to pick it |
|---|---|---|
| `terse` | A small handful of the highest-priority findings. Big-picture only. Questions and confirmations, no framing prose between turns. | Early-stage drafts; first pass on a long section; any time the author wants to know "what's the most important thing I should fix?" rather than the full list. |
| `standard` (default) | A focused list of findings, each anchored. One-line "why" before non-obvious questions. No upfront orientation, no end-of-phase recaps. | Default for most invocations. The author has used scriptorium before, doesn't need a tutorial, but appreciates anchoring when a question's purpose isn't obvious. |
| `full` | Every finding above the skill's confidence threshold, with per-finding rationale. Upfront orientation; 2-3 sentence rationale before each elicited field; end-of-phase recap. | First-time use; any time the author wants scriptorium to teach the workflow alongside doing it; late-stage pressure-test where the author wants the full list and the bandwidth to triage it. |

The structured shape of each skill's output does not change with
guidance level. `citation-audit` still produces the same kind of
claim-by-claim assessment table at every level; what changes is
how many rows it surfaces and how much rationale wraps each row.
What also changes is how much explanatory prose surrounds the
question-and-answer turns of a conversation-bearing skill.

## What "more critique" doesn't mean

Three things `full` is not:

- **`full` is not "the most accurate."** All three levels apply
  the same evidence base and the same skill logic. The difference
  is filtering and framing, not rigour.
- **`full` is not "the safest."** Surfacing every finding is only
  safer if you have the bandwidth to triage them. If you don't,
  `full` is the level most likely to produce paralysis.
- **`full` is not "what the maintainer would pick."** Most return
  users sit at `standard` for most invocations. `full` is the
  level for first-time use and for the moments where you have set
  aside time to do the full pass.

The mirror also matters: `terse` is not "lazy." For early drafts
the right move is often a small handful of high-priority findings
the author can act on now, not the exhaustive list. The point of
the skill is to surface what is tractable for the author to act
on next — not to enumerate every observation.

## For early-stage drafts

`terse` is the right default at draft phase. The reasoning:

- Early drafts have a lot of things that will change anyway. Most
  detailed findings on an early draft would be wasted because the
  prose they anchor to is about to be rewritten.
- The bandwidth-to-act question is sharpest at draft. The author
  wants to know what to fix before continuing to write — not
  every observation a skill could make.
- The structured output is still the same shape. `terse` does not
  give you a worse table; it gives you a shorter one.

The level is per-author and per-project, not per-skill. Set it
once in `MANUSCRIPT_STATE.yaml`; every conversation-bearing skill
reads it and adapts accordingly.

## The check-in protocol

Skills do not interrogate the author about the guidance level
every session. They read the field at entry, default to `standard`
if unset, and watch for signal during the session that the level
might be mis-set.

Signals a skill watches for:

- **Toward `full`** — the author asks "what does X mean?" or "why
  does this matter?" twice or more about scriptorium concepts.
- **Toward `terse`** — the author says some variant of "skip the
  explanation," "just ask the question," or consistently provides
  one-word answers that suggest the framing isn't earning its
  space.

When a signal fires the skill offers once, at the first natural
phase boundary: *"You've asked a few clarifying questions — want
me to switch to full? It adds a short rationale before each
field."* Or: *"You're moving fast — want me to drop to terse? Just
the questions."* If the author declines, the offer is not repeated
in that session.

A direct mid-flight command — *"switch to terse"*, *"go full"* —
always wins and updates the YAML.

The full protocol lives in
[`knowledge/conventions/guidance-level`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/guidance-level.md).

## How this shows up in skills

`meta.guidance_level` is read by every conversation-bearing skill.
The per-skill block below is generated from each skill's
`manifest.yaml#guidance_level_behavior` at docs-build time —
adding or removing a skill, or changing the per-level framing,
regenerates the block without manual edits.

<!-- GENERATED:guidance-level-skills:start -->
- **`argumentative-flow`**
  - `terse` — Open with one line ("running argumentative-flow on <section>"); emit the markdown report; no closing summary.
  - `standard` — Open with the section's role in the manuscript and what the structural diagnosis will check; close with a one-line summary of the most material structural issue found.
  - `full` — Open with what reader-expectation theory predicts about how the section should be organised (topic position to subject to stress position) and what narrative frameworks add; close with which proposed changes are about logic vs. about flow. The ESL-aware hedging preservation is surfaced in the preservation report.
- **`author-contribution-audit`**
  - `terse` — Open with one line ("running author-contribution audit"); emit the markdown report; no closing summary.
  - `standard` — Open with one sentence naming the state (present / absent / sketchy) and the number of listed authors; close with a one-line summary of the most material finding.
  - `full` — Open with what the audit does (ICMJE four criteria + CRediT 14 roles + journal-specific variants when target_venue is set) and why it matters (Wislar et al. 2011 BMJ — 21% of papers at top medical journals had honorary or ghost authorship; the CRediT taxonomy is the field's structural response). The structured output is unchanged across levels.
- **`citation-audit`**
  - `terse` — Open with a one-line "running citation audit"; emit the markdown report; no closing summary. Surfaces only the highest-priority claim-citation mismatches.
  - `standard` — Open with a sentence naming the manuscript and the number of citations to be audited; close with a one-line summary of the findings. The full table with per-claim rationale.
  - `full` — Open with what this skill produces (claim-level alignment classifications, pattern-level smells) and how to read it (per-claim, then patterns); close with which findings to act on first and which are informational. The structured output itself is unchanged across levels.
- **`compression`**
  - `terse` — Open with one line ("running compression on <section>, target <N> words"); emit the markdown report; no closing summary.
  - `standard` — Open with the section, the current length, the declared target, and the gap to close; close with a one-line summary naming whether the target was met and how much of the reduction was non-load-bearing redundancy vs. structural reduction.
  - `full` — Open with what compression-as-copyediting means (line editing, one step below argumentative-flow's developmental scope) and what the extraneous-vs-germane-load distinction predicts; close by naming which proposed edits cleared filler and which approached the germane-load boundary and should be reviewed carefully.
- **`desk-rejection-risk`**
  - `terse` — Open with a one-line "running desk-rejection-risk audit against {target_venue}"; emit the markdown report; no closing summary.
  - `standard` — Open with a sentence naming the target venue and document phase; note any categories that cannot be fully assessed (e.g. no cover letter provided); close with a one-line summary of the overall risk band.
  - `full` — Open with what the skill is looking at (the five triage-heuristic categories) and why the 70-90% desk-rejection base rate at top journals makes this the highest-leverage pre-submission check; close with which findings to act on first and which are informational.
- **`explain`**
  - `terse` — Suppress the "why this matters" prose; emit only the structured summary.
  - `standard` — Keep the framing around the structured summary; one-screenful target with sources cited at the end.
  - `full` — Keep the framing and the rationale; the synthesis aims for one screenful regardless of level — what changes is whether background prose accompanies the structured summary.
- **`figure-text-alignment`**
  - `terse` — Open with a one-line "running figure-text alignment (text-only)"; emit the markdown report; no closing summary.
  - `standard` — Open with a sentence naming the manuscript and the number of figures discovered; close with a one-line summary of the findings.
  - `full` — Open with what this skill produces (per-figure caption-vs-body-text alignment classification + pattern-level flags) and what it explicitly does not do (read figure images); close with which findings to act on first and which are informational. The no-image-reading posture is never relaxed based on guidance level.
- **`gap-finder`**
  - `terse` — Open with one line ("running gap analysis"); emit the markdown report; no closing summary. Surfaces the top three to five anchored gaps.
  - `standard` — Open with a sentence naming the focus question and the gap categories that will be checked; close with which category had the most findings and whether any are load-bearing. The full anchored list.
  - `full` — Open with what gap-finder is doing (structured taxonomy of seven gap categories: literature, evidence, methodological, population, translation, counterargument, internal-consistency) and why this matters (the seven categories suggest different remediation strategies). Adds per-gap search strategies the author can run.
- **`init`**
  - `terse` — Saves the preference and runs init itself at full this session; later invocations of other skills honor terse — purely questions and confirmations, no framing prose between turns.
  - `standard` — Saves the preference and runs init itself at full this session; later invocations honor standard — a one-line "why" on non-obvious fields only, no upfront orientation, no end-of-phase recap.
  - `full` — Saves the preference and runs init itself at full this session; later invocations honor full — orientation up front, per-field rationale, and an end-of-phase recap. init always runs at full regardless of the saved value because it is the user's first contact with scriptorium and the place to recalibrate the preference.
- **`outlier-sentence-detector`**
  - `terse` — Open with a one-line "running outlier-sentence detector"; emit the markdown report; surface up to ~3 flags per dimension; no closing summary.
  - `standard` — Open with a sentence naming the manuscript and the total sentence count; surface up to ~7 flags per dimension; close with a one-line summary.
  - `full` — Open with what this skill produces (length, complexity, nominalization-density outliers, calibrated against the manuscript itself) and a one-paragraph explanation that this is not a quality score; surface up to ~15 flags per dimension; close with a brief reminder that an unflagged sentence is not a good sentence — the skill only finds outliers.
- **`reporting-guideline-compliance`**
  - `terse` — Open with one line ("running reporting-guideline-compliance against <checklist> <version>"); emit the markdown report; no closing summary.
  - `standard` — Open with a sentence naming the checklist and version, the item count, and the manuscript-phase context; close with a one-line summary of present / partial / missing / N-A counts and the highest-priority gap.
  - `full` — Open with what reporting guidelines do (minimum-information standards so reviewers and readers can evaluate methodology consistently — the EQUATOR Network registry of ~600 active guidelines), what this audit produces (per-item present / partial / missing / N-A with a quoted anchor or explicit gap), and how to read it (act on missing first, then partial; N/A is not a gap; the audit does not invent prose to fill gaps).
- **`reporting-guideline-fit`**
  - `terse` — Open with one line ("running reporting-guideline-fit inference"); emit the markdown report; no closing summary.
  - `standard` — Open with one sentence naming the methods-section signal strength (clear / moderately clear / sketchy) and the count of applicable checklists; close with the recommended next step (the matching reporting-guideline-compliance run).
  - `full` — Open with what reporting guidelines do (standardise reporting so reviewers and readers can evaluate methodology consistently — the EQUATOR Network registry of ~500 active guidelines), why the inference matters (authors often don't know which checklist applies to their study design, especially across the AI-extension landscape), and the major design-to-checklist mapping.
- **`reviewer-simulation`**
  - `terse` — Open with one line ("running reviewer simulation across four lenses"); emit the markdown report; no closing summary. Returns one or two critiques per lens.
  - `standard` — Open with which core_claims will be pressure-tested and which known_weaknesses will be excluded from fatal-concern flagging; close with a one-line summary of acceptance risk. The full six-section per-lens output (Major / Minor / Fatal / Enthusiasm / Suggested Revisions / Acceptance Risk).
  - `full` — Open with what each lens is looking for and why Bornmann's low inter-reviewer agreement motivates the multi-lens approach (the surprising design choice authors most often ask about); close with which critiques to address first and which are framing-only. Adds per-critique rationale and reviewer-archetype grounding.
- **`terminology-normalization`**
  - `terse` — Open with a one-line "running terminology normalization"; emit the markdown report; no closing summary.
  - `standard` — Open with a sentence naming the manuscript and the declared terminology counts (e.g. "5 preferred terms, 3 forbidden, 2 synonym mappings"); close with a one-line summary of the findings.
  - `full` — Open with what this skill produces (preferred-term drift, forbidden-term occurrences, undeclared variants, suggested normalizations) and how to read it (which sections are enforcement, which are questions for the author); close with which findings to act on first and which are informational.
- **`tour`**
  - `terse` — tour ignores the saved level and always runs at full; truncating an onboarding tour defeats its purpose. A returning user is detected from MANUSCRIPT_STATE.yaml presence and tour skips to the relevant subset rather than truncating prose.
  - `standard` — Same as terse — tour always runs at full regardless of the saved level. The level still gets mentioned to the user as one of the things scriptorium will ask about during init.
  - `full` — tour's native level. Three or four turns: greet, ask what the user is working on, walk through the relevant subset of scriptorium, show an example MANUSCRIPT_STATE.yaml, end with one concrete next move (usually scriptorium:init).
- **`venue-fit`**
  - `terse` — Open with one line ("running venue-fit"); emit the markdown report; no closing summary beyond the report itself.
  - `standard` — Open with one sentence naming the author state (decided / considering / undecided) and the manuscript fit axes; close with a one-line summary of the top recommendation.
  - `full` — Open with what venue-fit is doing (scope / audience / methodological / novelty / significance / OA assessment per axis; not a probability estimate) and why the tier structure matters (most authors over-aim; tiered output saves time); close with which tier the author should consider first and why.
<!-- GENERATED:guidance-level-skills:end -->

The mapping is: *terse filters, standard is the default complete
list, full adds explanatory framing on top of the standard list*.
Two skills — `init` and `tour` — always run at `full` regardless
of the saved preference, because both exist to orient the author
and truncating that orientation defeats the point.

## Related

- [Start here](/concepts/start-here/) — the conceptual map this
  field is one branch of.
- [Declared-work scope](/concepts/declared-work-scope/) — the
  sister convention controlling *where* scriptorium operates;
  this page controls *how* it talks when it does.
- [Schema reference](/reference/manuscript-state-schema/) —
  `meta.guidance_level` in the canonical schema.
- [`knowledge/conventions/guidance-level`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/guidance-level.md)
  — the full convention note.
