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
3. **Honest scope.** Each knowledge document closes with an
   *Implementation priority* section that states whether the finding
   becomes a skill or stays framing-only context. Findings that
   shouldn't become skills are explicit.

## Layout

```text
knowledge/
├── prior-art/                # similar tools, projects, lineage
├── scientific-writing/       # methodology of good writing
├── peer-review/              # evidence on review processes
├── citations/                # citation practices and pitfalls
├── editing/                  # editing methodology
├── grants/                   # grant-writing evidence
├── critique-techniques/      # how to find problems systematically
└── reproducibility/          # the crisis context scriptorium responds to
```

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
- Items the research could not verify in-session are marked
  `[TODO verify]` rather than fabricated.
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
- [[citation-claim-alignment]] — the operational technique (Greenberg 2009).
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

The *Implementation priority* section of every document feeds
[`docs/roadmap.md`](../docs/roadmap.md). Findings that warrant a
skill go on the timeline; findings that warrant framing-only
treatment land in DESIGN.md or non-goals; findings that warrant
"maybe later" get an explicit trigger condition.

## How this was built

The first-pass evidence base (~40 documents) was produced by parallel
research agents over a focused session. Each agent was scoped to a
topical subdirectory, given strict citation-discipline instructions
(real DOIs only; mark unverifiable as `[TODO verify]`), and required
to close each document with the *Implementation priority* annotation.
The agents independently identified several non-obvious findings worth
the project's attention:

- LLM arithmetic is unreliable for statistical-consistency checks
  ([`statistical-inconsistency`](critique-techniques/statistical-inconsistency.md));
  scriptorium skills call out to deterministic scripts (Statcheck, GRIM)
  rather than recompute in-band.
- BERTScore's antonymy problem
  ([`semantic-preservation`](editing/semantic-preservation.md))
  means embedding similarity is *not* a safe guard against meaning
  flips during transformation.
- NIH's 2025 Simplified Review Framework bundles Significance and
  Innovation into a single factor
  ([`significance-positioning`](scientific-writing/significance-positioning.md)),
  changing what a `specific-aims` skill must accomplish.
- The 30.85% human–AI comment overlap from Liang et al. 2024
  ([`ai-peer-review-research`](peer-review/ai-peer-review-research.md))
  is the gold-standard benchmark `reviewer-simulation` will be
  evaluated against.

## Contributing knowledge

New knowledge documents are welcome. The bar:

- Real citations.
- *Implementation priority* annotation that's defensible (not aspirational).
- Cross-links to related documents.
- Honest acknowledgment of weak-evidence areas and debates.

See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the workflow.
