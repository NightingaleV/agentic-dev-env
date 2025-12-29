---
agent: 'agent'
tools: ['vscode/runCommand', 'execute', 'read', 'edit', 'search', 'web', 'agent', 'memory', 'ms-vscode.vscode-websearchforcopilot/websearch', 'todo']
description: 'Convert python script to follow databricks notebook format with markdown cells and code cells.'
---

Take following code and write module docstring, class docstring and also docstring for each method. Use google docstring conventions, but dont use types inside docstrings as we use typehints.

Write readable and telling information in docstring. When you are at it, you can slightly clean the code and polish the comments. Dont do changes to code structure or logic, just cleaning and making things more readable and up to production standards.