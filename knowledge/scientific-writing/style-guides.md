## Scientific style guides

*Last updated: 2026-05-17*

## Synthesis

Style manuals are the procedural memory of scientific writing. They codify
the thousands of small decisions — number formatting, citation form, unit
abbreviations, capitalization conventions, terminology for human subjects —
that journals enforce silently and that authors usually learn by being
corrected. The major manuals overlap on the basics but diverge sharply on
opinionated calls (Vancouver vs. name–year citations; serial comma;
abbreviation of common terms; SI conventions).

For a system like scriptorium, style guides matter at two layers. They
underwrite `terminology-normalization` and `journal-style-conversion` —
skills that will eventually need to know "if target venue is *JAMA*, use
AMA conventions; if *PNAS*, use a hybrid form." They also constrain what a
critique skill should *not* flag: an em-dash style preference is not a
problem worth raising; an ambiguous statistical claim is.

The most important practical fact: every major journal publishes its own
in-house overlay on one of these manuals. Following the manual gets you
most of the way; the journal-specific instructions-for-authors cover the
remaining differences. A scriptorium that wants to do style conversion
seriously will need both layers.

## Evidence and frameworks

### AMA Manual of Style (medicine)

*AMA Manual of Style: A Guide for Authors and Editors*. 11th ed. Oxford
University Press; 2020. ISBN-13 978-0-19-024655-6. [1]

The default for biomedical journals published by the AMA family
(*JAMA*, *JAMA Network Open*, JAMA specialty journals) and the most-cited
manual in clinical medicine. The 11th edition (March 2020) significantly
expanded the chapters on statistics and study design, and revised the
language guidance on inclusive terminology (e.g., person-first vs.
identity-first language; updated guidance on race, ethnicity, and sex/gender
reporting).

**Scope:** medicine, public health, clinical biomedicine.
**Citation style:** Vancouver-style numbered references; specific AMA
conventions for journal abbreviations (per *Index Medicus* / NLM).
**Opinionated calls:** prefers active voice in methods; specific guidance
on units (SI with conventional units where required); detailed rules on how
to report p-values, confidence intervals, and effect sizes. Strict on
abbreviation use — many common medical abbreviations require expansion at
first use.

### CSE Scientific Style and Format (general science)

*Scientific Style and Format: The CSE Manual for Authors, Editors, and
Publishers*. 8th ed. Council of Science Editors and University of Chicago
Press; 2014. ISBN-13 978-0-226-11649-5. [2]

The cross-disciplinary scientific manual, used widely in biology, ecology,
earth sciences, and general life sciences. The 8th edition (2014) is the
most recent; an online edition (*Scientific Style and Format Online*) is
maintained as the living reference.

**Scope:** general science (biology, ecology, earth sciences, chemistry
adjacent fields).
**Citation styles:** offers three — Citation-Sequence (numbered),
Citation-Name (alphabetic numbered), and Name-Year (author-year). Journals
pick one.
**Opinionated calls:** specific rules on taxonomic nomenclature, gene and
protein nomenclature, chemical naming, units (SI), and astronomical
conventions. Generally less prescriptive than AMA on prose style; more
prescriptive on naming conventions.

### Chicago Manual of Style

*The Chicago Manual of Style*. 17th ed. University of Chicago Press; 2017.
ISBN-13 978-0-226-28705-8. [3]

The general-purpose American English manual, dominant in humanities and
social-science book publishing but not the primary reference for laboratory
sciences. The 18th edition has been announced for late 2024 but the 17th
remains current in most installed copies. Some hybrid science journals
(e.g., *PNAS* for some elements) follow Chicago conventions.

**Scope:** humanities, social sciences, trade non-fiction, university-press
books.
**Citation styles:** offers two — Notes and Bibliography (footnote/endnote
style, humanities-leaning), Author-Date (parenthetical, common in social
sciences).
**Opinionated calls:** strong on punctuation conventions (serial comma is
mandatory); detailed treatment of long-form prose conventions; less useful
on technical/scientific notation than CSE or AMA.

### ACS Style Guide (chemistry)

*The ACS Style Guide: Effective Communication of Scientific Information*.
3rd ed. Coghill AM, Garson LR, eds. American Chemical Society / Oxford
University Press; 2006. ISBN-13 978-0-8412-3999-9. [4]

The default for chemistry journals published by ACS (*JACS*, *J Phys Chem*,
*Org Lett*, etc.). The 3rd edition is now older (2006); the ACS Publications
website maintains an updated *ACS Guide to Scholarly Communication* (online,
ongoing) that has effectively superseded the print volume for many practical
questions.

**Scope:** chemistry and chemistry-adjacent fields.
**Citation style:** ACS supports three formats — superscript number,
italic number in parentheses, author-year — chosen per journal.
**Opinionated calls:** extensive guidance on chemical nomenclature, reaction
schemes, structural drawings, and spectroscopic data reporting. Specific
guidance on figures, tables, and supplementary information for chemistry
papers.

### APA (psychology and social science)

*Publication Manual of the American Psychological Association*. 7th ed.
American Psychological Association; 2020. ISBN-13 978-1-4338-3216-1
(paperback), 978-1-4338-3215-4 (hardcover), 978-1-4338-3217-8
(spiral-bound). [5]

The default for psychology, education, communication studies, and many
social-science fields. The 7th edition (October 2019, effective 2020)
overhauled the layout requirements, added formal guidance on bias-free
language, and updated digital-source citation conventions.

**Scope:** psychology, education, social sciences, communication studies,
some health sciences.
**Citation style:** author–date parenthetical (Smith, 2020). Reference list
is alphabetical.
**Opinionated calls:** strong guidance on reporting statistics (specific
formats for effect sizes, confidence intervals, p-values), heavy emphasis
on bias-free language, specific format requirements for tables and figures.

### IEEE (engineering, computer science)

*IEEE Editorial Style Manual for Authors*. IEEE Publications Operations
(ongoing, current edition revised periodically). [6, TODO verify exact
edition and ISBN — IEEE distributes the manual as a PDF rather than as a
formal ISBN-bearing book]

The default for IEEE journals and most engineering/CS publications. The
IEEE Editorial Style Manual is short and prescriptive; the ACM has its own
parallel set of conventions.

**Scope:** electrical engineering, computer science, signal processing,
robotics.
**Citation style:** numbered references in square brackets [1], in the
order cited. References listed in citation order, not alphabetically.
**Opinionated calls:** abbreviation rules for journal names; formatting of
equations and algorithms; figure caption conventions. Less prescriptive on
prose style than AMA or APA.

### Other significant manuals

- **Vancouver** (ICMJE Recommendations) — *Recommendations for the Conduct,
  Reporting, Editing, and Publication of Scholarly Work in Medical
  Journals*. International Committee of Medical Journal Editors,
  icmje.org. This is the underlying citation form used by AMA and most
  biomedical journals.
- **AAAS (*Science* family)** — internal house style, derived from CSE with
  modifications.
- **Nature house style** — internal, derived from CSE with significant
  modifications.

## How this informs scriptorium

Style is not where critique skills should focus their attention. A
manuscript that needs structural surgery doesn't benefit from being told
its em-dash style is wrong. But style is exactly where *normalization* and
*conversion* skills earn their keep.

- **`terminology-normalization`** (planned, v0.3). Should consume the
  preferred/forbidden terminology declared in `MANUSCRIPT_STATE.yaml`
  *plus* the relevant style manual's standing guidance (e.g., AMA's
  inclusive-language rules; APA's bias-free language guide). The
  preferred-terms list in state is project-specific; the style manual
  layer is venue-specific.
- **`journal-style-conversion`** (planned). Needs a routing table mapping
  target venue → applicable manual → journal-specific overlay. A first
  cut: detect target venue, load the manual's defaults, then apply
  journal-specific overrides from the venue's instructions-for-authors.
- **`reference-format-conversion`** (planned utility). Mechanical
  conversion among Vancouver, author–date, and superscript numeric forms.
  This is the easiest style work to automate — citation styles are
  formally specified — and it should not interact with prose.
- **`reporting-compliance`** (proposed, see [[reporting-guidelines]]). Some
  reporting-guideline items are also style items (e.g., AMA's statistical
  reporting conventions overlap with CONSORT and STROBE). The two
  validation layers should be kept distinct in output but routed
  consistently in input.

A note on posture: scriptorium skills should treat style choices as
*venue-dependent*, not *correct/incorrect*. A skill that imposes Chicago
conventions on a CSE manuscript is doing damage, not improvement. The
target venue and applicable manual must be explicit in
`MANUSCRIPT_STATE.yaml` for any style-aware skill to run.

## Open questions / weak evidence

- The major manuals do not agree on serial comma, em-dash usage, or
  abbreviation conventions. There is no neutral default; "default" is
  always "default for some venue."
- Many manuals are revised on long cycles (AMA: 2007 → 2020; CSE: 2006 →
  2014; ACS: 2006 → unfinished). Practical advice often lives in
  journal-specific instructions rather than in the manual.
- The IEEE Editorial Style Manual is updated as a PDF rather than as a
  bound book with stable ISBN; tooling that depends on stable references
  may need to track the manual by date/version.
- Online "living" manuals (ACS Guide; CSE Online) are now often more
  current than their print parents. For machine-readable rule extraction,
  the online versions are better starting points but harder to cite
  durably.

## References

1. Christiansen S, Iverson C, Flanagin A, *et al*. *AMA Manual of Style: A
   Guide for Authors and Editors*. 11th ed. Oxford University Press; 2020.
   ISBN-13 978-0-19-024655-6.
2. Council of Science Editors, Style Manual Committee. *Scientific Style
   and Format: The CSE Manual for Authors, Editors, and Publishers*. 8th
   ed. Council of Science Editors and University of Chicago Press; 2014.
   ISBN-13 978-0-226-11649-5.
3. University of Chicago Press Editorial Staff. *The Chicago Manual of
   Style*. 17th ed. University of Chicago Press; 2017. ISBN-13
   978-0-226-28705-8.
4. Coghill AM, Garson LR, eds. *The ACS Style Guide: Effective
   Communication of Scientific Information*. 3rd ed. American Chemical
   Society / Oxford University Press; 2006. ISBN-13 978-0-8412-3999-9.
5. American Psychological Association. *Publication Manual of the American
   Psychological Association*. 7th ed. American Psychological Association;
   2020. ISBN-13 978-1-4338-3216-1 (paperback).
6. IEEE Publications Operations. *IEEE Editorial Style Manual for Authors*.
   IEEE; current edition. [TODO verify current edition/year; manual is
   distributed as a PDF rather than as an ISBN-bearing volume.]
7. International Committee of Medical Journal Editors. *Recommendations for
   the Conduct, Reporting, Editing, and Publication of Scholarly Work in
   Medical Journals*. icmje.org (Vancouver style underlying document).
