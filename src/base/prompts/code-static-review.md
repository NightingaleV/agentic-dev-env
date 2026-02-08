{% extends "agents/reviewer.md" %}


{% block requirements %}
**Code Quality Assessment**:

- Review code for adherence to established patterns and conventions
- Check for proper error handling, type safety, and defensive programming
- Evaluate code organization, naming conventions, and maintainability. 
- Assess test coverage and quality of test implementations
- Look for potential security vulnerabilities or performance issues
- Look for Python code smells & anti-patterns
- Look for meaningful naming and clarity
{% endblock %}


{% block review_steps %}
# Step 2 — Run Checks (best effort, based on what’s used)

Use tool to run commands for checks. Prefer project runner (uv or poetry) if user utilises that. (`uv run <command>` or `poetry run <command>`).
{% endblock %}



{% block outcome %}
# Final Step — Fix Loop (apply fixes inside the file, then re-run)

Only apply fixes to the reviewed file/s (`${fileBasename}`). Do not modify other files (tests, shared utils) without explicit user approval, even if it would make the fix cleaner. If a proper fix requires changes outside the file, propose a plan and minimal diff for those changes, but do not implement them without approval.

Iterate:
1) Check outputs of static analysis and consider what's relevant warnings/errors for files in review scope. Ignore irrelevant findings and false positives or for files outside of review scope.
2) Apply safe, high-confidence fixes directly using `edit`.
   - Keep diffs minimal and targeted.
   - Don’t refactor for “beauty” unless it removes real risk/complexity.
3) Re-run the same checks to verify improvement.
4) Stop when:
   - checks are clean, OR
   - remaining issues require product decisions / behavior changes (explain and propose options). Do not make behavior changes without explicit approval from the user. Do not make big refactors that require extensive changes without user approval.
   - If you identify behavior changes that require product decisions, clearly explain the change, its implications, and propose options for how to proceed. Do not make behavior changes without explicit approval from the user.
{% endblock %}