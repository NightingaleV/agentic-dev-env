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

### 📋 Prompt Templates (`/prompt_templates`)

Reusable prompts organized by type:

#### Agents (`/agents`)
- **debug.agent.md** - Systematic debugging and bug resolution workflows
- **frontend_developer.agent.md** - Frontend development guidance and best practices
- **high-lvl-plan.agent.md** - Strategic planning and architecture design
- **jira-assistant.agent.md** - JIRA integration and issue management

#### Prompts (`/prompts`)
- **code-review.prompt.md** - Code review guidelines and standards
- **code-into-tutorial-md.prompt.md** - Convert code snippets into tutorial documentation
- **create-specification.prompt.md** - Generate concise technical specifications
- **create-detailed-specification.prompt.md** - Comprehensive specification generation
- **create-unittest-python.prompt.md** - Python unit test generation
- **format-databricks-ntb.prompt.md** - Databricks notebook formatting
- **format-vscode-ntb.prompt.md** - VS Code notebook formatting
- **write-docstrings.prompt.md** - Generate Python docstrings
- **write-documentation.prompt.md** - Create technical documentation

#### Skills (`/skills`)
- **docstring-python/** - Specialized skill for Python docstring generation
- **brand-guidelines/** - Brand consistency guidelines for generated content

### 📦 Distribution Package (`/dist`)

Complete scaffolding structure ready for import into other projects:

- **.codex/** - OpenAI Codex configuration
- **.github/** - GitHub-specific configurations and prompts
- **.opencode/** - OpenCode AI settings
- **.vscode/** - VS Code extension configuration
- **docs/** - Complete documentation site (MkDocs + mkdocstrings)
- **tests/** - Testing frameworks and test specifications

### 📚 Documentation (`/docs`)

Comprehensive guides covering:
- Getting started tutorials
- How-to guides for common tasks
- API reference documentation
- Example implementations

## Quick Start

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/agentic-dev-env.git
   cd agentic-dev-env
   ```

2. **Copy templates to your project**
   ```bash
   cp -r dist/ /path/to/your/project/
   ```

3. **Configure your AI platform**
   - For GitHub Copilot: Copy `.vscode/` settings
   - For OpenCode: Copy `.opencode/` configuration
   - For Codex: Copy `.codex/` settings
   - For Warp: Integrate prompts into your Warp configuration

### Using Prompts

1. Select a prompt template from `/prompt_templates`
2. Customize variables for your use case
3. Use with your preferred AI platform
4. Version control your custom prompts

## Key Features

✅ **Framework-Agnostic** - Works with multiple AI platforms  
✅ **Pre-built Workflows** - Debug, code review, documentation, specifications  
✅ **Modular Design** - Mix and match prompts and skills  
✅ **Production Ready** - Tested configurations and best practices  
✅ **Well-Documented** - Comprehensive guides and examples  
✅ **Python/ML Focused** - Specialized for data science workflows  
✅ **Easy Integration** - Copy scaffolding to new projects  

## Documentation

- **[Project Guide](./AGENTS.md)** - Overview and project structure
- **[Distribution Docs](./dist/docs/)** - Full documentation site
- **[Examples](./dist/docs/examples/)** - Practical code examples

## Project Structure

```
agentic-dev-env/
├── README.md                 # This file
├── AGENTS.md                 # Project overview & guidelines
├── prompt_templates/         # Source templates
│   ├── agents/              # Agent specifications
│   ├── prompts/             # Standalone prompts
│   └── skills/              # Reusable skill modules
└── dist/                    # Distribution scaffold
    ├── .github/             # GitHub configuration
    ├── .vscode/             # VS Code settings
    ├── .opencode/           # OpenCode AI config
    ├── .codex/              # OpenAI Codex config
    ├── docs/                # Documentation (MkDocs)
    └── tests/               # Test frameworks
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

- **Python 3.8+** (for Python-specific skills)
- **MkDocs + mkdocs-material** (for documentation)
- **Git** (for version control)
- Access to your preferred AI platform (Copilot, OpenCode, Codex, or Warp)

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
