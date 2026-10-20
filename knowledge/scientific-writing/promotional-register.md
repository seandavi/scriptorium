# Promotional and transactional register

*Last updated: 2026-10-20*

## Synthesis

Academic prose degrades in a characteristic direction under both LLM assistance
and ordinary authorial enthusiasm: it starts *asserting value* where it should
*state fact*. The tell is not a vocabulary list, though vocabulary is the
visible symptom. It is a grammatical move — the sentence takes a position on how
good, important, or advantageous something is, in a place where the reader only
needed to know what it is.

The empirical trend is well documented. Vinkers, Tijdink and Otte analysed all
PubMed abstracts from 1974 to 2014 and found the absolute frequency of
preselected positive words rose from **2.0% (1974–80) to 17.5% (2014)**, a
relative increase of 880%, with the sharpest movement in *robust*, *novel*,
*innovative*, and *unprecedented* — up to a 15,000% relative increase
individually [^1]. Neutral and randomly selected words showed no comparable
rise, and neither did the Google Books corpus over the same period, so this is
specific to scientific writing rather than a general drift in English. The
effect was stronger for authors at institutions in countries where English is
not the majority language, which matters for how scriptorium handles it (see
*Open questions*, and [[esl-writers-swales-hyland]]).

LLM assistance accelerates the same drift from a different direction. Where the
human version is enthusiasm, the machine version is a learned register: models
trained on persuasive web text default to constructions that sell. The result
converges on the same surface features, which is why a single catalog serves
both.

The distinction that makes this tractable: **promotional register is not the
same as a significance claim.** A significance claim is a load-bearing,
falsifiable statement about why work matters, and it belongs in the abstract,
the significance statement, and the aims page — see [[significance-positioning]].
Promotional register is what fills the space when a significance claim is
*asserted rather than made*. Removing the latter usually strengthens the former,
because the real claim stops competing with decoration.

## Evidence and frameworks

### The transactional construction

The most durable of these constructions frames a design decision as a
transaction the reader benefits from. It reads as a pitch even when the
underlying fact is unremarkable.

| Transactional | Plain |
|---|---|
| "It is worth stating what this buys." | "This recovers approximately 1.5–2 days of contact time." |
| "This earns its keep by…" | "This is used for…" |
| "X pays for itself in…" | "X takes N hours and replaces M." |
| "What you get from this is…" | "This produces…" |

The construction is easy to detect because it requires a beneficiary. Prose that
names who benefits from a methodological choice, rather than what the choice
does, has switched register.

### Superlative self-assessment

A ranking claim the author is not positioned to make, and which no reader can
check.

| Superlative | Plain |
|---|---|
| "the best worked example anywhere in the curriculum" | "this material demonstrates the approach on data the instructors know in detail" |
| "the clearest available lesson in X" | "a direct application of X" |
| "the single change most likely to…" | "this makes the course cumulative because…" |
| "the strongest argument for…" | "one argument for… is" |

These differ from legitimate comparison: *"a modular format cannot carry a
sustained argument across one dataset; two residential weeks can"* is a
checkable structural claim. *"the sharpest distinction"* is not.

### Value assertion in place of statement

The sentence stops describing and starts appraising, usually with an evaluative
noun or a copula-plus-judgment.

| Asserted | Stated |
|---|---|
| "This also raises the floor." | "Trainees begin from a common baseline." |
| "The scarce skill is no longer execution." | "What remains difficult is determining whether the answer is correct." |
| "This supplies the check." | "This course teaches that evaluation." |
| "X does more work than a week of lectures." | *(cut; unmeasurable)* |
| "the durable outcome of the training" | "trainees can apply the questions to a method they have not seen" |
| "makes weak use of a scarce resource" | "produces limited engagement" |
| "sits least comfortably with what the course is for" | "is not statistical, and the course has limited time" |

### The high-frequency vocabulary

The default catalog, consistent with the AI-tell catalogs in
[[ai-writing-failure-modes]]: *robust* (outside its precise statistical sense),
*novel*, *innovative*, *unprecedented*, *cutting-edge*, *state-of-the-art*,
*world-class*, *revolutionize*, *transformative* (outside proposal vision
language, below), *seamless*, *pivotal*, *crucial*, *key* (adjectival),
*leverage*, *landscape* (abstract), *ecosystem*, *paradigm*, *showcase*,
*underscore*, *testament*, *delve*. The entries differ in how well they are
grounded:

- **Pre-LLM positive-word trend [^1]:** *robust*, *novel*, *innovative*,
  *unprecedented* (the four words with the sharpest rise among Vinkers'
  25 preselected positive words).
- **LLM-era excess style words in PubMed abstracts [^3]:** *crucial* (named in
  the main text as a common excess word, δ=0.037, and one of the 10-word common
  marker set); and, in the full list of 291 rarer 2024 excess style words
  (Fig. S6 of the arXiv v5 preprint), *pivotal*, *seamless*/*seamlessly*,
  *revolutionize*/*revolutionizing*, *transformative*, *leverages*/*leveraging*,
  *innovative*, *showcased*/*showcases*/*showcasing*,
  *underscore*/*underscores*/*underscored*/*underscoring*, and
  *delve*/*delves*/*delved*/*delving*. Kobak et al. count inflections
  separately, so the catalog's lemma (e.g. *leverage*) stands in for the listed
  forms. *Innovative* is backed by both studies.
- **Practice-derived only:** *cutting-edge*, *state-of-the-art*,
  *world-class*, *key*, *landscape*, *ecosystem*, *paradigm*, *testament*. None
  of these appears in Fig. S6 or in the main-text examples of [^3], and none is
  among the four words [^1] highlights. They come from the practice-derived
  catalogs, not from either corpus study.

### What this catalog must not touch

Three legitimate registers that a naive promotional-language filter will damage:

1. **Significance claims proper.** Covered by [[significance-positioning]].
   A grant or abstract that states why the work matters is doing required work.
2. **Funding-proposal vision language.** Proposals are evaluated on vision plus
   feasibility, not on finished results. "Long-term goal", "establish a
   foundation", and "transformative" are appropriate in an aims page or project
   summary *when a credible plan backs them*. The discipline for proposals is
   claim ↔ feasibility, not claim ↔ evidence; see [[grant-writing-evidence]] and
   [[nih-significance-patterns]]. A promotional-register pass run against a
   proposal must exempt the vision statement and audit feasibility instead.
3. **Evidence-tied hedging and boosters.** Hyland's metadiscourse work [^2] treats
   boosters ("clearly", "demonstrates") as a normal resource for staking a claim
   at its warranted strength. The defect is a booster *stronger than its
   evidence*, not the presence of boosters. See [[esl-writers-swales-hyland]].

## How this informs scriptorium

**`terminology-normalization` is the natural home.** The skill already enforces
`terminology.forbidden` from `MANUSCRIPT_STATE.yaml`, but it depends entirely on
the author supplying the list. In practice authors do not arrive with one; they
arrive with an instruction like *"drop the jargon."* This document supplies a
**default catalog** the skill can offer when `terminology.forbidden` is absent
or thin, so the skill is useful on first contact.

**The mechanism, not the list, is the contribution.** Field observation from the
first production use of scriptorium on a grant (C-DATA R25, Aug 2026): an
instruction to avoid a register decays across revision passes, because nothing
in the loop remembers it. The same instruction written into
`terminology.forbidden` becomes a **checkable gate** — a grep against the
declared list, run after every pass, independent of model recall. This is the
same property that makes `constraints.preserve_citations` work: the audit is
mechanical, so the claim is falsifiable rather than asserted. Externalising a
style constraint into declared state is what converts it from a preference into
a contract.

**`init` should offer the seed.** When an author declares
`project.target_type`, `init` can propose the relevant subset of this catalog
(full for manuscripts; vision-exempt for grants) as a starting
`terminology.forbidden`, which the author then edits. Proposing beats requiring:
the list is domain-sensitive, and *robust* is a legitimate technical term in a
statistics manuscript.

**Suggest, never auto-apply.** Consistent with the skill's existing constraint
and with `declared-work-scope`. Several entries above are judgment calls, and a
few — "raises the floor", "the scarce skill" — are defensible in some voices.

## Implementation priority for scriptorium

**Verdict:** Yes (knowledge layer + default catalog for `terminology-normalization`
and `init`). No (not a skill of its own). Reconsidered 2026-10-20: still holds.
As of this date `terminology-normalization` does not yet ground in this note or
ship a default catalog, so the "Yes" remains pending work rather than shipped.

**Yes — grounding and default data:** wire into `terminology-normalization` as
the source of its default forbidden catalog, and into `init` as the seed it
proposes at state-bootstrap time. Both are additive and neither changes existing
behavior when the author has already declared a list.

**No — dedicated skill:** a `promotional-register` skill would overlap
`terminology-normalization` almost completely. The gap being filled is *data the
existing skill lacks*, not a missing capability.

**Maybe later:** if `outlier-sentence-detector` gains a register dimension, the
value-assertion patterns above are a better signal than vocabulary frequency,
because they are structural and survive synonym substitution.

## Open questions / weak evidence

- **The catalog is practice-derived, not measured.** [^1] establishes the
  vocabulary trend empirically. The three *constructions* above (transactional,
  superlative self-assessment, value assertion) come from editorial observation
  during scriptorium's own use, not from a corpus study. They are stable and
  easy to detect, but no one has measured whether removing them changes reviewer
  assessment.
- **No evidence that promotional register harms outcomes.** The plausible story
  is that it costs credibility with expert readers, but [^1] deliberately stops
  at documenting the trend and asks whether the perception fits reality. Do not
  claim a review-score effect.
- **The non-native-English finding cuts against aggressive enforcement.** [^1]
  found authors outside majority-English countries used significantly more
  positive words. Per [[esl-writers-swales-hyland]], stance and intensity
  patterns vary legitimately across linguistic backgrounds, and a filter tuned
  to one register will disproportionately flag another author's normal prose.
  This is an argument for proposing rather than enforcing, and for keeping the
  author's declared list authoritative over the default.
- **Discipline variance is unmeasured here.** *Robust*, *novel*, and *key* carry
  precise meanings in statistics, chemistry, and cryptography respectively. The
  default catalog needs per-discipline exemptions that this document does not
  yet supply; see [[discipline-conventions]].
- **LLM marker words drift.** [^3] reports a lower bound of 13.5% of 2024
  PubMed abstracts processed with LLMs, inferred from excess style words; a
  2026 preprint on arXiv and medRxiv abstracts finds some LLM-associated lexical
  markers rising persistently and others rising then receding (Hubarava &
  Ineichen, arXiv:2610.26008; see [[corpus-based-stylometry]]). A fixed default
  list will age; date it and refresh it.

## References

[^1]: Vinkers CH, Tijdink JK, Otte WM. Use of positive and negative words in
    scientific PubMed abstracts between 1974 and 2014: retrospective analysis.
    *BMJ*. 2015;351:h6467. doi:10.1136/bmj.h6467. PMID 26668206.
    Retrospective analysis of all PubMed abstracts 1974–2014; 25 preselected
    words per category plus 100 random words, normalised to abstract count,
    with Google Books Ngram as a general-English control.

[^2]: Hyland K. *Metadiscourse: Exploring Interaction in Writing*. Continuum;
    2005. ISBN 9780826476104 (hardback); 9780826476111. The hedges-and-boosters
    framing this document relies on for the distinction between a booster and
    an overclaim.

[^3]: Kobak D, González-Márquez R, Horvát E-Á, Lause J. Delving into
    LLM-assisted writing in biomedical publications through excess vocabulary.
    *Science Advances*. 2025;11(27):eadt3813. doi:10.1126/sciadv.adt3813.
    Preprint arXiv:2406.07016. Excess-word analysis of over 15 million PubMed
    abstracts from 2010–2024. Word-level grounding above is from the arXiv v5
    HTML: main-text excess words (§2.1–2.2) and Fig. S6, "All 291 excess style
    words in 2024 with frequency below 0.02".
