# Python Learning Map

A complete, incremental guide from zero to advanced Python. Each concept builds on the previous one — work through it top to bottom.

---

## Quick Start

```bash
git clone <repository-url>
cd pythonLearning
python my_modules/basic_concepts/basics.py
```

---

## Table of Contents

### Beginner
1. [Variables & Data Types](#1-variables--data-types)
2. [Input & Output](#2-input--output)
3. [Operators](#3-operators)
4. [Conditional Statements](#4-conditional-statements)
5. [Loops](#5-loops)
6. [Functions](#6-functions)
7. [Scopes](#7-scopes)
8. [Data Structures](#8-data-structures)
9. [Strings](#9-strings)

### Intermediate
10. [Comprehensions](#10-comprehensions)
11. [File Handling](#11-file-handling)
12. [Exception Handling](#12-exception-handling)
13. [Modules & Imports](#13-modules--imports)
14. [Regular Expressions](#14-regular-expressions)
15. [Classes & OOP](#15-classes--oop)
16. [Inheritance & Polymorphism](#16-inheritance--polymorphism)
17. [Magic / Dunder Methods](#17-magic--dunder-methods)
18. [Functional Programming](#18-functional-programming)
19. [Built-in Functions](#19-built-in-functions)

### Advanced
20. [Decorators](#20-decorators)
21. [Property, Classmethod & Staticmethod](#21-property-classmethod--staticmethod)
22. [Generators & Iterators](#22-generators--iterators)
23. [Context Managers](#23-context-managers)
24. [Type Hinting](#24-type-hinting)
25. [Enums & Data Classes](#25-enums--data-classes)
26. [Concurrency](#26-concurrency)
27. [Async / Await](#27-async--await)
28. [Metaclasses](#28-metaclasses)
29. [Testing](#29-testing)
30. [Packaging & Virtual Environments](#30-packaging--virtual-environments)

### Famous Libraries
31. [Standard Library](#31-standard-library)
32. [Data Science — NumPy, Pandas, Matplotlib](#32-data-science--numpy-pandas-matplotlib)
33. [Web Development — Flask, FastAPI](#33-web-development--flask-fastapi)
34. [HTTP & APIs — Requests, HTTPX](#34-http--apis--requests-httpx)
35. [Web Scraping — BeautifulSoup, Selenium](#35-web-scraping--beautifulsoup-selenium)
36. [Databases — SQLAlchemy, SQLite](#36-databases--sqlalchemy-sqlite)
37. [AI & Machine Learning](#37-ai--machine-learning)
38. [Automation & CLI](#38-automation--cli)
39. [Useful Utilities](#39-useful-utilities)

---

## Beginner

---

### 1. Variables & Data Types

A **variable** is a named container that holds a value in memory. You create one simply by writing a name and assigning a value to it with `=`. Python is **dynamically typed**, which means you do not declare the type — Python figures it out at runtime.

**Core data types:**

| Type | Example | Description |
|------|---------|-------------|
| `int` | `42` | Whole numbers, no limit on size |
| `float` | `3.14` | Decimal numbers (IEEE 754 double precision) |
| `str` | `"hello"` | Text, immutable sequence of characters |
| `bool` | `True` / `False` | Boolean; a subclass of `int` (True == 1) |
| `NoneType` | `None` | Represents the absence of a value |

> **Dynamic typing** means the same variable can hold different types at different times. Use `type()` to inspect the current type.

**Type conversion (casting):** Python does not implicitly convert types — you must do it explicitly using built-in functions like `int()`, `float()`, and `str()`.

```python
name = "Alice"          # str
age = 25                # int
height = 5.9            # float
is_student = True       # bool
result = None           # NoneType

# Check type
print(type(name))       # <class 'str'>

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Swap variables — Python evaluates the right side first
a, b = 10, 20
a, b = b, a             # a=20, b=10

# Explicit type conversion
print(int("42"))        # 42
print(float("3.14"))    # 3.14
print(str(100))         # "100"
```

**File:** `my_modules/basic_concepts/basics.py`

---

### 2. Input & Output

Every program needs to communicate with the user. Python provides two fundamental tools: `print()` to display output, and `input()` to read text from the keyboard.

**`print()`** accepts any number of arguments separated by commas, and by default joins them with a space and ends with a newline. Both can be customized with the `sep` and `end` parameters.

**`input()`** always returns a **string**, no matter what the user types. If you need a number, you must convert it explicitly.

**f-strings** (formatted string literals, introduced in Python 3.6) are the recommended way to embed values inside strings. They are readable, concise, and support format specifiers for controlling decimal places, padding, percentages, and more.

```python
# Basic print
print("Hello, World!")
print("Name:", "Alice", "Age:", 25)          # Name: Alice Age: 25
print("joined", "with", "dashes", sep="-")  # joined-with-dashes
print("no newline", end=" "); print("same line")

# f-strings — embed expressions directly in strings
name, age = "Alice", 30
print(f"Hello, {name}! You are {age} years old.")
print(f"Next year: {age + 1}")
print(f"Pi: {3.14159:.2f}")        # Pi: 3.14   (.2f = 2 decimal places)
print(f"Score: {0.845:.1%}")       # Score: 84.5%
print(f"{'left':<10}|{'right':>10}")   # left padding / right padding

# User input — always returns a string
name = input("Enter your name: ")
age  = int(input("Enter your age: "))   # convert to int
print(f"Hello, {name}! You are {age} years old.")
```

---

### 3. Operators

Operators are symbols that perform operations on values (called **operands**). Python groups them into several categories:

- **Arithmetic** — basic math (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- **Comparison** — compare values, always return `True` or `False` (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- **Logical** — combine boolean values (`and`, `or`, `not`)
- **Assignment shortcuts** — combine an operation with assignment (`+=`, `-=`, etc.)
- **Identity** — check if two variables point to the *same object* in memory (`is`, `is not`)
- **Membership** — check if a value exists in a collection (`in`, `not in`)
- **Bitwise** — operate on individual bits of integers (`&`, `|`, `^`, `~`, `<<`, `>>`)
- **Walrus** (`:=`) — assign a value *and* return it in a single expression (Python 3.8+)

> `//` is **floor division** — it divides and rounds *down* to the nearest integer.
> `%` is **modulo** — it gives the *remainder* after division.
> `**` is **exponentiation** — `2 ** 10` means 2 to the power of 10.

```python
# Arithmetic
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...  (always returns float)
print(10 // 3)  # 3         (floor division, returns int)
print(10 % 3)   # 1         (remainder)
print(2 ** 10)  # 1024      (power)

# Comparison (always returns True or False)
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True

# Logical
print(True and False)   # False — both must be True
print(True or False)    # True  — at least one must be True
print(not True)         # False — inverts the value

# Assignment shortcuts
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x //= 4  # x = 6

# Identity vs equality
# == checks if values are equal; is checks if they are the same object
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == c)   # True  (same values)
print(a is c)   # False (different objects)
print(a is b)   # True  (b is just another name for a)

# Membership
print(2 in a)       # True
print(5 not in a)   # True

# Bitwise — operate on binary representations of integers
print(0b1010 & 0b1100)  # 8  (AND  — bits that are 1 in both)
print(0b1010 | 0b1100)  # 14 (OR   — bits that are 1 in either)
print(0b1010 ^ 0b1100)  # 6  (XOR  — bits that differ)
print(~0b1010)           # -11 (NOT — flip all bits)
print(1 << 3)            # 8  (left shift  = multiply by 2^3)
print(16 >> 2)           # 4  (right shift = divide by 2^2)

# Walrus operator := — assign and use in the same expression
# Avoids calling len() twice or storing in a separate line
numbers = [1, -3, 5, -2, 8]
if (n := len(numbers)) > 3:
    print(f"List has {n} items")   # List has 5 items

# Very useful in while loops to read until empty input
# while chunk := input("Enter text (blank to stop): "):
#     print(f"Got: {chunk}")
```

---

### 4. Conditional Statements

Conditional statements let your program make decisions — executing different blocks of code depending on whether a condition is `True` or `False`.

**How it works:**
- `if` evaluates a condition. If `True`, its block runs.
- `elif` (short for "else if") is checked only if all previous conditions were `False`.
- `else` runs when none of the above conditions were `True`.
- You can nest conditionals inside each other, but keep it shallow for readability.

**Truthy and falsy values:** Python treats certain values as `False` even if they're not literally `False`: `0`, `0.0`, `""`, `[]`, `{}`, `None`. Everything else is considered `True`.

**Ternary expression:** A compact one-liner for simple if/else: `value_if_true if condition else value_if_false`.

**`match / case`** (Python 3.10+): A cleaner alternative to long `elif` chains when comparing a value against multiple patterns.

```python
age = 20

# Standard if / elif / else
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary — one-liner for simple conditions
status = "adult" if age >= 18 else "minor"
print(status)   # adult

# Truthy / falsy
name = ""
if name:
    print("Has a name")
else:
    print("Name is empty")   # this runs because "" is falsy

# match / case (Python 3.10+) — like switch/case in other languages
command = "quit"
match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":      # match either value with |
        print("Stopping...")
    case _:                    # default / catch-all
        print("Unknown command")
```

---

### 5. Loops

Loops allow you to repeat a block of code multiple times without writing it out manually. Python has two types:

- **`for` loop** — iterates over a sequence (list, range, string, dict, etc.). Use this when you know *what* to iterate over.
- **`while` loop** — keeps running as long as a condition is `True`. Use this when you don't know in advance how many iterations you need.

**Key tools:**
- `range(start, stop, step)` — generates a sequence of numbers. `stop` is exclusive.
- `enumerate()` — gives you both the index and the value while iterating.
- `zip()` — pairs up two or more sequences to iterate together.
- `break` — immediately exits the loop.
- `continue` — skips the rest of the current iteration and goes to the next.
- `else` on a loop — runs only if the loop finished *without* hitting a `break`.

```python
# for loop — iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# range() — generates numbers
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # start=2, stop=10, step=2 → 2,4,6,8
    print(i)

# enumerate — get index alongside value
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 1: apple, 2: banana, 3: cherry

# zip — iterate two sequences together in lockstep
names = ["Alice", "Bob", "Charlie"]
ages  = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# while loop — runs until the condition becomes False
count = 0
while count < 5:
    print(count)
    count += 1

# break and continue
for i in range(10):
    if i == 3:
        continue   # skip 3, jump to next iteration
    if i == 7:
        break      # stop the loop entirely
    print(i)       # prints 0,1,2,4,5,6

# Loop else — only runs if loop completed without a break
for i in range(5):
    print(i)
else:
    print("Loop finished normally")
```

**File:** `my_modules/basic_concepts/loops.py`

---

### 6. Functions

A **function** is a reusable block of code that performs a specific task. Instead of copying the same code in multiple places, you define it once and call it whenever needed. This keeps your code **DRY** (Don't Repeat Yourself).

**Key concepts:**
- **Parameters** are the variables listed in the function definition.
- **Arguments** are the actual values passed when calling the function.
- **Default parameters** provide a fallback value if no argument is given.
- **`*args`** collects extra positional arguments into a tuple.
- **`**kwargs`** collects extra keyword arguments into a dictionary.
- A function returns `None` by default if no `return` statement is used.

**Closures:** A function defined inside another function can *remember* variables from the outer function even after the outer function has finished. This is called a closure and is the foundation of decorators.

**Recursion:** A function that calls itself. Every recursive function needs a **base case** to stop — otherwise it recurses forever and crashes.

```python
# Basic function
def greet(name, greeting="Hello"):   # greeting has a default value
    return f"{greeting}, {name}!"

print(greet("Bob"))            # Hello, Bob!
print(greet("Bob", "Hi"))      # Hi, Bob!

# Keyword arguments — pass by name, order doesn't matter
def describe(name, age, city):
    print(f"{name}, {age}, {city}")

describe(age=30, city="NYC", name="Alice")

# *args — collect any number of positional arguments
def total(*numbers):
    return sum(numbers)   # numbers is a tuple inside the function

print(total(1, 2, 3, 4))   # 10

# **kwargs — collect any number of keyword arguments
def profile(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

profile(name="Alice", age=30, city="NYC")

# Return multiple values (Python returns them as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9])   # unpacking

# Closures — inner function remembers outer function's variables
def make_counter(start=0):
    count = start           # this variable is "enclosed"
    def counter():
        nonlocal count      # tell Python we mean the outer 'count'
        count += 1
        return count
    return counter          # return the function itself, not its result

c = make_counter()
print(c())   # 1
print(c())   # 2
print(c())   # 3

# Recursion — a function that calls itself
# Base case (n <= 1) prevents infinite recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))   # 120  (5 × 4 × 3 × 2 × 1)
```

**File:** `my_modules/basic_concepts/functions.py`

---

### 7. Scopes

**Scope** determines where in your code a variable is visible and accessible. Python uses the **LEGB rule** to look up names in this order:

1. **L**ocal — variables defined inside the current function
2. **E**nclosing — variables in any outer (enclosing) functions (relevant for nested functions)
3. **G**lobal — variables defined at the top level of the module
4. **B**uilt-in — Python's own names like `len`, `print`, `range`

Python stops searching as soon as it finds a match. If no match is found, you get a `NameError`.

**`global` keyword** — lets you *modify* a global variable from inside a function. Without it, assigning to a name inside a function creates a *new local* variable, leaving the global untouched.

**`nonlocal` keyword** — lets you modify a variable in an *enclosing* (but not global) scope. Used in nested functions and closures.

```python
x = "global"

def outer():
    x = "enclosing"       # shadows the global x inside outer()

    def inner():
        x = "local"       # shadows the enclosing x inside inner()
        print(x)          # local

    inner()
    print(x)              # enclosing

outer()
print(x)                  # global — the original was never touched

# global — modify a module-level variable from inside a function
counter = 0

def increment():
    global counter         # without this, Python would create a new local
    counter += 1

increment()
increment()
print(counter)   # 2

# nonlocal — modify an enclosing (but not global) variable
def make_adder():
    total = 0
    def add(x):
        nonlocal total     # refers to the 'total' in make_adder's scope
        total += x
        return total
    return add

adder = make_adder()
print(adder(5))    # 5
print(adder(3))    # 8   (total persists between calls)
```

**File:** `my_modules/basic_concepts/pythonscopes.py`

---

### 8. Data Structures

Python has four built-in collection types, each suited to different situations:

| Type | Ordered | Mutable | Duplicates | Syntax |
|------|---------|---------|-----------|--------|
| `list` | Yes | Yes | Yes | `[1, 2, 3]` |
| `tuple` | Yes | No | Yes | `(1, 2, 3)` |
| `set` | No | Yes | No | `{1, 2, 3}` |
| `dict` | Yes* | Yes | Keys: No | `{"a": 1}` |

*Dicts preserve insertion order since Python 3.7.

**When to use which:**
- **List** — ordered collection that you'll modify (add, remove, sort).
- **Tuple** — fixed collection (coordinates, RGB, database records). Slightly faster than lists.
- **Set** — when you need uniqueness or fast membership testing.
- **Dict** — when you need to look up values by a meaningful key.

```python
# ── Lists ─────────────────────────────────────────────────────
fruits = ["apple", "banana", "cherry"]

fruits.append("date")          # add to end
fruits.insert(1, "avocado")    # insert at specific index
fruits.remove("banana")        # remove first occurrence by value
popped = fruits.pop()          # remove & return the last item
fruits.sort()                  # sort in place (ascending)
fruits.reverse()               # reverse in place

print(fruits[0])               # first item (index 0)
print(fruits[-1])              # last item (negative index)
print(fruits[1:3])             # slice — items at index 1 and 2
print(len(fruits))
print("apple" in fruits)       # True — membership test

# ── Tuples ────────────────────────────────────────────────────
# Immutable — once created, you cannot change a tuple
point = (3, 4)
x, y = point           # unpacking into separate variables

rgb = (255, 128, 0)    # good for fixed, meaningful groupings

# ── Sets ──────────────────────────────────────────────────────
# Automatically remove duplicates; fast O(1) membership lookup
nums = {1, 2, 3, 3, 2}
print(nums)            # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)           # {2, 3}       intersection (in both)
print(a | b)           # {1, 2, 3, 4} union (in either)
print(a - b)           # {1}          difference (in a but not b)
print(a ^ b)           # {1, 4}       symmetric difference

# ── Dictionaries ──────────────────────────────────────────────
# Key-value store; keys must be unique and immutable
person = {"name": "Alice", "age": 30}

print(person["name"])
print(person.get("email", "N/A"))  # safe access — returns default if missing

person["email"] = "alice@example.com"  # add or update
del person["age"]                       # remove a key

for key, value in person.items():
    print(f"{key}: {value}")

# Merge two dicts (Python 3.9+)
a = {"x": 1}
b = {"y": 2}
merged = a | b          # {"x": 1, "y": 2}
```

**Files:** `my_modules/basic_concepts/datastructures.py`, `Sets.py`, `15_dictionaries.py`

---

### 9. Strings

A **string** is an immutable, ordered sequence of characters. "Immutable" means you cannot change a string in place — every method that seems to modify a string actually returns a *new* string.

Strings support **indexing** (accessing one character) and **slicing** (accessing a range of characters) using the `[start:stop:step]` syntax. Negative indices count from the end.

Python strings come with a rich set of built-in methods for searching, transforming, splitting, joining, and testing content.

**String formatting options:**
- **f-strings** (Python 3.6+) — `f"Hello, {name}"` — recommended, most readable
- **`.format()`** — `"Hello, {}".format(name)` — older but still widely used
- **`%` formatting** — `"Hello, %s" % name` — legacy style, avoid in new code

```python
text = "Hello, World!"

# Common transformation methods
print(text.upper())                  # HELLO, WORLD!
print(text.lower())                  # hello, world!
print("  hello  ".strip())           # "hello"  (remove leading/trailing whitespace)
print(text.replace("World","Python"))# Hello, Python!
print(text.split(", "))             # ['Hello', 'World!']
print(", ".join(["a", "b", "c"]))  # a, b, c

# Indexing and slicing
#  H  e  l  l  o  ,     W  o  r  l  d  !
#  0  1  2  3  4  5  6  7  8  9 10 11 12
# -13 ...                              -1
print(text[0])      # H     (first character)
print(text[-1])     # !     (last character)
print(text[0:5])    # Hello (index 0 to 4)
print(text[-6:])    # World! (last 6 characters)
print(text[::-1])   # !dlroW ,olleH  (step=-1 reverses the string)

# Checking / searching
print(text.startswith("Hello"))  # True
print(text.endswith("!"))        # True
print("world" in text.lower())   # True — case-insensitive check
print("42".isdigit())            # True
print(text.find("World"))        # 7 — index of first occurrence, -1 if not found
print(text.count("l"))           # 3

# Multi-line strings — use triple quotes
poem = """
Roses are red,
Violets are blue.
"""

# Raw strings — backslashes are treated as literal characters
# Useful for Windows file paths and regular expressions
path = r"C:\Users\Alice\Documents"

# Format specifiers in f-strings
pi = 3.14159
score = 0.845
print(f"Pi: {pi:.2f}")            # Pi: 3.14   (2 decimal places)
print(f"Score: {score:.1%}")      # Score: 84.5%
print(f"{'left':<10}|{'right':>10}")  # padding / alignment
```

**File:** `my_modules/basic_concepts/stringsInPython.py`

---

## Intermediate

---

### 10. Comprehensions

Comprehensions are a concise, readable Python way to create new collections by transforming or filtering existing ones — all in a single line.

**Types:**
- **List comprehension** `[expr for item in iterable if condition]` → returns a `list`
- **Dict comprehension** `{key: val for item in iterable}` → returns a `dict`
- **Set comprehension** `{expr for item in iterable}` → returns a `set`
- **Generator expression** `(expr for item in iterable)` → returns a **lazy** iterator (no list built in memory)

**When to use:** Prefer comprehensions over manual `for` loops that just build a list — they are more Pythonic and slightly faster. However, avoid nesting more than two levels deep; at that point a regular loop is clearer.

**Generator expressions** are the memory-efficient alternative. Instead of building the entire list in memory, they compute values one at a time on demand. Use them when you only need to iterate once (e.g., passing to `sum()`, `max()`, or a loop).

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension — transform every item
squares = [x**2 for x in numbers]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With a filter condition
evens = [x for x in numbers if x % 2 == 0]
# [2, 4, 6, 8, 10]

# Transformation + filter
even_squares = [x**2 for x in numbers if x % 2 == 0]
# [4, 16, 36, 64, 100]

# Nested — flattening a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dict comprehension
square_map = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension — automatically removes duplicates
words = ["cat", "dog", "elephant", "ant", "cat"]
unique_lengths = {len(word) for word in words}
# {3, 8}

# Generator expression — identical syntax to list, but with ()
# Does NOT build a list; computes each value when asked
total = sum(x**2 for x in range(1_000_000))   # memory-efficient
```

---

### 11. File Handling

Programs often need to persist data between runs — reading configuration, saving results, loading datasets. Python's built-in `open()` function gives access to the filesystem.

**File modes:**
| Mode | Meaning |
|------|---------|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates file or **overwrites** existing. |
| `"a"` | Append. Creates or adds to end. |
| `"x"` | Exclusive create — fails if file exists. |
| `"b"` | Binary mode (combine: `"rb"`, `"wb"`) |

**Always use `with`** (the context manager syntax). It guarantees the file is closed properly even if an error occurs, preventing data loss and resource leaks.

**JSON** is the standard format for structured data exchange. The `json` module converts between Python objects and JSON strings. **CSV** is the standard for tabular data.

```python
# Write — creates or overwrites the file
with open("data.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Read — load the entire file as a string
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line — memory efficient for large files
with open("data.txt") as f:
    for line in f:
        print(line.strip())   # strip() removes the trailing newline

# Append — add to the end without overwriting
with open("data.txt", "a") as f:
    f.write("Line 3\n")

# JSON — structured data (dicts, lists, strings, numbers)
import json

data = {"name": "Alice", "scores": [95, 87, 92]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)      # write Python object as JSON

with open("data.json") as f:
    loaded = json.load(f)             # read JSON back as Python object
    print(loaded["name"])             # Alice

# CSV — tabular data (spreadsheet-style)
import csv

rows = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
with open("people.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)

with open("people.csv") as f:
    for row in csv.reader(f):
        print(row)
```

**Files:** `my_modules/files_handling/`

---

### 12. Exception Handling

When something goes wrong at runtime — dividing by zero, opening a missing file, converting invalid input — Python raises an **exception**. If unhandled, the program crashes with a traceback. Exception handling lets you catch these errors and respond gracefully.

**Structure:**
- `try` — the code that might raise an exception
- `except` — what to do if a specific exception occurs
- `else` — runs only if **no** exception was raised in `try`
- `finally` — **always** runs, whether an exception occurred or not (ideal for cleanup)

**Hierarchy:** All exceptions inherit from `BaseException`. Most you'll deal with inherit from `Exception`. You can catch a parent class to catch all its children (e.g., catching `Exception` catches almost everything).

**Custom exceptions** let you create meaningful error types specific to your application. Always inherit from `Exception` (or a more specific subclass).

```python
# Basic try / except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catching multiple exception types
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number")
except KeyboardInterrupt:
    print("Cancelled by user")

# else and finally
try:
    data = int("42")
except ValueError as e:
    print(f"Error: {e}")
else:
    # Only runs if try succeeded — good for code that depends on try succeeding
    print(f"Parsed successfully: {data}")
finally:
    # Always runs — use for cleanup (close files, release connections)
    print("This always executes")

# Raise your own exception
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError(f"Insufficient funds: balance={balance}, amount={amount}")
    return balance - amount

# Define custom exception types for your application
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount} from balance of {balance}")
        self.balance = balance
        self.amount = amount

try:
    raise InsufficientFundsError(100, 200)
except InsufficientFundsError as e:
    print(e)
    print(f"Tried to take: {e.amount}")
```

**Files:** `my_modules/advanced_concepts/07_errors.py`, `08_raise_errors.py`, `09_else_finally.py`

---

### 13. Modules & Imports

A **module** is simply a Python file. When a project grows beyond one file, you split code into modules to keep it organized and reusable. A **package** is a folder containing an `__init__.py` file — it groups related modules together.

**Why modules matter:**
- Avoid name conflicts between different parts of your project
- Reuse code across multiple files without copying
- Python ships with a huge **standard library** of ready-made modules

**`if __name__ == "__main__"`** — this guard makes a file behave differently when run directly versus when imported. Code inside it only runs when you execute the file directly, not when another file imports it.

```python
# Import the entire module — access things via module.name
import math
print(math.sqrt(16))     # 4.0
print(math.pi)           # 3.14159...

# Import specific names — no need for the module prefix
from math import sqrt, pi
print(sqrt(25))          # 5.0

# Import with an alias — useful for long names or naming conventions
import numpy as np
import pandas as pd

# Your own module
# ── utils.py ──────────────────
# def add(a, b):
#     return a + b

# ── main.py ───────────────────
# from utils import add
# print(add(2, 3))   # 5

# Package import — folders with __init__.py become importable packages
from my_modules.basic_concepts.functions import some_function

# The __name__ guard
# When run directly: __name__ == "__main__"
# When imported:     __name__ == "module_name"
if __name__ == "__main__":
    print("Running directly, not imported")
```

**Files:** `my_modules/basic_concepts/modules_in_python.py`, `mymodule.py`

---

### 14. Regular Expressions

A **regular expression** (regex) is a pattern that describes a set of strings. They are used to search, validate, and manipulate text. Python's `re` module provides full regex support.

**Why use regex?** Plain string methods (`find`, `replace`, `split`) work well for simple cases, but regex handles complex patterns — like "find all email addresses" or "validate a phone number format" — in a single expression.

**Key functions:**
| Function | Description |
|----------|-------------|
| `re.search(pattern, text)` | Find first match anywhere in text |
| `re.match(pattern, text)` | Match only at the start of text |
| `re.findall(pattern, text)` | Return all matches as a list |
| `re.sub(pattern, replace, text)` | Replace all matches |
| `re.compile(pattern)` | Pre-compile for reuse (faster in loops) |

**Common pattern symbols:**
- `.` — any character except newline
- `\d` — digit (0–9), `\w` — word char (letters/digits/_), `\s` — whitespace
- `+` — one or more, `*` — zero or more, `?` — zero or one
- `^` — start of string, `$` — end of string
- `[]` — character class: `[a-z]`, `[0-9]`
- `()` — capture group

```python
import re

text = "Contact: info@example.com or support@python.org at +1-800-555-0100"

# search — finds the first match, returns a match object (or None)
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(match.group())   # 800-555-0100

# findall — returns all non-overlapping matches as a list of strings
emails = re.findall(r"[\w.]+@[\w.]+", text)
print(emails)   # ['info@example.com', 'support@python.org']

# sub — replace all matches with a replacement string
cleaned = re.sub(r"\s+", " ", "too   many    spaces")
print(cleaned)  # too many spaces

# Capture groups — parentheses extract specific parts of a match
pattern = r"(\w+)@(\w+)\.(\w+)"
for m in re.finditer(pattern, text):
    print(m.group(0))   # full match: info@example.com
    print(m.group(1))   # group 1:   info (username)
    print(m.group(2))   # group 2:   example (domain)

# Compile for reuse — more efficient when using the same pattern many times
phone_re = re.compile(r"\+?\d[\d\-]{7,}")
phones = phone_re.findall(text)

# Common patterns for reference
# r"\d+"         one or more digits
# r"\w+"         one or more word characters
# r"[a-zA-Z]+"   one or more letters
# r"^\d{4}$"     exactly 4 digits, full string
# r"https?://"   http or https
```

**File:** `my_modules/external_modules/03_regular_expressions.py`

---

### 15. Classes & OOP

**Object-Oriented Programming (OOP)** is a programming style that organises code around **objects** — bundles of related data (attributes) and behaviour (methods).

A **class** is a blueprint. An **object** (or **instance**) is a concrete thing created from that blueprint.

**Four pillars of OOP:**
1. **Encapsulation** — bundling data and methods together; hiding internal details
2. **Inheritance** — a new class reuses and extends an existing class
3. **Polymorphism** — different classes respond to the same interface in their own way
4. **Abstraction** — exposing only what's necessary, hiding complexity

**Key terms:**
- `__init__` — the **constructor**, called automatically when an object is created
- `self` — refers to the current instance (like `this` in other languages)
- **Instance attributes** — unique to each object (`self.name`)
- **Class attributes** — shared by all instances (`species = "..."`)
- `__str__` — what `print(obj)` shows; `__repr__` — what the debugger/REPL shows

```python
class Dog:
    # Class attribute — shared by every Dog instance
    species = "Canis lupus familiaris"

    # Constructor — called when you write Dog("Rex", 5)
    def __init__(self, name, age):
        self.name = name    # instance attribute — unique per object
        self.age = age

    # Instance method — always takes self as first argument
    def bark(self):
        return f"{self.name} says: Woof!"

    # Human-readable representation (used by print())
    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

    # Developer representation (used in REPL and debugger)
    def __repr__(self):
        return f"Dog({self.name!r}, {self.age!r})"

# Creating instances
rex   = Dog("Rex", 5)
bella = Dog("Bella", 3)

print(rex.bark())       # Rex says: Woof!
print(rex)              # Dog(name=Rex, age=5)
print(Dog.species)      # access class attribute via class name

# A class with encapsulation using @property (see section 21)
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance   # _ prefix = "internal, don't touch directly"

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount(1000)
account.deposit(500)
print(account.balance)   # 1500
```

**Files:** `my_modules/oops_concepts/01_classes.py`, `02_constructors.py`, `03_instances_class_attributes.py`

---

### 16. Inheritance & Polymorphism

**Inheritance** lets a new class (**child/subclass**) acquire the attributes and methods of an existing class (**parent/superclass**). This enables code reuse and creates natural "is-a" relationships (a `Dog` *is an* `Animal`).

**Polymorphism** means "many forms" — different classes can be used through the same interface. You can call `animal.speak()` on a list of different animal types and each responds in its own way, without the caller needing to know the specific type.

**Abstract base classes (ABC)** enforce a contract: any subclass *must* implement the abstract methods. Trying to instantiate an abstract class raises a `TypeError`. This prevents accidentally using an incomplete class.

**`super()`** calls the parent class's version of a method, which is essential when overriding to avoid duplicating the parent's logic.

```python
from abc import ABC, abstractmethod

# Abstract base class — defines an interface, cannot be instantiated directly
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass   # subclasses MUST implement this method

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

# Concrete subclasses — each implements speak() differently
class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow!"

# Polymorphism in action — same call, different results
animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())   # each responds in its own way

# Type inspection
print(isinstance(animals[0], Animal))   # True — Dog IS-A Animal
print(isinstance(animals[0], Dog))      # True
print(issubclass(Dog, Animal))          # True

# Multiple inheritance — a class can inherit from more than one parent
class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class FlyingDog(Dog, Flyable):
    pass   # inherits from both Dog and Flyable

superdog = FlyingDog("Krypto")
print(superdog.speak())   # Krypto: Woof!
print(superdog.fly())     # Krypto is flying!

# super() — call the parent's method when overriding
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)   # call Dog's __init__
        self.owner = owner

    def speak(self):
        base = super().speak()   # call Dog's speak()
        return f"{base} (Guide dog for {self.owner})"
```

**File:** `my_modules/oops_concepts/04_inheritance.py`

---

### 17. Magic / Dunder Methods

**Magic methods** (also called **dunder methods** — short for "double underscore") are special methods that Python calls automatically in response to built-in operations. By implementing them in your class, you make your objects behave like built-in types.

For example: `+` calls `__add__`, `len()` calls `__len__`, `print()` calls `__str__`, `for x in obj` calls `__iter__`, and `with obj` calls `__enter__` / `__exit__`.

This is how Python achieves operator overloading cleanly — you define the behaviour, Python wires it up to the familiar syntax.

**Common dunder methods:**

| Method | Triggered by |
|--------|-------------|
| `__init__` | `MyClass()` |
| `__str__` | `print(obj)`, `str(obj)` |
| `__repr__` | REPL, debugger, `repr(obj)` |
| `__len__` | `len(obj)` |
| `__add__` | `obj + other` |
| `__eq__` | `obj == other` |
| `__lt__` | `obj < other` |
| `__getitem__` | `obj[key]` |
| `__iter__` | `for x in obj` |
| `__bool__` | `if obj:` |
| `__enter__` / `__exit__` | `with obj:` |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Representation
    def __str__(self):           # for humans — print()
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):          # for developers — REPL, debugger
        return f"Vector({self.x!r}, {self.y!r})"

    # Arithmetic operators
    def __add__(self, other):    # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):    # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):   # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    # Comparison
    def __eq__(self, other):     # v1 == v2
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):     # v1 < v2
        return abs(self) < abs(other)

    # Numeric / container behaviour
    def __abs__(self):           # abs(v) — magnitude
        return (self.x**2 + self.y**2) ** 0.5

    def __len__(self):           # len(v)
        return 2

    def __bool__(self):          # if v:
        return self.x != 0 or self.y != 0

    def __iter__(self):          # for coord in v:
        yield self.x
        yield self.y

    def __getitem__(self, index): # v[0], v[1]
        return (self.x, self.y)[index]

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)     # Vector(4, 6)
print(abs(v1))     # 2.23...
print(list(v1))    # [1, 2]
print(v1[0])       # 1
print(bool(v1))    # True
```

**Files:** `my_modules/advanced_concepts/06_dunder_magic_methods.py`, `my_modules/oops_concepts/05_operator_overloading.py`

---

### 18. Functional Programming

**Functional programming** is a style where you treat functions as first-class values — you can store them in variables, pass them as arguments, and return them from other functions. Python supports this alongside OOP.

**Key ideas:**
- **Lambda** — an anonymous function defined inline, limited to a single expression. Good for short, one-off functions.
- **`map(func, iterable)`** — applies a function to every item. Returns an iterator.
- **`filter(func, iterable)`** — keeps only items where the function returns `True`. Returns an iterator.
- **`reduce(func, iterable)`** — cumulatively combines all items into a single value.
- **First-class functions** — functions are objects; you can pass them around like any other value.

> Prefer list comprehensions over `map`/`filter` for readability in most cases. Use `map`/`filter` when you already have a named function to apply.

```python
from functools import reduce

# Lambda — anonymous function: lambda args: expression
square  = lambda x: x ** 2
add     = lambda x, y: x + y

print(square(5))    # 25
print(add(3, 4))    # 7

numbers = [1, 2, 3, 4, 5]

# map — transform every item
squares = list(map(lambda x: x**2, numbers))
print(squares)      # [1, 4, 9, 16, 25]

# filter — keep items that pass a test
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)        # [2, 4]

# reduce — combine all items into one value (left to right)
total   = reduce(lambda acc, x: acc + x, numbers)   # 15
product = reduce(lambda acc, x: acc * x, numbers)   # 120

# Lambdas shine as sort keys — tell Python *how* to compare items
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
people.sort(key=lambda p: p[1])   # sort by age (index 1)

words = ["banana", "apple", "cherry"]
words.sort(key=len)               # sort by string length

# First-class functions — pass a function as an argument
def apply(func, value):
    return func(value)

print(apply(square, 5))    # 25
print(apply(str, 42))      # "42"
print(apply(abs, -7))      # 7
```

**Files:** `my_modules/advanced_concepts/11_map.py`, `12_filter.py`, `13_reduce.py`

---

### 19. Built-in Functions

Python ships with dozens of powerful built-in functions — no import needed. These cover the most common operations on collections, types, and objects.

**Most important built-ins to know:**

| Function | Purpose |
|----------|---------|
| `len(x)` | Number of items |
| `min(x)` / `max(x)` | Smallest / largest |
| `sum(x)` | Total of all items |
| `sorted(x)` | Return sorted copy |
| `reversed(x)` | Reversed iterator |
| `enumerate(x)` | Index + value pairs |
| `zip(a, b)` | Pair up sequences |
| `any(x)` / `all(x)` | Boolean tests |
| `map(f, x)` / `filter(f, x)` | Transform / filter |
| `abs()`, `round()`, `pow()` | Math |
| `isinstance()`, `type()` | Type checks |
| `getattr()`, `setattr()`, `hasattr()` | Dynamic attribute access |

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))        # 8
print(min(numbers))        # 1
print(max(numbers))        # 9
print(sum(numbers))        # 31
print(sorted(numbers))     # [1, 1, 2, 3, 4, 5, 6, 9]  (new list)
print(list(reversed(numbers)))

# zip — pairs items from two sequences; stops at the shorter one
names = ["Alice", "Bob", "Charlie"]
ages  = [30, 25, 35]
pairs = list(zip(names, ages))   # [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

# enumerate — adds an index to any iterable
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")    # 1. Alice, 2. Bob, 3. Charlie

# any — True if at least one item is truthy
# all — True if every item is truthy
print(any([False, True, False]))   # True
print(all([True, True, True]))     # True
print(all([True, False, True]))    # False

# Type conversion
int("42"), float("3.14"), str(100)
list((1, 2, 3)), tuple([1, 2]), set([1, 2, 2, 3])

# Math built-ins
print(abs(-5))              # 5
print(round(3.14159, 2))    # 3.14
print(divmod(10, 3))        # (3, 1) — quotient and remainder together
print(pow(2, 10, 1000))     # 24 — 2^10 mod 1000 (efficient for large numbers)

# Reflection — inspect objects at runtime
class Foo:
    x = 1
print(hasattr(Foo, "x"))    # True  — does the attribute exist?
print(getattr(Foo, "x"))    # 1     — get it
setattr(Foo, "y", 2)        # set an attribute dynamically
print(vars(Foo))            # dict of all attributes
```

---

## Advanced

---

### 20. Decorators

A **decorator** is a function that wraps another function to add behaviour *before* or *after* it runs — without modifying the original function's source code. Decorators are applied using the `@` syntax.

**How it works:** A decorator is simply a function that:
1. Takes a function as an argument
2. Defines an inner `wrapper` function that adds extra behaviour
3. Returns the `wrapper`

`@functools.wraps(func)` is essential — it copies the original function's name, docstring, and metadata onto the wrapper so debugging tools still show the right information.

**Real-world uses:** Logging, timing, access control, caching, retry logic, input validation — any cross-cutting concern you want to apply cleanly across many functions.

```python
import functools
import time

# A decorator is just a function that takes a function and returns a function
def log(func):
    @functools.wraps(func)   # preserves original function's name and docstring
    def wrapper(*args, **kwargs):
        print(f"→ Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} returned {result}")
        return result
    return wrapper

@log                # equivalent to: add = log(add)
def add(a, b):
    return a + b

add(2, 3)
# → Calling add with (2, 3), {}
# ← add returned 5

# Decorator with arguments — add a layer of wrapping
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # prints 3 times

# Practical: timing decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

# Built-in: memoization (cache results to avoid recomputing)
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    # Without caching this would be extremely slow for large n
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))   # instant, computed only once per input
```

**Files:** `my_modules/advanced_concepts/01_decorators.py`, `02_decorators_with_arguments.py`

---

### 21. Property, Classmethod & Staticmethod

These three decorators control *how* methods work relative to the class and its instances.

**`@property`** turns a method into a read-only attribute. It allows you to add validation or computation while the caller accesses it as a simple attribute (no parentheses). Combine with `@<name>.setter` to validate on write.

**`@classmethod`** receives the **class itself** (`cls`) as the first argument, not an instance. The primary use case is **alternative constructors** — providing multiple ways to create an object.

**`@staticmethod`** has no implicit first argument at all — it doesn't know about the class or any instance. It's a regular function that lives inside the class for logical grouping.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   # _prefix = internal, use the property instead

    # @property — access like an attribute: t.celsius (not t.celsius())
    @property
    def celsius(self):
        return self._celsius

    # @<name>.setter — runs when you write: t.celsius = 30
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    # Computed property — no stored value, calculated on the fly
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # @classmethod — receives cls (the class), not self (the instance)
    # Classic use: alternative constructor (create from different input)
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)   # calls Circle.__init__ via cls()

    # @staticmethod — no access to class or instance
    # Use for utility functions that logically belong with the class
    @staticmethod
    def is_valid_radius(r):
        return r > 0

t = Temperature(25)
print(t.celsius)        # 25   (reads via property getter)
print(t.fahrenheit)     # 77.0 (computed on access)
t.celsius = 30          # triggers the setter with validation

c = Circle.from_diameter(10)
print(c.radius)                    # 5.0
print(Circle.is_valid_radius(-1))  # False
```

**Files:** `my_modules/advanced_concepts/03_getter_and_setter.py`, `04_property_decorator.py`, `05_instance_static_class_methods.py`

---

### 22. Generators & Iterators

**Iterators** are objects that produce values one at a time, on demand. Any object with `__iter__` and `__next__` methods is an iterator.

**Generators** are a simple way to create iterators using the `yield` keyword. When a generator function hits `yield`, it pauses execution and hands the value to the caller. The next time `next()` is called, it resumes from exactly where it left off — local variables and all.

**Why this matters:** Generators are *lazy* — they produce values only when asked. This makes them extremely memory-efficient for large or even infinite sequences. A generator that produces 1 million numbers uses the same memory as one that produces 10.

**`yield from`** delegates to another iterable, making it easy to compose generators together.

```python
# Generator function — uses yield instead of return
def count_up(start, end):
    current = start
    while current <= end:
        yield current      # pause here, hand value to caller
        current += 1       # resume here on next call

for num in count_up(1, 5):
    print(num)   # 1, 2, 3, 4, 5

# Generator expression — like list comprehension but lazy (uses parentheses)
gen = (x**2 for x in range(1_000_000))  # no list built; values on demand
print(next(gen))   # 0
print(next(gen))   # 1

# Infinite generator — can only work because values are computed lazily
def naturals():
    n = 1
    while True:
        yield n
        n += 1

from itertools import islice
first_ten = list(islice(naturals(), 10))
print(first_ten)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Custom iterator class — implementing the iterator protocol manually
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self      # the object is its own iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration   # signals the for loop to stop
        self.current -= 1
        return self.current + 1

for n in Countdown(5):
    print(n)   # 5, 4, 3, 2, 1

# yield from — delegate to another iterable (great for recursive generators)
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # recurse into sub-lists
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], 5])))   # [1, 2, 3, 4, 5]
```

---

### 23. Context Managers

A **context manager** is an object that manages resources by defining what happens when you enter and exit a `with` block. Python guarantees the `__exit__` method is called even if an exception occurs — making it ideal for cleanup tasks like closing files, releasing locks, or disconnecting from a database.

**Two ways to create one:**
1. **Class-based** — implement `__enter__` and `__exit__` methods
2. **`@contextmanager` decorator** — write a generator function with `yield`; code before `yield` is setup, code after is teardown

The built-in `open()` function is a context manager — that's why `with open(...) as f:` automatically closes the file.

```python
# Class-based context manager
class DatabaseConnection:
    def __enter__(self):
        # Setup: acquire the resource
        print("Connecting to database...")
        self.connection = "mock_connection"
        return self.connection   # bound to the 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Teardown: always runs, even if an exception occurred
        print("Closing connection...")
        # Return True to suppress the exception, False to re-raise it
        return False

with DatabaseConnection() as conn:
    print(f"Using {conn}")
# Output:
# Connecting to database...
# Using mock_connection
# Closing connection...

# contextlib — simpler generator-based approach
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield              # execution of the with block happens here
    finally:
        elapsed = time.perf_counter() - start
        print(f"Elapsed: {elapsed:.4f}s")

with timer():
    result = sum(range(1_000_000))
# Elapsed: 0.0312s

# You can also use contextlib.suppress to silently ignore specific exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    open("nonexistent.txt")   # no crash — error silently ignored
```

**File:** `my_modules/files_handling/05_with.py`

---

### 24. Type Hinting

**Type hints** are annotations that describe the expected types of variables, function parameters, and return values. They were introduced in Python 3.5 and are entirely **optional** — Python does not enforce them at runtime.

**Why use them?**
- IDEs and editors use them to provide better auto-complete and catch bugs before running
- Tools like `mypy` can statically check your code for type errors
- They serve as inline documentation, making code much easier to understand at a glance

**`Optional[T]`** means the value can be `T` or `None`. Since Python 3.10 you can write `T | None` instead.

**`Protocol`** enables **structural subtyping** (duck typing, formalized). A class satisfies a Protocol if it has the required methods — no explicit `class Foo(MyProtocol)` needed.

```python
from typing import Optional, Union, Callable, TypedDict
from typing import Protocol

# Basic function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Variable annotations
count: int = 0
names: list[str] = ["Alice", "Bob"]
mapping: dict[str, int] = {"a": 1}

# Optional — the function may return None (e.g., when not found)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)   # returns str or None

# Union — accept multiple types (Python 3.10+ shorthand: int | str)
def process(value: int | str) -> str:
    return str(value)

# Callable — a function that takes one int and returns an int
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

# TypedDict — a dict with a known set of typed keys
class Movie(TypedDict):
    title: str
    year: int
    rating: float

film: Movie = {"title": "Inception", "year": 2010, "rating": 8.8}

# Protocol — structural typing (the class doesn't need to inherit from Protocol)
# Any class that has a draw() method satisfies the Drawable protocol
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())   # works — Circle matches the Drawable protocol
```

---

### 25. Enums & Data Classes

**Enums (Enumerations)** are a set of named, constant values. Instead of using bare strings or magic numbers (`status = 1`, `direction = "N"`), enums make the intent explicit, prevent typos, and enable IDE support.

**Data classes** (Python 3.7+) automatically generate boilerplate methods (`__init__`, `__repr__`, `__eq__`) for classes that primarily exist to hold data. You define the fields with type annotations and Python does the rest.

**When to use each:**
- **Enum** — for a fixed set of related constants (states, directions, colors, HTTP methods)
- **Dataclass** — for simple data containers where you'd otherwise write lots of repetitive `__init__` code

```python
# ── Enums ─────────────────────────────────────────────────────
from enum import Enum, auto

# auto() assigns values automatically (1, 2, 3, ...)
class Color(Enum):
    RED   = auto()
    GREEN = auto()
    BLUE  = auto()

class Direction(Enum):
    NORTH = "N"   # or assign explicit values
    SOUTH = "S"
    EAST  = "E"
    WEST  = "W"

print(Color.RED)          # Color.RED
print(Color.RED.value)    # 1
print(Color.RED.name)     # RED
print(list(Color))        # [Color.RED, Color.GREEN, Color.BLUE]

# Enums work in match statements (Python 3.10+)
def describe_color(c: Color) -> str:
    match c:
        case Color.RED:   return "warm"
        case Color.BLUE:  return "cool"
        case _:           return "other"

# ── Data Classes ──────────────────────────────────────────────
from dataclasses import dataclass, field

# @dataclass automatically creates __init__, __repr__, and __eq__
@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
print(p1)          # Point(x=1.0, y=2.0)
print(p1 == p2)    # True  — __eq__ compares all fields

# Default values and computed defaults
@dataclass
class Student:
    name: str
    age: int
    grades: list[float] = field(default_factory=list)   # mutable default

    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

s = Student("Alice", 20, [95.0, 87.5, 92.0])
print(s.average())   # 91.5

# frozen=True makes the dataclass immutable (like a named tuple, but typed)
@dataclass(frozen=True)
class RGB:
    r: int
    g: int
    b: int

red = RGB(255, 0, 0)
# red.r = 128   # raises FrozenInstanceError
```

---

### 26. Concurrency

**Concurrency** is about doing multiple things in overlapping time periods. Python offers three models:

- **Threading** — multiple threads share the same process memory. Good for **I/O-bound** tasks (network requests, reading files) because threads can wait while others run. Note: Python's **GIL (Global Interpreter Lock)** prevents true parallel CPU execution in threads.
- **Multiprocessing** — spawns separate processes, each with its own memory. Bypasses the GIL. Good for **CPU-bound** tasks (math, image processing).
- **`concurrent.futures`** — a high-level, unified interface for both threading and multiprocessing. The `Executor` pattern makes it easy to submit tasks and collect results.

**Rule of thumb:** I/O-bound → use `threading` or `asyncio`. CPU-bound → use `multiprocessing`.

```python
# ── Threading ─────────────────────────────────────────────────
import threading, time

def download(url):
    print(f"Downloading {url}...")
    time.sleep(2)              # simulate a network delay
    print(f"Done: {url}")

# All 5 threads run concurrently — total time ~2s, not 10s
threads = [threading.Thread(target=download, args=(f"url_{i}",)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()    # wait for all to complete

# Thread safety — use a Lock to prevent race conditions
counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    with lock:        # only one thread enters this block at a time
        counter += 1

# ── Multiprocessing ───────────────────────────────────────────
from multiprocessing import Pool

def square(x):
    return x ** 2

# Pool creates worker processes and distributes work across them
with Pool(4) as pool:
    results = pool.map(square, range(10))   # runs in parallel
print(results)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ── concurrent.futures — high-level interface ──────────────────
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ThreadPoolExecutor: same as threading but simpler API
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(download, f"url_{i}") for i in range(5)]
    results = [f.result() for f in futures]  # collect results
```

**Files:** `my_modules/external_modules/04_threading.py`, `my_modules/comprehensive_examples/07_concurrency_threading_multiprocessing.py`

---

### 27. Async / Await

**Asynchronous programming** is Python's most efficient model for I/O-bound work. While one task waits for a network response, the event loop runs another task — all in a single thread.

**Key concepts:**
- **Coroutine** — a function defined with `async def`. It doesn't run when called; it returns a coroutine object.
- **`await`** — suspends the current coroutine and hands control back to the event loop until the awaited task completes.
- **`asyncio.run()`** — the entry point; starts the event loop and runs a coroutine.
- **`asyncio.gather()`** — runs multiple coroutines *concurrently* and waits for all of them.

**vs. threading:** `asyncio` uses cooperative multitasking (you explicitly `await`). Threading uses preemptive multitasking (the OS switches threads). `asyncio` has less overhead and is better for thousands of concurrent connections (e.g., web servers).

```python
import asyncio

# async def creates a coroutine — not run immediately
async def fetch_data(url):
    print(f"Fetching {url}...")
    await asyncio.sleep(1)     # yield control to event loop (simulates network)
    return f"Data from {url}"

# Run a single coroutine
async def main():
    result = await fetch_data("https://api.example.com")
    print(result)

asyncio.run(main())

# Run multiple concurrently — all 3 start at once, total time ~1s not 3s
async def main():
    urls = ["url_1", "url_2", "url_3"]
    results = await asyncio.gather(*[fetch_data(u) for u in urls])
    for r in results:
        print(r)

asyncio.run(main())

# Async context manager — __aenter__ and __aexit__
class AsyncDB:
    async def __aenter__(self):
        print("Connecting...")
        return self

    async def __aexit__(self, *args):
        print("Disconnecting...")

async def main():
    async with AsyncDB() as db:
        print("Using DB")

# Async generator — yields values asynchronously
async def stream_data():
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for item in stream_data():
        print(item)
```

**File:** `my_modules/comprehensive_examples/01_async_await_basics.py`

---

### 28. Metaclasses

A **metaclass** is a class whose instances are themselves classes. Just as a regular class controls how its instances behave, a metaclass controls how classes are created and what they can do.

The default metaclass for all Python classes is `type`. When Python sees `class Foo:`, it calls `type("Foo", (bases,), {attributes})` behind the scenes.

**When to use:** Metaclasses are powerful but complex. In practice, they are used in frameworks (Django ORM, SQLAlchemy, pytest) to add automatic behaviour to all subclasses. Before reaching for a metaclass, consider if `__init_subclass__` or a class decorator solves your problem more simply.

```python
# type() is the built-in metaclass — you can use it to create classes dynamically
MyClass = type("MyClass", (object,), {"greet": lambda self: "Hello!"})
print(MyClass().greet())   # Hello!

# Custom metaclass — subclass type and override __call__ or __new__
# Example: Singleton pattern — only one instance allowed per class
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]   # always return the same object

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "connected"

db1 = Database()
db2 = Database()
print(db1 is db2)   # True — same instance every time

# __init_subclass__ — simpler alternative for many metaclass use cases
# Called automatically whenever the class is subclassed
class PluginBase:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase.plugins.append(cls)   # auto-register every subclass

class PluginA(PluginBase): pass
class PluginB(PluginBase): pass

print(PluginBase.plugins)   # [<class 'PluginA'>, <class 'PluginB'>]
```

---

### 29. Testing

**Testing** is the practice of verifying that your code behaves as expected. Writing tests prevents regressions (bugs that come back after being fixed) and gives you confidence to refactor.

**`unittest`** is Python's built-in testing framework, modelled after Java's JUnit. It uses classes and is verbose but requires no installation.

**`pytest`** is the de-facto standard in the Python community. It uses simple functions (no class required), has much cleaner output, and offers powerful features like parametrize, fixtures, and plugins.

**Key testing concepts:**
- **Unit test** — test a single function or method in isolation
- **Fixture** — setup code that provides test data or resources, run before each test
- **Parametrize** — run the same test with multiple sets of inputs
- **Assertion** — the check that confirms a result is correct

```python
# ── unittest ──────────────────────────────────────────────────
import unittest

def add(a, b):    return a + b
def divide(a, b):
    if b == 0: raise ValueError("Cannot divide by zero")
    return a / b

class TestMath(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)

    def test_divide_result(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=2)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

```python
# ── pytest (pip install pytest) ────────────────────────────────
# Run: pytest test_math.py -v

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)

# Parametrize — one test, many input/output combinations
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
])
def test_add_cases(a, b, expected):
    assert add(a, b) == expected

# Fixtures — setup code shared across multiple tests
@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4, 5]

def test_sum(sample_numbers):
    assert sum(sample_numbers) == 15

def test_max(sample_numbers):
    assert max(sample_numbers) == 5
```

---

### 30. Packaging & Virtual Environments

A **virtual environment** is an isolated Python installation for a specific project. It keeps that project's dependencies separate from other projects and from the system Python — preventing version conflicts.

**`pip`** is Python's package manager. It downloads packages from PyPI (Python Package Index).

A **package** is a distributable, installable piece of software. `pyproject.toml` is the modern way to describe your package's metadata and dependencies so others can install it with `pip`.

```bash
# Create a virtual environment in a folder called 'venv'
python -m venv venv

# Activate it (your prompt will change to show the venv name)
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

# Install packages into the active environment
pip install requests numpy pandas

# Save all installed packages and their exact versions
pip freeze > requirements.txt

# Reproduce the environment on another machine
pip install -r requirements.txt

# Deactivate when done
deactivate
```

```
# Standard Python package structure
my_package/
├── my_package/
│   ├── __init__.py      ← marks this as a package
│   ├── core.py
│   └── utils.py
├── tests/
│   └── test_core.py
├── README.md
├── requirements.txt
└── pyproject.toml       ← package metadata (modern standard)
```

```toml
# pyproject.toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "my_package"
version = "0.1.0"
description = "A short description"
dependencies = ["requests>=2.28"]
```

```bash
# Build and publish to PyPI
pip install build twine
python -m build            # creates dist/ folder with wheel and tar.gz
twine upload dist/*        # upload to PyPI (needs account)
```

**File:** `my_modules/comprehensive_examples/05_python_packaging_tutorial.py`

---

## Famous Libraries

---

### 31. Standard Library

Python's **standard library** is a massive collection of modules that ship with every Python installation — no install required. It covers file I/O, networking, math, dates, data structures, text processing, and much more.

```python
# os — interact with the operating system and filesystem
import os
print(os.getcwd())                        # current working directory
os.makedirs("new_dir/sub", exist_ok=True) # create nested directories
os.path.exists("file.txt")               # check if path exists
os.path.join("folder", "file.txt")       # OS-appropriate path separator

# pathlib — modern, object-oriented paths (preferred over os.path)
from pathlib import Path
p = Path("my_folder/data.txt")
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("hello")           # write directly
print(p.read_text())            # read directly
for f in Path(".").glob("*.py"):
    print(f)                    # find all .py files in current dir

# sys — Python interpreter info
import sys
print(sys.version)    # Python version string
print(sys.argv)       # command-line arguments as a list
sys.exit(0)           # exit with a status code

# math — mathematical functions
import math
math.sqrt(16), math.ceil(4.2), math.floor(4.8)
math.log(100, 10)     # 2.0
math.pi, math.e, math.factorial(5)

# datetime — dates, times, and durations
from datetime import datetime, timedelta, date
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # format to string
birthday = datetime.strptime("1990-06-15", "%Y-%m-%d")   # parse from string
tomorrow = now + timedelta(days=1)          # arithmetic on dates

# collections — specialised container types
from collections import Counter, defaultdict, deque, namedtuple

# Counter: count occurrences of elements
words = ["apple", "banana", "apple", "cherry", "apple"]
print(Counter(words).most_common(2))   # [('apple', 3), ('banana', 1)]

# defaultdict: no KeyError for missing keys — auto-creates with default
dd = defaultdict(list)
dd["fruits"].append("apple")   # 'fruits' key created automatically

# deque: double-ended queue — O(1) append/pop from both ends
q = deque([1, 2, 3])
q.appendleft(0)    # [0, 1, 2, 3]
q.popleft()        # 0

# namedtuple: immutable record with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)   # 3 4

# itertools — efficient looping tools
from itertools import chain, combinations, permutations, product

list(chain([1, 2], [3, 4]))              # [1, 2, 3, 4]  — merge iterables
list(combinations([1,2,3], 2))           # [(1,2),(1,3),(2,3)]
list(permutations([1,2,3], 2))
list(product([0,1], repeat=3))           # all 3-bit binary combinations

# functools — higher-order functions
from functools import partial, lru_cache

@lru_cache(maxsize=128)        # memoize expensive function calls
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

power_of_2 = partial(pow, 2)   # pre-fill the first argument of pow()
print(power_of_2(10))          # 1024

# random — random number generation
import random
random.random()                            # float in [0.0, 1.0)
random.randint(1, 100)                     # integer in [1, 100]
random.choice(["a", "b", "c"])            # random element
random.shuffle([1, 2, 3, 4, 5])           # shuffle in place

# logging — production-ready alternative to print() for debugging
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logging.debug("Detailed diagnostic info")
logging.info("Informational message")
logging.warning("Something unexpected happened")
logging.error("A serious error occurred")
logging.critical("Program cannot continue")
```

---

### 32. Data Science — NumPy, Pandas, Matplotlib

These three libraries form the foundation of data science and scientific computing in Python.

- **NumPy** provides fast, multi-dimensional arrays (ndarray) and mathematical operations on them. Most data science libraries are built on top of it.
- **Pandas** provides DataFrames — labelled, tabular data structures that make loading, cleaning, and analysing datasets intuitive.
- **Matplotlib** is the core plotting library. **Seaborn** is built on top of it for statistical visualizations with less code.

```bash
pip install numpy pandas matplotlib seaborn
```

#### NumPy — fast numerical arrays

```python
import numpy as np

# NumPy arrays are faster and more memory-efficient than Python lists
# because they store homogeneous data in contiguous memory
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)    # (5,)   — 1D array with 5 elements
print(b.shape)    # (2, 3) — 2 rows, 3 columns
print(b.dtype)    # int64  — element type

# Array creation shortcuts
np.zeros((3, 3))              # 3x3 matrix of zeros
np.ones((2, 4))               # 2x4 matrix of ones
np.arange(0, 10, 0.5)         # like range() but supports floats
np.linspace(0, 1, 5)          # 5 evenly spaced values: 0, .25, .5, .75, 1.0
np.random.rand(3, 3)          # random floats in [0, 1)

# Vectorized operations — no loops needed, operates on all elements at once
print(a * 2)         # [2, 4, 6, 8, 10]
print(a ** 2)        # [1, 4, 9, 16, 25]
print(np.sqrt(a))

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
A @ B                          # matrix multiplication
np.linalg.inv(A)               # matrix inverse

# Indexing and slicing (much more powerful than lists)
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr[0, :]          # first row:  [1, 2, 3]
arr[:, 1]          # second col: [2, 5, 8]
arr[arr > 4]       # boolean indexing: [5, 6, 7, 8, 9]

# Statistics
np.mean(a), np.std(a), np.sum(a), np.min(a), np.max(a)
```

#### Pandas — data manipulation

```python
import pandas as pd

# DataFrame — 2D table with labelled rows and columns
data = {
    "name":  ["Alice", "Bob", "Charlie", "Diana"],
    "age":   [25, 30, 35, 28],
    "city":  ["NYC", "LA", "Chicago", "NYC"],
    "score": [92.5, 85.0, 78.3, 95.1],
}
df = pd.DataFrame(data)

# Exploration
print(df.head())        # first 5 rows
print(df.info())        # column types and null counts
print(df.describe())    # statistical summary (mean, std, min, max, ...)

# Selecting data
df["name"]              # one column → Series
df[["name", "age"]]     # multiple columns → DataFrame
df.iloc[0]              # first row by position
df.loc[df["age"] > 28]  # filter rows where age > 28

# Transforming
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else "B")

# GroupBy — split into groups, apply a function, combine results
df.groupby("city")["score"].mean()

# Sorting
df.sort_values("score", ascending=False)

# File I/O
df.to_csv("students.csv", index=False)
df2 = pd.read_csv("students.csv")

# Handling missing values — real-world data always has gaps
df.dropna()           # remove rows with any missing value
df.fillna(0)          # fill missing values with 0
df.isna().sum()       # count missing values per column

# Merge / join — combine two DataFrames like a SQL join
df1 = pd.DataFrame({"id": [1,2,3], "name": ["A","B","C"]})
df2 = pd.DataFrame({"id": [1,2,4], "score": [90,85,78]})
pd.merge(df1, df2, on="id", how="inner")  # only rows with matching ids
```

#### Matplotlib & Seaborn — visualization

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="o", label="linear")
plt.title("Line Plot"); plt.xlabel("x"); plt.ylabel("y")
plt.legend(); plt.show()

# Bar chart and histogram
plt.bar(["A","B","C","D"], [23, 45, 12, 67])
plt.show()

import numpy as np
plt.hist(np.random.normal(50, 10, 1000), bins=30)
plt.show()

# Subplots — multiple plots in one figure
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x, y); axes[0].set_title("Left")
axes[1].bar(["A","B"], [1,2]); axes[1].set_title("Right")
plt.tight_layout(); plt.show()

# Seaborn — higher-level statistical plots with less code
df = sns.load_dataset("tips")
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
sns.boxplot(data=df, x="day", y="total_bill")
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
```

**Files:** `my_modules/comprehensive_examples/08_pandas_data_analysis.py`, `09_vectors_numerical_computing.py`

---

### 33. Web Development — Flask, FastAPI

**Flask** is a lightweight "micro" web framework. It gives you the essentials (routing, request handling, templating) without enforcing a project structure. Great for small to medium APIs and web apps.

**FastAPI** is a modern, high-performance framework built on top of Python's async capabilities and Pydantic. It automatically generates interactive API documentation and validates request/response data using type hints.

**Django** (not shown here) is the "batteries-included" framework — it comes with a built-in ORM, admin panel, authentication, and more. Best for larger, full-featured web applications.

```bash
pip install flask
pip install fastapi uvicorn
```

#### Flask

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route — maps a URL to a Python function
@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"

# Dynamic URL segments
@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

# REST API endpoint — GET all users
@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

# REST API endpoint — create a new user
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()       # parse JSON request body
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201   # 201 Created

if __name__ == "__main__":
    app.run(debug=True)
```

#### FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model — defines the shape and validation of request/response data
class User(BaseModel):
    name: str
    age: int

users = []

@app.get("/users")
def get_users():
    return users

@app.post("/users", status_code=201)
def create_user(user: User):
    users.append(user)
    return user

# Run: uvicorn main:app --reload
# Auto-generated interactive docs at: http://127.0.0.1:8000/docs
```

**File:** `my_modules/flask_basic/main.py`

---

### 34. HTTP & APIs — Requests, HTTPX

**`requests`** is the most popular HTTP library in Python. It makes sending HTTP requests (GET, POST, PUT, DELETE) and handling responses simple and readable. Virtually every Python developer uses it.

**`httpx`** is a modern alternative with the same API as `requests` but adds **async support** — essential when you need to make many concurrent HTTP calls in an async application.

**REST APIs** communicate using standard HTTP methods, status codes, and JSON. Understanding how to make and handle these requests is fundamental to integrating with any web service.

```bash
pip install requests httpx
```

```python
import requests

# GET — retrieve data
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)   # 200 = OK
data = response.json()        # parse JSON response body

# GET with query parameters — ?userId=1 appended to URL
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

# POST — send data to create a resource
payload = {"title": "New Post", "body": "Content", "userId": 1}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload              # automatically sets Content-Type: application/json
)
print(response.status_code)   # 201 = Created

# Authentication via headers
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get("https://api.example.com/data", headers=headers)

# Robust error handling — always handle failures in production
try:
    r = requests.get("https://api.example.com", timeout=5)
    r.raise_for_status()      # raises HTTPError for 4xx/5xx responses
    data = r.json()
except requests.Timeout:
    print("Request timed out")
except requests.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.ConnectionError:
    print("Network problem")

# Session — reuse connection and share headers/cookies across requests
with requests.Session() as s:
    s.headers.update({"Authorization": "Bearer TOKEN"})
    r1 = s.get("https://api.example.com/endpoint1")
    r2 = s.get("https://api.example.com/endpoint2")
```

```python
# httpx — async version (great for FastAPI or asyncio apps)
import httpx, asyncio

# Sync (identical API to requests)
response = httpx.get("https://httpbin.org/get")
print(response.json())

# Async — makes concurrent requests efficiently
async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]

asyncio.run(fetch_all(["https://httpbin.org/get"] * 3))
```

**File:** `my_modules/external_modules/02_requests_modules.py`

---

### 35. Web Scraping — BeautifulSoup, Selenium

**Web scraping** is the automated extraction of data from websites. It's used for price monitoring, research data collection, content aggregation, and more.

- **BeautifulSoup** parses static HTML (the raw HTML the server sends). Use it when the page content is in the initial HTML response.
- **Selenium** automates a real browser. Use it when content is loaded dynamically by JavaScript (e.g., infinite scroll, single-page apps) or when you need to click buttons and fill forms.

> Always check a site's `robots.txt` and Terms of Service before scraping. Be respectful — add delays between requests.

```bash
pip install beautifulsoup4 requests
pip install selenium
```

```python
# BeautifulSoup — parse and navigate HTML/XML
import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

# Navigate the DOM tree
title = soup.find("title").text
print(title)

# Find all matching elements
books = soup.find_all("article", class_="product_pod")
for book in books[:5]:
    name  = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    print(f"{name}: {price}")

# CSS selectors — same syntax as browser developer tools
links = [a["href"] for a in soup.select("a[href]")[:5]]

# Selenium — control a real browser for JavaScript-heavy sites
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()    # needs ChromeDriver installed
driver.get("https://example.com")

# Interact with page elements
search_box = driver.find_element(By.ID, "search")
search_box.send_keys("python")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for dynamic content to appear before reading it
result = WebDriverWait(driver, timeout=10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "result"))
)
print(result.text)
driver.quit()
```

---

### 36. Databases — SQLAlchemy, SQLite

Databases store data that persists beyond the lifetime of your program. Python has excellent built-in support for SQLite and excellent third-party support for all major databases.

- **`sqlite3`** — built-in, zero-config, file-based database. Perfect for development, small apps, and local storage.
- **SQLAlchemy** — the most popular Python ORM (Object Relational Mapper). It lets you work with databases using Python classes instead of raw SQL, and supports SQLite, PostgreSQL, MySQL, and more.

**ORM advantage:** Instead of writing `INSERT INTO users ...`, you write `session.add(user)`. Database tables map to Python classes; rows map to objects.

```bash
pip install sqlalchemy
```

```python
# ── sqlite3 — raw SQL ─────────────────────────────────────────
import sqlite3

# connect() creates the file if it doesn't exist
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

# Use ? placeholders to prevent SQL injection
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)",
               ("Alice", "alice@example.com"))
conn.commit()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)   # (1, 'Alice', 'alice@example.com')

conn.close()

# ── SQLAlchemy — ORM ──────────────────────────────────────────
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

# Each class maps to a database table
class User(Base):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String, nullable=False)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"

engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)   # create tables if they don't exist

# Session manages the database connection and transaction
with Session(engine) as session:
    alice = User(name="Alice", email="alice@example.com")
    session.add(alice)
    session.commit()

    users = session.query(User).all()
    print(users)

    alice = session.query(User).filter_by(name="Alice").first()
    print(alice)
```

---

### 37. AI & Machine Learning

Python is the dominant language for AI and ML because of its rich ecosystem. Three tiers of tools:

1. **Scikit-learn** — classical machine learning (regression, classification, clustering). Best for structured/tabular data.
2. **PyTorch / TensorFlow** — deep learning frameworks for training neural networks on images, text, and sequences.
3. **LLM APIs** — call pre-trained large language models via an API without training your own model.

```bash
pip install scikit-learn
pip install torch torchvision    # or: pip install tensorflow
pip install openai anthropic
```

#### Scikit-learn — the ML pipeline

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Load data
X, y = load_iris(return_X_y=True)

# 2. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Preprocess — scale features to have mean=0, std=1
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)     # use the same scaler fitted on train

# 4. Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Evaluate
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
print(classification_report(y_test, predictions))

# All sklearn models share the same fit/predict API — easy to swap
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
```

#### LLM APIs — call AI models

```python
# OpenAI API
from openai import OpenAI
client = OpenAI(api_key="YOUR_KEY")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "Explain list comprehensions in Python."}
    ]
)
print(response.choices[0].message.content)

# Anthropic Claude API
import anthropic
client = anthropic.Anthropic(api_key="YOUR_KEY")
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explain decorators in Python."}]
)
print(message.content[0].text)
```

**File:** `my_modules/ai/03_llm_api.py`

---

### 38. Automation & CLI

Python is excellent for automation — running tasks on a schedule, processing files in bulk, and building command-line tools that accept arguments.

**`argparse`** (standard library) lets your script accept command-line arguments with help text and validation built in.

**`click`** is a third-party library that makes building CLI tools elegant using decorators. It handles argument parsing, validation, and help text with minimal boilerplate.

**`schedule`** runs functions on a recurring schedule (every 30 minutes, every day at 9am, etc.) within a long-running Python process.

```bash
pip install click schedule
```

#### argparse — standard library CLI

```python
import argparse

parser = argparse.ArgumentParser(description="Process a file")
parser.add_argument("filename",                          help="Input file")
parser.add_argument("-o", "--output", default="out.txt", help="Output file")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-n", "--count",  type=int, default=10)

args = parser.parse_args()
# Run: python script.py input.txt -o result.txt -v -n 20
# Automatic --help generated from the descriptions above
```

#### click — elegant CLI framework

```python
import click

@click.command()
@click.argument("name")
@click.option("--count", default=1,   help="Number of greetings")
@click.option("--shout", is_flag=True,help="Make it uppercase")
def hello(name, count, shout):
    """Greet someone by name."""
    for _ in range(count):
        msg = f"Hello, {name}!"
        click.echo(msg.upper() if shout else msg)

if __name__ == "__main__":
    hello()
# Run: python script.py Alice --count 3 --shout
```

#### schedule — task scheduling

```python
import schedule, time

def send_reminder():
    print("Remember to drink water!")

def daily_backup():
    print("Running backup...")

schedule.every(30).minutes.do(send_reminder)
schedule.every().day.at("09:00").do(daily_backup)
schedule.every().monday.do(daily_backup)

# Keep the program running to allow the schedule to trigger
while True:
    schedule.run_pending()
    time.sleep(1)
```

#### shutil — file operations

```python
import shutil

shutil.copy("source.txt", "destination.txt")    # copy file
shutil.copy2("source.txt", "backup/")           # copy preserving metadata
shutil.move("old.txt", "new.txt")               # move or rename
shutil.rmtree("old_folder")                     # delete folder and all contents
shutil.make_archive("backup", "zip", "folder/") # create a zip archive
```

**Files:** `my_modules/files_handling/07_shutil.py`, `08_argparse.py`

---

### 39. Useful Utilities

These libraries solve common real-world problems and appear frequently across Python projects.

```bash
pip install pydantic Pillow rich python-dotenv
```

#### pydantic — data validation

Pydantic defines the shape of your data using Python type hints and validates it automatically. It is the backbone of FastAPI's request/response validation and is used anywhere you need to parse external data (API responses, config files, user input) into structured Python objects.

```python
from pydantic import BaseModel, field_validator
from typing import Optional

class User(BaseModel):
    name:  str
    age:   int
    email: str
    score: Optional[float] = None   # optional field with default None

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v

user = User(name="Alice", age=30, email="alice@example.com")
print(user.model_dump())     # {'name': 'Alice', 'age': 30, ...}

try:
    bad = User(name="Bob", age=-5, email="bob@example.com")
except Exception as e:
    print(e)   # ValidationError with details
```

#### Pillow — image processing

Pillow is the go-to library for image manipulation: resizing thumbnails, converting formats, applying filters, drawing text on images, and batch processing image files.

```python
from PIL import Image, ImageFilter, ImageDraw

img = Image.open("photo.jpg")
print(img.size, img.mode)   # (1920, 1080) RGB

# Resize and save
img.resize((800, 600)).save("resized.jpg")

# Apply filters
img.filter(ImageFilter.BLUR).save("blurred.jpg")
img.filter(ImageFilter.SHARPEN).save("sharp.jpg")

# Convert format
img.save("photo.png")    # simply change the extension

# Draw on the image
draw = ImageDraw.Draw(img)
draw.rectangle([10, 10, 100, 100], outline="red", width=3)
draw.text((50, 50), "Hello!", fill="white")
img.save("annotated.jpg")
```

#### rich — beautiful terminal output

Rich makes terminal output readable and professional — coloured text, formatted tables, progress bars, syntax-highlighted code, and more.

```python
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

# Coloured, styled output using markup tags
console.print("[bold green]Success![/bold green]")
console.print("[red]Error:[/red] Something went wrong")
console.print("[yellow]Warning:[/yellow] Disk space low")

# Pretty table
table = Table(title="Users")
table.add_column("Name",  style="cyan")
table.add_column("Age",   style="magenta")
table.add_column("Score", style="green")
table.add_row("Alice", "30", "92.5")
table.add_row("Bob",   "25", "85.0")
console.print(table)

# Progress bar — wrap any iterable
for item in track(range(100), description="Processing..."):
    pass   # your work here
```

#### python-dotenv — environment variables

Store sensitive configuration (API keys, database URLs, secrets) in a `.env` file instead of hardcoding them in your source code. Never commit `.env` to version control.

```python
# .env file (in project root, added to .gitignore):
# API_KEY=abc123secret
# DATABASE_URL=postgresql://user:pass@localhost/mydb

from dotenv import load_dotenv
import os

load_dotenv()   # reads .env and sets environment variables

api_key = os.getenv("API_KEY")
db_url  = os.getenv("DATABASE_URL", "sqlite:///default.db")  # with fallback
```

---

## Repository Structure

```
my_modules/
├── basic_concepts/          # Variables, loops, functions, data structures
├── oops_concepts/           # Classes, inheritance, operator overloading
├── advanced_concepts/       # Decorators, error handling, functional programming
├── datastructures/          # Trees, algorithms
├── files_handling/          # File I/O, os, shutil, argparse
├── external_modules/        # requests, threading, regex
├── comprehensive_examples/  # Async, packaging, Pandas, NumPy, concurrency
├── flask_basic/             # Web development with Flask
├── ai/                      # AI projects and LLM API usage
└── python_projects/         # Complete mini-projects
    ├── calculator/
    ├── millionaire/
    ├── news-api/
    ├── pdfmerger/
    └── drink-water-reminder/
```

---

*Work through the concepts in order. Run every example. Modify them and see what happens. The best way to learn Python is to write Python.*
