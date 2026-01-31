## Recommended `docs/` folder layout

Suggested baseline (adjust to what already exists):

- `docs/index.md` – landing page / quickstart
- `docs/install.md` - installation instructions
- `docs/getting_started/`
  - `docs/getting_started/install.md` - Installation guide
  - `docs/getting_started/overview.md` - Overview of the project
  - `docs/getting_started/quick_start.md` - Quick start guide: Your First success path
- `docs/tutorials/` – learning guides with step-by-step instructions
- `docs/how_to/` – task recipes, specific procedures, contains code examples
- `docs/explanation/` – explanations, feature descriptions, architecture, decisions. Should contain nested subfolders properly organizing conceptual content if needed.
- `docs/api/` – API reference (mkdocstrings). There should be ideally one file per top-level package or module.
- `docs/assets/` – images, diagrams, small static files
- `docs/contributing/` - contribution guidelines
  - `docs/contributing/conventions.md` - general project conventions for contributors

Keep filenames lowercase with underscores: `my_feature.md`. Sample applies to folders too: `my_feature/`. Each folder will have an `index.md` as landing page.

## Placement decision tree (agent-friendly)

- New user needs first success path → tutorials/
- User already knows basics, wants a task done → how_to/
- User asks “why is it built like this?” or “how does it work?” → explanation/
- User asks “what functions/classes exist and what do they take?” → api/