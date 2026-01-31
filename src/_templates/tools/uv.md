



### Package Manager
- This project uses **uv** (not pip or poetry) as the package manager
- Always use `uv sync` to install dependencies, `uv run` to execute Python commands
- Build commands use `uv build --wheel`

### Environment Setup
```bash
# Install core dependencies
uv sync
# Install project dependencies with optional dependency groups
uv sync --group dev
```

### Build and Package
```bash
# Build package
uv build

# Clean build artifacts
rm -rf build dist *.egg-info .pytest_cache .mypy_cache .coverage htmlcov
```

### Documentation
```bash
# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build
```