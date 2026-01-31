{% extends "agents/reviewer.md" %}
{%- block frontmatter -%}
---
description: Review code regarding completed project steps against original plans and coding standards.
mode: subagent
temperature: 0.2
tools:
  write: true
  edit: true
  bash: true
---
{%- endblock frontmatter -%}