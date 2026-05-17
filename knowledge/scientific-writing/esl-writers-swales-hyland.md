# ESL writers and the Swales / Hyland tradition

*Last updated: 2026-05-17*

## Synthesis

A substantial fraction of scholarly writing today is produced by authors
for whom English is an additional language, and the dominant pedagogical
tradition for teaching them — running from John Swales' genre analysis
through Ken Hyland's corpus-linguistic work on metadiscourse — provides
the most empirically grounded account of *what* makes academic prose
function as academic prose. The point is not that ESL writers need a
softened "easy English" version of scientific writing. The point is
that the patterns native speakers acquire by osmosis (hedging force,
citation integration, stance marking, interactive vs. interactional
metadiscourse) are *explicit, conventional, and discipline-specific* —
exactly the kinds of patterns an agentic editor can audit. The
commercial tools that target this audience (Paperpal, Trinka,
Writefull) are essentially Hyland's framework operationalised.

For scriptorium, the load-bearing implication is that ESL-relevant
audits — especially hedging calibration, stance/voice consistency, and
citation-integration patterns — are not a separate "ESL pass" but the
core of what `argumentative-flow` should already be doing. The
Swales/Hyland literature gives us a vocabulary for naming what good
sentence-level critique attends to. Framing these checks as
"ESL-friendly" rather than "for ESL writers" is the right move: they
help every author, but they help non-native writers most.

## Evidence and frameworks

### Swales' CARS model

John Swales' 1990 *Genre Analysis: English in Academic and Research
Settings* [1] introduced the **Create-A-Research-Space (CARS)** model
of research article introductions. The three rhetorical moves are:

1. **Establishing a territory** — claiming centrality, making
   topic generalisations, reviewing previous research.
2. **Establishing a niche** — counter-claiming, indicating a gap,
   question-raising, or continuing a tradition.
3. **Occupying the niche** — outlining purposes, announcing
   present research, announcing principal findings, indicating
   structure.

CARS is the single most-cited framework in academic-writing pedagogy
and is the implicit skeleton of most "how to write an introduction"
advice. Swales' 2004 *Research Genres* [2] extends the framework
beyond introductions and explicitly addresses cross-disciplinary
variation; see also [[discipline-conventions]].

The framework matters here because the *gap statement* is the move
that most often goes wrong: too aggressive ("no prior work has…"),
too vague ("more research is needed"), or absent. CARS gives an
editor concrete questions to ask of an introduction — which move is
present, which is missing, which is misordered.

### Hyland's metadiscourse and hedging

Ken Hyland's work is the empirical complement to Swales' rhetorical
analysis. His 1998 *Hedging in Scientific Research Articles* [3] is
the canonical corpus study of how scientists modulate the strength of
their claims through modal verbs ("may", "might"), epistemic adverbs
("possibly", "apparently"), approximators ("approximately", "about"),
and indirect attributions ("it has been suggested"). The central
finding is that hedging is not optional softening; it is **how
scientific claims are calibrated to evidence**. Under-hedging reads
as overclaiming and triggers reviewer hostility; over-hedging reads
as evasive or under-confident.

Hyland's 2005 *Metadiscourse* [4] distinguishes:

- **Interactive metadiscourse** — devices that organise the text
  (transitions, frame markers, endophoric markers, evidentials, code
  glosses).
- **Interactional metadiscourse** — devices that signal the author's
  stance toward the proposition and the reader (hedges, boosters,
  attitude markers, self-mentions, engagement markers).

Hyland & Jiang's 2018 corpus study [5] tracked these features across
four disciplines over fifty years and documented a *significant
increase in interactive features and decrease in interactional
types*, which they read as academic prose becoming more author-driven
and less reader-engaging — a finding that informs how to interpret
"stance" advice. The full title — "*In this paper we suggest*:
Changing patterns of disciplinary metadiscourse" — is itself an
example of the construction it studies.

### Flowerdew on EAL academic writing

John Flowerdew's work [6] documents the specific obstacles English
as an Additional Language (EAL) writers face — not vocabulary or
grammar in the surface sense, but the cultural and disciplinary
conventions that govern stance, citation integration, and
self-positioning. His repeated empirical observation is that the
hardest part of EAL academic writing is not producing
grammatical sentences; it is producing sentences with the right
*rhetorical force* for the discipline.

### Specific patterns ESL writers struggle with

The pedagogical literature [3,4,6] converges on a small set of
high-leverage difficulties:

- **Hedging miscalibration.** Direct translation from a first
  language can produce claims that are too strong ("this proves",
  "this shows clearly") or too tentative ("it might possibly be
  suggested that…"). Both fail in characteristic ways under peer
  review.
- **Citation integration.** Three patterns coexist in academic
  English — integral ("Smith (2020) argues…"), non-integral
  ("(Smith 2020)"), and reporting verbs with varying force
  ("notes" vs. "claims" vs. "demonstrates"). The choice carries
  stance information that is invisible to grammar checkers.
- **Voice and stance.** First-person vs. impersonal constructions,
  use of boosters ("clearly", "obviously"), and engagement markers
  ("note that", "consider…") vary by discipline and venue.
- **Idiomatic transitions.** "Moreover", "in particular",
  "specifically", "in contrast", "however" carry slightly
  different logical loads that are conventionalised, not derivable
  from dictionary meaning.

These are the things tools like Paperpal and Writefull check; they
are also exactly what [[reader-expectation-approach]] and
[[argument-mapping]] should care about at the sentence level.

## How this informs scriptorium

1. **`argumentative-flow` should attend to hedging force.** A claim
   in `core_claims` that the prose hedges (or fails to hedge)
   inconsistently is a real defect, not stylistic noise. The
   conservative-edit posture is well-suited: flagging hedging
   miscalibration is cheaper than rewriting it.
2. **Stance consistency belongs in critique skills, not in a
   separate ESL pass.** Branding a check as "ESL" risks ghetto-ising
   it. Frame it as: "Is the hedging force consistent with the
   strength of the evidence cited?"
3. **Citation integration tells you about stance.** A skill that
   audits citation-claim alignment ([[citation-claim-alignment]])
   should also flag reporting-verb force — "demonstrates" vs.
   "suggests" is a hedging choice that should match the cited
   study's strength of evidence.
4. **Discipline awareness.** Hyland & Jiang [5] document
   disciplinary variation; scriptorium's knowledge base is
   biomedical-coded (see [[discipline-conventions]]). State the
   scope.

## Implementation priority for scriptorium

**Verdict:** Maybe later — *no dedicated `esl-friendliness-pass`
skill*; instead, **embed ESL-aware checks in existing critique
skills** (v0.1 / v0.3) and call this out explicitly in skill
descriptions.

**If Yes (later):** the trigger would be evidence that users want a
standalone audit framed around hedging/stance/citation-integration.
The skill would be `stance-and-hedging-audit`, v0.3+. Required data:
`core_claims` and `terminology` from `MANUSCRIPT_STATE.yaml`,
plus the bibliography for evidence-strength lookup. Output: a list
of claims whose hedging force does not match their evidentiary
support, with suggested rewordings preserving the citation set.

**Why "maybe" rather than "yes now":** the work overlaps heavily
with `argumentative-flow` (v0.1) and any future
`citation-claim-alignment` skill. Spinning it out before those
skills mature risks fragmenting responsibility. The right v0.1 move
is to make sure `argumentative-flow`'s description names hedging
calibration explicitly so users invoke it for that purpose. Promote
to a standalone skill if and only if the embedded version under-uses
the framework or users explicitly ask for an ESL-targeted tool.

**Condition that flips to Yes:** (a) a user requests a
standalone hedging/stance pass, *or* (b) `argumentative-flow` is
shown not to cover hedging force reliably on real manuscripts.

## Open questions / weak evidence

- The corpus-linguistic findings are descriptive, not interventional.
  Hyland tells us what skilled academic prose looks like; whether
  rewriting toward those norms improves outcomes (acceptance,
  citation, reviewer sentiment) is largely unmeasured.
- The "ESL writer" category is heterogeneous: a Chinese-L1
  computational biologist and a Brazilian-L1 humanities scholar
  share little. Discipline often dominates language background.
- Commercial tools (Paperpal, Writefull, Trinka) report internal
  evaluations but rarely publish externally verifiable benchmarks.
  Their value proposition is mostly an existence proof that the
  market exists, not evidence that their interventions work.

## References

[1] Swales, J. M. (1990). *Genre Analysis: English in Academic and
Research Settings*. Cambridge University Press. ISBN
9780521338134.

[2] Swales, J. M. (2004). *Research Genres: Explorations and
Applications*. Cambridge University Press. ISBN 9780521533348
(paperback; hardback ISBN 9780521825603). [TODO verify hardback
ISBN — the originally listed 9780521531344 appears not to be the
canonical hardback identifier.]

[3] Hyland, K. (1998). *Hedging in Scientific Research Articles*.
John Benjamins Publishing. ISBN 9789027250698.

[4] Hyland, K. (2005). *Metadiscourse: Exploring Interaction in
Writing*. Continuum. ISBN 9780826476104.

[5] Hyland, K., & Jiang, F. K. (2018). "In this paper we suggest":
Changing patterns of disciplinary metadiscourse. *English for
Specific Purposes*, 51, 18–30. DOI: 10.1016/j.esp.2018.02.001.
(The DOI originally referenced as 10.1016/j.esp.2018.04.005 does
not resolve to this paper; the correct DOI ends in `.02.001`.)

[6] Flowerdew, J. (2001). Attitudes of journal editors to nonnative
speaker contributions. *TESOL Quarterly*, 35(1), 121–150. DOI:
10.2307/3587862. See also Flowerdew, J. (2013). *Discourse in
English Language Education*. Routledge. ISBN 9780415499651.
