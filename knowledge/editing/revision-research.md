# Revision research: what evidence says about effective revision

*Last updated: 2026-05-17*

## Synthesis

The composition-studies literature on revision is older and more
robust than most computational writing systems acknowledge. The
central finding, first articulated by Sommers in 1980 and refined by
Faigley & Witte in 1981, is that **experienced writers and novice
writers revise differently in kind, not just in degree**. Novice
writers treat revision as cleanup: surface fixes, word swaps,
proofreading-shaped activity. Experienced writers treat revision as
*re-seeing the work*: they revisit structure, argument, and meaning
across multiple passes, and they treat each pass as having a distinct
purpose rather than attempting to fix everything at once.

This has direct implications for an agentic writing system. A skill
that promises to "improve the paper" combines what experienced
writers do across many discrete passes — and produces the
characteristic novice-revision artifact: superficial change without
structural improvement, or structural change without local polish.
Scriptorium's one-skill-one-responsibility discipline is the agentic
analog of the experienced-writer practice of *single-purpose passes*.

The further implication is that revision is *iterative and
non-linear*. The "outline-then-write-then-edit" linear model that
guides most novice writers is not how experienced writers actually
work. Scriptorium should not lock authors into a single ordering of
skill invocations; the orchestrator (`manuscript-pipeline`, v0.2)
should support re-entry into earlier critique passes after
transformation passes, because that is what working revision looks
like.

## Evidence

**Sommers (1980), *College Composition and Communication* 31(4):
378–388.** "Revision Strategies of Student Writers and Experienced
Adult Writers." A landmark empirical study: eight freshman students
and seven experienced adult writers (journalists, editors, academics)
wrote three compositions, rewrote each two times, suggested
revisions for an anonymous-author composition, and were interviewed
three times. Key findings:

- Student writers operated with implicit, uncodified revision
  procedures, predominantly *word-level* — reaching for the
  thesaurus, polishing diction, fixing surface errors.
- Experienced writers operated with codified principles. They
  characterized revision as a recursive activity — "finding what I
  want to say" rather than "fixing what I already said."
- Experienced writers made larger, deeper changes throughout the
  writing process, not at the end. Sommers's framing: revision is
  not an editing stage; it is the writing process itself.

Sommers's contribution is that she demonstrated, empirically, that
experts and novices conceptualize the *purpose* of revision
differently. The expert's revision is closer to what Einsohn (see
[[copyediting-vs-developmental]]) would call developmental editing
applied to one's own draft.[^1]

**Faigley & Witte (1981), *College Composition and Communication*
32(4):400–414.** "Analyzing Revision." Built on Sommers by introducing
a **taxonomy of revision changes** that has become canonical in
composition research:

- **Surface changes** — formal and meaning-preserving edits (spelling,
  punctuation, tense, abbreviation, word-form, substitutions, reorderings).
- **Meaning changes** — additions, deletions, substitutions, and
  reorderings of content that change what the text says.

Meaning changes further split into **microstructural** (sentence-
or local-paragraph-level meaning shifts) and **macrostructural**
(thesis-level, argument-level, organization-level meaning shifts).[^2]

The Faigley & Witte taxonomy maps neatly onto editing levels (see
[[copyediting-vs-developmental]]):

| Faigley & Witte | Editing level | Scriptorium category |
|---|---|---|
| Surface | Copyediting | Normalization |
| Microstructural meaning | Line editing | Transformation (narrow) |
| Macrostructural meaning | Developmental | Transformation (broad) |

Faigley & Witte's contribution to scriptorium specifically: the
taxonomy provides a vocabulary for *describing what a transformation
skill did*. A semantic diff produced by `compression` should be
classifiable as predominantly surface or microstructural; one
produced by `argumentative-flow` should be classifiable as
macrostructural. If a "compression" skill is producing macrostructural
changes, the skill is doing the wrong job.

**Multi-pass discipline in expert practice.** The follow-on
composition-studies literature consistently observes that experienced
writers separate concerns across passes. The argument for separation
is not aesthetic; it is cognitive. Trying to fix structure, argument,
prose, and citation at once produces shallow attention to each.
Writing-process research summarized in Hayes & Flower (1980) and
extended in Hayes (2012) frames revision as a planning-translation-
reviewing cycle that re-enters itself rather than a terminal
proofread.[^3]

**The outline-then-write vs. draft-then-outline debate.** Practitioner
writing on academic composition (notably G. Whitesides' essay on
writing papers, *Advanced Materials* 2004) advocates an
**outline-first** discipline: write the outline, get reviewer
agreement on the outline, *then* write the prose. This pushes
macrostructural work earlier — the argument is settled before any
sentence has the inertia of being already-written. Whitesides's
specific recommendation: the outline should be on the order of one
page per figure, with each section's purpose explicit before any
paragraph is composed.[^4]

The counter-position — draft-then-outline — is associated with
writers who prefer to discover their argument by writing it. Both
work; the failure mode that scriptorium must guard against is
*neither* — drafting without an outline, then editing without a
re-outlining pass. That produces local fluency over global incoherence,
and it is the failure mode LLMs are most prone to amplify because
they are good at local fluency.

## How this informs scriptorium

**Passes have purposes.** Each scriptorium skill targets one of
Faigley & Witte's categories. Authors invoking multiple skills should
understand the sequence as a multi-pass revision in the
expert-writer sense, not as a single "improve this" instruction.

**The orchestrator (v0.2) must support re-entry.** Sommers and the
follow-on literature show that expert revision is recursive: a
developmental change at iteration 3 may require returning to a
copyediting concern. `manuscript-pipeline` should not enforce a
strict linear sequence; it should sequence intelligently *and* allow
re-entry. The state file's `phase` field (draft, review, revision,
submission) tracks where the manuscript is overall, but does not
constrain skill ordering within a phase.

**Surface vs. meaning diffs in skill output.** When a transformation
skill modifies prose, its semantic-diff output should classify the
change as surface, microstructural, or macrostructural. This makes
the conservative-edit posture inspectable: a `compression` skill that
declares its changes are surface-and-microstructural-only can be
verified against its own output.

**The "Remaining Weaknesses" section is the expert-revision
instinct.** Experienced writers know what they did *not* fix and can
articulate it. Skills should do the same — not because the LLM has
expert judgment, but because the discipline of articulating what was
not addressed is the same discipline that distinguishes expert from
novice revision.

**Don't bundle.** A single skill that does compression *and*
argumentative-flow *and* citation-cleanup is, in revision-research
terms, a novice-revision skill: it tries to do everything at once
and is unlikely to do any one thing deeply. The scriptorium pattern
explicitly prevents this bundling, and the rationale is the four
decades of composition-studies evidence on what bundling produces.

## Open questions / weak evidence

- Most revision research is on student writing or general English
  composition. Scientific writing — with its rigid section structure,
  high citation density, and quantitative claims — has been less
  studied as a revision context.
- Whether multi-pass discipline transfers to AI-assisted writing the
  same way it transfers to unassisted writing is empirically open.
  Plausible but not established.
- Sommers and Faigley & Witte are from a pre-word-processor era.
  Some of their observations about how writers physically revise
  (longhand, retyping) are dated; the conceptual taxonomy is not.

## References

[^1]: Sommers N. Revision strategies of student writers and
    experienced adult writers. *College Composition and Communication*.
    1980;31(4):378–388. doi:10.2307/356588 (also indexed via the
    NCTE archive: doi:10.58680/ccc198015930).

[^2]: Faigley L, Witte S. Analyzing revision. *College Composition
    and Communication*. 1981;32(4):400–414. doi:10.2307/356602 (NCTE
    archive: doi:10.58680/ccc198115887).

[^3]: Hayes JR, Flower LS. Identifying the organization of writing
    processes. In: Gregg LW, Steinberg ER, eds. *Cognitive Processes
    in Writing*. Erlbaum; 1980:3–30. Updated framework in Hayes JR.
    Modeling and remodeling writing. *Written Communication*.
    2012;29(3):369–388. doi:10.1177/0741088312451260.

[^4]: Whitesides GM. Whitesides' group: Writing a paper. *Advanced
    Materials*. 2004;16(15):1375–1377. doi:10.1002/adma.200400767.
