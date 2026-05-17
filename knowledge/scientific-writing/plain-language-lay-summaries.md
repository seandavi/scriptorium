# Plain language and lay summaries in scientific writing

*Last updated: 2026-05-17*

## Synthesis

Plain-language writing — the practice of communicating with non-
expert audiences using familiar vocabulary, short sentences, and
clear structure — has migrated from a fringe communication concern
to a policy and funding requirement. The Plain Writing Act of 2010
(US Public Law 111-274) [1] mandates plain writing in US federal
agency public communication. The EU Clinical Trials Regulation
536/2014 [2] requires lay summaries for every clinical trial
conducted in EU member states. The Wellcome Trust, MRC, NIHR, and
other major funders require lay summaries on grant applications [3].
Cochrane has mandated plain-language summaries for every systematic
review since 2013 [4]. PLOS journals require an Author Summary (a
non-technical summary of findings) for original research [5]. The
NIH Clear Communication initiative is the dominant US-side
infrastructure for plain-language public-facing research
communication [6].

The relevant point for scriptorium is that lay-summary writing is
a **distinct genre with codified expectations**, not a "simpler
abstract." Cochrane plain-language summaries follow specific
templates with a "key messages" section, a clearly headed
intervention/comparison/outcome structure, GRADE language
translation, and length norms (~400–700 words). EU CTR lay
summaries follow regulator-specified content checklists. Funders
score lay summaries explicitly. A skill that purports to
"simplify" a manuscript without respecting these genre conventions
produces something that looks like a plain-language summary but is
not — it is a stylistically simplified abstract, which is a
different artefact.

Whether scriptorium should build a `lay-summary-pass` skill depends
on demand. The skill is technically tractable (LLMs do
register-shift comparatively well), and the genre conventions are
well-codified. But author-side demand is concentrated in regulated
genres (clinical trials, Cochrane reviews, certain funded grant
schemes); a general-purpose research paper does not typically need
a lay summary at submission. The right call for v0.1/v0.2 is to
note the skill as a maybe-later candidate, watch for
funder-requirement signals, and design MANUSCRIPT_STATE to
accommodate the skill without requiring it.

## Evidence and frameworks

### Policy mandates

**Plain Writing Act of 2010 (US Public Law 111-274).** [1] Signed
13 October 2010. Requires federal agencies to use "plain writing"
— clear, concise, well-organised, audience-appropriate — in every
covered document. Agencies must designate plain-writing leads,
maintain plain-writing sections on their websites, and report
annually on compliance. The Act applies to federal communication;
its indirect effect on US-based researchers is through the agencies
that fund them (NIH, NSF, CDC, FDA) and that increasingly require
plain-language elements in their applications and outputs.

**EU Clinical Trials Regulation 536/2014.** [2] Applies to all
clinical trials conducted in EU/EEA member states (in force since
January 2022). Sponsors must submit, within one year of trial
completion (six months for paediatric trials), a lay summary
written so as to be understandable to non-specialists. Content is
regulator-prescribed: identification, sponsor, scientific
information, population, IMPs, adverse reactions, overall results,
interpretation, planned follow-up, where to find more information.
Summaries must be translated into the languages of the participating
member states. This is the most operationally consequential
lay-summary requirement currently in force; non-compliance has
regulatory consequences.

**NIH Clear Communication and plain-language guidance.** [6] The
NIH Office of Communications and Public Liaison maintains plain-
language guidance for NIH-produced public-facing materials. The
guidance is internal-facing but is widely cited as the de facto
standard for NIH-funded researcher communication: average 20 words
per sentence, one idea per sentence, one topic per paragraph, key
message first. National Cancer Institute's *Clear & Simple*
materials extend the guidance to low-literacy audiences.

**Funder requirements.** [3] The Wellcome Trust requires a plain-
language summary on grant applications (typically 200–300 words).
NIHR (UK), MRC (UK), CIHR (Canada), NHMRC (Australia), and the
European Research Council have similar requirements with varying
length and content specifications. The Wellcome public-engagement
funding scheme is a notable extension: lay summaries are not just
required, they are evaluated by lay-reviewer panels.

### Practitioner standards

**Cochrane plain-language summaries.** [4] Cochrane has mandated PLS
for every systematic review since the early 2010s; the standards
have evolved through "PLEACS" (Plain Language Expectations for
Authors of Cochrane Summaries) into the current handbook guidance.
Current template: 400–700 words, standardised headings, top-line
"Key messages" (2–3 short bullets), explicit GRADE-language
translation ("we are confident that…", "we are not confident
because…"), search date stated, technical terms avoided. The
Cochrane standards are the most rigorously documented genre
conventions for plain-language summaries; they are the natural
reference if scriptorium ever builds a lay-summary skill.

**PLOS Author Summaries.** [5] PLOS Biology, PLOS Medicine, and PLOS
Computational Biology require an Author Summary for original
research. The summary appears immediately after the abstract and is
intended to be accessible to non-experts in the immediate field.
The PLOS guidance specifies that it must address what the work
contributes, why it matters, and what readers should take from it,
without jargon. The length norm is roughly 150–200 words.

### Science-communication research

**Bubela et al. (2009), "Science communication reconsidered."** [7]
The interdisciplinary consensus paper that consolidated a generation
of science-communication thinking. The paper articulates a
post-deficit-model view: the public is not an empty vessel into
which science can be poured, and communication that treats it that
way fails. Effective science communication accounts for the
audience's existing schemas, values, and contexts.

**Brossard and Lewenstein (2010).** [8] The canonical critique of
the **deficit model** of public understanding of science. Identifies
four models: deficit (give them facts), contextual (situate the
facts in audience-relevant frames), lay-expertise (recognise that
non-specialists have relevant knowledge), and public participation
(engage the audience as participants, not recipients). The
implication for plain-language writing: a lay summary that simply
strips jargon and shortens sentences from a research paper is a
deficit-model artifact. A *good* lay summary translates content
into the audience's frame — addressing their actual questions,
explaining the trade-offs, situating the work in their decision
context.

### Tools and metrics

**Readability indices** (Flesch Reading Ease, Flesch-Kincaid Grade
Level, SMOG, Gunning Fog, Coleman-Liau) are widely used as
automated plain-language proxies. They are well-validated for
target audiences (originally military training materials and
public health pamphlets) but **fail systematically for scientific
text**. The reasons are detailed in [[quantitative-quality-measures]]:
the formulas inflate difficulty for correctly used technical
vocabulary; they are insensitive to genuine cognitive complexity
beyond syllables-and-sentence-length. They are useful as outlier
flags ("this passage is at grade 18, suspiciously high even for
your audience") but not as quality scores.

**Hemingway Editor** is the most visible practitioner tool in the
plain-language space. Its core heuristic — flag long sentences,
passive voice, adverbs, complex words — is a useful triage layer
but, like the indices, it is genre-naive and produces false
positives on legitimate scientific prose.

## How this informs scriptorium

A `lay-summary-pass` skill, if built, would need to do four things
the existing transformation skills do not do:

1. **Genre-conform** to a target standard (Cochrane PLS, EU CTR,
   PLOS Author Summary, Wellcome lay summary). The target is a
   MANUSCRIPT_STATE field, e.g. `lay_summary_target: cochrane-pls |
   eu-ctr | plos-author-summary | wellcome | nih-public | custom`.
2. **Register-shift** without removing technical content the lay
   reader needs (effect direction, certainty language, what was
   measured). This is *not* the same as compression; it is closer
   to translation. Skopos-theoretic framing in
   [[semantic-preservation]] is the right intellectual model:
   purpose-relative preservation.
3. **Preserve numeric findings** with appropriate framing. Effect
   sizes should be presented in audience-meaningful units (natural
   frequencies, absolute risk reductions, NNTs where appropriate).
4. **Cite, but for non-specialists.** A lay summary does not have a
   formal bibliography, but it must not invent claims and must point
   to where the technical findings can be verified.

The preservation contract for a lay-summary skill is *different* from
the contract for compression/flow skills. Section-boundary
preservation is irrelevant (the lay summary is a separate artefact).
Statistic-string preservation needs adaptation rules
("p<0.05" → "the result was statistically significant"; numeric
effect sizes preserved with appropriate denominators). Citation
preservation becomes "all *claims* must be supported by the source
paper", not "all citation keys must remain intact." The skill needs
its own preservation report variant.

The risks of getting a lay-summary skill wrong are non-trivial:

- **Overclaim drift.** Plain-language phrasing tends to drop hedges
  ("may improve" → "improves"). This is exactly the
  citation-overreach failure mode ([[citation-overreach-research]])
  that scriptorium's `avoid_hype` constraint is meant to prevent.
- **Deficit-model artefact.** A skill that mechanically strips
  jargon and shortens sentences without addressing the audience's
  frame produces simplified scientific prose, not a lay summary.
  Brossard and Lewenstein [8] is the warning.
- **Misleading numeric framing.** Relative risk reductions sound
  larger than absolute risk reductions; NNT framings are more
  honest. A lay-summary skill must default to honest framing.

## Implementation priority for scriptorium

**Verdict:** **Maybe later** — a dedicated `lay-summary-pass` skill
is plausible but not v0.1.

**Condition that would flip to Yes:**

- Funder mandates expand and authors begin asking for explicit
  lay-summary tooling. Evidence: NIH adds a lay-summary section to
  the standard application; NSF adopts something similar; UK funders
  tighten enforcement of existing requirements.
- A Cochrane-affiliated or systematic-review-focused user community
  surfaces as a scriptorium audience. Cochrane PLS is the most
  rigorously specified target and the most natural first build.
- Evidence accumulates that LLM-generated lay summaries
  systematically inflate certainty (per [[citation-overreach-research]]
  reasoning), establishing a clear problem the skill must solve
  rather than create.

**If Yes (anticipated scope):**

- **Skill name**: `lay-summary-pass`
- **Phase**: v0.3 (after `compression` and `argumentative-flow`
  mature; depends on Skopos-style purpose-relative preservation
  being well-established in the codebase).
- **Scope**: Generate a target-genre-conformant lay summary from the
  manuscript abstract + key-findings sections. Target genre selected
  via MANUSCRIPT_STATE field `lay_summary_target`. Output is a
  separate document, not an in-place transformation. Preservation
  report tracks numeric findings, hedging strength, and source-text
  attribution.
- **Required data**:
  - `MANUSCRIPT_STATE.target_audience` (already plausible field).
  - `MANUSCRIPT_STATE.lay_summary_target` (new).
  - Genre templates (Cochrane PLS, EU CTR, PLOS, Wellcome) as
    scriptorium-bundled reference resources.
  - Hedging vocabulary (Hyland-style hedge markers; see also
    [[semantic-preservation]] open question on Hyland's hedging
    list) for the certainty-preservation check.

**Why this is not v0.1:** Author demand is concentrated in specific
regulated genres, not in general research papers. Building a skill
without a clear user community produces theatre. The lay-summary
genre is also a place where overclaim drift can cause real harm —
inflated certainty in plain language reaches a wider audience than
inflated certainty in a technical paper. The skill should not ship
before scriptorium's hedging-preservation and overclaim-detection
machinery is mature.

## Open questions / weak evidence

- Empirical evidence on whether LLM-generated lay summaries are
  systematically worse than human ones is thin. Plausible failure
  modes (overclaim, deficit-model affect, numeric framing errors)
  are documented in the science-communication literature but not
  benchmarked against LLM output specifically.
- The Cochrane PLS template is mature and detailed; the EU CTR
  template is regulator-defined but less didactically documented.
  Funder lay-summary norms vary widely; there is no single template.
- Readability indices remain the de facto plain-language metric in
  many funder contexts despite their well-known failures on
  scientific text. Scriptorium should not rely on them as quality
  scores (see [[quantitative-quality-measures]]) but may need to
  *report* them because funders/reviewers do.

## References

1. United States. Plain Writing Act of 2010, Public Law 111-274
   (124 Stat. 2861), 13 October 2010.
   https://www.govinfo.gov/app/details/PLAW-111publ274.
2. Regulation (EU) No 536/2014 of the European Parliament and of
   the Council of 16 April 2014 on clinical trials on medicinal
   products for human use. *Official Journal of the European Union*.
   2014;L158:1–76. https://eur-lex.europa.eu/eli/reg/2014/536/oj.
3. Wellcome Trust. Grant conditions for grantholders, including
   lay-summary expectations.
   https://wellcome.org/research-funding/guidance/policies-grant-conditions
   (accessed 2026-05-17).
4. Cochrane. Guidance for writing a Cochrane Plain Language
   Summary. *Cochrane Handbook for Systematic Reviews of
   Interventions*. Chapter III, Section 2 supplementary material.
   https://training.cochrane.org/handbook/current/chapter-iii-s2-supplementary-material
   (accessed 2026-05-17).
5. Public Library of Science. Submission Guidelines: PLOS Medicine
   Author Summary.
   https://journals.plos.org/plosmedicine/s/submission-guidelines
   (accessed 2026-05-17).
6. National Institutes of Health. Plain Language at NIH (Clear
   Communication).
   https://www.nih.gov/institutes-nih/nih-office-director/office-communications-public-liaison/clear-communication/plain-language-nih
   (accessed 2026-05-17).
7. Bubela T, Nisbet MC, Borchelt R, et al. Science communication
   reconsidered. *Nature Biotechnology*. 2009;27(6):514–518.
   doi:10.1038/nbt0609-514. PMID: 19513051.
8. Brossard D, Lewenstein BV. A critical appraisal of models of
   public understanding of science: Using practice to inform
   theory. In: Kahlor LA, Stout PA, eds. *Communicating Science:
   New Agendas in Communication*. Routledge; 2010:11–39.
