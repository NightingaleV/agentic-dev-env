{% extends "review/_code_review.md" %}

{% block activities %}
# Step 2 — Run Checks (best effort, based on what’s used)
Use tool to run commands for checks. Prefer project runner (uv or poetry) if user utilises that. (`uv run <command>` or `poetry run <command>`):
- If `pre-commit` exists: run `pre-commit run --files ${fileBasename}` (or nearest equivalent).
- If `ruff` exists: run `ruff check ${fileBasename}` and/or `ruff format --check ${fileBasename}`.
- If `black` exists: run `black --check ${fileBasename}`.
- If `flake8` exists: run `flake8 ${fileBasename}`.
- If `pylint` exists: run `pylint ${fileBasename}` (or module path if needed).
- If `mypy` exists: run `mypy ${fileBasename}` (or project invocation per config).
- If `pytest`/`unittest` exists: run tests covering `${fileBasename}` (e.g. `pytest tests/ --cov=${fileBasename}`).

If a command fails due to environment/tool not installed:
- Note it clearly.
- Fall back to config inspection + static reasoning.
- Do NOT hallucinate tool output.

{% endblock %}