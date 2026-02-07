# Python docstrings (Extended Google style conventions)

## Mission
When editing or creating Python code, write **high-quality Google-style docstrings** for:
- Modules (top-of-file docstring)
- Public classes
- Public functions
- Public methods and properties

Docstrings must render well in **mkdocs + mkdocs-material + mkdocstrings**.

## Definitions (for this repo)
- **Public API**: no leading underscore (e.g., `fetch_prices`, `Client.get`). Docstring for Private/internal objects (leading underscore) should be concise versions, explanations included only when behavior is non-obvious.
- **Type hints are the source of truth**: do **not** repeat types in docstrings when type hints exist.

## Authoring workflow
1. Identify public objects changed/created.
2. For each object, draft:
   - A one-line summary (what it does)
   - What matters to callers and users: constraints, invariants, side effects
3. Add only the sections that apply (e.g., include `Raises:` only when callers should care).
4. Add at least one runnable `Examples:` snippet for every public callable. But if the component has a lot of different arguments (like plots, data processing functions, etc.), consider adding multiple examples using mkdocs-material content tabs to illustrate different use cases.
5. Read it like a user: “Can I use this without opening the source?”

## Output requirements
For every **public** object, add/upgrade a docstring that:
1. Follows **Google style**
2. Is **clear, concrete, and non-marketing**
3. Does **not** repeat type hints
4. Includes runnable `Examples:` for every public callable

## Google docstring structure (standard)
Include sections only when meaningful:
- Short summary (1 line)
- Optional extended summary (1–3 short paragraphs)
- `Args:`
- `Returns:`
- `Raises:`
- `Attributes:` (classes, when useful)
- `Methods:` (classes, when useful)
- `Examples:`

## Extended docstring structure
As we are using mkdocstrings, we can leverage richer formatting:
- Use **admonitions** for important notes, warnings, tips
- Use **content tabs** for alternative examples (e.g., sync vs. async)

Example of admonitions and content tabs in docstrings:
```py
"""Fetch historical stock prices for a given ticker symbol.

Abstract: Component Summary
  This function retrieves historical stock price data from a third-party API
  for the specified ticker symbol over a defined time period. It returns the data
  as a pandas DataFrame for easy analysis.

Args:
  ticker: Stock ticker symbol (e.g., "AAPL").
  period: Time period to fetch. Defaults to "1y".

Returns:
  A DataFrame containing historical stock prices.

Note: Requires an active internet connection.
  The data is fetched from a third-party API. Ensure you handle network errors appropriately.

Tip: API calls limits
  Free tier allows up to 500 requests per day. Consider caching results to avoid hitting limits.

Question: FAQ
  Q: **What time zones are the timestamps in?**
  A: All timestamps are in UTC.

  Q: **Can I fetch intraday data?**
  A: Yes, set the `period` argument to "1d" or "5

Example:
  === "Basic usage"

    The most common way to fetch the data is to call `fetch_prices` with a ticker and optional period:
    ```py
    from finance import fetch_prices

    df = fetch_prices("AAPL", period="6mo")
    print(df.head())
    # Output:
    #         date        open        high         low       close   volume
    # 0  2024-01-01  150.00  155.00  149.00  154.00  1000000
    # 1  2024-01-02  154.00  156.00  153.00  155.00   800000
    # ...
    ```

  === "Async usage"

    If you prefer to use the async version, you can call `fetch_prices_async` within an async context.

    !!! note "Async version"
        The async version is useful when you want to fetch data for multiple tickers concurrently or integrate with an async application.

    ```py
    import asyncio
    from finance import fetch_prices_async  

    async def main():
        df = await fetch_prices_async("AAPL", period="6mo")
        print(df.head())
    asyncio.run(main())
    # Output:
    #         date        open        high         low       close   volume
    # 0  2024-01-01  150.00  155.00  149.00  154.00  1000000
    # 1  2024-01-02  154.00  156.00  153.00  155.00   800000
    ```
"""
```

Allowed admonition types: 

- `Abstract`: A brief summary or overview of a concept or topic.
- `Note`: General information or explanations.
- `Tip`: Helpful tips or best practices.
- `Warning`: Important warnings or cautions.
- `Danger`: Critical warnings or common errors, or unexpected behavior.
- `Info`: Additional information or context that may be useful to the reader.
- `Success`: Positive outcomes, success stories, or examples of good practices.
- `Example`: Code examples that illustrate a concept or usage.

## Formatting rules
- Use triple double quotes: `"""Docstring..."""`
- Summary line ends with a period.
- Wrap lines roughly ~88–100 chars when reasonable (don’t force ugly wrapping).
- Prefer imperative/active voice (“Fetch prices…”, “Validate payload…”).
- Examples must be **copy-pastable** (no pseudocode).

### Formatting `Examples:`
- Use content tabs (`=== "Title for Example"`) for multiple examples.
- Title should summarize the example’s purpose.
- Example should have short description (1-2 sentences) of what it demonstrates.
- If the example demonstrates a common use case, put it first.
- If example is focused on a specific argument or edge case, consider putting it in a separate tab with a descriptive title. Feed free to describe the case or args the example focuses in the further description of the example.
- Use fenced code blocks with `python` or `py` language identifier.


## Markdown in docstrings (mkdocstrings-friendly)
- Prefer fenced code blocks with language identifiers in `Examples:` (e.g., ```py).
- You may use mkdocs-material **admonitions** and **content tabs** where they add clarity.
- Avoid nesting admonitions inside each other.
- Keep function/method docstrings simple; put richer narrative/context in module/class docstrings.

## Content rules
### 1) Keep it user-facing
Explain what it does, what matters, and any side effects (I/O, network, mutation, caching).

### 2) Don’t repeat types in docstrings
Describe meaning, not types. The user will see type hints.

✅ Do
```py
Args:
  ticker: Stock ticker symbol (e.g., "AAPL").
  period: Time period to fetch. Defaults to "1y".

Returns:
  A DataFrame containing historical stock prices.
```

❌ Don’t
```py 
Args:
  ticker (str): ...
  period (str, optional): ...

Returns:
  pd.DataFrame: ...
```

## Object-specific rules
### Module docstrings
Every module should start with a module docstring that answers:
- What the module provides/contains/implements
- Typical usage
- Important constraints (timezone assumptions, caching, side effects)

### Class docstrings
Class docstrings should describe:
- What the class represents/does/implements
- Lifecycle/ownership (resources, caches)
- Key invariants
- Constructor expectations (especially if non-obvious)

If the class is primarily a data container, document fields in `Attributes:`. Otherwise, document the public attributes that matter to callers.

### Method/property docstrings
- For obvious getters/setters, keep it brief but still include an example (even a tiny one).
- Mention side effects (writes to disk, network calls, mutates internal state).
- In `Raises:`, document meaningful error conditions (don’t list every low-level exception).

## `Examples:` rules (important)
Every public callable must have `Examples:` with at least one runnable example.

Examples should:
- Use realistic values (`"AAPL"`, `"1d"`, etc.)
- Show the most common happy path first
- Avoid network calls in examples unless the module is literally a client library
- Prefer tiny examples that won’t rot quickly
- Don’t use `>>>` prompts; use standard script-style code blocks so users can copy-paste directly.

If a function is async, example must use `asyncio.run(...)`.

## Quality checklist (must pass)
- [ ] Module has a top-quality docstring following software engineering best practices
- [ ] Every public function/class/method/property has a docstring
- [ ] Every public callable has `Examples:` with runnable code
- [ ] Args/Attributes describe meaning but **no types**
- [ ] Returns describes meaning (and shape if non-obvious)
- [ ] Raises lists meaningful exceptions + when they occur
- [ ] No fluff; no internal implementation narration unless it affects use
