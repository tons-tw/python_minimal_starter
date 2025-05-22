# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a minimal Python starter template using UV package manager. The project follows modern Python standards with a clean structure designed for rapid prototyping.

## Development Commands

### Environment Setup

```bash
uv sync                    # Install all dependencies
uv sync --no-dev          # Install production dependencies only
```

### Running the Application

```bash
uv run python src/main.py  # Run the main application
```

### Code Quality

```bash
uv run pyproject-fmt .    # Format pyproject.toml
uv run ruff format        # Format code
uv run ruff check         # Run linter
uv run ruff check --fix   # Auto-fix linting issues
```

### Virtual Environment (Optional)

```bash
source .venv/bin/activate  # Activate venv for direct shell access
deactivate                 # Deactivate venv
```

### Dependency Management

```bash
uv add <package>          # Add production dependency
uv add <package> --dev    # Add development dependency
uv sync --upgrade         # Upgrade all dependencies
```

## Project Structure

- `src/main.py`: Main entry point
- `pyproject.toml`: Project configuration and dependencies
- `uv.lock`: Dependency lock file (auto-generated, do not edit manually)

## Code Style

- **Line length**: 80 characters
- **Indentation**: 2 spaces
- **Import sorting**: Enabled (Ruff isort)
- **Python version**: 3.13.*

## Architecture Notes

The project uses UV (by Astral) as a modern, fast alternative to pip/poetry. UV handles virtual environment creation, dependency resolution, and package installation. The `.venv/` directory contains the virtual environment and is managed automatically by UV.

When adding new functionality:

1. Keep the minimal structure - avoid over-engineering
2. Add production dependencies sparingly
3. Use Ruff for all formatting and linting needs
4. The main application logic starts in `src/main.py`
