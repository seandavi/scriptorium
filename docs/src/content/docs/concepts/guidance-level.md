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
The four skills where the field most visibly changes behaviour:

- **`init`** — the only skill that actively elicits the preference
  on first run. At `full` the conversation includes orientation,
  per-field rationale, and an end-of-phase recap. At `terse` it
  is purely questions and confirmations. At `standard` it
  includes a one-line "why" only on non-obvious fields.
- **`citation-audit`** — at `terse`, surfaces only the
  highest-priority claim-citation mismatches. At `standard`, the
  full table with per-claim rationale. At `full`, the standard
  table plus per-claim grounding citations to the relevant
  knowledge notes.
- **`reviewer-simulation`** — at `terse`, returns one or two
  critiques per lens. At `standard`, the full six-section
  per-lens output (Major / Minor / Fatal / Enthusiasm / Suggested
  Revisions / Acceptance Risk). At `full`, the standard output
  plus per-critique rationale and reviewer-archetype grounding.
- **`gap-finder`** — at `terse`, the top three to five anchored
  gaps. At `standard`, the full anchored list. At `full`, the
  full list plus per-gap search strategies the author can run.

The mapping is: *terse filters, standard is the default complete
list, full adds explanatory framing on top of the standard list*.

Skills that do not conversational-elicit input (`tour`,
`outlier-sentence-detector`, `terminology-normalization`) still
read the level for output verbosity, but the level's effect is
smaller because there is no question-and-answer surface to frame.

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
