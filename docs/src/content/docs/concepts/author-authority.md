---
title: Author authority
description: Which skill refusals are defaults the author can override, which are fixed, how to override, and how a skill reports that it did.
sidebar:
  order: 14
---

Scriptorium's skills ship with defaults. By default they decline to
generate from a blank page, and they decline or ask before uses that
a funder's or publisher's AI policy restricts. Those defaults are the
author's to change. Each one is a declared **guard**, and the author
can override any policy or scope guard, for one run or for the whole
project. The author cannot override an accuracy guard.

This page is the author-facing summary. The full convention, with its
evidence and open questions, is
[`knowledge/conventions/author-authority`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/author-authority.md).

## What you can override, and what you can't

Every guard has one of three kinds.

| Kind | What it protects | Default | Can the author override it? |
|---|---|---|---|
| `policy` | Compliance with a funder's or publisher's rule | `ask` or `refuse` | Yes |
| `scope` | The [declared-work scope](/concepts/declared-work-scope/) boundary | `refuse` | Yes |
| `accuracy` | Correctness of the output itself | `refuse` | No |

**Policy and scope guards are overridable** because they are
judgements that belong to the author. ICMJE holds authors accountable
for every part of the work, so the decision sits with the person who
answers for it. How a policy applies to a given request usually turns
on facts the author has and the skill does not: what they have
already written, how the output will be used, what their institution
advises. The skill states the concern and its source; the author
decides. Scope guards encode the declared-work boundary, which is a
structural default rather than a rule anyone else imposes.

**Accuracy guards are fixed** because overriding one would not give
the author a riskier choice. It would give them a false result: an
invented citation, an altered statistic, a claim to have checked a
paper or figure the skill never saw. No author circumstance makes an
invented citation real. A guard is classed `accuracy` only when
overriding it would make the output wrong. A guard that makes the
output riskier, less conventional or less likely to be accepted is
`policy` or `scope`.

## What a guard does when it fires

- **`ask`.** The skill states the concern and its source in one line,
  then asks whether to proceed.
- **`refuse`.** The skill declines by default. It states the concern
  and its source, and says how to override: answer in this run, or
  add an entry under `meta.overrides`.

The one-line statement of the concern appears at every
[guidance level](/concepts/guidance-level/), including `terse`, and
an override never suppresses it. The author who set an override still
sees, each run, what it lets through.

## How to override

### For one run

Answer the skill. When a guard fires, tell the skill to proceed (or,
for an `ask` guard, answer yes). The answer applies to that run only.

### For the project

Record standing overrides in `MANUSCRIPT_STATE.yaml` under
`meta.overrides`. Each entry names a guard and the skills it applies
to; `"*"` means every skill that declares the guard. `note` is
optional free text for your own record; skills don't interpret it.

```yaml
project:
  title: "Working title"
  target_type: manuscript
document_phase:
  current: draft
meta:
  overrides:
    - guard: citation-recommendations
      skills: [citation-audit, gap-finder]
      note: "Name verified papers for unsupported claims; I decide what to cite."
    - guard: figure-image-reading
      skills: [figure-text-alignment]
    - guard: outline-phase
      skills: ["*"]
```

`scriptorium validate MANUSCRIPT_STATE.yaml` accepts this file. Under
these overrides:

- `citation-audit` and `gap-finder` may name papers, but only works
  they resolved against Crossref or PubMed in that session. The
  `no-parametric-citations` accuracy guard still applies, so nothing
  comes from model memory.
- `figure-text-alignment` reads figure images and labels every
  image-derived finding "unvalidated vision". The
  `no-image-integrity-claims` accuracy guard still applies.
- Every skill that declares `outline-phase` runs on an outline-phase
  manuscript instead of declining.

The guard ids each skill declares are in the
[table below](#guards-by-skill).

## Precedence

For a policy or scope guard, the first of these that applies decides:

1. **A per-run answer.** What you say in this run wins in either
   direction. You can proceed past a guard whose default is `refuse`,
   or decline to proceed even though `meta.overrides` lists the guard.
2. **`meta.overrides`.** An entry naming the guard and this skill (or
   `"*"`) means the skill proceeds without asking.
3. **The guard's `default`.**

Accuracy guards sit outside this order. Neither a per-run answer nor
`meta.overrides` overrides them. Asked to, the skill says the guard
protects correctness and cannot be overridden.

## "Overrides applied"

A skill that proceeds past any guard, through a per-run answer or
`meta.overrides`, writes one line in its output, directly under the
report title, listing the guard ids:

```text
Overrides applied: citation-recommendations, outline-phase
```

The line lists every guard the skill proceeded past in that run,
including an `ask` guard you answered yes to. It is omitted when no
override applied. It makes the report self-describing: a co-author or
reviewer reading it later can see which guards were set aside without
reconstructing the conversation.

## What `validate` rejects

`scriptorium validate` checks `meta.overrides` against the guards the
bundled skills declare in their `manifest.yaml`. It reports an error,
and exits non-zero, for:

- a guard id no bundled skill declares (also when `skills` is `"*"`);
- a guard of kind `accuracy`;
- a skill listed in `skills` that does not declare the guard.

For example, this file is rejected with three errors:

```yaml
project:
  title: "Working title"
  target_type: manuscript
document_phase:
  current: draft
meta:
  overrides:
    - guard: no-parametric-citations
      skills: [citation-audit]
    - guard: figure-image-reading
      skills: [reporting-guideline-fit]
    - guard: nih-application-prose
      skills: [specific-aims]
```

```text
  meta/overrides/0: guard 'no-parametric-citations' is an accuracy guard and cannot be overridden
  meta/overrides/1: skill 'reporting-guideline-fit' does not declare guard 'figure-image-reading' (declared by: figure-text-alignment)
  meta/overrides/2: unknown guard 'nih-application-prose': no bundled skill declares it
```

The third entry is the example in the `MANUSCRIPT_STATE.yaml`
template. `nih-application-prose` belongs to the planned
`specific-aims` skill (see the [roadmap](/roadmap/)), so `validate`
rejects it until that skill ships. The JSON Schema separately checks
the shape of each entry: `guard` and `skills` are required, ids are
kebab-case, and no other keys are allowed. See the
[schema reference](/reference/manuscript-state-schema/#metaoverrides).

## Guards by skill

The table is generated from the `guards:` list in each skill's
`manifest.yaml` at docs-build time, so it matches what the skills
declare. A guard id shared by several skills has the same definition
in each. `explain`, `init` and `tour` declare no guards.

<!-- GENERATED:author-authority-guards:start -->
<!-- GENERATED:author-authority-guards:end -->

## Related

- [Declared-work scope](/concepts/declared-work-scope/): the boundary
  the scope guards encode.
- [Guidance level](/concepts/guidance-level/): changes the framing
  around a skill's work, never whether a guard's concern is stated.
- [Schema reference](/reference/manuscript-state-schema/): the
  `meta.overrides` field.
- [Glossary](/concepts/glossary/): guard, override, accuracy guard.
- [`knowledge/conventions/author-authority`](https://github.com/seandavi/scriptorium/blob/main/knowledge/conventions/author-authority.md):
  the full convention.
