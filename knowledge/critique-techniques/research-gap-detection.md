# Research-gap detection: methodology and LLM-specific failure modes

*Last updated: 2026-05-20*

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

The most widely cited gap taxonomy in the health-sciences
literature is Robinson et al.'s 2011 framework [5], which
identifies seven categories: evidence, knowledge, practical-
knowledge, methodological, empirical, theoretical, and
population. Müller et al.'s 2018 review [TODO verify citation; the
operations-research-gap literature also has a Robinson-like
taxonomy with slightly different category labels] is the
operations-research analogue. Across taxonomies, the agreement is
on the structure (there are kinds of gaps) more than on the
specific labels. The categories scriptorium's gap-finder skill
should consume in some form:

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

## Implementation priority for scriptorium

**Verdict:** Direct grounding for the `gap-finder` skill (v0.3
candidate, currently `needs-grounding` until both this note and
[[literature-search-strategies]] land). This note documents the
*detection* side; literature-search-strategies documents the
*direction-suggestion* side. Both are required because the
skill's job is to surface gaps **and** point at how to fill them.

**Why useful context anyway:**

- The taxonomy is reusable for any future scriptorium skill that
  needs to distinguish kinds of incompleteness in a manuscript.
  The seven-category breakdown is a useful project-wide
  vocabulary.

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

[5] Robinson, K. A., Akinyede, O., Dutta, T., Sawin, V. I.,
Li, T., Spencer, M. R., Turkelson, C. M., & Weston, C. (2013).
*Framework for determining research gaps during systematic
review: evaluation* (Methods Research Report). Agency for
Healthcare Research and Quality (US). PMID: 23534077. (The
seven-category gap taxonomy widely cited in the
health-sciences-gap-detection literature.)

[6] Müller, R., & Köhler, T. (2018). Research gap framework: A
systematic review approach for identifying gaps in the
literature. [TODO verify exact citation; the Müller et al.
operations-research-gap framework is widely cited in
business / operations literature with a similar shape to
Robinson 2011, but the exact reference details should be
checked against the primary source.]

[7] Toulmin, S. (2003). *The Uses of Argument* (updated ed.).
Cambridge University Press. ISBN: 9780521534833. (Toulmin's
argument-warrant-data framework, the underlying methodology
for counterargument-gap detection.)
