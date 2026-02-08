## Code Review Checks
Use tool to run commands for checks. Prefer project runner (uv or poetry) if user utilises that. (`uv run <command>` or `poetry run <command>`):

- If `pre-commit` exists: run `pre-commit run --files ${fileBasename}` (or nearest equivalent).
- If `ruff` exists: run `ruff check ${fileBasename}` and/or `ruff format --check ${fileBasename}`.
- If `black` exists: run `black --check ${fileBasename}`.
- If `flake8` exists: run `flake8 ${fileBasename}`.
- If `pylint` exists: run `pylint ${fileBasename}` (or module path if needed).
- If `mypy` exists: run `mypy ${fileBasename}` (or project invocation per config).
- If `pytest`/`unittest` exists: run tests covering `${fileBasename}` (e.g. `pytest tests/ --cov=${fileBasename}`).
- If `mkdocs` exists: run `mkdocs build` to check for doc issues, ignoring warnings about missing site_url or similar non-blocking config issues.

If a command fails due to environment/tool not installed:
- Note it clearly.
- Fall back to config inspection + static reasoning.
- Do NOT hallucinate tool output.


### Cheatsheet for common commands:
```bash
# Linting with pylint
uv run pylint $fileName

# Linting with flake8
uv run flake8 $fileName

# Type checking
uv run mypy $fileName

# Additional security scan
uv run bandit -r $fileName -ll

# Check for secrets
uv run detect-secrets scan
```

### Documentation
```bash
# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build
```