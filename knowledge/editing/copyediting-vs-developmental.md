# Copyediting vs developmental editing: the editing taxonomy

*Last updated: 2026-05-17*

## Synthesis

Professional editing is not one activity but a gradient of activities,
each with its own scope, license to modify, and characteristic
failure modes. The standard division in the English-language editing
literature runs from **proofreading** (typographical, mechanical) to
**copyediting** (grammar, style, internal consistency) to **line
editing** (sentence-level voice, flow, clarity) to **substantive /
developmental editing** (structure, argument, organization). The
boundaries are conventions, not laws; different houses and professional
bodies (CSE, Editorial Freelancers Association, Council of Editors of
Learned Journals) draw them slightly differently. But the underlying
principle is shared: heavier-touch editing requires more explicit
authorization and produces more potential for distortion of the
author's intent.

This gradient matters for scriptorium because skills sit at different
points on it. `terminology-normalization` and journal-style
conversion are copyediting. `compression` and active-voice
transformations are line editing. `argumentative-flow` and any future
restructuring skill are developmental editing. Mixing them — calling
"clean up this paragraph" and getting back a structurally rearranged
argument — is the operating-mode mismatch that makes single-prompt
LLM editing untrustworthy. Scriptorium's one-skill-one-responsibility
discipline is the editorial-taxonomy discipline ported into
agent design.

## Evidence

**Einsohn (2011, 2019), *The Copyeditor's Handbook* (3rd ed., UC
Press, ISBN 978-0520286726).** The most widely used English-language
reference on copyediting. Einsohn is explicit about scope:
"Copyeditors are expected to query structural and organizational
problems, but they are not expected to fix these problems.
Reorganizing or restructuring a manuscript is called developmental
editing." And: "copyeditors are not rewriters, ghost writers, or
substantive editors. Although copyeditors are expected to make simple
revisions to smooth awkward passages, copyeditors do not have license
to rewrite a text line by line."[^1]

Einsohn divides copyediting into four "Cs": clarity, coherency,
consistency, and correctness. These map onto sentence- and
paragraph-level interventions, *not* paragraph-restructuring or
argument-redesign work. The handbook's repeated injunction is that
the copyeditor *queries* the author when something larger is wrong —
they do not silently fix it.

**Mossop (2020), *Revising and Editing for Translators* (4th ed.,
Routledge, ISBN 978-1138895164).** Though framed for translation,
Mossop's parameter system applies cleanly to scientific editing.
He defines **twelve parameters** in four groups: (1) **meaning
transfer** (accuracy, completeness); (2) **content** (logic, facts);
(3) **language and style** (smoothness, tailoring to readership,
sub-language conventions, idiom, mechanics); (4) **physical
presentation** (layout, typography, organization).[^2]

The Mossop framing is useful for scriptorium because each parameter
is a separable check. A skill can target *accuracy* without
addressing *idiom*; a skill can target *logic* without addressing
*smoothness*. This separability is what enables skills to compose:
the editorial trace is the parameters touched, in order, by which
skill.

**The Council of Science Editors (CSE) *Manual*, 9th edition (2024,
ISBN 978-0226683942).** The CSE Manual is the field-standard
reference for scientific publishing in the English-language
biomedical and life-sciences literature. Originally the *CBE Manual*
(Council of Biology Editors, 1965–2000). The 9th edition delivers
comprehensive guidance on style, citation systems, and editorial
practice for scientific manuscripts. CSE recognizes three citation
systems (citation-sequence, name-year, citation-name), which
scriptorium's [[csl-and-bibliographic-standards]] tooling must
accommodate.[^3]

CSE's scope is closer to copyediting and house-style enforcement than
to substantive editing, reflecting the journal-production reality
that most scientific copyediting happens after acceptance and after
the developmental editing has already been done (typically by the
authors themselves, via peer review).

**Practitioner consensus on the gradient.** The Editorial Freelancers
Association, the Chartered Institute of Editing and Proofreading
(UK), and most editorial training programs converge on roughly four
levels:

| Level | Scope | Author authorization needed |
|-------|-------|---|
| Proofreading | Typos, layout, mechanical errors | Minimal |
| Copyediting | Grammar, style, consistency, fact-spot-check | Standard |
| Line editing | Sentence-level voice, flow, clarity | Explicit |
| Developmental / substantive editing | Structure, argument, organization | Explicit + collaborative |

These distinctions are not academic. Pricing in professional editing
markets correlates closely with scope; reputational risk for the
editor scales with scope (a copyeditor who restructured your
manuscript is a problem; a developmental editor who only fixed commas
is a different problem); and *time required* scales with scope.

## How this informs scriptorium

The editing taxonomy maps cleanly onto scriptorium's skill categories
as defined in [[DESIGN]] §"Design philosophy":

| Editing level | DESIGN.md category | Example skills (current + planned) |
|---|---|---|
| Proofreading | Normalization | (none yet — typography is downstream of scriptorium) |
| Copyediting | Normalization | `terminology-normalization`, journal-style-conversion |
| Line editing | Transformation (narrow) | `compression`, redundancy-removal, active-voice |
| Developmental | Transformation (broad) | `argumentative-flow`, restructuring |
| (Cross-cutting) | Critique | `citation-audit`, `reviewer-simulation` |
| (Cross-cutting) | Validation | figure-text-alignment, statistics-consistency |

Three concrete design consequences follow.

**1. Skill descriptions must declare their editing level.** A skill's
SKILL.md should make explicit whether it operates at the copyediting,
line-editing, or developmental level. This sets author expectations
and informs the auto-invocable vs explicit-only decision: copyediting
skills can default to auto-invocable (low rewrite risk);
developmental-level skills must be explicit-only (high rewrite risk).

**2. The conservative-edit posture is the copyediting default,
extended.** Einsohn's "copyeditors do not have license to rewrite a
text line by line" is the same principle as DESIGN.md's "preserving
every citation, preserving every quantitative statement, minimizing
rewrite surface area." Scriptorium's restraint is the editorial
profession's restraint, made enforceable in the
`MANUSCRIPT_STATE.yaml` constraints.

**3. Developmental edits must surface "remaining weaknesses"
explicitly.** DESIGN.md already calls for this: "Skills that need to
make aggressive changes should be invoked explicitly … and emit a
clear 'Remaining Weaknesses' section so the author sees what they
didn't fix." This mirrors the developmental-editor's query letter —
the document that accompanies a substantive edit and explains what
the editor changed, what they considered changing and didn't, and
what they think the author should still address.

For Mossop's parameter system specifically: scriptorium can use it as
a *checklist vocabulary* in critique outputs. When `citation-audit`
flags a quotation mismatch, that is a *Logic / Facts* finding under
Mossop. When `argumentative-flow` flags a paragraph that doesn't
follow from the previous one, that is a *Smoothness* finding.
Vocabulary parity with established editing literature makes the
output legible to anyone trained in the editorial tradition.

## Open questions / weak evidence

- The English-language editing taxonomy is not universal. In some
  scientific publishing traditions (e.g., German, Japanese), the
  developmental-vs-copyediting split is less sharp; "lektorat" or
  equivalent terms span multiple Anglophone categories.
- Practitioner-vocabulary documents (EFA's editorial levels, CIEP's
  editorial fact sheets) are the dominant source for the four-level
  gradient. Academic empirical work on whether these levels are
  cognitively or practically distinct is thin.
- The boundary between line editing and developmental editing is
  particularly soft: a heavy line edit and a light developmental edit
  produce similar artifacts. Scriptorium should not pretend the
  boundary is sharper than it is.

## References

[^1]: Einsohn A, Schwartz M. *The Copyeditor's Handbook: A Guide for
    Book Publishing and Corporate Communications*. 4th ed. University
    of California Press; 2019. ISBN 978-0520286726.

[^2]: Mossop B. *Revising and Editing for Translators*. 4th ed.
    Routledge; 2020. ISBN 978-1138895164. See chapter 17, "The
    Revision Parameters."

[^3]: Council of Science Editors. *Scientific Style and Format: The
    CSE Manual for Authors, Editors, and Publishers*. 9th ed.
    University of Chicago Press; 2024. ISBN 978-0226683942.
    https://www.csemanual.org/
