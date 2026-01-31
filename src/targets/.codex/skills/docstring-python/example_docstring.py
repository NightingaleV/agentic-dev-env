"""Example module demonstrating repo docstring conventions (Google style).

Note: "Description"
    This module is intentionally small but showcases **"gold standard" documentation**:
    - A module docstring with clear purpose + **runnable examples**
    - **Google-style docstrings** for public classes/functions/methods/properties
    - **No repeated types** in docstrings (type hints already exist)
    - mkdocs-material **admonitions** and **content tabs** shown in docstrings (mkdocstrings-friendly)

Tip: "Practical tip"
    You can use mkdocs-material **admonitions** and **content tabs** in docstrings! They will be rendered
    correctly by mkdocstrings without nesting issues. Just **avoid nesting admonitions** inside each other.

    Use admonitions mainly in the **module** and **class** docstrings to provide additional context, and keep
    **function/method docstrings simple**.

Info: "mkdocstrings"
    You can see how mkdocstrings renders these docstrings in the generated **API reference**
    documentation for this module.

The main "domain" here is a tiny, local-only signal scoring utility to keep
examples stable (**no network calls**, **no current-time dependencies**).

Examples:
    **Basic function usage:**

    ```py
    from example_docstring import score_signal

    result = score_signal(value=0.72, threshold=0.5)
    print(result)  # 1.0
    ```

    **Class usage:**

    ```py
    from example_docstring import SignalScorer

    scorer = SignalScorer(threshold=0.6)
    print(scorer.score(0.72))       # 1.0
    print(scorer.is_positive(0.1))  # False
    ```
"""


from __future__ import annotations

from dataclasses import dataclass


def score_signal(value: float, threshold: float = 0.5) -> float:
    """Convert a numeric value into a binary score using a threshold.

    Args:
        value: Input value to score.
        threshold: Values greater than or equal to this are scored as positive.
            Defaults to 0.5.

    Returns:
        1.0 if `value >= threshold`, otherwise 0.0.

    Raises:
        ValueError: If `threshold` is not in the interval [0.0, 1.0].

    Examples:
        ```py
        from example_docstring import score_signal

        print(score_signal(0.49))  # 0.0
        print(score_signal(0.5))   # 1.0
        print(score_signal(0.9, threshold=0.95))  # 0.0
        ```
    """
    if not (0.0 <= threshold <= 1.0):
        raise ValueError("`threshold` must be within [0.0, 1.0].")
    return 1.0 if value >= threshold else 0.0


@dataclass(slots=True)
class SignalScorer:
    """Score values and keep the decision rule in one place.
    
    Abstract: "What this class is for"
        Use a scorer object when you want a **consistent rule** (threshold) applied
        across many calls and you want a single place to document it.

    Attributes:
        threshold: Values greater than or equal to this are treated as positive.

    Tip: "Practical tip"
        Keep examples **copy-paste runnable** and stable:
        - Prefer **no network calls**
        - Avoid **current-time dependencies**
        - Show outputs as **Python comments**

    Warning: "Threshold bounds"
        `threshold` must be within `[0.0, 1.0]`. Invalid values raise `ValueError`.

    Info: "Docs rendering"
        mkdocstrings can render **Google-style docstrings** and mkdocs-material extensions
        like **admonitions** and **content tabs**. Avoid **nesting admonitions**.

    Examples:
        ```py
        from example_docstring import SignalScorer

        scorer = SignalScorer(threshold=0.7)
        print(scorer.score(0.7))        # 1.0
        print(scorer.is_positive(0.69)) # False
        ```
    """

    threshold: float = 0.5

    def __post_init__(self) -> None:
        """Validate invariants after initialization.

        Raises:
            ValueError: If `threshold` is not in the interval [0.0, 1.0].

        Examples:
            ```py
            from example_docstring import SignalScorer

            scorer = SignalScorer(threshold=0.0)
            print(scorer.threshold)  # 0.0
            ```
        """
        if not (0.0 <= self.threshold <= 1.0):
            raise ValueError("`threshold` must be within [0.0, 1.0].")

    @property
    def decision_rule(self) -> str:
        """Human-readable description of the current scoring rule.

        Returns:
            A short string describing how positivity is determined.

        Examples:
            ```py
            from example_docstring import SignalScorer

            scorer = SignalScorer(threshold=0.6)
            print(scorer.decision_rule)  # value >= 0.6
            ```
        """
        return f"value >= {self.threshold}"

    def score(self, value: float) -> float:
        """Score a value according to the scorer's threshold.

        Args:
            value: Input value to score.

        Returns:
            1.0 if `value >= threshold`, otherwise 0.0.

        Examples:
            ```py
            from example_docstring import SignalScorer

            scorer = SignalScorer(threshold=0.8)
            print(scorer.score(0.79))  # 0.0
            print(scorer.score(0.8))   # 1.0
            ```
        """
        return score_signal(value=value, threshold=self.threshold)

    def is_positive(self, value: float) -> bool:
        """Check whether a value is considered positive by this scorer.

        Args:
            value: Input value to evaluate.

        Returns:
            True if `value >= threshold`, otherwise False.

        Examples:
            ```py
            from example_docstring import SignalScorer

            scorer = SignalScorer(threshold=0.5)
            print(scorer.is_positive(0.49))  # False
            print(scorer.is_positive(0.5))   # True
            ```
        """
        return value >= self.threshold

    def summarize(self) -> str:
        """Create a short summary suitable for logs or UI.

        Returns:
            A concise summary string describing the scorer configuration.

        Examples:
            ```py
            from example_docstring import SignalScorer

            scorer = SignalScorer(threshold=0.55)
            print(scorer.summarize())  # SignalScorer(threshold=0.55)
            ```
        """
        return f"SignalScorer(threshold={self.threshold})"
