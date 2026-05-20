# tour — conversational onboarding for new users

The single skill a maintainer can point a new user at instead of
linking them to documentation. Three or four turns, no work,
ends with one concrete next move.

## When to invoke

- `/scriptorium:tour` — what someone runs the first time they
  try scriptorium. Designed to be pointed at: "install scriptorium
  and run `/scriptorium:tour`" is a single-line pitch a maintainer
  can drop in Slack or email.
- "What is scriptorium?" or "How do I get started?" — handle the
  question conversationally rather than linking to a doc.

## What it does

1. Greets and states what scriptorium is in one paragraph.
2. Asks what the user is working on (manuscript / grant / review /
   exploring).
3. Walks through the 3-4 skills that matter for their case, shows
   an example `MANUSCRIPT_STATE.yaml` excerpt, mentions guidance
   levels briefly.
4. Ends with one concrete next command (usually
   `/scriptorium:init <dir>`), not a menu.

## What it explicitly will not do

- Write any file (`MANUSCRIPT_STATE.yaml` or otherwise).
- Auto-invoke `init`, `citation-audit`, `reviewer-simulation`,
  `argumentative-flow`, or `explain`. Suggests only.
- Read manuscript prose, bibliography, or any file other than a
  detection-only check of `MANUSCRIPT_STATE.yaml` in the cwd.
- Run past four turns. Tour is short.

## Relation to `scriptorium:explain`

`tour` is interactive; `explain` is reference-shaped. The tour
suggests `explain` at the end for users who want to drill into a
specific skill. The two skills cover different use cases — keep
both.
