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

# Step 3 — Understand Functionality Before Fixing

A code review is not just style-checking. Your first job is to understand what the code is **intended** to do and how it behaves in practice. Offload this task to subagents if possible.

### 3.1 Establish intent
- Infer expected behavior from:
  - function/class names, docstrings, type hints
  - call sites and usage patterns
  - tests (if present) and test naming
  - configs / CLI / API contracts
- If intent is ambiguous, **call it out explicitly** and propose the most likely interpretation(s) before making changes.

### 3.2 Validate behavior with a sandbox (optional)
If the runtime behavior is unclear, you may create a **temporary sandbox** to explore it.

**Hard rules**
- **Do not modify** `${fileBasename}` (or any production files) during this step.
- Sandbox is for **observation only**: understand behavior, edge cases, and failure modes.
- Keep changes isolated and reversible.

**Sandbox guidelines**
- Create a temporary file (e.g., `tmp_review_<component_name>.py`) that runs in the same project virtual environment.
- You may:
  - import and execute functions/classes from `${fileBasename}`
  - use small, representative inputs (can be mocked)
  - mock or stub external dependencies (I/O, network, DB) when needed
  - print outputs, logs, and debug info (keep it minimal and relevant)
  - probe edge cases (nulls, empty inputs, invalid types, boundary values)
- Avoid:
  - writing to real databases/services
  - mutating real files or stateful resources
  - relying on long-running or flaky external systems

### 3.3 Capture findings
Before proposing fixes, write a short summary:
- “What this code does” (observed behavior)
- “What it probably should do” (intended behavior)
- key assumptions + uncertainties
- notable edge cases or surprising behavior

### 3.4 Cleanup
Delete the sandbox file after you’re done exploring, before entering the fix loop.

{% endblock %}
