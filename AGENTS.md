# AGENTS.md

## Project Overview
- This repository is a Python CLI budget app that manages transactions stored in CSV files.
- The app should stay simple, scriptable, and testable.

## Coding Rules
- Always use type hints for functions, methods, and public data structures.
- Keep each function at 50 lines or less.
- Prefer small, single-purpose helpers over large blocks of logic.

## TDD Rules
- Write the test first before implementing any behavior.
- Red, green, refactor is the default workflow.
- Do not merge or commit behavior changes that are not covered by tests.

## Quality Rules
- Keep cyclomatic complexity at 10 or lower.
- If a function starts getting complex, split it before adding more logic.

## Quality Review Rules
- Before every commit, run a quality check through the `qa_engineer` subagent.
- Do not consider work complete until the subagent review is addressed.

## Test Commands
- Run tests with `pytest`.
- Check cyclomatic complexity with `radon cc`.

## Commit Rules
- Commit once a single feature is implemented.
- Push after the feature commit is complete.
