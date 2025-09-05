# Python Learning Guide

This repository is a comprehensive Python learning playground. It covers all fundamental and advanced concepts of Python programming, with code examples and explanations for each topic. Use this guide to learn Python from scratch or to deepen your understanding of advanced features.

## Table of Contents

1. Variables and Data Types
2. Basic Input/Output
3. Operators
4. Conditional Statements
5. Loops
6. Functions
7. Data Structures
8. List Comprehensions
9. String Manipulation
10. Exception Handling
11. Classes and Objects
12. File Handling
13. Modules and Imports
14. Useful Built-in Functions
15. Decorators
16. Generators
17. Lambda Functions
18. Map, Filter, Reduce
19. Context Managers
20. Inheritance & Polymorphism
21. Exception Chaining & Custom Exceptions
22. Type Hinting
23. Concurrency (Threading & Multiprocessing)
24. Metaclasses
25. Property Decorators
26. Async/Await
27. Data Classes
28. Testing (unittest)
29. Packaging & Virtual Environments

---

## 1. Variables and Data Types

```python
name = "Maverick"
age = 25
height = 5.9
is_student = True
```

## 2. Basic Input/Output

```python
print("Hello, World!")
# user_name = input("Enter your name: ")
# print("Welcome,", user_name)
```

## 3. Operators

```python
a = 10
b = 3
print("Addition:", a + b)
print("Division:", a / b)
print("Exponent:", a ** b)
print("Is a > b?", a > b)
print("Logical AND:", a > 5 and b < 5)
```

## 4. Conditional Statements

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## 5. Loops

```python
for i in range(5):
    print("For loop iteration:", i)

count = 0
while count < 3:
    print("While loop count:", count)
    count += 1
```

## 6. Functions

```python
def greet(name):
    print(f"Hello, {name}!")
greet("Maverick")
```

## 7. Data Structures

```python
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_set = {7, 8, 9}
my_dict = {"name": "Maverick", "age": 25}
```

Common operations:

```python
my_list.append(4)
my_list.remove(2)
my_list.insert(1, 10)
my_list.pop()
print(my_list[1:3])
print(len(my_list))
print(my_tuple[0])
print(my_set | {8, 9, 11})
my_dict["city"] = "Delhi"
del my_dict["age"]
print(list(my_dict.keys()))
```

## 8. List Comprehensions

```python
evens = [x for x in range(10) if x % 2 == 0]
squares = [x**2 for x in range(5)]
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
```

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

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

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

```python
nums = [5, 2, 9]
print(max(nums))
print(min(nums))
print(sum(nums))
print(len(nums))
print(sorted(nums))
print(list(reversed(nums)))
print(list(enumerate(nums)))
print(list(zip(nums, ['a', 'b', 'c'])))
print(any(x > 8 for x in nums))
print(all(x > 0 for x in nums))
```

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

---

For more details and advanced examples, see the code in `my_modules/ai/python_learning.py`.
