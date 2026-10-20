# venue-fit — author-side venue recommendation with preprint mode

Tiered venue recommendation (`Likely fit` / `Stretch` / `Probably
premature`) with per-axis fit reasoning, explicit predatory-venue
refusal, opt-in preprint server + pre/post-publication review
platform suggestions, and optional bias-managed calibration via
author publication history.

## When to invoke

- The author is choosing where to submit and wants a tiered
  recommendation grounded in declared work.
- The author has a venue in mind and wants to pressure-test the
  choice ("is this the right home for this paper?").
- The author is undecided and wants `candidate_venues` populated.

## The three author states

The skill detects the state from `MANUSCRIPT_STATE.yaml`:

- **Decided** (`project.target_venue` set) — assesses the
  declared venue; offers 1-3 alternatives if a fit mismatch
  surfaces.
- **Considering** (`project.candidate_venues` non-empty) —
  assesses each declared candidate; tiers them; surfaces
  additional candidates the author may not have listed.
- **Undecided** (both empty) — full open recommendation; offers
  to write the top tier to `project.candidate_venues` with
  explicit author confirmation.

## What this skill explicitly will not do

- Predict per-venue acceptance probabilities. The peer-review
  variance literature (Bornmann κ ≈ 0.17 inter-reviewer agreement)
  makes this indefensible. Tiers only.
- Include a predatory-flagged venue in any tier. The skill
  maintains a `## Predatory signals detected` section in every
  output, whether or not flags fired, so the check is visible.
- Judge predatory status at the publisher level. Per-journal
  judgments only (MDPI has both well-respected venues and venues
  with serious concerns).
- Generate a cover letter, auto-submit, or auto-write to
  `MANUSCRIPT_STATE.yaml` without explicit consent.
- Name a benchmark paper from memory. Benchmarks come from the
  manuscript's bibliography or are verified in the same session.

The probability, predatory-tier and benchmark rules are fixed
accuracy guards.

## What it declines or asks about by default

These are guards the author can override for one run, or for the
project under `meta.overrides` in `MANUSCRIPT_STATE.yaml` (see
[`knowledge/conventions/author-authority.md`](../../knowledge/conventions/author-authority.md)).
The skill states the concern in one line each time, and a report
produced past one carries an `Overrides applied:` line.

- Operate without `project.target_type`, or with it set to `other`
  (`target-type-required`). On override, generic manuscript logic.
- Operate on outline-phase manuscripts (`outline-phase`).
- Assess audience fit when `style.audience` is too broad
  (`audience-granularity-required`). On override, the audience
  axis is marked `cannot-assess`.
- Editor-side or reviewer-side assessment (`editorial-side-use`):
  asked, not refused, when the user is a reviewer or editor of a
  submitted manuscript. This is author-side decision support.

## Optional inputs

- **Author publication history** (ORCID / Google Scholar /
  declared past venues) — used as calibration of feasibility,
  not as a source for the recommendation list. The list comes
  from manuscript fit; history shifts which tier each candidate
  falls into. Authors can override ("ignore my history", "be
  ambitious", "be realistic").
- **Venue preferences** — open-access required, max APC,
  indexing requirements, preprint preference. Applied as hard
  filters before tiering when declared.
- **Funder constraints** — NIH / Wellcome / cOAlition S / HHMI /
  Gates requirements, including funder APC rules (Wellcome
  DOAJ-only, HHMI no hybrid, Gates none; NIH caps proposed, not
  finalised as of October 2026). Hard filters.

## Preprint mode

Preprint server + pre/post-publication review platform
recommendations are opt-in. If signals are unclear, the skill
asks once; if the author opts out, the section is suppressed
entirely. The exception is HHMI: for an original research article
that is a major contribution from a covered HHMI lab, preprinting
is required and the section is included, restricted to HHMI's
designated servers. A Gates-funded author gets a strong prompt,
not a requirement. When in scope, the skill names PCI, Review Commons,
F1000Research, and eLife's post-2022 reviewed-preprint model as
strategic alternatives to traditional pre-publication review —
a timing/transparency/community-signal decision, not a single
best answer.

## See also

- [`SKILL.md`](SKILL.md) — full Claude Code skill (frontmatter,
  protocol, output template).
- [`prompt.md`](prompt.md) — platform-neutral version.
- [`manifest.yaml`](manifest.yaml) — machine-readable metadata.
- `/scriptorium:desk-rejection-risk` — natural follow-on once a
  venue is chosen. Venue-fit recommends; desk-rejection-risk
  pressure-tests the choice.
- `/scriptorium:reviewer-simulation` — recommended before
  submitting to a `Stretch` venue.
- `/scriptorium:explain venue-fit` — full design tour.
