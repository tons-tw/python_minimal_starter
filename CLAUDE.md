# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minimal Python 3.14 starter template using `uv` as the package manager. Entry point is `src/main.py`.

## Development Principles

Trade-off priority, from highest to lowest:

1. **Readability first** — code is read more than written. Optimize for clarity and maintainability. Consider architecture and performance only after readability is solid.
2. **Simple beats clever** (Occam's razor) — prefer the simplest working solution. Reach for complexity only after proving a simpler approach is insufficient.
3. **Make it work, then make it good** (lean execution) — ship a minimal working version first, then iterate. Don't stall on premature polish.

### Naming
- Simple and memorable, but not over-abbreviated.
- Prefer `fetch_user` over both `f` and `retrieve_user_record_from_database`.

### Comments
- Default: no comment. Good names already explain the *what*.
- Required: when logic is non-obvious or complex. Explain the *why* — hidden constraints, non-intuitive invariants, workarounds — not the *what*.

## Commands

```sh
# Install/sync dependencies
uv sync

# Run the application
uv run src/main.py

# Format code (run in this order)
uv run pyproject-fmt .
uv run ruff format
uv run ruff check --fix

# Lint
uv run ruff check

# Test (coverage is on via pytest addopts)
uv run pytest

# Add a dependency
uv add <package>        # runtime
uv add --dev <package>  # dev only
```

## Code Style

- **2-space indentation** (not 4) — enforced via ruff, `.editorconfig`, and `.vscode/settings.json`
- **80-character line length**
- **LF line endings**
- Ruff handles formatting and linting. Enabled rules: `B`, `C4`, `I`, `PIE`, `PT`, `RET`, `RUF`, `SIM`, `TCH`, `UP` (see `pyproject.toml`)
- `pyproject-fmt` formats `pyproject.toml`

## Testing

- Test files use `*_test.py` naming and live next to the source file (no separate `tests/` folder)
- Example: `src/fib.py` → `src/fib_test.py`
- `src/main.py` is excluded from coverage via `[tool.coverage] run.omit` (entry points aren't measured)
