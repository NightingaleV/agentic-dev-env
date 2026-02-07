{% extends "review/_code_review.md" %}

{% block objective %}
Review the changes made in project files as per the diff provided. For each changed file, perform a comprehensive code review focusing on correctness, style, performance, security, and test coverage. Provide constructive feedback and suggest improvements where necessary.
{% endblock %}

{% block scope %}
# Step 0 — Collect Change Set

## Inputs
- Optional: user-provided diff base (branch name / commit hash / tag), called `DIFF_BASE`.
- Optional: user-provided paths, called `PATHS` (otherwise review repo-wide).

## Strategy (priority order)
1) If `DIFF_BASE` is provided: review changes from `DIFF_BASE` to current HEAD (plus include any local staged + unstaged deltas on top, if present).
2) Else (default): review staged changes first, then unstaged changes, then untracked files.

Commands (always run):
- `git status --porcelain=v1 -uall`

If DIFF_BASE is provided:
- `git --no-pager fetch --all --prune`
- `BASE=$(git --no-pager merge-base ${DIFF_BASE} HEAD)`
- `git --no-pager diff $BASE..HEAD -- ${PATHS:-.}`

Then always include local WIP on top (if any):
- `git --no-pager diff --cached -- ${PATHS:-.}`   # staged
- `git --no-pager diff -- ${PATHS:-.}`           # unstaged
- `git ls-files --others --exclude-standard -- ${PATHS:-.}`  # untracked (no pager anyway)

If DIFF_BASE is NOT provided:
- `git --no-pager diff --cached -- ${PATHS:-.}`  # staged
- `git --no-pager diff -- ${PATHS:-.}`           # unstaged
- `git ls-files --others --exclude-standard -- ${PATHS:-.}`  # untracked

{% endblock %}
