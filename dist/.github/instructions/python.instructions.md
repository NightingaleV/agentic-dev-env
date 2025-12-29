---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

## Python Code Conventions

Your coding should include:
- Adherence to design principles (e.g., DRY, SOLID)

- Use type hints (not in docstrings) for better readability and maintainability.

- Pythonic idioms and best practices (e.g., PEP 8)
- Consideration of edge cases and error handling
- Thoughtful use of comments, but only where necessary, don't overuse them.
- Leverage Spark best practices (e.g., broadcast joins, partitioning, cache management)

### Python Type-hints

- Use type hints for function signatures and class attributes.
- Do not use Dict, List, Union, Tuple from typing module, use built-in types instead (e.g. dict, list, tuple).
- Use Pydantic models for complex data structures.

#### Exaple: Type Annotations
```python
# ✅ Good - use built-in types
def process_data(items: list[dict], config: dict[str, str]) -> tuple[int, str]:
    pass

# ❌ Avoid - old typing module imports
from typing import List, Dict, Union, Tuple
def process_data(items: List[Dict], config: Dict[str, str]) -> Tuple[int, str]:
    pass
```

## Preferred Approaches 

- Prefer dataclasses for simple data containers instead of dict. If user specifies dict, create TypedDict. Dictionaries are mainly used for dynamically generated data structures.
- Prefer dataclasses and/or pydantic models for structured data.
- Use pathlib for file path manipulations instead of os.path.
- Use f-strings for string formatting instead of .format() or % operator.
- Use list comprehensions and generator expressions for creating lists and iterators instead of map() and filter().
- Use context managers (with statement) for resource management instead of manual open/close.
- Use logging module for logging instead of print statements.
- Use asserts in methods and functions for validation.

## Python Documentation Standards

- Use docstrings for all public modules, classes, methods and functions.
- Use Google style docstrings.
- Use clear and concise descriptions oriented towards the user.
- Type hints should be used for types, avoid redundant type info in docstrings.

Instead of:
Args:
  ticker (str): The stock ticker symbol
  period (str, optional): Time period to fetch. Defaults to "1y" (1 year).
  interval (str, optional): Data interval. Defaults to "1d" (daily).
Lets have:
Args:
  ticker: The stock ticker symbol
  period: Time period to fetch. Defaults to "1y" (1 year).
  interval: Data interval. Defaults to "1d" (daily).
