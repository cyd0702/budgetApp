---
name: csv-budget-cli
description: Python CSV-based CLI budget app workflow, including TDD implementation, test-first development, refactoring, and pre-commit quality review. Use when working in this repository on transaction handling, CSV loading, summaries, filtering, or other CLI budget app changes.
---

# CSV Budget CLI

Use this skill when working on the budget app in this repository.

## Workflow

1. Start from a test.
2. Implement the smallest change that makes the test pass.
3. Refactor while keeping complexity low.
4. Run `pytest`.
5. Run `radon cc`.
6. Ask `qa_engineer` to review before commit.

## Rules

- Use type hints everywhere that matters.
- Keep functions short and focused.
- Prefer explicit CSV parsing and clear data transformations.
- Keep cyclomatic complexity at or below 10.
- Treat CSV-backed behavior as the source of truth.

## When modifying behavior

- Add or update tests first.
- Prefer narrow helpers over broad rewrites.
- Keep output and data shape stable unless the task explicitly changes them.
