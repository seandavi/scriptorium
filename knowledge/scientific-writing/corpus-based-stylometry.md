# Corpus-based stylometry: what's defensible for author-voice extraction

*Last updated: 2026-10-20*

## Synthesis

Stylometry — the quantitative analysis of writing style — has a forty-year empirical track record on a *specific* problem: **discriminating one author from another** given a corpus of known-authorship text. Burrows' Delta (Burrows 2002) [^1], Hoover's vocabulary-richness measures (Hoover 2003) [^2], Argamon's stylistic-feature taxonomy [^3], and the Stamatatos 2009 survey [^4] established that function-word frequencies, character n-gram distributions, and sentence-length distributions discriminate authors reliably even in adversarial conditions (forensic linguistics, contested authorship, anonymized texts). The classic worked example is the Federalist Papers attribution problem, which Mosteller and Wallace (1964) [^5] settled by Bayesian analysis of function-word counts decades before "stylometry" was the standard term.

For scriptorium the question is *not* "can we discriminate this author from another author" — that's the well-studied problem and the answer is yes. The question is **"can we extract a profile from a 3–5 paper single-author corpus that the author recognizes as their voice and that a downstream skill can usefully consume?"** This is a harder, less-studied problem. Authorship attribution succeeds with surprisingly small training sets on function-word counts alone, but profile-for-self-recognition is a different objective: the author is not comparing themselves to another author, they are evaluating whether the profile is a faithful description of how they write. Authors are notoriously poor judges of their own writing (the curse-of-knowledge literature is one strand; the self-report-vs-corpus mismatch in writing-pedagogy is another), and the small-corpus signal-to-noise on idiosyncratic tics is lower than for population-discriminating features.

The defensible position for a scriptorium `voice-profile` skill is therefore: **extract the features stylometry has shown are robust at small corpus size — function-word distributions, sentence-length distributions, hedge / stance markers, citation-placement patterns, paragraph-opening patterns — and refuse to extract features that the literature does not support at this scale.** Argumentative-pattern claims ("how this author handles counterarguments"), authorial-intent claims, and field-or-discipline-blind voice claims all sit beyond what 3–5 papers can defensibly support.

Work published since 2025 sharpens one caveat and adds one. The sharpened caveat: LLM *editing* leaves a weaker and different stylometric trace than LLM *generation*, so a profile built from an author's recent, possibly LLM-edited papers cannot reliably separate the author's habits from the editor's [^12]. The added one: LLMs prompted with a few of a person's texts still imitate implicit personal style poorly, especially outside formal registers [^13], and the automatic metrics used to score "write like me" output correlate poorly with human judgment [^14]. Both point the same way: the author, not a metric, has to be the arbiter of whether a profile describes them.

## Evidence and frameworks

### What stylometry reliably measures

The Stamatatos 2009 survey [^4] is the canonical entry point. The features that recurrently outperform in authorship-attribution benchmarks are:

- **Function-word frequencies.** "the", "of", "and", "to", "a" — the most frequent function words carry the strongest author signal because they are used unconsciously and at high enough rates that small corpora produce stable estimates. Burrows' Delta is built on the 30–500 most frequent words.
- **Character n-grams.** Trigram and 4-gram character frequencies (including punctuation) carry surprisingly strong signal, partly because they pick up morphological and orthographic preferences below the word level.
- **Sentence-length distributions.** Mean, variance, and shape of the sentence-length distribution. Stable across genres for a given author; varies meaningfully between authors.
- **Punctuation frequencies.** Em-dash usage, semicolon frequency, parenthetical density. These are conscious-but-habitual features.
- **Part-of-speech n-grams.** Slightly more computationally expensive; useful in domains where lexical choice is genre-constrained (e.g. legal writing, abstracts).

Hoover's work on vocabulary richness [^2] adds type-token ratio variants and Yule's K as measures of lexical diversity, though these are sensitive to text length and need adjustment for short corpora.

### What stylometry struggles with at small corpus size

- **Authorial-intent and argumentative-pattern claims.** The corpus needs to be large enough to see counterarguments handled multiple times before "this author preempts counterarguments" becomes a defensible claim. 3–5 papers may show *examples* of preemption but not stable *patterns*.
- **Topic-confounded features.** A biomedical author writing about cardiology will have a different vocabulary distribution from the same author writing about oncology. Feature-extraction needs to either control for topic (function-words and POS distributions are more topic-robust) or be explicit about the field-mixing.
- **Cross-genre voice.** Grant prose, paper prose, blog prose, and README prose are different registers for the same author. The voice profile derived from one is not portable to another without explicit acknowledgment.
- **Voice-as-AI-marker confusion.** Kobak et al. (arXiv 2024; *Science Advances* 2025) [^6] documented LLM-edited writing's lexical fingerprint ("delve," "underscore," "intricate") across more than 15 million PubMed abstracts from 2010–2024, estimating that at least 13.5% of 2024 abstracts were processed with LLMs. An author whose recent papers have been LLM-edited will have a voice profile that *includes* the LLM fingerprint as if it were their own voice. The stylometric tools cannot distinguish — and the 2025–2026 evidence below shows why this is structural rather than a tooling gap.

### LLM-era evidence (2025–2026)

- **Generation and editing leave different traces.** Shan, Lee & Hao (2026) [^12] report that AI *generation* leaves a consistent "stylometric footprint" (chiefly entropy and lexical diversity) across 8 LLMs and 5 domains, but AI *editing* of human text does not reproduce it: AI-edited texts show only a small increase in lexical diversity and a decrease in entropy, with lexical density becoming the dominant editing-associated signal. In their words, stylometric features "separate AI-edited text from AI-generated text but are substantially less effective at separating it from human-written text." For a voice profile this is the relevant case: authors' papers are more likely LLM-*edited* than LLM-*generated*.
- **LLM style differs from human style beyond vocabulary.** Reinhart et al. (2025, *PNAS*) [^11] compared parallel human and LLM corpora using Biber's lexical, grammatical, and rhetorical features and found systematic differences between LLMs and humans that persist from smaller to larger models and are larger for instruction-tuned than base models. This is the verified work in the "stylistic fingerprinting of AI text" line that earlier drafts of this note (and [[ai-writing-failure-modes]]) attributed to "Reizinger 2024"; no Reizinger paper on that topic could be located.
- **Scientific prose is drifting on many axes at once.** Hubarava & Ineichen (2026; accepted at EMNLP 2026 per the arXiv record) [^15] apply interrupted time-series regression to arXiv (AI, statistics, quantitative biology) and medRxiv abstracts around the November 2022 ChatGPT release and find post-2022 changes in vocabulary, punctuation, readability, and syntax — including longer average word length and lower maximum dependency-tree depth — and conclude that isolated marker frequencies capture "only part of the shift." *Researcher inference:* a contamination check for a voice profile cannot rely on a fixed marker-word list.
- **Few-shot imitation of personal style is weak.** Wang et al. (2025; EMNLP 2025 Findings per the arXiv record) [^13] evaluated in-context imitation of more than 400 real authors' styles and found LLMs approximate style in structured formats (news, email) but struggle with nuanced, informal writing (blogs, forums). *Researcher inference:* handing a downstream skill three exemplar papers is not a substitute for an explicit, author-confirmed feature profile.
- **Automatic style metrics are not a proxy for the author.** Jangra et al. (2025; accepted at EMNLP 2026 per the arXiv record) [^14] note that existing style-personalization benchmarks and metrics have known limitations, including poor correlation with human subjects, and find that ensembles of diverse metrics consistently outperform any single evaluator (BLEU, embeddings, or LLM-as-judge).
- **LLM revision shifts voice and meaning.** Abdulhai et al. (2026, preprint) [^16] report that heavy LLM users more often said the resulting writing was "not in their voice," and that LLM revisions altered semantic meaning even when the model was asked to make only grammar edits. See [[semantic-preservation]] for the preservation side of this.

### The Hyland stance / engagement framework as the bridge

The general-stylometry literature is genre-neutral; the Hyland framework (stance: hedges, boosters, attitude markers, self-mention; engagement: reader pronouns, directives, questions) is academic-prose-specific and gives a vocabulary for the *kinds of voice signal that matter for scholarly writing* [^7] [^8]. The intersection is the right scope for a scriptorium voice profile:

- **Hedge density** (per 1000 words; types per Hyland's taxonomy). Stable at small corpus size; directly consumable by `argumentative-flow`'s hedge-preservation constraint.
- **Self-mention frequency** ("we", "the authors", passive constructions). Distinguishes authors and is corpus-stable.
- **Citation-placement pattern.** Parenthetical (Smith 2020) vs narrative (Smith 2020 showed that…) vs clause-final. Stable at small corpus size; directly consumable.
- **Attitude markers and boosters.** Less stable at small corpus size; surface but with confidence flags.

See [[esl-writers-swales-hyland]] for the deeper treatment of the Hyland framework as it bears on `argumentative-flow`; that grounding is the corresponding lens for the consumer side of a voice profile.

### Authors are imperfect judges of their own voice

Two strands of evidence:

- The expert-blind-spot / curse-of-knowledge literature ([[author-role-evidence]] section on Camerer, Loewenstein & Weber 1989 [^9]) establishes that informed agents systematically fail to predict less-informed agents' perceptions. Applied to writing: authors fail to see their own habitual patterns because they are constitutive of how they think about prose.
- The scientific-writing-pedagogy literature documents that authors describing their own voice in self-report produce a sanitised account that does not match corpus measurement. This is widely observed in writing-center practice, but the October 2026 refresh did not locate a peer-reviewed empirical study that measures the self-report-vs-corpus gap for academic authors; treat this strand as practice observation, not established finding.

The implication: a voice profile is **information the author needs to be shown**, not information the author can volunteer. The skill's job is to surface defensible signal; the author's job is to confirm, correct, or override.

## How this informs scriptorium

- **A `voice-profile` skill (v0.3, design phase per [#43](https://github.com/seandavi/scriptorium/issues/43))** should ground in the *intersection* of general stylometry and the Hyland framework. The features it extracts at v0.3 scope should be: sentence-length distribution, function-word top-K frequencies, hedge density and type, self-mention frequency, citation-placement pattern, paragraph-opening pattern. Defer argumentative-pattern claims to a later iteration or to a different (and not-yet-grounded) skill.
- **`MANUSCRIPT_STATE.yaml#author_voice` schema slot** should record the extracted profile separately from the author-declared overrides, so the author always has the last word. See the v0.3 design memo on `voice-profile` for the proposed three-layer shape.
- **Corpus provenance, not detection.** Because AI-edited text is hard to separate from human text stylometrically [^12], the skill should not try to detect and strip LLM contamination from the author's corpus. It should instead ask the author which corpus papers were LLM-edited and record the corpus date range, so the profile's provenance is explicit. (Researcher inference from [^12] and [^15].)
- **Composition with `argumentative-flow`.** A voice profile is the operational definition of "voice" that argumentative-flow's hedging-preservation constraint already partially defends. Once a profile exists, argumentative-flow can use the hedge-density target as a constraint rather than a black-box "preserve the source's hedging" rule.
- **Composition with `persona-calibration` ([#44](https://github.com/seandavi/scriptorium/issues/44))** is direct: voice profile is the independent calibration signal against which persona drift can be detected without requiring the real author's time in every checkpoint.
- **Boundary with the `humanizer` skill (an external user-side skill, not part of scriptorium):** humanizer removes AI tells (Kobak's "delve", em-dash overuse, rule-of-three); voice-profile extracts the author's signal on the *same* stylistic axis. The same em-dash in a voice profile is "this author uses em-dashes"; in a humanizer pass it's "remove em-dash overuse." The two skills should not compose into the same pipeline pass without explicit user choice about which objective wins.

## Limits and caveats

- **Population-level findings do not directly transfer to single-manuscript profiles.** The Kobak excess-vocabulary method [^6] works on 15 million abstracts; applying its logic to one author's 3–5 papers is noisy. Honest output should report confidence intervals where possible and "insufficient corpus" otherwise.
- **The corpus must be author-confirmed single-authored.** Co-authored material introduces confounding voice and should be excluded or weighted, not silently included.
- **Voice profile is not voice preservation.** Extracting that an author uses hedges at density D doesn't tell you whether the *current* manuscript should be at density D; the author's choice may legitimately vary by venue, genre, and submission iteration.
- **Detection-arms-race-with-AI-writing is out of scope.** Sadasivan et al. 2023 [^10] established that AI-text detection is fundamentally limited; a voice profile is *not* an AI-text detector and should not be marketed or used as one. The 2026 finding that AI-edited text is stylometrically close to human text [^12] reinforces this.
- **Self-recognition is the calibration target, not classification accuracy.** The literature gives strong classification results on held-out test sets; scriptorium's target is the (harder, less-studied) author-recognizes-this-as-me criterion. A profile can be classification-accurate and self-recognition-poor. Automatic style metrics do not substitute for the author's judgment [^14].

## Implementation priority for scriptorium

**Verdict:** Yes (knowledge layer for v0.3 `voice-profile` skill design and #42 persona docs). Reconsidered 2026-10-20: still holds. The 2025–2026 evidence changes the skill's corpus-intake step (record LLM-editing provenance rather than attempt detection) but not the verdict or the feature set.

**Why this layer is load-bearing:** The `voice-profile` skill is making empirical claims about what can be extracted from a small corpus. Without a grounding note, those claims are unfalsifiable. With this note, the skill's design (and the schema decisions in `MANUSCRIPT_STATE.yaml#author_voice`) can point at a specific evidence base, and contributors can argue with the feature set on evidence rather than aesthetics. This is the same posture as [[statistical-inconsistency]] grounding the future `statistics-consistency` skill.

**What this is not:** This is not a recipe for implementing stylometric measurement. The grounding answers *which features are defensible at small corpus size*; the implementation question (Burrows' Delta vs PCA on function-word counts vs simpler relative-frequency comparison; how to handle topic confounds; what baseline corpus to use) is decided in the skill, not the grounding note.

**Condition that would expand this note:** if the `voice-profile` skill grows to attempt argumentative-pattern extraction (claim-first vs evidence-first; counterargument handling) at larger corpus sizes, the note needs a section on what the literature supports at that level. Not v0.3 scope.

## Open questions / weak evidence

- **Self-recognition has no canonical empirical paper.** "Authors recognize this as their voice" is a usability criterion, not a stylometry-literature criterion. The acceptance criterion in #43 implicitly relies on this; no specific paper grounds it directly. The closest 2025–2026 work [^13] [^14] evaluates whether *generated* text matches an author's style, not whether an author recognizes a *descriptive profile* of their own style.
- **Cross-genre voice stability** is theoretically expected (function words are genre-robust) but not directly measured for the academic-paper-vs-grant-prose case. Treat as a defensible-but-not-decisive expectation.
- **The Kobak fingerprint contaminates recent authors' profiles** in ways the literature is only just beginning to characterise. Authors whose recent prose has been LLM-edited carry that signal forward. Shan et al. [^12] and Hubarava & Ineichen [^15] are the first direct evidence that editing-induced change is subtle and multi-dimensional; neither measures it at single-author scale.
- **The "Reizinger 2024" AI-text-fingerprinting citation is resolved here as unlocatable.** The verified work in that line is Reinhart et al. 2025 [^11]. [[ai-writing-failure-modes]] removed the same attribution as unresolvable in its own October 2026 refresh.
- **Empirical paper on self-report vs corpus mismatch in writing.** Practice-literature consensus exists; no peer-reviewed empirical study was located in the May 2026 pass or the October 2026 refresh. The claim is now worded as practice observation in the body text.
- **Several 2026 sources are preprints.** [^12], [^14], and [^15] carry venue acceptances only via their arXiv records; [^16] is an unrefereed preprint. Re-check their published versions at the next refresh.

## References

[^1]: Burrows, J. (2002). 'Delta': A Measure of Stylistic Difference and a Guide to Likely Authorship. *Literary and Linguistic Computing*, 17(3), 267–287. DOI: 10.1093/llc/17.3.267.

[^2]: Hoover, D. L. (2003). Another perspective on vocabulary richness. *Computers and the Humanities*, 37(2), 151–178. DOI: 10.1023/A:1022673822140.

[^3]: Argamon, S., Koppel, M., Pennebaker, J. W., & Schler, J. (2009). Automatically profiling the author of an anonymous text. *Communications of the ACM*, 52(2), 119–123. DOI: 10.1145/1461928.1461959. (Representative of Argamon's broader stylistic-feature line of work; see also the Argamon-led JASIST work on text genre and gender attribution.)

[^4]: Stamatatos, E. (2009). A survey of modern authorship attribution methods. *Journal of the American Society for Information Science and Technology*, 60(3), 538–556. DOI: 10.1002/asi.21001.

[^5]: Mosteller, F., & Wallace, D. L. (1964). *Inference and Disputed Authorship: The Federalist*. Addison-Wesley. (Reissued by CSLI Publications, David Hume Series, ISBN 9781575865522.) The foundational worked example for function-word-based authorship attribution.

[^6]: Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Science Advances*, 11(27), eadt3813. DOI: 10.1126/sciadv.adt3813. Preprint: arXiv:2406.07016 (first posted 2024 as "Delving into ChatGPT usage in academic writing through excess vocabulary").

[^7]: Hyland, K. (2005). Stance and engagement: a model of interaction in academic discourse. *Discourse Studies*, 7(2), 173–192. DOI: 10.1177/1461445605050365.

[^8]: Hyland, K. (1999). Academic attribution: citation and the construction of disciplinary knowledge. *Applied Linguistics*, 20(3), 341–367. DOI: 10.1093/applin/20.3.341.

[^9]: Camerer, C., Loewenstein, G., & Weber, M. (1989). The Curse of Knowledge in Economic Settings: An Experimental Analysis. *Journal of Political Economy*, 97(5), 1232–1254. DOI: 10.1086/261651.

[^10]: Sadasivan, V. S., Kumar, A., Balasubramanian, S., Wang, W., & Feizi, S. (2023). Can AI-Generated Text Be Reliably Detected? arXiv:2303.11156. (The arXiv record states the paper was published in *Transactions on Machine Learning Research*.)

[^11]: Reinhart, A., Markey, B., Laudenbach, M., Pantusen, K., Yurko, R., Weinberg, G., & Brown, D. W. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. *Proceedings of the National Academy of Sciences*, 122(8), e2422455122. DOI: 10.1073/pnas.2422455122. Preprint: arXiv:2410.16107.

[^12]: Shan, Z., Lee, Y., & Hao, S. (2026). AI Writers Have a Consistent Stylometric Footprint, but AI Editors Do Not. arXiv:2608.27855 (arXiv comment: EMNLP 2026 Main).

[^13]: Wang, Z., Tripto, N. I., Park, S., Li, Z., & Zhou, J. (2025). Catch Me If You Can? Not Yet: LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors. arXiv:2509.14543 (arXiv comment: EMNLP 2025 Findings).

[^14]: Jangra, A., Sarrafzadeh, B., Cucerzan, S., de Wynter, A., & Jauhar, S. K. (2025). Evaluating Style-Personalized Text Generation: Challenges and Directions. arXiv:2508.06374 (arXiv comment: accepted to EMNLP 2026 main).

[^15]: Hubarava, H., & Ineichen, B. V. (2026). Accelerated Drift of Scientific Prose in the LLM Era: Evidence from an Interrupted Time-Series Analysis. arXiv:2610.26008 (arXiv comment: accepted at EMNLP 2026).

[^16]: Abdulhai, M., White, I., Wan, Y., Qureshi, I., Leibo, J. Z., Kleiman-Weiner, M., & Jaques, N. (2026). How LLMs Distort Our Written Language. arXiv:2603.18161. Preprint.

See also: [[esl-writers-swales-hyland]], [[ai-writing-failure-modes]], [[author-role-evidence]], [[semantic-preservation]].
