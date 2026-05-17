#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Preprocess source markdown + Quarto into the Astro/Starlight content tree.

Four things happen:

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

DOCS_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = DOCS_DIR.parent
KNOWLEDGE_SRC = REPO_ROOT / "knowledge"
DESIGN_SRC = REPO_ROOT / "DESIGN.md"
ROADMAP_SRC = REPO_ROOT / "docs" / "roadmap.md"

CONTENT_ROOT = DOCS_DIR / "src" / "content" / "docs"
KNOWLEDGE_OUT = CONTENT_ROOT / "concepts" / "knowledge"
DESIGN_OUT = CONTENT_ROOT / "concepts" / "design.md"
ROADMAP_OUT = CONTENT_ROOT / "roadmap.md"
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
                "The agentic-scriptorium thesis, design philosophy, and "
                "the shared-state contract."
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


def main() -> None:
    print("Preprocessing scriptorium docs site")
    print(f"  source: {REPO_ROOT}")
    print(f"  output: {DOCS_DIR / 'src/content/docs'}")

    print("\n[1/3] Root docs")
    process_root_docs()

    print("\n[2/3] Knowledge layer")
    n_knowledge = process_knowledge()
    print(f"  processed {n_knowledge} markdown file(s)")

    print("\n[3/3] Quarto sources")
    n_qmd = process_qmd()
    if n_qmd == 0:
        print("  (no .qmd files under docs/qmd/; skipping)")
    else:
        print(f"  rendered {n_qmd} .qmd file(s)")

    print("\nDone.")


if __name__ == "__main__":
    main()
