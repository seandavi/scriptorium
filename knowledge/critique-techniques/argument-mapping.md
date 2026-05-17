# Argument mapping: diagramming structure to expose gaps

*Last updated: 2026-05-17*

## Synthesis

Argument mapping is the practice of decomposing a piece of reasoning
into its constituent moves — claim, evidence, inferential warrant,
qualifier, rebuttal — and rendering those moves as a graph so that
gaps, missing premises, and unsupported inferences become visible. The
practice has roots in Stephen Toulmin's 1958 monograph *The Uses of
Argument* [^1] and in the subsequent argumentation-schemes literature
formalised by Walton, Reed & Macagno [^2]. Both contributions reject
the formal-logic-only view that an argument's validity can be assessed
by syntax alone; both insist that real arguments depend on
context-sensitive *warrants* (Toulmin) or *schemes* (Walton et al.)
that are themselves open to critical scrutiny.

For peer review, this matters because the failure modes of scientific
prose are rarely formal-logic errors. They are missing warrants
("how does the cited result actually license this claim?"), absent
qualifiers ("results generalise to X" without specifying the boundary),
and unaddressed rebuttals ("the alternative explanation is not
discussed"). A structured argument map turns those failure modes into
locatable, nameable absences rather than vague complaints. Empirically,
controlled studies of computer-aided argument mapping in critical-
thinking instruction find gains of 0.7–0.85 SD in critical-thinking
test scores [^3], which is among the larger educational effects in the
literature on transferable reasoning skill.

For scriptorium, argument mapping is the underlying theory for skills
that audit logical flow — particularly `argumentative-flow` and
`reviewer-simulation`. It is the layer between high-level rubrics
("does the conclusion follow from the data?") and surface-level
edits ("this paragraph is unclear"): it gives the LLM a structured
decomposition to argue against. See also
[[critique-quality-evidence]] in `knowledge/peer-review/` for what
makes a critique act on these gaps usefully.

## Techniques and tools

### Toulmin (1958)

Toulmin's model decomposes an argument into six components: **claim**
(C), **data** / **grounds** (D), **warrant** (W), **backing** (B),
**modal qualifier** (Q), and **rebuttal** (R) [^1]. Toulmin's
formulation is worth quoting: a warrant answers the question "how do
you get there?" — i.e. it is the inferential principle that licenses
moving from data to claim, and it is itself open to further support
(backing) and to defeat (rebuttal). Toulmin's central methodological
move — separating *what is claimed* from *what licenses the claim* —
remains the load-bearing distinction in every subsequent argument-
mapping system. The updated 2003 edition (Cambridge University Press,
ISBN 0-521-53483-6 paperback / 0-521-82748-5 hardback) is the standard
modern reference.

In manuscript critique, Toulmin's components map directly onto common
review concerns:

- **Missing warrant**: "the cited result does not, on its own,
  license this inference."
- **Missing qualifier**: "the conclusion is stated unconditionally
  but the data support only a restricted version."
- **Unaddressed rebuttal**: "the alternative explanation is not
  considered."
- **Insufficient backing**: "the cited support is itself contested
  in the literature."

### Walton, Reed & Macagno (2008)

Walton, Reed & Macagno's *Argumentation Schemes* [^2] (Cambridge
University Press, ISBN 9780521723749) catalogues 96 stereotyped
argument patterns — appeal to expert opinion, argument from analogy,
argument from cause to effect, argument from sign — each paired with a
fixed list of **critical questions** that an interlocutor should ask
to test the scheme's application. For example, the scheme "argument
from expert opinion" attaches critical questions including: Is the
expert source genuinely an expert in this field? Is the expert's
opinion consistent with that of other experts? Is the expert's
opinion presented accurately? Each scheme is, in effect, a checklist
for a particular kind of move.

For scientific manuscripts the scheme-plus-critical-questions structure
is unusually well-suited, because most paragraphs in a Discussion
section deploy a small set of recurring schemes: from-data-to-claim,
from-analogy, from-mechanism, from-correlation-to-cause, from-expert-
consensus. Each scheme has a known and finite set of ways to fail.

### Paul & Elder; Browne & Keeley

The Paul–Elder framework formalises **eight elements of reasoning**
(purpose, question, information, concepts, assumptions, inferences,
implications, point of view) and **nine intellectual standards**
(clarity, accuracy, precision, relevance, depth, breadth, logic,
significance, fairness) [^4]. It is more pedagogical than Toulmin and
more abstract than Walton et al., but it provides a useful checklist
when critiquing the *frame* of an argument — i.e. what hidden purpose
or unstated assumption is doing the work.

Browne & Keeley's *Asking the Right Questions* (12th ed., Pearson 2017,
ISBN 9780134431994) [^5] is the most widely adopted undergraduate text
for applied argument critique. Its operational moves — identify the
issue, identify the conclusion, identify the reasons, search for
ambiguity, identify the assumptions, search for fallacies, evaluate the
evidence, consider rival causes, examine statistics — translate
readily into a sequence of audit prompts.

### Computational argument-mapping tools

- **Rationale** and **bCisive** (Austhink / Tim van Gelder) — commercial
  argument-mapping software with a long track record of educational use;
  Rationale is the engine behind the 0.7–0.85 SD critical-thinking
  gains cited above [^3].
- **MindMup** — lightweight, free, browser-based concept/argument mapping
  used widely in classroom settings; not Toulmin-specific but well-
  suited to argument-tree work.
- **Carneades Argumentation System** — open-source (MPL-2.0) research
  prototype originally developed with Walton; implements computational
  evaluation of arguments built from schemes, including critical-
  question handling [^6]. Available at
  https://carneades.github.io/.

For scriptorium, the relevant lesson is not to embed these tools but
to *steal their schema*: a Toulmin-style decomposition plus a Walton-
style critical-question audit is sufficient as a critique prompt
backbone.

### Use in scientific peer review

Reviewers implicitly perform argument mapping every time they ask "but
how do you get from this data to this claim?" The implicit version is
fragile — it depends on the reviewer's tacit critical-thinking habits,
which Schroter et al. (2008) showed are unevenly distributed even
among trained reviewers (see [[critique-quality-evidence]]). Making
the mapping explicit — naming the claim, the warrant, the missing
qualifier — turns an inarticulate "this doesn't follow" into an
actionable critique.

## How this informs scriptorium

- **`argumentative-flow`** — should decompose paragraphs into Toulmin
  components when assessing flow. The output structure for a flagged
  flow gap should name which component is missing (warrant, qualifier,
  rebuttal) rather than just "logic unclear."
- **`reviewer-simulation`** — each persona can be primed with a small
  set of Walton schemes likely to be deployed in that paper's
  discipline (e.g. correlation-to-cause for observational studies;
  mechanism-to-clinical-claim for translational work) and the
  associated critical questions.
- **Schema discipline**: scriptorium's structured-output principle
  fits naturally — each critique can emit `{claim, data, warrant,
  qualifier, rebuttal, missing_component}` and downstream skills
  consume the structure.

LLM limits: LLMs can produce plausible Toulmin decompositions, but
they cannot reliably verify whether a warrant actually holds (that
requires domain knowledge plus, often, recomputation — see
[[statistical-inconsistency]]). The honest framing is that argument
mapping is a *structuring* skill, not a *verification* skill.
Scriptorium's job is to make the structure legible; the human author
remains responsible for verifying that the warrants are sound.

## Limits and caveats

- Toulmin's scheme can flatten complex arguments into a single
  C-D-W tuple where multiple parallel arguments are operating; for
  multi-step inference chains a single map is inadequate and a
  tree is required.
- Walton et al.'s 96 schemes are a useful inventory but the boundary
  between schemes is fuzzy; the same paragraph can plausibly be
  parsed under several schemes. The right move is usually to apply
  the critical-questions union, not to insist on a single scheme.
- The educational evidence for argument mapping (van Gelder and
  colleagues) is for *teaching* critical thinking; the inference that
  mapping by itself improves manuscript quality is weaker. The
  empirical question scriptorium should track: do authors who see a
  Toulmin-decomposed critique actually revise more substantively
  than authors who receive prose-only critique?
- LLMs are particularly prone to inventing plausible-but-absent
  warrants when prompted to "fill in the missing premise." The
  conservative-edit posture (see DESIGN.md) implies that critique
  skills should *flag* missing warrants rather than supply them.

## References

[^1]: Toulmin SE. *The Uses of Argument*. Updated edition. Cambridge
    University Press, 2003. ISBN 0-521-53483-6 (paperback);
    0-521-82748-5 (hardback). First edition 1958.

[^2]: Walton D, Reed C, Macagno F. *Argumentation Schemes*. Cambridge
    University Press, 2008. ISBN 9780521723749.

[^3]: van Gelder T. Using argument mapping to improve critical
    thinking skills. In: Davies M, Barnett R, eds. *The Palgrave
    Handbook of Critical Thinking in Higher Education*. Palgrave
    Macmillan, 2015. Effect sizes reported across multiple
    semester-long courses: 0.7–0.85 SD in critical-thinking measures.

[^4]: Paul R, Elder L. *The Miniature Guide to Critical Thinking:
    Concepts and Tools*. 8th edition. Foundation for Critical
    Thinking, 2019. ISBN 9780944583401. See also
    https://louisville.edu/ideastoaction/about/criticalthinking/framework.

[^5]: Browne MN, Keeley SM. *Asking the Right Questions: A Guide to
    Critical Thinking*. 12th edition. Pearson, 2017.
    ISBN 9780134431994 (print); 9780137501731 (eText).

[^6]: Gordon TF, Walton D. The Carneades argumentation system. *Argument
    & Computation*. Open-source repository:
    https://carneades.github.io/. License MPL-2.0.
