# Knowledge layer

The evidence base scriptorium's skills ground in. **The skills without
this layer are generic LLM prompts; with it, they are grounded in
established practice.**

## Why this layer exists

Most AI writing tools rely on the LLM's pretraining to "know" what good
scientific writing is. That works inconsistently and unaccountably.
Scriptorium takes the opposite approach: skills cite the specific
evidence they ground in, so a contributor or reviewer can trace any
behavior back to its source.

The cost is real work — building this evidence base took
[a substantial first-pass effort](#how-this-was-built) — but it
produces three durable benefits:

1. **Defensible design.** When someone asks "why does `citation-audit`
   classify claims this way?", the answer is a paper.
2. **Accountable evolution.** When the evidence updates, the skills
   should update. Knowledge documents declare their last-updated date.
3. **Honest scope.** Knowledge documents close with an
   *Implementation priority* section that states whether the finding
   becomes a skill or stays framing-only context. Findings that
   shouldn't become skills are explicit. Two notes don't have the
   section yet; see [Notes without a verdict](#notes-without-a-verdict).

## Layout

```text
knowledge/
├── prior-art/                # similar tools, projects, lineage (6 notes)
├── scientific-writing/       # methodology of good writing (14 notes)
├── peer-review/              # evidence on review processes (9 notes)
├── citations/                # citation practices and pitfalls (4 notes, 1 of them Quarto)
├── editing/                  # editing methodology (3 notes)
├── grants/                   # grant-writing evidence (3 notes)
├── critique-techniques/      # how to find problems systematically (7 notes)
├── reproducibility/          # the crisis context scriptorium responds to (1 note)
├── author-roles/             # career stage, role, and language behavioral evidence (2 notes)
└── conventions/              # the load-bearing conventions skills share (2 notes)
```

Current size: 51 notes (50 markdown + 1 Quarto), grown from the
first-pass batch of ~40. The October 2026 refresh re-verified existing
notes and added none. The most recent additions track v0.2 and v0.3
work:

- `knowledge/scientific-writing/promotional-register.md` — the default
  promotional-register catalog in `terminology-normalization`.
- `knowledge/scientific-writing/corpus-based-stylometry.md` — voice-profile design.
- `knowledge/scientific-writing/literature-search-strategies.md` — gap-finder.
- `knowledge/critique-techniques/research-gap-detection.md` — gap-finder.
- `knowledge/peer-review/venue-selection.md` — venue-fit.
- `knowledge/peer-review/predatory-publishing.md` — venue-fit refusal.
- `knowledge/peer-review/preprint-landscape.md` — venue-fit opt-in mode.
- `knowledge/author-roles/author-role-evidence.md` — persona / voice work.
- `knowledge/conventions/declared-work-scope.md` — the project-wide refusal-on-blankness convention.
- `knowledge/conventions/guidance-level.md` — the project-wide framing convention.

The two `conventions/` notes are project-wide rather than topical:
they define the [`declared-work-scope`](conventions/declared-work-scope.md)
refusal posture every skill inherits, and the
[`guidance-level`](conventions/guidance-level.md) framing every
conversation-bearing skill respects. Each is explained user-side in
its concept page
([declared-work-scope](../docs/src/content/docs/concepts/declared-work-scope.md)
and [guidance-level](../docs/src/content/docs/concepts/guidance-level.md));
the knowledge notes here are the underlying evidence record for those
conventions.

Each subdirectory has a consistent document structure:

```markdown
# Topic title

*Last updated: YYYY-MM-DD*

## Synthesis
(1–3 paragraphs — what the evidence shows)

## Evidence and frameworks
(Detailed treatment with citations)

## How this informs scriptorium
(Concrete connections to specific skills + MANUSCRIPT_STATE schema)

## Implementation priority for scriptorium
**Verdict:** Yes (v0.X) | Maybe later | No
**If Yes:** skill name, phase, scope, required data
**If Maybe later:** condition that would flip to Yes
**If No:** why this is useful context anyway

## Open questions / weak evidence

## References
(Numbered citations with DOIs/PMIDs/ISBNs)
```

## Citation discipline

- Real DOIs, PMIDs, ISBNs, arXiv IDs only.
- Unverified items may carry a `[TODO verify]` marker while a note is
  being drafted, but a note does not merge with any. Material that
  cannot be verified is left out, not fabricated.
- Where source language matters (Toulmin's argument model, Gopen & Swan's
  reader-expectation principles, Kerr's HARKing definition, etc.), the
  text is quoted directly.
- Each document closes with a numbered reference list.

## How skills reference knowledge

Every skill's `README.md` includes a `## Grounding` section listing the
specific knowledge documents the skill draws on. Example for
`citation-audit`:

```markdown
## Grounding

This skill is grounded in:
- [[citation-claim-alignment]] — the operational technique (the
  reference-accuracy / editorial spot-check protocol), with Greenberg
  2009's distortion categories.
- [[citation-accuracy-evidence]] — error prevalence (de Lacey, Pavlovic).
- [[citation-overreach-research]] — spin and primary-vs-review (Boutron, Yavchitz).
- [[hallucination-in-llm-citations]] — the AI failure mode this skill must NOT introduce.
```

This keeps the design accountable: a skill that drifts from its
grounding either gets updated or gets its grounding extended.

## Cross-linking

Documents link to one another with `[[doc-name]]` syntax (Obsidian-
compatible). Documents in different subdirectories link freely; the
knowledge layer is a graph, not a tree.

## The roadmap connection

The *Implementation priority* section of each document feeds
[`docs/roadmap.md`](../docs/roadmap.md). Findings that warrant a
skill go on the timeline; findings that warrant framing-only
treatment land in DESIGN.md or non-goals; findings that warrant
"maybe later" get an explicit trigger condition.

### Notes without a verdict

Two notes still have no *Implementation priority* section. Their
"How this informs scriptorium" sections propose standalone skills that
[`docs/roadmap.md`](../docs/roadmap.md) doesn't list, so a verdict
would be a new project decision rather than a record of current use:

- [`internal-consistency`](critique-techniques/internal-consistency.md)
  proposes a standalone `internal-consistency` critique skill. The note
  already grounds `figure-text-alignment`, `terminology-normalization`,
  `reporting-guideline-compliance` and `gap-finder`.
- [`logical-fallacy-detection`](critique-techniques/logical-fallacy-detection.md)
  proposes a future `spin-audit` skill. The note already grounds
  `gap-finder`.

## How this was built

The first-pass evidence base (~40 documents) was produced by parallel
research agents over a focused session. Each agent was scoped to a
topical subdirectory, given strict citation-discipline instructions
(real DOIs only; flag anything unverifiable rather than fabricate
it), and required to close each document with the *Implementation
priority* annotation.
In October 2026 every note was re-verified (#125): identifiers were
checked against Crossref, PubMed, arXiv or the publisher, misattributed
findings were corrected, and material that could not be verified was
removed (#147).

Several findings from these passes matter for the project's design:

- LLMs are unreliable at recomputing test statistics
  ([`statistical-inconsistency`](critique-techniques/statistical-inconsistency.md)).
  A statistical-consistency check should have the LLM extract the
  statistics and pass them to deterministic tools (Statcheck, GRIM)
  rather than recompute them in-band.
- BERTScore and similar embedding metrics are documented to be
  insensitive to negation and to numerical changes
  ([`semantic-preservation`](editing/semantic-preservation.md)),
  so embedding similarity is *not* a safe guard against meaning
  flips during transformation.
- NIH's 2025 Simplified Review Framework combines Significance and
  Innovation into Factor 1, Importance of the Research, and NIH's
  scoring guidance makes the Factor 1 score a ceiling on the overall
  impact score
  ([`significance-positioning`](scientific-writing/significance-positioning.md)).
  This changes what the planned `specific-aims` and
  `aims-significance-coherence` skills must check.
- Liang et al. 2024 (*NEJM AI*) found 30.85% overlap between the
  points GPT-4 and human reviewers raised on Nature-family papers,
  against 28.58% between two human reviewers
  ([`ai-peer-review-research`](peer-review/ai-peer-review-research.md)).
  The note names these overlap figures as the benchmark for
  evaluating `reviewer-simulation`.

## Contributing knowledge

New knowledge documents are welcome. The bar:

- Real citations.
- *Implementation priority* annotation that's defensible (not aspirational).
- Cross-links to related documents.
- Honest acknowledgment of weak-evidence areas and debates.

See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the workflow.
