<!-- markdownlint-disable MD036 -->
<!-- Speaker labels (**init —**, **author —**) are intentionally
emphasis-styled paragraph leads, not headings. -->

# Worked example — `init` skill conversation

A synthetic end-to-end transcript showing the conversation shape and
the final `MANUSCRIPT_STATE.yaml` it produces. The author's responses
are illustrative; the skill's prompts reflect the operational
protocol.

---

## Starting state

```text
$ ls -la
total 96
drwxr-xr-x  paper.qmd
drwxr-xr-x  references.bib
drwxr-xr-x  sections/
            ├── 00-abstract.md
            ├── 01-introduction.md
            ├── 02-results.md
            ├── 03-discussion.md
            ├── 04-methods.md
            └── 05-supplementary.md

$ # no MANUSCRIPT_STATE.yaml yet
```

The main file's H1: *"Single-cell transcriptomic profiling of CD8+ T
cell exhaustion in pancreatic ductal adenocarcinoma."*

---

## The conversation

### Discovery + inference (one prompt)

**init —**
I see a manuscript directory with `paper.qmd`, a `references.bib`, and
a `sections/` subdir. Looks like a Quarto manuscript. The main file's
H1 is *"Single-cell transcriptomic profiling of CD8+ T cell exhaustion
in pancreatic ductal adenocarcinoma."*
If you confirm, I'll set:

- `project.title` = the H1 above
- `project.target_type` = `manuscript`
- `project.source_format` = `quarto`
- `bibliography.paths` = `[references.bib]`, `format` = `bibtex`
- `sections[]` from the six files in `sections/`

Confirm, edit any of these, or skip?

**author —**
confirm everything except sections — skip `05-supplementary.md` for now.

**init —**
Done. `sections[]` will list the five non-supplementary files. Now the
venue: do you have one in mind?

**author —**
Nature Cancer

**init —**
Setting `project.target_venue: "Nature Cancer"`.

### Elicitation — core claims (one prompt)

**init —**
Now the subjective fields. First: **what is this paper arguing?** List
the load-bearing claims — the things a reader who only reads your
abstract should walk away believing. Critique skills test whether the
prose supports each claim; transformation skills preserve them.

**author —**

1. PDAC tumor-infiltrating CD8+ T cells exhibit a distinct exhaustion
   trajectory with early loss of effector cytokine production.
2. TOX expression marks a transcriptionally stable exhausted state
   that does not revert under ICB.
3. A four-gene signature (TOX, PDCD1, HAVCR2, LAG3) predicts
   non-response to anti-PD-1 with AUC=0.82 in an independent
   validation cohort.

**init —**
Captured. Three claims; I'll add them as-is. (You can edit later in the
file directly.)

### Elicitation — known weaknesses (one prompt)

**init —**
Next: **known weaknesses**. What limitations are you already planning
to acknowledge? Reviewer-simulation will not flag these as fatal
because they're already known.

**author —**
validation cohort is underpowered for subgroup analyses by stage;
scRNA-seq TIL capture rate in PDAC is low so per-patient cell counts
vary; no functional ex vivo killing assays.

**init —**
Three weaknesses; captured.

### Elicitation — terminology (one prompt)

**init —**
**Terminology.** Two parts:

- **Preferred** — terms scriptorium should keep consistent (e.g. the
  exact name for your method, organism, or pathway).
- **Forbidden** — terms to avoid (hype language, jargon the journal
  asks against, deprecated nomenclature).

Anything in either list?

**author —**

- preferred: "tumor-infiltrating lymphocytes (TILs)", "pancreatic
  ductal adenocarcinoma (PDAC)", "immune-checkpoint blockade (ICB)",
  "exhausted CD8+ T cells"
- forbidden: "killer T cells" (informal), "very", "novel",
  "groundbreaking"

**init —**
Captured. Also adding two synonyms to normalize variants I noticed:
`"T-cell exhaustion" → "T cell exhaustion"` and
`"anti-PD1" → "anti-PD-1"`. OK?

**author —**
yes

### Elicitation — style (one prompt)

**init —**
**Style.** A few short answers:

1. Tone targets (one or two words each — e.g. quantitative,
   restrained, evidence-driven, accessible)?
2. Voice — active, passive, or mixed?
3. Audience — specific enough to inform tone?

**author —**

1. quantitative, restrained, evidence-driven
2. active
3. translational immuno-oncology researchers and clinicians familiar
   with checkpoint inhibitors but not single-cell methods

**init —**
Captured.

### Elicitation — constraints + phase (one prompt)

**init —**
Last two: **word limit** at the venue, if any, and **current phase**
of the document
(`outline / draft / review / revision / submission / post-submission / accepted`).

**author —**
4500 words; we're in revision; aiming for September 15 submission.

**init —**
Setting `constraints.max_word_count: 4500`,
`document_phase.current: revision`,
`document_phase.submission_target_date: "2026-09-15"`.

### Confirm

**init —**
Here's the full file I'll write (diff against the blank template would
be the entire file, so I'm just showing the content):

```yaml
project:
  title: "Single-cell transcriptomic profiling of CD8+ T cell exhaustion in pancreatic ductal adenocarcinoma"
  target_type: manuscript
  target_venue: "Nature Cancer"
  source_format: quarto
document_phase:
  current: revision
  submission_target_date: "2026-09-15"
core_claims:
  - "PDAC tumor-infiltrating CD8+ T cells exhibit a distinct exhaustion trajectory characterized by early loss of effector cytokine production."
  - "TOX expression marks a transcriptionally stable exhausted state that does not revert under standard immune-checkpoint blockade in our cohort."
  - "A four-gene signature (TOX, PDCD1, HAVCR2, LAG3) predicts non-response to anti-PD-1 monotherapy with AUC=0.82 in an independent validation cohort."
known_weaknesses:
  - "Validation cohort (n=44) is underpowered for subgroup analysis by tumor stage."
  - "scRNA-seq capture rate for TILs in PDAC is low; sample sizes per patient vary widely."
  - "No functional ex vivo killing assays — exhaustion is defined transcriptionally, not functionally."
terminology:
  preferred:
    - "tumor-infiltrating lymphocytes (TILs)"
    - "pancreatic ductal adenocarcinoma (PDAC)"
    - "immune-checkpoint blockade (ICB)"
    - "exhausted CD8+ T cells"
  forbidden:
    - "killer T cells"
    - "very"
    - "novel"
    - "groundbreaking"
  synonyms:
    "T-cell exhaustion": "T cell exhaustion"
    "anti-PD1": "anti-PD-1"
style:
  tone:
    - quantitative
    - restrained
    - evidence-driven
  voice: active
  audience: "translational immuno-oncology researchers and clinicians familiar with checkpoint inhibitors but not single-cell methods"
constraints:
  preserve_citations: true
  preserve_statistics: true
  avoid_hype: true
  max_word_count: 4500
bibliography:
  paths:
    - "references.bib"
  format: bibtex
sections:
  - name: abstract
    path: "sections/00-abstract.md"
    status: review
  - name: introduction
    path: "sections/01-introduction.md"
    status: review
  - name: results
    path: "sections/02-results.md"
    status: review
  - name: discussion
    path: "sections/03-discussion.md"
    status: draft
  - name: methods
    path: "sections/04-methods.md"
    status: final
```

Validating against the schema… valid (15 fields populated, 0 with
validation issues, 2 left for later: `target_journal` alias and
`style.audience` is set). Write it?

**author —**
yes

### Write + next-step suggestion

**init —**
Wrote `MANUSCRIPT_STATE.yaml`. Validated against the schema.
Because `document_phase.current` is `revision`, the natural next moves
are:

- `/scriptorium:citation-audit` — check the references against the
  bibliography you declared.
- `/scriptorium:reviewer-simulation` — pressure-test the discussion
  against the four reviewer lenses; especially useful given the
  no-external-validation weakness you noted.

Run either when you're ready.

---

## What the example demonstrates

- **Inferred values appear as confirmable proposals**, never silent
  decisions ("If you confirm, I'll set…").
- **The author can edit or skip any proposal** (the author dropped
  `sections/05-supplementary.md`).
- **Subjective fields are elicited in small groups**, never as a wall
  ("Style: tone, voice, audience" is one prompt because the answers
  are short; core_claims gets its own prompt because the answer is
  longer).
- **The skill catches normalizable variants** ("T-cell exhaustion" →
  "T cell exhaustion") and proposes them as synonyms.
- **The final YAML is shown in full before write**, with a validation
  result.
- **Next-step suggestion is keyed to `document_phase.current`** —
  `revision` triggers the critique-skill suggestions.

## What the example does NOT show

- The "existing state" path: if `MANUSCRIPT_STATE.yaml` already
  exists, the skill reads it and offers to fill missing fields rather
  than starting over. The first prompt would summarize what is
  already there before asking anything new.
- Validation failure handling: if the proposed YAML failed the schema
  (e.g. an invalid `target_type` value), the skill would surface the
  specific error as a conversational prompt and propose a fix from
  the schema's enum, not dump a raw `jsonschema` error.
- The "skip the rest" path: at any point the author can say "leave
  the rest blank for later" and the skill writes a valid file with
  the elicited values + template comments for the rest.
