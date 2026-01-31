# AGENTS.md (docs/)

This folder contains the project documentation site built with **MkDocs**, **mkdocs-material**, and **mkdocstrings** (API reference rendered from Python docstrings).  
If you’re an agent making changes here, optimize for **clarity, consistency, and zero broken builds**.


{% include '/docs/docs_diataxis_style.md' %}

{% include '/docs/docs_structure_diataxis.md' %}

{% include '/docs/docs_mkdocs_conventions.md' %}

---

## When adding a new feature to the codebase

Minimum docs expectation:
1. Add or update a **How-to** or **Tutorial** (depending on complexity and scope of changes).
2. Ensure that the **API Reference** is updated via docstrings.
3. If it affects certain concepts, add or update **Explanation** docs.
4. If it affects installation or setup, update **Installation** docs.
5. Add a short note to `docs/index.md` or a “Quickstart” section if it changes onboarding.

---

Don’t invent behavior. If you can’t confirm from code/tests, say so or leave it out.
