"""Tests for ``scripts/sync_skill_assets.py``.

``init``, ``explain`` and ``tour`` carry copies of repo files under
``skills/<name>/assets/`` so they work when installed alone via
``npx skills add``. These tests fail when a copy drifts from its
canonical source; the fix is ``just sync-skill-assets``.
"""

from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path
from types import ModuleType

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "sync_skill_assets.py"


def _load_script() -> ModuleType:
    spec = importlib.util.spec_from_file_location("sync_skill_assets", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sync_skill_assets = _load_script()


def test_declared_skills_and_sources_exist() -> None:
    for skill, rels in sync_skill_assets.SKILL_ASSETS.items():
        assert (REPO_ROOT / "skills" / skill / "SKILL.md").is_file(), skill
        for rel in rels:
            assert (REPO_ROOT / rel).is_file(), f"{skill}: missing canonical source {rel}"


def test_bundled_assets_match_canonical_sources() -> None:
    stale = ", ".join(str(p.relative_to(REPO_ROOT)) for p in sync_skill_assets.stale_assets())
    assert not stale, f"bundled skill assets out of sync ({stale}); run `just sync-skill-assets`"


def test_no_undeclared_bundled_assets() -> None:
    extra = ", ".join(str(p.relative_to(REPO_ROOT)) for p in sync_skill_assets.undeclared_assets())
    assert not extra, f"files under skills/*/assets/ not in SKILL_ASSETS: {extra}"


@pytest.fixture
def repo_copy(tmp_path: Path) -> Path:
    """A minimal repo tree holding just the declared sources and skill dirs."""
    for skill, rels in sync_skill_assets.SKILL_ASSETS.items():
        (tmp_path / "skills" / skill).mkdir(parents=True, exist_ok=True)
        for rel in rels:
            dest = tmp_path / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO_ROOT / rel, dest)
    return tmp_path


def test_sync_repairs_drift_and_removes_undeclared(repo_copy: Path) -> None:
    sync_skill_assets.sync(repo_copy)
    assert sync_skill_assets.stale_assets(repo_copy) == []

    drifted = repo_copy / "skills" / "init" / "assets" / "schemas" / "manuscript-state.schema.json"
    drifted.write_text("{}\n", encoding="utf-8")
    orphan = repo_copy / "skills" / "tour" / "assets" / "orphan.md"
    orphan.write_text("stale\n", encoding="utf-8")

    assert sync_skill_assets.stale_assets(repo_copy) == [drifted]
    assert sync_skill_assets.undeclared_assets(repo_copy) == [orphan]

    changed = sync_skill_assets.sync(repo_copy)

    assert set(changed) == {drifted, orphan}
    assert not orphan.exists()
    assert sync_skill_assets.stale_assets(repo_copy) == []
    assert sync_skill_assets.undeclared_assets(repo_copy) == []
