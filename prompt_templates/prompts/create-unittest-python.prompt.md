---
agent: "agent"
description: "Interview the tech lead with clarifying questions, then produce a clear Jira task for a data science team."
tools: ['vscode/runCommand', 'execute/testFailure', 'execute/getTerminalOutput', 'execute/runTask', 'execute/getTaskOutput', 'execute/createAndRunTask', 'execute/runInTerminal', 'execute/runTests', 'read', 'edit/createDirectory', 'edit/createFile', 'edit/editFiles', 'search', 'web', 'agent', 'ms-python.python/getPythonEnvironmentInfo', 'ms-python.python/getPythonExecutableCommand', 'ms-python.python/installPythonPackage', 'todo']
---


# Generate Unit Tests for a Component

Generate a set of unit tests for the component named `$COMPONENT_NAME`. 

Ensure that the tests cover critical functionalities and edge cases of the component. Use appropriate testing frameworks and best practices for writing unit tests.