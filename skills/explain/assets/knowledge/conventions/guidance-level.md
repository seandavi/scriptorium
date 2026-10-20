# Guidance level: how much framing each skill adds around its work

*Last updated: 2026-05-20*

## Synthesis

Scriptorium's skills walk an author through structured editorial work
— populating shared state, auditing citations, simulating reviewers,
restructuring argument. A first-time user benefits from each skill
explaining *why* it asks what it asks, so they learn the workflow as
they go; a user on their fifth manuscript finds the same prose
patronising and slow. The cost of guessing wrong is real in both
directions: under-framed scriptorium feels like an interrogation,
over-framed scriptorium feels like a seminar the user didn't sign up
for.

The convention is to let the author pick once, persist the choice in
`MANUSCRIPT_STATE.yaml`, and let every skill read it. The author can
change it at any time by editing the YAML or saying so mid-flight.
Skills also watch for signal that the level is mis-set and offer a
gentle correction once per session if so.

This is not an evidence-based knowledge note — it documents a
scriptorium-side convention, not a finding from the literature. It
lives here because every skill grounds in it and updates should
propagate consistently.

## The three levels

The schema field is `meta.guidance_level` and has three values:

### `terse`

Questions and confirmations only. No prose between turns. The skill
behaves like a competent assistant who knows you already know what
you're doing.

```text
Author: /scriptorium:init
Skill:  Title from paper.qmd? "Effects of dietary X on Y in mice"
Author: yes
Skill:  target_type: manuscript?
Author: yes
Skill:  core_claims — list them:
```

Best for: authors on their second-or-later scriptorium project, or
authors who prefer to read documentation themselves rather than have
each skill walk them through it inline.

### `standard` *(default when unset)*

Brief one-line "why" before non-obvious questions; no upfront
roadmap, no end-of-phase recaps.

```text
Skill:  core_claims — these are what reviewer-simulation tests
        against. List the load-bearing arguments your abstract
        commits to.
Author: ...
```

Best for: returning users who don't need orientation but appreciate a
short anchor when a question's purpose isn't self-evident. This is
the safe default when `meta.guidance_level` is absent.

### `full`

The complete experience. Upfront orientation when the skill starts;
2-3 sentence "why this matters / how to think about answering" before
each elicited field; end-of-phase recap so the author can see where
they are in the arc.

The framing is deliberately educational. The `full` level treats
each skill invocation as an opportunity for the author to learn the
workflow alongside doing it — not as a lecture, but as just-in-time
context that builds a mental model of how scriptorium uses each
field. By the end of a manuscript at `full`, an author has been
taught what `core_claims` is for, why `known_weaknesses` matters at
review time, how `reviewer-simulation` consumes the state, and so
on. They've earned the right to drop to `standard` on their next
project.

```text
Skill:  Before we start, here's the plan. We'll populate one YAML
        file that every other skill reads. About half is inferable
        from your files; the other half I'll ask you about. You can
        stop at any point — only title, target type, and phase are
        required. Ready?

        ...

Skill:  core_claims — what is this paper arguing? Reviewer-simulation
        literally tests whether your prose supports each one, so the
        specificity here directly controls the sharpness of later
        critiques. List the 2-4 things a reader of just your abstract
        should walk away believing. "We characterise X" is too vague;
        "X is required for Y in Z" is the right grain.
Author: ...
```

Best for: first-time scriptorium users; authors who want to
*learn* how scriptorium uses each field as they fill it in; users
running an unfamiliar skill they haven't invoked before and who'd
rather understand it than read the SKILL.md cold. Most users will
spend their first manuscript here and drop to `standard` afterward;
some will stay at `full` indefinitely because they like the
just-in-time framing.

## The check-in protocol

Skills should not interrogate the author about their preference every
session. The protocol:

1. **At skill entry**, read `meta.guidance_level`. If absent, default
   to `standard`. Adapt the conversation accordingly.
2. **Watch for signal during the session.**
   - Toward `full`: the author asks "what does X mean?" or "why
     does this matter?" twice or more about scriptorium concepts they
     should already know.
   - Toward `terse`: the author says some variant of "skip the
     explanation", "I know", "just ask the question", or
     consistently provides one-word answers that suggest the prose
     framing isn't earning its space.
3. **Offer once at the first natural phase boundary** if a strong
   signal fired. *"You've asked a few clarifying questions — want me
   to switch to `full`? It adds a short rationale before each field
   so the workflow gets explained as you go."* Or: *"You're moving
   fast — want me to drop to `terse`? Just the questions, no
   preface."* If accepted, update `meta.guidance_level` in the YAML.
4. **Never repeat the offer in the same session.** If the author
   declines, respect that for the rest of the session.
5. **A direct mid-flight command always wins.** *"Switch to terse"*
   should take immediate effect and update the YAML.

## Implementation priority for scriptorium

**Verdict:** Adopt in every skill that elicits author input or runs
multi-turn conversations. The four v0.1 skills (`init`,
`citation-audit`, `reviewer-simulation`, `argumentative-flow`) all
qualify; `scriptorium:explain` does too. Pure CLI subcommands
(`scriptorium validate`, `prompt-pack`, `list`, `trace`) do not
qualify — they have no conversation to adapt.

**How a skill adopts it:**

1. Add `knowledge/conventions/guidance-level.md` to the skill's
   `grounding:` list in `SKILL.md`.
2. In the skill's operational protocol, after reading
   `MANUSCRIPT_STATE.yaml`, read `meta.guidance_level` and adapt the
   conversation:
   - `terse` → suppress all explanatory prose; ask questions, accept
     confirmations.
   - `standard` → one-line context where the question isn't
     self-explanatory; otherwise terse.
   - `full` → orientation turn, 2-3 sentence rationale per elicited
     field, end-of-phase recap. The framing is the level's *teaching
     surface* — its job is to let the author learn the workflow
     while doing it.
3. Run the check-in protocol above.

**What this is not:** This is not a verbosity slider. The
*information density* of a skill's output should not change with
guidance level — `citation-audit` still produces the same structured
claim-by-claim assessment regardless of level. What changes is the
framing and explanatory prose around the structured work.

## Cross-references

- `schemas/manuscript-state.schema.json` — canonical enum and
  default.
- `templates/MANUSCRIPT_STATE.yaml` — commented `meta:` block author
  can uncomment to set the preference manually.
- `skills/init/SKILL.md` — the skill that elicits the preference on
  first run.
- `skills/explain/SKILL.md` — companion skill users at the `full`
  level are nudged toward for any unfamiliar skill they're about to
  invoke.
