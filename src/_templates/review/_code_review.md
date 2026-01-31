{%- block frontmatter -%}{%- endblock frontmatter -%}
{% block action %}
Review the code or files that agent/user specifies. Use a structured approach to ensure thoroughness and accuracy.
{% endblock %}

{% block scope %}
**Scope rule (STRICT):**
- You may ONLY modify reviewed file/s (`${fileBasename}`).
- You may READ other files (configs, imports, interfaces) for context.
- If fixing properly requires edits elsewhere (tests, shared utils), propose a plan + minimal diff, but do not edit other files unless user explicitly allows it.
{% endblock %}


# Review Requirements
When reviewing completed work, you will:

1. **Plan Alignment Analysis** - If plan exists (can be provided by user or inferred from context):
   - Compare the implementation against the original planning document or step description
   - Identify any deviations from the planned approach, architecture, or requirements
   - Assess whether deviations are justified improvements or problematic departures
   - Verify that all planned functionality has been implemented

2. **Code Quality Assessment**:
   - Review code for adherence to established patterns and conventions
   - Check for proper error handling, type safety, and defensive programming
   - Evaluate code organization, naming conventions, and maintainability. 
   - Assess test coverage and quality of test implementations
   - Look for potential security vulnerabilities or performance issues
   - Look for Python code smells & anti-patterns
   - Look for meaningful naming and clarity

3. **Architecture and Design Review**:
   - Ensure the implementation follows SOLID principles and established architectural patterns
   - Check for proper separation of concerns and loose coupling
   - Readability over complexity and abstraction.
   - Verify that the code integrates well with existing systems
   - Assess scalability and extensibility considerations

4. **Documentation and Standards**:
   - Verify that code includes appropriate comments and documentation
   - Check that file headers, function documentation, and inline comments are present and accurate
   - Ensure adherence to project-specific coding standards and conventions

5. **Issue Identification and Recommendations**:
   - Clearly categorize issues as: Critical (must fix), Important (should fix), or Suggestions (nice to have)
   - For each issue, provide specific examples and actionable recommendations
   - When you identify plan deviations, explain whether they're problematic or beneficial
   - Suggest specific improvements with code examples when helpful

6. **Communication Protocol**:
   - If you find significant deviations from the plan, ask the coding agent to review and confirm the changes
   - If you identify issues with the original plan itself, recommend plan updates
   - For implementation problems, provide clear guidance on fixes needed
   - Always acknowledge what was done well before highlighting issues


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
