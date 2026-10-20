# gap-finder — collaborative gap identification with search-strategy directions

Identifies gaps in *existing draft prose* — claims under-supported,
premises missing, related work not engaged with, counterarguments
not addressed, internal-consistency mismatches across sections —
and suggests directions for filling them as pasteable search
strategies (never invented citations).

Critique category. Collaborative shape, not adversarial: findings
are framed as opportunities to strengthen, not deficiencies to
defend against. Distinct from `reviewer-simulation` (which is
adversarial by design) and complementary to it.

## When to invoke

- Author explicitly asks "what's missing here?" / "what gaps
  are there?" / "what's the discussion not engaging with?" on
  a manuscript at draft phase or later.
- Author has a focus question and a section to scan.

## When this skill declines by default

These are scope guards: the skill states the concern and declines
unless the author overrides it (see
[Guards and overrides](#guards-and-overrides)).

- `document_phase.current = outline` — no declared prose to
  anchor findings against (`outline-phase`).
- The user's question implies operating on prose that doesn't
  exist yet ("what should the related work section say" when
  there's no related work section). The author owns the
  proposer step (`generation-from-blankness`,
  `pre-declaration-ideation`).

Without a focus question on a long manuscript, the skill asks one
clarifying question rather than producing exhaustive output.

## What it explicitly will not do

- Invent specific citations. Suggested directions are search
  strategies, never citations from model memory. This is fixed.
- By default: draft prose to fill any gap (per
  declared-work-scope), operate on outline-phase or
  pre-declaration questions, or name papers the manuscript does
  not cite. The author can override each.
- Produce findings without manuscript-passage anchors.
- Produce critique-shaped findings (that's
  `reviewer-simulation`'s job).
- Auto-invoke other skills.

## Guards and overrides

The skill declares its guards in [`manifest.yaml`](manifest.yaml),
following the
[`author-authority`](../../knowledge/conventions/author-authority.md)
convention. The scope guards are defaults. The author overrides one
for a single run by answering "proceed", or for the project with an
entry under `meta.overrides` in `MANUSCRIPT_STATE.yaml`:

- `outline-phase` — scans the outline; findings anchor in outline
  entries.
- `generation-from-blankness` — drafts only from declared
  `core_claims` and the author's stub text, with no citations.
- `pre-declaration-ideation` — offers directions anchored to
  declared `core_claims` for the author to choose from.
- `citation-recommendations` — names only works resolved against
  Crossref or PubMed in that session, as works to read.

The accuracy guard `no-parametric-citations` is fixed: no override
lifts it. When a run proceeds past a scope guard, the report opens
with `Overrides applied: <guard ids>`.

## The seven gap categories

A scriptorium adaptation: five categories adapted from Miles (2017;
Adu & Miles 2023), plus two manuscript-internal additions
(counterargument, internal-consistency), with realist-synthesis /
PRISMA-ScR framing. Robinson et al. (2011) reason codes are
available as an evidence-gap sub-tag:

1. Literature gap
2. Evidence gap
3. Methodological gap (PRISMA-ScR PCC framing where relevant)
4. Population gap
5. Translation gap
6. Counterargument gap (realist-synthesis MCO framing)
7. Internal-consistency gap (cross-section)

The output organises findings by category. Empty categories are
declared explicitly — silence is indistinguishable from
"didn't check".

## See also

- [`SKILL.md`](SKILL.md) — full Claude Code skill (operational
  protocol, output template, hard constraints).
- [`prompt.md`](prompt.md) — platform-neutral version.
- [`manifest.yaml`](manifest.yaml) — machine-readable metadata.
- `/scriptorium:citation-audit` — natural pair when gap-finder
  surfaces evidence gaps; pressure-test existing citations.
- `/scriptorium:reviewer-simulation` — natural pair when
  gap-finder surfaces counterargument gaps; reviewers will
  catch them too.
- `/scriptorium:argumentative-flow` — natural pair when
  gap-finder surfaces internal-consistency gaps.
- `/scriptorium:explain gap-finder` — full design tour.
