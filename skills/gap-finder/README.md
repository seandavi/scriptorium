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

## When this skill refuses (cleanly)

- `document_phase.current = outline` — no declared prose to
  anchor findings against.
- The user's question implies operating on prose that doesn't
  exist yet ("what should the related work section say" when
  there's no related work section). The author owns the
  proposer step.
- No focus question supplied on a long manuscript — the skill
  asks one clarifying question rather than producing exhaustive
  output.

## What it explicitly will not do

- Draft prose to fill any gap (per declared-work-scope).
- Invent specific citations. Suggested directions are search
  strategies, never `cite this paper`.
- Operate on outline-phase or pre-declaration questions.
- Produce findings without manuscript-passage anchors.
- Produce critique-shaped findings (that's
  `reviewer-simulation`'s job).
- Auto-invoke other skills.

## The seven gap categories

Robinson 2011 (AHRQ) taxonomy plus realist-synthesis / PRISMA-ScR
methodology:

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
