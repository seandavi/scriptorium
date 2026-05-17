"""scriptorium: an agentic scriptorium for scholarly writing.

This package ships:

* A CLI (:mod:`scriptorium.cli`) for installing skills into Claude Code,
  validating ``MANUSCRIPT_STATE.yaml``, and generating prompt packs for
  platform-neutral use.
* The skill bundle itself, shipped as package data and copied into
  ``~/.claude/plugins/scriptorium/`` by ``scriptorium install``.
* A JSON Schema for ``MANUSCRIPT_STATE.yaml`` used by the validator.

See ``DESIGN.md`` for the design rationale and ``INSTALL.md`` for install
paths beyond the Claude Code default.
"""

from __future__ import annotations

__version__ = "0.1.0.dev0"
__all__ = ["__version__"]
