# Template System User Guide

This guide explains how to use the Jinja2 template system to reuse content across your agent configuration files.

## Overview

The build system supports Jinja2 template includes, allowing you to:
- Create reusable content snippets in `/src/templates/`
- Include them in base files (`/src/base/`)
- Include them in target-specific files (`/src/targets/`)
- Nest templates (templates can include other templates)

## Quick Start

### 1. Create a Template

Create a reusable template in `/src/templates/`:

```markdown
# src/templates/python_testing_best_practices.md

## Testing Best Practices

- Write tests that validate behavior, not implementation
- Keep tests simple and readable
- Use descriptive test names: `test_<what>_<when>_<then>()`
- Mock only external dependencies (network, DB, filesystem)
- Cover happy path + key edge cases
```

### 2. Include Template in Base File

In any file under `/src/base/`, use the `{% include %}` directive:

```markdown
# src/base/prompts/create-unittest-python.md
---
description: "Generate unit tests for Python components"
---

# Python Unit Test Generation

Generate comprehensive unit tests following our standards.

{% include "python_testing_best_practices.md" %}

## Additional Requirements

- Use pytest as the testing framework
- Target test coverage: 80%+
- Include parametrized tests for edge cases
```

### 3. Include Template in Target-Specific File

Templates work the same way in target-specific files:

```markdown
# src/targets/.github/prompts/review-tests.prompt.md
---
description: "Review test quality and coverage"
---

# Test Review Guidelines

When reviewing tests, ensure they follow our standards:

{% include "python_testing_best_practices.md" %}

## GitHub-Specific Checks

- Verify CI/CD test pipelines pass
- Check code coverage reports
- Ensure no flaky tests
```

### 4. Build to Apply Templates

Run the build to resolve all template includes:

```bash
./build.sh
```

The output in `dist/` will have all templates resolved and content merged.

## Examples

### Example 1: Shared Code Style Guide

**Template:** `/src/templates/code_style_python.md`
```markdown
## Python Code Style

- Follow PEP 8 conventions
- Maximum line length: 100 characters
- Use type hints for public APIs
- Write docstrings for all public functions
```

**Usage in Base Prompt:** `/src/base/prompts/code-review-diff.md`
```markdown
# Code Review Guidelines

{% include "code_style_python.md" %}

When reviewing diffs, focus on:
- Logic correctness
- Performance implications
- Security considerations
```

**Result:** After build, `dist/.github/prompts/code-review-diff.prompt.md` contains merged content.

### Example 2: Nested Templates

Templates can include other templates:

**Template 1:** `/src/templates/error_handling_basics.md`
```markdown
## Error Handling Basics

- Use specific exception types
- Always provide context in error messages
- Log errors with appropriate severity levels
```

**Template 2:** `/src/templates/python_error_handling.md`
```markdown
## Python Error Handling

{% include "error_handling_basics.md" %}

### Python-Specific

- Use `raise ... from e` for exception chaining
- Prefer built-in exceptions when appropriate
- Document exceptions in docstrings (Raises: section)
```

**Usage:** `/src/base/agents/debug.md`
```markdown
# Debug Agent

{% include "python_error_handling.md" %}

When debugging, trace error origins systematically.
```

### Example 3: Multiple Includes in One File

You can include multiple templates:

```markdown
# src/base/prompts/write-production-code.md
---
description: "Guidelines for production-ready code"
---

# Production Code Standards

## Style Guidelines
{% include "code_style_python.md" %}

## Error Handling
{% include "python_error_handling.md" %}

## Testing Requirements
{% include "python_testing_best_practices.md" %}

## Performance
- Profile before optimizing
- Use appropriate data structures
- Consider memory usage
```

## Template Locations and Paths

### Template Directory
All templates must be in `/src/templates/` (flat or nested):

```
/src/templates/
  python_testing_best_practices.md
  code_style_python.md
  error_handling_basics.md
  python_error_handling.md
```

### Include Syntax
Use the filename relative to `/src/templates/`:

```markdown
{% include "python_testing_best_practices.md" %}
```

For nested directories (if you create them):
```markdown
{% include "python/testing_best_practices.md" %}
```

## Advanced Usage

### Conditional Includes (Future)

While not currently configured, Jinja2 supports conditional logic:

```markdown
{% if target == "github" %}
{% include "github_specific_guidelines.md" %}
{% endif %}
```

To enable this, you'd need to pass variables in the build script's `template.render()` call.

### Variables in Templates (Future)

You can also pass variables to templates:

```markdown
# Template with variable
Project: {{ project_name }}
Version: {{ version }}
```

To use this, modify `build.py` to pass variables:
```python
template.render(project_name="my-project", version="1.0.0")
```

## How It Works

1. **Template Discovery**: Build script loads all files from `/src/templates/` into Jinja2 environment

2. **File Processing**: When processing `.md` files from `/src/base/` or `/src/targets/`:
   - Reads file content
   - Checks for Jinja2 syntax (`{%` or `{{`)
   - If found, processes through Jinja2 template engine
   - Resolves all `{% include %}` directives recursively

3. **Output**: Writes processed content to `/dist/` with templates fully resolved

## Template Guidelines

### Do's ✅

- **Keep templates focused**: One concept per template
- **Use descriptive names**: `python_testing_best_practices.md` not `test.md`
- **Document templates**: Add comments at the top explaining purpose
- **Version control**: Templates are source code, commit them
- **Reuse liberally**: If content appears in 2+ files, make it a template

### Don'ts ❌

- **Don't put target-specific content in templates**: Templates are shared
- **Don't create circular includes**: Template A includes B, B includes A (infinite loop)
- **Don't use complex Jinja2 logic**: Keep it simple for maintainability
- **Don't duplicate templates**: Consolidate similar templates

## Troubleshooting

### Template Not Found Error

```
⚠️  Template not found while processing /src/base/prompts/test.md: python_test.md
```

**Solution**: Check that template exists in `/src/templates/python_test.md`

### Template Processing Error

```
⚠️  Error processing template in /src/base/agents/test.md: unexpected '}'
```

**Solution**: Check Jinja2 syntax - common issues:
- Unclosed tags: `{% include "file.md"` (missing `%}`)
- Wrong quotes: `{% include 'file.md' %}` (use double quotes)

### Content Not Updating After Template Change

**Solution**: Rebuild to apply template changes:
```bash
./build.sh --clean
```

## Examples in This Project

See existing templates:

1. **`/src/templates/python_test_core.md`**
   - Reusable testing guidelines
   - Can be included in test-related prompts and instructions

## Best Practices Summary

1. **Create templates for repeated content** (appears in 2+ files)
2. **Name templates descriptively** (what they contain, not where they're used)
3. **Keep templates simple** (avoid complex logic)
4. **Document template purpose** (add header comments)
5. **Test after changes** (rebuild and verify output)
6. **Version control templates** (they're as important as code)

---

For more information:
- See `build.py` for implementation details
- See `build_config.yaml` for template configuration
- See [Jinja2 Documentation](https://jinja.palletsprojects.com/) for advanced features
