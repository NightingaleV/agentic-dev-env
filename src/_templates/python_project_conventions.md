## Project Conventions for Python Development

### Package Manager
- This project uses **uv** as the package manager (pip is only fallback)
- Always use `uv sync` to install dependencies, `uv run` to execute Python commands
- To add a new dependency, use `uv add <package>`.
- To add a dev dependency, use `uv add --group dev pytest pytest-mock coverage`.
- Optional dependencies are grouped in `pyproject.toml` under `dev` and `docs` groups.
- Build commands use `uv build --wheel`

### Testing Considerations

- Coverage target: minimum 30% (configured in pyproject.toml)
- Use `--cov` flag with pytest for coverage reports
- Tests follow pytest framework with pytest runner
- Tests are located `tests/` directory
- When creating / updating tests, strictly follow the conventions established in `/tests/AGENTS.md`

### Commit & VersioningGuidelines
- Use conventional commits for commit messages, ensure clarity and consistency
- Understand the implication of commit types on versioning and changelogs
- **Semantic Versioning**:
  - Commit format: `<type>: message`
  - Major tags: `api`, `major`
  - Minor tags: `feat`
  - Patch tags: `fix`, `perf`
  - Other allowed tags: `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `test`
- **Branches**: Primary development on `develop`, releases merged to `master`