
## VS Code notebook syntax (Jupytext percent format, `.py`)

### File header (recommended)

Use the Jupytext header so VS Code can round-trip between `.ipynb` and `.py:percent` reliably:

```python
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
# ---
```

---

### Markdown cells

Use `# %% [markdown]` and store markdown in a triple-quoted string:

```python
# %% [markdown]
"""
## Title of the section

Short explanation.
"""
```

---

### Code cells

Use `# %%`:

```python
# %%
print("This is a code cell")

def add(a, b):
	return a + b
```

---

### Markdown inside markdown cells

Use standard Markdown (lists, links, fenced code blocks, etc.).
