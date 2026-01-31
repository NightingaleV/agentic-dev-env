## Recommended `docs/` folder layout

Suggested baseline (adjust to what already exists):


- `docs/modules/<module_name>/` – for each major module/package in the codebase, create a subfolder with its own Diátaxis structure:
  - `docs/modules/<module_name>/tutorial.md` - Tutorial for that module.
  - `docs/modules/<module_name>/how_to_<task>.md` - How-to guide for a specific task in that module.
  - `docs/modules/<module_name>/explanation/<topic>.md` - Explanation topics related to that module. 
  - `docs/modules/<module_name>/examples/<example>.py` - Practical examples related to that module. Can be linked from other docs.
  - `docs/modules/<module_name>/api.md` - API reference for that module.
  - `docs/modules/<module_name>/assets/` - Images and diagrams specific to that module.

For the documentation that is not specific to a single module, use `docs/general` folder with following structure:

- `docs/general/` – shared content not specific to one module:
  -  `docs/general/assets/` – images and diagrams used across multiple docs pages.
  -  `docs/general/tutorials/` – code snippets and examples referencing multiple modules or not module related guides.
     -  `docs/general/tutorials/quick_start.md` – quick start page for new users.
     -  `docs/general/tutorials/contributing.md` – contribution guidelines.
  -  `docs/general/explanation/` – common conceptual topics not related to just one module.
     -  `docs/general/explanation/overview.md` – project overview.
  -  `docs/general/how_to/` – common how-to guides that reference multiple modules from package.
     -  `docs/general/how_to/install.md` – installation guide.

Keep filenames lowercase with underscores: `my_feature.md`. Sample applies to folders too: `my_feature/`. Each folder will have an `index.md` as landing page.
