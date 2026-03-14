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

Variables store data. Python is dynamically typed — no need to declare the type.

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

# Swap variables
a, b = 10, 20
a, b = b, a             # a=20, b=10

# Type conversion
print(int("42"))        # 42
print(float("3.14"))    # 3.14
print(str(100))         # "100"
```

**File:** `my_modules/basic_concepts/basics.py`

---

### 2. Input & Output

```python
# Print with formatting
print("Name:", "Alice", "Age:", 25)
print("joined", "with", "dashes", sep="-")

# f-strings (recommended)
name, age = "Alice", 30
print(f"Hello, {name}! You are {age} years old.")
print(f"Pi: {3.14159:.2f}")        # Pi: 3.14
print(f"Score: {0.845:.1%}")       # Score: 84.5%

# User input (always returns string)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

---

### 3. Operators

```python
# Arithmetic
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3  (floor division)
print(10 % 3)   # 1  (modulo)
print(2 ** 10)  # 1024 (power)

# Comparison
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 3)    # True

# Logical
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Assignment shortcuts
x = 10
x += 5   # 15
x -= 3   # 12
x *= 2   # 24
x //= 4  # 6

# Identity and membership
a = [1, 2, 3]
b = a
print(a is b)       # True (same object)
print(2 in a)       # True
print(5 not in a)   # True

# Bitwise
print(0b1010 & 0b1100)  # 8  (AND)
print(0b1010 | 0b1100)  # 14 (OR)
print(0b1010 ^ 0b1100)  # 6  (XOR)
print(~0b1010)           # -11 (NOT)
print(1 << 3)            # 8  (left shift)
print(16 >> 2)           # 4  (right shift)

# Walrus operator := (Python 3.8+) — assign and return in one expression
numbers = [1, -3, 5, -2, 8]
if (n := len(numbers)) > 3:
    print(f"List has {n} items")   # List has 5 items

# Useful in while loops
import re
while chunk := input("Enter text (blank to stop): "):
    print(f"Got: {chunk}")
```

---

### 4. Conditional Statements

```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary
status = "adult" if age >= 18 else "minor"

# match / case (Python 3.10+)
command = "quit"
match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":
        print("Stopping...")
    case _:
        print("Unknown command")
```

---

### 5. Loops

```python
# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# range()
for i in range(2, 10, 2):   # 2, 4, 6, 8
    print(i)

# enumerate — index + value
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control: break, continue, else
for i in range(10):
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
    print(i)

for i in range(5):
    print(i)
else:
    print("Done")   # runs if no break occurred

# zip — iterate two sequences together
names = ["Alice", "Bob", "Charlie"]
ages  = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

**File:** `my_modules/basic_concepts/loops.py`

---

### 6. Functions

```python
# Basic
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))            # Hello, Bob!
print(greet("Bob", "Hi"))      # Hi, Bob!

# Keyword arguments
def describe(name, age, city):
    print(f"{name}, {age}, {city}")

describe(age=30, city="NYC", name="Alice")

# *args and **kwargs
def total(*numbers):
    return sum(numbers)

def profile(**info):
    for k, v in info.items():
        print(f"{k}: {v}")

total(1, 2, 3, 4)                           # 10
profile(name="Alice", age=30, city="NYC")

# Return multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9])

# Closures — inner function captures outer variable
def make_counter(start=0):
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())   # 1
print(c())   # 2
print(c())   # 3

# Recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))   # 120
```

**File:** `my_modules/basic_concepts/functions.py`

---

### 7. Scopes

Python resolves names in this order: **Local → Enclosing → Global → Built-in** (LEGB).

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local

    inner()
    print(x)       # enclosing

outer()
print(x)           # global

# global keyword — modify global from inside function
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)   # 1

# nonlocal keyword — modify enclosing scope from nested function
def make_adder(n):
    total = 0
    def add(x):
        nonlocal total
        total += x
        return total
    return add

adder = make_adder(0)
print(adder(5))    # 5
print(adder(3))    # 8
```

**File:** `my_modules/basic_concepts/pythonscopes.py`

---

### 8. Data Structures

#### Lists — ordered, mutable

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("date")          # add to end
fruits.insert(1, "avocado")    # insert at index
fruits.remove("banana")        # remove by value
popped = fruits.pop()          # remove and return last
fruits.sort()
fruits.reverse()

print(fruits[0])               # first
print(fruits[-1])              # last
print(fruits[1:3])             # slice
print(len(fruits))
print("apple" in fruits)       # True
```

#### Tuples — ordered, immutable

```python
point = (3, 4)
x, y = point           # unpacking

# Use for fixed data: coordinates, RGB, records
rgb = (255, 128, 0)
```

#### Sets — unordered, unique values

```python
nums = {1, 2, 3, 3, 2}
print(nums)            # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)           # {2, 3}  intersection
print(a | b)           # {1, 2, 3, 4}  union
print(a - b)           # {1}  difference
print(a ^ b)           # {1, 4}  symmetric difference
```

#### Dictionaries — key-value pairs

```python
person = {"name": "Alice", "age": 30}

print(person["name"])
print(person.get("email", "N/A"))  # default if missing

person["email"] = "alice@example.com"
del person["age"]

for key, value in person.items():
    print(f"{key}: {value}")

# Merging dicts (Python 3.9+)
a = {"x": 1}
b = {"y": 2}
merged = a | b          # {'x': 1, 'y': 2}
```

**Files:** `my_modules/basic_concepts/datastructures.py`, `Sets.py`, `15_dictionaries.py`

---

### 9. Strings

```python
text = "Hello, World!"

print(text.upper())                         # HELLO, WORLD!
print(text.lower())                         # hello, world!
print(text.strip())                         # remove whitespace
print(text.replace("World", "Python"))
print(text.split(", "))                     # ['Hello', 'World!']
print(", ".join(["a", "b", "c"]))          # a, b, c

# Slicing
print(text[0:5])    # Hello
print(text[-6:])    # World!
print(text[::-1])   # !dlroW ,olleH

# Checking
print(text.startswith("Hello"))  # True
print(text.endswith("!"))        # True
print("world" in text.lower())   # True
print("42".isdigit())            # True

# Multi-line
poem = """
Roses are red,
Violets are blue.
"""

# Raw string (file paths, regex)
path = r"C:\Users\Alice\Documents"

# Format methods
print("{} is {}".format("Python", "great"))
print(f"{'left':<10}|{'right':>10}")   # padding/alignment
```

**File:** `my_modules/basic_concepts/stringsInPython.py`

---

## Intermediate

---

### 10. Comprehensions

Clean one-liners for building collections.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension
squares = [x**2 for x in numbers]
evens   = [x for x in numbers if x % 2 == 0]

# Nested
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]

# Dict comprehension
square_map = {x: x**2 for x in range(1, 6)}

# Set comprehension
unique_lengths = {len(word) for word in ["cat", "dog", "elephant"]}

# Generator expression — memory-efficient, doesn't build a list
total = sum(x**2 for x in range(1_000_000))
```

---

### 11. File Handling

```python
# Write
with open("data.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Read
with open("data.txt", "r") as f:
    content = f.read()

# Read line by line
with open("data.txt") as f:
    for line in f:
        print(line.strip())

# Append
with open("data.txt", "a") as f:
    f.write("Line 3\n")

# JSON
import json

data = {"name": "Alice", "scores": [95, 87, 92]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    loaded = json.load(f)

# CSV
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

```python
# Basic
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple + else + finally
try:
    data = int("42")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Success: {data}")   # runs only if no exception
finally:
    print("Always runs")        # cleanup goes here

# Raise exceptions
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError(f"Insufficient funds: {balance}")
    return balance - amount

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount} from {balance}")
        self.balance = balance
        self.amount = amount

try:
    raise InsufficientFundsError(100, 200)
except InsufficientFundsError as e:
    print(e)
```

**Files:** `my_modules/advanced_concepts/07_errors.py`, `08_raise_errors.py`, `09_else_finally.py`

---

### 13. Modules & Imports

```python
# Import entire module
import math
print(math.sqrt(16))     # 4.0

# Import specific names
from math import sqrt, pi

# Import with alias
import numpy as np
import pandas as pd

# Your own module
# utils.py
def add(a, b):
    return a + b

# main.py
from utils import add

# Package — folder with __init__.py
from my_modules.basic_concepts.functions import some_function

# __name__ guard — code only runs when file is executed directly
if __name__ == "__main__":
    print("Running directly")
```

**Files:** `my_modules/basic_concepts/modules_in_python.py`, `mymodule.py`

---

### 14. Regular Expressions

```python
import re

text = "Contact: info@example.com or support@python.org at +1-800-555-0100"

# Search — find first match
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print(match.group())         # +1-800-555-0100 (last part)

# Findall — all matches
emails = re.findall(r"[\w.]+@[\w.]+", text)
print(emails)   # ['info@example.com', 'support@python.org']

# Substitution
cleaned = re.sub(r"\s+", " ", "too   many    spaces")
print(cleaned)  # too many spaces

# Groups
pattern = r"(\w+)@(\w+)\.(\w+)"
for m in re.finditer(pattern, text):
    print(m.group(0))   # full match
    print(m.group(1))   # username part

# Common patterns
r"\d+"       # one or more digits
r"\w+"       # word characters (letters, digits, _)
r"[a-z]+"   # lowercase letters
r"^\d{4}$"  # exactly 4 digits, full string
r"https?://"# http or https

# Compile for reuse
phone_re = re.compile(r"\+?\d[\d\-]{7,}")
```

**File:** `my_modules/external_modules/03_regular_expressions.py`

---

### 15. Classes & OOP

```python
class Dog:
    species = "Canis lupus familiaris"   # class attribute

    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Dog({self.name!r}, {self.age!r})"

rex = Dog("Rex", 5)
print(rex.bark())       # Rex says: Woof!
print(rex)              # Dog(name=Rex, age=5)
print(Dog.species)

# Class with property (encapsulated attribute)
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

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

```python
from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass   # subclasses must implement this

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow!"

# Polymorphism — same interface, different behavior
animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())

# Type checks
print(isinstance(animals[0], Animal))   # True
print(issubclass(Dog, Animal))          # True

# Multiple inheritance
class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class FlyingDog(Dog, Flyable):
    pass

superdog = FlyingDog("Krypto")
print(superdog.speak())   # Krypto: Woof!
print(superdog.fly())     # Krypto is flying!

# super() — call parent method
class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def speak(self):
        return f"{super().speak()} (Guide dog for {self.owner})"
```

**File:** `my_modules/oops_concepts/04_inheritance.py`

---

### 17. Magic / Dunder Methods

Special methods that Python calls automatically (surrounded by double underscores).

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representations
    def __str__(self):           # for print()
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):          # for debugging
        return f"Vector({self.x!r}, {self.y!r})"

    # Arithmetic operators
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return abs(self) < abs(other)

    # Length / magnitude
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __len__(self):
        return 2   # number of dimensions

    # Make iterable
    def __iter__(self):
        yield self.x
        yield self.y

    # Boolean test
    def __bool__(self):
        return self.x != 0 or self.y != 0

    # Container access
    def __getitem__(self, index):
        return (self.x, self.y)[index]

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)        # Vector(4, 6)
print(abs(v1))        # 2.23...
print(list(v1))       # [1, 2]
print(v1[0])          # 1

# Context manager protocol
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        return False   # don't suppress exceptions

with ManagedResource() as r:
    print("Using resource")
```

**File:** `my_modules/advanced_concepts/06_dunder_magic_methods.py`, `05_operator_overloading.py`

---

### 18. Functional Programming

```python
from functools import reduce

# Lambda — anonymous single-expression function
square  = lambda x: x ** 2
add     = lambda x, y: x + y

# map — apply function to every item
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))   # [1, 4, 9, 16, 25]

# filter — keep items where function is True
evens   = list(filter(lambda x: x % 2 == 0, numbers))   # [2, 4]

# reduce — accumulate to single value
total   = reduce(lambda acc, x: acc + x, numbers)        # 15
product = reduce(lambda acc, x: acc * x, numbers)        # 120

# Sorting with key
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
people.sort(key=lambda p: p[1])          # sort by age

words = ["banana", "apple", "cherry"]
words.sort(key=len)                       # sort by length

# First-class functions — pass functions as arguments
def apply(func, value):
    return func(value)

print(apply(square, 5))   # 25
print(apply(str, 42))     # "42"
```

**Files:** `my_modules/advanced_concepts/11_map.py`, `12_filter.py`, `13_reduce.py`

---

### 19. Built-in Functions

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))        # 8
print(min(numbers))        # 1
print(max(numbers))        # 9
print(sum(numbers))        # 31
print(sorted(numbers))     # sorted copy
print(list(reversed(numbers)))

# zip
names = ["Alice", "Bob", "Charlie"]
ages  = [30, 25, 35]
pairs = list(zip(names, ages))   # [('Alice', 30), ...]

# enumerate
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# any / all
print(any([False, True, False]))   # True
print(all([True, True, True]))     # True

# Type conversions
int("42"), float("3.14"), str(100)
list((1, 2, 3)), tuple([1, 2]), set([1, 2, 2, 3])

# abs, round, divmod, pow
print(abs(-5))              # 5
print(round(3.14159, 2))    # 3.14
print(divmod(10, 3))        # (3, 1)
print(pow(2, 10, 1000))     # 24 (2^10 mod 1000)

# vars, dir, hasattr, getattr, setattr
class Foo:
    x = 1
print(hasattr(Foo, "x"))    # True
print(getattr(Foo, "x"))    # 1
```

---

## Advanced

---

### 20. Decorators

Decorators wrap a function to add behavior without modifying it.

```python
import functools
import time

# Basic decorator
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

add(2, 3)

# Decorator with arguments
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

# Useful built-in decorators
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

# Timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper
```

**Files:** `my_modules/advanced_concepts/01_decorators.py`, `02_decorators_with_arguments.py`

---

### 21. Property, Classmethod & Staticmethod

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    # @property — getter (access like an attribute, not a method)
    @property
    def celsius(self):
        return self._celsius

    # @<prop>.setter — validate on assignment
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # @classmethod — receives the class (cls), not the instance
    # Use to create alternative constructors
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # @staticmethod — utility function, no access to class or instance
    @staticmethod
    def is_valid_radius(r):
        return r > 0

t = Temperature(25)
print(t.celsius)       # 25
print(t.fahrenheit)    # 77.0
t.celsius = 30

c = Circle.from_diameter(10)
print(c.radius)                      # 5.0
print(Circle.is_valid_radius(-1))    # False
```

**Files:** `my_modules/advanced_concepts/03_getter_and_setter.py`, `04_property_decorator.py`, `05_instance_static_class_methods.py`

---

### 22. Generators & Iterators

Generators produce values lazily — memory efficient for large sequences.

```python
# Generator function — yield instead of return
def count_up(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

for num in count_up(1, 5):
    print(num)   # 1, 2, 3, 4, 5

# Generator expression (like list comprehension but lazy)
gen = (x**2 for x in range(1_000_000))
print(next(gen))   # 0
print(next(gen))   # 1

# Infinite generator
def naturals():
    n = 1
    while True:
        yield n
        n += 1

from itertools import islice
first_ten = list(islice(naturals(), 10))

# Custom iterator with __iter__ and __next__
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in Countdown(5):
    print(n)   # 5, 4, 3, 2, 1

# yield from — delegate to another generator
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

print(list(flatten([1, [2, [3, 4]], 5])))   # [1, 2, 3, 4, 5]
```

---

### 23. Context Managers

Handle setup and teardown automatically via the `with` statement.

```python
# Class-based context manager
class DatabaseConnection:
    def __enter__(self):
        print("Connecting...")
        self.connection = "mock_connection"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection...")
        return False   # return True to suppress exceptions

with DatabaseConnection() as conn:
    print(f"Using {conn}")

# contextlib — simpler approach
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        print(f"Elapsed: {time.time() - start:.4f}s")

with timer():
    result = sum(range(1_000_000))
```

**File:** `my_modules/files_handling/05_with.py`

---

### 24. Type Hinting

Type hints make code readable and enable IDE support. Not enforced at runtime.

```python
from typing import Optional, Union, Callable, TypedDict
from collections.abc import Sequence

# Basic hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# Variable annotations
count: int = 0
names: list[str] = ["Alice", "Bob"]
mapping: dict[str, int] = {"a": 1}

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Union (Python 3.10+: use X | Y)
def process(value: int | str) -> str:
    return str(value)

# Callable
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

# TypedDict
class Movie(TypedDict):
    title: str
    year: int
    rating: float

# Protocol — structural subtyping (duck typing, formalized)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing circle")

def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())   # works — Circle matches Drawable protocol
```

---

### 25. Enums & Data Classes

```python
# Enums — named constants
from enum import Enum, auto

class Color(Enum):
    RED   = auto()
    GREEN = auto()
    BLUE  = auto()

class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST  = "E"
    WEST  = "W"

print(Color.RED)            # Color.RED
print(Color.RED.value)      # 1
print(Color.RED.name)       # RED
print(list(Color))          # [Color.RED, Color.GREEN, Color.BLUE]

for color in Color:
    print(color)

# Data classes — reduce boilerplate for data-holding classes
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
print(p1)          # Point(x=1.0, y=2.0)
print(p1 == p2)    # True (auto __eq__)

@dataclass
class Student:
    name: str
    age: int
    grades: list[float] = field(default_factory=list)

    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

s = Student("Alice", 20, [95.0, 87.5, 92.0])
print(s.average())   # 91.5

# Frozen (immutable)
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

red = Color(255, 0, 0)
# red.r = 128   # raises FrozenInstanceError
```

---

### 26. Concurrency

```python
# Threading — good for I/O-bound tasks (network, disk)
import threading
import time

def download(url):
    print(f"Downloading {url}...")
    time.sleep(2)
    print(f"Done: {url}")

threads = [threading.Thread(target=download, args=(f"url_{i}",)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

# Thread-safe counter with Lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1

# Multiprocessing — good for CPU-bound tasks (math, image processing)
from multiprocessing import Pool

def square(x):
    return x ** 2

with Pool(4) as pool:
    results = pool.map(square, range(10))
print(results)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# concurrent.futures — higher-level interface
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(download, f"url_{i}") for i in range(5)]
    results = [f.result() for f in futures]
```

**Files:** `my_modules/external_modules/04_threading.py`, `my_modules/comprehensive_examples/07_concurrency_threading_multiprocessing.py`

---

### 27. Async / Await

Async is for I/O-bound tasks where you can do other things while waiting.

```python
import asyncio

async def fetch_data(url):
    print(f"Fetching {url}...")
    await asyncio.sleep(1)          # simulate network delay
    return f"Data from {url}"

# Run a single coroutine
async def main():
    result = await fetch_data("https://api.example.com")
    print(result)

asyncio.run(main())

# Run multiple concurrently (~1 second, not 3)
async def main():
    urls = ["url_1", "url_2", "url_3"]
    results = await asyncio.gather(*[fetch_data(u) for u in urls])
    for r in results:
        print(r)

asyncio.run(main())

# Async context manager
class AsyncDB:
    async def __aenter__(self):
        print("Connecting...")
        return self

    async def __aexit__(self, *args):
        print("Disconnecting...")

async def main():
    async with AsyncDB() as db:
        print("Using DB")

# Async generator
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

A metaclass controls how a class itself is created. Use sparingly.

```python
# type() is the default metaclass — all classes are instances of type
MyClass = type("MyClass", (object,), {"greet": lambda self: "Hello!"})
print(MyClass().greet())   # Hello!

# Custom metaclass — Singleton pattern
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "connected"

db1 = Database()
db2 = Database()
print(db1 is db2)   # True

# __init_subclass__ — simpler alternative for plugin registration
class PluginBase:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase.plugins.append(cls)

class PluginA(PluginBase): pass
class PluginB(PluginBase): pass

print(PluginBase.plugins)   # [<class 'PluginA'>, <class 'PluginB'>]
```

---

### 29. Testing

```python
# unittest — standard library
import unittest

def add(a, b):    return a + b
def divide(a, b):
    if b == 0: raise ValueError("Cannot divide by zero")
    return a / b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
```

```python
# pytest (pip install pytest) — simpler, more powerful
# Run: pytest test_file.py -v

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)

# Parametrize — run same test with different inputs
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected

# Fixtures — setup/teardown
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
```

---

### 30. Packaging & Virtual Environments

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows

# Install packages
pip install requests numpy pandas

# Save / restore dependencies
pip freeze > requirements.txt
pip install -r requirements.txt

deactivate
```

```
# Package structure
my_package/
├── my_package/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── tests/
│   └── test_core.py
├── README.md
├── requirements.txt
└── pyproject.toml
```

```toml
# pyproject.toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.backends.legacy:build"

[project]
name = "my_package"
version = "0.1.0"
dependencies = ["requests>=2.28"]
```

```bash
pip install build twine
python -m build
twine upload dist/*
```

**File:** `my_modules/comprehensive_examples/05_python_packaging_tutorial.py`

---

## Famous Libraries

---

### 31. Standard Library

Python ships with powerful built-in modules — no install needed.

```python
# os — filesystem
import os
print(os.getcwd())
os.makedirs("new_dir", exist_ok=True)
os.path.exists("file.txt")
os.path.join("folder", "file.txt")

# pathlib — modern, object-oriented paths (preferred over os.path)
from pathlib import Path
p = Path("my_folder/data.txt")
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("hello")
print(p.read_text())
for f in Path(".").glob("*.py"):
    print(f)

# sys
import sys
print(sys.version)
print(sys.argv)     # command-line arguments
sys.exit(0)

# math
import math
math.sqrt(16), math.ceil(4.2), math.floor(4.8)
math.log(100, 10), math.pi, math.factorial(5)

# datetime
from datetime import datetime, timedelta, date
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
tomorrow = now + timedelta(days=1)

# collections
from collections import Counter, defaultdict, deque, namedtuple

words = ["apple", "banana", "apple", "cherry", "apple"]
print(Counter(words).most_common(2))   # [('apple', 3), ('banana', 1)]

dd = defaultdict(list)
dd["fruits"].append("apple")           # no KeyError for missing keys

q = deque([1, 2, 3])
q.appendleft(0)     # [0, 1, 2, 3]
q.popleft()         # 0

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)

# itertools
from itertools import chain, combinations, permutations, product, groupby, islice

list(chain([1, 2], [3, 4]))             # [1, 2, 3, 4]
list(combinations([1,2,3], 2))          # [(1,2), (1,3), (2,3)]
list(permutations([1,2,3], 2))
list(product([0,1], repeat=3))          # all 3-bit combos

# functools
from functools import partial, lru_cache, reduce

@lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

power_of_2 = partial(pow, 2)
print(power_of_2(10))   # 1024

# random
import random
random.random()                         # 0.0 to 1.0
random.randint(1, 100)
random.choice(["a","b","c"])
random.shuffle([1, 2, 3, 4, 5])

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logging.info("General info")
logging.warning("Something unexpected")
logging.error("Error occurred")
```

**Files:** `my_modules/files_handling/06_os.py`, `my_modules/external_modules/03_regular_expressions.py`

---

### 32. Data Science — NumPy, Pandas, Matplotlib

```bash
pip install numpy pandas matplotlib seaborn
```

#### NumPy — fast numerical arrays

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)    # (5,)
print(b.shape)    # (2, 3)

# Array creation
np.zeros((3, 3)), np.ones((2, 4))
np.arange(0, 10, 0.5)
np.linspace(0, 1, 5)   # 5 evenly spaced values

# Element-wise operations
print(a * 2)          # [2, 4, 6, 8, 10]
print(np.sqrt(a))

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
A @ B                  # matrix multiply
np.linalg.inv(A)       # matrix inverse

# Indexing
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr[0, :]              # first row
arr[:, 1]              # second column
arr[arr > 4]           # boolean indexing

# Statistics
np.mean(a), np.std(a), np.sum(a), np.min(a), np.max(a)
```

#### Pandas — data manipulation

```python
import pandas as pd

data = {
    "name":  ["Alice", "Bob", "Charlie", "Diana"],
    "age":   [25, 30, 35, 28],
    "city":  ["NYC", "LA", "Chicago", "NYC"],
    "score": [92.5, 85.0, 78.3, 95.1],
}
df = pd.DataFrame(data)

print(df.head())
print(df.info())
print(df.describe())

# Selecting
df["name"]
df[["name", "age"]]
df.iloc[0]                       # by position
df.loc[df["age"] > 28]           # filter rows

# Modifying
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else "B")

# Groupby
df.groupby("city")["score"].mean()

# Sorting
df.sort_values("score", ascending=False)

# Read/write
df.to_csv("students.csv", index=False)
df2 = pd.read_csv("students.csv")

# Missing data
df.dropna()
df.fillna(0)
df.isna().sum()

# Merge
df1 = pd.DataFrame({"id": [1,2,3], "name": ["A","B","C"]})
df2 = pd.DataFrame({"id": [1,2,4], "score": [90,85,78]})
pd.merge(df1, df2, on="id", how="inner")
```

#### Matplotlib & Seaborn — visualization

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="o", label="linear")
plt.title("Line Plot")
plt.xlabel("x"); plt.ylabel("y")
plt.legend(); plt.show()

# Bar chart
plt.bar(["A","B","C","D"], [23, 45, 12, 67], color="steelblue")
plt.show()

# Histogram
import numpy as np
plt.hist(np.random.normal(50, 10, 1000), bins=30)
plt.show()

# Subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x, y); axes[1].bar(["A","B"], [1,2])
plt.tight_layout(); plt.show()

# Seaborn (statistical visualization)
df = sns.load_dataset("tips")
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")
sns.boxplot(data=df, x="day", y="total_bill")
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
```

**Files:** `my_modules/comprehensive_examples/08_pandas_data_analysis.py`, `09_vectors_numerical_computing.py`

---

### 33. Web Development — Flask, FastAPI

#### Flask — lightweight web framework

```bash
pip install flask
```

```python
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"

users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
```

#### FastAPI — modern, async, auto-documented

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
# Auto docs: http://127.0.0.1:8000/docs
```

> **Django** — full-featured framework with admin, ORM, auth built in. Best for larger apps. `pip install django`

**File:** `my_modules/flask_basic/main.py`

---

### 34. HTTP & APIs — Requests, HTTPX

```bash
pip install requests httpx
```

```python
import requests

# GET
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)    # 200
data = response.json()

# GET with params
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

# POST
payload = {"title": "New Post", "body": "Content", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

# Headers and auth
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get("https://api.example.com/data", headers=headers)

# Error handling
try:
    r = requests.get("https://api.example.com", timeout=5)
    r.raise_for_status()    # raises HTTPError for 4xx/5xx
    data = r.json()
except requests.Timeout:
    print("Timed out")
except requests.HTTPError as e:
    print(f"HTTP error: {e}")

# Session — reuse connection + shared headers/cookies
with requests.Session() as s:
    s.headers.update({"Authorization": "Bearer TOKEN"})
    r1 = s.get("https://api.example.com/a")
    r2 = s.get("https://api.example.com/b")
```

```python
# httpx — modern requests with async support
import httpx, asyncio

# Sync (same API as requests)
response = httpx.get("https://httpbin.org/get")

# Async
async def fetch():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get")
        return r.json()

asyncio.run(fetch())
```

**File:** `my_modules/external_modules/02_requests_modules.py`

---

### 35. Web Scraping — BeautifulSoup, Selenium

```bash
pip install beautifulsoup4 requests
pip install selenium
```

```python
# BeautifulSoup — parse static HTML
import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title").text
books = soup.find_all("article", class_="product_pod")
for book in books[:5]:
    name  = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text
    print(f"{name}: {price}")

# CSS selectors
links = [a["href"] for a in soup.select("a[href]")[:5]]

# Selenium — JavaScript-rendered pages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

element = driver.find_element(By.ID, "search")
element.send_keys("python")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

result = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "result"))
)
print(result.text)
driver.quit()
```

---

### 36. Databases — SQLAlchemy, SQLite

```bash
pip install sqlalchemy
```

```python
# sqlite3 — built-in
import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
conn.commit()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)
conn.close()

# SQLAlchemy — ORM
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id    = Column(Integer, primary_key=True)
    name  = Column(String, nullable=False)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"

engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(User(name="Alice", email="alice@example.com"))
    session.commit()
    users = session.query(User).all()
    print(users)
```

---

### 37. AI & Machine Learning

```bash
pip install scikit-learn
pip install torch torchvision    # or: pip install tensorflow
pip install openai anthropic
```

#### Scikit-learn — classical machine learning

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
print(classification_report(y_test, predictions))

# Other models follow the same fit/predict API
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
```

#### LLM APIs

```python
# OpenAI
from openai import OpenAI
client = OpenAI(api_key="YOUR_KEY")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",   "content": "Explain list comprehensions."}
    ]
)
print(response.choices[0].message.content)

# Anthropic Claude
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

#### argparse — command-line arguments (standard library)

```python
import argparse

parser = argparse.ArgumentParser(description="Process files")
parser.add_argument("filename",                         help="Input file path")
parser.add_argument("-o", "--output", default="out.txt",help="Output file")
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-n", "--count",  type=int, default=10)

args = parser.parse_args()
print(args.filename, args.output, args.verbose, args.count)
# Run: python script.py input.txt -o result.txt -v -n 20
```

#### click — elegant CLI framework

```bash
pip install click
```

```python
import click

@click.command()
@click.argument("name")
@click.option("--count", default=1, help="Number of greetings")
@click.option("--shout", is_flag=True, help="Uppercase output")
def hello(name, count, shout):
    for _ in range(count):
        msg = f"Hello, {name}!"
        click.echo(msg.upper() if shout else msg)

if __name__ == "__main__":
    hello()
# Run: python script.py Alice --count 3 --shout
```

#### schedule — task scheduling

```bash
pip install schedule
```

```python
import schedule, time

def send_reminder():
    print("Remember to drink water!")

schedule.every(30).minutes.do(send_reminder)
schedule.every().day.at("09:00").do(send_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)
```

#### shutil — file operations

```python
import shutil

shutil.copy("source.txt", "destination.txt")
shutil.copy2("source.txt", "backup/")        # preserve metadata
shutil.move("old.txt", "new.txt")
shutil.rmtree("old_folder")
shutil.make_archive("backup", "zip", "folder/")
```

**Files:** `my_modules/files_handling/07_shutil.py`, `08_argparse.py`

---

### 39. Useful Utilities

#### pydantic — data validation

```bash
pip install pydantic
```

```python
from pydantic import BaseModel, field_validator
from typing import Optional

class User(BaseModel):
    name:  str
    age:   int
    email: str
    score: Optional[float] = None

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Age must be positive")
        return v

user = User(name="Alice", age=30, email="alice@example.com")
print(user.model_dump())   # convert to dict
```

#### Pillow — image processing

```bash
pip install Pillow
```

```python
from PIL import Image, ImageFilter, ImageDraw

img = Image.open("photo.jpg")
print(img.size, img.mode)   # (1920, 1080) RGB

img.resize((800, 600)).save("resized.jpg")
img.filter(ImageFilter.BLUR).save("blurred.jpg")
img.save("photo.png")       # convert format

draw = ImageDraw.Draw(img)
draw.rectangle([10, 10, 100, 100], outline="red", width=3)
draw.text((50, 50), "Hello!", fill="white")
```

#### rich — beautiful terminal output

```bash
pip install rich
```

```python
from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()
console.print("[bold green]Success![/bold green]")
console.print("[red]Error:[/red] Something went wrong")

# Pretty table
table = Table(title="Users")
table.add_column("Name", style="cyan")
table.add_column("Age",  style="magenta")
table.add_row("Alice", "30")
table.add_row("Bob",   "25")
console.print(table)

# Progress bar
for item in track(range(100), description="Processing..."):
    pass
```

#### python-dotenv — environment variables

```bash
pip install python-dotenv
```

```python
# .env file:
# API_KEY=abc123
# DATABASE_URL=sqlite:///app.db

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
db_url  = os.getenv("DATABASE_URL")
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
