{% extends "prompts/code-full-review.md" %}

{% block action %}
You are performing a **full code review** of the files specified by the user/agent.
{% endblock %}


{% block scope %}
# Review Scope
Include in the review the files user/agent specifies. The user might ask you to review specific files only, or provide a diff base (branch name / commit hash / tag) to review changes since then. You can read and see other files (dependencies, docs) for context, but only modify the specified files.
{% endblock %}