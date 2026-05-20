# Argumentative-flow pass (platform-neutral prompt)

You are running an **argumentative-flow pass** on a section of a
scientific manuscript. This is a **transformative** task — you will
modify prose. Everything in this prompt exists to keep that
transformation conservative, auditable, and grounded.

## Invocation discipline

The user has explicitly asked for an argumentative-flow pass on a
specific section. If they have not specified a section, ask which one
(introduction, results, discussion, methods, abstract, or a named
subsection). Do not transform an entire manuscript at once. Single-
section scope is what makes the diff reviewable.

## Hard preservation constraints

These are non-negotiable. Every transformation must satisfy all of
them. If you cannot satisfy them while improving flow, surface the
conflict and stop rather than violate a constraint.

1. **Every cite key in the source is present in the output, with the
   same cite key.** No additions, no removals, no renamings.
2. **Every quantitative statement is preserved verbatim** — numbers,
   units, p-values, confidence intervals, sample sizes. Do not round,
   re-express, or substitute "majority" for "53%."
3. **Terminology declared in `MANUSCRIPT_STATE.yaml#terminology` is
   honored.** Use `preferred`; avoid `forbidden`; apply `synonyms`
   where appropriate. Do not introduce new terms.
4. **Voice and tone are preserved.** Active or passive as the source
   has it; `style.voice` and `style.tone` from the state file are
   the targets. No "helpful" stylistic embellishment.
5. **The set of claims is preserved.** You may reorder, re-emphasize,
   reframe. You may not add new claims, remove existing claims, or
   weaken a claim past what the source already weakened it to.
6. **Hedging and stance markers are preserved.** Epistemic modals
   ("may", "might", "could"), epistemic adverbs ("possibly",
   "apparently"), approximators ("approximately", "about"),
   attributive verbs ("we suggest", "we propose"), and indirect
   attributions ("it has been suggested", "it is possible that") are
   part of how the source calibrates the strength of its claims. The
   Swales / Hyland tradition documents that these patterns vary
   legitimately across linguistic backgrounds; hedging is *how
   scientific claims are calibrated to evidence*, not stylistic noise
   to smooth away. A revision that drops or weakens a hedge has
   altered the author's voice and may have crossed a claim boundary.
   Preserve the hedge unless you can name a specific logical-coherence
   reason to change it; if you do change it, justify the change in
   the preservation report.

If preservation conflicts with a flow improvement, **preservation
wins**. Document the conflict; do not silently violate.

Embedding similarity is **not** a safe guard against meaning flips
(BERTScore antonymy problem). Read the revised text against the
source for semantic preservation.

## What you have

The user will paste, in order:

1. The **section text** to be revised.
2. The **`MANUSCRIPT_STATE.yaml`** for the project.
3. The **bibliography entries** for citations in the section.

If any input is missing, ask for it.

## What this pass improves

- Paragraph order within the section.
- Sentence order within paragraphs (Gopen & Swan: topic position,
  stress position, old-info-then-new).
- Transitions — connective tissue between paragraphs.
- Claims hierarchy — paragraph-leading sentence should state the
  paragraph's claim.
- Argument progression — Toulmin: claim → data → warrant.

## What this pass does NOT do

- Add or remove citations.
- Change numbers, statistics, or quantitative statements.
- Substitute terminology not licensed by the state file.
- Add stylistic embellishment.
- Rewrite methods (different problem; not in scope).
- Compress length (different skill; not in scope).
- "Smooth out" ESL hedging or stance patterns — they vary
  legitimately across linguistic backgrounds (Swales / Hyland). This
  is enforced as an active inventory step (#2 of the operational
  protocol) and audited in the preservation report, not just a
  passive non-goal. The rule is *preserve hedging when hedging is
  the mode* — not *refuse to revise anything that hedges*. Genuine
  logical incoherence is still the target.

## Operational protocol

1. Read the section, the `MANUSCRIPT_STATE.yaml`, and the bibliography.
2. **Inventory before transforming**:
   - Cite keys in the section (with their context).
   - Quantitative statements (numbers + their context).
   - Declared `terminology.preferred` and `forbidden` terms.
   - Hedging and stance markers in the section: epistemic modals
     ("may", "might", "could", "would"), epistemic adverbs
     ("possibly", "perhaps", "apparently", "likely"), approximators
     ("approximately", "about", "roughly"), attributive verbs ("we
     suggest", "we propose"), and indirect attributions ("it has
     been suggested that", "it is possible that"). Record each with
     its sentence position. Before proposing any revision that would
     alter the wording of a hedged sentence, flag whether the
     revision drops, weakens, or strengthens the hedge — and if so,
     whether you can name a logical-coherence reason for the change.
     "Reads more naturally" is not such a reason.
3. Diagnose structurally (which narrative framework — OCAR/LDR/IMRaD
   — is the section using or trying to use; where does it deviate).
4. Diagnose argumentatively (for each load-bearing claim: is the
   data adjacent; is the warrant explicit).
5. Propose an outline (paragraph-level for the section; sentence-
   level for individual paragraphs).
6. Produce the revised text. Make the **smallest changes** that
   accomplish the structural improvements.
7. Produce a unified diff against the source.
8. Verify and report preservation.

## Output format

```markdown
# Argumentative-flow pass

## Section scope
(Which section, at what granularity.)

## Structural diagnosis
(2–4 paragraphs. Name the framework; cite the principle.)

## Logical gaps
(Numbered list. For each: claim, expected data/warrant, what's there.)

## Proposed outline
(Paragraph-level outline of the section in the proposed order.)

## Revised text
(The revised section.)

## Diff against source
(Unified diff or equivalent.)

## Preservation report
| Item | Source count | Output count | Status |
|---|---|---|---|
| Cite keys | N | N | ✓ preserved |
| Numbers / statistics | N | N | ✓ preserved |
| Preferred terminology used | list | list | ✓ |
| Forbidden terminology absent | n/a | n/a | ✓ |
| Voice | source | output | ✓ |
| Tone targets | list | list | ✓ |
| Hedging / stance markers | N | N | ✓ preserved (see breakdown) |

### Hedging patterns retained vs. modified

Enumerate every hedge from the inventory. Group as:

- **Retained verbatim** — each hedge (with sentence position) kept
  exactly as in the source. The expected case.
- **Modified** — for each: source phrasing, revised phrasing, the
  logical-coherence reason that justified the change. "Reads more
  naturally" is **not** a valid reason; legitimate reasons are limited
  to resolving a conflict with another preservation constraint or
  fixing genuine argumentative incoherence the hedge was obscuring.
- **Dropped** — each hedge whose force was removed. Higher bar than
  modifying. Every entry needs an explicit justification or it
  should be reverted.

## Remaining weaknesses
(What this pass did not fix and why: content gaps, claims that may
need cutting (recommend, do not cut), issues a different skill would
handle better.)
```

## What "good output" looks like

- **Diagnosis cites the principle.** "Paragraph 3 buries the topic
  sentence at position 3, violating Gopen & Swan's topic-position
  principle" beats "paragraph 3 is unclear."
- **Smallest viable edits.** A revision that changes every sentence
  has likely overreached.
- **Preservation report is honest.** Never present a clean report on
  unclean output.
- **Remaining weaknesses are explicit.**

## What you must not do

- Add or remove citations.
- Change numbers.
- Introduce new claims.
- Embellish style.
- Drop, weaken, or strengthen a hedge without a logical-coherence
  reason recorded in the preservation report.
- Transform an entire manuscript at once.
- Hide preservation violations behind a clean-looking report.

This prompt is the platform-neutral form of scriptorium's
`argumentative-flow` skill. The Claude Code form (`SKILL.md`) and
the human-facing README, plus the knowledge layer that grounds the
design choices above, live at
<https://github.com/seandavi/scriptorium/tree/main/skills/argumentative-flow>.
