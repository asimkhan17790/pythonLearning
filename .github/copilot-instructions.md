# Copilot Instructions for pythonLearning

## Project Overview

- This codebase is a Python learning playground, organized by topic in `my_modules/basic/` and `my_modules/oops_concepts/`.
- Each file demonstrates a specific Python concept (functions, classes, constructors, inheritance, etc.) with simple, self-contained examples.

## Directory Structure

- `my_modules/basic/`: Foundational Python topics (functions, loops, conditionals, data structures, etc.)
- `my_modules/oops_concepts/`: Object-oriented programming concepts (classes, constructors, inheritance, etc.)
- Each topic is a separate `.py` file, named with a prefix for ordering (e.g., `01_classes.py`).

## Importing Across Modules

- To import between modules, use Python package-style imports (e.g., `from my_modules.oops_concepts.02_constructors import Employee`).
- Always run scripts from the project root using the `-m` flag for correct import resolution:
  ```sh
  python -m my_modules.basic.main
  ```
- Ensure every folder in the import path contains an `__init__.py` file (can be empty).

## Patterns & Conventions

- Each OOP concept is demonstrated in a separate file with a class and example usage at the bottom.
- Function and class names use `snake_case` and `CamelCase` respectively, following Python conventions.
- Docstrings are used for class and method documentation in OOP files.
- No external dependencies; all code is standard Python 3.

## Developer Workflows

- No build step required; run any `.py` file directly or as a module from the project root.
- No test suite or test runner is present; code is validated by running scripts and observing output.
- Linting may be configured via `.pylintrc`.

## Examples

- See `my_modules/oops_concepts/02_constructors.py` for a parameterized constructor pattern.
- See `my_modules/basic/functions.py` for function definitions, lambdas, and recursion.

## Integration Points

- No external APIs or services are integrated.
- No database or persistent storage is used.

## Special Notes

- This project is for learning and experimentation; code is intentionally simple and may not follow production best practices.
- If you add new modules, follow the existing naming and directory conventions for discoverability.
