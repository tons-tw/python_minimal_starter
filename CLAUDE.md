# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minimal Python 3.13 starter template using `uv` as the package manager. Entry point is `src/main.py`.

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

# Test
uv run pytest src/

# Test with coverage
uv run pytest src/ --cov=src

# Add a dependency
uv add <package>        # runtime
uv add --dev <package>  # dev only
```

## Code Style

- **2-space indentation** (not 4) — configured in ruff and .vscode/settings.json
- **80-character line length**
- **LF line endings**
- Ruff handles formatting and linting (with `I` import-sorting rule enabled)
- `pyproject-fmt` formats `pyproject.toml` (also 2-space indent, 80-col width)

## Testing

- Test files use `*_test.py` naming and live next to the source file (no separate `tests/` folder)
- Example: `src/add.py` → `src/add_test.py`
