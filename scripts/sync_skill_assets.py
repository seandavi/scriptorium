#!/usr/bin/env python3
"""Copy canonical repo files into the skills that need them standalone.

``npx skills add seandavi/scriptorium`` installs each skill's directory
and nothing else, so a skill that reads ``schemas/`` or ``knowledge/``
would find nothing. Each file listed in ``SKILL_ASSETS`` is copied to
``skills/<name>/assets/<same repo-relative path>``; the canonical file
stays where it is and is the only copy anyone edits.

Run ``just sync-skill-assets`` after editing a canonical file, or
``--check`` to list stale copies without writing (exit 1 if any).
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SKILL_ASSETS: dict[str, tuple[str, ...]] = {
    "init": ("schemas/manuscript-state.schema.json",),
    "explain": (
        ".claude-plugin/plugin.json",
        "schemas/manuscript-state.schema.json",
        "knowledge/README.md",
        "knowledge/conventions/guidance-level.md",
        "knowledge/conventions/declared-work-scope.md",
    ),
    "tour": (
        "knowledge/README.md",
        "templates/MANUSCRIPT_STATE.example.yaml",
    ),
}


def asset_pairs(repo_root: Path = REPO_ROOT) -> list[tuple[Path, Path]]:
    """Return ``(canonical source, bundled copy)`` for every declared asset."""
    return [
        (repo_root / rel, repo_root / "skills" / skill / "assets" / rel)
        for skill, rels in SKILL_ASSETS.items()
        for rel in rels
    ]


def stale_assets(repo_root: Path = REPO_ROOT) -> list[Path]:
    """Bundled copies that are missing or differ from their source."""
    return [
        dest
        for src, dest in asset_pairs(repo_root)
        if not dest.is_file() or not filecmp.cmp(src, dest, shallow=False)
    ]


def undeclared_assets(repo_root: Path = REPO_ROOT) -> list[Path]:
    """Files under ``skills/*/assets/`` that ``SKILL_ASSETS`` does not list."""
    declared = {dest for _, dest in asset_pairs(repo_root)}
    return sorted(
        path
        for path in (repo_root / "skills").glob("*/assets/**/*")
        if path.is_file() and path not in declared
    )


def sync(repo_root: Path = REPO_ROOT) -> list[Path]:
    """Copy stale assets into place; remove undeclared ones. Return changed paths."""
    changed: list[Path] = []
    for src, dest in asset_pairs(repo_root):
        if dest.is_file() and filecmp.cmp(src, dest, shallow=False):
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
        changed.append(dest)
    for path in undeclared_assets(repo_root):
        path.unlink()
        changed.append(path)
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="report stale or undeclared copies without writing; exit 1 if any",
    )
    args = parser.parse_args(argv)

    if args.check:
        problems = stale_assets() + undeclared_assets()
        for path in problems:
            print(f"out of sync: {path.relative_to(REPO_ROOT)}")
        return 1 if problems else 0

    for path in sync():
        print(f"updated: {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
