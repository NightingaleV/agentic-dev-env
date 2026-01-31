# Agentic Development Environment

A comprehensive scaffolding framework for AI code agents and development workflows using prompt templates, agent specifications, and reusable prompts for popular AI development platforms.

## Overview

This repository provides a modular, production-ready foundation for integrating AI agents into your development workflow. It includes pre-built agent definitions, prompt templates, and skill modules designed to work with:

- **GitHub Copilot**
- **OpenCode AI**
- **OpenAI Codex**
- **Warp.Dev AI**

Perfect for teams building AI-driven development pipelines, particularly for **Python and Machine Learning projects**.

## What's Inside

The project uses a source-to-distribution build system:

### Source Structure (`/src`)

#### Base Content (`/src/base`)
Shared content copied to all agent frameworks:

- **agents/** - Agent definitions (code-reviewer, debug, high-lvl-plan, jira-assistant)
- **prompts/** - Reusable prompts for code review, documentation, specifications, testing
- **skills/** - Specialized skill modules (docstring-python, brand-guidelines)
- **instructions/** - GitHub-specific instructions for Python development

#### Target-Specific (`/src/targets`)
Platform-specific overrides and additions:

- **.codex/** - Codex-only prompts and customizations
- **.opencode/** - OpenCode-specific agents and commands
- **.github/** - GitHub Copilot instructions and configuration
- **docs/, tests/, .vscode/** - Project documentation and settings
- **AGENTS.md** - Project overview

#### Templates (`/src/templates`)
Jinja2 templates for content reuse:
- **python_test_core.md** - Reusable testing guidelines

### Distribution Package (`/dist`)

Generated build output ready for import into other projects:

- **.github/** - GitHub Copilot (agents with `.agent.md` suffix, prompts with `.prompt.md`)
- **.opencode/** - OpenCode AI (singular folders: `skill/`, `agent/`, `command/`)
- **.codex/** - OpenAI Codex (no suffix transformations)
- **docs/, tests/, .vscode/** - Documentation and project settings
- **AGENTS.md** - Project guide

### 📚 Documentation (`/docs`)

Comprehensive guides covering:
- Getting started tutorials
- How-to guides for common tasks
- API reference documentation
- Example implementations

## Quick Start

### Setup Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/agentic-dev-env.git
   cd agentic-dev-env
   ```

2. **Install dependencies using uv**
   ```bash
   # Install uv if not already installed
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Create virtual environment and install dependencies
   uv venv
   uv sync
   ```

3. **Build distribution files**
   ```bash
   # Build all targets
   ./build.sh
   
   # Or build specific target
   ./build.sh --target .github
   
   # Clean and rebuild
   ./build.sh --clean
   
   # Advanced: use Python directly
   uv run python build.py --clean
   ```

### Using in Your Project

1. **Copy distribution to your project**
   ```bash
   # Copy entire dist/ folder
   cp -r dist/ /path/to/your/project/
   
   # Or copy specific target
   cp -r dist/.github /path/to/your/project/
   ```

2. **Configure your AI platform**
   - For GitHub Copilot: Copy `.github/` folder
   - For OpenCode: Copy `.opencode/` configuration
   - For Codex: Copy `.codex/` settings
   - For Warp: Integrate prompts into your Warp configuration

### Working with Templates

The project includes a powerful Jinja2 template system for reusing content:

```markdown
# In your file (src/base/prompts/my-prompt.md)
{% include "python_test_core.md" %}
```

This includes shared content from `/src/templates/` into your files. Perfect for:
- Shared guidelines and best practices
- Common code style rules
- Reusable documentation snippets

📖 **[Read the Template Guide](./TEMPLATE_GUIDE.md)** for detailed usage instructions.

## Key Features

✅ **Framework-Agnostic** - Works with multiple AI platforms  
✅ **Pre-built Workflows** - Debug, code review, documentation, specifications  
✅ **Modular Design** - Mix and match prompts and skills  
✅ **Template System** - Jinja2-powered content reuse across files  
✅ **Automated Build** - Single command to generate all distributions  
✅ **Production Ready** - Tested configurations and best practices  
✅ **Well-Documented** - Comprehensive guides and examples  
✅ **Python/ML Focused** - Specialized for data science workflows  
✅ **Easy Integration** - Copy scaffolding to new projects  

## Documentation

- **[Quick Reference](./QUICK_REFERENCE.md)** - Cheat sheet for common tasks
- **[Project Guide](./AGENTS.md)** - Overview and project structure
- **[Template System Guide](./TEMPLATE_GUIDE.md)** - How to use Jinja2 templates
- **[Build Configuration](./build_config.yaml)** - Customize build behavior
- **[Distribution Docs](./dist/docs/)** - Full documentation site
- **[Examples](./dist/docs/examples/)** - Practical code examples

## Project Structure

```
agentic-dev-env/
├── README.md                  # This file
├── AGENTS.md                  # Detailed project guide
├── TEMPLATE_GUIDE.md          # Template system user guide
├── pyproject.toml             # Python project configuration
├── uv.lock                    # Lock file for uv
├── build.py                   # Build script
├── build.sh                   # Build wrapper script
├── build_config.yaml          # Build configuration
├── build_config.yaml          # Build configuration
├── src/                       # Source files
│   ├── base/                 # Shared content (all targets)
│   │   ├── agents/          # Agent definitions (no suffix)
│   │   ├── prompts/         # Prompt templates (no suffix)
│   │   ├── skills/          # Reusable skill modules
│   │   └── instructions/    # GitHub instructions
│   ├── targets/             # Target-specific content
│   │   ├── .github/        # GitHub Copilot overrides
│   │   ├── .opencode/      # OpenCode AI overrides
│   │   ├── .codex/         # Codex overrides
│   │   ├── docs/           # Documentation
│   │   ├── tests/          # Test specifications
│   │   ├── .vscode/        # VS Code settings
│   │   └── AGENTS.md       # Project overview
│   └── templates/           # Jinja2 templates
│       └── python_test_core.md
└── dist/                     # Generated distribution (gitignored)
    ├── .github/             # GitHub Copilot (with suffixes)
    ├── .opencode/           # OpenCode AI (singular folders)
    ├── .codex/              # OpenAI Codex (no suffixes)
    ├── docs/                # Documentation
    ├── tests/               # Test specifications
    └── AGENTS.md            # Project overview
```

## Best Practices

### For AI Agents

1. **Clarity First** - Agent instructions must be unambiguous and complete
2. **Gradual Complexity** - Start with simple prompts, add context progressively
3. **Test Thoroughly** - Validate agent output before production use
4. **Document Everything** - Keep prompts versioned and documented
5. **Iterate Regularly** - Refine prompts based on real-world usage

### For Documentation

- Follow **Diátaxis** structure: Tutorials → How-to → Explanation → Reference
- Keep documentation up-to-date with code changes
- Use mkdocstrings to auto-generate API docs from code
- Maintain link integrity and avoid broken references
- Optimize for user experience and clarity

## Usage Examples

### Generate Python Unit Tests
```bash
# Use the create-unittest-python.prompt.md template
# with your code snippet and desired test framework
```

### Code Review Process
```bash
# Apply code-review.prompt.md to pull requests
# Get consistent feedback across your team
```

### Debug Complex Issues
```bash
# Use debug.agent.md workflow to systematically
# identify and resolve bugs
```

## Contributing

Contributions are welcome! Please:

1. Follow existing prompt and template conventions
2. Update documentation alongside code changes
3. Ensure all examples are tested and working
4. Maintain consistency with brand guidelines
5. Keep the project organized and well-documented

## Requirements

- **Python 3.10+** (for build system and Python-specific skills)
- **uv** (for dependency management) - [Install uv](https://docs.astral.sh/uv/)
- **Git** (for version control)
- Access to your preferred AI platform (Copilot, OpenCode, Codex, or Warp)

### Build System Dependencies

The build system requires:
- `jinja2>=3.1.0` - Template engine for content reuse
- `pyyaml>=6.0` - YAML configuration parser

These are automatically installed via `uv sync`.

## Platform Setup

### GitHub Copilot
```bash
# Copy VS Code configuration
cp -r dist/.vscode ~/.config/Code/User/
```

### OpenCode AI
```bash
# Use .opencode/ configuration
# Follow OpenCode documentation for setup
```

### OpenAI Codex
```bash
# Use .codex/ configuration
# Set API keys and preferences
```

### Warp.Dev AI
```bash
# Import prompts from prompt_templates/
# Follow Warp documentation for integration
```

## License

This project is provided as-is for educational and development purposes. See [LICENSE](./LICENSE) for details.

## Support

For issues, questions, or suggestions:
- Open a [GitHub Issue](https://github.com/yourusername/agentic-dev-env/issues)
- Check existing documentation in [docs/](./dist/docs/)
- Review [AGENTS.md](./AGENTS.md) for project guidelines

## Roadmap

- [ ] Additional agent templates (security, performance)
- [ ] Integration examples for popular frameworks
- [ ] Community-contributed prompts and skills
- [ ] Interactive prompt builder tool
- [ ] Metrics and evaluation frameworks

## Related Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [OpenAI Codex Documentation](https://platform.openai.com/docs/guides/code)
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Python Docstring Conventions](https://pep257.pycqa.org/)

---

**Made for developers who want to leverage AI agents in their workflow efficiently and consistently.**
