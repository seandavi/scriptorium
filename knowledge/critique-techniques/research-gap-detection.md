# Research-gap detection: methodology and LLM-specific failure modes

*Last updated: 2026-10-20*

## Synthesis

"Research gap" is a load-bearing term in scholarly writing that
hides several distinct things: a *literature gap* (no published
work on a question), an *evidence gap* (work exists but is
contradictory or thin), a *methodological gap* (the question has
been studied but with a method that has known limitations), a
*population gap* (the question has been studied but not in the
relevant population), a *practical-translation gap* (the science
exists but hasn't been operationalised), and others. The
methodology literature on systematic reviews, scoping reviews, and
realist syntheses treats these as separate analytical objects
[1, 2, 3]. For a manuscript-side gap-detection skill, conflating
them produces vague output ("the discussion could be deeper");
distinguishing them produces actionable output ("the prior work
cited establishes mechanism but not effect size in the relevant
population — that's a population gap the limitations section
should name").

The published methodology that's most relevant to a manuscript-
internal gap-detection skill is the **PRISMA-ScR scoping-review
methodology** [4] and the **realist-synthesis framework** of
Pawson et al. [3]. Scoping reviews are explicitly designed to map
what's known and what's missing, and the PRISMA-ScR extension
provides a structured way to think about the question. Realist
synthesis adds the "for whom, under what conditions, and why"
layer that makes gap statements actionable rather than just
descriptive. A gap-detection skill working on a single manuscript
borrows methodology from these traditions even though it isn't
doing a full review.

The LLM-specific failure modes are also well-documented and they
are particularly acute for gap detection: **hallucinated
literature** (the model invents papers to fill a gap),
**hand-wavy generalities** ("consider expanding the discussion"
with no anchor), and **reviewer-shaped over-reach** (the model
produces critique-style findings rather than gap-style findings
with directions). Each has a documented mitigation. The
hallucination problem is the same as in `citation-audit` — never
let a generation step add citations — but applied to *future*
citations the author might pursue rather than existing ones being
audited. The vagueness problem is mitigated by requiring every
finding to anchor in a specific manuscript passage. The
over-reach problem is mitigated by framing the output as
*opportunities* rather than *deficiencies*.

For scriptorium, the practical takeaway is that gap-detection must
be **a structured taxonomy** (literature / evidence /
methodological / population / translation / counterargument /
internal-consistency gaps), with each finding **anchored to a
specific manuscript passage that exists**, and with **directions
for searching rather than invented citations** as the actionable
output.

## Evidence and frameworks

### Taxonomies of research gaps

Two published frameworks underlie most gap taxonomies, and a
third synthesises them. They should not be conflated:

- **Robinson, Saldanha & McKoy (2011)** [5], an AHRQ methods
  report, is the health-sciences framework for identifying gaps
  *from systematic reviews*. It does **not** list seven gap
  types. It characterises each gap with PICOS elements
  (population, intervention, comparison, outcomes, setting) and
  classifies the *reason* the gap exists as "(a) insufficient or
  imprecise information, (b) biased information; (c)
  inconsistency or unknown consistency, and (d) not the right
  information" [5]. A 2013 follow-up applied the framework to 50
  systematic reviews, identified about 600 unique research gaps,
  and revised the instructions [8].
- **Müller-Bloch & Kranz (2015)** [6], an information-systems
  paper presented at ICIS 2015, proposes a framework for
  rigorously identifying research gaps in qualitative literature
  reviews. It is the business / information-systems analogue to
  Robinson, and the taxonomy below describes it as a six-type
  model [10].
- **Miles (2017)** [9], a doctoral-workshop paper, is the source
  of the widely repeated **seven-type taxonomy**. Miles combines
  the two frameworks above and defines knowledge gaps (an issue
  not sufficiently studied), evidence gaps (contradictory
  findings), theoretical gaps, practical-knowledge gaps (a
  discrepancy between practice and knowledge), empirical gaps
  (propositions needing empirical validation), population gaps
  (populations not adequately represented), and methodological
  gaps. The list is as summarised in a 2024 manuscript-writing
  guide [11]. Adu & Miles (2023) [10] republish the model as a
  book chapter. The workshop paper is not peer reviewed and has
  no DOI; cite the 2023 chapter where a stable identifier is
  needed.

Across taxonomies, the agreement is on the structure (there are
kinds of gaps) more than on the specific labels.
**Scriptorium's seven categories are a project-compiled
adaptation, not a published taxonomy** (researcher synthesis, not
a source claim). Literature, evidence, methodological, and
population gaps correspond to Miles's knowledge, evidence,
methodological, and population gaps. The practical-translation
gap corresponds to Miles's practical-knowledge gap.
Counterargument and internal-consistency gaps are
manuscript-internal additions with no counterpart in Miles.
Miles's theoretical and empirical gaps are not separate
scriptorium categories. Robinson's four reasons are a useful
sub-tag for scriptorium's evidence gaps. The categories
scriptorium's gap-finder skill should consume in some form:

- **Literature gap** — no published work on the question.
  Detectable from a manuscript when a claim is made without
  citation in a field with otherwise dense citation. Often
  surfaces in the introduction or related work.
- **Evidence gap** — published work exists but is thin or
  contradictory. Detectable when a load-bearing claim cites only
  one or two sources, or when the manuscript surfaces conflicting
  results without resolving them.
- **Methodological gap** — the question has been studied but with
  methods that have known limitations. Detectable when prior work
  is cited and the manuscript's methods address a different
  methodological angle without explicitly framing the
  improvement.
- **Population gap** — studied in one population but the
  manuscript claims relevance to another. Detectable when the
  introduction discusses a clinical / demographic / disease
  population not represented in the cited prior work.
- **Practical-translation gap** — science exists but hasn't been
  operationalised. Detectable when a manuscript's discussion
  treats clinical translation as a closed question when the prior
  work cited is mechanistic only.
- **Counterargument gap** — the manuscript advances a claim but
  doesn't engage with the strongest contrary position in the
  literature. Detectable when a claim is asserted without the
  "but X argued Y" structure that careful scholarly writing
  uses.
- **Internal-consistency gap** — a cross-section gap. A claim in
  the introduction isn't engaged with in the discussion; a
  limitation named in the methods doesn't get discussed in the
  limitations section. Detectable via cross-section text search.

A gap-detection skill should emit findings tagged with the
category, because the categories suggest different remediation
strategies (a literature gap can be filled with new citations; a
counterargument gap can be filled by acknowledging and addressing
the contrary view; an internal-consistency gap is a writing fix,
not a research fix).

### Scoping-review methodology (PRISMA-ScR)

Tricco et al.'s 2018 PRISMA-ScR extension [4] is the canonical
guidance for scoping reviews, which are the systematic-review
sibling explicitly designed to map gaps. The PRISMA-ScR checklist
items most relevant to a single-manuscript gap-finder are:

- **Define the research question concretely.** Scoping reviews
  use the PCC framework (Population / Concept / Context) — gap
  statements that don't name all three are inactionable.
- **State the inclusion criteria for evidence.** What counts as
  "addressing the gap"? Methodological-gap statements that don't
  specify what method would close the gap are too vague.
- **Distinguish "no evidence" from "no relevant evidence
  found".** Important for honesty: a gap claim must be
  defensible against the response "you didn't look hard enough".

For a manuscript-internal skill, the PCC framing is the most
borrowable methodology: every gap finding should specify (where
relevant) the population, the concept, and the context. "The
methods don't address generalisation" is too vague; "the methods
don't address generalisation to elderly patients with
multimorbidity (population)" is actionable.

### Realist synthesis: mechanism-context-outcome

Pawson et al.'s realist-synthesis framework [3] adds the
explanatory layer: gap statements aren't just descriptive
("nobody has studied X") but explanatory ("the mechanism that
would link X to outcome Y under context Z hasn't been
established"). For a gap-finder skill working on a manuscript
draft, this maps to: when a finding is asserted, the skill can
flag the absence of a mechanism statement, or the absence of
context-of-applicability framing, even if the result itself is
established.

This is particularly useful for the **counterargument-gap**
category. A claim that "treatment X works" without engagement
with the literature on "treatment X fails under context Z" is a
realist-synthesis gap. The skill can name the missing context
without inventing the contrary literature.

### LLM-specific failure modes in gap detection

The general AI-writing-failure-modes literature
([[ai-writing-failure-modes]]) covers the broad categories.
Three are particularly relevant to gap detection:

1. **Hallucinated future literature.** The model invents papers
   to "fill" the gap it found. This is the same failure as
   citation-audit's invented-citation problem, but harder to
   catch because the hallucinated papers haven't been added to
   the manuscript yet — they're in the *suggested directions*
   output, which the author may then cite. The defence is the
   same: never let a generation step produce specific
   bibliographic entries. Suggestions are *search terms* and
   *angles*; never *cite this paper*.

2. **Vague exhortation.** The model produces output like
   "consider deepening the discussion" or "more engagement with
   prior work would strengthen the paper". This is the modal
   LLM failure mode on gap questions, and it's not useful — the
   author already knows the discussion could be deeper. The
   defence is structural: every finding must cite a specific
   manuscript passage as anchor (the gap is *here*, in this
   sentence) and a specific direction (search for *this kind of
   evidence*, considering *this angle*).

3. **Critique creep.** The model produces critique-shaped output
   ("the methodology is flawed because...") rather than gap-
   shaped output ("the methodology doesn't address X, which a
   reviewer might raise"). Critique is reviewer-simulation's
   job. The defence is framing: gap-finder output frames
   findings as *opportunities to strengthen* with directions,
   not as *deficiencies to defend against*.

A fourth less-cited but real failure mode is the **gap-of-
convenience problem**: the model identifies gaps that are easy
to find (introduction citations) but misses the harder cross-
section gaps that require reading the whole manuscript. The
defence is operational: the skill's protocol must enumerate
which gap categories to check rather than producing
opportunistic output.

## How this informs scriptorium

For the `gap-finder` skill specifically:

1. **Structured gap taxonomy.** Output is organised by gap
   category (literature / evidence / methodological / population
   / translation / counterargument / internal-consistency), not
   by manuscript section. This makes the categories visible to
   the author and makes the output actionable per category.
   When the skill names the taxonomy's provenance, it should say
   that five of the categories are adapted from Miles's gap
   types (Miles 2017, republished as Adu & Miles 2023 [10]), and
   that counterargument and internal-consistency gaps are
   scriptorium additions. Robinson et al. (2011) [5] supply the
   optional evidence-gap reason codes in item 7. The skill
   should not attribute the seven categories to Robinson.

2. **Every finding anchors in declared prose.** Per
   [[declared-work-scope]], the skill operates on existing
   draft prose. Every gap finding cites a specific manuscript
   passage. Findings that can't anchor in declared prose are out
   of scope.

3. **Suggested directions, not invented citations.** The same
   hard rule as `citation-audit`. Output is search terms and
   angles. The author runs the search.

4. **Realist-synthesis framing for counterargument gaps.** When
   the manuscript advances a claim that has known counterarguments
   in the literature, the skill names the absence of the
   counterargument engagement as a gap finding (with realist-
   synthesis-style mechanism / context / outcome framing where
   relevant).

5. **PRISMA-ScR PCC framing for methodological gaps.** When the
   skill flags a methodological gap, it spells out the
   population, the concept, and the context where relevant.
   "The methods don't generalise" is too vague; "the methods
   don't address the population in question (older adults with
   multimorbidity)" is actionable.

6. **Refuses opportunistic output.** The skill works through the
   gap categories systematically rather than producing whatever
   gaps the model notices first. The output template enumerates
   the categories checked; categories where nothing was found are
   declared explicitly ("no internal-consistency gaps detected on
   the sections provided") so silence isn't ambiguous.

7. **Robinson's reason codes as an optional evidence-gap tag.**
   When the skill flags an evidence gap, it can say *why* the
   cited evidence falls short: insufficient or imprecise,
   possibly biased, inconsistent, or not the right information
   [5]. This makes the suggested direction more specific. For
   example, "not the right information" points to a different
   population or outcome; "inconsistent" points to a search for
   the conflicting studies.

## Implementation priority for scriptorium

**Verdict:** Direct grounding for the `gap-finder` skill, which
has shipped (`skills/gap-finder/SKILL.md` lists this note and
[[literature-search-strategies]] in its grounding). This note
documents the *detection* side; literature-search-strategies
documents the *direction-suggestion* side. Both are required
because the skill's job is to surface gaps **and** point at how
to fill them.

**Correction to carry into the skill (2026-10-20):** gap-finder's
`full`-level framing and its Grounding section attribute the
seven-category taxonomy to "Robinson 2011 *AHRQ*". As documented
above, Robinson et al. (2011) [5] supply PICOS characterisation
and four reasons for gaps, not seven gap types. The seven types
come from Miles (2017) [9]. Five of scriptorium's seven
categories adapt Miles's types; counterargument and
internal-consistency are project additions. Suggested skill
wording: "five categories adapted from Miles (2017; Adu & Miles
2023), plus two manuscript-internal additions; Robinson et al.
(2011) reason codes available as an evidence-gap sub-tag". Cite
Adu & Miles (2023) [10] where a stable identifier is needed. The
skill text should be corrected (tracked in the skills issue, not
edited here).

**Why useful context anyway:**

- The taxonomy is reusable for any future scriptorium skill that
  needs to distinguish kinds of incompleteness in a manuscript.
  The seven-category breakdown is a useful project-wide
  vocabulary, provided its project-adapted status is stated.

- The "hallucinated future literature" failure mode is one not
  yet named explicitly elsewhere in the knowledge layer. Worth
  pointing at from [[ai-writing-failure-modes]] when that note
  next gets updated — it's a forward-looking variant of the
  citation-hallucination problem and deserves its own line.

- PRISMA-ScR's PCC framing and the realist-synthesis
  mechanism/context/outcome framing are both small, transferable
  vocabulary improvements scriptorium can adopt across skills.
  Worth being explicit that these are useful framings even
  outside the gap-finder context.

**Condition that would flip this:** if a future scriptorium skill
needs to do full systematic-review work (which is well outside
the current scope), this note would expand to cover the
systematic-review-side methodology (search protocols, screening,
data extraction) it currently doesn't. That's a v0.5+ question if
it ever arises.

## Open questions / weak evidence

- **The seven-type taxonomy is weakly sourced.** Miles (2017) [9]
  is a workshop paper, not peer reviewed. Its reach comes from
  repetition in methods guides and teaching materials, not from
  validation. Neither Miles nor scriptorium's adaptation has
  been tested for inter-rater agreement on manuscript text.
- **Müller-Bloch & Kranz's six categories were not checked
  against the primary text** in the October 2026 refresh.
  Automated access to the ICIS paper was blocked. The six-type
  description above comes from Adu & Miles (2023) [10].

## Cross-references

- [[literature-search-strategies]] — the direction-suggestion
  side of the gap-finder skill. This note covers detection;
  that note covers what the skill suggests as next steps.
- [[ai-writing-failure-modes]] — hallucination, voice loss, and
  the broader failure-mode landscape. Gap-finder's specific
  failure modes (hallucinated future literature, vague
  exhortation, critique creep) are variants documented here for
  gap-detection specifically.
- [[citation-claim-alignment]] — the parallel skill that audits
  existing citations. Gap-finder is the structural analogue for
  *future* citations the author should pursue; the no-invention
  rule is shared between them.
- [[argument-mapping]] — for the counterargument-gap category,
  argument-mapping's Toulmin-warrant analysis is the underlying
  framework for detecting missing premises.
- [[internal-consistency]] — for the internal-consistency-gap
  category, this note's cross-section consistency methodology is
  the detection mechanism.
- [[common-critiques-taxonomy]] — what reviewers flag is a
  useful prior on which gaps actually matter for the
  manuscript's acceptance.
- [[declared-work-scope]] — the project-wide convention.
  Gap-finder operates on declared prose; refuses on
  pre-declaration questions; never produces prose to fill a gap.

## References

[1] Arksey, H., & O'Malley, L. (2005). Scoping studies: towards a
methodological framework. *International Journal of Social
Research Methodology*, 8(1), 19-32.
DOI: 10.1080/1364557032000119616. (Foundational scoping-review
methodology paper.)

[2] Munn, Z., Peters, M. D. J., Stern, C., Tufanaru, C.,
McArthur, A., & Aromataris, E. (2018). Systematic review or
scoping review? Guidance for authors when choosing between a
systematic or scoping review approach. *BMC Medical Research
Methodology*, 18(1), 143. DOI: 10.1186/s12874-018-0611-x.
PMID: 30453902. (Distinction between systematic and scoping
review approaches; relevant for understanding what counts as
a "gap" vs. an "answer".)

[3] Pawson, R., Greenhalgh, T., Harvey, G., & Walshe, K. (2005).
Realist review — a new method of systematic review designed for
complex policy interventions. *Journal of Health Services
Research & Policy*, 10(suppl 1), 21-34.
DOI: 10.1258/1355819054308530. PMID: 16053581. (Realist
synthesis methodology; the mechanism-context-outcome framing
borrowable for counterargument-gap analysis.)

[4] Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K.,
Colquhoun, H., Levac, D., Moher, D., Peters, M. D. J., Horsley,
T., Weeks, L., Hempel, S., Akl, E. A., Chang, C., McGowan, J.,
Stewart, L., Hartling, L., Aldcroft, A., Wilson, M. G., Garritty,
C., ... Straus, S. E. (2018). PRISMA extension for scoping
reviews (PRISMA-ScR): Checklist and explanation. *Annals of
Internal Medicine*, 169(7), 467-473. DOI: 10.7326/M18-0850.
PMID: 30178033. (Canonical scoping-review checklist; the PCC
framing the gap-finder skill borrows from.)

[5] Robinson, K. A., Saldanha, I. J., & McKoy, N. A. (2011).
*Frameworks for determining research gaps during systematic
reviews* (Methods Future Research Needs Report No. 11-EHC043-EF).
Agency for Healthcare Research and Quality (US). PMID: 21977524.
NCBI Bookshelf: NBK62478. (The PICOS-plus-reasons framework:
gaps characterised by PICOS elements and classified by reason
— insufficient/imprecise, biased, inconsistent, or not the
right information. Corrected 2026-10-20: the entry previously
listed the 2013 evaluation report's authors under PMID 23534077,
which resolves to an unrelated HCUP statistical brief; the 2013
report is now [8].)

[6] Müller-Bloch, C., & Kranz, J. (2015). A framework for
rigorously identifying research gaps in qualitative literature
reviews. In *Proceedings of the 36th International Conference on
Information Systems (ICIS 2015)*, Fort Worth, TX. Association for
Information Systems.
https://aisel.aisnet.org/icis2015/proceedings/ResearchMethods/2/.
(Corrected 2026-10-20: this entry replaces an unverified
placeholder citing "Müller, R., & Köhler, T. (2018)", which
could not be found. The information-systems gap framework that
the placeholder described is this paper.)

[7] Toulmin, S. (2003). *The Uses of Argument* (updated ed.).
Cambridge University Press. ISBN: 9780521534833. (Toulmin's
argument-warrant-data framework, the underlying methodology
for counterargument-gap detection.)

[8] Robinson, K. A., Akinyede, O., Dutta, T., Sawin, V. I.,
Li, T., Spencer, M. R., Turkelson, C. M., & Weston, C. (2013).
*Framework for determining research gaps during systematic
review: evaluation* (Methods Research Report No. 13-EHC019-EF).
Agency for Healthcare Research and Quality (US). PMID: 23487868.
NCBI Bookshelf: NBK126708. (Evaluation and revision of [5];
applied to 50 systematic reviews.)

[9] Miles, D. A. (2017). A taxonomy of research gaps: Identifying
and defining the seven research gaps. *Doctoral Student Workshop:
Finding Research Gaps — Research Methods and Strategies*, Dallas,
TX, pp. 1–15. (Workshop paper; not peer reviewed; no DOI. Source
of the seven-type taxonomy: knowledge, evidence, theoretical,
practical-knowledge, empirical, population, methodological.)

[10] Adu, P., & Miles, D. A. (2023). Understanding the seven types
of research gaps. In *Dissertation Research Methods*. Routledge.
DOI: 10.4324/9781003268154-5. (Book-chapter version of the Miles
taxonomy, which describes it as an amalgamation of Robinson et
al. 2011 and Müller-Bloch & Kranz.)

[11] Sefcik, J. S., Glasofer, A., & Smith, M. L. (2024). Writing
manuscript "bookends": Strategies to effectively frame science.
*Health Behavior Research*, 7(4). DOI: 10.4148/2572-1836.1258.
PMCID: PMC12459627. (Secondary source quoting the definitions of
the seven Miles gap types; cited here because the 2017 workshop
paper is not reliably retrievable.)
