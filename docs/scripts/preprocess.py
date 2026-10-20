#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6.0"]
# ///
"""Preprocess source markdown + Quarto into the Astro/Starlight content tree.

Six things happen:

1. Top-level repo docs (`DESIGN.md`, `docs/roadmap.md`) are copied into the
   site as standalone pages with appropriate frontmatter.
2. The `knowledge/` tree is mirrored under
   `docs/src/content/docs/concepts/knowledge/`, with Obsidian-style
   `[[wikilinks]]` rewritten to Starlight URLs and frontmatter added.
3. Any `.qmd` files in `knowledge/` are rendered via quartobot (citation
   resolution from inline `@pmid:` / `@doi:` keys) plus Quarto (citeproc
   rendering); the resulting markdown is then put through the same
   wikilink / frontmatter pass as the `.md` knowledge docs.
4. Any `.qmd` files found under `docs/qmd/` (currently none) are
   rendered via the Quarto CLI directly into the content tree.
5. The skills reference page (``docs/src/content/docs/reference/skills.md``)
   is regenerated from each ``skills/<name>/manifest.yaml``. Categorisation,
   lifecycle fit, modifies-or-suggests, author-side-only flag, and required
   bibliography are all read from the manifests; the table cannot drift
   from the manifests because the manifests are the source.
6. Concept pages that mix hand-written prose with manifest-driven tables
   (``concepts/workflow-stage.md`` skill-by-stage table,
   ``concepts/guidance-level.md`` per-skill block) have their generated
   blocks replaced in-place between sentinel comments. The surrounding
   prose stays under version control; only the bracketed block changes.

Quartobot and Quarto are optional — if neither is installed and no `.qmd`
files exist, the relevant steps no-op cleanly.

The generated output is gitignored; the source of truth lives at the
repo root. Contributors edit `knowledge/*.{md,qmd}` and run
`just preprocess` to refresh the site.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

DOCS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = DOCS_DIR.parent
KNOWLEDGE_SRC = REPO_ROOT / "knowledge"
DESIGN_SRC = REPO_ROOT / "DESIGN.md"
ROADMAP_SRC = REPO_ROOT / "docs" / "roadmap.md"
SKILLS_SRC = REPO_ROOT / "skills"

CONTENT_ROOT = DOCS_DIR / "src" / "content" / "docs"
KNOWLEDGE_OUT = CONTENT_ROOT / "concepts" / "knowledge"
DESIGN_OUT = CONTENT_ROOT / "concepts" / "design.md"
ROADMAP_OUT = CONTENT_ROOT / "roadmap.md"
SKILLS_OUT = CONTENT_ROOT / "reference" / "skills.md"
WORKFLOW_STAGE_OUT = CONTENT_ROOT / "concepts" / "workflow-stage.md"
GUIDANCE_LEVEL_OUT = CONTENT_ROOT / "concepts" / "guidance-level.md"
QMD_SRC = DOCS_DIR / "qmd"

# Knowledge subdirectories rendered as sidebar sections — display name +
# sidebar order. Unlisted subdirs fall back to Starlight's default
# (folder-name as label, alphabetic order).
SUBDIR_DISPLAY = {
    "prior-art": ("Prior art", 10),
    "scientific-writing": ("Scientific writing", 20),
    "peer-review": ("Peer review", 30),
    "citations": ("Citations", 40),
    "editing": ("Editing", 50),
    "grants": ("Grants", 60),
    "critique-techniques": ("Critique techniques", 70),
    "reproducibility": ("Reproducibility", 80),
}

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def extract_title(text: str) -> str | None:
    """Return the first H1 in ``text``, or None if none present."""
    m = H1_RE.search(text)
    return m.group(1).strip() if m else None


def strip_first_h1(text: str) -> str:
    """Remove the first H1 line so Starlight's frontmatter title is the sole H1."""
    return H1_RE.sub("", text, count=1).lstrip("\n")


def yaml_quote(s: str) -> str:
    """Quote a string for YAML — handles colons, quotes, embedded newlines."""
    safe = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()
    return f'"{safe}"'


def build_knowledge_index() -> dict[str, Path]:
    """Map every knowledge doc slug to its path relative to KNOWLEDGE_SRC.

    Both `.md` and `.qmd` source files are indexed; the slug is the
    filename stem, so `[[citation-accuracy-evidence]]` resolves
    regardless of which extension the source uses.
    """
    index: dict[str, Path] = {}
    if not KNOWLEDGE_SRC.is_dir():
        return index
    for src in KNOWLEDGE_SRC.rglob("*"):
        if src.name == "README.md":
            continue
        if src.suffix in {".md", ".qmd"}:
            index[src.stem] = src.relative_to(KNOWLEDGE_SRC)
    return index


def render_qmd(qmd_path: Path) -> str:
    """Render a knowledge .qmd file to GFM markdown via quartobot + Quarto.

    Runs the resolve-then-render dance: quartobot resolves persistent-ID
    cite keys (`@pmid:`, `@doi:`) to CSL JSON, then `quarto render`
    produces final markdown with citations formatted via citeproc. The
    rendered markdown is returned as a string; nothing is left in the
    source tree (the Quarto build dir and the resolved references.json
    are gitignored anyway).
    """
    if shutil.which("quarto") is None:
        raise RuntimeError(
            f"Quarto is required to render {qmd_path.relative_to(REPO_ROOT)}. "
            "Install from https://quarto.org/docs/get-started/."
        )
    if shutil.which("quartobot") is None:
        raise RuntimeError(
            f"quartobot is required to render {qmd_path.relative_to(REPO_ROOT)} "
            "(citation resolution from inline @pmid: / @doi: keys). "
            "Install with: uv tool install quartobot"
        )

    src_dir = qmd_path.parent
    # quartobot writes references.json into the .qmd's directory; the
    # .qmd's frontmatter references it relatively. The file is gitignored.
    resolve_cmd = [
        "quartobot",
        "resolve",
        "--from-scan",
        str(src_dir),
        "--output",
        str(src_dir / "references.json"),
        "--id-mode",
        "citation-key",
    ]
    result = subprocess.run(resolve_cmd, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        raise RuntimeError(f"quartobot resolve failed for {qmd_path}")

    with tempfile.TemporaryDirectory() as tmpdir:
        render_cmd = [
            "quarto",
            "render",
            str(qmd_path),
            "--to",
            "gfm",
            "--output-dir",
            tmpdir,
        ]
        result = subprocess.run(render_cmd, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            sys.stderr.write(result.stdout)
            sys.stderr.write(result.stderr)
            raise RuntimeError(f"quarto render failed for {qmd_path}")
        rendered = Path(tmpdir) / (qmd_path.stem + ".md")
        if not rendered.is_file():
            raise RuntimeError(
                f"Expected Quarto to produce {rendered.name}; found "
                f"{[p.name for p in Path(tmpdir).iterdir()]}"
            )
        return rendered.read_text(encoding="utf-8")


def rewrite_wikilinks(text: str, index: dict[str, Path]) -> str:
    """Convert ``[[slug]]`` and ``[[slug|display]]`` to Starlight links."""

    def repl(m: re.Match[str]) -> str:
        target = m.group(1).strip()
        display = (m.group(2) or target).strip()
        rel = index.get(target)
        if rel is None:
            # Unresolved wikilink — render literally so it's visible
            # for follow-up cleanup instead of silently dropping.
            return f"`[[{target}]]`"
        url_path = rel.with_suffix("").as_posix()
        return f"[{display}](/concepts/knowledge/{url_path}/)"

    return WIKILINK_RE.sub(repl, text)


def fix_relative_md_links(text: str) -> str:
    """Strip the trailing ``.md`` from intra-knowledge relative links.

    Existing knowledge docs link to siblings with paths like
    ``(critique-techniques/statistical-inconsistency.md)``. Starlight URLs
    don't carry the extension; drop it.
    """
    return re.sub(
        r"\]\(([^)]+?)\.md(#[^)]+)?\)",
        lambda m: f"]({m.group(1)}{m.group(2) or ''}/)",
        text,
    )


def rewrite_repo_root_links(text: str) -> str:
    """Rewrite ``../docs/roadmap.md`` and ``../CONTRIBUTING.md`` style links.

    The knowledge README links back to repo-root docs with relative paths
    that break inside the site. Map the common ones to site URLs or to
    GitHub URLs for files not (yet) hosted in the site.
    """
    repl_map = {
        "(../docs/roadmap.md)": "(/roadmap/)",
        "(../CONTRIBUTING.md)": (
            "(https://github.com/seandavi/scriptorium/blob/main/CONTRIBUTING.md)"
        ),
        "(../DESIGN.md)": "(/concepts/design/)",
        "(../README.md)": "(/)",
    }
    for old, new in repl_map.items():
        text = text.replace(old, new)
    return text


def write_with_frontmatter(
    dest: Path,
    title: str,
    body: str,
    description: str | None = None,
    sidebar_order: int | None = None,
) -> None:
    """Write a Starlight markdown file with frontmatter to ``dest``."""
    lines = ["---", f"title: {yaml_quote(title)}"]
    if description:
        lines.append(f"description: {yaml_quote(description)}")
    if sidebar_order is not None:
        lines.append(f"sidebar:\n  order: {sidebar_order}")
    lines.append("---")
    lines.append("")
    lines.append(body.lstrip("\n"))
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(lines), encoding="utf-8")


def emit_directory_landing(subdir: str) -> None:
    """Write an index.md for a knowledge subdirectory so it has a landing page."""
    display, order = SUBDIR_DISPLAY.get(subdir, (subdir.replace("-", " ").title(), 999))
    dest = KNOWLEDGE_OUT / subdir / "index.md"
    if dest.exists():
        return
    body = (
        f"The {display.lower()} subsection of the knowledge layer. Browse the "
        "individual documents from the sidebar."
    )
    write_with_frontmatter(
        dest,
        title=display,
        body=body,
        description=f"Knowledge layer — {display.lower()}.",
        sidebar_order=order,
    )


def _iter_knowledge_sources() -> list[Path]:
    """Yield every `.md` and `.qmd` source file under knowledge/, sorted."""
    sources: list[Path] = []
    for path in KNOWLEDGE_SRC.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".qmd"}:
            sources.append(path)
    return sorted(sources)


def process_knowledge() -> int:
    """Mirror knowledge/ into the site. Return the count of files processed."""
    if not KNOWLEDGE_SRC.is_dir():
        print("  (no knowledge/ directory; skipping)")
        return 0
    if KNOWLEDGE_OUT.exists():
        shutil.rmtree(KNOWLEDGE_OUT)
    KNOWLEDGE_OUT.mkdir(parents=True, exist_ok=True)
    index = build_knowledge_index()

    count = 0
    for src_path in _iter_knowledge_sources():
        rel = src_path.relative_to(KNOWLEDGE_SRC)

        # .qmd files go through quartobot + Quarto to resolve citations
        # before the standard knowledge-doc post-processing kicks in.
        if src_path.suffix == ".qmd":
            print(f"  rendering {rel} via quartobot + Quarto")
            text = render_qmd(src_path)
            # The site URL for a .qmd is the same as for a .md with the
            # same stem — strip the suffix when computing the destination.
            rel = rel.with_suffix(".md")
        else:
            text = src_path.read_text(encoding="utf-8")

        # Strip any pre-existing frontmatter — we generate our own.
        text = FRONTMATTER_RE.sub("", text, count=1)
        title = extract_title(text) or src_path.stem
        body = strip_first_h1(text)
        body = rewrite_wikilinks(body, index)
        body = fix_relative_md_links(body)
        body = rewrite_repo_root_links(body)

        # Top-level knowledge/README → concepts/knowledge/index.md
        if src_path == KNOWLEDGE_SRC / "README.md":
            dest = KNOWLEDGE_OUT / "index.md"
            write_with_frontmatter(
                dest,
                title="Knowledge layer",
                body=body,
                description="The evidence base scriptorium's skills ground in.",
                sidebar_order=0,
            )
        else:
            dest = KNOWLEDGE_OUT / rel
            write_with_frontmatter(dest, title=title, body=body)
        count += 1

    # One landing page per subdirectory so the sidebar tree is navigable.
    for subdir in sorted({p.parts[0] for p in index.values() if len(p.parts) > 1}):
        emit_directory_landing(subdir)

    return count


def process_root_docs() -> None:
    """Copy DESIGN.md and roadmap.md into the site with Starlight frontmatter."""
    if DESIGN_SRC.is_file():
        text = DESIGN_SRC.read_text(encoding="utf-8")
        text = FRONTMATTER_RE.sub("", text, count=1)
        title = extract_title(text) or "Design"
        body = strip_first_h1(text)
        write_with_frontmatter(
            DESIGN_OUT,
            title=title,
            body=body,
            description=(
                "The agentic-scriptorium thesis, design philosophy, and the shared-state contract."
            ),
            sidebar_order=0,
        )
        print(f"  wrote {DESIGN_OUT.relative_to(DOCS_DIR)}")
    else:
        print("  (no DESIGN.md; skipping)")

    if ROADMAP_SRC.is_file():
        text = ROADMAP_SRC.read_text(encoding="utf-8")
        text = FRONTMATTER_RE.sub("", text, count=1)
        title = extract_title(text) or "Roadmap"
        body = strip_first_h1(text)
        write_with_frontmatter(
            ROADMAP_OUT,
            title=title,
            body=body,
            description="What ships when, and why.",
        )
        print(f"  wrote {ROADMAP_OUT.relative_to(DOCS_DIR)}")
    else:
        print("  (no docs/roadmap.md; skipping)")


def process_qmd() -> int:
    """Render any .qmd files under docs/qmd/ into matching .md output via quarto."""
    if not QMD_SRC.is_dir():
        return 0
    qmd_files = sorted(QMD_SRC.rglob("*.qmd"))
    if not qmd_files:
        return 0
    if shutil.which("quarto") is None:
        print(
            "  ! .qmd source files exist under docs/qmd/ but quarto is "
            "not installed. Install from https://quarto.org/docs/get-started/."
        )
        return 0
    count = 0
    for qmd in qmd_files:
        rel = qmd.relative_to(QMD_SRC)
        out_md = CONTENT_ROOT / rel.with_suffix(".md")
        out_md.parent.mkdir(parents=True, exist_ok=True)
        cmd = [
            "quarto",
            "render",
            str(qmd),
            "--to",
            "gfm",
            "--output",
            str(out_md.name),
            "--output-dir",
            str(out_md.parent),
        ]
        print(f"  quarto render {rel}")
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            sys.exit(result.returncode)
        count += 1
    return count


# ---------------------------------------------------------------------------
# Skills reference page generator
# ---------------------------------------------------------------------------
#
# Replaces the previously hand-maintained
# ``docs/src/content/docs/reference/skills.md``. The page is regenerated
# on every ``just preprocess`` from each ``skills/<name>/manifest.yaml``,
# so the table cannot drift from what actually ships.
#
# Output shape matches the hand-maintained page that shipped in PR #101:
# a top-level table, a per-category detail section with one table per
# category, a lifecycle-fit summary, an author-side-only callout, and a
# source-of-truth footer. The generator is deterministic — running it
# twice on unchanged manifests produces byte-identical output.

# Categories rendered in display order, with the short description used
# under each per-category detail heading.
_CATEGORY_ORDER: list[tuple[str, str, str]] = [
    (
        "critique",
        "Critique",
        "Critique skills assess existing prose and emit structured findings. "
        "They do not modify the manuscript and they do not invent citations.",
    ),
    (
        "validation",
        "Validation",
        "Validation skills check existing prose against an external standard "
        "and emit structured findings. They do not modify the manuscript.",
    ),
    (
        "normalization",
        "Normalization",
        "Normalization skills enforce author-declared style and terminology. "
        "They emit a structured report plus a list of suggested edits. They "
        "do not auto-apply edits to the manuscript file.",
    ),
    (
        "transformation",
        "Transformation",
        "Transformation skills modify prose. Both shipped transformation "
        "skills inherit the same preservation contract — citations, "
        "statistics, declared terminology, declared core claims, and the "
        "author's hedging stance are preserved or surfaced as per-edit notes. "
        "Both are explicit-invocation only and operate on a single named "
        "section at a time. The author reviews each diff and decides.",
    ),
    (
        "meta",
        "Meta",
        "Meta skills orient new users and explain scriptorium itself. They "
        "read no manuscript content and modify nothing.",
    ),
    (
        "utility",
        "Utility",
        "Utility skills set up scriptorium state. They modify "
        "`MANUSCRIPT_STATE.yaml` (and only that file) when the author confirms.",
    ),
]

# Lifecycle phases declared in the JSON Schema, in render order.
_PHASES_IN_ORDER: list[str] = ["outline", "draft", "review", "revision", "submission"]
_ALL_PHASES_SET: frozenset[str] = frozenset(_PHASES_IN_ORDER)

# Conventions docs are universal scaffolding rather than topical
# grounding; they're filtered from the "Primary grounding" column so the
# detail tables stay readable.
_GROUNDING_FILTER_PREFIXES: tuple[str, ...] = (
    "knowledge/conventions/",
    "knowledge/README.md",
    "schemas/",
)


def _load_manifests() -> list[dict[str, Any]]:
    """Load every ``skills/<name>/manifest.yaml`` into a dict.

    Sorted by skill name for deterministic output.
    """
    manifests: list[dict[str, Any]] = []
    if not SKILLS_SRC.is_dir():
        return manifests
    for skill_dir in sorted(SKILLS_SRC.iterdir(), key=lambda p: p.name):
        if not skill_dir.is_dir():
            continue
        manifest_path = skill_dir / "manifest.yaml"
        if not manifest_path.is_file():
            continue
        with manifest_path.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        if not isinstance(data, dict):
            continue
        # Normalize: ensure required keys exist with sensible defaults so
        # downstream code can avoid defensive .get() everywhere.
        data.setdefault("name", skill_dir.name)
        data.setdefault("category", "unknown")
        data.setdefault("modifies", [])
        data.setdefault("grounding", [])
        data.setdefault("inputs", [])
        data.setdefault("lifecycle_phases", [])
        manifests.append(data)
    return manifests


def _normalise_description(raw: str) -> str:
    """Collapse a YAML folded-scalar description into one line."""
    return " ".join(str(raw).split()).strip()


def _first_sentence(text: str) -> str:
    """Return the first sentence of ``text``, preserving its terminator.

    Cheap heuristic: scan for the first period/question/exclamation
    followed by whitespace or end-of-string. Falls back to the whole
    string on no terminator.
    """
    text = _normalise_description(text)
    match = re.search(r"[.!?](\s|$)", text)
    if match is None:
        return text
    return text[: match.start() + 1].strip()


def _render_lifecycle(phases: list[str]) -> str:
    """Render a list of phase strings for the main table.

    All five canonical phases collapse to "any phase". Otherwise the
    phases render in canonical order separated by "·".
    """
    phase_set = set(phases)
    if phase_set >= _ALL_PHASES_SET:
        return "any phase"
    ordered = [p for p in _PHASES_IN_ORDER if p in phase_set]
    if not ordered:
        return "not declared"
    return " · ".join(ordered)


def _render_modifies(manifest: dict[str, Any]) -> str:
    """Render the ``modifies`` column for the main table.

    Categories drive most of the answer:
      - ``transformation`` and ``normalization`` skills always render as
        ``suggests`` — they propose edits but never auto-apply (their
        manifest's ``modifies:`` field declares the *intended scope* of
        the suggestion, not an auto-apply contract; see argumentative-flow
        and compression for canonical examples).
      - For other categories, the ``modifies:`` list drives the result:
        - empty list → ``no``
        - state-file-only target → ``state file only`` (or
          ``state file only (opt-in)`` if the skill is critique-category
          and the write is a documented side-effect, e.g. venue-fit).
    """
    category = manifest.get("category")
    if category in {"transformation", "normalization"}:
        return "suggests"
    modifies = manifest.get("modifies") or []
    if not modifies:
        return "no"
    targets = [str(t) for t in modifies]
    state_only = all(
        t.startswith("MANUSCRIPT_STATE") or t == "manuscript_state_yaml" for t in targets
    )
    if state_only:
        if category == "critique":
            return "state file only (opt-in)"
        return "state file only"
    return "suggests"


def _render_author_side(manifest: dict[str, Any]) -> str:
    return "**yes**" if manifest.get("positioning") == "author-side-only" else "no"


def _render_reqs_bib(manifest: dict[str, Any]) -> str:
    """Find the ``bibliography`` input and report whether it's required."""
    inputs = manifest.get("inputs") or []
    for entry in inputs:
        if not isinstance(entry, dict):
            continue
        if entry.get("name") == "bibliography":
            return "yes" if entry.get("required") else "optional"
    return "no"


def _topical_grounding(manifest: dict[str, Any], *, limit: int = 3) -> list[str]:
    """Return up to ``limit`` non-conventions grounding paths."""
    out: list[str] = []
    for path in manifest.get("grounding") or []:
        path_str = str(path)
        if path_str.startswith(_GROUNDING_FILTER_PREFIXES):
            continue
        out.append(path_str)
        if len(out) >= limit:
            break
    return out


def _skill_repo_link(name: str) -> str:
    return f"https://github.com/seandavi/scriptorium/blob/main/skills/{name}/README.md"


def _grounding_repo_link(path: str) -> str:
    """Render ``knowledge/foo/bar.md`` as a markdown link to the repo."""
    slug = Path(path).stem
    href = f"https://github.com/seandavi/scriptorium/blob/main/{path}"
    return f"[`{slug}`]({href})"


def _render_main_table(manifests: list[dict[str, Any]]) -> str:
    rows = [
        "| Skill | Category | Lifecycle fit | Modifies | Author-side only | Reqs bib |",
        "|---|---|---|---|---|---|",
    ]
    for m in manifests:
        name = m["name"]
        rows.append(
            "| "
            + " | ".join(
                [
                    f"[`{name}`]({_skill_repo_link(name)})",
                    str(m.get("category", "")),
                    _render_lifecycle(m.get("lifecycle_phases") or []),
                    _render_modifies(m),
                    _render_author_side(m),
                    _render_reqs_bib(m),
                ]
            )
            + " |"
        )
    return "\n".join(rows)


def _render_category_section(label: str, intro: str, manifests: list[dict[str, Any]]) -> str:
    """Render one per-category detail section."""
    body = [f"### {label}", "", intro, ""]
    body.append("| Skill | One line | Primary grounding |")
    body.append("|---|---|---|")
    for m in manifests:
        name = m["name"]
        one_line = _first_sentence(m.get("description", ""))
        grounding_links = ", ".join(_grounding_repo_link(g) for g in _topical_grounding(m)) or "—"
        body.append(f"| `{name}` | {one_line} | {grounding_links} |")
    return "\n".join(body)


def _render_lifecycle_summary(manifests: list[dict[str, Any]]) -> str:
    """Render the "Lifecycle fit, summarised" table.

    Each canonical phase maps to the skills that declare it in
    ``lifecycle_phases``. The result is bucketed for readability:
    show the *new* skills at each phase, not the cumulative set, so
    the table conveys what unlocks where.
    """
    by_phase: dict[str, list[str]] = {p: [] for p in _PHASES_IN_ORDER}
    for m in manifests:
        for phase in m.get("lifecycle_phases") or []:
            if phase in by_phase:
                by_phase[phase].append(m["name"])
    # Cumulative: at each phase, list every skill that's invocable.
    rows = ["| Phase | Skills invocable |", "|---|---|"]
    for phase in _PHASES_IN_ORDER:
        names = by_phase[phase]
        if not names:
            cell = "—"
        else:
            cell = ", ".join(f"`{n}`" for n in sorted(names))
        rows.append(f"| `{phase}` | {cell} |")
    return "\n".join(rows)


def _render_author_side_list(manifests: list[dict[str, Any]]) -> str:
    items = []
    for m in manifests:
        if m.get("positioning") == "author-side-only":
            items.append(f"- `{m['name']}`")
    if not items:
        return "_(no author-side-only skills currently ship.)_"
    return "\n".join(items)


def _generate_skills_page(manifests: list[dict[str, Any]]) -> str:
    """Return the full markdown for the regenerated skills page."""
    by_category: dict[str, list[dict[str, Any]]] = {}
    for m in manifests:
        by_category.setdefault(m.get("category", "unknown"), []).append(m)

    parts: list[str] = []
    parts.append(
        "---\n"
        "title: Skills\n"
        'description: "Every shipped scriptorium skill, organised by category and '
        'lifecycle stage, with grounding pointers."\n'
        "sidebar:\n"
        "  order: 10\n"
        "---\n"
    )
    parts.append(
        "<!--\n"
        "  GENERATED FILE — DO NOT EDIT BY HAND.\n"
        "  Regenerated by docs/scripts/preprocess.py from every\n"
        "  skills/<name>/manifest.yaml. Edit the manifest, not this file.\n"
        "-->\n"
    )
    parts.append(
        "Every scriptorium skill is single-responsibility, reads "
        "`MANUSCRIPT_STATE.yaml`, and emits structured markdown. The table "
        "below is generated from each skill's `manifest.yaml` at docs-build "
        "time — `category`, lifecycle fit, modifies-manuscript, "
        "author-side-only, and required bibliography all come straight from "
        "the manifest fields.\n"
    )
    parts.append(
        "Each row links to the skill's `README.md` in the repo, which is the "
        "full operational contract (inputs, outputs, refusal behaviours, "
        "output schema, complete grounding list).\n"
    )
    parts.append("## Categorisation axes\n")
    parts.append(
        "Three axes give you most of what you need to decide which skill to "
        "run next:\n\n"
        "- **Category** — what kind of operation the skill performs.\n"
        "  - *critique* — assesses; does not modify the manuscript.\n"
        "  - *validation* — checks against an external standard; does not modify.\n"
        "  - *normalization* — enforces declared style; suggests edits, "
        "never auto-applies.\n"
        "  - *transformation* — modifies prose under a preservation contract.\n"
        "  - *meta* — orientation or explanation; no manuscript modification.\n"
        "  - *utility* — bootstrap; modifies only `MANUSCRIPT_STATE.yaml`.\n"
        "- **Lifecycle stage** — which `document_phase` values the skill is "
        "invokable in. Skills refuse cleanly on phases for which they do "
        "not have enough declared state to ground against.\n"
        "- **Modifies the manuscript?** — *no* (most critique skills), "
        "*suggests* (normalization and transformation skills emit diffs the "
        "author reviews and applies), or *state file only* (utility, or "
        "opt-in for some critique skills).\n"
    )
    parts.append(
        "Two additional flags some authors need:\n\n"
        "- **Author-side only?** — *yes* for skills whose `manifest.yaml` "
        "declares `positioning: author-side-only`. Editorial-side use "
        "violates ICMJE / NIH / major-publisher policy and the skill itself "
        "refuses to run on a manuscript the user did not author.\n"
        "- **Requires bibliography?** — *yes* when the manifest's "
        "`bibliography` input is `required: true`; *optional* when the "
        "input is declared but not required; *no* when the manifest does "
        "not declare a `bibliography` input at all.\n"
    )
    parts.append("## All shipped skills\n")
    parts.append(_render_main_table(manifests) + "\n")
    parts.append("## Per-category detail\n")
    for cat_key, cat_label, cat_intro in _CATEGORY_ORDER:
        cat_manifests = sorted(by_category.get(cat_key, []), key=lambda m: m["name"])
        if not cat_manifests:
            continue
        parts.append(_render_category_section(cat_label, cat_intro, cat_manifests) + "\n")
    parts.append("## Lifecycle fit, summarised\n")
    parts.append(
        "Skills declare which `document_phase` values they operate on in "
        "their `manifest.yaml#lifecycle_phases`. They refuse cleanly on "
        "phases for which they do not have enough declared state to ground "
        "against. The phases listed under each row below are cumulative — "
        "skills invocable at `draft` are also invocable at `review`, "
        "`revision`, and `submission` (unless the skill explicitly narrows "
        "to a later phase).\n"
    )
    parts.append(_render_lifecycle_summary(manifests) + "\n")
    parts.append(
        "`MANUSCRIPT_STATE.yaml#document_phase` is set by `scriptorium:init` "
        "and is what the skills read.\n"
    )
    parts.append("## Author-side only\n")
    parts.append(
        "Skills whose `manifest.yaml` declares `positioning: author-side-only` "
        "refuse to run on a manuscript the user did not author. Editorial-side "
        "use violates ICMJE, NIH, and major-publisher peer-review policy.\n"
    )
    parts.append(_render_author_side_list(manifests) + "\n")
    parts.append("## Source of truth\n")
    parts.append(
        "This page is generated at docs-build time by "
        "`docs/scripts/preprocess.py` from every `skills/<name>/manifest.yaml`. "
        "To change what appears here, edit the manifest. Editing this file "
        "directly is wasted work — the next preprocess pass will overwrite it.\n"
    )
    return "\n".join(parts).rstrip() + "\n"


def process_skills_reference() -> int:
    """Regenerate the reference/skills.md page from skill manifests.

    Returns the count of manifests read.
    """
    manifests = _load_manifests()
    if not manifests:
        print("  (no skills/ manifests found; skipping)")
        return 0
    text = _generate_skills_page(manifests)
    SKILLS_OUT.parent.mkdir(parents=True, exist_ok=True)
    SKILLS_OUT.write_text(text, encoding="utf-8")
    try:
        rel = SKILLS_OUT.relative_to(DOCS_DIR)
    except ValueError:
        rel = SKILLS_OUT
    print(f"  wrote {rel}")
    return len(manifests)


# ---------------------------------------------------------------------------
# Sentinel-block substitution for partially-generated concept pages
# ---------------------------------------------------------------------------
#
# The concept pages under ``docs/src/content/docs/concepts/`` keep their
# hand-written prose under version control, but include generated
# manifest-driven blocks (the skill-by-stage table, the per-skill
# guidance-level behaviour list) that should never drift from
# ``skills/<name>/manifest.yaml``.
#
# Sentinel pattern:
#
#     <!-- GENERATED:<id>:start -->
#     ...content replaced on every preprocess pass...
#     <!-- GENERATED:<id>:end -->
#
# The block (including the markers) is replaced wholesale by the
# generator. If the page does not contain the sentinels, the preprocess
# step prints a warning and leaves the file untouched — a missing
# sentinel pair is a maintainer error, not a silent overwrite.


def _replace_sentinel_block(text: str, block_id: str, new_body: str) -> tuple[str, bool]:
    """Replace the body between ``GENERATED:<block_id>:start/end`` markers.

    Returns ``(new_text, replaced)``. ``replaced`` is ``False`` when the
    sentinel pair is absent — the caller should warn but not write.

    ``new_body`` is inserted between the markers exactly as supplied
    (with a single newline above and below). Leading/trailing blank
    lines in ``new_body`` are stripped to keep output deterministic.
    """
    start_marker = f"<!-- GENERATED:{block_id}:start -->"
    end_marker = f"<!-- GENERATED:{block_id}:end -->"
    # Match the start marker, any content (including zero bytes — supports
    # the bootstrap case where the page ships with just the two markers
    # back-to-back), then the end marker.
    pattern = re.compile(
        re.escape(start_marker) + r"(?:\n.*?)?\n" + re.escape(end_marker),
        re.DOTALL,
    )
    if not pattern.search(text):
        return text, False
    body = new_body.strip("\n")
    replacement = f"{start_marker}\n{body}\n{end_marker}"
    return pattern.sub(replacement, text), True


# ---------------------------------------------------------------------------
# Concept page: workflow-stage skill-by-stage table
# ---------------------------------------------------------------------------
#
# The "How this shows up in skills" table on
# ``concepts/workflow-stage.md`` is regenerated from each manifest's
# ``lifecycle_phases:`` declaration. Surrounding prose (Hayes framing,
# the notes on patterns at the bottom) stays hand-written.

# Columns rendered in the skill-by-stage table, in display order.
_WORKFLOW_STAGE_COLUMNS: list[str] = ["outline", "draft", "review", "revision", "submission"]


def _render_workflow_stage_table(manifests: list[dict[str, Any]]) -> str:
    """Render the skill-by-stage table for ``concepts/workflow-stage.md``.

    Each row is a shipped skill; columns are the five canonical
    pre-submission phases. A cell is ``yes`` if the manifest's
    ``lifecycle_phases`` declares that phase. The omission case (``—``)
    is the default; the further nuance ("refuses cleanly" vs "thin
    output") lives in surrounding prose and in each skill's
    ``manifest.yaml#refusal_behaviour`` once that field lands.
    """
    header_cells = ["Skill"] + [c.capitalize() for c in _WORKFLOW_STAGE_COLUMNS]
    rows: list[str] = [
        "| " + " | ".join(header_cells) + " |",
        "|" + "|".join(["---"] * len(header_cells)) + "|",
    ]
    sorted_manifests = sorted(manifests, key=lambda m: m["name"])
    for m in sorted_manifests:
        declared = set(m.get("lifecycle_phases") or [])
        name_cell = f"`{m['name']}`"
        phase_cells = ["yes" if phase in declared else "—" for phase in _WORKFLOW_STAGE_COLUMNS]
        rows.append("| " + " | ".join([name_cell, *phase_cells]) + " |")
    return "\n".join(rows)


def process_workflow_stage_concept() -> bool:
    """Replace the generated skill-by-stage table inside the concept page.

    Returns True if the table was written, False if the sentinel
    markers are missing or the page itself does not exist.
    """
    if not WORKFLOW_STAGE_OUT.is_file():
        print(f"  (no {WORKFLOW_STAGE_OUT.name}; skipping)")
        return False
    manifests = _load_manifests()
    if not manifests:
        print("  (no skills/ manifests found; skipping)")
        return False
    original = WORKFLOW_STAGE_OUT.read_text(encoding="utf-8")
    table = _render_workflow_stage_table(manifests)
    updated, replaced = _replace_sentinel_block(original, "workflow-stage-table", table)
    if not replaced:
        print(
            f"  ! {WORKFLOW_STAGE_OUT.name} is missing the "
            "GENERATED:workflow-stage-table sentinel block; skipping"
        )
        return False
    if updated != original:
        WORKFLOW_STAGE_OUT.write_text(updated, encoding="utf-8")
        try:
            rel = WORKFLOW_STAGE_OUT.relative_to(DOCS_DIR)
        except ValueError:
            rel = WORKFLOW_STAGE_OUT
        print(f"  wrote {rel}")
    else:
        print(f"  ({WORKFLOW_STAGE_OUT.name} table already up to date)")
    return True


# ---------------------------------------------------------------------------
# Concept page: per-skill guidance-level behaviour block
# ---------------------------------------------------------------------------
#
# The "How this shows up in skills" list on
# ``concepts/guidance-level.md`` is regenerated from each manifest's
# ``guidance_level_behavior:`` mapping. The mapping has exactly three
# string keys — ``terse``, ``standard``, ``full`` — each holding a
# one-or-two-sentence factual description of how that skill behaves
# at that level. Sourced from each ``skills/<name>/SKILL.md``;
# encoded in the manifest so the concept page cannot drift from
# what the skill actually does.

_GUIDANCE_LEVELS: list[str] = ["terse", "standard", "full"]


def _render_guidance_level_block(manifests: list[dict[str, Any]]) -> str:
    """Render the per-skill guidance-level behaviour list.

    Each shipped skill becomes a top-level bullet with three nested
    bullets — one per level. Skills missing the manifest field are
    surfaced inline so the omission is visible at docs-build time
    rather than silently absent from the rendered page.
    """
    lines: list[str] = []
    sorted_manifests = sorted(manifests, key=lambda m: m["name"])
    for m in sorted_manifests:
        name = m["name"]
        behavior = m.get("guidance_level_behavior") or {}
        if not isinstance(behavior, dict) or not all(k in behavior for k in _GUIDANCE_LEVELS):
            lines.append(
                f"- **`{name}`** — _missing `guidance_level_behavior` in `manifest.yaml`._"
            )
            continue
        lines.append(f"- **`{name}`**")
        for level in _GUIDANCE_LEVELS:
            description = _normalise_description(str(behavior[level]))
            lines.append(f"  - `{level}` — {description}")
    return "\n".join(lines)


def process_guidance_level_concept() -> bool:
    """Replace the generated per-skill block inside the concept page.

    Returns True if the block was written, False if the sentinel
    markers are missing or the page itself does not exist.
    """
    if not GUIDANCE_LEVEL_OUT.is_file():
        print(f"  (no {GUIDANCE_LEVEL_OUT.name}; skipping)")
        return False
    manifests = _load_manifests()
    if not manifests:
        print("  (no skills/ manifests found; skipping)")
        return False
    original = GUIDANCE_LEVEL_OUT.read_text(encoding="utf-8")
    block = _render_guidance_level_block(manifests)
    updated, replaced = _replace_sentinel_block(original, "guidance-level-skills", block)
    if not replaced:
        print(
            f"  ! {GUIDANCE_LEVEL_OUT.name} is missing the "
            "GENERATED:guidance-level-skills sentinel block; skipping"
        )
        return False
    if updated != original:
        GUIDANCE_LEVEL_OUT.write_text(updated, encoding="utf-8")
        try:
            rel = GUIDANCE_LEVEL_OUT.relative_to(DOCS_DIR)
        except ValueError:
            rel = GUIDANCE_LEVEL_OUT
        print(f"  wrote {rel}")
    else:
        print(f"  ({GUIDANCE_LEVEL_OUT.name} block already up to date)")
    return True


def main() -> None:
    print("Preprocessing scriptorium docs site")
    print(f"  source: {REPO_ROOT}")
    print(f"  output: {DOCS_DIR / 'src/content/docs'}")

    print("\n[1/5] Root docs")
    process_root_docs()

    print("\n[2/5] Knowledge layer")
    n_knowledge = process_knowledge()
    print(f"  processed {n_knowledge} markdown file(s)")

    print("\n[3/5] Skills reference page")
    n_skills = process_skills_reference()
    print(f"  generated reference page from {n_skills} manifest(s)")

    print("\n[4/5] Concept-page sentinel blocks")
    process_workflow_stage_concept()
    process_guidance_level_concept()

    print("\n[5/5] Quarto sources")
    n_qmd = process_qmd()
    if n_qmd == 0:
        print("  (no .qmd files under docs/qmd/; skipping)")
    else:
        print(f"  rendered {n_qmd} .qmd file(s)")

    print("\nDone.")


if __name__ == "__main__":
    main()
