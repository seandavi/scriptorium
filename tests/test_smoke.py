"""Smoke tests to verify the package imports and exposes its public API.

These are intentionally minimal — real test coverage lands with the CLI
and skill implementations in subsequent PRs.
"""

from __future__ import annotations


def test_package_imports() -> None:
    """The top-level package imports without error."""
    import scriptorium

    assert scriptorium.__version__


def test_version_is_string() -> None:
    """The exported __version__ is a non-empty string."""
    from scriptorium import __version__

    assert isinstance(__version__, str)
    assert __version__
