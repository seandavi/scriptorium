# Author authority: who decides what a skill may do

*Last updated: 2026-10-20*

## Synthesis

The author decides what scriptorium's skills may do and where they
apply. A skill that declines on a funder's or publisher's policy, or
because the request falls outside the
[[declared-work-scope]] convention, is making a call that belongs to
the author: they know their circumstances, and they carry the
responsibility for the submitted work. Those refusals are therefore
**defaults the author can override**, not rules the skill enforces.

One class of refusal is different. Some guards exist because the skill
would otherwise produce *wrong output*: an invented citation, an
altered statistic, a claim to have read a paper it never saw.
Overriding such a guard does not give the author a riskier choice; it
gives them a false result. These **accuracy guards** stay fixed.

This note defines the mechanism every skill shares: guards declared in
each skill's `manifest.yaml`, project-level overrides in
`MANUSCRIPT_STATE.yaml` under `meta.overrides`, the precedence between
them, and the "Overrides applied" line a skill writes when it proceeds
under an override. Like [[guidance-level]], it documents a
scriptorium-side convention rather than a finding from the literature.

## Evidence and frameworks

### Accountability sits with the author

ICMJE's fourth authorship criterion is "agreement to be accountable
for all aspects of the work in ensuring that questions related to the
accuracy or integrity of any part of the work are appropriately
investigated and resolved" [1]. ICMJE's recommendations also make AI
tools ineligible for authorship and ask authors to disclose their use
[2]; [[credit-taxonomy-authorship]] covers the detail. Accountability
and the decision travel together. A tool that refuses on its own reading
of a policy takes a decision away from the person who answers for it,
without taking on any of the accountability.

### Policy guards rest on interpretation

Funder and publisher rules are real constraints, but how they apply to
a given request is usually a judgement. NIH NOT-OD-25-132 says NIH
"will not consider applications that are either substantially
developed by AI, or contain sections substantially developed by AI, to
be original ideas of applicants" [3]. The notice does not define
"substantially" ([[nih-significance-patterns]]). Whether a particular
use crosses that line depends on facts the author has and the skill
does not: what the author has already written, how the output will be
used, what their institution advises. The skill's job is to state the
concern and its source, so the author decides informed. It is not the
skill's job to settle the reading for them.

### Scope guards are a structural default

[[declared-work-scope]] sets where scriptorium operates: on prose the
author has written or scaffolding they have declared. That cut is
argued from Hayes' writing model and the failure modes of blank-slate
generation, and it remains the default. The note anticipated that an
author might explicitly invite help beyond the boundary; this
convention is how they do so.

### Accuracy guards protect correctness, not caution

The accuracy guards defend against failure modes that make output
false regardless of who asked for it. LLMs fabricate references
([[hallucination-in-llm-citations]]). Embedding similarity misses
negation and number changes, so a transformation can flip meaning
without detection ([[semantic-preservation]]). LLMs are unreliable at
recomputing test statistics ([[statistical-inconsistency]]). An author
can reasonably accept a policy risk or step outside the default scope.
No author circumstance makes an invented citation real, so an override
there would only change whether the error ships.

## How this informs scriptorium

### The three guard kinds

| Kind | What it protects | Default | Author can override? |
|---|---|---|---|
| `policy` | Compliance with a funder's or publisher's rule | `ask` or `refuse` | Yes |
| `scope` | The [[declared-work-scope]] boundary | `refuse` | Yes |
| `accuracy` | Correctness of the output itself | `refuse` | No |

A guard is classified `accuracy` only when overriding it would make
the output wrong. A guard that makes the output riskier, less
conventional, or less likely to be accepted is `policy` or `scope`.

### Declaring a guard

Each skill lists its guards in `skills/<name>/manifest.yaml`:

```yaml
guards:
  - id: nih-application-prose      # kebab-case
    kind: policy                   # policy | scope | accuracy
    summary: "One line the skill shows the author"
    source: "NIH NOT-OD-25-132"    # required for policy; the convention note for scope
    default: ask                   # ask | refuse; accuracy guards are always refuse
```

One id means one guard. Several skills may declare the same id (a
scope guard several skills share, say), but only with an identical
definition: the same `kind`, `summary`, `source` and `default`
everywhere. A manifest may not declare the same id twice.

### Overriding a guard for a project

The author records standing overrides in `MANUSCRIPT_STATE.yaml`:

```yaml
meta:
  overrides:
    - guard: nih-application-prose
      skills: [specific-aims]      # or ["*"] for every skill that declares the guard
      note: "free text from the author (optional)"
```

`skills` names the skills the override applies to; `"*"` matches every
skill that declares the guard. `note` is for the author's own record
and is not interpreted.

### What a guard does when it fires

- **`ask`.** The skill states the concern and its source in one line,
  then asks the author whether to proceed.
- **`refuse`.** The skill declines by default. It states the concern
  and its source, and tells the author how to override: answer in this
  run, or add an entry under `meta.overrides`.

The statement of the concern is one line at every
[[guidance-level]], including `terse`. Guidance level changes the
framing around a skill's work, not whether the author is told about a
guard.

### Precedence

For a non-accuracy guard, the first of these that applies decides:

1. **A per-run answer.** What the author says in this run wins in
   either direction. They can proceed past a guard whose default is
   `refuse`, or decline to proceed even though `meta.overrides` lists
   the guard.
2. **`meta.overrides`.** An entry naming the guard and this skill (or
   `"*"`) means the skill proceeds without asking.
3. **The guard's `default`.**

An override never suppresses the one-line statement of the concern.
The author who set the override still sees, each run, what it lets
through.

Accuracy guards sit outside this order. Neither a per-run answer nor
`meta.overrides` overrides them. When asked to, the skill says the
guard protects correctness and cannot be overridden.

### "Overrides applied"

A skill that proceeds past a guard, through a per-run answer or
`meta.overrides`, says so in its output with one line listing the
guard ids:

```text
Overrides applied: nih-application-prose
```

The line is omitted when no override was applied. It makes the output
self-describing. A co-author or reviewer reading it later can see
which guards the author chose to proceed past without reconstructing
the conversation.

### Validation

`scriptorium validate` checks `meta.overrides` against the guards the
bundled skills declare. It reports an error for:

- an override naming a guard id no skill declares;
- an override naming a `kind: accuracy` guard;
- an override listing a skill that does not declare the guard.

`"*"` with an unknown guard id is the same unknown-id error. The
schema itself (`schemas/manuscript-state.schema.json`) checks the
shape of each entry.

## Implementation priority for scriptorium

**Verdict:** Yes (next release). The shared mechanism (this note, the
`meta.overrides` schema, the manifest `guards:` registry and the
`validate` cross-checks) lands first (#157). Skills adopt it after
that (#158).

**How a skill adopts it:**

1. Add `knowledge/conventions/author-authority.md` to the skill's
   `grounding:` list in `SKILL.md`.
2. Declare each guard the skill applies under `guards:` in its
   `manifest.yaml`, classified by the table above. Refusals from
   [[declared-work-scope]] become `kind: scope` guards with
   `default: refuse`.
3. In the operational protocol, read `meta.overrides` alongside the
   rest of `MANUSCRIPT_STATE.yaml` and apply the precedence above when
   a guard fires.
4. When the skill proceeds past any guard, write the "Overrides
   applied" line in its output.

**What this is not:** This is not a way to switch skills off or to
loosen accuracy. It moves policy and scope decisions to the author
and keeps the author informed each time one of them is exercised.

## Open questions / weak evidence

- **Classification at the margin.** Some guards mix kinds. For
  example, "never present generated NIH prose as ready to submit" is
  partly policy and partly accuracy, because unlabelled output
  misrepresents where the prose came from. A borderline guard should
  be split into a fixed accuracy part and an overridable policy part
  rather than forced into one kind.
- **Persisting per-run answers.** This convention does not say
  whether a skill should offer to record a per-run answer under
  `meta.overrides`. It is left to experience with converted skills.
- **Policy drift.** A policy guard's `source` names the notice or rule
  it rests on. When the rule changes, the guard needs updating; the
  manifest does not record the date a source was last checked.

## References

[1] International Committee of Medical Journal Editors. *Defining
the Role of Authors and Contributors*.
<https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html>.
The four authorship criteria are quoted in
[[credit-taxonomy-authorship]].

[2] International Committee of Medical Journal Editors.
*Recommendations for the Conduct, Reporting, Editing, and Publication
of Scholarly Work in Medical Journals*, updated May 2023 (AI
authorship guidance) and January 2026 (Section V, "Use of Artificial
Intelligence in Publishing").
<https://www.icmje.org/news-and-editorials/updated_recommendations_may2023.html>;
<https://www.icmje.org/news-and-editorials/updated_recommendations_jan2026.html>.

[3] NIH. NOT-OD-25-132: Supporting Fairness and Originality in NIH
Research Applications. Released July 17, 2025; effective for
applications submitted to the September 25, 2025 receipt date and
beyond. <https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html>

## Cross-references

- [[declared-work-scope]] — the scope convention whose refusals are
  `kind: scope` guards with `default: refuse`.
- [[guidance-level]] — controls framing; the one-line concern
  statement appears at every level.
- [[credit-taxonomy-authorship]] — ICMJE accountability and AI
  disclosure.
- [[nih-significance-patterns]] — NOT-OD-25-132, the source of the
  first policy guard.
- [[hallucination-in-llm-citations]], [[semantic-preservation]],
  [[statistical-inconsistency]] — failure modes behind the accuracy
  guards.
- `schemas/manuscript-state.schema.json` — the `meta.overrides`
  definition.
- `templates/MANUSCRIPT_STATE.yaml` — commented `meta.overrides`
  example.
