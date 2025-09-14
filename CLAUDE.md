# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive Python learning repository organized by topic. It contains practical examples and exercises covering Python fundamentals through advanced concepts, with additional specialized modules for web development and AI projects.

## Directory Structure

- `my_modules/basic_concepts/`: Core Python fundamentals (variables, functions, loops, conditionals, data structures)
- `my_modules/advanced_concepts/`: Advanced topics (decorators, magic methods, error handling, functional programming)
- `my_modules/datastructures/`: Data structure implementations and algorithms
- `my_modules/files_handling/`: File I/O operations and handling
- `my_modules/external_modules/`: External library usage and integration
- `my_modules/flask_basic/`: Web development with Flask framework
- `my_modules/ai/`: AI and machine learning related code
- `my_modules/VidSnapAI/`: Video processing AI project

## Common Commands

### Running Python Files
```bash
# Run any Python file directly
python path/to/file.py

# Run as module from project root (preferred for imports)
python -m my_modules.basic_concepts.filename
```

### Linting
```bash
# Lint specific file
pylint path/to/file.py

# Lint entire directory
pylint my_modules/
```

Note: Linting is configured via `.pylintrc` with disabled checks: C0114 (missing-module-docstring), C0115 (missing-class-docstring), C0116 (missing-function-docstring).

### Dependencies
Some modules have their own requirements:
- `my_modules/external_modules/requirements.txt`
- `my_modules/flask_basic/requirements.txt`
- `my_modules/VidSnapAI/requirements.txt`

Install dependencies for specific modules as needed:
```bash
pip install -r my_modules/flask_basic/requirements.txt
```

## Module Import Patterns

- Use Python package-style imports: `from my_modules.basic_concepts.filename import ClassName`
- Always run scripts from project root for proper import resolution
- Each directory contains `__init__.py` files for package structure
- No external dependencies in basic/advanced concept modules - pure Python 3

## Code Architecture

- **Learning-focused**: Each file demonstrates a specific concept with self-contained examples
- **Progressive complexity**: Basic concepts → Advanced concepts → Specialized applications
- **Modular design**: Topics separated into individual files with descriptive naming (e.g., `01_classes.py`)
- **Example-driven**: Each concept includes practical usage examples at the bottom of files
- **No production patterns**: Code prioritizes clarity and learning over production best practices

## Development Notes

- No build process required - direct Python execution
- No formal test suite - validation through running examples and observing output
- Files use standard Python naming conventions (snake_case functions, CamelCase classes)
- Flask applications in `flask_basic/` follow standard Flask project structure with static/ and templates/ directories