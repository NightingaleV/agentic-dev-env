---
name: document-python-component
description: Toolkit for documenting python components (modules, classes, functions) using docstrings and further rendered by mkdocstrings in docs website.
metadata:
  short-description: Generate docstring documentation for python components.
---

## What this skill does
When editing or creating Python code, write **high-quality Google-style docstrings** for:
- Modules (top-of-file docstring)
- Public classes
- Public functions
- Public methods and properties


## When to Use This Skill
- Use this skill when you need to generate or enhance documentation for a Python component.
- Creating/Updating docstrings inside the python code.
- Add or modify a public module/class/function/method/property
- See missing, vague, outdated, or inconsistent docstrings
- Prepare code for API docs (mkdocstrings pages)
- Introduce non-obvious behavior, edge cases, or side effects in components


## Core Capabilities

---

## Output requirements
For every **public** object:
1. Add/upgrade docstring in **Google style**
2. Keep descriptions **clear, concrete, and non-marketing**
3. Do not mention parameter types if type hints exist

---

## Google docstring structure (standard)
Use these sections as needed (only include what applies):
- Short summary (1 line)
- Optional extended summary (1–3 short paragraphs)
- Args:
- Returns:
- Raises:
- Attributes: (for classes, when useful)
- Examples:
- Notes: (optional)
- Warning: (rare)

---

## Formatting rules
- Triple double quotes: `"""Docstring..."""`
- Summary line ends with a period.
- Wrap lines roughly ~88–100 chars when reasonable (don’t force ugly wrapping).
- Prefer **imperative/active voice** (“Fetch prices…”, “Validate payload…”).
- Examples must be **copy-pastable** (no pseudocode).

---

## Docstring rules
### 1) Keep it user-facing
Explain what it does, what matters, and any side effects (I/O, network, mutation, caching).


### 2) Don’t repeat types in docstrings

### ✅ Do
```py
Args:
  ticker: Stock ticker symbol (e.g., "AAPL").
  period: Time period to fetch. Defaults to "1y".

Returns:
  A DataFrame containing historical stock prices.

```

### ❌ Don't
```py 
Args:
  ticker (str): ...
  period (str, optional): ...

Returns:
  pd.DataFrame: ...
```

---
Here’s a ready-to-drop `SKILL.md` that follows the **Agent Skills open standard** used by **Codex / Claude Code / GitHub Copilot** (YAML frontmatter + instructions body). ([OpenAI Developers][1])

````md
---
name: python-docstrings-google
description: Write/upgrade Python module, class, and function docstrings in Google style for mkdocstrings. Ensure every public API has clear docs + at least one runnable example usage, without repeating type hints.
metadata:
  short-description: Google-style docstrings + examples for all public APIs (mkdocs/mkdocstrings friendly)
---

# Skill: Python docstrings (Google style) with runnable examples

## What this skill does
When editing or creating Python code, write **high-quality Google-style docstrings** for:
- Modules (top-of-file docstring)
- Public classes
- Public functions
- Public methods and properties

Docstrings must render well in **mkdocs + mkdocs-material + mkdocstrings**.

> This repo uses type hints → **do not repeat types in docstring**.

---

## When to use
Use this skill whenever you:
- Add or modify a public module/class/function/method/property
- See missing, vague, outdated, or inconsistent docstrings
- Prepare code for API docs (mkdocstrings pages)
- Introduce non-obvious behavior, edge cases, or side effects

**Public API rule of thumb**
- Public = no leading underscore (e.g., `fetch_prices`, `AlphaVantageClient`, `Client.get`)
- Private/internal = leading underscore (e.g., `_parse`, `_helper`) → docstring optional unless it’s tricky

---


## Authoring process (follow this every time)

1. Identify public objects changed/created.
2. For each object, draft:
   * One-line summary (what it does)
   * What matters: constraints, side effects, invariants
3. Add sections only if meaningful (`Raises` only when callers should care).
4. Add ideally runnable `Examples:` snippet.
5. Read it like a user: “Can I use this without opening the source?”


---

## Output requirements
For every **public** object:
1. Add/upgrade docstring in **Google style**
2. Include **at least one runnable example** (preferably minimal) inside `Examples:`
3. Keep descriptions **clear, concrete, and non-marketing**
4. Do not mention parameter types if type hints exist


---

## Google python docstring structure (used standard)
Use these sections as needed (only include what applies):
- Short summary (1 line)
- Optional extended summary (1–3 short paragraphs)
- Args:
- Returns:
- Raises:
- Attributes: (for classes, when useful)
- Examples:
- Notes: (optional)
- Warning: (rare)

---

## Formatting rules
- Triple double quotes: `"""Docstring..."""`
- Summary line ends with a period.
- Wrap lines roughly ~88–100 chars when reasonable (don’t force ugly wrapping).
- Prefer **imperative/active voice** (“Fetch prices…”, “Validate payload…”).
- Examples must be **copy-pastable** (no pseudocode).
- Use fenced code blocks with language identifiers in `Examples:` (e.g., ```py ...
- Use markdown syntax inside docstrings where applicable (e.g., for code blocks, lists, highlighting important parts with bold text).

### Advanced formatting
- Use mkdocs-material admonitions for `Note:` / `Warning:` blocks inside docstrings (don’t nest them).
- Use other mkdocs-material formatting as needed admonitions / blocks.


---

## Module docstring rules

Every module should start with a module docstring that answers:

* What the module provides, contains, or implements
* Typical usage
* Important constraints (timezone assumptions, caching, side effects)

---

## Class docstring rules

Class docstring must describe:

* What the class represents/does/implements
* Lifecycle/ownership (does it hold resources? caches?)
* Any key invariants
* Constructor expectations (especially if non-obvious)

If the class is primarily a data container, document the meaning of fields in `Attributes:`. If the class is not container, still document public attributes that matter to users.

---

## Method docstring rules

* For “obvious” getters/setters, keep it brief but still include an example (even a tiny one).
* Mention side effects (writes to disk, network calls, mutates internal state).
* Mention error conditions in `Raises:` (don’t list every possible low-level exception—wrap or describe the meaningful ones).

---

## Args/Returns/Attributes section rules

Describe meaning, not types. User will see type hints.

### ✅ Do
```py
Args:
  ticker: Stock ticker symbol (e.g., "AAPL").
  period: Time period to fetch. Defaults to "1y".
````

### ❌ Don’t (redundant types)

```py
Args:
  ticker (str): ...
  period (str, optional): ...
```

---

## `Examples` section rules (important)
Every public callable must have `Examples:` with at least one example.

Examples should:
- Use realistic values (`"AAPL"`, `"1d"`, etc.)
- Show the most common happy path first
- Avoid network calls in examples unless the module is literally a client library
- Prefer tiny examples that won’t rot quickly
- Don't use >>> interactive prompts; use standard script style so user can copy-paste it directly.

If a function is async, example must use `asyncio.run(...)`.


---

## Quality checklist (must pass)

* [ ] Module has a top quality docstring following software engineering conventions and best practices
* [ ] Every public function/class/method/property has a docstring
* [ ] Every public callable has `Examples:` with runnable code
* [ ] Args/Attributes have descriptions but **no types**
* [ ] Returns describes meaning (and shape if non-obvious)
* [ ] Raises lists meaningful exceptions + when they occur
* [ ] No fluff; no internal implementation narration unless it affects use

---

