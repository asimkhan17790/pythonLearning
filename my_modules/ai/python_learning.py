
# This file contains all basic syntax with examples for Python learning.
# It covers all fundamental concepts and constructs of Python programming language.
# Each section includes code snippets and explanations to help beginners understand and practice Python coding.
# The file is organized into sections based on different topics, making it easy to navigate and find specific information.
# This file serves as a comprehensive guide for anyone looking to learn Python from scratch or enhance their existing skills.
# Should cover all topics extensively
# Author: Maverick Khan

# -----------------------------
# 1. Variables and Data Types
# -----------------------------
# Variables store data. Python is dynamically typed.
from typing import Dict, Tuple, Optional
import sqlite3
import unittest
from dataclasses import dataclass
import asyncio
import multiprocessing
import time
import threading
from functools import reduce
name = "Maverick"
age = 25
height = 5.9
is_student = True

# -----------------------------
# 2. Basic Input/Output
# -----------------------------
# Use print() to display output, input() to get user input.
print("Hello, World!")
# user_name = input("Enter your name: ")
# print("Welcome,", user_name)

# -----------------------------
# 3. Operators
# -----------------------------
# Arithmetic, comparison, logical, assignment, etc.
a = 10
b = 3
print("Addition:", a + b)
print("Division:", a / b)
print("Exponent:", a ** b)
print("Is a > b?", a > b)
print("Logical AND:", a > 5 and b < 5)

# -----------------------------
# 4. Conditional Statements
# -----------------------------
# if, elif, else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# -----------------------------
# 5. Loops
# -----------------------------
# for loop, while loop
for i in range(5):
    print("For loop iteration:", i)

count = 0
while count < 3:
    print("While loop count:", count)
    count += 1

# -----------------------------
# 6. Functions
# -----------------------------
# Define and call functions


def greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")


greet("Maverick")

# -----------------------------
# 7. Data Structures
# -----------------------------

# Lists, Tuples, Sets, Dictionaries
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
my_dict = {"name": "Maverick", "age": 25}

# List operations
my_list.append(4)  # Add an element
my_list.remove(2)  # Remove an element
my_list.insert(1, 10)  # Insert at index
my_list.pop()  # Remove last element
print("List after operations:", my_list)
print("List slicing:", my_list[1:3])  # Slicing
print("List length:", len(my_list))

# Tuple operations (tuples are immutable)
print("Tuple element:", my_tuple[0])  # Access element
print("Tuple slicing:", my_tuple[1:])
print("Tuple length:", len(my_tuple))

# Set operations
my_set.add(10)  # Add element
my_set.remove(7)  # Remove element
my_set2 = {8, 9, 11}
print("Set union:", my_set | my_set2)  # Union
print("Set intersection:", my_set & my_set2)  # Intersection
print("Set difference:", my_set - my_set2)  # Difference
print("Set after operations:", my_set)

# Dictionary operations
my_dict["city"] = "Delhi"  # Add key-value pair
del my_dict["age"]  # Remove key
print("Dictionary keys:", list(my_dict.keys()))
print("Dictionary values:", list(my_dict.values()))
print("Dictionary items:", list(my_dict.items()))
print("Dictionary after operations:", my_dict)


# -----------------------------
# 8. List Comprehensions
# -----------------------------
# List comprehensions provide a concise way to create lists.
# Syntax: [expression for item in iterable if condition]
# Example: Get all even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# You can use list comprehensions for transformations:
# Example: Square each number in a list
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# You can also use nested comprehensions:
# Example: Flatten a 2D list
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# List comprehensions are more readable and efficient than using loops for simple list creation and transformation tasks.

# -----------------------------
# 9. String Manipulation
# -----------------------------

text = "Python is fun!"
# Convert to uppercase
print("Uppercase:", text.upper())
# Convert to lowercase
print("Lowercase:", text.lower())
# Replace substring
print("Replace:", text.replace("fun", "awesome"))
# Find substring
print("Find 'is':", text.find("is"))
# Count occurrences
print("Count 'n':", text.count("n"))
# Split into list
print("Split:", text.split())
# Join list into string
words = ["Python", "is", "cool"]
print("Join:", " ".join(words))
# Strip whitespace
text2 = "   padded text   "
print("Strip:", text2.strip())
# Startswith/Endswith
print("Startswith 'Python':", text.startswith("Python"))
print("Endswith '!':", text.endswith("!"))
# Check if all characters are digits
num_str = "12345"
print("Is digit:", num_str.isdigit())
# Check if all characters are alphabetic
alpha_str = "Hello"
print("Is alpha:", alpha_str.isalpha())
# String formatting
name = "Maverick"
print(f"Hello, {name}!")

# -----------------------------
# 10. Exception Handling
# -----------------------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# -----------------------------
# 11. Classes and Objects
# -----------------------------


class Person:
    """Represents a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


p = Person("Maverick", 25)
p.introduce()

# -----------------------------
# 12. File Handling
# -----------------------------
# Reading and writing files
# with open("example.txt", "w") as f:
#     f.write("Hello, file!")
# with open("example.txt", "r") as f:
#     print(f.read())

# -----------------------------
# 13. Modules and Imports
# -----------------------------
# import math
# print(math.sqrt(16))


# -----------------------------
# 14. Useful Built-in Functions
# -----------------------------
nums = [5, 2, 9]
# max() returns the largest value
print("Max:", max(nums))
# min() returns the smallest value
print("Min:", min(nums))
# sum() returns the sum of all values
print("Sum:", sum(nums))
# len() returns the number of items
print("Length:", len(nums))
# sorted() returns a sorted list
print("Sorted:", sorted(nums))
# reversed() returns an iterator for reversed list
print("Reversed:", list(reversed(nums)))
# enumerate() returns pairs of (index, value)
print("Enumerate:", list(enumerate(nums)))
# zip() combines multiple lists into tuples
print("Zip:", list(zip(nums, ['a', 'b', 'c'])))
# any() returns True if any element is True
print("Any:", any(x > 8 for x in nums))
# all() returns True if all elements are True
print("All:", all(x > 0 for x in nums))


# -----------------------------
# 15. Decorators
# -----------------------------
# Functions that modify other functions
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

# -----------------------------
# 16. Generators
# -----------------------------
# Functions that yield values one at a time


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


for num in count_up_to(3):
    print("Generator value:", num)

# -----------------------------
# 17. Lambda Functions
# -----------------------------
# Anonymous functions


def add(x, y): return x + y


print("Lambda add:", add(2, 3))

# -----------------------------
# 18. Map, Filter, Reduce
# -----------------------------
nums = [1, 2, 3, 4]
print("Map (squared):", list(map(lambda x: x**2, nums)))
print("Filter (even):", list(filter(lambda x: x % 2 == 0, nums)))
print("Reduce (sum):", reduce(lambda x, y: x + y, nums))


# -----------------------------
# 19. Context Managers
# -----------------------------
# Context managers are used to properly manage resources (like files, network connections, locks, etc.)
# They ensure setup and cleanup actions are performed automatically, even if errors occur.
# The most common context manager is 'with open(...) as ...' for file handling.
# When you use 'with', Python automatically closes the file when the block ends.
# This prevents resource leaks and makes code safer and cleaner.

# Example: Writing to a file using a context manager
with open("example.txt", "w") as f:
    f.write("Context manager example.")
# Here, 'f' is the file object. The file is opened for writing, and after the block, it is closed automatically.


# Example: Using a context manager for a database connection
with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    conn.commit()
# Here, the database connection 'conn' is automatically closed after the block, even if an error occurs.

# -----------------------------
# 20. Inheritance & Polymorphism
# -----------------------------


class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


pet = Dog()
pet.speak()

# -----------------------------
# 21. Exception Chaining & Custom Exceptions
# -----------------------------


class MyError(Exception):
    pass


try:
    raise MyError("Custom error!")
except MyError as e:
    print("Caught exception:", e)


# -----------------------------
# 22. Type Hinting
# -----------------------------
# Type hinting allows you to specify the expected data types of function arguments and return values.
# This helps with code readability, editor autocompletion, and static analysis tools (like mypy).
# Type hints do not enforce types at runtime, but can catch bugs earlier during development.

def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns an integer."""
    return a + b


print("Type hinting:", add_numbers(2, 5))

# You can use type hints for other types:


def greet_user(name: str) -> None:
    print(f"Hello, {name}!")


greet_user("Maverick")


def get_names() -> list[str]:
    return ["Alice", "Bob", "Charlie"]


print("Names:", get_names())

# You can also use type hints for classes and complex types:


def get_user_info(user_id: int) -> Optional[Dict[str, Tuple[str, int]]]:
    # Example: returns None or a dictionary with user info
    if user_id == 1:
        return {"user": ("Maverick", 25)}
    return None


print("User info:", get_user_info(1))


# -----------------------------
# 23. Concurrency (Threading & Multiprocessing)
# -----------------------------
# Threading allows you to run multiple operations concurrently in the same process.
# Multiprocessing allows you to run code in separate processes, taking advantage of multiple CPU cores.

# Threading operations
def worker():
    print("Thread starting")
    time.sleep(1)
    print("Thread finished")


# Create a thread
t = threading.Thread(target=worker)
# Start the thread
t.start()
# Wait for the thread to finish
t.join()

# You can create multiple threads
threads = []
for i in range(3):
    th = threading.Thread(target=lambda: print(f"Thread {i} running"))
    threads.append(th)
    th.start()
for th in threads:
    th.join()

# Threading operations:
# - threading.Thread: create a thread
# - start(): start the thread
# - join(): wait for thread to finish
# - is_alive(): check if thread is running
print("Is thread alive?", t.is_alive())
# - threading.current_thread(): get current thread object
print("Current thread:", threading.current_thread().name)
# - threading.active_count(): number of active threads
print("Active thread count:", threading.active_count())
# - threading.Lock(): create a lock for synchronization
lock = threading.Lock()
with lock:
    print("Lock acquired in thread")

# Multiprocessing operations


def process_worker():
    print("Process running")


# Create a process
p = multiprocessing.Process(target=process_worker)
# Start the process
p.start()
# Wait for the process to finish
p.join()

# You can create multiple processes
processes = []
for i in range(2):
    proc = multiprocessing.Process(
        target=lambda: print(f"Process {i} running"))
    processes.append(proc)
    proc.start()
for proc in processes:
    proc.join()

# Multiprocessing operations:
# - multiprocessing.Process: create a process
# - start(): start the process
# - join(): wait for process to finish
# - is_alive(): check if process is running
print("Is process alive?", p.is_alive())
# - multiprocessing.current_process(): get current process object
print("Current process:", multiprocessing.current_process().name)
# - multiprocessing.active_children(): list of active child processes
print("Active child processes:", multiprocessing.active_children())
# - multiprocessing.Queue(): create a queue for inter-process communication
queue = multiprocessing.Queue()
queue.put("Hello from main process")
print("Queue get:", queue.get())
# - multiprocessing.Pool: create a pool of worker processes for parallel tasks


def square(x):
    return x * x


with multiprocessing.Pool(2) as pool:
    print("Pool map:", pool.map(square, [1, 2, 3]))


# -----------------------------
# 24. Metaclasses
# -----------------------------
# Metaclasses are 'classes of classes': they define how classes themselves are constructed.
# In Python, classes are objects, and metaclasses allow you to customize class creation, modify attributes, or enforce patterns.
# The default metaclass is 'type'. You can create your own by inheriting from 'type'.
# Use cases include: automatic attribute validation, singleton pattern, logging, or API enforcement.
#
# Example: A metaclass that prints when a class is created
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=Meta):
    pass
# When MyClass is defined, 'Meta.__new__' runs and prints a message.

# -----------------------------
# 25. Property Decorators
# -----------------------------


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height


r = Rectangle(3, 4)
print("Rectangle area:", r.area)


# -----------------------------
# 26. Async/Await
# -----------------------------
# Async/await is used for asynchronous programming in Python, allowing you to write code that performs non-blocking operations (like I/O, network calls, etc.).
# 'async def' defines a coroutine function. 'await' pauses execution until the awaited coroutine completes.
# The event loop schedules and runs coroutines.

async def async_hello():
    await asyncio.sleep(1)  # Simulate async I/O
    print("Hello from async!")

# To run a coroutine, use asyncio.run()
# asyncio.run(async_hello())  # Uncomment to run

# Example: Running multiple coroutines concurrently


async def greet(name):
    await asyncio.sleep(0.5)
    print(f"Hello, {name}!")


async def main():
    await asyncio.gather(
        async_hello(),
        greet("Alice"),
        greet("Bob")
    )

# asyncio.run(main())  # Uncomment to run all coroutines together

# Async/await is useful for tasks like web scraping, network requests, or handling many simultaneous connections efficiently.

# -----------------------------
# 27. Data Classes
# -----------------------------


@dataclass
class Point:
    x: int
    y: int


pt = Point(2, 3)
print("Data class Point:", pt)

# -----------------------------
# 28. Testing (unittest)
# -----------------------------


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

# if __name__ == "__main__":
#     unittest.main()

# -----------------------------
# 29. Packaging & Virtual Environments
# -----------------------------
# Use 'pip' to install packages: pip install requests
# Create virtual environment: python -m venv env
# Activate: source env/bin/activate (macOS/Linux) or .\\env\\Scripts\\activate (Windows)
# Requirements file: pip freeze > requirements.txt

# End of Complete Python Guide
