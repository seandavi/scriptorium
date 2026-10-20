# Semantic preservation: how to think about "preserving meaning" measurably

*Last updated: 2026-10-20*

## Synthesis

Transformation skills that promise to "compress" or "improve flow"
without altering meaning are making a strong claim — and "meaning"
is harder to operationalize than the casual usage suggests. The
translation-studies literature has wrestled with this for decades:
Nida's distinction between *formal equivalence* (preserving surface
form) and *dynamic equivalence* (preserving reader response) and the
Skopos school's emphasis on *function in target context* are the
intellectual ancestors of any serious account of "did the meaning
survive the edit." The computational literature offers a different
toolkit — sentence embeddings, BERTScore, and related metrics — that
can quantify surface-level semantic overlap. These metrics are
documented to be insensitive to some of the cases that matter most:
negation [^4] and numerical changes [^5]. Hedging changes are a
plausible further weak spot, but this note has no direct source for
that (researcher inference).

The practical posture scriptorium adopts is **conservative preservation
by structured invariants**, not measured similarity. Rather than
trusting an embedding-distance metric to tell us whether an edit
preserved meaning, the system declares specific
structured artifacts — citations, statistics, terminology, claim
strings — that *must* be preserved verbatim or with explicit
authorization. This is a coarser but more reliable approach: it
catches the failure modes that matter most for scientific manuscripts
and degrades gracefully when the model's "meaning preservation" is
worse than promised.

## Evidence

**Nida's formal vs. dynamic equivalence (Nida 1964, *Toward a Science
of Translating*; refined as functional equivalence in later work).**
Nida framed translation as a choice between preserving the *form* of
the source (word order, syntax, lexical correspondence) and
preserving the *effect on the reader* (idiomatic adaptation, cultural
substitution, register shifts). Dynamic equivalence was meant to
prioritize reader response: a translation succeeds if the target-
language reader is moved or informed the way the source-language
reader was.[^1]

For scientific editing, dynamic equivalence is the *wrong* target.
A scientific manuscript's "meaning" is not its reader's emotional
response — it is the specific propositional content of its claims,
methods, results, and citations. Formal equivalence — preserving
that propositional content exactly — is closer to the right standard.
This is why scriptorium's preservation rules are structural
("preserve every citation, preserve every statistic") rather than
holistic ("preserve the spirit").

**Skopos theory (Vermeer, Reiss, Nord).** The functionalist German
translation school argues that translation is determined by the
*purpose* (skopos) of the target text in its target context. Three
rules: skopos (purpose), coherence (target text is comprehensible),
and fidelity (intertextual coherence with source).[^2]

For scriptorium, the relevance is that **edits should be evaluated
against the manuscript's purpose**, which is encoded in
`MANUSCRIPT_STATE.yaml` (`target_venue`, `target_type`, `core_claims`).
A compression that drops a hedging adverb is a different edit
depending on whether the target venue values precision over brevity
or vice versa. Skopos gives us the language to talk about this:
*purpose-relative preservation*, not absolute preservation.

**Computational semantic similarity: sentence embeddings.** Modern
embedding models (SBERT, OpenAI's text-embedding-3-*, etc.) project
sentences into vector space where cosine similarity correlates with
semantic similarity. For paraphrase detection and rough relatedness,
these metrics work well. They are insensitive to surface form —
which is the goal — and capture semantic equivalence across
synonyms.

**BERTScore (Zhang et al. 2020, ICLR).** Computes token-level
embedding similarity between candidate and reference sentences,
weighted by inverse document frequency. Outperforms n-gram metrics
(BLEU, ROUGE) on tasks where meaning matters more than surface
wording. Widely used for summarization and machine translation
evaluation.[^3]

But — and this is the load-bearing limitation — BERTScore and other
BERT-based metrics are insensitive to negation. Anschütz et al.
(2023) summarise prior work showing that models such as BERT "lack
understanding of negated phrases and do not attribute sufficient
importance to the word 'not'". They conclude that "learned
evaluation metrics based on these models are insensitive to
negations".[^4] The minimal-pair studies they review, including the
DEMETR benchmark, tested BERTScore and other metrics on negation and
antonym perturbations, and found that most metrics "struggle to
detect negations".[^4] Numbers are a second documented weak spot:
BERTScore "exhibits low sensitivity to numerical variation".[^5]
Two illustrative cases (researcher examples, not measured results):
"the best treatment" and "the worst treatment" differ by one
polarity-bearing token in an otherwise identical context; "p < 0.05"
and "p < 0.5" differ by one character but make profoundly different
scientific claims.

For scientific manuscripts, the differences that matter are exactly
the differences embedding metrics handle worst: numerical changes,
hedging strength, polarity, scope of claims. A revision that flips
"we observed an effect" to "we did not observe an effect" could
still receive a high BERTScore (an illustration, not a measured
figure) — and be catastrophically wrong.

**Why diff-size is not preservation.** A small textual diff and a
preserved meaning are *not the same thing*. Single-word changes can
reverse polarity ("can" → "cannot"), strengthen claims ("suggests" →
"proves"), or change quantities. Trusting "small diff = meaning
preserved" is a particularly seductive failure mode because diffs
*look* informative — they show the user exactly what changed — while
hiding *why* the change matters.

**Practical heuristics for structured preservation.** The translation-
quality-assurance literature, and the editing-checklist tradition
described in [[copyediting-vs-developmental]], converge on a set of
structured invariants that map well to scientific writing:

- **Claim-set preservation.** Every assertion in the input must be
  present in the output, in equivalent strength. Hedging changes
  (e.g., "suggests" → "shows") count as claim changes.
- **Statistic-string preservation.** Every numerical value, p-value,
  effect size, confidence interval, and sample size must be
  byte-identical in input and output.
- **Citation-set preservation.** Every citation key/DOI present in
  the input must be present in the output, attached to a
  semantically compatible claim.
- **Terminology preservation.** Terms declared in
  `MANUSCRIPT_STATE.yaml` (preferred terms; forbidden terms) must
  obey the declared rules.
- **Section-boundary preservation.** Without explicit license, a
  transformation skill must not move content across section
  boundaries.

These invariants are coarse compared to "meaning preservation in the
full philosophical sense," but they are *checkable* — and they
collectively cover the failure modes that produce real scientific
harm.

## How this informs scriptorium

**`MANUSCRIPT_STATE.yaml` preservation constraints are the operating
contract.** The fields `preserve_citations`, `preserve_statistics`,
`preserve_terminology`, `avoid_hype` are not aspirational defaults;
they are checkable invariants that transformation skills must respect
and that the orchestrator can verify post-edit. Verification is by
structured comparison — citation set membership, statistic-string
exact match, terminology-rule conformance — not by embedding
similarity.

**Skills emit a structured preservation report.** When a
transformation skill modifies prose, its output includes a
preservation-report section: claims preserved, claims modified
(with rationale), statistics preserved (exact-match count), citations
preserved (set-equality check), terminology compliance. The author
inspects the report alongside the prose diff.

**Semantic similarity metrics are an *aid*, not a check.** Where
sentence-level cosine similarity is below some threshold, that is
informative — but only as a hint to look at the change. The decision
to accept the edit is the author's, informed by the structured
preservation report, not by an embedding score.

**Translate, don't transform.** Nida's framing is useful: scriptorium
transformation skills are doing something more like *formal-
equivalence translation* than like *editorial rewriting*. The output
should be defensibly the *same text*, with specific declared changes,
not a *better text* that happens to share content. This framing
keeps the conservative-edit posture honest.

**Mossop's logic and accuracy parameters (see
[[copyediting-vs-developmental]]) are the failure-mode vocabulary.**
A preservation violation is a *Logic* or *Accuracy* failure under
Mossop's twelve-parameter system. The vocabulary is shared with the
broader editing tradition; the scriptorium contract is just a
machine-checkable subset of it.

## Open questions / weak evidence

- The set of structured invariants above is plausibly sufficient for
  most scientific manuscripts; whether it is *demonstrably*
  sufficient — i.e., whether respecting all five invariants
  guarantees acceptable meaning preservation across realistic edits —
  is an empirical question that scriptorium's Venice paper case
  study and subsequent evaluations should help answer.
- Hedging-strength changes ("suggests" → "demonstrates") are the
  hardest category to detect automatically. A vocabulary of hedge
  markers (Hyland's hedging taxonomy, etc.) could feed a future
  `hedging-preservation` check. Hyland's categories (modal verbs,
  epistemic lexical verbs, epistemic adjectives, epistemic adverbs,
  epistemic nouns; boosters: *demonstrate*, *prove*, *establish*,
  *clearly*, *certainly*) are well-defined in the published work
  and can be operationalised manually; no canonical openly-licensed
  machine-readable list was located in this sweep, so any in-skill
  list will be a project-compiled distillation.
- Embedding-based metrics may be useful for *triage* — flagging
  paragraphs where similarity is unexpectedly low — even if they
  cannot serve as accept/reject criteria.
- No source in this note measures embedding-metric sensitivity to
  hedging-strength changes specifically. The negation and numerical
  evidence [^4], [^5] makes it plausible, but it is not shown.

## References

[^1]: Nida EA. *Toward a Science of Translating*. Brill; 1964.
    The dynamic-equivalence framing was refined in later work
    (Nida & Taber, *The Theory and Practice of Translation*, 1969);
    "dynamic" was later relabeled "functional" equivalence.

[^2]: Vermeer HJ. Skopos and commission in translational action. In:
    Venuti L, ed. *The Translation Studies Reader*. Routledge;
    2000:221–232. See also Nord C. *Translating as a Purposeful
    Activity*. St Jerome; 1997. ISBN 978-1900650021.

[^3]: Zhang T, Kishore V, Wu F, Weinberger KQ, Artzi Y. BERTScore:
    Evaluating text generation with BERT. *International Conference
    on Learning Representations*. 2020. arXiv:1904.09675.

[^4]: Anschütz M, Miguel Lozano D, Groh G. This is not correct!
    Negation-aware evaluation of language generation systems. In:
    *Proceedings of the 16th International Natural Language
    Generation Conference (INLG 2023)*. Association for
    Computational Linguistics; 2023:163–175.
    DOI: 10.18653/v1/2023.inlg-main.12. arXiv:2307.13989.
    Its related-work section reviews the minimal-pair studies,
    including Karpinska M, Raj N, Thai K, Song Y, Gupta A, Iyyer M.
    DEMETR: Diagnosing evaluation metrics for translation. In:
    *Proceedings of EMNLP 2022*:9540–9561.
    DOI: 10.18653/v1/2022.emnlp-main.649. arXiv:2210.13746.
    (Added 2026-10-20. The note previously described a "documented
    antonymy problem" with no direct source; the negation evidence
    here replaces it. No source was found that measures antonym
    pairs such as "best"/"worst" on their own, so that example is
    now labelled illustrative.)

[^5]: Huang Y-S, Lee Y-Y, Chou T-H, Lin C, Wang C-J. FinNuE:
    Exposing the risks of using BERTScore for numerical semantic
    evaluation in finance. arXiv:2511.09997 (2025; FinAI@CIKM 2025
    workshop, non-archival). It reports that BERTScore "exhibits
    low sensitivity to numerical variation" and often assigns high
    similarity to numerically divergent text pairs. (Corrected
    2026-10-20: FinNuE was previously attributed to "Sun et al."
    and listed as an antonymy critique. It is by Huang et al. and
    concerns numerical, not polarity, insensitivity.)
