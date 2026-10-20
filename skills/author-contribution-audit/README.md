# author-contribution-audit — ICMJE + CRediT audit of the Author Contributions section

Audits the manuscript's Author Contributions section against the
two converged standards — **ICMJE's four authorship criteria** and
**CRediT's 14 contributor roles** — and emits soft recommendations
the author can apply. When `project.target_venue` is set, also
compares against journal-specific variants (NEJM, Nature, JAMA,
Cell Press, PLOS, eLife each have small variants on top of the
baseline).

Operates on declared prose — the Author Contributions section
where it lives in the manuscript. **Does not duplicate authorship
data in `MANUSCRIPT_STATE.yaml`** (the schema deliberately omits
a `contributors:` field; declared prose lives in the manuscript,
not in state).

## When to invoke

- The author asks for a contributions check.
- Pre-submission verification that the section meets the venue's
  requirements.
- After ICMJE-relevant changes (added or removed authors, changed
  contribution patterns, drafted contributions for a new
  collaborator).

## What it explicitly will not do

- Auto-write or rewrite the Author Contributions section.
- Fabricate CRediT mappings without author input — asks rather
  than guesses. This is a fixed accuracy guard
  (`no-invented-manuscript-facts`).
- Duplicate authorship data in MANUSCRIPT_STATE.yaml.
- Verify truthfulness of contributions — the author team owns
  ground truth; the skill audits how contributions are
  documented.

## What it declines or asks about by default

These are guards the author can override for one run, or for the
project under `meta.overrides` in `MANUSCRIPT_STATE.yaml` (see
[`knowledge/conventions/author-authority.md`](../../knowledge/conventions/author-authority.md)).
The skill states the concern in one line each time, and a report
produced past one carries an `Overrides applied:` line.

- Adjudicate authorship disputes (`authorship-dispute-adjudication`;
  ICMJE criteria are the framework; whether to add or remove an
  author is the author team's decision). On override, a
  conditional reading of the documented text only.
- Recommend listing or keeping LLMs / chatbots / AI tools as
  authors (`llm-authorship`; per ICMJE 2023 and aligned
  major-journal policies). Refused by default; the finding is
  always reported.
- Operate on outline-phase manuscripts (`outline-phase`).
- Editorial-side use (`editorial-side-use`): asked, not refused,
  when the user is a reviewer or editor of a submitted manuscript.

## The three states

The skill detects the section's state and adapts:

- **Section present** — per-author audit against ICMJE four
  criteria + CRediT 14-role coverage; ghost / honorary / LLM-
  as-author signal detection.
- **Section absent** — flag the absence; suggest a CRediT-shaped
  skeleton (template, not populated mapping).
- **Section sketchy / incomplete** — per-author, list what's
  missing or under-documented; suggest candidate CRediT roles
  phrased as "consider whether Author X should claim Y if they
  did Z".

## Grounding

Primarily grounded in
[`knowledge/peer-review/credit-taxonomy-authorship.md`](../../knowledge/peer-review/credit-taxonomy-authorship.md)
— CRediT's 14 roles (Brand et al. 2015), ICMJE's four authorship
criteria, the Wislar et al. 2011 *BMJ* prevalence data (21% of
papers at top medical journals had honorary or ghost authorship),
the ICMJE 2023 LLM-as-author policy update, and the ICMJE
AI-disclosure rules (May 2023 and January 2024, consolidated into
Section V in January 2026).

Field-convention handling (biomedicine first/last; math
alphabetical; CS contribution-based; particle physics
hyperauthorship) is in the same note's "Authorship order by
field" section.

## See also

- [`SKILL.md`](SKILL.md) — full Claude Code skill (operational
  protocol, output template, hard constraints).
- [`prompt.md`](prompt.md) — platform-neutral version.
- [`manifest.yaml`](manifest.yaml) — machine-readable metadata.
- `/scriptorium:reviewer-simulation` — natural pair before
  submission; reviewers check authorship structure as part of
  triage.
- `/scriptorium:desk-rejection-risk` — natural pair when
  `target_venue` is set; some venues have authorship-structure
  desk-rejection triggers.
- `/scriptorium:explain author-contribution-audit` — full design
  tour.
