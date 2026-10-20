# Scriptorium repo tasks. The docs site has its own justfile under docs/.

set shell := ["bash", "-uc"]

# Default: list available recipes.
default:
    @just --list

# Copy canonical schemas/, knowledge/ and templates/ files into skills/*/assets/.
sync-skill-assets:
    uv run python scripts/sync_skill_assets.py
