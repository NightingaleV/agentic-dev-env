
### Code Style Conventions
- **Type Hints**: Use Python 3.12+ syntax (`list[str]`, `dict[str, int]`), not `Union`, `Dict`, `List`
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