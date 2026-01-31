## Goals for docs changes

- Keep docs **user-first**: practical, without jargon, clear, and accurate.
- Ensure docs are **complete enough** for new users to onboard and use the project.
- Maintain **buildability**: docs should always build without errors or warnings.
- Preserve **link integrity**: no broken internal or external links.

## Documentation Artifacts (conventional)

We follow the *Diátaxis* style split. 

- **Tutorials**: learning-oriented, step-by-step, “do this then that”. Serves as getting started section and onboarding to component. Can link to how-to guides for specific tasks. Assumes nothing, includes commands/output, tiny dataset, happy path only. Is wide enough to cover main use cases and happy paths so user has good understanding after reading.
- **How-to guides**: task-oriented, goal-driven, examples assumes basic familiarity, can include edge cases and troubleshooting. Focused on “do X” for a specific task. Can link to explanations for deeper understanding.
- **Topics & Concepts / Explanation**: Understanding-oriented, clarifying a particular topic. Detailed explanations of features, architecture, design decisions. Can contain nested subfolders properly organizing conceptual content if needed.
- **API Reference**: auto-generated from code docstrings (mkdocstrings), follows code structure of packages/modules and contains mkdocstrings references to modules. Information-oriented, technical descriptions of machinery, API documentation. Follows package and module structure of main python codebase. Includes potentially nested subfolders properly organizing conceptual content if needed.

## Voice + structure

- Use 2nd person: “Run this”, “You’ll see…”
- Lead with goal, then steps, then what success looks like.
- Prefer short paragraphs + lists. No wall-of-text.

## Placement decision tree (agent-friendly)

- New user needs first success path → tutorial
- User already knows basics, wants a task done → how to guide
- User asks “why is it built like this?” or “how does it work?” → explanation
- User asks “what functions/classes exist and what do they take?” → api

