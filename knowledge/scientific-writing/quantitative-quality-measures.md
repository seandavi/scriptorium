# Quantitative quality measures: what they can and cannot tell us

*Last updated: 2026-05-17*

## Synthesis

The temptation to quantify writing quality is older than the
computational tools used to do it. Flesch's 1948 reading-ease
formula [1] and the Flesch-Kincaid grade level (Kincaid et al. 1975)
[2] are the foundational entries; SMOG, Gunning Fog, Coleman-Liau,
and the Automated Readability Index extend the same family.
Lexical-diversity measures (type-token ratio, MTLD, HD-D) [3]
quantify vocabulary breadth. Modern entries include BERTScore
(Zhang et al. 2020) [4] for semantic similarity, Coh-Metrix
(Graesser, McNamara et al.) [5] for cohesion and discourse-level
features, and LIWC (Pennebaker) [6] for psycholinguistic
categorisation. Hyland's corpus work [7, 8] has documented stable
diachronic patterns in academic writing — increasing
metadiscourse, shifting stance marker frequencies, evolving
sentence-length distributions.

The blunt assessment: **most quantitative writing-quality measures
are noise for scholarly text.** They were designed for or
validated on materials very different from research papers
(military training pamphlets, public health flyers, classroom
narratives). When applied to scientific prose they systematically
mis-score correctly-used technical terminology as
"difficult", penalise legitimate nominalisation, and fail to
capture the dimensions that actually matter (argument coherence,
claim-evidence alignment, hedging calibration). Sand-Jensen's
satirical-but-cited 2007 *Oikos* paper [9] is a useful corrective:
following readability heuristics aggressively produces consistently
boring text without making it consistently good.

The constructive position is that quantitative measures are useful
**diagnostically** — as outlier flags that prompt human
inspection — and harmful **prescriptively** — as targets to be
optimised. A sentence at Flesch-Kincaid grade 25 in a paper aimed
at clinicians is worth a human look. A skill that automatically
rewrites that sentence to grade 12 is producing theatre. For
scriptorium, this distinction is the design principle: there
should be **no general-purpose "writing score" skill**, because such
a skill would be theatre; there *may* be narrow outlier-detection
skills that surface candidate problems for human review.

## Evidence and frameworks

### Readability indices

**Flesch Reading Ease (1948)** [1] and **Flesch-Kincaid Grade
Level (1975)** [2] use surface features — average sentence length,
average syllables per word — to produce a single difficulty score.
The Flesch formula:

> Score = 206.835 − 1.015 × (words/sentences) − 84.6 × (syllables/words)

Scores range from 0 (very hard) to 100 (very easy); a score of 60
corresponds roughly to 8th-grade reading level. Flesch-Kincaid
Grade Level outputs a US grade-level number directly.

**SMOG** (McLaughlin 1969) uses polysyllabic word counts in
30-sentence samples; **Gunning Fog** counts "complex" (3+ syllable)
words; **Coleman-Liau** uses character-per-word and
sentence-per-100-words counts; **Automated Readability Index**
uses character and word counts. All are variants on the same
syllables-and-sentence-length theme.

**Why these fail on scientific text.** All formulas in this family
share a structural defect: they assume that long words and long
sentences indicate difficulty for the *reader's* purpose. For a
research paper read by a domain expert, neither assumption holds:

- A long word may be a precise technical term ("immunohistochemistry",
  "phosphorylation", "heterozygous"). For the expert reader the
  word is *easier* than a circumlocution would be.
- A long sentence may contain a precisely structured argument
  that, broken into short sentences, becomes harder to follow
  because the connective tissue is destroyed.
- Correctly used jargon reduces cognitive load for the expert
  reader (see [[hayes-flower-writing-model]]) because it triggers
  pre-built schemas; rephrasing into "plain language" increases
  load by forcing schema reconstruction.

The formulas are valid for their original domain (audience-
calibrated public-facing materials, low-literacy adaptation,
military training texts) and they are valid as plain-language
diagnostics for that genre (see [[plain-language-lay-summaries]]).
They are *invalid* as quality indices for scientific writing aimed
at expert audiences. Sand-Jensen's 2007 *Oikos* paper [9]
satirises the consequence: a manuscript can satisfy every
readability heuristic while being unreadable in the sense that
matters (no argument, no contribution, no interest).

### Lexical diversity

The **type-token ratio (TTR)** is the simplest lexical-diversity
measure: number of unique words divided by total word count. Its
problem is *length sensitivity* — TTR mechanically falls as text
length grows, because the rate of new-word introduction declines.

**MTLD (Measure of Textual Lexical Diversity)** and **HD-D
(Hypergeometric Distribution)** [3] are sophisticated alternatives.
MTLD computes the mean length of word strings that maintain a
criterion TTR; HD-D uses the hypergeometric distribution to
estimate vocabulary breadth in a length-independent way. McCarthy
& Jarvis (2010) [3] validated these and found that MTLD in
particular performs well across text lengths.

For scientific writing, lexical diversity is at best weakly
diagnostic. Methods sections are deliberately low-diversity
(repeating "we sequenced", "we cultured") because reproducibility
demands it. Discussion sections are higher-diversity. Diversity
varies systematically by section, by sub-discipline, and by
authorial style; mean diversity carries no quality signal.

### Sentence-length distributions and corpus stylistics

Hyland and Jiang's corpus work [7, 8] is the most careful study of
academic writing patterns over time. Their 2018 paper, *"In this
paper we suggest": Changing patterns of disciplinary
metadiscourse*, [7] used a 2.2-million-word corpus from top
journals in four disciplines over 50 years and documented:

- A significant increase in **interactive** metadiscourse
  (transitions, frame markers, evidentials, endophoric markers).
- A significant decrease in **interactional** metadiscourse
  (hedges, boosters, attitude markers, self-mention) — but with
  field heterogeneity, declining in soft fields and *rising* in
  sciences.
- Sentence-length distributions trending shorter on average over
  the corpus period.

The work demonstrates that academic-writing style is not a
timeless ideal; it drifts measurably and the drift is
field-specific. For an automated quality tool, this matters
because *the target distribution is moving* — a sentence-length
heuristic calibrated to 1970s writing will misfit 2020s writing
and vice versa.

### Hedging vocabulary

Hyland's broader work on hedges and boosters has produced
catalogued vocabularies of hedging markers (modal verbs *may*,
*might*, *could*; epistemic verbs *suggest*, *appear*, *seem*;
adverbs *possibly*, *probably*; nouns *possibility*, *suggestion*)
and boosters (*demonstrate*, *prove*, *establish*, *clearly*,
*certainly*). The lists exist in Hyland's published monographs
and corpus articles, but no openly-licensed canonical machine-
readable distribution was located during this sweep — research-
practice typically extracts the categories manually from the
published taxonomy. Scriptorium would need to compile its own list
from the published categories rather than depend on an upstream
canonical file.

The diagnostic use is not "this paper has too many hedges" but
"this revision pass removed N hedges without recording a
rationale" — i.e., overclaim-drift detection
([[citation-overreach-research]]). Hedging vocabularies are
useful as *invariants to preserve*, not as quality scores.

### Modern embedding-based measures

**BERTScore (Zhang et al. 2020).** [4] Token-level embedding
similarity between candidate and reference sentences. Outperforms
n-gram metrics (BLEU, ROUGE) on tasks where meaning matters more
than surface wording. Already discussed in [[semantic-preservation]]
with the **antonymy limitation**: BERTScore registers "the best
treatment" and "the worst treatment" as ~95% similar despite
their opposite polarity. Modern sentence-similarity metrics share
this failure mode for the cases that matter most in scientific
writing — numerical changes, hedging changes, polarity flips.

**Coh-Metrix (Graesser, McNamara et al.).** [5] A research-grade
analyser that computes 200+ measures across cohesion, lexical
sophistication, syntactic complexity, narrativity, and reading
ease. Validated extensively in educational-text and second-
language-learning research. Its strength is that it goes beyond
surface readability into referential and causal cohesion. Its
weakness is the same as every other tool in this space — most
measures are noise for any specific judgement.

**LIWC (Pennebaker).** [6] Lexicon-based psycholinguistic
categorisation: words tagged into emotional, cognitive, social,
and structural categories. Used heavily in personality and
social-psychological research. For scientific writing, LIWC's
"analytic" composite has some traction (it scores formal,
hierarchical, logically structured text high) but the rest of the
categories are largely irrelevant.

### Honest assessment of what these measures provide

The composition-studies literature ([[revision-research]]) and the
cognitive-process literature ([[hayes-flower-writing-model]]) both
converge on the same point: writing quality is dimensional. There
is no single number that captures it, and any tool that produces
one is throwing information away. The useful operations are:

1. **Outlier flagging.** Catch sentences/paragraphs/sections that
   deviate sharply from the surrounding text. Extreme length,
   extreme complexity, sudden vocabulary shift.
2. **Drift detection across revisions.** Catch when a revision
   pass has changed measurable properties without intending to
   (hedging removal, terminology drift, reading-grade shift).
3. **Style-conformance diagnostics for specific genres.** Cochrane
   plain-language summaries have a target reading grade; CONSORT
   methods sections have expected vocabulary; specific journals
   have house styles. Comparison against a genre target is
   sometimes informative.

The useful operations are *not*:

- "Score this manuscript's writing quality."
- "Improve this manuscript's readability."
- "Make this section more readable."

These are theatre. They quantify the wrong things, optimise
against bad proxies, and signal effort to authors and reviewers
without correlating with actual quality.

## How this informs scriptorium

The design principle: **no general-purpose quality score in
scriptorium**, ever. Skills that produce single-number quality
scores are theatre and the project should refuse to ship them.

What scriptorium *should* do with quantitative measures:

**`outlier-sentence-detector` (candidate v0.3).** A narrow skill
that flags sentences outside reasonable distributional bounds for
their section — excessive length (e.g., >50 words), excessive
nesting depth, extreme complexity scores relative to the rest of
the section. The output is *flag-for-human-review*, not rewrite.
Calibration: distributions are computed from the manuscript itself
(or a corpus matched to its discipline) so the heuristic adapts to
the author's baseline, not to a universal target.

**`terminology-drift-detector` (already in v0.3 spec).** Catches
within-manuscript drift: a term that was "scRNA-seq" in the
introduction has become "single-cell RNA sequencing" in the
methods. This is a narrow, deterministic check; the underlying
concern is consistency, not quality. See also
[[internal-consistency]] for the bookkeeping layer this sits in.

**Hedging-preservation in transformation skills.** Skills that
modify prose should report, in their preservation report, whether
the count of hedging markers changed between input and output.
This is not a quality score; it is a *change-tracking diagnostic*
that surfaces inadvertent overclaim drift. The vocabulary used
should be Hyland-derived (see [[semantic-preservation]] open
question).

**Genre-conformance reporting (v0.3+, conditional).** If a
`lay-summary-pass` skill is built ([[plain-language-lay-summaries]]),
genre-conformance metrics (Cochrane PLS reading-grade target,
word-count limits) become *reportable* — not as quality scores,
but as conformance checks against an external standard.

**What scriptorium will *not* do (named in DESIGN.md):**

- No overall manuscript quality score.
- No "readability" rewrite that targets a Flesch-Kincaid number.
- No lexical-diversity optimisation.
- No BERTScore- or embedding-based "meaning preservation" pass/fail
  (the antonymy problem makes this irresponsible).
- No imitation of journal-house style by automated rewriting.

This is the *honest negative space* that distinguishes scriptorium
from a generic AI writing tool. The list of refused features
should appear in DESIGN.md as a positive claim about scope.

## Implementation priority for scriptorium

**Verdict:** **Selective Yes.** No general-purpose quality-score
skill — that's theatre. Narrow diagnostic skills are valuable.

**Yes-now (in scope, v0.2 / v0.3):**

- **`outlier-sentence-detector`** (v0.3 candidate): flag sentences
  outside reasonable section-local distributional bounds for human
  review. Required data: section-aware sentence segmentation, a
  distance metric (length, nesting depth), reporting interface.
  No automated rewrite.
- **`terminology-drift-detector`** (already in v0.3 spec): catch
  within-manuscript term variation. Required data: term-form
  candidate list (from frequency counts or from MANUSCRIPT_STATE
  `preferred_terms`), section-level scan.
- **Hedging-change reporting** in transformation skills (built
  into the preservation report template, v0.2): track hedge-marker
  count delta as part of the preservation report; the skill does
  not enforce a target, only reports the change. Required data:
  Hyland-derived hedging vocabulary as a bundled resource.

**No-don't-build (named explicitly):**

- General-purpose quality scoring.
- Flesch-Kincaid optimisation / target rewriting.
- Lexical-diversity-targeted rewriting.
- BERTScore- or embedding-similarity-based accept/reject for edits.

**Useful context even where no skill is built:** This document is
the basis for **the most important honest-positioning statement
in DESIGN.md** — what scriptorium will refuse to do. The refusal
list distinguishes scriptorium from generic AI writing tools and
is a defensible thought-leadership position.

## Open questions / weak evidence

- The claim that readability indices fail systematically for
  scientific text is widely repeated but the empirical literature
  formally validating this is patchier than the volume of
  commentary suggests. The strongest specific critique is in the
  technical-writing and information-design literature; the
  scientific-writing literature relies more on commentary than on
  controlled experiments. One adjacent result: Tanprasert & Kauchak
  (2021) "Flesch-Kincaid is Not a Text Simplification Evaluation
  Metric" (GEM workshop) shows Flesch-Kincaid is not a valid
  *evaluation* metric for simplification; the analogous study
  specifically validating "Flesch-Kincaid mis-scores scientific
  research articles" was not located in this sweep.
- A clean, openly-licensed machine-readable Hyland hedging-marker
  list was not located during this sweep; scriptorium would need to
  compile its own from the published taxonomy.
- LIWC requires a paid license (academic licenses sold by Receptiviti;
  commercial use requires a separate commercial license). This
  precludes bundling LIWC in scriptorium without licensing. Coh-
  Metrix is distributed by the Arizona State SoLET lab under
  research-use terms; redistribution as part of a deployed tool
  requires direct contact with the maintainers.
- The boundary between "outlier" and "stylistically unusual but
  correct" is empirical. The skill should be honest that it
  produces candidates, not verdicts.

## References

1. Flesch RF. A new readability yardstick. *Journal of Applied
   Psychology*. 1948;32(3):221–233. doi:10.1037/h0057532.
2. Kincaid JP, Fishburne RP, Rogers RL, Chissom BS. Derivation of
   New Readability Formulas (Automated Readability Index, Fog
   Count and Flesch Reading Ease Formula) for Navy Enlisted
   Personnel. Research Branch Report 8-75. Naval Technical
   Training Command, Millington TN; 1975.
3. McCarthy PM, Jarvis S. MTLD, vocd-D, and HD-D: A validation
   study of sophisticated approaches to lexical diversity
   assessment. *Behavior Research Methods*. 2010;42(2):381–392.
   doi:10.3758/BRM.42.2.381. PMID: 20479170.
4. Zhang T, Kishore V, Wu F, Weinberger KQ, Artzi Y. BERTScore:
   Evaluating text generation with BERT. *International Conference
   on Learning Representations*. 2020. arXiv:1904.09675.
5. Graesser AC, McNamara DS, Louwerse MM, Cai Z. Coh-Metrix:
   Analysis of text on cohesion and language. *Behavior Research
   Methods, Instruments, & Computers*. 2004;36(2):193–202.
   doi:10.3758/BF03195564. See also Graesser AC, McNamara DS,
   Kulikowich JM. Coh-Metrix: Providing multilevel analyses of
   text characteristics. *Educational Researcher*. 2011;40(5):
   223–234. doi:10.3102/0013189X11413260.
6. Tausczik YR, Pennebaker JW. The psychological meaning of
   words: LIWC and computerized text analysis methods. *Journal
   of Language and Social Psychology*. 2010;29(1):24–54.
   doi:10.1177/0261927X09351676. See also Pennebaker JW et al.,
   *The Development and Psychometric Properties of LIWC-22*
   (technical manual; LIWC.app).
7. Hyland K, Jiang FK. "In this paper we suggest": Changing
   patterns of disciplinary metadiscourse. *English for Specific
   Purposes*. 2018;51:18–30. doi:10.1016/j.esp.2018.04.005.
8. Hyland K. *Hedging in Scientific Research Articles*.
   Pragmatics & Beyond New Series 54. John Benjamins; 1998.
   ISBN 9789027250698. See also Hyland K. *Metadiscourse:
   Exploring Interaction in Writing*. Continuum; 2005.
9. Sand-Jensen K. How to write consistently boring scientific
   literature. *Oikos*. 2007;116(5):723–727.
   doi:10.1111/j.0030-1299.2007.15674.x.
