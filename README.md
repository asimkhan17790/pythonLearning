# Python Learning Guide 🐍

Welcome to the most comprehensive Python learning playground! This repository is designed to take you from a complete beginner to an advanced Python developer. Whether you're just starting your programming journey or looking to master advanced Python concepts, this guide has everything you need.

## 🎯 What You'll Learn

This repository covers **everything** from basic syntax to advanced topics like metaclasses, async programming, and web development. Each concept includes:
- **Clear explanations** with real-world context
- **Hands-on examples** you can run immediately
- **Progressive difficulty** that builds on previous concepts
- **Best practices** and common pitfalls to avoid

## 🆕 **What's New - Professional Level Content!**

We've added **comprehensive professional modules** (`my_modules/comprehensive_examples/`) that cover:

🔥 **Advanced Async/Await & REST APIs** - Production-ready async programming with real API examples
🏗️ **Complete OOP Mastery** - Every OOP concept from basics to design patterns
📦 **Professional Import & Packaging** - Build and publish your own Python packages
⚡ **Advanced Topics** - Regex, databases, logging, configuration management
🔄 **Threading vs Multiprocessing** - Master concurrency with clear performance comparisons
🐼 **Pandas Data Analysis** - Complete data manipulation, big data handling, and visualization
🔢 **Vectors & Numerical Computing** - NumPy mastery for scientific computing and ML
🚀 **Real-world Examples** - Bank systems, calculators, recommendation systems, and more!

These modules transform you from a Python learner to a **professional Python developer**.

## 🚀 Quick Start

1. **Clone this repository**:
   ```bash
   git clone <repository-url>
   cd pythonLearning
   ```

2. **Start with the basics**:
   ```bash
   python -m my_modules.basic_concepts.01_variables
   ```

3. **Follow the learning path** outlined below, or jump to any topic that interests you!

## 📚 Learning Path

### 🟢 **Beginner Level** (Start Here!)
1. [Variables and Data Types](#1-variables-and-data-types) - The building blocks of Python
2. [Basic Input/Output](#2-basic-inputoutput) - Interacting with users
3. [Operators](#3-operators) - Mathematical and logical operations
4. [Conditional Statements](#4-conditional-statements) - Making decisions in code
5. [Loops](#5-loops) - Repeating actions efficiently
6. [Functions](#6-functions) - Organizing and reusing code

### 🟡 **Intermediate Level**
7. [Data Structures](#7-data-structures) - Lists, dictionaries, sets, and tuples
8. [List Comprehensions](#8-list-comprehensions) - Elegant data processing
9. [String Manipulation](#9-string-manipulation) - Working with text
10. [Exception Handling](#10-exception-handling) - Managing errors gracefully
11. [Classes and Objects](#11-classes-and-objects) - Object-oriented programming basics
12. [File Handling](#12-file-handling) - Reading and writing files
13. [Modules and Imports](#13-modules-and-imports) - Organizing larger projects

### 🔴 **Advanced Level**
14. [Useful Built-in Functions](#14-useful-built-in-functions) - Python's powerful toolkit
15. [Decorators](#15-decorators) - Modifying function behavior
16. [Generators](#16-generators) - Memory-efficient iteration
17. [Lambda Functions](#17-lambda-functions) - Anonymous functions
18. [Map, Filter, Reduce](#18-map-filter-reduce) - Functional programming
19. [Context Managers](#19-context-managers) - Resource management
20. [Inheritance & Polymorphism](#20-inheritance--polymorphism) - Advanced OOP
21. [Exception Chaining & Custom Exceptions](#21-exception-chaining--custom-exceptions)
22. [Type Hinting](#22-type-hinting) - Better code documentation
23. [Concurrency](#23-concurrency-threading--multiprocessing) - Parallel programming
24. [Metaclasses](#24-metaclasses) - Classes that create classes
25. [Property Decorators](#25-property-decorators) - Controlled attribute access
26. [Async/Await](#26-asyncawait) - Asynchronous programming basics
27. [Data Classes](#27-data-classes) - Simplified class creation
28. [Testing](#28-testing-unittest) - Writing reliable code
29. [Packaging & Virtual Environments](#29-packaging--virtual-environments) - Project management

### 🚀 **Professional Level** - New Comprehensive Modules!
30. [Advanced Async/Await & REST APIs](#30-advanced-asyncawait--rest-apis) - Production-ready async programming
31. [Comprehensive Object-Oriented Programming](#31-comprehensive-object-oriented-programming) - Master OOP concepts
32. [Library Imports & Module Management](#32-library-imports--module-management) - Professional import practices
33. [Python Packaging & Distribution](#33-python-packaging--distribution) - Create and publish packages
34. [Advanced Topics: Regex, Database, Logging](#34-advanced-topics-regex-database-logging) - Production essentials
35. [Threading vs Multiprocessing](#35-threading-vs-multiprocessing) - Comprehensive concurrency guide
36. [Pandas Data Analysis](#36-pandas-data-analysis) - Complete data manipulation and analysis
37. [Vectors & Numerical Computing](#37-vectors--numerical-computing) - NumPy and scientific computing mastery

---

## 1. Variables and Data Types

Variables are like labeled containers that store data in memory. Python is **dynamically typed**, meaning you don't need to declare variable types explicitly - Python figures it out based on the value you assign.

### Understanding Variables in Memory

```python
# Variable assignment creates a reference to an object in memory
name = "Maverick"
age = 25

# Multiple variables can reference the same object
first_name = name
current_age = age

# Check if they reference the same object
print(id(name))           # Memory address (e.g., 140712345678912)
print(id(first_name))     # Same memory address
print(name is first_name) # True - same object in memory

# Variables are just labels pointing to objects
x = 100
y = 100
print(x is y)             # True - Python optimizes small integers
```

### Strings - Immutable Text Sequences

Strings represent text data and are **immutable** (cannot be changed after creation):

```python
# Different ways to create strings
name = "Maverick"                    # Double quotes
message = 'Hello, World!'           # Single quotes
path = r"C:\Users\name\folder"      # Raw string (ignores escape characters)
multiline = """This is a
multiline string that spans
multiple lines"""                   # Triple quotes for multiline

# String immutability demonstration
original = "Hello"
print(id(original))                 # Memory address: 140712345678912
modified = original + " World"      # Creates NEW string object
print(id(modified))                 # Different memory address: 140712345678920
print(original)                     # Still "Hello" - unchanged

# String indexing and slicing
text = "Python Programming"
print(f"First character: {text[0]}")      # P
print(f"Last character: {text[-1]}")      # g
print(f"First 6 chars: {text[:6]}")       # Python
print(f"Last 11 chars: {text[7:]}")       # ramming
print(f"Every 2nd char: {text[::2]}")     # Pto rgamn

# Escape characters
escaped = "He said, \"Hello!\" and left\nNext line here\tTab here"
print(escaped)
# Output:
# He said, "Hello!" and left
# Next line here	Tab here

# String encoding and Unicode
unicode_text = "Hello 世界 🌍"         # Unicode support
print(f"Length: {len(unicode_text)}")      # Length: 10 (counts Unicode chars)
print(f"Encoded: {unicode_text.encode('utf-8')}")  # b'Hello \xe4\xb8\x96\xe7\x95\x8c \xf0\x9f\x8c\x8d'
```

### Integers - Whole Numbers with Unlimited Precision

Python integers have **arbitrary precision** - they can be as large as memory allows:

```python
# Regular integers
age = 25
year = 2024
negative = -42

# Large integers (no overflow in Python!)
huge_number = 123456789012345678901234567890
print(f"Huge number: {huge_number}")
print(f"Type: {type(huge_number)}")        # Still <class 'int'>

# Different number bases
binary = 0b1010      # Binary (base 2) = 10 in decimal
octal = 0o12         # Octal (base 8) = 10 in decimal
hexadecimal = 0xa    # Hexadecimal (base 16) = 10 in decimal

print(f"Binary 1010: {binary}")           # 10
print(f"Octal 12: {octal}")               # 10
print(f"Hex a: {hexadecimal}")            # 10

# Integer operations preserve type when possible
result = 10 + 5      # 15 (int)
division = 10 // 3   # 3 (int - floor division)
power = 2 ** 100     # 1267650600228229401496703205376 (still int!)

# Underscores for readability (Python 3.6+)
million = 1_000_000
pi_digits = 3.14159_26535_89793
print(f"Million: {million}")              # 1000000
print(f"Pi: {pi_digits}")                 # 3.141592653589793
```

### Floats - IEEE 754 Double Precision Numbers

Floats represent decimal numbers but have limitations due to binary representation:

```python
# Basic float usage
height = 5.9
pi = 3.14159
temperature = -2.5

# Scientific notation
speed_of_light = 2.998e8    # 299,800,000
planck_constant = 6.626e-34 # 0.0000000000000000000000000000000000626626

# Float precision limitations
print(0.1 + 0.2)                          # 0.30000000000000004 (not 0.3!)
print(0.1 + 0.2 == 0.3)                   # False

# Proper float comparison
import math
def float_equal(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance

print(float_equal(0.1 + 0.2, 0.3))        # True

# Special float values
positive_infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(f"Infinity: {positive_infinity}")    # inf
print(f"Is infinite: {math.isinf(positive_infinity)}")  # True
print(f"NaN: {not_a_number}")             # nan
print(f"Is NaN: {math.isnan(not_a_number)}")  # True

# Float precision and rounding
value = 1/3
print(f"1/3 = {value}")                   # 0.3333333333333333
print(f"Rounded: {round(value, 4)}")      # 0.3333
print(f"Decimal module for precision:")
from decimal import Decimal, getcontext
getcontext().prec = 50  # Set precision to 50 digits
precise = Decimal(1) / Decimal(3)
print(f"Precise 1/3: {precise}")          # 0.33333333333333333333333333333333333333333333333333
```

### Booleans - Truth Values with Rich Behavior

Booleans represent truth values and are actually a subclass of integers:

```python
# Basic boolean values
is_student = True
is_employed = False

# Booleans are integers!
print(f"True as int: {int(True)}")        # 1
print(f"False as int: {int(False)}")      # 0
print(f"True + True: {True + True}")      # 2
print(f"True * 5: {True * 5}")            # 5

# Boolean evaluation of different types
print("=== Truthy and Falsy Values ===")
# Falsy values (evaluate to False)
falsy_values = [False, 0, 0.0, '', [], {}, set(), None, complex(0,0)]
for value in falsy_values:
    print(f"{repr(value):15} -> {bool(value)}")

# Truthy values (evaluate to True)
truthy_values = [True, 1, -1, 'hello', [1,2], {'a':1}, {1,2}, 42, 3.14]
for value in truthy_values:
    print(f"{repr(value):15} -> {bool(value)}")

# Short-circuit evaluation
def expensive_operation():
    print("Expensive operation called!")
    return True

# 'and' stops at first False, 'or' stops at first True
result1 = False and expensive_operation()  # expensive_operation() not called
result2 = True or expensive_operation()    # expensive_operation() not called
result3 = True and expensive_operation()   # expensive_operation() IS called

# Boolean operators return actual values, not just True/False
print(f"'hello' and 'world': {'hello' and 'world'}")    # 'world'
print(f"'' or 'default': {'' or 'default'}")            # 'default'
print(f"None or 0 or 'value': {None or 0 or 'value'}")  # 'value'
```

### None - The Null Value

None represents the absence of a value and is a singleton object:

```python
# None is a singleton - there's only one None object
data = None
other_none = None
print(f"Same None object: {data is other_none}")  # True
print(f"None ID: {id(None)}")                     # Same for all None references

# Common None patterns
def might_return_none(condition):
    if condition:
        return "Some value"
    return None  # Explicit None return

def implicit_none():
    pass  # Functions without return statement return None

result1 = might_return_none(False)
result2 = implicit_none()
print(f"Explicit None: {result1}")               # None
print(f"Implicit None: {result2}")               # None

# None checking patterns
value = None

# Good - use 'is' for None comparison
if value is None:
    print("Value is None")

# Bad - don't use == with None
if value == None:  # Works but not recommended
    print("This works but use 'is' instead")

# None vs empty containers
empty_list = []
none_value = None

print(f"Empty list is falsy: {bool(empty_list)}")    # False
print(f"None is falsy: {bool(none_value)}")          # False
print(f"But they're different: {empty_list is not none_value}")  # True
```

### Advanced Variable Concepts

```python
# Variable scope and the global namespace
global_var = "I'm global"

def demonstrate_scope():
    local_var = "I'm local"
    global global_var

    print(f"Local variable: {local_var}")
    print(f"Global variable: {global_var}")

    # Access global variables
    print(f"All globals: {list(globals().keys())}")
    print(f"All locals: {list(locals().keys())}")

demonstrate_scope()

# Variable unpacking and multiple assignment
# Tuple unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")                # x=10, y=20, z=30

# Extended unpacking with *
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")  # First: 1, Middle: [2, 3, 4], Last: 5

# Swapping variables (Pythonic way)
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")          # a=5, b=10
a, b = b, a
print(f"After swap: a={a}, b={b}")           # a=10, b=5

# Chained assignment
x = y = z = 0
print(f"x={x}, y={y}, z={z}")                # All are 0, but be careful with mutable objects!

# Dangerous chained assignment with mutable objects
list1 = list2 = []  # Both point to same list!
list1.append(1)
print(f"list1: {list1}, list2: {list2}")     # Both show [1] - unexpected!

# Safe way with mutable objects
list3, list4 = [], []  # Different objects
list3.append(1)
print(f"list3: {list3}, list4: {list4}")     # list3: [1], list4: []

# Dynamic typing in action
variable = 42        # integer
print(f"Type: {type(variable)}, Value: {variable}")

variable = "Hello"   # now it's a string
print(f"Type: {type(variable)}, Value: {variable}")

variable = [1, 2, 3] # now it's a list
print(f"Type: {type(variable)}, Value: {variable}")

# Variables referencing functions
def greet():
    return "Hello!"

my_function = greet  # Variable holds function reference
print(f"Function result: {my_function()}")   # Hello!
print(f"Function type: {type(my_function)}") # <class 'function'>
```

### Memory Management and Garbage Collection

```python
import sys
import gc

# Reference counting
data = [1, 2, 3, 4, 5]
print(f"Reference count: {sys.getrefcount(data)}")  # 2 (variable + getrefcount parameter)

another_ref = data
print(f"Reference count after assignment: {sys.getrefcount(data)}")  # 3

del another_ref
print(f"Reference count after deletion: {sys.getrefcount(data)}")    # 2

# Memory usage
import tracemalloc
tracemalloc.start()

# Create some objects
big_list = list(range(100000))
big_dict = {i: i**2 for i in range(10000)}

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()

# Garbage collection info
print(f"Garbage collection counts: {gc.get_count()}")
collected = gc.collect()
print(f"Objects collected: {collected}")
```

**💡 Advanced Pro Tips:**
- **Memory Efficiency**: Use `__slots__` in classes to reduce memory usage
- **Type Hints**: Use type annotations for better code documentation (Python 3.5+)
- **Immutable vs Mutable**: Understand which types can be changed in-place
- **Identity vs Equality**: Use `is` for identity, `==` for equality
- **Integer Caching**: Python caches integers -5 to 256 for performance
- **String Interning**: Python may intern identical strings for memory efficiency

## 2. Basic Input/Output

Input/Output (I/O) operations allow your programs to communicate with users and external systems. Python provides powerful and flexible I/O capabilities.

### Output - The print() Function Deep Dive

The `print()` function is much more powerful than it appears:

```python
# Basic print usage
print("Hello, World!")                    # Output: Hello, World!
print("Multiple", "arguments", "here")     # Output: Multiple arguments here

# Print function signature: print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)

# Controlling separators
print("apple", "banana", "cherry", sep=", ")        # Output: apple, banana, cherry
print("apple", "banana", "cherry", sep=" | ")       # Output: apple | banana | cherry
print("apple", "banana", "cherry", sep="")          # Output: applebananacherry

# Controlling line endings
print("Loading", end="")                   # No newline
print(".", end="")                         # Output so far: Loading.
print(".", end="")                         # Output so far: Loading..
print(" Complete!")                        # Output: Loading.. Complete!

# Printing to different outputs
import sys
print("Standard output")                   # Goes to stdout
print("Error message", file=sys.stderr)   # Goes to stderr

# Writing to files using print
with open("output.txt", "w") as file:
    print("This goes to a file", file=file)
    print("Line 2", file=file)

# Flushing output immediately
import time
for i in range(5):
    print(f"Processing {i}...", end=" ", flush=True)  # Immediate output
    time.sleep(1)  # Simulate work
print("Done!")

# Print with custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):              # Defines how print() shows the object
        return f"Person(name='{self.name}', age={self.age})"

    def __repr__(self):             # Defines how the object appears in containers
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(person)                      # Output: Person(name='Alice', age=30)
print([person])                    # Output: [Person('Alice', 30)]
```

### String Formatting - From Basic to Advanced

Python offers multiple string formatting approaches, each with its strengths:

```python
name = "Alice"
age = 30
height = 5.6
balance = 1234.567

# 1. f-strings (Python 3.6+) - RECOMMENDED
# Basic f-string usage
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)                    # Output: Hello, Alice! You are 30 years old.

# Advanced f-string formatting
print(f"Name: {name:>10}")         # Right-align in 10 characters: "     Alice"
print(f"Age: {age:0>3}")           # Zero-pad to 3 digits: "030"
print(f"Height: {height:.2f}")     # 2 decimal places: "5.60"
print(f"Balance: ${balance:,.2f}") # Currency format: "$1,234.57"

# f-strings with expressions
print(f"Next year: {age + 1}")     # Output: Next year: 31
print(f"Uppercase: {name.upper()}") # Output: Uppercase: ALICE
print(f"Is adult: {age >= 18}")    # Output: Is adult: True

# f-strings with date formatting
from datetime import datetime
now = datetime.now()
print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")  # Output: Current time: 2024-03-15 14:30:25

# 2. .format() method (Python 2.7+)
# Positional arguments
template = "Hello, {}! You are {} years old."
print(template.format(name, age))  # Output: Hello, Alice! You are 30 years old.

# Named arguments
template = "Hello, {name}! You are {age} years old."
print(template.format(name=name, age=age))

# Formatting with .format()
print("Height: {:.2f}".format(height))           # Output: Height: 5.60
print("Balance: ${:,.2f}".format(balance))       # Output: Balance: $1,234.57
print("Name: {:>10}".format(name))               # Output: Name:      Alice

# 3. % formatting (old style, but still useful)
print("Hello, %s! You are %d years old." % (name, age))  # Output: Hello, Alice! You are 30 years old.
print("Height: %.2f" % height)                           # Output: Height: 5.60
print("Balance: $%,.2f" % balance)                       # Output: Balance: $1,234.57

# Advanced formatting examples
# Number formatting
number = 42
print(f"Binary: {number:b}")       # Output: Binary: 101010
print(f"Octal: {number:o}")        # Output: Octal: 52
print(f"Hex: {number:x}")          # Output: Hex: 2a
print(f"Scientific: {1234.5:e}")   # Output: Scientific: 1.234500e+03

# Percentage formatting
ratio = 0.845
print(f"Success rate: {ratio:.1%}") # Output: Success rate: 84.5%

# Complex formatting
data = {"name": "Bob", "score": 95.5, "rank": 3}
print(f"Student {data['name']} scored {data['score']:.1f}% (rank #{data['rank']})")
# Output: Student Bob scored 95.5% (rank #3)
```

### Input - Getting and Validating User Data

The `input()` function is the primary way to get user input, but it requires careful handling:

```python
# Basic input usage
user_name = input("Enter your name: ")     # Always returns a string
print(f"Hello, {user_name}!")

# Input always returns strings - conversion needed
age_str = input("Enter your age: ")        # "25" (string)
age = int(age_str)                         # 25 (integer)
print(f"Next year you'll be {age + 1}")

# Common input patterns with error handling
def get_integer_input(prompt, min_val=None, max_val=None):
    """Get integer input with validation"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None

def get_float_input(prompt):
    """Get float input with validation"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def get_yes_no_input(prompt):
    """Get yes/no input"""
    while True:
        response = input(f"{prompt} (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'")

# Example usage
# age = get_integer_input("Enter your age (0-120): ", 0, 120)
# height = get_float_input("Enter your height in feet: ")
# is_student = get_yes_no_input("Are you a student?")

# Input with default values
def get_input_with_default(prompt, default):
    """Get input with a default value"""
    response = input(f"{prompt} [{default}]: ").strip()
    return response if response else default

# name = get_input_with_default("Enter your name", "Anonymous")

# Reading multiple values from one line
def get_coordinates():
    """Get x, y coordinates from user"""
    while True:
        try:
            coords_str = input("Enter x,y coordinates (e.g., 10,20): ")
            x_str, y_str = coords_str.split(',')
            x = float(x_str.strip())
            y = float(y_str.strip())
            return x, y
        except ValueError:
            print("Please enter two numbers separated by a comma")

# x, y = get_coordinates()
```

### Advanced Input/Output Techniques

```python
# Reading passwords securely (no echo)
import getpass

# password = getpass.getpass("Enter password: ")  # Input not shown
# print(f"Password length: {len(password)}")

# Command line arguments
import sys

print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
print(f"Number of arguments: {len(sys.argv) - 1}")

# More sophisticated argument parsing
import argparse

def demo_argparse():
    parser = argparse.ArgumentParser(description="Demo program")
    parser.add_argument("name", help="Your name")
    parser.add_argument("--age", type=int, default=25, help="Your age")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    # This would parse command line args: python script.py Alice --age 30 -v
    # args = parser.parse_args()
    # print(f"Hello {args.name}, age {args.age}")
    # if args.verbose:
    #     print("Verbose mode enabled")

# Environment variables
import os

# Reading environment variables
user_home = os.environ.get('HOME', '/default/path')  # Get HOME or default
python_path = os.environ.get('PYTHONPATH', '')
print(f"Home directory: {user_home}")

# Setting environment variables (for child processes)
os.environ['MY_VARIABLE'] = 'my_value'

# Standard streams
import sys

# Reading from stdin (useful for piped input)
# if not sys.stdin.isatty():  # Check if input is piped
#     for line in sys.stdin:
#         print(f"Received: {line.strip()}")

# Writing to stderr
def log_error(message):
    print(f"ERROR: {message}", file=sys.stderr)

log_error("This is an error message")

# Progress bars and indicators
def show_progress(current, total, bar_length=50):
    """Display a progress bar"""
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress: |{bar}| {percent:.1%} ({current}/{total})', end='', flush=True)

# Simulate progress
import time
total_items = 100
for i in range(total_items + 1):
    show_progress(i, total_items)
    time.sleep(0.01)  # Simulate work
print()  # New line after progress bar

# Colored output (cross-platform)
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # Reset to default

def colored_print(text, color):
    """Print colored text"""
    print(f"{color}{text}{Colors.END}")

colored_print("This is red text", Colors.RED)
colored_print("This is green text", Colors.GREEN)
colored_print("This is bold text", Colors.BOLD)
```

### File I/O Integration with Input/Output

```python
# Logging user interactions
import datetime

def log_interaction(user_input, response):
    """Log user interactions to a file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("interaction_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] Input: {user_input} | Response: {response}\n")

# Interactive session with logging
def interactive_calculator():
    """Simple calculator with logging"""
    print("Simple Calculator (type 'quit' to exit)")

    while True:
        try:
            expression = input("Enter expression: ").strip()

            if expression.lower() == 'quit':
                print("Goodbye!")
                break

            # Evaluate safely (in real code, use a proper parser)
            result = eval(expression)  # Warning: Don't use eval() with untrusted input!
            print(f"Result: {result}")

            # Log the interaction
            log_interaction(expression, result)

        except Exception as e:
            error_msg = f"Error: {e}"
            print(error_msg)
            log_interaction(expression, error_msg)

# interactive_calculator()

# Reading configuration from user
def setup_user_profile():
    """Interactive user profile setup"""
    profile = {}

    print("=== User Profile Setup ===")
    profile['name'] = input("Full name: ").strip()
    profile['email'] = input("Email: ").strip()
    profile['age'] = get_integer_input("Age: ", 1, 120)
    profile['city'] = input("City: ").strip()

    # Confirm and save
    print("\n=== Profile Summary ===")
    for key, value in profile.items():
        print(f"{key.title()}: {value}")

    if get_yes_no_input("\nSave this profile?"):
        import json
        with open("user_profile.json", "w") as f:
            json.dump(profile, f, indent=2)
        print("Profile saved successfully!")
    else:
        print("Profile not saved.")

    return profile

# profile = setup_user_profile()
```

**💡 Advanced Pro Tips:**

- **Input Validation**: Always validate and sanitize user input
- **Error Handling**: Use try-except blocks for robust input handling
- **User Experience**: Provide clear prompts and helpful error messages
- **Security**: Never use `eval()` with untrusted input - use `ast.literal_eval()` for safe evaluation
- **Internationalization**: Consider Unicode and different locales for global applications
- **Accessibility**: Support screen readers and other assistive technologies
- **Performance**: For large outputs, consider buffering and pagination
- **Cross-platform**: Test I/O behavior on different operating systems

**⚠️ Common Pitfalls:**
- Forgetting that `input()` always returns strings
- Not handling empty input or whitespace
- Using `eval()` without proper security considerations
- Not validating input ranges and types
- Ignoring keyboard interrupts (Ctrl+C)
- Poor error messages that don't help users understand what went wrong

## 3. Operators

Operators are symbols that perform operations on variables and values. Python provides a rich set of operators that work with different data types and have specific precedence rules.

### Arithmetic Operators - Mathematical Operations

Python provides comprehensive arithmetic operations with automatic type handling:

```python
# Basic arithmetic operators
a = 10
b = 3

print(f"a = {a}, b = {b}")
print("=== Basic Arithmetic ===")
print(f"Addition: {a} + {b} = {a + b}")           # 13
print(f"Subtraction: {a} - {b} = {a - b}")        # 7
print(f"Multiplication: {a} * {b} = {a * b}")     # 30
print(f"Division: {a} / {b} = {a / b}")           # 3.3333333333333335
print(f"Floor Division: {a} // {b} = {a // b}")   # 3 (rounds down)
print(f"Modulus: {a} % {b} = {a % b}")            # 1 (remainder)
print(f"Exponentiation: {a} ** {b} = {a ** b}")   # 1000

# Type behavior in arithmetic operations
print("\n=== Type Behavior ===")
int_result = 5 + 3          # int + int = int
float_result = 5.0 + 3      # float + int = float
mixed_result = 10 / 3       # Division always returns float

print(f"5 + 3 = {int_result} (type: {type(int_result)})")           # 8 (int)
print(f"5.0 + 3 = {float_result} (type: {type(float_result)})")     # 8.0 (float)
print(f"10 / 3 = {mixed_result} (type: {type(mixed_result)})")      # 3.333... (float)

# Advanced arithmetic examples
print("\n=== Advanced Examples ===")
# Complex numbers
complex1 = 3 + 4j
complex2 = 1 + 2j
print(f"Complex addition: {complex1} + {complex2} = {complex1 + complex2}")

# Large number arithmetic (unlimited precision)
huge1 = 12345678901234567890
huge2 = 98765432109876543210
print(f"Large numbers: {huge1} + {huge2} = {huge1 + huge2}")

# Float precision issues
print(f"0.1 + 0.2 = {0.1 + 0.2}")                # 0.30000000000000004 (precision issue)
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")   # False

# Safe float comparison
import math
def float_equal(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance

print(f"Safe comparison: {float_equal(0.1 + 0.2, 0.3)}")  # True

# Modulus with negative numbers
print("\n=== Modulus Behavior ===")
print(f"10 % 3 = {10 % 3}")      # 1
print(f"-10 % 3 = {-10 % 3}")    # 2 (Python's modulus has sign of divisor)
print(f"10 % -3 = {10 % -3}")    # -2
print(f"-10 % -3 = {-10 % -3}")  # -1

# Floor division behavior
print("\n=== Floor Division Behavior ===")
print(f"10 // 3 = {10 // 3}")       # 3
print(f"-10 // 3 = {-10 // 3}")     # -4 (floors towards negative infinity)
print(f"10.5 // 2 = {10.5 // 2}")   # 5.0 (returns float when operand is float)

# Augmented assignment operators
print("\n=== Augmented Assignment ===")
x = 10
print(f"Initial x: {x}")
x += 5    # Equivalent to x = x + 5
print(f"After x += 5: {x}")    # 15
x -= 3    # x = x - 3
print(f"After x -= 3: {x}")    # 12
x *= 2    # x = x * 2
print(f"After x *= 2: {x}")    # 24
x //= 5   # x = x // 5
print(f"After x //= 5: {x}")   # 4
x **= 3   # x = x ** 3
print(f"After x **= 3: {x}")   # 64
```

### Comparison Operators - Testing Relationships

Comparison operators return boolean values and can be chained:

```python
# Basic comparison operators
a, b, c = 10, 3, 10

print("=== Basic Comparisons ===")
print(f"a = {a}, b = {b}, c = {c}")
print(f"a == b: {a == b}")      # False (equal)
print(f"a != b: {a != b}")      # True (not equal)
print(f"a > b: {a > b}")        # True (greater than)
print(f"a < b: {a < b}")        # False (less than)
print(f"a >= c: {a >= c}")      # True (greater than or equal)
print(f"a <= c: {a <= c}")      # True (less than or equal)

# Identity operators (is, is not)
print("\n=== Identity vs Equality ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 == list2: {list1 == list2}")   # True (same content)
print(f"list1 is list2: {list1 is list2}")   # False (different objects)
print(f"list1 is list3: {list1 is list3}")   # True (same object)
print(f"list1 is not list2: {list1 is not list2}")  # True

# Identity with immutable objects (optimization)
x = 100
y = 100
print(f"x is y (small integers): {x is y}")   # True (Python caches small integers)

x = 1000
y = 1000
print(f"x is y (large integers): {x is y}")   # May be False (depends on implementation)

# Membership operators (in, not in)
print("\n=== Membership Testing ===")
fruits = ["apple", "banana", "cherry"]
text = "Hello, World!"
numbers = {1, 2, 3, 4, 5}

print(f"'apple' in fruits: {'apple' in fruits}")         # True
print(f"'grape' not in fruits: {'grape' not in fruits}") # True
print(f"'World' in text: {'World' in text}")             # True
print(f"3 in numbers: {3 in numbers}")                   # True

# Chained comparisons (Pythonic!)
print("\n=== Chained Comparisons ===")
score = 85
print(f"Score: {score}")
print(f"0 <= score <= 100: {0 <= score <= 100}")        # True
print(f"80 < score < 90: {80 < score < 90}")             # True

age = 25
print(f"Age: {age}")
print(f"18 <= age < 65: {18 <= age < 65}")               # True

# Equivalent to: (18 <= age) and (age < 65)
# This is more readable and efficient than separate comparisons

# Comparison with different types
print("\n=== Type Comparisons ===")
# Numbers can be compared across types
print(f"5 == 5.0: {5 == 5.0}")           # True
print(f"5 is 5.0: {5 is 5.0}")           # False (different types)

# Strings are compared lexicographically
print(f"'apple' < 'banana': {'apple' < 'banana'}")      # True
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")        # True (ASCII values)

# Comparing None
value = None
print(f"value is None: {value is None}")                 # True (recommended)
print(f"value == None: {value == None}")                 # True (works but not recommended)
```

### Logical Operators - Boolean Logic

Logical operators work with truth values and support short-circuit evaluation:

```python
# Basic logical operators
print("=== Basic Logical Operators ===")
x, y = True, False

print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")     # False (both must be True)
print(f"x or y: {x or y}")       # True (at least one must be True)
print(f"not x: {not x}")         # False (opposite of x)
print(f"not y: {not y}")         # True (opposite of y)

# Short-circuit evaluation
print("\n=== Short-Circuit Evaluation ===")
def expensive_true():
    print("Expensive True function called")
    return True

def expensive_false():
    print("Expensive False function called")
    return False

# 'and' stops at first False
print("Testing: False and expensive_true()")
result = False and expensive_true()  # expensive_true() not called
print(f"Result: {result}")

# 'or' stops at first True
print("\nTesting: True or expensive_false()")
result = True or expensive_false()   # expensive_false() not called
print(f"Result: {result}")

# When evaluation continues
print("\nTesting: True and expensive_true()")
result = True and expensive_true()   # expensive_true() IS called
print(f"Result: {result}")

# Logical operators return actual values, not just True/False
print("\n=== Return Values ===")
print(f"'hello' and 'world': {'hello' and 'world'}")    # 'world' (last truthy)
print(f"'' and 'world': {'' and 'world'}")              # '' (first falsy)
print(f"None or 'default': {None or 'default'}")        # 'default' (first truthy)
print(f"0 or [] or 'value': {0 or [] or 'value'}")      # 'value' (first truthy)

# Practical applications
print("\n=== Practical Applications ===")
# Default value pattern
name = ""
display_name = name or "Anonymous"
print(f"Display name: {display_name}")    # Anonymous

# Validation pattern
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")          # True

# Complex conditions
temperature = 75
is_sunny = True
is_weekend = False

good_picnic_weather = (temperature > 70 and is_sunny) and (is_weekend or temperature > 80)
print(f"Good picnic weather: {good_picnic_weather}")  # False

# De Morgan's laws
a, b = True, False
print(f"\n=== De Morgan's Laws ===")
print(f"not (a and b) == (not a) or (not b): {not (a and b) == (not a) or (not b)}")  # True
print(f"not (a or b) == (not a) and (not b): {not (a or b) == (not a) and (not b)}")  # True
```

### Bitwise Operators - Binary Operations

Bitwise operators work on the binary representation of numbers:

```python
# Basic bitwise operators
print("=== Bitwise Operators ===")
a = 12  # Binary: 1100
b = 7   # Binary: 0111

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

print(f"a & b (AND): {a & b} (binary: {bin(a & b)})")      # 4 (0100)
print(f"a | b (OR): {a | b} (binary: {bin(a | b)})")       # 15 (1111)
print(f"a ^ b (XOR): {a ^ b} (binary: {bin(a ^ b)})")      # 11 (1011)
print(f"~a (NOT): {~a} (binary: {bin(~a)})")               # -13 (two's complement)

# Bit shifting
print(f"\n=== Bit Shifting ===")
x = 5  # Binary: 101
print(f"x = {x} (binary: {bin(x)})")
print(f"x << 2: {x << 2} (binary: {bin(x << 2)})")         # 20 (10100) - left shift
print(f"x >> 1: {x >> 1} (binary: {bin(x >> 1)})")         # 2 (10) - right shift

# Practical applications
print(f"\n=== Practical Applications ===")
# Check if number is power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

for num in [1, 2, 3, 4, 5, 8, 16, 15]:
    print(f"{num} is power of 2: {is_power_of_2(num)}")

# Set/clear/toggle bits
flags = 0b00000000  # 8-bit flags
FLAG_READ = 1       # 0b00000001
FLAG_WRITE = 2      # 0b00000010
FLAG_EXECUTE = 4    # 0b00000100

# Set flags
flags |= FLAG_READ | FLAG_WRITE
print(f"After setting READ and WRITE: {bin(flags)}")

# Check if flag is set
has_read = bool(flags & FLAG_READ)
print(f"Has READ permission: {has_read}")

# Clear flag
flags &= ~FLAG_WRITE  # Clear WRITE flag
print(f"After clearing WRITE: {bin(flags)}")

# Toggle flag
flags ^= FLAG_EXECUTE  # Toggle EXECUTE flag
print(f"After toggling EXECUTE: {bin(flags)}")
```

### Operator Precedence and Associativity

Understanding operator precedence prevents bugs and improves code clarity:

```python
# Operator precedence demonstration
print("=== Operator Precedence ===")

# Arithmetic operators precedence
result1 = 2 + 3 * 4      # Multiplication first: 2 + 12 = 14
result2 = (2 + 3) * 4    # Parentheses override: 5 * 4 = 20
print(f"2 + 3 * 4 = {result1}")      # 14
print(f"(2 + 3) * 4 = {result2}")    # 20

# Exponentiation is right-associative
result3 = 2 ** 3 ** 2    # Right-to-left: 2 ** (3 ** 2) = 2 ** 9 = 512
result4 = (2 ** 3) ** 2  # Left-to-right: (2 ** 3) ** 2 = 8 ** 2 = 64
print(f"2 ** 3 ** 2 = {result3}")     # 512
print(f"(2 ** 3) ** 2 = {result4}")   # 64

# Comparison and logical operators
age = 25
has_license = True
is_adult = age >= 18 and has_license  # Comparison before logical AND
print(f"is_adult = {is_adult}")       # True

# Complex expression
score = 85
bonus = 10
final_score = score + bonus if score >= 80 else score
print(f"Final score: {final_score}")  # 95

# Precedence table (highest to lowest):
# 1. Parentheses: ()
# 2. Exponentiation: **
# 3. Unary: +x, -x, ~x
# 4. Multiplication, Division: *, /, //, %
# 5. Addition, Subtraction: +, -
# 6. Bitwise shifts: <<, >>
# 7. Bitwise AND: &
# 8. Bitwise XOR: ^
# 9. Bitwise OR: |
# 10. Comparisons: ==, !=, <, >, <=, >=, is, is not, in, not in
# 11. Boolean NOT: not
# 12. Boolean AND: and
# 13. Boolean OR: or
# 14. Conditional expression: if-else
# 15. Assignment: =, +=, -=, etc.

print("\n=== Complex Expression ===")
# Let's trace through a complex expression
x, y, z = 5, 3, 2
result = x + y * z ** 2 > 20 and not x % 2 == 0
# Step by step:
# 1. z ** 2 = 2 ** 2 = 4
# 2. y * 4 = 3 * 4 = 12
# 3. x + 12 = 5 + 12 = 17
# 4. 17 > 20 = False
# 5. x % 2 = 5 % 2 = 1
# 6. 1 == 0 = False
# 7. not False = True
# 8. False and True = False
print(f"x + y * z ** 2 > 20 and not x % 2 == 0 = {result}")  # False
```

### Special Operators and Advanced Techniques

```python
# Walrus operator (Python 3.8+) - Assignment expressions
print("=== Walrus Operator (:=) ===")
# Traditional approach
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = []
for n in numbers:
    result = n ** 2
    if result > 25:
        squared.append(result)

print(f"Traditional: {squared}")

# With walrus operator
squared_walrus = [result for n in numbers if (result := n ** 2) > 25]
print(f"With walrus: {squared_walrus}")

# Useful in while loops
# while (line := input("Enter text (empty to quit): ")) != "":
#     print(f"You entered: {line}")

# Operator overloading in custom classes
print("\n=== Operator Overloading ===")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):           # Defines + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):          # Defines * operator
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):            # Defines == operator
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2    # Calls __add__
v4 = v1 * 2     # Calls __mul__

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v3}")
print(f"v1 * 2 = {v4}")
print(f"v1 == v2: {v1 == v2}")

# Ternary operator (conditional expression)
print(f"\n=== Ternary Operator ===")
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Multiple ternary operators (avoid overuse)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade: {grade}")

# Chained assignment with caution
print(f"\n=== Chained Assignment ===")
# Safe with immutable objects
a = b = c = 5
print(f"a={a}, b={b}, c={c}")

# Dangerous with mutable objects
list1 = list2 = []  # Both point to same list!
list1.append(1)
print(f"list1: {list1}, list2: {list2}")  # Both show [1]

# Safe way
list3, list4 = [], []
list3.append(1)
print(f"list3: {list3}, list4: {list4}")  # Only list3 shows [1]
```

**💡 Advanced Pro Tips:**

- **Precedence**: When in doubt, use parentheses for clarity
- **Short-circuit**: Leverage short-circuit evaluation for performance and safety
- **Chaining**: Use comparison chaining for readable range checks
- **Identity vs Equality**: Use `is` for None checks, `==` for value comparison
- **Bitwise**: Useful for flags, permissions, and low-level operations
- **Walrus**: Great for reducing redundant calculations in comprehensions
- **Type Mixing**: Be aware of automatic type promotion in arithmetic

**⚠️ Common Pitfalls:**
- Confusing `=` (assignment) with `==` (comparison)
- Not understanding operator precedence leading to unexpected results
- Using `==` instead of `is` for None comparisons
- Chained assignment with mutable objects creating shared references
- Forgetting that division `/` always returns float, even with integer operands

## 4. Conditional Statements

Conditional statements allow your program to make decisions and execute different code paths based on conditions. Python's conditional system is both powerful and elegant, supporting everything from simple if-else logic to complex pattern matching.

### Basic If-Else Structure

The foundation of decision making in Python:

```python
# Basic if-else structure
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")
else:
    print("You are a minor")
    print("You need parental consent for many activities")

# Understanding truthiness in conditions
user_input = input("Enter something (or press Enter): ")

# These are equivalent ways to check for empty input
if user_input:  # Pythonic way - checks truthiness
    print(f"You entered: {user_input}")
else:
    print("You entered nothing")

# Explicit comparison (less Pythonic but clearer for beginners)
if user_input != "":
    print(f"You entered: {user_input}")
else:
    print("You entered nothing")

# Understanding falsy values in conditions
test_values = [0, "", [], {}, None, False, 0.0]
for value in test_values:
    if value:
        print(f"{repr(value)} is truthy")
    else:
        print(f"{repr(value)} is falsy")  # All of these will print as falsy
```

### Multiple Conditions with elif

Building complex decision trees:

```python
# Multiple conditions - order matters!
score = 85

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory"
elif score >= 60:
    grade = "D"
    message = "Needs improvement"
else:
    grade = "F"
    message = "Please see instructor"

print(f"Score: {score}, Grade: {grade}")
print(f"Comment: {message}")

# Age categorization with detailed logic
age = 25
has_job = True
lives_alone = True

if age < 13:
    category = "Child"
    responsibilities = ["School", "Chores", "Learning"]
elif age < 18:
    category = "Teenager"
    responsibilities = ["School", "Part-time work", "Preparing for adulthood"]
elif age < 25:
    category = "Young Adult"
    if has_job:
        responsibilities = ["Career building", "Financial independence"]
    else:
        responsibilities = ["Job searching", "Skill development"]
elif age < 65:
    category = "Adult"
    responsibilities = ["Career", "Family", "Savings"]
    if lives_alone:
        responsibilities.append("Complete independence")
else:
    category = "Senior"
    responsibilities = ["Retirement planning", "Health maintenance"]

print(f"Age: {age}")
print(f"Category: {category}")
print(f"Key responsibilities: {', '.join(responsibilities)}")

# Demonstrating elif vs multiple if statements
number = 85

# Using elif (efficient - stops at first match)
print("=== Using elif ===")
if number >= 90:
    print("A grade")
elif number >= 80:  # This executes and stops here
    print("B grade")
elif number >= 70:  # This is skipped
    print("C grade")

# Using multiple if statements (inefficient - checks all conditions)
print("\n=== Using multiple if statements ===")
if number >= 90:
    print("A grade")
if number >= 80:    # This executes
    print("B grade")
if number >= 70:    # This also executes!
    print("C grade")
```

### Complex Conditions and Logical Operators

Combining multiple conditions for sophisticated logic:

```python
# Complex weather decision system
temperature = 75
humidity = 60
wind_speed = 10
is_sunny = True
chance_of_rain = 20

print(f"Weather conditions:")
print(f"Temperature: {temperature}°F")
print(f"Humidity: {humidity}%")
print(f"Wind speed: {wind_speed} mph")
print(f"Sunny: {is_sunny}")
print(f"Chance of rain: {chance_of_rain}%")

# Complex condition with multiple factors
if temperature > 70 and is_sunny and chance_of_rain < 30:
    if humidity < 70 and wind_speed < 15:
        activity = "Perfect for outdoor picnic!"
    elif wind_speed >= 15:
        activity = "Good for kite flying, but secure items"
    else:
        activity = "Nice day, but might feel muggy"
elif temperature > 60 and chance_of_rain < 50:
    activity = "Good for outdoor activities with light jacket"
elif chance_of_rain >= 50:
    activity = "Indoor activities recommended"
else:
    activity = "Stay warm indoors"

print(f"Recommended activity: {activity}")

# User authentication system
username = "alice"
password = "secret123"
is_account_locked = False
failed_attempts = 2
max_attempts = 3
is_admin = True

if not username or not password:
    print("Username and password are required")
elif is_account_locked:
    print("Account is locked. Contact administrator.")
elif failed_attempts >= max_attempts:
    print("Too many failed attempts. Account will be locked.")
elif username == "alice" and password == "secret123":
    if is_admin:
        print("Welcome, Administrator!")
        print("You have full system access")
    else:
        print("Welcome, User!")
        print("You have standard access")
else:
    print("Invalid credentials")
    failed_attempts += 1
    print(f"Failed attempts: {failed_attempts}/{max_attempts}")

# Membership and range checking
user_age = 25
valid_ages = range(18, 65)
premium_members = ["alice", "bob", "charlie"]
username = "alice"

if user_age in valid_ages and username in premium_members:
    print("Access granted: Premium member")
    discount = 0.20
elif user_age in valid_ages:
    print("Access granted: Standard member")
    discount = 0.10
elif user_age < 18:
    print("Access denied: Too young")
    discount = 0.0
else:
    print("Access granted: Senior discount")
    discount = 0.15

print(f"Discount applied: {discount:.0%}")
```

### Advanced Conditional Patterns

Sophisticated techniques for clean, efficient code:

```python
# Guard clauses - early returns for cleaner code
def process_order(items, user_type, payment_method):
    """Process an order with multiple validation checks"""

    # Guard clauses - handle edge cases first
    if not items:
        return "Error: No items in order"

    if user_type not in ["standard", "premium", "admin"]:
        return "Error: Invalid user type"

    if payment_method not in ["credit", "debit", "paypal"]:
        return "Error: Invalid payment method"

    # Main processing logic (now simpler)
    total = sum(item['price'] for item in items)

    if user_type == "premium":
        total *= 0.9  # 10% discount
    elif user_type == "admin":
        total *= 0.8  # 20% discount

    return f"Order processed: ${total:.2f} via {payment_method}"

# Test the function
sample_items = [{"name": "Book", "price": 20}, {"name": "Pen", "price": 5}]
result = process_order(sample_items, "premium", "credit")
print(result)

# Nested conditions vs flattened conditions
# Less readable - deeply nested
def check_access_nested(user):
    if user:
        if user.get('active'):
            if user.get('role') in ['admin', 'user']:
                if user.get('permissions'):
                    return "Access granted"
                else:
                    return "No permissions"
            else:
                return "Invalid role"
        else:
            return "Inactive user"
    else:
        return "No user provided"

# More readable - flattened with guard clauses
def check_access_flat(user):
    if not user:
        return "No user provided"

    if not user.get('active'):
        return "Inactive user"

    if user.get('role') not in ['admin', 'user']:
        return "Invalid role"

    if not user.get('permissions'):
        return "No permissions"

    return "Access granted"

# Test both approaches
test_user = {
    'active': True,
    'role': 'admin',
    'permissions': ['read', 'write']
}

print(f"Nested approach: {check_access_nested(test_user)}")
print(f"Flat approach: {check_access_flat(test_user)}")

# Dictionary-based dispatch (alternative to long if-elif chains)
def get_tax_rate_traditional(state):
    """Traditional if-elif approach"""
    if state == "CA":
        return 0.0725
    elif state == "NY":
        return 0.08
    elif state == "TX":
        return 0.0625
    elif state == "FL":
        return 0.06
    else:
        return 0.05  # default rate

def get_tax_rate_dict(state):
    """Dictionary-based approach - more scalable"""
    tax_rates = {
        "CA": 0.0725,
        "NY": 0.08,
        "TX": 0.0625,
        "FL": 0.06
    }
    return tax_rates.get(state, 0.05)  # default rate if state not found

# Both produce the same results but dict approach is more maintainable
print(f"CA tax rate (traditional): {get_tax_rate_traditional('CA'):.2%}")
print(f"CA tax rate (dictionary): {get_tax_rate_dict('CA'):.2%}")
```

### Ternary Operators and Conditional Expressions

Concise conditional logic for simple cases:

```python
# Basic ternary operator
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Multiple ternary operators (use sparingly)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(f"Grade: {grade}")

# Better approach for multiple conditions - use regular if-elif
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(f"Better grade calculation: {get_grade(85)}")

# Ternary for default values
name = ""
display_name = name if name else "Anonymous"  # or: name or "Anonymous"
print(f"Display name: {display_name}")

# Ternary in list comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
categories = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"Categories: {categories}")

# Ternary for function selection
import math

def safe_sqrt(number):
    return math.sqrt(number) if number >= 0 else f"Cannot calculate sqrt of {number}"

test_numbers = [16, -4, 0, 25]
for num in test_numbers:
    result = safe_sqrt(num)
    print(f"sqrt({num}) = {result}")

# Conditional assignment patterns
# Setting configuration based on environment
environment = "production"  # Could be "development", "staging", "production"

# Using ternary for simple cases
debug_mode = True if environment == "development" else False
log_level = "DEBUG" if debug_mode else "INFO"

# Using dictionary for multiple options
config = {
    "development": {"debug": True, "log_level": "DEBUG", "db_pool": 5},
    "staging": {"debug": False, "log_level": "INFO", "db_pool": 10},
    "production": {"debug": False, "log_level": "ERROR", "db_pool": 20}
}

settings = config.get(environment, config["production"])  # fallback to production
print(f"Environment: {environment}")
print(f"Settings: {settings}")

# Ternary with function calls (be careful with side effects)
def expensive_operation():
    print("Expensive operation called!")
    return "expensive_result"

def cheap_operation():
    print("Cheap operation called!")
    return "cheap_result"

use_expensive = False
# This calls the appropriate function
result = expensive_operation() if use_expensive else cheap_operation()
print(f"Result: {result}")
```

### Error Handling in Conditionals

Defensive programming with conditional checks:

```python
# Checking for None values
user_data = {"name": "Alice", "age": None, "email": "alice@example.com"}

# Safe way to check None
if user_data.get("age") is not None:
    if user_data["age"] >= 18:
        print("User is an adult")
    else:
        print("User is a minor")
else:
    print("Age information not available")

# Checking for empty collections
shopping_cart = []

if shopping_cart:  # Pythonic way
    total_items = len(shopping_cart)
    print(f"Cart has {total_items} items")
else:
    print("Cart is empty")

# Type checking in conditions
def process_data(data):
    """Safely process different types of data"""

    if isinstance(data, str):
        if data.strip():  # Check for non-empty string
            return f"Text length: {len(data)}"
        else:
            return "Empty text provided"

    elif isinstance(data, (int, float)):
        if data > 0:
            return f"Positive number: {data}"
        elif data < 0:
            return f"Negative number: {data}"
        else:
            return "Zero"

    elif isinstance(data, list):
        if data:  # Non-empty list
            return f"List with {len(data)} items: {data}"
        else:
            return "Empty list"

    elif isinstance(data, dict):
        if data:
            return f"Dictionary with keys: {list(data.keys())}"
        else:
            return "Empty dictionary"

    else:
        return f"Unsupported data type: {type(data)}"

# Test with different data types
test_data = ["hello", 42, -5, 0, [1, 2, 3], [], {"a": 1}, {}, None]
for data in test_data:
    result = process_data(data)
    print(f"process_data({repr(data)}) -> {result}")

# Safe attribute access
class User:
    def __init__(self, name, profile=None):
        self.name = name
        self.profile = profile

user1 = User("Alice", {"age": 25, "city": "NYC"})
user2 = User("Bob")  # No profile

# Safe way to access nested attributes
for user in [user1, user2]:
    print(f"User: {user.name}")

    # Check if profile exists and has the required key
    if hasattr(user, 'profile') and user.profile and 'age' in user.profile:
        age = user.profile['age']
        status = "adult" if age >= 18 else "minor"
        print(f"  Age: {age} ({status})")
    else:
        print("  Age: Unknown")

    # Using getattr with default
    profile = getattr(user, 'profile', {})
    city = profile.get('city', 'Unknown')
    print(f"  City: {city}")
```

### Best Practices and Common Patterns

Professional techniques for writing maintainable conditional code:

```python
# 1. Use constants for magic numbers
MIN_VOTING_AGE = 18
RETIREMENT_AGE = 65
SENIOR_DISCOUNT_AGE = 60

age = 25

if age >= MIN_VOTING_AGE:
    print("Eligible to vote")

if age >= SENIOR_DISCOUNT_AGE:
    print("Eligible for senior discount")

# 2. Extract complex conditions into functions
def is_business_hours(hour, day_of_week):
    """Check if current time is during business hours"""
    weekday = day_of_week < 5  # Monday=0, Friday=4
    business_hours = 9 <= hour < 17  # 9 AM to 5 PM
    return weekday and business_hours

def is_holiday(date):
    """Check if date is a holiday (simplified)"""
    holidays = ["2024-01-01", "2024-07-04", "2024-12-25"]
    return date in holidays

# Usage
current_hour = 14  # 2 PM
current_day = 2    # Wednesday
current_date = "2024-03-15"

if is_business_hours(current_hour, current_day) and not is_holiday(current_date):
    print("Office is open")
else:
    print("Office is closed")

# 3. Use enums for better code clarity
from enum import Enum

class UserRole(Enum):
    GUEST = "guest"
    USER = "user"
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"

class AccessLevel(Enum):
    NONE = 0
    READ = 1
    WRITE = 2
    DELETE = 3

def get_access_level(role):
    """Get access level based on user role"""
    access_map = {
        UserRole.GUEST: AccessLevel.NONE,
        UserRole.USER: AccessLevel.READ,
        UserRole.ADMIN: AccessLevel.WRITE,
        UserRole.SUPER_ADMIN: AccessLevel.DELETE
    }
    return access_map.get(role, AccessLevel.NONE)

user_role = UserRole.ADMIN
access = get_access_level(user_role)

if access.value >= AccessLevel.WRITE.value:
    print("User can modify data")
elif access.value >= AccessLevel.READ.value:
    print("User can view data")
else:
    print("User has no access")

# 4. Validation patterns
def validate_email(email):
    """Comprehensive email validation"""
    if not email:
        return False, "Email is required"

    if not isinstance(email, str):
        return False, "Email must be a string"

    email = email.strip()

    if not email:
        return False, "Email cannot be empty"

    if "@" not in email:
        return False, "Email must contain @ symbol"

    if email.count("@") != 1:
        return False, "Email must contain exactly one @ symbol"

    local, domain = email.split("@")

    if not local or not domain:
        return False, "Email must have both local and domain parts"

    if "." not in domain:
        return False, "Domain must contain a dot"

    return True, "Valid email"

# Test email validation
test_emails = ["user@example.com", "invalid", "", "user@@example.com", "user@", "@example.com"]

for email in test_emails:
    is_valid, message = validate_email(email)
    status = "✓" if is_valid else "✗"
    print(f"{status} {email}: {message}")
```

### Switch Case in Python (Match-Case - Python 3.10+)

Python doesn't have traditional switch statements, but uses **match-case** for pattern matching:

```python
# Basic match-case (Python 3.10+)
grade = 'B'

match grade:
    case 'A':
        print("Excellent! Grade: A")
    case 'B':
        print("Good job! Grade: B")        # Output: Good job! Grade: B
    case 'C':
        print("Average. Grade: C")
    case 'D':
        print("Below average. Grade: D")
    case _:  # Default case
        print("Invalid grade or F")

# Multiple values in one case
day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")                   # Output: Weekend
    case _:
        print("Invalid day")

# Match with conditions (guards)
score = 85

match score:
    case x if x >= 90:
        print("Grade: A")
    case x if x >= 80:
        print("Grade: B")                  # Output: Grade: B
    case x if x >= 70:
        print("Grade: C")
    case x if x >= 60:
        print("Grade: D")
    case _:
        print("Grade: F")

# Matching data structures
def process_data(data):
    match data:
        case {"type": "user", "name": str(name)}:
            return f"User: {name}"
        case {"type": "admin", "permissions": list(perms)}:
            return f"Admin with permissions: {perms}"
        case [first, *rest]:
            return f"List starting with {first}, rest: {rest}"
        case int(x) if x > 0:
            return f"Positive integer: {x}"
        case _:
            return "Unknown data type"

# Examples
print(process_data({"type": "user", "name": "Alice"}))     # Output: User: Alice
print(process_data([1, 2, 3, 4]))                        # Output: List starting with 1, rest: [2, 3, 4]
print(process_data(42))                                   # Output: Positive integer: 42
```

**💡 Pro Tips:**
- Python uses indentation (4 spaces) to group code blocks
- Use `elif` instead of multiple `if` statements for efficiency
- Match-case is more readable for complex pattern matching
- Use `_` as the default case in match statements
- Match-case supports destructuring of data structures

**🔍 Real-World Example:**
```python
# Grade calculator with match-case
score = 85

match score:
    case x if x >= 90:
        grade = "A"
    case x if x >= 80:
        grade = "B"
    case x if x >= 70:
        grade = "C"
    case x if x >= 60:
        grade = "D"
    case _:
        grade = "F"

print(f"Score: {score}, Grade: {grade}")                 # Output: Score: 85, Grade: B
```

## 5. Loops

Loops are fundamental control structures that allow you to repeat code blocks efficiently. Python provides powerful and flexible looping constructs that make iteration both readable and performant.

### Understanding Python's Iteration Protocol

Before diving into specific loop types, it's important to understand how Python handles iteration:

```python
# Understanding iterables vs iterators
print("=== Understanding Iteration ===")

# Iterables - objects that can be iterated over
my_list = [1, 2, 3, 4, 5]
my_string = "Hello"
my_dict = {"a": 1, "b": 2}

# Check if object is iterable
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

test_objects = [my_list, my_string, my_dict, 42, 3.14]
for obj in test_objects:
    print(f"{repr(obj)} is iterable: {is_iterable(obj)}")

# Getting an iterator from an iterable
my_iterator = iter(my_list)
print(f"\nIterator object: {my_iterator}")

# Manual iteration using next()
try:
    while True:
        item = next(my_iterator)
        print(f"Next item: {item}")
except StopIteration:
    print("Iterator exhausted")

# Behind the scenes of for loops
print("\n=== What for loops actually do ===")
# This for loop:
for item in [1, 2, 3]:
    print(item)

# Is equivalent to:
iterator = iter([1, 2, 3])
try:
    while True:
        item = next(iterator)
        print(item)
except StopIteration:
    pass
```

### For Loops - Iterate Over Sequences

The most common and Pythonic way to iterate:

```python
# Basic for loop with range
print("=== Basic For Loops ===")
for i in range(5):
    print(f"Iteration {i}")                # Output: Iteration 0, 1, 2, 3, 4

# Range with start, stop, step
print("\n=== Range Variations ===")
for i in range(2, 10, 2):  # start=2, stop=10, step=2
    print(f"Even number: {i}")             # Output: 2, 4, 6, 8

for i in range(10, 0, -2):  # Counting backwards
    print(f"Countdown: {i}")               # Output: 10, 8, 6, 4, 2

# Iterate over different data structures
print("\n=== Iterating Over Collections ===")

# Lists
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

# Strings (character by character)
word = "Python"
print("Letters in 'Python':")
for letter in word:
    print(letter, end=" ")                 # Output: P y t h o n
print()  # New line

# Tuples
coordinates = (10, 20, 30)
for coord in coordinates:
    print(f"Coordinate: {coord}")

# Sets (unordered)
unique_numbers = {3, 1, 4, 1, 5, 9}  # Note: duplicate 1 is removed
print(f"Unique numbers: {unique_numbers}")
for num in unique_numbers:
    print(f"Number: {num}")               # Order not guaranteed

# Advanced enumeration and indexing
print("\n=== Enumeration and Indexing ===")
fruits = ["apple", "banana", "cherry"]

# Basic enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")             # Output: 0: apple, 1: banana, 2: cherry

# Enumerate with custom start
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")            # Output: #1: apple, #2: banana, #3: cherry

# When you need both index and value
shopping_list = ["milk", "bread", "eggs", "cheese"]
for i, item in enumerate(shopping_list):
    if i == 0:
        print(f"First item: {item}")
    elif i == len(shopping_list) - 1:
        print(f"Last item: {item}")
    else:
        print(f"Item {i + 1}: {item}")

# Dictionary iteration patterns
print("\n=== Dictionary Iteration ===")
person = {"name": "Alice", "age": 30, "city": "NYC", "job": "Engineer"}

# Iterate over keys (default)
print("Keys:")
for key in person:
    print(f"  {key}")

# Iterate over values
print("Values:")
for value in person.values():
    print(f"  {value}")

# Iterate over key-value pairs (most common)
print("Key-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Filtering during iteration
print("Adult information only:")
for key, value in person.items():
    if key != "age" or value >= 18:
        print(f"  {key}: {value}")

# Multiple sequence iteration with zip
print("\n=== Multiple Sequence Iteration ===")
names = ["Alice", "Bob", "Charlie", "Diana"]
ages = [25, 30, 35, 28]
cities = ["NYC", "LA", "Chicago", "Miami"]

# Basic zip
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Triple zip
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, lives in {city}")

# Zip with different length sequences (stops at shortest)
scores = [85, 92, 78]  # Shorter than other lists
for name, score in zip(names, scores):
    print(f"{name} scored {score}")        # Only first 3 names

# Using zip for parallel processing
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = []
for a, b in zip(list1, list2):
    sums.append(a + b)
print(f"Sums: {sums}")                     # [11, 22, 33, 44]

# Reversing sequences
print("\n=== Reversing Sequences ===")
numbers = [1, 2, 3, 4, 5]

# Using reversed()
for num in reversed(numbers):
    print(f"Reversed: {num}")              # 5, 4, 3, 2, 1

# Using slicing (creates new list)
for num in numbers[::-1]:
    print(f"Sliced reverse: {num}")        # 5, 4, 3, 2, 1

# Sorting during iteration
print("\n=== Sorting During Iteration ===")
words = ["banana", "apple", "cherry", "date"]

# Alphabetical order
for word in sorted(words):
    print(f"Alphabetical: {word}")

# By length
for word in sorted(words, key=len):
    print(f"By length: {word}")

# Reverse alphabetical
for word in sorted(words, reverse=True):
    print(f"Reverse alphabetical: {word}")
```

### While Loops - Condition-Based Iteration

When you need to loop based on a condition rather than a sequence:

```python
# Basic while loop
print("=== Basic While Loop ===")
count = 0
print("Counting with while loop:")
while count < 3:
    print(f"Count: {count}")
    count += 1                             # Don't forget to update the condition!

# While loop with complex conditions
print("\n=== Complex Conditions ===")
balance = 1000
minimum_balance = 100
withdrawal = 150

while balance > minimum_balance and withdrawal > 0:
    if balance >= withdrawal:
        balance -= withdrawal
        print(f"Withdrew ${withdrawal}. Balance: ${balance}")
        withdrawal = int(input("Next withdrawal amount (0 to stop): ") or "0")
    else:
        print(f"Insufficient funds. Balance: ${balance}")
        break

# While loop for user input validation
print("\n=== Input Validation Loop ===")
def get_valid_age():
    while True:
        try:
            age_input = input("Enter your age (18-100): ")
            age = int(age_input)

            if 18 <= age <= 100:
                return age
            else:
                print("Age must be between 18 and 100")

        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None

# valid_age = get_valid_age()
# print(f"Valid age entered: {valid_age}")

# Infinite loop with break conditions
print("\n=== Infinite Loop Patterns ===")
import random

attempt = 1
max_attempts = 5

while True:  # Infinite loop
    guess = random.randint(1, 10)
    target = 7

    print(f"Attempt {attempt}: Guessed {guess}")

    if guess == target:
        print(f"Success! Found {target} in {attempt} attempts")
        break
    elif attempt >= max_attempts:
        print(f"Failed to find {target} in {max_attempts} attempts")
        break

    attempt += 1

# While loop for processing data until exhausted
print("\n=== Data Processing Loop ===")
data_queue = ["task1", "task2", "task3", "task4", "task5"]

while data_queue:  # Continue while list is not empty
    current_task = data_queue.pop(0)  # Remove first item
    print(f"Processing: {current_task}")

    # Simulate some processing time
    import time
    time.sleep(0.1)

    print(f"Completed: {current_task}")
    print(f"Remaining tasks: {len(data_queue)}")

print("All tasks completed!")

# While loop with else clause
print("\n=== While Loop with Else ===")
search_list = [2, 4, 6, 8, 10]
target = 7

i = 0
while i < len(search_list):
    if search_list[i] == target:
        print(f"Found {target} at index {i}")
        break
    i += 1
else:
    print(f"{target} not found in the list")  # This runs because no break occurred
```

### Loop Control Statements

Advanced control over loop execution:

```python
# Break - Exit loop immediately
print("=== Break Statement ===")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(f"Processing {i}")
# Output: 0, 1, 2, 3, 4, then "Breaking at 5"

# Continue - Skip to next iteration
print("\n=== Continue Statement ===")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")
# Output: 1, 3, 5, 7, 9

# Practical example: Processing files with error handling
print("\n=== Practical Example: File Processing ===")
filenames = ["data1.txt", "corrupted.txt", "data2.txt", "empty.txt", "data3.txt"]
processed_count = 0
max_files = 3

for filename in filenames:
    if processed_count >= max_files:
        print(f"Reached maximum files ({max_files})")
        break

    # Simulate different file conditions
    if "corrupted" in filename:
        print(f"Skipping corrupted file: {filename}")
        continue

    if "empty" in filename:
        print(f"Skipping empty file: {filename}")
        continue

    # Process valid file
    print(f"Processing file: {filename}")
    processed_count += 1

print(f"Total files processed: {processed_count}")

# Pass - Placeholder for future code
print("\n=== Pass Statement ===")
for i in range(5):
    if i == 2:
        pass  # TODO: Add special handling for index 2
    print(f"Item {i}")

# Loop else clause - Runs when loop completes without break
print("\n=== Loop Else Clause ===")

# Example 1: Search with else
def find_item(items, target):
    for i, item in enumerate(items):
        if item == target:
            return f"Found '{target}' at index {i}"
    else:
        return f"'{target}' not found"

numbers = [10, 20, 30, 40, 50]
print(find_item(numbers, 30))  # Found
print(find_item(numbers, 60))  # Not found

# Example 2: Prime number checker
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True  # Loop completed without finding a divisor

test_numbers = [2, 3, 4, 5, 15, 17, 25, 29]
for num in test_numbers:
    result = "prime" if is_prime(num) else "not prime"
    print(f"{num} is {result}")

# Nested loop control
print("\n=== Nested Loop Control ===")
matrix = [
    [1, 2, 3],
    [4, 0, 6],  # Contains zero
    [7, 8, 9]
]

target = 0
found = False

for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == target:
            print(f"Found {target} at position ({i}, {j})")
            found = True
            break
    if found:
        break  # Break outer loop too
else:
    print(f"{target} not found in matrix")

# Better approach using functions for nested loop control
def find_in_matrix(matrix, target):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                return (i, j)
    return None

position = find_in_matrix(matrix, 0)
if position:
    print(f"Found 0 at position {position}")
else:
    print("Value not found")
```

### Nested Loops and Complex Patterns

Advanced looping patterns for sophisticated tasks:

```python
# Multiplication table with formatting
print("=== Formatted Multiplication Table ===")
print("   ", end="")
for j in range(1, 6):
    print(f"{j:4}", end="")
print()

for i in range(1, 6):
    print(f"{i:2}:", end="")
    for j in range(1, 6):
        product = i * j
        print(f"{product:4}", end="")
    print()

# Creating patterns
print("\n=== Pattern Generation ===")

# Triangle pattern
print("Triangle:")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# Inverted triangle
print("\nInverted Triangle:")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Diamond pattern
print("\nDiamond:")
# Upper half
for i in range(5):
    print(" " * (4 - i) + "*" * (2 * i + 1))
# Lower half
for i in range(3, -1, -1):
    print(" " * (4 - i) + "*" * (2 * i + 1))

# Number pattern
print("\nNumber Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Matrix operations
print("\n=== Matrix Operations ===")
# Create a 3x3 matrix
matrix_a = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i * 3 + j + 1)
    matrix_a.append(row)

matrix_b = []
for i in range(3):
    row = []
    for j in range(3):
        row.append((i + 1) * (j + 1))
    matrix_b.append(row)

print("Matrix A:")
for row in matrix_a:
    for value in row:
        print(f"{value:3}", end="")
    print()

print("\nMatrix B:")
for row in matrix_b:
    for value in row:
        print(f"{value:3}", end="")
    print()

# Matrix addition
print("\nMatrix A + B:")
result_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result_matrix.append(row)

for row in result_matrix:
    for value in row:
        print(f"{value:3}", end="")
    print()

# Working with nested data structures
print("\n=== Nested Data Processing ===")
students = [
    {"name": "Alice", "grades": [85, 92, 78, 96]},
    {"name": "Bob", "grades": [79, 85, 88, 82]},
    {"name": "Charlie", "grades": [92, 88, 84, 90]}
]

# Calculate and display averages
print("Student Grade Report:")
print("-" * 40)
for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)

    print(f"{name}:")
    print(f"  Grades: {', '.join(map(str, grades))}")
    print(f"  Average: {average:.1f}")

    # Find highest and lowest grades
    highest = max(grades)
    lowest = min(grades)
    print(f"  Range: {lowest} - {highest}")
    print()

# Complex search in nested structures
print("=== Complex Search Example ===")
inventory = [
    {"category": "Electronics", "items": [
        {"name": "Laptop", "price": 999, "stock": 5},
        {"name": "Phone", "price": 699, "stock": 12}
    ]},
    {"category": "Books", "items": [
        {"name": "Python Guide", "price": 39, "stock": 20},
        {"name": "Data Science", "price": 45, "stock": 8}
    ]}
]

def find_item_by_name(inventory, item_name):
    for category in inventory:
        for item in category["items"]:
            if item["name"].lower() == item_name.lower():
                return {
                    "category": category["category"],
                    "item": item
                }
    return None

# Search for items
search_items = ["laptop", "python guide", "tablet"]
for search_term in search_items:
    result = find_item_by_name(inventory, search_term)
    if result:
        item = result["item"]
        category = result["category"]
        print(f"Found '{search_term}' in {category}: ${item['price']}, Stock: {item['stock']}")
    else:
        print(f"'{search_term}' not found")
```

### Loop Performance and Optimization

Understanding performance implications and optimization techniques:

```python
# Performance considerations
print("=== Performance Comparisons ===")
import time

# Timing different approaches
def time_operation(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start

# List comprehension vs loop
def loop_approach(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i ** 2)
    return result

def comprehension_approach(n):
    return [i ** 2 for i in range(n) if i % 2 == 0]

n = 10000
result1, time1 = time_operation(loop_approach, n)
result2, time2 = time_operation(comprehension_approach, n)

print(f"Loop approach: {time1:.4f} seconds")
print(f"Comprehension approach: {time2:.4f} seconds")
print(f"Speedup: {time1/time2:.2f}x faster" if time2 < time1 else f"Slowdown: {time2/time1:.2f}x slower")

# Memory efficiency with generators
print("\n=== Memory Efficiency ===")
import sys

# List (stores all values in memory)
large_list = [x ** 2 for x in range(1000)]
print(f"List memory usage: {sys.getsizeof(large_list)} bytes")

# Generator (computes values on demand)
large_generator = (x ** 2 for x in range(1000))
print(f"Generator memory usage: {sys.getsizeof(large_generator)} bytes")

# Using generator in loop
def process_large_dataset():
    for value in (x ** 2 for x in range(1000000)):
        if value > 1000000:
            return value
    return None

result = process_large_dataset()
print(f"First large value: {result}")

# Loop optimization techniques
print("\n=== Optimization Techniques ===")

# 1. Avoid repeated attribute lookup
class DataProcessor:
    def __init__(self):
        self.data = list(range(1000))

    def process_slow(self):
        result = []
        for item in self.data:
            if self.is_valid(item):  # Repeated method lookup
                result.append(self.transform(item))
        return result

    def process_fast(self):
        result = []
        is_valid = self.is_valid  # Cache method lookup
        transform = self.transform
        for item in self.data:
            if is_valid(item):
                result.append(transform(item))
        return result

    def is_valid(self, item):
        return item % 2 == 0

    def transform(self, item):
        return item ** 2

processor = DataProcessor()
result1, time1 = time_operation(processor.process_slow)
result2, time2 = time_operation(processor.process_fast)

print(f"Slow method: {time1:.4f} seconds")
print(f"Fast method: {time2:.4f} seconds")
print(f"Improvement: {time1/time2:.2f}x faster")

# 2. Use appropriate data structures
print("\n=== Data Structure Choice ===")

# Slow: checking membership in list
large_list = list(range(10000))
def find_in_list(target):
    return target in large_list

# Fast: checking membership in set
large_set = set(range(10000))
def find_in_set(target):
    return target in large_set

target = 9999
result1, time1 = time_operation(find_in_list, target)
result2, time2 = time_operation(find_in_set, target)

print(f"List lookup: {time1:.6f} seconds")
print(f"Set lookup: {time2:.6f} seconds")
print(f"Set is {time1/time2:.0f}x faster")
```

**💡 Advanced Pro Tips:**

- **Iteration Protocol**: Understanding iterators and iterables helps write more efficient code
- **Generator Expressions**: Use `(x for x in iterable)` for memory-efficient iteration
- **Built-in Functions**: Functions like `zip()`, `enumerate()`, and `reversed()` are optimized C implementations
- **List Comprehensions**: Generally faster than equivalent for loops for simple operations
- **Avoid Nested Loops**: Consider using dictionary lookups or set operations for better performance
- **Early Termination**: Use `break` and `continue` to avoid unnecessary iterations
- **Cache Lookups**: Store method/attribute lookups outside loops when possible

**⚠️ Common Pitfalls:**
- Modifying a list while iterating over it
- Infinite loops due to forgetting to update loop variables
- Using `range(len(list))` instead of direct iteration
- Not understanding the difference between `break` and `continue`
- Excessive nesting making code hard to read and maintain

## 6. Functions

Functions help organize code into reusable blocks:

### Basic Function Definition

```python
# Simple function
def greet(name):
    """This function greets someone by name"""
    print(f"Hello, {name}!")

greet("Maverick")                          # Output: Hello, Maverick!

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")                 # Output: 5 + 3 = 8

# Function with multiple returns
def get_name_age():
    return "Alice", 25

name, age = get_name_age()                 # Tuple unpacking
print(f"Name: {name}, Age: {age}")         # Output: Name: Alice, Age: 25
```

### Function Parameters and Arguments

```python
# Default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))           # Output: Hello, Mr. Smith!
print(greet_with_title("Johnson", "Dr."))  # Output: Hello, Dr. Johnson!

# Variable-length arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))                    # Output: 6
print(sum_all(1, 2, 3, 4, 5))              # Output: 15

# Keyword arguments (**kwargs)
def create_profile(**details):
    profile = "Profile:\n"
    for key, value in details.items():
        profile += f"  {key}: {value}\n"
    return profile

print(create_profile(name="Alice", age=30, city="NYC"))
# Output:
# Profile:
#   name: Alice
#   age: 30
#   city: NYC

# Mixed parameters (order matters: regular, *args, **kwargs)
def complex_function(required, default="default", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("must_have", "custom", 1, 2, 3, extra="info", debug=True)
# Output:
# Required: must_have
# Default: custom
# Args: (1, 2, 3)
# Kwargs: {'extra': 'info', 'debug': True}
```

### Advanced Function Concepts

```python
# Local vs Global scope
global_var = "I'm global"

def demo_scope():
    local_var = "I'm local"
    global global_var
    global_var = "Modified global"
    print(f"Local: {local_var}")
    print(f"Global inside function: {global_var}")

demo_scope()
print(f"Global outside: {global_var}")     # Output: Modified global

# Functions as first-class objects
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Store functions in variables
operations = [square, cube]
number = 4
for operation in operations:
    result = operation(number)
    print(f"{operation.__name__}({number}) = {result}")
# Output: square(4) = 16, cube(4) = 64

# Higher-order functions (functions that take other functions)
def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]

nums = [1, 2, 3, 4]
squared = apply_operation(nums, square)
print(f"Squared: {squared}")               # Output: [1, 4, 9, 16]

# Nested functions and closures
def outer_function(x):
    def inner_function(y):
        return x + y                       # x is captured from outer scope
    return inner_function

add_5 = outer_function(5)                  # Creates a closure
print(add_5(3))                            # Output: 8

# Recursive functions
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")              # Output: 5! = 120

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fib_sequence = [fibonacci(i) for i in range(8)]
print(f"Fibonacci: {fib_sequence}")        # Output: [0, 1, 1, 2, 3, 5, 8, 13]
```

### Function Documentation and Type Hints

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle

    Examples:
        >>> calculate_area(5)
        78.53981633974483
    """
    import math
    return math.pi * radius ** 2

# Using the function
area = calculate_area(5.0)
print(f"Area: {area:.2f}")                 # Output: Area: 78.54

# Check function documentation
print(calculate_area.__doc__)              # Prints the docstring
help(calculate_area)                       # Shows detailed help
```

**💡 Pro Tips:**
- Use descriptive function names that explain what they do
- Keep functions focused on a single task (Single Responsibility Principle)
- Use type hints for better code documentation and IDE support
- Write docstrings for complex functions
- Avoid global variables when possible - use parameters and return values

## 7. Data Structures

Python provides several built-in data structures, each optimized for different use cases:

### Lists - Ordered, Mutable Collections

Lists are the most versatile data structure in Python:

```python
# Creating lists
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
empty_list = []

# Adding elements
my_list.append(6)           # Add to end: [1, 2, 3, 4, 5, 6]
my_list.insert(0, 0)        # Insert at index 0: [0, 1, 2, 3, 4, 5, 6]
my_list.extend([7, 8])      # Add multiple: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Removing elements
my_list.remove(0)           # Remove first occurrence: [1, 2, 3, 4, 5, 6, 7, 8]
popped = my_list.pop()      # Remove and return last: 8, list: [1, 2, 3, 4, 5, 6, 7]
popped_at = my_list.pop(0)  # Remove at index 0: 1, list: [2, 3, 4, 5, 6, 7]
my_list.clear()             # Remove all elements: []

# List methods with examples
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")              # Output: [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Length: {len(numbers)}")           # Output: 8
print(f"Count of 1: {numbers.count(1)}")   # Output: 2
print(f"Index of 4: {numbers.index(4)}")   # Output: 2

# Sorting and reversing
numbers.sort()                             # Sort in place: [1, 1, 2, 3, 4, 5, 6, 9]
print(f"Sorted: {numbers}")
numbers.reverse()                          # Reverse in place: [9, 6, 5, 4, 3, 2, 1, 1]
print(f"Reversed: {numbers}")

# Slicing (doesn't modify original)
sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"First 3: {sample[:3]}")            # Output: [0, 1, 2]
print(f"Last 3: {sample[-3:]}")            # Output: [7, 8, 9]
print(f"Middle: {sample[3:7]}")            # Output: [3, 4, 5, 6]
print(f"Every 2nd: {sample[::2]}")         # Output: [0, 2, 4, 6, 8]
print(f"Reversed: {sample[::-1]}")         # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2                   # Output: [1, 2, 3, 4, 5, 6]
repeated = list1 * 3                       # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(f"Combined: {combined}")
print(f"Repeated: {repeated}")
```

### Strings - Immutable Text Sequences

Strings have many powerful methods for text manipulation:

```python
text = "  Hello, Python World!  "
sample = "python programming"

# Case methods
print(f"Upper: {text.upper()}")            # Output: "  HELLO, PYTHON WORLD!  "
print(f"Lower: {text.lower()}")            # Output: "  hello, python world!  "
print(f"Title: {sample.title()}")          # Output: "Python Programming"
print(f"Capitalize: {sample.capitalize()}") # Output: "Python programming"
print(f"Swapcase: {sample.swapcase()}")    # Output: "PYTHON PROGRAMMING"

# Whitespace methods
print(f"Strip: '{text.strip()}'")          # Output: "Hello, Python World!"
print(f"Left strip: '{text.lstrip()}'")    # Output: "Hello, Python World!  "
print(f"Right strip: '{text.rstrip()}'")   # Output: "  Hello, Python World!"

# Search methods
text_clean = text.strip()
print(f"Find 'Python': {text_clean.find('Python')}")      # Output: 7
print(f"Index 'World': {text_clean.index('World')}")      # Output: 14
print(f"Count 'o': {text_clean.count('o')}")              # Output: 2
print(f"Starts with 'Hello': {text_clean.startswith('Hello')}")  # Output: True
print(f"Ends with '!': {text_clean.endswith('!')}")       # Output: True

# Replace and split methods
replaced = text_clean.replace("Python", "Amazing")
print(f"Replaced: {replaced}")             # Output: "Hello, Amazing World!"

words = text_clean.split()                 # Split by whitespace
print(f"Words: {words}")                   # Output: ['Hello,', 'Python', 'World!']

csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print(f"Fruits: {fruits}")                 # Output: ['apple', 'banana', 'cherry']

# Join method
joined = " | ".join(fruits)
print(f"Joined: {joined}")                 # Output: "apple | banana | cherry"

# String validation methods
test_strings = ["123", "abc123", "Hello", "hello world", "   "]
for s in test_strings:
    print(f"'{s}' - digit: {s.isdigit()}, alpha: {s.isalpha()}, "
          f"alnum: {s.isalnum()}, space: {s.isspace()}")
# Output:
# '123' - digit: True, alpha: False, alnum: True, space: False
# 'abc123' - digit: False, alpha: False, alnum: True, space: False
# 'Hello' - digit: False, alpha: True, alnum: True, space: False
# 'hello world' - digit: False, alpha: False, alnum: False, space: False
# '   ' - digit: False, alpha: False, alnum: False, space: True

# String formatting
name = "Alice"
age = 30
score = 95.5
print(f"Name: {name}, Age: {age}, Score: {score:.1f}")    # Output: Name: Alice, Age: 30, Score: 95.5
print("Name: {}, Age: {}, Score: {:.1f}".format(name, age, score))  # Same output
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))        # Same output
```

### Dictionaries - Key-Value Mappings

Dictionaries store data as key-value pairs:

```python
# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}
dict_from_pairs = dict([("a", 1), ("b", 2), ("c", 3)])

# Accessing and modifying
print(f"Name: {person['name']}")           # Output: Alice
print(f"Age: {person.get('age')}")         # Output: 30
print(f"Country: {person.get('country', 'Unknown')}")  # Output: Unknown (default)

person["email"] = "alice@email.com"        # Add new key-value
person["age"] = 31                         # Update existing value
print(f"Updated person: {person}")

# Dictionary methods
student_grades = {"math": 95, "science": 88, "english": 92, "history": 85}

# Keys, values, and items
print(f"Subjects: {list(student_grades.keys())}")        # Output: ['math', 'science', 'english', 'history']
print(f"Grades: {list(student_grades.values())}")        # Output: [95, 88, 92, 85]
print(f"Items: {list(student_grades.items())}")          # Output: [('math', 95), ('science', 88), ...]

# Dictionary operations
print(f"Number of subjects: {len(student_grades)}")      # Output: 4
print(f"Has 'math': {'math' in student_grades}")         # Output: True
print(f"Has 'art': {'art' in student_grades}")           # Output: False

# Removing items
removed_grade = student_grades.pop("history")            # Remove and return: 85
print(f"Removed grade: {removed_grade}")
print(f"After removal: {student_grades}")

# Update and merge dictionaries
additional_grades = {"art": 90, "music": 87}
student_grades.update(additional_grades)                 # Merge dictionaries
print(f"After update: {student_grades}")

# Dictionary comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print(f"Squared: {squared_numbers}")                     # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Copying dictionaries
original = {"a": 1, "b": 2}
shallow_copy = original.copy()                           # Shallow copy
deep_copy = dict(original)                               # Another way to copy

# Clear dictionary
test_dict = {"x": 1, "y": 2}
test_dict.clear()                                        # Remove all items
print(f"Cleared dict: {test_dict}")                     # Output: {}
```

### Tuples - Ordered, Immutable Collections

```python
# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)                        # Note the comma for single item
empty_tuple = ()

# Accessing tuple elements
print(f"X coordinate: {coordinates[0]}")   # Output: 10
print(f"First color: {colors[0]}")         # Output: red
print(f"Last color: {colors[-1]}")         # Output: blue

# Tuple methods (limited since tuples are immutable)
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2: {numbers.count(2)}")  # Output: 3
print(f"Index of 3: {numbers.index(3)}")  # Output: 2

# Tuple unpacking
point = (5, 10)
x, y = point                               # Unpack into variables
print(f"X: {x}, Y: {y}")                  # Output: X: 5, Y: 10

# Multiple assignment
a, b, c = 1, 2, 3                         # Same as a, b, c = (1, 2, 3)
print(f"a={a}, b={b}, c={c}")             # Output: a=1, b=2, c=3
```

### Sets - Unordered Collections of Unique Elements

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 2, 4, 3, 5])      # Duplicates removed: {1, 2, 3, 4, 5}
empty_set = set()                          # Note: {} creates empty dict, not set

# Adding and removing elements
fruits.add("orange")                       # Add single element
fruits.update(["grape", "kiwi"])           # Add multiple elements
print(f"Fruits: {fruits}")

fruits.remove("banana")                    # Remove (raises error if not found)
fruits.discard("mango")                    # Remove (no error if not found)
popped_fruit = fruits.pop()                # Remove and return arbitrary element
print(f"After modifications: {fruits}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union: {set1 | set2}")            # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(f"Intersection: {set1 & set2}")     # Output: {4, 5}
print(f"Difference: {set1 - set2}")       # Output: {1, 2, 3}
print(f"Symmetric diff: {set1 ^ set2}")   # Output: {1, 2, 3, 6, 7, 8}

# Set methods
print(f"Is subset: {set1.issubset({1, 2, 3, 4, 5, 6})}")     # Output: True
print(f"Is superset: {set1.issuperset({1, 2})}")            # Output: True
print(f"Is disjoint: {set1.isdisjoint({9, 10})}")           # Output: True
```

**💡 Pro Tips:**
- Use lists for ordered, mutable collections
- Use tuples for ordered, immutable collections (like coordinates)
- Use sets for unique elements and fast membership testing
- Use dictionaries for key-value mappings and fast lookups
- List/dict comprehensions are often more readable than loops
- Remember that strings are immutable - methods return new strings

## 8. List Comprehensions

List comprehensions are a powerful and elegant way to create lists in Python. They provide a concise way to transform and filter data, making your code more readable and often faster than traditional loops.

### Basic List Comprehensions

The basic syntax is: `[expression for item in iterable]`

```python
# Traditional way with a loop
squares_traditional = []
for x in range(5):
    squares_traditional.append(x**2)
print(f"Traditional way: {squares_traditional}")

# List comprehension way (more Pythonic!)
squares_comprehension = [x**2 for x in range(5)]
print(f"List comprehension: {squares_comprehension}")

# Both produce: [0, 1, 4, 9, 16]
```

### List Comprehensions with Conditions

Add `if` conditions to filter elements: `[expression for item in iterable if condition]`

```python
# Get even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")  # [0, 2, 4, 6, 8]

# Get squares of odd numbers only
odd_squares = [x**2 for x in range(10) if x % 2 == 1]
print(f"Squares of odd numbers: {odd_squares}")  # [1, 9, 25, 49, 81]

# Filter words by length
words = ["python", "is", "awesome", "and", "powerful"]
long_words = [word for word in words if len(word) > 3]
print(f"Words longer than 3 characters: {long_words}")  # ['python', 'awesome', 'powerful']

# Transform and filter in one go
names = ["alice", "bob", "charlie", "diana"]
capitalized_short_names = [name.title() for name in names if len(name) <= 5]
print(f"Capitalized short names: {capitalized_short_names}")  # ['Alice', 'Bob', 'Diana']
```

### Working with Strings

```python
# Extract numbers from a string
text = "I have 3 cats, 2 dogs, and 15 fish"
numbers = [int(char) for char in text if char.isdigit()]
print(f"Numbers found: {numbers}")  # [3, 2, 1, 5]

# Convert to uppercase vowels only
sentence = "Python programming is fun"
vowels_upper = [char.upper() for char in sentence if char.lower() in 'aeiou']
print(f"Uppercase vowels: {vowels_upper}")  # ['o', 'o', 'a', 'i', 'i', 'u']

# Create acronym from words
phrase = "Application Programming Interface"
acronym = [word[0].upper() for word in phrase.split()]
print(f"Acronym: {''.join(acronym)}")  # API
```

### Nested List Comprehensions

Handle multi-dimensional data and complex transformations:

```python
# Flatten a 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a multiplication table
multiplication_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication table:")
for row in multiplication_table:
    print(row)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Extract specific elements from nested structure
students = [
    {"name": "Alice", "grades": [95, 87, 92]},
    {"name": "Bob", "grades": [78, 85, 90]},
    {"name": "Charlie", "grades": [88, 91, 85]}
]

# Get all grades from all students
all_grades = [grade for student in students for grade in student["grades"]]
print(f"All grades: {all_grades}")

# Get names of students with any grade above 90
high_achievers = [student["name"] for student in students
                 if any(grade > 90 for grade in student["grades"])]
print(f"High achievers: {high_achievers}")  # ['Alice', 'Charlie']
```

### Dictionary and Set Comprehensions

Python also supports dictionary and set comprehensions with similar syntax:

```python
# Dictionary comprehensions {key: value for item in iterable}
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print(f"Squares dictionary: {squares_dict}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Create word length dictionary
words = ["python", "java", "javascript", "go", "rust"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Set comprehensions {expression for item in iterable}
text = "programming"
unique_letters = {letter for letter in text if letter != 'm'}
print(f"Unique letters (no 'm'): {unique_letters}")  # {'p', 'r', 'o', 'g', 'a', 'n', 'i'}

# Get unique word lengths
sentences = ["Python is great", "I love coding", "Data science rocks"]
unique_word_lengths = {len(word) for sentence in sentences for word in sentence.split()}
print(f"Unique word lengths: {unique_word_lengths}")
```

### Advanced List Comprehensions

```python
# Conditional expressions (ternary operator in comprehensions)
numbers = [-2, -1, 0, 1, 2, 3]
abs_or_zero = [abs(x) if x != 0 else "zero" for x in numbers]
print(f"Absolute values or zero: {abs_or_zero}")  # [2, 1, 'zero', 1, 2, 3]

# Multiple conditions
ages = [15, 22, 17, 30, 25, 16, 45]
categories = [
    "teen" if 13 <= age <= 19
    else "young adult" if 20 <= age <= 29
    else "adult" if 30 <= age <= 49
    else "senior"
    for age in ages
]
print(f"Age categories: {categories}")

# Working with enumerate for index and value
fruits = ["apple", "banana", "cherry", "date"]
indexed_fruits = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
print(f"Indexed fruits: {indexed_fruits}")

# Zip multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]
profiles = [f"{name} ({age}) from {city}"
           for name, age, city in zip(names, ages, cities)]
print(f"Profiles: {profiles}")
```

### Performance and When to Use

```python
import time

# Performance comparison: List comprehension vs traditional loop
def time_traditional_loop():
    start = time.time()
    result = []
    for i in range(100000):
        if i % 2 == 0:
            result.append(i**2)
    end = time.time()
    return end - start, len(result)

def time_list_comprehension():
    start = time.time()
    result = [i**2 for i in range(100000) if i % 2 == 0]
    end = time.time()
    return end - start, len(result)

# Run performance tests
loop_time, loop_count = time_traditional_loop()
comp_time, comp_count = time_list_comprehension()

print(f"Traditional loop: {loop_time:.4f}s, {loop_count} items")
print(f"List comprehension: {comp_time:.4f}s, {comp_count} items")
print(f"List comprehension is {loop_time/comp_time:.2f}x faster!")
```

**💡 Pro Tips:**
- List comprehensions are generally faster than equivalent for loops
- Use comprehensions for simple transformations and filtering
- For complex logic, traditional loops might be more readable
- Dictionary and set comprehensions follow the same pattern
- You can use multiple `for` clauses and `if` conditions in one comprehension

**⚠️ When NOT to Use Comprehensions:**
- When the logic becomes too complex (readability matters!)
- When you need to handle exceptions within the loop
- When you need to break out of the loop early
- When the resulting line becomes too long (PEP 8 recommends max 79 characters)

**🔍 Real-World Examples:**

```python
# Data processing example
sales_data = [
    {"product": "laptop", "price": 999, "quantity": 2, "category": "electronics"},
    {"product": "mouse", "price": 25, "quantity": 10, "category": "electronics"},
    {"product": "book", "price": 15, "quantity": 5, "category": "books"},
    {"product": "headphones", "price": 150, "quantity": 3, "category": "electronics"}
]

# Calculate total revenue for electronics over $50
electronics_revenue = [
    item["price"] * item["quantity"]
    for item in sales_data
    if item["category"] == "electronics" and item["price"] > 50
]
print(f"Electronics revenue (>$50): ${sum(electronics_revenue)}")

# Create product summary with discounted prices
product_summary = [
    {
        "product": item["product"],
        "original_price": item["price"],
        "discounted_price": item["price"] * 0.9,  # 10% discount
        "total_value": item["price"] * item["quantity"] * 0.9
    }
    for item in sales_data
    if item["quantity"] > 2  # Only items with quantity > 2
]

for summary in product_summary:
    print(f"{summary['product']}: ${summary['original_price']} → ${summary['discounted_price']:.2f}")

# Text analysis example
text = "The quick brown fox jumps over the lazy dog"
word_analysis = [
    {
        "word": word,
        "length": len(word),
        "vowels": sum(1 for char in word.lower() if char in 'aeiou'),
        "consonants": sum(1 for char in word.lower() if char.isalpha() and char not in 'aeiou')
    }
    for word in text.split()
    if len(word) > 3  # Only analyze words longer than 3 characters
]

print("\nWord analysis:")
for analysis in word_analysis:
    print(f"{analysis['word']}: {analysis['length']} letters, "
          f"{analysis['vowels']} vowels, {analysis['consonants']} consonants")
```

**🚀 Advanced Techniques:**

```python
# Flattening nested lists with conditions
nested_numbers = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
even_numbers = [num for sublist in nested_numbers for num in sublist if num % 2 == 0]
print(f"Even numbers from nested lists: {even_numbers}")

# Creating combinations
colors = ["red", "blue", "green"]
sizes = ["small", "large"]
combinations = [f"{color} {size}" for color in colors for size in sizes]
print(f"Color-size combinations: {combinations}")

# Matrix operations
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

# Matrix addition using list comprehensions
matrix_sum = [
    [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
    for i in range(len(matrix_a))
]
print(f"Matrix sum: {matrix_sum}")
```

List comprehensions are one of Python's most elegant features. They make code more concise, readable, and often faster than traditional loops. Master them, and your Python code will become much more Pythonic!

## 9. String Manipulation

```python
text = "Python is fun!"
print(text.upper())
print(text.lower())
print(text.replace("fun", "awesome"))
print(text.find("is"))
print(text.count("n"))
print(text.split())
print(" ".join(["Python", "is", "cool"]))
print("   padded text   ".strip())
print(text.startswith("Python"))
print(text.endswith("!"))
print("12345".isdigit())
print("Hello".isalpha())
print(f"Hello, {name}!")
```

## 10. Exception Handling

Handle errors gracefully to make your programs robust:

### Basic Exception Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")       # Output: Cannot divide by zero!

# Handling multiple exceptions
def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None

print(safe_division(10, 2))                # Output: 5.0
print(safe_division(10, 0))                # Output: Error: Cannot divide by zero, None
print(safe_division("10", 2))              # Output: Error: Invalid types for division, None
```

### Advanced Exception Handling

```python
# Multiple exceptions in one except block
def process_data(data):
    try:
        # Convert to integer and perform calculation
        number = int(data)
        result = 100 / number
        return result
    except (ValueError, TypeError):
        print(f"Invalid input: {data}")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

print(process_data("5"))                   # Output: 20.0
print(process_data("abc"))                 # Output: Invalid input: abc, None
print(process_data(0))                     # Output: Cannot divide by zero, None

# Catching all exceptions (use sparingly)
def risky_operation(data):
    try:
        # Some risky operation
        result = eval(data)  # Never do this in real code!
        return result
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}: {e}")
        return None

print(risky_operation("2 + 3"))            # Output: 5
print(risky_operation("2 / 0"))            # Output: An error occurred: ZeroDivisionError: division by zero

# Getting exception details
import traceback

def detailed_error_handling():
    try:
        numbers = [1, 2, 3]
        print(numbers[10])  # This will raise IndexError
    except IndexError as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Exception args: {e.args}")
        print("Full traceback:")
        traceback.print_exc()

detailed_error_handling()
```

### Try-Except-Else-Finally

```python
# Complete exception handling structure
def file_operations(filename):
    file = None
    try:
        print(f"Trying to open {filename}")
        file = open(filename, 'r')
        content = file.read()
        print(f"File content: {content}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    except PermissionError:
        print(f"Permission denied for {filename}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        # Runs only if no exception occurred
        print("File read successfully!")
    finally:
        # Always runs, regardless of exceptions
        if file and not file.closed:
            file.close()
            print("File closed.")
        print("Cleanup completed.")

# Test with non-existent file
file_operations("nonexistent.txt")

# Better approach using context managers
def safe_file_read(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return None
    except PermissionError:
        print(f"Permission denied for {filename}")
        return None
    # File automatically closed due to 'with' statement
```

### Custom Exceptions

```python
# Creating custom exception classes
class CustomError(Exception):
    """Base custom exception"""
    pass

class ValidationError(CustomError):
    """Raised when validation fails"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code

class DatabaseError(CustomError):
    """Raised when database operations fail"""
    pass

# Using custom exceptions
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("Age must be an integer", error_code="TYPE_ERROR")
    if age < 0:
        raise ValidationError("Age cannot be negative", error_code="VALUE_ERROR")
    if age > 150:
        raise ValidationError("Age seems unrealistic", error_code="RANGE_ERROR")
    return True

# Testing custom exceptions
test_ages = [25, -5, "abc", 200]

for age in test_ages:
    try:
        validate_age(age)
        print(f"Age {age} is valid")
    except ValidationError as e:
        print(f"Validation failed for {age}: {e} (Code: {e.error_code})")

# Exception chaining
def process_user_data(user_data):
    try:
        age = user_data['age']
        validate_age(age)
    except KeyError as e:
        raise ValidationError("Missing required field") from e
    except ValidationError:
        raise  # Re-raise the same exception

try:
    process_user_data({'name': 'Alice'})  # Missing 'age' key
except ValidationError as e:
    print(f"Processing failed: {e}")
    print(f"Original cause: {e.__cause__}")
```

### Practical Exception Handling Patterns

```python
# Retry pattern
import time
import random

def unreliable_operation():
    """Simulates an operation that sometimes fails"""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network timeout")
    return "Success!"

def retry_operation(max_attempts=3, delay=1):
    for attempt in range(max_attempts):
        try:
            result = unreliable_operation()
            print(f"Operation succeeded on attempt {attempt + 1}")
            return result
        except ConnectionError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max attempts reached. Operation failed.")
                raise

# result = retry_operation()

# Input validation pattern
def get_valid_integer(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            return None

# age = get_valid_integer("Enter your age (0-120): ", 0, 120)

# Graceful degradation pattern
def get_user_preference(user_id):
    """Try multiple methods to get user preference"""
    try:
        # Try primary method (database)
        return get_from_database(user_id)
    except DatabaseError:
        try:
            # Fallback to cache
            return get_from_cache(user_id)
        except Exception:
            # Last resort: return default
            return get_default_preference()

def get_from_database(user_id):
    raise DatabaseError("Database unavailable")

def get_from_cache(user_id):
    raise Exception("Cache miss")

def get_default_preference():
    return {"theme": "light", "language": "en"}

user_pref = get_user_preference("user123")
print(f"User preference: {user_pref}")     # Output: User preference: {'theme': 'light', 'language': 'en'}
```

**💡 Pro Tips:**
- Be specific with exception types - catch what you can handle
- Use `finally` for cleanup code that must run
- Prefer context managers (`with` statement) for resource management
- Log exceptions for debugging, but don't expose internal errors to users
- Create custom exceptions for domain-specific errors
- Use exception chaining to preserve error context

## 11. Classes and Objects

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
p = Person("Maverick", 25)
p.introduce()
```

## 12. File Handling

```python
with open("example.txt", "w") as f:
    f.write("Hello, file!")
with open("example.txt", "r") as f:
    print(f.read())
```

## 13. Modules and Imports

```python
import math
print(math.sqrt(16))
```

## 14. Useful Built-in Functions

Python provides many powerful built-in functions that make coding more efficient and readable:

### Mathematical Functions

```python
# Basic math functions
nums = [5, 2, 9, 1, 8]
print(max(nums))           # Output: 9 (largest value)
print(min(nums))           # Output: 1 (smallest value)
print(sum(nums))           # Output: 25 (sum of all values)
print(abs(-10))            # Output: 10 (absolute value)
print(pow(2, 3))           # Output: 8 (2 to the power of 3)
print(round(3.14159, 2))   # Output: 3.14 (round to 2 decimal places)

# Advanced math (requires import math)
import math
print(math.sqrt(16))       # Output: 4.0 (square root)
print(math.ceil(4.2))      # Output: 5 (round up)
print(math.floor(4.8))     # Output: 4 (round down)
```

### Type Conversion Functions

```python
# Converting between types
print(int("123"))          # Output: 123 (string to integer)
print(int(3.14))           # Output: 3 (float to integer)
print(float("3.14"))       # Output: 3.14 (string to float)
print(str(123))            # Output: '123' (integer to string)
print(bool(1))             # Output: True (any non-zero is True)
print(bool(0))             # Output: False (zero is False)
print(list("hello"))       # Output: ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))    # Output: (1, 2, 3)
print(set([1, 2, 2, 3]))   # Output: {1, 2, 3} (removes duplicates)
```

### Sequence Functions

```python
# Working with sequences
data = [5, 2, 9, 1, 8]
text = "hello"

print(len(data))           # Output: 5 (length of list)
print(len(text))           # Output: 5 (length of string)
print(sorted(data))        # Output: [1, 2, 5, 8, 9] (returns new sorted list)
print(list(reversed(data))) # Output: [8, 1, 9, 2, 5] (reversed list)
print(list(enumerate(data))) # Output: [(0, 5), (1, 2), (2, 9), (3, 1), (4, 8)]

# range() - generates sequences of numbers
print(list(range(5)))      # Output: [0, 1, 2, 3, 4]
print(list(range(2, 8)))   # Output: [2, 3, 4, 5, 6, 7]
print(list(range(0, 10, 2))) # Output: [0, 2, 4, 6, 8] (step by 2)
```

### Logical Functions

```python
# Boolean logic functions
scores = [85, 92, 78, 95, 88]
grades = [0, 0, 0]

print(any(score > 90 for score in scores))  # Output: True (at least one > 90)
print(all(score > 70 for score in scores))  # Output: True (all > 70)
print(any(grades))                          # Output: False (no truthy values)
print(all(grades))                          # Output: False (not all truthy)

# Combining sequences
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print(list(zip(names, ages)))              # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]
print(list(zip(nums1, nums2, nums3)))      # Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

### Input/Output Functions

```python
# Getting input and displaying output
name = input("Enter your name: ")          # Gets user input as string
age = int(input("Enter your age: "))       # Convert input to integer

print("Hello", name)                       # Output: Hello [name]
print("Name:", name, "Age:", age)          # Output: Name: [name] Age: [age]
print(f"Hi {name}, you are {age} years old") # f-string formatting

# Advanced print options
print("Loading", end="")                   # No newline at end
print(".", end="")                         # Output: Loading...
print(".", end="")
print(" Done!")                           # Output: Loading... Done!

print("apple", "banana", "cherry", sep=", ") # Output: apple, banana, cherry
```

### Utility Functions

```python
# Object inspection and utilities
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}

print(type(my_list))       # Output: <class 'list'>
print(type(42))            # Output: <class 'int'>
print(isinstance(my_list, list))  # Output: True
print(isinstance(42, str))        # Output: False

print(id(my_list))         # Output: unique object ID
print(dir(my_list))        # Output: list of available methods
print(help(len))           # Output: documentation for len function

# Variable checking
x = 10
print(vars())              # Output: dictionary of local variables
print(globals().keys())    # Output: global variable names
```

### Filter and Map Functions

```python
# Filter - selects elements that meet a condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)               # Output: [2, 4, 6, 8, 10]

# Map - applies function to all elements
squares = list(map(lambda x: x**2, numbers))
print(squares)             # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Map with multiple iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(sums)                # Output: [5, 7, 9]
```

### Advanced Built-in Functions

```python
# eval() and exec() - execute code from strings (use carefully!)
result = eval("2 + 3 * 4")
print(result)              # Output: 14

# hasattr() and getattr() - check and get object attributes
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(hasattr(p, 'name'))  # Output: True
print(getattr(p, 'name'))  # Output: Alice
print(getattr(p, 'age', 'Unknown'))  # Output: Unknown (default value)

# callable() - check if object can be called
print(callable(print))     # Output: True
print(callable(42))        # Output: False

# ord() and chr() - character/ASCII conversions
print(ord('A'))            # Output: 65 (ASCII value)
print(chr(65))             # Output: A (character from ASCII)
```

**💡 Pro Tips:**
- Use `help(function_name)` to get documentation for any function
- Many functions return iterators - use `list()` to see all results
- `filter()` and `map()` are memory-efficient alternatives to list comprehensions
- Always validate input when using `eval()` - it can execute any Python code
- Use `isinstance()` instead of `type()` for type checking (handles inheritance)

## 15. Decorators

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@my_decorator
def say_hi():
    print("Hi!")
say_hi()
```

## 16. Generators

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(3):
    print(num)
```

## 17. Lambda Functions

```python
add = lambda x, y: x + y
print(add(2, 3))
```

## 18. Map, Filter, Reduce

```python
nums = [1, 2, 3, 4]
print(list(map(lambda x: x**2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
from functools import reduce
print(reduce(lambda x, y: x + y, nums))
```

## 19. Context Managers

```python
with open("example.txt", "w") as f:
    f.write("Context manager example.")
import sqlite3
with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    conn.commit()
```

## 20. Inheritance & Polymorphism

```python
class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def speak(self):
        print("Woof!")
pet = Dog()
pet.speak()
```

## 21. Exception Chaining & Custom Exceptions

```python
class MyError(Exception):
    pass
try:
    raise MyError("Custom error!")
except MyError as e:
    print("Caught exception:", e)
```

## 22. Type Hinting

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
print(add_numbers(2, 5))
```

## 23. Concurrency (Threading & Multiprocessing)

```python
import threading, multiprocessing, time
# Threading

def worker():
    print("Thread starting")
    time.sleep(1)
    print("Thread finished")
t = threading.Thread(target=worker)
t.start()
t.join()
# Multiprocessing

def process_worker():
    print("Process running")
p = multiprocessing.Process(target=process_worker)
p.start()
p.join()
```

## 24. Metaclasses

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)
class MyClass(metaclass=Meta):
    pass
```

## 25. Property Decorators

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def area(self):
        return self._width * self._height
r = Rectangle(3, 4)
print(r.area)
```

## 26. Async/Await

```python
import asyncio
async def async_hello():
    await asyncio.sleep(1)
    print("Hello from async!")
# asyncio.run(async_hello())
```

## 27. Data Classes

```python
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
pt = Point(2, 3)
print(pt)
```

## 28. Testing (unittest)

```python
import unittest
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)
# if __name__ == "__main__":
#     unittest.main()
```

## 29. Packaging & Virtual Environments

- Use `pip` to install packages: `pip install requests`
- Create virtual environment: `python -m venv env`
- Activate: `source env/bin/activate` (macOS/Linux) or `.\env\Scripts\activate` (Windows)
- Requirements file: `pip freeze > requirements.txt`

## 30. Regular Expressions

Regular expressions (regex) are powerful tools for pattern matching and text processing:

```python
import re

# Basic pattern matching
text = "The phone numbers are 123-456-7890 and 555-123-4567"

# Find all phone numbers
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print(f"Found phones: {phones}")           # Output: ['123-456-7890', '555-123-4567']

# Check if pattern exists
if re.search(phone_pattern, text):
    print("Phone number found!")           # Output: Phone number found!

# Replace patterns
censored = re.sub(phone_pattern, "XXX-XXX-XXXX", text)
print(f"Censored: {censored}")             # Output: The phone numbers are XXX-XXX-XXXX and XXX-XXX-XXXX

# Common patterns
email_text = "Contact us at john@example.com or support@company.org"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, email_text)
print(f"Emails found: {emails}")           # Output: ['john@example.com', 'support@company.org']

# URL extraction
url_text = "Visit https://www.example.com or http://test.org for more info"
url_pattern = r'https?://[^\s]+'
urls = re.findall(url_pattern, url_text)
print(f"URLs found: {urls}")               # Output: ['https://www.example.com', 'http://test.org']

# Groups and capturing
date_text = "Today is 2024-03-15 and yesterday was 2024-03-14"
date_pattern = r'(\d{4})-(\d{2})-(\d{2})'
dates = re.findall(date_pattern, date_text)
print(f"Dates (year, month, day): {dates}") # Output: [('2024', '03', '15'), ('2024', '03', '14')]

# Named groups
match = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', date_text)
if match:
    print(f"Year: {match.group('year')}")   # Output: Year: 2024
    print(f"Month: {match.group('month')}")  # Output: Month: 03
```

## 31. Working with JSON

JSON (JavaScript Object Notation) is a popular data format:

```python
import json

# Python dictionary to JSON
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "is_employed": True,
    "salary": None
}

# Convert to JSON string
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)
# Output:
# {
#   "name": "Alice",
#   "age": 30,
#   "skills": ["Python", "JavaScript", "SQL"],
#   "is_employed": true,
#   "salary": null
# }

# Parse JSON string back to Python
parsed_data = json.loads(json_string)
print(f"Parsed name: {parsed_data['name']}")  # Output: Parsed name: Alice

# Working with JSON files
# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read from file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
    print(f"Loaded data: {loaded_data}")

# Handling JSON errors
invalid_json = '{"name": "Alice", "age":}'  # Missing value
try:
    parsed = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON parsing error: {e}")       # Output: JSON parsing error: ...
```

## 32. Working with Dates and Times

Python's datetime module provides comprehensive date and time functionality:

```python
from datetime import datetime, date, time, timedelta
import time as time_module

# Current date and time
now = datetime.now()
today = date.today()
current_time = datetime.now().time()

print(f"Now: {now}")                       # Output: Now: 2024-03-15 14:30:25.123456
print(f"Today: {today}")                   # Output: Today: 2024-03-15
print(f"Current time: {current_time}")     # Output: Current time: 14:30:25.123456

# Creating specific dates
birthday = date(1990, 5, 15)
meeting_time = datetime(2024, 3, 20, 14, 30, 0)
print(f"Birthday: {birthday}")             # Output: Birthday: 1990-05-15
print(f"Meeting: {meeting_time}")          # Output: Meeting: 2024-03-20 14:30:00

# Formatting dates
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")           # Output: Formatted: 2024-03-15 14:30:25

friendly_format = now.strftime("%B %d, %Y at %I:%M %p")
print(f"Friendly: {friendly_format}")      # Output: Friendly: March 15, 2024 at 02:30 PM

# Parsing date strings
date_string = "2024-03-15 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed: {parsed_date}")            # Output: Parsed: 2024-03-15 14:30:00

# Date arithmetic
one_week_later = today + timedelta(days=7)
one_month_ago = now - timedelta(days=30)
print(f"One week later: {one_week_later}") # Output: One week later: 2024-03-22
print(f"One month ago: {one_month_ago}")   # Output: One month ago: 2024-02-14 14:30:25.123456

# Time differences
age = today - birthday
print(f"Age in days: {age.days}")          # Output: Age in days: 12326

# Working with timestamps
timestamp = time_module.time()
from_timestamp = datetime.fromtimestamp(timestamp)
print(f"Timestamp: {timestamp}")           # Output: Timestamp: 1710511825.123
print(f"From timestamp: {from_timestamp}") # Output: From timestamp: 2024-03-15 14:30:25.123456
```

---

## 🎯 Practical Exercises & Projects

### Beginner Projects (Choose 1-2 to start)

#### 1. **Personal Information Manager**
```python
# Create a program that:
# - Asks for user's name, age, favorite color
# - Calculates birth year
# - Creates a personalized greeting
# - Saves info to a file

name = input("What's your name? ")
age = int(input("How old are you? "))
color = input("What's your favorite color? ")

birth_year = 2024 - age
print(f"Hello {name}! You were born in {birth_year}.")
print(f"Your favorite color {color} is awesome!")
```

#### 2. **Number Guessing Game**
```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("I'm thinking of a number between 1 and 100!")
print(f"You have {max_attempts} attempts to guess it.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print(f"🎉 Congratulations! You found it in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low! Try higher.")
    else:
        print("Too high! Try lower.")

    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Attempts remaining: {remaining}")
else:
    print(f"Game over! The number was {secret}")
```

#### 3. **Simple Calculator**
```python
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, **")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation: ")
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Cannot divide by zero!")
                    continue
            elif operation == '**':
                result = num1 ** num2
            else:
                print("Invalid operation!")
                continue

            print(f"Result: {num1} {operation} {num2} = {result}")

            if input("Continue? (y/n): ").lower() != 'y':
                break

        except ValueError:
            print("Please enter valid numbers!")

calculator()
```

### Intermediate Projects

#### 4. **Todo List Manager**
```python
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added: {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Completed: {self.tasks[index]['task']}")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return

        for i, task in enumerate(self.tasks):
            status = "✅" if task["completed"] else "❌"
            print(f"{i+1}. {status} {task['task']}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed: {removed['task']}")

# Usage example
todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Build a project")
todo.show_tasks()
todo.complete_task(0)
todo.show_tasks()
```

#### 5. **File-Based Student Grade Manager**
```python
import json

class GradeManager:
    def __init__(self, filename="grades.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.students = json.load(f)
        except FileNotFoundError:
            self.students = {}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=2)

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = []
            print(f"Added student: {name}")
        else:
            print(f"Student {name} already exists!")

    def add_grade(self, name, subject, grade):
        if name in self.students:
            self.students[name].append({"subject": subject, "grade": grade})
            print(f"Added grade for {name}: {subject} - {grade}")
        else:
            print(f"Student {name} not found!")

    def get_average(self, name):
        if name in self.students and self.students[name]:
            grades = [item['grade'] for item in self.students[name]]
            return sum(grades) / len(grades)
        return 0

    def show_report(self, name):
        if name in self.students:
            print(f"\n--- {name}'s Report ---")
            for item in self.students[name]:
                print(f"{item['subject']}: {item['grade']}")
            print(f"Average: {self.get_average(name):.2f}")
        else:
            print(f"Student {name} not found!")

# Usage
gm = GradeManager()
gm.add_student("Alice")
gm.add_grade("Alice", "Math", 95)
gm.add_grade("Alice", "Science", 88)
gm.show_report("Alice")
gm.save_data()
```

### Advanced Challenges

#### 6. **Web Scraper with Error Handling**
```python
import requests
from bs4 import BeautifulSoup
import csv
import time

class WebScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def scrape_quotes(self, max_pages=3):
        quotes = []

        for page in range(1, max_pages + 1):
            try:
                url = f"http://quotes.toscrape.com/page/{page}/"
                response = self.session.get(url, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.content, 'html.parser')
                quote_elements = soup.find_all('div', class_='quote')

                for quote_elem in quote_elements:
                    quote_text = quote_elem.find('span', class_='text').get_text()
                    author = quote_elem.find('small', class_='author').get_text()
                    tags = [tag.get_text() for tag in quote_elem.find_all('a', class_='tag')]

                    quotes.append({
                        'quote': quote_text,
                        'author': author,
                        'tags': ', '.join(tags)
                    })

                print(f"Scraped page {page}: {len(quote_elements)} quotes")
                time.sleep(1)  # Be respectful to the server

            except requests.RequestException as e:
                print(f"Error scraping page {page}: {e}")
                continue

        return quotes

    def save_to_csv(self, quotes, filename='quotes.csv'):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['quote', 'author', 'tags'])
            writer.writeheader()
            writer.writerows(quotes)
        print(f"Saved {len(quotes)} quotes to {filename}")

# Usage
scraper = WebScraper()
all_quotes = scraper.scrape_quotes(3)
scraper.save_to_csv(all_quotes)
```

## 🚀 Next Steps & Learning Paths

### 🎯 **Choose Your Specialization Path**

#### **Web Development Track** 🌐
1. Complete Flask basics: `my_modules/flask_basic/`
2. Master async programming: `my_modules/comprehensive_examples/01_async_await_basics.py`
3. Learn REST API development: `my_modules/comprehensive_examples/02_rest_api_tutorial.py`
4. **Next**: Django, FastAPI, GraphQL, Frontend integration

#### **Data Science & Analytics Track** 📊
1. Master OOP concepts: `my_modules/comprehensive_examples/03_oop_comprehensive.py`
2. Learn database operations: `my_modules/comprehensive_examples/06_advanced_topics.py`
3. Explore AI modules: `my_modules/ai/`
4. **Next**: pandas, numpy, matplotlib, scikit-learn, Jupyter notebooks

#### **DevOps & Automation Track** ⚙️
1. Master imports and packaging: `my_modules/comprehensive_examples/04_library_imports_tutorial.py`
2. Learn Python packaging: `my_modules/comprehensive_examples/05_python_packaging_tutorial.py`
3. Advanced logging and configuration: `my_modules/comprehensive_examples/06_advanced_topics.py`
4. **Next**: Docker, CI/CD, AWS/Azure, Infrastructure as Code

#### **Software Engineering Track** 🏗️
1. Complete all comprehensive examples in order
2. Focus on OOP design patterns and SOLID principles
3. Master testing and debugging techniques
4. **Next**: System design, microservices, architecture patterns

### 1. **Explore the Learning Modules**
Navigate through the enhanced `my_modules/` directory:

**Foundation Modules:**
- `basic_concepts/` - Python fundamentals
- `advanced_concepts/` - Deeper language features
- `datastructures/` - Data structure implementations

**Application Modules:**
- `flask_basic/` - Web development with Flask
- `ai/` - Machine learning and AI basics
- `VidSnapAI/` - Computer vision project
- `external_modules/` - Third-party library integration

**🆕 Professional Modules:**
- `comprehensive_examples/` - **Production-ready examples and tutorials**
  - Advanced async/await and REST APIs
  - Complete OOP mastery
  - Professional import practices
  - Python packaging and distribution
  - Regex, databases, logging, and configuration

### 2. **Build Progressive Projects**

**Beginner Projects** (Weeks 1-4):
- **Personal Task Manager** - File I/O, basic OOP
- **Weather App** - API integration, error handling
- **Simple Calculator** - Functions, input validation
- **Text Analysis Tool** - String manipulation, regex

**Intermediate Projects** (Months 1-3):
- **Blog System** - Flask, databases, user authentication
- **Data Dashboard** - Visualization with matplotlib/plotly
- **API Service** - FastAPI, async programming, testing
- **Web Scraper** - Beautiful Soup, requests, data processing

**Advanced Projects** (Months 3-6):
- **Package on PyPI** - Full packaging workflow, documentation
- **Microservice Architecture** - Multiple services, Docker, APIs
- **ML Pipeline** - Data processing, model training, deployment
- **Real-time Application** - WebSockets, async programming, databases

### 3. **Professional Development**

**Code Quality & Testing:**
```bash
# Set up development tools
pip install black isort flake8 mypy pytest pytest-cov

# Run quality checks
black your_code.py          # Format code
isort your_code.py          # Sort imports
flake8 your_code.py         # Lint code
mypy your_code.py           # Type checking
pytest --cov=your_module    # Run tests with coverage
```

**Industry Best Practices:**
- Follow PEP 8 style guidelines
- Write comprehensive tests (aim for 80%+ coverage)
- Use type hints throughout your code
- Document your code and APIs
- Implement proper logging and error handling
- Practice code reviews and pair programming

### 4. **Community & Continuous Learning**

**Open Source Contribution:**
1. Start with documentation fixes
2. Fix beginner-friendly issues
3. Contribute new features
4. Maintain your own projects

**Learning Resources by Level:**

**📚 Books:**
- *Beginner*: "Automate the Boring Stuff with Python"
- *Intermediate*: "Python Tricks" by Dan Bader
- *Advanced*: "Effective Python" by Brett Slatkin
- *Architecture*: "Clean Code" by Robert Martin

**🌐 Online Platforms:**
- **Real Python** - Comprehensive tutorials and courses
- **Python.org** - Official documentation and tutorials
- **Talk Python** - Podcasts and courses
- **PyBites** - Coding challenges and exercises

**🏅 Practice Platforms:**
- **LeetCode** - Algorithm and data structure problems
- **HackerRank** - Python-specific challenges
- **Codewars** - Community-driven coding challenges
- **Python Challenge** - Python-specific puzzles

**🤝 Community:**
- **Python Discord** - Real-time help and discussions
- **r/Python** - Reddit community for news and discussions
- **Local Python meetups** - Network with local developers
- **PyCon conferences** - Annual Python conferences worldwide

### 5. **Specialization Areas**

**Web Development:**
- Django, FastAPI, Flask-RESTful
- Frontend: HTML/CSS/JavaScript, React/Vue
- Databases: PostgreSQL, MongoDB
- Deployment: Heroku, AWS, Docker

**Data Science & Machine Learning:**
- NumPy, Pandas, Matplotlib, Seaborn
- Scikit-learn, TensorFlow, PyTorch
- Jupyter Notebooks, Google Colab
- Big Data: Spark, Hadoop

**DevOps & Cloud:**
- Docker, Kubernetes
- AWS/Azure/GCP services
- CI/CD pipelines (GitHub Actions, Jenkins)
- Infrastructure as Code (Terraform, Ansible)

**Game Development:**
- Pygame for 2D games
- Panda3D for 3D games
- Arcade library for modern games

**Mobile Development:**
- Kivy for cross-platform apps
- BeeWare for native mobile apps

## 📝 Learning Tips

1. **Code Every Day**: Even 30 minutes daily builds strong habits
2. **Build Projects**: Apply concepts immediately in real projects
3. **Read Others' Code**: Study GitHub repositories and open-source projects
4. **Debug Actively**: Don't just fix errors, understand why they happened
5. **Teach Others**: Explaining concepts helps solidify your understanding

## 🤝 Contributing

Found a bug or want to improve examples? Contributions are welcome!
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

---

**Happy coding! 🐍✨**

For more details and advanced examples, explore the code in `my_modules/` directories.
