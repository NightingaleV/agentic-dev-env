
### Code Style Conventions
- **Line Length**: Maximum 120 characters
- **Docstrings**: Google Docstring conventions
- **Validation**: Use asserts in methods/functions for validation
- **Design Principles**: Follow DRY, SOLID principles
- **Error Handling**: Consider edge cases and provide proper

### Tech Stack Preferences
- **Visualizations**: Plotly (primary), Seaborn (alternative)
- **Data Processing**: Pandas (general), PySpark (performance-critical pipelines)
- **ML Tracking**: MLflow for artifact/metrics logging
- **Documentation**: MkDocs with Material theme
- **Frontend**: Streamlit (simple), Reflex (complex applications) / Dash (alternative)

## Type Hinting
- **Type Hints**: Use Python 3.12+ syntax (`list[str]`, `dict[str, int]`), not `Union`, `Dict`, `List` from `typing` module
- Options: When arg types are limited number of options, consider using `Literal` for clarity (e.g., `Literal["1d", "1w", "1m"]` for time periods).
- **Type hints are the source of truth**: do **not** repeat types in docstrings when type hints exist.
- **Optional args**: Use `Optional` or default to `None` for optional arguments (e.g., `def fetch_data(period: Optional[str] = None) -> pd.DataFrame:`)
- Use TypedDicts for structured data user input is complex and when appropriate (e.g., API responses, configuration objects) to improve readability and maintainability.