"""Tests for the Claude Code plugin marketplace manifest.

`.claude-plugin/marketplace.json` is what lets users install scriptorium
with `/plugin marketplace add seandavi/scriptorium` followed by
`/plugin install scriptorium@scriptorium`. These tests check the manifest
parses, declares the required marketplace fields, and that each declared
plugin's source resolves to a real plugin directory in the repo.

The schema reference lives at
https://code.claude.com/docs/en/plugin-marketplaces.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE_FILE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


@pytest.fixture(scope="module")
def marketplace() -> dict:
    assert MARKETPLACE_FILE.is_file(), f"missing {MARKETPLACE_FILE}"
    return json.loads(MARKETPLACE_FILE.read_text(encoding="utf-8"))


def test_marketplace_has_required_fields(marketplace: dict) -> None:
    for field in ("name", "owner", "plugins"):
        assert field in marketplace, f"marketplace.json missing required field: {field}"


def test_marketplace_name_is_kebab_case(marketplace: dict) -> None:
    name = marketplace["name"]
    assert isinstance(name, str)
    assert KEBAB_RE.match(name), f"marketplace name {name!r} is not kebab-case"


def test_owner_has_name(marketplace: dict) -> None:
    owner = marketplace["owner"]
    assert isinstance(owner, dict)
    assert owner.get("name"), "owner.name is required"


def test_plugins_is_nonempty_list(marketplace: dict) -> None:
    plugins = marketplace["plugins"]
    assert isinstance(plugins, list)
    assert plugins, "marketplace declares no plugins"


def test_plugin_names_are_unique_and_kebab_case(marketplace: dict) -> None:
    names = [p["name"] for p in marketplace["plugins"]]
    assert len(names) == len(set(names)), f"duplicate plugin names: {names}"
    for name in names:
        assert KEBAB_RE.match(name), f"plugin name {name!r} is not kebab-case"


def test_each_plugin_has_name_and_source(marketplace: dict) -> None:
    for plugin in marketplace["plugins"]:
        assert plugin.get("name"), f"plugin missing name: {plugin}"
        assert "source" in plugin, f"plugin {plugin.get('name')!r} missing source"


def test_relative_path_sources_resolve_to_a_plugin(marketplace: dict) -> None:
    """Each relative-path source must point to a directory with plugin.json.

    Marketplace-relative paths are resolved against the marketplace root
    (the directory containing `.claude-plugin/`), not the manifest file's
    directory. A valid plugin directory contains
    `.claude-plugin/plugin.json`.
    """
    for plugin in marketplace["plugins"]:
        source = plugin["source"]
        if not isinstance(source, str):
            continue
        assert source.startswith("./"), (
            f"plugin {plugin['name']!r} relative source {source!r} must start with './'"
        )
        assert ".." not in source, f"plugin {plugin['name']!r} source must not contain '..'"
        plugin_dir = (REPO_ROOT / source).resolve()
        assert plugin_dir.is_dir(), (
            f"plugin {plugin['name']!r} source {source!r} does not resolve to a directory"
        )
        manifest = plugin_dir / ".claude-plugin" / "plugin.json"
        assert manifest.is_file(), (
            f"plugin {plugin['name']!r} source has no .claude-plugin/plugin.json"
        )


def test_marketplace_name_not_reserved(marketplace: dict) -> None:
    """Reserved names are blocked by the official marketplace registry."""
    reserved = {
        "claude-code-marketplace",
        "claude-code-plugins",
        "claude-plugins-official",
        "anthropic-marketplace",
        "anthropic-plugins",
        "agent-skills",
        "anthropic-agent-skills",
        "knowledge-work-plugins",
        "life-sciences",
    }
    assert marketplace["name"] not in reserved, (
        f"marketplace name {marketplace['name']!r} is reserved"
    )


def test_plugin_json_repository_is_string() -> None:
    """Claude Code's plugin manifest schema requires `repository` to be a
    string URL, not an npm-style `{type, url}` object. Marketplace installs
    fail validation if this drifts."""
    plugin_json = json.loads(
        (REPO_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    if "repository" in plugin_json:
        assert isinstance(plugin_json["repository"], str), (
            f"plugin.json repository must be a string URL, got "
            f"{type(plugin_json['repository']).__name__}"
        )


def test_plugin_version_matches_plugin_json_when_both_set(marketplace: dict) -> None:
    """Drift between plugin.json and marketplace entry versions silently
    breaks updates — plugin.json wins, so the marketplace entry can mask
    a published bump. Catch the mismatch in CI."""
    plugin_json = json.loads(
        (REPO_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    pj_version = plugin_json.get("version")
    for plugin in marketplace["plugins"]:
        if plugin.get("source") == "./" and "version" in plugin:
            assert plugin["version"] == pj_version, (
                f"marketplace plugin {plugin['name']!r} version "
                f"{plugin['version']!r} drifts from plugin.json version "
                f"{pj_version!r}"
            )
