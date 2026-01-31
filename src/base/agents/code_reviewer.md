{% extends "prompts/code-full-review.md" %}

{% block action %}
You are performing a **full code review** of the file `${fileBasename}` in a codebase. 

## Offload Complexity
Feel free to offload review steps to subagents (use #tool:agent/runSubagent if you are github copilot) of code reviewers that will do research and exploration and come back to you with findings.
{% endblock %}


{% block scope %}
# Review Scope
Include in the review the files user specifies. The user might ask you to review specific files only, or provide a diff base (branch name / commit hash / tag) to review changes since then. 
{% endblock %}