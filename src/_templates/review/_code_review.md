# Code Review Guidelines

{% block action %}
{% endblock %}

{% block scope %}
**Scope rule (STRICT):**
- You may ONLY modify reviewed file (`${fileBasename}`).
- You may READ other files (configs, imports, interfaces) for context.
- If fixing properly requires edits elsewhere (tests, shared utils), propose a plan + minimal diff, but do not edit other files unless user explicitly allows it.
{% endblock %}


# Review Requirements
Cover:
- Security issues & attack vectors
- Correctness vs specification/intent if specs are provided
- Functional bugs & edge cases
- Formatting/style per project conventions (PEP8, etc)
- Edge cases & correctness risks
- Performance tradeoffs
- Maintainability (SOLID/DRY), readability
- Error handling robustness
- Resource management leaks
- Documentation (Google-style docstrings for public APIs)
- Tests: suggest cases (don’t implement outside file)
- Python code smells & anti-patterns
- Dependency bloat & config hygiene

---

# Step 1 — Context + Discovery (do this first)
1. Read `${fileBasename}` fully.
2. Identify internal dependencies and external imports for context.
3. Identify project tooling/config by searching for:
   - `pyproject.toml`, `setup.cfg`, `tox.ini`, `.flake8`, `mypy.ini`, `pylintrc`, `.pylintrc`
   - tool sections like `[tool.black]`, `[tool.ruff]`, `[tool.flake8]`, `[tool.mypy]`, `[tool.pylint]`
4. Detect whether these tools are used by checking (best effort):
   - `pyproject.toml` dependencies / `requirements*.txt` / `poetry.lock` / `uv.lock`
   - CI configs
5. If a tool is NOT present in the project config/deps, do NOT force it.

---

{% block activities %}

{% endblock %}
---


# Final Step — Fix Loop (apply fixes inside the file, then re-run)
Iterate:
1) Prioritize fixes:
   - **Critical**: security, data corruption, crashes, major typing bugs
   - **Major**: correctness edge cases, significant maintainability issues
   - **Minor**: style, formatting, docstrings, naming
2) Apply safe, high-confidence fixes directly using `edit`.
   - Keep diffs minimal and targeted.
   - Don’t refactor for “beauty” unless it removes real risk/complexity.
3) Re-run the same checks to verify improvement.
4) Stop when:
   - checks are clean, OR
   - remaining issues require product decisions / behavior changes (explain and propose options).

---

# Output Format (STRICT)
## Tooling Results
- Commands run
- Key findings (Critical/Major/Minor)
- What you couldn’t run (why)

## Patch Summary (file-only)
- What you changed
- Re-run results after patch

## Review Notes
### Critical
### Major
### Minor
### Suggestions
### Testing ideas
### Learning (teach juniors)


## Follow-ups
- Only questions needed for risky/ambiguous behavior changes
