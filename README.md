# tons-tw/python-minimal-starter

> THIS IS THE WAY!

Minimal Python 3.14 starter template with `uv`, `ruff`, and `pytest`.

## Getting Started
```sh
# to install uv (see docs for other platforms: https://docs.astral.sh/uv/getting-started/installation/)
curl -LsSf https://astral.sh/uv/install.sh | sh

# to sync environment (uv will fetch Python 3.14 automatically)
uv sync

# to start the application
uv run src/main.py
```

## Common Scripts
```sh
# to format the code
uv run pyproject-fmt .
uv run ruff format
uv run ruff check --fix

# to lint the code
uv run ruff check

# to run tests (coverage is on via pytest addopts)
uv run pytest src/

# to add a dependency
uv add <package>         # runtime
uv add --dev <package>   # dev only

# to upgrade dependencies
uv sync --upgrade

# to sync environment for production (no dev deps)
uv sync --no-dev
```
