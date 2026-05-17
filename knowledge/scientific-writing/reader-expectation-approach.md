## Reader-expectation approach (Gopen & Swan)

*Last updated: 2026-05-17*

## Synthesis

George Gopen and Judith Swan's 1990 article "The Science of Scientific
Writing" (*American Scientist* 78(6): 550–558) [1] is the most
methodologically careful piece of writing advice in the scientific writing
literature, and the one most directly grounded in linguistics and reader
psychology. Its central insight, repeated in Gopen's later books [2, 3], is
that **prose meaning is fixed by what the reader does with the text, not by
what the writer intends** — and that readers operate by predictable
structural expectations about *where* in a sentence different kinds of
information will appear. Writers who satisfy those expectations are read
fluently; writers who violate them produce work that is technically
grammatical but locally hard to parse.

Three of Gopen and Swan's prescriptions — the **topic position**, the
**stress position**, and **subject–verb proximity** — are unusually
operationalizable. They map onto sentence-level transformations that an
editing tool can perform without semantic risk. This is why the
reader-expectation approach is the framework most directly relevant to
scriptorium's `argumentative-flow` and any future sentence-level editing
skills: it tells you *which structural moves to test for* without requiring
you to understand the content.

The framework's status as "evidence-based" should be qualified. Gopen and
Swan ground their prescriptions in reading-process research (Bock, Just &
Carpenter, etc.) and demonstrate them on real scientific paragraphs, but
they do not present a randomized intervention. The strongest empirical claim
is that violations of these expectations measurably slow reader
comprehension at the local scale — not that following them improves citation
outcomes. The framework's authority comes from its mechanism, not from
outcomes data.

## Evidence and frameworks

### The core claim

The article's foundational sentence is quoted endlessly because it inverts
the naïve model of writing:

> "The fundamental purpose of scientific discourse is not the mere
> presentation of information and thought, but rather its actual
> communication. It does not matter how pleased an author might be to have
> converted all the right data into sentences and paragraphs; it matters
> only whether a large majority of the reading audience accurately perceives
> what the author had in mind." [1]

And later:

> "The meaning of any prose is not that which the writer intends, but that
> which readers interpret." [1, paraphrase widely cited]

This reframes editing from a *correctness* problem (is the grammar right?)
to a *prediction* problem (will the typical reader land where I want them
to?). The reader's expectations are not optional — they are the substrate
on which any communication happens.

### The structural principles

Gopen and Swan identify several reader expectations. The four most useful
operationally are:

**1. Topic position.** Readers expect the beginning of a sentence (or
clause) to tell them whose story this sentence is about and to link it to
what came before. A sentence that opens with a new piece of information
disorients the reader, because they expected to find a connection to
already-known material there.

**2. Stress position.** Readers expect the end of a sentence (the position
just before the period, or before a colon or semicolon) to carry the new,
emphasized information.

> "Readers naturally emphasize the material that arrives at a point of
> syntactic closure." [1]

A sentence whose intended punchline lives mid-sentence rather than at the
stress position will be read with the wrong emphasis even if the wording is
otherwise perfect.

**3. Subject–verb proximity.** Readers expect the grammatical subject and
its verb to be near each other.

> "Readers expect a grammatical subject to be followed immediately by the
> verb. Anything of length that intervenes between subject and verb is read
> as an interruption, and therefore as something of lesser importance." [1]

Long noun phrases or qualifying clauses inserted between subject and verb
are processed as *parenthetical* even when the writer intended them as
essential. This is one of the most common failure modes in scientific
prose, where a long methodological qualifier is stuffed between subject and
verb.

**4. Old-information-before-new.** Across sentence boundaries, readers
expect the topic position of sentence N+1 to anchor in something the topic
position or stress position of sentence N established. This is how
paragraphs *flow*: each topic refers back, each stress position pushes
forward.

These principles compose: a well-formed paragraph chains
topic-old → stress-new → topic-old (the just-introduced new) → stress-new,
and so on. The flow is mechanical and the diagnostic is mechanical:
underline the topic and stress positions of each sentence, then check
whether the topics chain back and the stresses chain forward.

### Follow-on work

Gopen developed the framework at book length in:

- *The Sense of Structure: Writing from the Reader's Perspective* (Pearson
  Longman, 2004; ISBN-13 978-0-205-29632-3) [2] — applies the framework
  beyond science writing.
- *Expectations: Teaching Writing from the Reader's Perspective* (Pearson,
  2004; ISBN-13 978-0-205-29617-0) [3] — pedagogical companion volume.

Schimel (*Writing Science*, 2012) imports the topic-position / stress-position
distinction wholesale and treats it as the sentence-level operating system
for the OCAR-structured paragraph (see [[narrative-frameworks]]).

The reader-expectation approach has been quietly adopted by Duke's Thompson
Writing Program, the AAAS communication workshops, and a growing list of
graduate research-skills curricula, but it is not formally evaluated in
controlled studies. Its endurance is striking: 36 years on, it remains the
default citation when someone needs to justify a sentence-level revision in
scientific prose.

## How this informs scriptorium

The reader-expectation framework is the strongest theoretical grounding for
several skills:

- **`argumentative-flow`** (current). The skill's paragraph-level diagnostic
  should explicitly check old-information chaining across sentence
  boundaries. If consecutive sentences fail to anchor their topic positions
  in prior stress positions, the paragraph has a flow defect even if every
  sentence is locally fine.
- **`compression`** (planned, v0.3). Aggressive compression that strips
  long subordinate clauses must respect subject–verb proximity. A
  compression skill that *fixes* a 30-word subject phrase is doing more
  than reducing length; it's making the sentence readable. This should be
  named in the skill's rationale, not done silently.
- **`reviewer-simulation`** (current). The "I had to re-read this paragraph
  three times" reviewer reaction is almost always a topic/stress violation.
  The simulator should be able to identify *where* in the paragraph the
  reader was thrown off, not just that they were.
- **Sentence-level rewrite skills** (planned). Any future sentence-rewrite
  skill should expose its rationale in Gopen/Swan terms — "moved
  *thermal stability* into stress position because it carries the new
  information" — so that the edit is inspectable and the user can disagree
  with the diagnosis, not just the wording.

The framework also disciplines the *posture* of editing skills. Because the
diagnosis is mechanical (positions, distances), an LLM editor can apply it
with much higher confidence than it can apply, say, "make this more
elegant." Skills should prefer mechanical Gopen/Swan moves to subjective
ones whenever the mechanical move is sufficient.

## Open questions / weak evidence

- Gopen and Swan's principles are demonstrated on examples; they have not
  been validated by eye-tracking or reading-time experiments at scale.
  The cognitive-science substrate they cite (Bock, Just & Carpenter) is
  real but predates the framework.
- The framework is English-centric. Topic and stress positions in languages
  with different default word orders (German, Japanese) do not map cleanly.
  An LLM editor needs to be careful about applying these rules to
  non-English manuscripts or to translation-adjacent prose.
- It is unclear whether following the principles improves *outcome*
  measures (citation, reviewer recommendation) or only proximal
  comprehension measures (reading time, comprehension accuracy).

## References

1. Gopen GD, Swan JA. The Science of Scientific Writing. *American
   Scientist*. 1990;78(6):550–558. (November–December 1990 issue.)
2. Gopen GD. *The Sense of Structure: Writing from the Reader's
   Perspective*. Pearson Longman; 2004. ISBN-13 978-0-205-29632-3.
3. Gopen GD. *Expectations: Teaching Writing from the Reader's
   Perspective*. Pearson; 2004. ISBN-13 978-0-205-29617-0.
