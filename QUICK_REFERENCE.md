# Quick Reference Card

## Build Commands

```bash
./build.sh                     # Build all targets
./build.sh --target .github    # Build specific target
./build.sh --clean             # Clean and rebuild
```

## Directory Structure

```
src/base/              → Shared content (all targets)
src/targets/           → Target-specific overrides
src/templates/         → Reusable Jinja2 templates
dist/                  → Generated output (70 files)
```

## Template Usage

### Create Template
```bash
# Create in src/templates/
echo "## My Guidelines" > src/templates/my_guide.md
```

### Use Template
```markdown
<!-- In any .md file under src/base/ or src/targets/ -->
{% include "my_guide.md" %}
```

### Build
```bash
./build.sh
```

## File Naming Rules

### Base Files (src/base/)
- No suffix: `debug.md`, `test.md`
- Build adds suffix per target

### Target Files (src/targets/)
- Include suffix: `debug.agent.md`, `test.prompt.md`
- No transformation

## Folder Mappings

| Base Folder   | .github      | .opencode  | .codex     |
|---------------|--------------|------------|------------|
| skills/       | skills/      | skill/     | skills/    |
| agents/       | agents/      | agent/     | agents/    |
| prompts/      | prompts/     | command/   | prompts/   |
| instructions/ | instructions/| (none)     | (none)     |

## File Suffixes

| Base Folder   | .github          | .opencode | .codex |
|---------------|------------------|-----------|--------|
| agents/       | .agent.md        | .md       | .md    |
| prompts/      | .prompt.md       | .md       | .md    |
| instructions/ | .instructions.md | -         | -      |
| skills/       | .md              | .md       | .md    |

## Common Tasks

### Add shared prompt
```bash
# 1. Create in base
vim src/base/prompts/my-prompt.md

# 2. Build
./build.sh

# 3. Appears in all targets:
# - dist/.github/prompts/my-prompt.prompt.md
# - dist/.opencode/command/my-prompt.md
# - dist/.codex/prompts/my-prompt.md
```

### Override for specific target
```bash
# 1. Create target-specific version
vim src/targets/.github/prompts/my-prompt.prompt.md

# 2. Build
./build.sh

# 3. Target version takes precedence for .github
```

### Share content via template
```bash
# 1. Create template
vim src/templates/shared_content.md

# 2. Include in files
echo "{% include 'shared_content.md' %}" >> src/base/prompts/test.md

# 3. Build
./build.sh
```

## Troubleshooting

### Template not found
```
⚠️ Template not found: my_template.md
```
**Fix:** Create `src/templates/my_template.md`

### Build fails
```bash
# Check Python/uv setup
uv sync

# Try clean rebuild
./build.sh --clean
```

### Changes not appearing
```bash
# Rebuild to apply changes
./build.sh --clean
```

## Documentation

- **Full Guide:** [AGENTS.md](./AGENTS.md)
- **Template Guide:** [TEMPLATE_GUIDE.md](./TEMPLATE_GUIDE.md)
- **Configuration:** [build_config.yaml](./build_config.yaml)

---
**Version:** 0.1.0 | **Build System:** Python + Jinja2 + uv
