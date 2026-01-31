
## General Notebook formatting goals

- Produce a notebook that is easy to skim and execute top-to-bottom.
- Keep the original logic intact: only reorganize into cells and add lightweight explanations in markdown if needed.
- Prefer small, focused cells over large multi-purpose cells.
- Prefer to split notebook into chapters/sections/subsections as needed.

---

## Structure rules

### Chapters, sections, and subsections

- Chapters group major phases (examples: Ingestion, Transformation, Analysis, Export).
- Sections group related steps within a chapter (examples: Load, Clean, Feature Engineering).
- Subsections typically map to a single code cell (use a clear cell title).
- Ensure that variable names are descriptive, meaningful and short.

### Narrative vs code

- Use markdown cells to:
	- state the goal of the chapter/section
	- explain inputs/outputs and key decisions
	- summarize complex logic or non-obvious invariants
- Avoid over-explaining. Prefer short paragraphs and lists.

### Cell boundaries

- Each code cell should be a logical block.
- Define helpers before first use.
- Avoid creating hidden state across distant cells.

---

## Quality checklist

- Headings and cell titles are consistent and descriptive.
- Markdown explains “why” and “what”, not every line of code.
- Code stays formatted and readable.
- No behavior changes (only formatting and rephrasing of comments when needed).
