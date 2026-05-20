# Hayes-Flower writing model and cognitive load in scientific prose

*Last updated: 2026-05-17*

## Synthesis

The Hayes-Flower cognitive-process model of writing (1980/1981) and
its 2012 revision are the canonical psychological account of what
writers do when they write. The model recasts writing as three
interleaved processes — **planning**, **translating** (turning ideas
into language), and **reviewing** — under a top-level monitor that
decides which process to deploy when. Crucially, the processes are
**recursive**: a writer drops out of translating to re-plan, drops out
of reviewing to re-translate, and so on, in whatever order the
emerging text demands. The linear "plan, write, edit" sequence taught
to undergraduates is a normative pedagogical fiction; experienced
writers move between the three processes constantly. [1, 2]

Sweller's **cognitive load theory** (1988; updated 2019) gives the
parallel account on the *reader* side. Working memory is severely
limited (roughly 4±1 chunks for novel information); long-term memory
is functionally unlimited but accessible only through schemas that
have to be constructed. Anything in the text that imposes load
without contributing to schema construction — clunky syntax, gratuitous
nominalisations, badly ordered information — is **extraneous load**
and degrades comprehension. Anything that helps the reader build the
intended schema is **germane load** and is the load you want. [3, 4]

The link this document makes explicit: **Gopen and Swan's
reader-expectation principles
([[reader-expectation-approach]]) are essentially mechanisms for
minimising extraneous cognitive load on the reader**. Topic position
tells the reader where to find the connection to prior context (no
search cost). Stress position tells the reader where to find the
new information (no guessing about emphasis). Subject-verb proximity
avoids the working-memory cost of holding a subject open while a
qualifier elapses. Old-information-before-new exploits already-built
schemas before adding to them. Cognitive load theory provides the
*why*; Gopen and Swan provide the *what to do*. Together they give
the `argumentative-flow` skill and its successors a cognitive-science
substrate that is otherwise easy to mistake for stylistic preference.

## Evidence and frameworks

### The original Hayes-Flower model (1980/1981)

Hayes and Flower introduced the model in a 1980 chapter [5] and refined
it in their landmark 1981 *CCC* article [1], based on think-aloud
protocols collected from writers as they composed. Three components:

- **Task environment** — the rhetorical situation (audience, topic,
  exigence) and the text-produced-so-far.
- **Long-term memory** — knowledge of topic, audience, genre, and
  writing schemas.
- **Writing processes** — planning, translating, and reviewing,
  arbitrated by a *monitor*.

The most cited claim from the article is that writing is **not
linear** but recursive. A writer planning a section may, mid-plan,
realise the introduction needs revision; will jump to reviewing the
introduction; may, in reviewing, identify a missing argument; will
jump back to planning. The monitor decides where to put attention.
This pattern repeated across protocols and across writer expertise
levels (though with quite different distributions — expert writers
plan more, novice writers translate more impulsively).

The model has been criticised for under-specifying the monitor and
for being silent on motivation, affect, and social context, but it
remains the reference architecture for the cognitive-process
tradition in composition research.

### Hayes' 2012 update

Hayes' "Modeling and Remodeling Writing" [2] revised the architecture
in three important ways:

1. **Motivation and affect** are now top-level components, not
   absent.
2. **Working memory** is foregrounded as the bottleneck constraining
   all processing — making the link to Sweller's cognitive load
   theory explicit.
3. The three processes are renamed and reorganised: **proposer**
   (generates content), **translator** (turns proposals into
   language), **transcriber** (turns language into orthography),
   and **evaluator** (the reviewer role). The collaboration among
   these and the task environment is mediated by a control structure.

For scriptorium specifically, Hayes' 2012 emphasis on working memory
as the bottleneck is the connection point: a writer with working
memory consumed by formatting concerns, citation lookup, or hedging
choices has less working memory for the proposer and evaluator. An
agentic system that absorbs the cheap cognitive load — formatting,
references, terminology consistency — frees working memory for the
processes that actually require human judgement.

### Sweller's cognitive load theory

Sweller's 1988 paper [3] introduced cognitive load theory in the
context of problem solving and learning. The 2019 twenty-year update
with van Merrienboer and Paas [4] consolidates four decades of
empirical work. The theory distinguishes three types of load:

- **Intrinsic load**: the inherent difficulty of the material
  relative to the learner's existing schemas. Manipulable only by
  pre-training or schema construction.
- **Extraneous load**: load imposed by how the material is
  *presented*, not by what it *is*. Manipulable by editing.
- **Germane load**: load that contributes to schema construction —
  the productive cognitive work.

The pedagogical injunction is to minimise extraneous load so that
working-memory capacity is available for germane processing. Applied
to scientific prose: every reader-confusing structural choice
(buried topic, misplaced stress, distant subject-verb pair) consumes
working memory that the reader needed for the actual argument.

The 2019 update further documents the **expertise-reversal effect**
(scaffolding that helps novices hurts experts) and the **transient
information effect** (information that disappears before working
memory can process it). Both are relevant to scientific writing —
short-circuited passages and densely cross-referenced material
exhibit these failure modes routinely.

### Sweetland Center and practitioner translation

The Sweetland Center for Writing (University of Michigan) [6] is one
of the few academic writing centres that explicitly grounds its
scientific-writing pedagogy in cognitive-process and cognitive-load
research. Its workshops and online materials translate Sweller's
constructs into actionable revisions: chunking, signposting,
parallel structure, and the staging of new information after old.
Other comparable translations appear at Duke's Thompson Writing
Program and in graduate research-skills curricula, but Sweetland's
materials are the most explicit about the cognitive-science
grounding.

## How this informs scriptorium

The Hayes-Flower and Sweller frameworks together do three things for
scriptorium that no single principle does on its own:

1. **They justify the discipline of one-skill-one-responsibility.**
   Hayes' updated model treats working memory as the bottleneck for
   the writer; analogously, an LLM context window with attention
   spread across compression, flow, citation accuracy, and
   reviewer-style critique is a working-memory bottleneck for the
   model. Decomposing into single-purpose skills *is* the
   working-memory remedy.
2. **They justify the conservative-edit posture in
   [[semantic-preservation]].** A skill that minimises extraneous
   load — moving stress-bearing material to the stress position,
   pulling subjects close to their verbs — is doing precisely the
   reader-side cognitive-load reduction Sweller's theory predicts is
   most valuable. Anchoring the rationale in cognitive load theory
   makes it inspectable and defensible.
3. **They name what scriptorium does *not* do.** Some prose
   improvement requires schema construction in the reader (germane
   load), and that is a content choice, not a sentence-level edit.
   Skills should refuse to invent germane scaffolding; that is the
   author's job.

Specific skill implications:

- **`argumentative-flow`** (current). Its underlying logic — chained
  topic/stress positions, old-info-before-new — should be cited in
  the skill's rationale as cognitive-load-reduction, not as
  Gopen-and-Swan-style. Both are correct; the cognitive grounding
  is more defensible to a sceptical reader.
- **`compression`** (planned, v0.3). Compression is justified
  cognitively when it removes extraneous load (filler, unmotivated
  repetition); it is *not* justified when it removes germane content
  (scaffolding the reader needs). The skill's prompt and
  preservation report should distinguish these cases.
- **`reviewer-simulation`** (current). A reviewer's "I had to read
  this three times" reaction is, in Sweller terms, an extraneous-load
  signal. The simulator can be more precise about *where* the load
  spiked rather than which feeling the reviewer reported.

The MANUSCRIPT_STATE schema does not yet encode reader expertise. A
v0.3 addition — `target_reader_expertise: novice | trained | expert`
— would let cognitive-load-aware skills calibrate. An expert reader
tolerates compressed, schema-dense prose; a novice reader needs more
scaffolding. The expertise-reversal effect [4] says the *same* prose
helps one and hurts the other.

## Implementation priority for scriptorium

**Verdict:** **No new skill.** This is theoretical grounding for
existing skills (`argumentative-flow`, `reviewer-simulation`) and
future skills (`compression`).

**Why useful context anyway:**

- DESIGN.md should cite Hayes-Flower and Sweller as the cognitive-
  science substrate for the skill architecture and for the
  conservative-edit posture in [[semantic-preservation]]. This
  hardens the JOSS paper / thought-leadership story against the
  charge that scriptorium's editing principles are stylistic
  preferences.
- Prompts inside existing skills should reference cognitive-load
  vocabulary ("extraneous load", "schema construction") when
  explaining their diagnoses. This makes diagnoses inspectable in
  language the reader can engage with.
- The `target_reader_expertise` field is a small, cheap addition to
  MANUSCRIPT_STATE that lights up cognitive-load-aware behaviour in
  multiple skills. Worth adding in v0.2 even before any skill formally
  uses it.

A future "cognitive-load-audit" skill is *not* recommended. The
diagnoses cognitive load theory enables are largely already covered
by Gopen-and-Swan-grounded analysis. Adding a separate audit skill
would double-bill the same diagnoses and would tempt theatrical
quantification (see [[quantitative-quality-measures]]).

## Open questions / weak evidence

- The link between Sweller's quantitative load constructs and
  sentence-level structural choices is theoretically clean but
  empirically under-validated for scientific text. Eye-tracking and
  reading-time work on actual research articles is sparse.
- The 2012 Hayes architecture has not been operationalised
  computationally in any reference implementation — it remains a
  descriptive model, not a generative one.
- The expertise-reversal effect is well-established for instructional
  materials (Kalyuga and colleagues, Nückles et al. on writing-to-
  learn journals); the *direct* extension to expert/novice reading of
  published research articles is plausible but, in our search, not
  pinned to a single empirical validation paper specific to scientific-
  article reading. The skill should treat `target_reader_expertise`
  as a design-motivated parameter grounded in the instructional-design
  literature rather than as a claim with direct empirical validation
  in research-article comprehension.

## References

1. Flower L, Hayes JR. A cognitive process theory of writing.
   *College Composition and Communication*. 1981;32(4):365–387.
   doi:10.2307/356600 (NCTE archive: doi:10.58680/ccc198115885).
2. Hayes JR. Modeling and remodeling writing. *Written
   Communication*. 2012;29(3):369–388.
   doi:10.1177/0741088312451260.
3. Sweller J. Cognitive load during problem solving: Effects on
   learning. *Cognitive Science*. 1988;12(2):257–285.
   doi:10.1207/s15516709cog1202_4.
4. Sweller J, van Merrienboer JJG, Paas F. Cognitive architecture
   and instructional design: 20 years later. *Educational Psychology
   Review*. 2019;31:261–292. doi:10.1007/s10648-019-09465-5.
5. Hayes JR, Flower LS. Identifying the organization of writing
   processes. In: Gregg LW, Steinberg ER, eds. *Cognitive Processes
   in Writing*. Erlbaum; 1980:3–30.
6. Sweetland Center for Writing, University of Michigan. Online
   resources for graduate and faculty writers, including science-
   writing materials.
   https://lsa.umich.edu/sweetland (accessed 2026-05-17).
