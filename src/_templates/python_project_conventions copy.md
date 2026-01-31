

### Testing Considerations

- Coverage target: minimum 30% (configured in pyproject.toml)
- Use `--cov` flag with pytest for coverage reports
- Tests follow pytest framework with pytest runner
- Tests are located `tests/` directory
- When creating / updating tests, strictly follow the conventions established in `/tests/AGENTS.md`


### Guidelines
- Use conventional commits for commit messages, ensure clarity and consistency
- Understand the implication of commit types on versioning and changelogs
- **Semantic Versioning**:
  - Commit format: `<type>: message`
  - Major tags: `api`, `major`
  - Minor tags: `feat`
  - Patch tags: `fix`, `perf`
  - Other allowed tags: `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `test`
- **Branches**: Primary development on `develop`, releases merged to `master`