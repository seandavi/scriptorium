---
title: Convert your manuscript to markdown
description: Scriptorium works best on markdown-flavored manuscript text. This guide covers the common source formats.
sidebar:
  order: 20
---

Scriptorium [works best on markdown-flavored manuscript text](/concepts/design/). This guide covers the common source formats. Pick the section that matches yours.

## Already markdown (Quarto, plain `.md`, Pandoc Markdown)

No conversion needed. Skip to [Install](/how-to/install/) and start running skills.

## Microsoft Word (`.docx`)

Recommended: [pandoc](https://pandoc.org/).

```bash
pandoc manuscript.docx -o manuscript.md --wrap=preserve --markdown-headings=atx
```

Alternative: [mammoth](https://github.com/mwilliamson/python-mammoth) (better for Word-styled documents).

```bash
mammoth manuscript.docx --output-format=markdown > manuscript.md
```

What you lose: tracked changes, comments, complex tables, embedded images-as-objects. Re-resolve manually if relevant.

## LaTeX (`.tex`)

```bash
pandoc manuscript.tex -o manuscript.md \
  --bibliography references.bib \
  --citeproc \
  --wrap=preserve
```

What you lose: custom macros; complex math environments survive but rarely render in markdown viewers; TikZ figures need separate export.

## Google Docs

File → Download → Markdown (`.md`) — built-in since 2024. Or download as Word and use the `.docx` instructions above.

## Overleaf / shared LaTeX

Use the LaTeX instructions above on the project's main `.tex`.

## PDF (last resort)

Quality varies. Try:

```bash
pdftotext -layout manuscript.pdf manuscript.txt
```

Or [marker](https://github.com/VikParuchuri/marker) / [nougat](https://github.com/facebookresearch/nougat) for academic PDF OCR. Expect manual cleanup. Citations, figure refs, and table structure usually need re-resolution.

## After conversion

- Validate that citations and figure references survived (a quick diff against the source helps).
- Populate `MANUSCRIPT_STATE.yaml` with `project.source_format:` set to the original format (`docx-via-pandoc`, `latex`, `gdocs-export`, etc.) — this is a hint for skills that may apply format-specific parsing in v0.2+.
- Run `scriptorium validate <state-file>` before running any skills.

## Related

- [Design — manuscript format scope](/concepts/design/) — why scriptorium leans on markdown.
- [GitHub issue #25](https://github.com/seandavi/scriptorium/issues/25) — the canonical tracking issue.
