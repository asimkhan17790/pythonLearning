"""
Python Packaging and Distribution Tutorial
==========================================

This module demonstrates how to:
- Create Python packages
- Structure package directories
- Write setup.py and pyproject.toml
- Build and distribute packages
- Upload to PyPI
- Install packages with pip
- Create virtual environments
- Manage dependencies
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import json


def create_sample_package_structure():
    """Create a complete sample package structure"""
    print("=" * 60)
    print("CREATING SAMPLE PACKAGE STRUCTURE")
    print("=" * 60)

    # Define package structure
    package_name = "awesome_calculator"
    base_dir = Path(f"{package_name}_demo")

    # Create directory structure
    structure = {
        base_dir: None,
        base_dir / package_name: None,
        base_dir / package_name / "core": None,
        base_dir / package_name / "utils": None,
        base_dir / "tests": None,
        base_dir / "docs": None,
        base_dir / "examples": None,
    }

    print(f"\n1. Creating package directory structure for '{package_name}':")

    try:
        # Create directories
        for directory in structure.keys():
            directory.mkdir(parents=True, exist_ok=True)
            print(f"   ✅ Created: {directory}")

        # Create package files
        create_package_files(base_dir, package_name)

        print(f"\n✅ Package structure created successfully!")
        return base_dir

    except Exception as e:
        print(f"❌ Failed to create package structure: {e}")
        return None


def create_package_files(base_dir: Path, package_name: str):
    """Create all necessary package files"""

    print(f"\n2. Creating package files:")

    # 1. Main package __init__.py
    init_py_content = f'''"""
{package_name} - An awesome calculator package

A comprehensive calculator package with basic arithmetic,
scientific functions, and utility operations.
"""

__version__ = "1.0.0"
__author__ = "Python Developer"
__email__ = "developer@example.com"
__description__ = "An awesome calculator package for Python"

# Import main classes and functions for easy access
from .core.calculator import Calculator
from .core.scientific import ScientificCalculator
from .utils.formatters import format_result, format_currency
from .utils.validators import validate_number, validate_operation

# Define what gets imported with "from awesome_calculator import *"
__all__ = [
    "Calculator",
    "ScientificCalculator",
    "format_result",
    "format_currency",
    "validate_number",
    "validate_operation",
]

# Package initialization
print(f"{{package_name}} v{{__version__}} loaded successfully!")
'''

    with open(base_dir / package_name / "__init__.py", "w") as f:
        f.write(init_py_content)
    print("   ✅ Created: __init__.py")

    # 2. Core calculator module
    calculator_py_content = '''"""
Core calculator functionality
"""

from typing import Union, List, Optional
from ..utils.validators import validate_number


class Calculator:
    """Basic calculator with arithmetic operations"""

    def __init__(self):
        self.history: List[str] = []
        self.memory = 0.0

    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        validate_number(a, "first operand")
        validate_number(b, "second operand")
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers"""
        validate_number(a, "first operand")
        validate_number(b, "second operand")
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        validate_number(a, "first operand")
        validate_number(b, "second operand")
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers"""
        validate_number(a, "dividend")
        validate_number(b, "divisor")
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        """Raise base to the power of exponent"""
        validate_number(base, "base")
        validate_number(exponent, "exponent")
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def get_history(self) -> List[str]:
        """Get calculation history"""
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear calculation history"""
        self.history.clear()

    def memory_store(self, value: float) -> None:
        """Store value in memory"""
        validate_number(value, "memory value")
        self.memory = value

    def memory_recall(self) -> float:
        """Recall value from memory"""
        return self.memory

    def memory_clear(self) -> None:
        """Clear memory"""
        self.memory = 0.0
'''

    # Create core directory files
    core_dir = base_dir / package_name / "core"
    with open(core_dir / "__init__.py", "w") as f:
        f.write('"""Core calculator functionality"""\\n')
    print("   ✅ Created: core/__init__.py")

    with open(core_dir / "calculator.py", "w") as f:
        f.write(calculator_py_content)
    print("   ✅ Created: core/calculator.py")

    # 3. Scientific calculator module
    scientific_py_content = '''"""
Scientific calculator with advanced mathematical functions
"""

import math
from typing import Union
from .calculator import Calculator
from ..utils.validators import validate_number


class ScientificCalculator(Calculator):
    """Scientific calculator extending basic calculator"""

    def sin(self, angle: float, degrees: bool = False) -> float:
        """Calculate sine of angle"""
        validate_number(angle, "angle")
        if degrees:
            angle = math.radians(angle)
        result = math.sin(angle)
        unit = "°" if degrees else "rad"
        self.history.append(f"sin({angle}{unit}) = {result}")
        return result

    def cos(self, angle: float, degrees: bool = False) -> float:
        """Calculate cosine of angle"""
        validate_number(angle, "angle")
        if degrees:
            angle = math.radians(angle)
        result = math.cos(angle)
        unit = "°" if degrees else "rad"
        self.history.append(f"cos({angle}{unit}) = {result}")
        return result

    def tan(self, angle: float, degrees: bool = False) -> float:
        """Calculate tangent of angle"""
        validate_number(angle, "angle")
        if degrees:
            angle = math.radians(angle)
        result = math.tan(angle)
        unit = "°" if degrees else "rad"
        self.history.append(f"tan({angle}{unit}) = {result}")
        return result

    def log(self, x: float, base: float = math.e) -> float:
        """Calculate logarithm"""
        validate_number(x, "argument")
        validate_number(base, "base")
        if x <= 0:
            raise ValueError("Logarithm argument must be positive")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")

        if base == math.e:
            result = math.log(x)
            self.history.append(f"ln({x}) = {result}")
        else:
            result = math.log(x, base)
            self.history.append(f"log_{base}({x}) = {result}")
        return result

    def sqrt(self, x: float) -> float:
        """Calculate square root"""
        validate_number(x, "argument")
        if x < 0:
            raise ValueError("Square root of negative number is not real")
        result = math.sqrt(x)
        self.history.append(f"√{x} = {result}")
        return result

    def factorial(self, n: int) -> int:
        """Calculate factorial"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial argument must be a non-negative integer")
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result
'''

    with open(core_dir / "scientific.py", "w") as f:
        f.write(scientific_py_content)
    print("   ✅ Created: core/scientific.py")

    # 4. Utils modules
    utils_dir = base_dir / package_name / "utils"
    with open(utils_dir / "__init__.py", "w") as f:
        f.write('"""Utility functions for the calculator package"""\\n')
    print("   ✅ Created: utils/__init__.py")

    # Validators module
    validators_py_content = '''"""
Input validation utilities
"""

from typing import Union


def validate_number(value: Union[int, float], name: str = "value") -> None:
    """Validate that a value is a number"""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number, got {type(value).__name__}")

    if isinstance(value, float) and (value != value):  # Check for NaN
        raise ValueError(f"{name} cannot be NaN")


def validate_operation(operation: str) -> bool:
    """Validate calculator operation"""
    valid_operations = {"+", "-", "*", "/", "**", "sin", "cos", "tan", "log", "sqrt"}
    return operation in valid_operations


def validate_range(value: float, min_val: float = None, max_val: float = None, name: str = "value") -> None:
    """Validate that a number is within a specified range"""
    validate_number(value, name)

    if min_val is not None and value < min_val:
        raise ValueError(f"{name} must be >= {min_val}, got {value}")

    if max_val is not None and value > max_val:
        raise ValueError(f"{name} must be <= {max_val}, got {value}")
'''

    with open(utils_dir / "validators.py", "w") as f:
        f.write(validators_py_content)
    print("   ✅ Created: utils/validators.py")

    # Formatters module
    formatters_py_content = '''"""
Output formatting utilities
"""

from typing import Union
from decimal import Decimal, ROUND_HALF_UP


def format_result(value: Union[int, float], precision: int = 2) -> str:
    """Format calculation result with specified precision"""
    if isinstance(value, int):
        return str(value)

    # Use Decimal for precise rounding
    decimal_value = Decimal(str(value))
    rounded = decimal_value.quantize(Decimal(f'1E-{precision}'), rounding=ROUND_HALF_UP)

    # Remove trailing zeros
    formatted = str(rounded).rstrip('0').rstrip('.')
    return formatted if formatted else '0'


def format_currency(amount: float, currency: str = "$", precision: int = 2) -> str:
    """Format number as currency"""
    formatted_amount = format_result(amount, precision)
    return f"{currency}{formatted_amount}"


def format_percentage(value: float, precision: int = 2) -> str:
    """Format number as percentage"""
    percentage = value * 100
    formatted = format_result(percentage, precision)
    return f"{formatted}%"


def format_scientific(value: float, precision: int = 2) -> str:
    """Format number in scientific notation"""
    return f"{value:.{precision}e}"
'''

    with open(utils_dir / "formatters.py", "w") as f:
        f.write(formatters_py_content)
    print("   ✅ Created: utils/formatters.py")

    # 5. Create setup.py
    create_setup_files(base_dir, package_name)

    # 6. Create tests
    create_test_files(base_dir, package_name)

    # 7. Create documentation files
    create_documentation_files(base_dir, package_name)

    # 8. Create example files
    create_example_files(base_dir, package_name)


def create_setup_files(base_dir: Path, package_name: str):
    """Create setup and configuration files"""

    print(f"\n3. Creating setup and configuration files:")

    # 1. setup.py (traditional approach)
    setup_py_content = f'''"""
Setup script for {package_name}
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
def read_requirements(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        return []

setup(
    name="{package_name}",
    version="1.0.0",
    author="Python Developer",
    author_email="developer@example.com",
    description="An awesome calculator package for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/{package_name}",
    project_urls={{
        "Bug Reports": "https://github.com/yourusername/{package_name}/issues",
        "Source": "https://github.com/yourusername/{package_name}",
        "Documentation": "https://awesome-calculator.readthedocs.io/",
    }},
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements("requirements.txt"),
    extras_require={{
        "dev": read_requirements("requirements-dev.txt"),
        "test": ["pytest>=7.0", "pytest-cov>=4.0"],
        "docs": ["sphinx>=5.0", "sphinx-rtd-theme>=1.0"],
    }},
    entry_points={{
        "console_scripts": [
            "{package_name}={package_name}.cli:main",
        ],
    }},
    include_package_data=True,
    package_data={{
        "{package_name}": ["data/*.json", "templates/*.txt"],
    }},
    keywords="calculator mathematics arithmetic scientific",
    zip_safe=False,
)
'''

    with open(base_dir / "setup.py", "w") as f:
        f.write(setup_py_content)
    print("   ✅ Created: setup.py")

    # 2. pyproject.toml (modern approach)
    pyproject_toml_content = f'''[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "{package_name}"
version = "1.0.0"
description = "An awesome calculator package for Python"
readme = "README.md"
license = {{file = "LICENSE"}}
authors = [
    {{name = "Python Developer", email = "developer@example.com"}},
]
maintainers = [
    {{name = "Python Developer", email = "developer@example.com"}},
]
keywords = ["calculator", "mathematics", "arithmetic", "scientific"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering :: Mathematics",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
requires-python = ">=3.8"
dependencies = [
    # Add your dependencies here
    # "requests>=2.28.0",
    # "click>=8.0.0",
]

[project.optional-dependencies]
dev = [
    "black>=22.0",
    "isort>=5.0",
    "flake8>=5.0",
    "mypy>=1.0",
    "pre-commit>=2.0",
]
test = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "pytest-mock>=3.0",
]
docs = [
    "sphinx>=5.0",
    "sphinx-rtd-theme>=1.0",
    "myst-parser>=0.18",
]

[project.urls]
Homepage = "https://github.com/yourusername/{package_name}"
Documentation = "https://awesome-calculator.readthedocs.io/"
Repository = "https://github.com/yourusername/{package_name}.git"
"Bug Reports" = "https://github.com/yourusername/{package_name}/issues"
Changelog = "https://github.com/yourusername/{package_name}/blob/main/CHANGELOG.md"

[project.scripts]
{package_name} = "{package_name}.cli:main"

[tool.setuptools]
package-dir = {{"{package_name}" = "{package_name}"}}

[tool.setuptools.packages.find]
include = ["{package_name}*"]
exclude = ["tests*"]

[tool.black]
line-length = 88
target-version = ['py38']
include = '\\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "--cov={package_name} --cov-report=html --cov-report=term-missing"
'''

    with open(base_dir / "pyproject.toml", "w") as f:
        f.write(pyproject_toml_content)
    print("   ✅ Created: pyproject.toml")

    # 3. MANIFEST.in
    manifest_content = '''include README.md
include LICENSE
include CHANGELOG.md
include requirements*.txt
recursive-include awesome_calculator/data *.json
recursive-include awesome_calculator/templates *.txt
recursive-exclude tests *
recursive-exclude * __pycache__
recursive-exclude * *.py[co]
'''

    with open(base_dir / "MANIFEST.in", "w") as f:
        f.write(manifest_content)
    print("   ✅ Created: MANIFEST.in")

    # 4. Requirements files
    requirements_content = '''# Core dependencies
# Add your package dependencies here
# requests>=2.28.0
# click>=8.0.0
'''

    with open(base_dir / "requirements.txt", "w") as f:
        f.write(requirements_content)
    print("   ✅ Created: requirements.txt")

    requirements_dev_content = '''# Development dependencies
black>=22.0
isort>=5.0
flake8>=5.0
mypy>=1.0
pre-commit>=2.0
pytest>=7.0
pytest-cov>=4.0
pytest-mock>=3.0
sphinx>=5.0
sphinx-rtd-theme>=1.0
twine>=4.0
build>=0.8.0
'''

    with open(base_dir / "requirements-dev.txt", "w") as f:
        f.write(requirements_dev_content)
    print("   ✅ Created: requirements-dev.txt")


def create_test_files(base_dir: Path, package_name: str):
    """Create test files"""

    print(f"\n4. Creating test files:")

    tests_dir = base_dir / "tests"

    # Test __init__.py
    with open(tests_dir / "__init__.py", "w") as f:
        f.write("")
    print("   ✅ Created: tests/__init__.py")

    # Test calculator
    test_calculator_content = f'''"""
Tests for the Calculator class
"""

import pytest
from {package_name}.core.calculator import Calculator


class TestCalculator:
    """Test cases for Calculator class"""

    def setup_method(self):
        """Setup test calculator instance"""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation"""
        result = self.calc.add(2, 3)
        assert result == 5
        assert "2 + 3 = 5" in self.calc.get_history()

    def test_subtract(self):
        """Test subtraction operation"""
        result = self.calc.subtract(10, 4)
        assert result == 6
        assert "10 - 4 = 6" in self.calc.get_history()

    def test_multiply(self):
        """Test multiplication operation"""
        result = self.calc.multiply(6, 7)
        assert result == 42
        assert "6 × 7 = 42" in self.calc.get_history()

    def test_divide(self):
        """Test division operation"""
        result = self.calc.divide(15, 3)
        assert result == 5
        assert "15 ÷ 3 = 5" in self.calc.get_history()

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Division by zero is not allowed"):
            self.calc.divide(10, 0)

    def test_power(self):
        """Test power operation"""
        result = self.calc.power(2, 3)
        assert result == 8
        assert "2 ^ 3 = 8" in self.calc.get_history()

    def test_memory_operations(self):
        """Test memory store, recall, and clear"""
        self.calc.memory_store(42)
        assert self.calc.memory_recall() == 42

        self.calc.memory_clear()
        assert self.calc.memory_recall() == 0

    def test_history_operations(self):
        """Test history functionality"""
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)

        history = self.calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history
        assert "3 × 4 = 12" in history

        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0

    def test_invalid_input_types(self):
        """Test invalid input types raise TypeError"""
        with pytest.raises(TypeError):
            self.calc.add("2", 3)

        with pytest.raises(TypeError):
            self.calc.multiply(2, "3")
'''

    with open(tests_dir / "test_calculator.py", "w") as f:
        f.write(test_calculator_content)
    print("   ✅ Created: tests/test_calculator.py")

    # Test scientific calculator
    test_scientific_content = f'''"""
Tests for the ScientificCalculator class
"""

import math
import pytest
from {package_name}.core.scientific import ScientificCalculator


class TestScientificCalculator:
    """Test cases for ScientificCalculator class"""

    def setup_method(self):
        """Setup test scientific calculator instance"""
        self.calc = ScientificCalculator()

    def test_inheritance(self):
        """Test that ScientificCalculator inherits from Calculator"""
        # Should have basic calculator functionality
        result = self.calc.add(2, 3)
        assert result == 5

    def test_sin(self):
        """Test sine function"""
        result = self.calc.sin(math.pi / 2)
        assert abs(result - 1.0) < 1e-10

        result_degrees = self.calc.sin(90, degrees=True)
        assert abs(result_degrees - 1.0) < 1e-10

    def test_cos(self):
        """Test cosine function"""
        result = self.calc.cos(0)
        assert abs(result - 1.0) < 1e-10

        result_degrees = self.calc.cos(0, degrees=True)
        assert abs(result_degrees - 1.0) < 1e-10

    def test_tan(self):
        """Test tangent function"""
        result = self.calc.tan(math.pi / 4)
        assert abs(result - 1.0) < 1e-10

        result_degrees = self.calc.tan(45, degrees=True)
        assert abs(result_degrees - 1.0) < 1e-10

    def test_log_natural(self):
        """Test natural logarithm"""
        result = self.calc.log(math.e)
        assert abs(result - 1.0) < 1e-10

    def test_log_base_10(self):
        """Test logarithm base 10"""
        result = self.calc.log(100, 10)
        assert abs(result - 2.0) < 1e-10

    def test_log_invalid_arguments(self):
        """Test logarithm with invalid arguments"""
        with pytest.raises(ValueError, match="Logarithm argument must be positive"):
            self.calc.log(-1)

        with pytest.raises(ValueError, match="Logarithm base must be positive"):
            self.calc.log(10, -1)

        with pytest.raises(ValueError, match="not equal to 1"):
            self.calc.log(10, 1)

    def test_sqrt(self):
        """Test square root function"""
        result = self.calc.sqrt(16)
        assert result == 4

        result = self.calc.sqrt(2)
        assert abs(result - math.sqrt(2)) < 1e-10

    def test_sqrt_negative(self):
        """Test square root of negative number"""
        with pytest.raises(ValueError, match="Square root of negative number"):
            self.calc.sqrt(-1)

    def test_factorial(self):
        """Test factorial function"""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120

    def test_factorial_invalid(self):
        """Test factorial with invalid arguments"""
        with pytest.raises(ValueError, match="non-negative integer"):
            self.calc.factorial(-1)

        with pytest.raises(ValueError, match="non-negative integer"):
            self.calc.factorial(3.14)
'''

    with open(tests_dir / "test_scientific.py", "w") as f:
        f.write(test_scientific_content)
    print("   ✅ Created: tests/test_scientific.py")

    # pytest.ini
    pytest_ini_content = '''[tool:pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --tb=short
    --cov=awesome_calculator
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80
'''

    with open(tests_dir / "pytest.ini", "w") as f:
        f.write(pytest_ini_content)
    print("   ✅ Created: tests/pytest.ini")


def create_documentation_files(base_dir: Path, package_name: str):
    """Create documentation files"""

    print(f"\n5. Creating documentation files:")

    # README.md
    readme_content = f'''# {package_name.replace("_", " ").title()}

An awesome calculator package for Python with basic arithmetic and scientific functions.

## Features

- ✅ Basic arithmetic operations (add, subtract, multiply, divide, power)
- ✅ Scientific functions (trigonometry, logarithms, square root, factorial)
- ✅ Memory operations (store, recall, clear)
- ✅ Calculation history
- ✅ Input validation and error handling
- ✅ Result formatting utilities
- ✅ Comprehensive type hints
- ✅ 100% test coverage

## Installation

### From PyPI (when published)
```bash
pip install {package_name}
```

### From source
```bash
git clone https://github.com/yourusername/{package_name}.git
cd {package_name}
pip install -e .
```

### Development installation
```bash
git clone https://github.com/yourusername/{package_name}.git
cd {package_name}
pip install -e ".[dev]"
```

## Quick Start

### Basic Calculator

```python
from {package_name} import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)        # 8
result = calc.multiply(4, 6)   # 24
result = calc.divide(15, 3)    # 5.0

# View calculation history
history = calc.get_history()
print(history)  # ['5 + 3 = 8', '4 × 6 = 24', '15 ÷ 3 = 5']

# Memory operations
calc.memory_store(42)
value = calc.memory_recall()   # 42
```

### Scientific Calculator

```python
from {package_name} import ScientificCalculator
import math

calc = ScientificCalculator()

# All basic calculator functions plus:
result = calc.sin(math.pi / 2)     # 1.0
result = calc.cos(0)               # 1.0
result = calc.log(10, base=10)     # 1.0
result = calc.sqrt(16)             # 4.0
result = calc.factorial(5)         # 120
```

### Formatting Utilities

```python
from {package_name} import format_result, format_currency

# Format results
formatted = format_result(3.14159, precision=2)  # "3.14"
currency = format_currency(29.99)                # "$29.99"
```

## Command Line Interface

After installation, you can use the calculator from the command line:

```bash
{package_name} --help
```

## API Reference

### Calculator Class

#### Methods

- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers (raises ValueError for division by zero)
- `power(base, exponent)` - Raise base to the power of exponent
- `get_history()` - Get list of calculation history
- `clear_history()` - Clear calculation history
- `memory_store(value)` - Store value in memory
- `memory_recall()` - Recall value from memory
- `memory_clear()` - Clear memory

### ScientificCalculator Class

Inherits all methods from Calculator plus:

- `sin(angle, degrees=False)` - Calculate sine
- `cos(angle, degrees=False)` - Calculate cosine
- `tan(angle, degrees=False)` - Calculate tangent
- `log(x, base=e)` - Calculate logarithm
- `sqrt(x)` - Calculate square root
- `factorial(n)` - Calculate factorial

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/yourusername/{package_name}.git
cd {package_name}

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### Running tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov={package_name}

# Run specific test file
pytest tests/test_calculator.py
```

### Code formatting

```bash
# Format code
black {package_name}/ tests/

# Sort imports
isort {package_name}/ tests/

# Type checking
mypy {package_name}/
```

### Building the package

```bash
# Build distribution packages
python -m build

# Upload to PyPI (test)
python -m twine upload --repository testpypi dist/*

# Upload to PyPI (production)
python -m twine upload dist/*
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass (`pytest`)
6. Commit your changes (`git commit -am 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

## Support

- 📧 Email: developer@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/{package_name}/issues)
- 📖 Documentation: [Read the Docs](https://awesome-calculator.readthedocs.io/)

## Acknowledgments

- Thanks to the Python community for inspiration
- Built with love and Python 🐍
'''

    with open(base_dir / "README.md", "w") as f:
        f.write(readme_content)
    print("   ✅ Created: README.md")

    # LICENSE
    license_content = '''MIT License

Copyright (c) 2024 Python Developer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

    with open(base_dir / "LICENSE", "w") as f:
        f.write(license_content)
    print("   ✅ Created: LICENSE")

    # CHANGELOG.md
    changelog_content = '''# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Nothing yet

### Changed
- Nothing yet

### Deprecated
- Nothing yet

### Removed
- Nothing yet

### Fixed
- Nothing yet

### Security
- Nothing yet

## [1.0.0] - 2024-01-15

### Added
- Initial release
- Basic calculator functionality (add, subtract, multiply, divide, power)
- Scientific calculator functionality (trigonometry, logarithms, square root, factorial)
- Memory operations (store, recall, clear)
- Calculation history
- Input validation and error handling
- Result formatting utilities
- Comprehensive test suite
- Type hints throughout codebase
- Command-line interface
- Documentation and examples

### Changed
- Nothing (initial release)

### Fixed
- Nothing (initial release)
'''

    with open(base_dir / "CHANGELOG.md", "w") as f:
        f.write(changelog_content)
    print("   ✅ Created: CHANGELOG.md")


def create_example_files(base_dir: Path, package_name: str):
    """Create example files"""

    print(f"\n6. Creating example files:")

    examples_dir = base_dir / "examples"

    # Basic usage example
    basic_example_content = f'''#!/usr/bin/env python3
"""
Basic Calculator Usage Example

This example demonstrates the basic functionality of the {package_name} package.
"""

from {package_name} import Calculator, format_result

def main():
    print("=== Basic Calculator Example ===\\n")

    # Create calculator instance
    calc = Calculator()

    # Perform calculations
    print("Performing basic calculations:")
    result1 = calc.add(15, 25)
    print(f"15 + 25 = {{result1}}")

    result2 = calc.multiply(7, 8)
    print(f"7 × 8 = {{result2}}")

    result3 = calc.divide(100, 4)
    print(f"100 ÷ 4 = {{result3}}")

    result4 = calc.power(2, 10)
    print(f"2^10 = {{result4}}")

    # Memory operations
    print("\\nMemory operations:")
    calc.memory_store(42)
    print("Stored 42 in memory")

    remembered = calc.memory_recall()
    print(f"Recalled from memory: {{remembered}}")

    # Calculation history
    print("\\nCalculation history:")
    history = calc.get_history()
    for i, calculation in enumerate(history, 1):
        print(f"{{i}}. {{calculation}}")

    # Formatted results
    print("\\nFormatted results:")
    pi_approx = 22 / 7
    formatted = format_result(pi_approx, precision=4)
    print(f"22/7 = {{formatted}}")

    print("\\n=== Example completed ===")

if __name__ == "__main__":
    main()
'''

    with open(examples_dir / "basic_usage.py", "w") as f:
        f.write(basic_example_content)
    print("   ✅ Created: examples/basic_usage.py")

    # Scientific calculator example
    scientific_example_content = f'''#!/usr/bin/env python3
"""
Scientific Calculator Usage Example

This example demonstrates the scientific functionality of the {package_name} package.
"""

import math
from {package_name} import ScientificCalculator, format_result

def main():
    print("=== Scientific Calculator Example ===\\n")

    # Create scientific calculator instance
    calc = ScientificCalculator()

    # Trigonometric functions
    print("Trigonometric functions:")

    # Using radians
    sin_pi_2 = calc.sin(math.pi / 2)
    print(f"sin(π/2) = {{format_result(sin_pi_2, 6)}}")

    cos_0 = calc.cos(0)
    print(f"cos(0) = {{format_result(cos_0, 6)}}")

    # Using degrees
    sin_90 = calc.sin(90, degrees=True)
    print(f"sin(90°) = {{format_result(sin_90, 6)}}")

    tan_45 = calc.tan(45, degrees=True)
    print(f"tan(45°) = {{format_result(tan_45, 6)}}")

    # Logarithmic functions
    print("\\nLogarithmic functions:")

    ln_e = calc.log(math.e)
    print(f"ln(e) = {{format_result(ln_e, 6)}}")

    log10_100 = calc.log(100, 10)
    print(f"log₁₀(100) = {{format_result(log10_100, 6)}}")

    log2_8 = calc.log(8, 2)
    print(f"log₂(8) = {{format_result(log2_8, 6)}}")

    # Square roots
    print("\\nSquare roots:")
    sqrt_16 = calc.sqrt(16)
    print(f"√16 = {{format_result(sqrt_16, 6)}}")

    sqrt_2 = calc.sqrt(2)
    print(f"√2 = {{format_result(sqrt_2, 6)}}")

    # Factorials
    print("\\nFactorials:")
    fact_5 = calc.factorial(5)
    print(f"5! = {{fact_5}}")

    fact_10 = calc.factorial(10)
    print(f"10! = {{fact_10:,}}")

    # Combined operations (scientific calculator also has basic operations)
    print("\\nCombined operations:")

    # Calculate area of circle: A = π * r²
    radius = 5
    area = calc.multiply(math.pi, calc.power(radius, 2))
    print(f"Area of circle (r={{radius}}): {{format_result(area, 2)}}")

    # Calculate hypotenuse: c = √(a² + b²)
    a, b = 3, 4
    c_squared = calc.add(calc.power(a, 2), calc.power(b, 2))
    hypotenuse = calc.sqrt(c_squared)
    print(f"Hypotenuse of triangle ({{a}}, {{b}}): {{format_result(hypotenuse, 2)}}")

    # Calculation history
    print("\\nCalculation history (last 10):")
    history = calc.get_history()
    for i, calculation in enumerate(history[-10:], 1):
        print(f"{{i:2}}. {{calculation}}")

    print("\\n=== Scientific example completed ===")

if __name__ == "__main__":
    main()
'''

    with open(examples_dir / "scientific_usage.py", "w") as f:
        f.write(scientific_example_content)
    print("   ✅ Created: examples/scientific_usage.py")


def demonstrate_packaging_commands():
    """Demonstrate packaging and distribution commands"""
    print("\n" + "=" * 60)
    print("PACKAGING AND DISTRIBUTION COMMANDS")
    print("=" * 60)

    print("\\n1. Setting up development environment:")
    print("   # Create virtual environment")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # Linux/Mac")
    print("   venv\\\\Scripts\\\\activate     # Windows")
    print("")
    print("   # Install development dependencies")
    print("   pip install -e '.[dev]'")

    print("\\n2. Testing your package:")
    print("   # Run tests")
    print("   pytest")
    print("")
    print("   # Run tests with coverage")
    print("   pytest --cov=awesome_calculator --cov-report=html")
    print("")
    print("   # Type checking")
    print("   mypy awesome_calculator/")

    print("\\n3. Code quality:")
    print("   # Format code")
    print("   black awesome_calculator/ tests/")
    print("")
    print("   # Sort imports")
    print("   isort awesome_calculator/ tests/")
    print("")
    print("   # Linting")
    print("   flake8 awesome_calculator/")

    print("\\n4. Building the package:")
    print("   # Install build tools")
    print("   pip install build twine")
    print("")
    print("   # Clean previous builds")
    print("   rm -rf build/ dist/ *.egg-info/")
    print("")
    print("   # Build package")
    print("   python -m build")
    print("")
    print("   # This creates:")
    print("   # dist/awesome_calculator-1.0.0.tar.gz (source distribution)")
    print("   # dist/awesome_calculator-1.0.0-py3-none-any.whl (wheel)")

    print("\\n5. Testing the built package:")
    print("   # Install from wheel")
    print("   pip install dist/awesome_calculator-1.0.0-py3-none-any.whl")
    print("")
    print("   # Test import")
    print("   python -c \\"import awesome_calculator; print('Success!')\\"")

    print("\\n6. Uploading to PyPI:")
    print("   # Check package")
    print("   twine check dist/*")
    print("")
    print("   # Upload to Test PyPI first")
    print("   twine upload --repository testpypi dist/*")
    print("")
    print("   # Test installation from Test PyPI")
    print("   pip install --index-url https://test.pypi.org/simple/ awesome-calculator")
    print("")
    print("   # Upload to real PyPI")
    print("   twine upload dist/*")

    print("\\n7. Local installation methods:")
    print("   # Install in editable/development mode")
    print("   pip install -e .")
    print("")
    print("   # Install from local directory")
    print("   pip install /path/to/package/")
    print("")
    print("   # Install from git repository")
    print("   pip install git+https://github.com/user/repo.git")

    print("\\n8. Version management:")
    print("   # Update version in setup.py or pyproject.toml")
    print("   # Create git tag")
    print("   git tag v1.0.1")
    print("   git push origin v1.0.1")
    print("")
    print("   # Or use bumpversion tool")
    print("   pip install bumpversion")
    print("   bumpversion patch  # 1.0.0 -> 1.0.1")
    print("   bumpversion minor  # 1.0.1 -> 1.1.0")
    print("   bumpversion major  # 1.1.0 -> 2.0.0")


def demonstrate_virtual_environments():
    """Demonstrate virtual environment usage"""
    print("\\n" + "=" * 60)
    print("VIRTUAL ENVIRONMENTS")
    print("=" * 60)

    print("\\n1. Why use virtual environments?")
    print("   - Isolate project dependencies")
    print("   - Avoid version conflicts")
    print("   - Reproducible development environments")
    print("   - Clean project deployments")

    print("\\n2. Creating virtual environments:")
    print("   # Using venv (Python 3.3+)")
    print("   python -m venv myproject_env")
    print("   python -m venv venv  # Common name")
    print("")
    print("   # Using virtualenv (older method)")
    print("   pip install virtualenv")
    print("   virtualenv myproject_env")
    print("")
    print("   # Using conda")
    print("   conda create --name myproject python=3.11")

    print("\\n3. Activating virtual environments:")
    print("   # Linux/Mac")
    print("   source venv/bin/activate")
    print("")
    print("   # Windows")
    print("   venv\\\\Scripts\\\\activate")
    print("   # or")
    print("   venv\\\\Scripts\\\\activate.bat")
    print("")
    print("   # Conda")
    print("   conda activate myproject")

    print("\\n4. Working with virtual environments:")
    print("   # Check which Python you're using")
    print("   which python")
    print("   python --version")
    print("")
    print("   # Install packages")
    print("   pip install requests pandas")
    print("")
    print("   # List installed packages")
    print("   pip list")
    print("   pip freeze")
    print("")
    print("   # Save requirements")
    print("   pip freeze > requirements.txt")
    print("")
    print("   # Install from requirements")
    print("   pip install -r requirements.txt")

    print("\\n5. Deactivating virtual environments:")
    print("   # For venv and virtualenv")
    print("   deactivate")
    print("")
    print("   # For conda")
    print("   conda deactivate")

    print("\\n6. Managing multiple environments:")
    print("   # List conda environments")
    print("   conda env list")
    print("")
    print("   # Remove conda environment")
    print("   conda env remove --name myproject")
    print("")
    print("   # Export conda environment")
    print("   conda env export > environment.yml")
    print("")
    print("   # Create from environment file")
    print("   conda env create -f environment.yml")

    print("\\n7. Best practices:")
    print("   - Always use virtual environments for projects")
    print("   - Use descriptive names for environments")
    print("   - Keep requirements.txt updated")
    print("   - Don't commit virtual environment folders to git")
    print("   - Use .gitignore to exclude venv/, .env/, etc.")


def demonstrate_dependency_management():
    """Demonstrate dependency management"""
    print("\\n" + "=" * 60)
    print("DEPENDENCY MANAGEMENT")
    print("=" * 60)

    print("\\n1. Requirements files:")
    print("   # Basic requirements.txt")
    print("   requests>=2.28.0")
    print("   click>=8.0.0")
    print("   pandas>=1.5.0,<2.0.0")
    print("")
    print("   # Development requirements (requirements-dev.txt)")
    print("   pytest>=7.0.0")
    print("   black>=22.0.0")
    print("   mypy>=1.0.0")
    print("")
    print("   # Install requirements")
    print("   pip install -r requirements.txt")
    print("   pip install -r requirements-dev.txt")

    print("\\n2. Setup.py dependencies:")
    print("   setup(")
    print("       install_requires=[")
    print("           'requests>=2.28.0',")
    print("           'click>=8.0.0',")
    print("       ],")
    print("       extras_require={")
    print("           'dev': ['pytest>=7.0', 'black>=22.0'],")
    print("           'docs': ['sphinx>=5.0'],")
    print("       }")
    print("   )")
    print("")
    print("   # Install with extras")
    print("   pip install .[dev]")
    print("   pip install .[dev,docs]")

    print("\\n3. Modern dependency management (pipenv):")
    print("   # Install pipenv")
    print("   pip install pipenv")
    print("")
    print("   # Initialize project")
    print("   pipenv install")
    print("")
    print("   # Install packages")
    print("   pipenv install requests")
    print("   pipenv install pytest --dev")
    print("")
    print("   # Generate requirements.txt")
    print("   pipenv requirements > requirements.txt")

    print("\\n4. Poetry (modern dependency management):")
    print("   # Install poetry")
    print("   pip install poetry")
    print("")
    print("   # Initialize project")
    print("   poetry init")
    print("")
    print("   # Add dependencies")
    print("   poetry add requests")
    print("   poetry add pytest --group dev")
    print("")
    print("   # Install dependencies")
    print("   poetry install")

    print("\\n5. Version specifiers:")
    print("   # Exact version")
    print("   package==1.2.3")
    print("")
    print("   # Minimum version")
    print("   package>=1.2.3")
    print("")
    print("   # Compatible release")
    print("   package~=1.2.3  # >=1.2.3, <1.3.0")
    print("")
    print("   # Version range")
    print("   package>=1.2.0,<2.0.0")
    print("")
    print("   # Exclude versions")
    print("   package>=1.2.0,!=1.3.0")


def main():
    """Main function demonstrating Python packaging"""
    print("📦 COMPREHENSIVE PYTHON PACKAGING TUTORIAL")
    print("Learn how to create, package, and distribute Python libraries.")

    # Create sample package
    package_dir = create_sample_package_structure()

    if package_dir:
        print(f"\\n✅ Sample package created at: {package_dir.absolute()}")

        # Show final directory structure
        print("\\nFinal package structure:")
        for root, dirs, files in os.walk(package_dir):
            # Skip __pycache__ directories
            dirs[:] = [d for d in dirs if d != '__pycache__']

            level = root.replace(str(package_dir), '').count(os.sep)
            indent = '  ' * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = '  ' * (level + 1)
            for file in files:
                if not file.endswith('.pyc'):
                    print(f"{subindent}{file}")

    # Demonstrate commands and concepts
    demonstrate_packaging_commands()
    demonstrate_virtual_environments()
    demonstrate_dependency_management()

    print("\\n" + "=" * 60)
    print("PYTHON PACKAGING TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\\n💡 Key Packaging Concepts:")
    print("- Package structure with __init__.py files")
    print("- setup.py and pyproject.toml configuration")
    print("- Version management and semantic versioning")
    print("- Dependency management and requirements")
    print("- Testing and code quality tools")
    print("- Building distributions (sdist and wheel)")
    print("- Publishing to PyPI")

    print("\\n🛠️ Essential Tools:")
    print("- setuptools: Package building")
    print("- build: Modern build frontend")
    print("- twine: Package uploading")
    print("- pytest: Testing framework")
    print("- black: Code formatting")
    print("- mypy: Type checking")
    print("- venv: Virtual environments")

    print("\\n📚 Next Steps:")
    print("- Practice creating your own packages")
    print("- Learn about namespace packages")
    print("- Explore continuous integration (CI/CD)")
    print("- Study semantic versioning")
    print("- Learn about package security")
    print("- Explore modern tools like Poetry")


if __name__ == "__main__":
    main()