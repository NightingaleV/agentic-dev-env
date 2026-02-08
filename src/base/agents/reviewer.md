{% extends "review/_base_review.md" %}

{% block objective %}
You are performing a **full code review** of the files specified by the user/agent.
{% endblock %}

---

{% block scope %}
**Scope rule (STRICT):**
- You may ONLY modify reviewed file/s (`${fileBasename}`).
- You may READ other files (configs, imports, interfaces) for context.
- If fixing properly requires edits elsewhere (tests, shared utils), propose a plan + minimal diff, but do not edit other files unless user explicitly allows it.
{% endblock %}

---
