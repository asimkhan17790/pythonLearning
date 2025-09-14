# Python Learning Guide 🐍

Welcome to the most comprehensive Python learning playground! This repository is designed to take you from a complete beginner to an advanced Python developer. Whether you're just starting your programming journey or looking to master advanced Python concepts, this guide has everything you need.

## 🎯 What You'll Learn

This repository covers **everything** from basic syntax to advanced topics like metaclasses, async programming, and web development. Each concept includes:
- **Clear explanations** with real-world context
- **Hands-on examples** you can run immediately
- **Progressive difficulty** that builds on previous concepts
- **Best practices** and common pitfalls to avoid

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
11. [Classes and Objects](#11-classes-and-objects) - Object-oriented programming
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
26. [Async/Await](#26-asyncawait) - Asynchronous programming
27. [Data Classes](#27-data-classes) - Simplified class creation
28. [Testing](#28-testing-unittest) - Writing reliable code
29. [Packaging & Virtual Environments](#29-packaging--virtual-environments) - Project management

---

## 1. Variables and Data Types

Variables are like labeled boxes that store data. Python has several built-in data types:

```python
# String - Text data
name = "Maverick"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

# Integer - Whole numbers
age = 25
year = 2024
negative_number = -10

# Float - Decimal numbers
height = 5.9
pi = 3.14159
temperature = -2.5

# Boolean - True/False values
is_student = True
is_employed = False
can_vote = age >= 18  # This evaluates to True

# None - Represents nothing/empty
data = None
```

**💡 Pro Tips:**
- Python is dynamically typed - you don't need to declare variable types
- Variable names should be descriptive: use `student_count` instead of `sc`
- Use snake_case for variable names (words separated by underscores)

**🔍 Try This:**
```python
# Check variable types
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

## 2. Basic Input/Output

Learn to communicate with users through your programs:

```python
# Output - Displaying information
print("Hello, World!")
print("My name is", name, "and I am", age, "years old")

# Different ways to format output
print(f"Hello, {name}! You are {age} years old.")  # f-strings (recommended)
print("Hello, {}! You are {} years old.".format(name, age))  # .format()
print("Hello, %s! You are %d years old." % (name, age))  # % formatting

# Input - Getting user data
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))  # Convert string to integer
user_height = float(input("Enter your height: "))  # Convert to float

print(f"Welcome, {user_name}! You are {user_age} years old and {user_height} feet tall.")
```

**💡 Pro Tips:**
- `input()` always returns a string - convert with `int()`, `float()`, etc.
- f-strings (f"text {variable}") are the most readable formatting method
- Use descriptive prompts: "Enter your age: " instead of just "Age: "

**⚠️ Common Mistake:**
```python
# This will cause an error!
age = input("Enter your age: ")  # This is a string!
next_year = age + 1  # Can't add number to string

# Correct way:
age = int(input("Enter your age: "))  # Convert to integer
next_year = age + 1  # Now this works!
```

## 3. Operators

Operators are symbols that perform operations on variables and values:

```python
a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.3333...
print("Floor Division:", a // b) # 3 (rounds down)
print("Modulus:", a % b)         # 1 (remainder)
print("Exponent:", a ** b)       # 1000 (10 to the power of 3)

# Comparison Operators
print("Equal:", a == b)          # False
print("Not equal:", a != b)      # True
print("Greater than:", a > b)    # True
print("Less than:", a < b)       # False
print("Greater or equal:", a >= b) # True
print("Less or equal:", a <= b)   # False

# Logical Operators
x = True
y = False
print("AND:", x and y)           # False (both must be True)
print("OR:", x or y)             # True (at least one must be True)
print("NOT:", not x)             # False (opposite of x)

# Practical example
age = 20
has_license = True
can_drive = age >= 18 and has_license
print("Can drive:", can_drive)   # True
```

**💡 Pro Tips:**
- Use `//` for integer division when you don't want decimals
- `%` (modulus) is great for checking if numbers are even: `number % 2 == 0`
- Combine logical operators for complex conditions

**🔍 Try This:**
```python
# Check if a number is even or odd
number = 15
is_even = number % 2 == 0
print(f"{number} is {'even' if is_even else 'odd'}")
```

## 4. Conditional Statements

Make decisions in your code based on different conditions:

```python
age = 20

# Basic if-else
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Multiple conditions with elif
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Complex conditions
temperature = 75
is_sunny = True

if temperature > 70 and is_sunny:
    print("Perfect weather for a picnic!")
elif temperature > 70 and not is_sunny:
    print("Warm but cloudy")
elif temperature <= 32:
    print("It's freezing!")
else:
    print("Cool weather")

# Ternary operator (shorthand if-else)
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")
```

**💡 Pro Tips:**
- Python uses indentation (4 spaces) to group code blocks
- Use `elif` instead of multiple `if` statements for efficiency
- Ternary operator is great for simple assignments

**🔍 Real-World Example:**
```python
# Grade calculator
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
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

## 🚀 Next Steps

### 1. **Explore the Modules**
Navigate through the `my_modules/` directory:
- Start with `basic_concepts/` for foundations
- Move to `advanced_concepts/` for deeper topics
- Check out `flask_basic/` for web development
- Explore `ai/` for machine learning basics

### 2. **Build Your Own Projects**
- **Portfolio Website** (Flask + HTML/CSS)
- **Data Analysis Tool** (pandas + matplotlib)
- **API Client** (requests + JSON handling)
- **Game Development** (pygame or tkinter)
- **Automation Scripts** (file handling + scheduling)

### 3. **Join the Community**
- Share your projects on GitHub
- Contribute to open-source Python projects
- Join Python Discord servers or forums
- Attend local Python meetups

### 4. **Advanced Learning Resources**
- **Books**: "Automate the Boring Stuff", "Python Tricks", "Effective Python"
- **Online**: Real Python, Python.org tutorials, freeCodeCamp
- **Practice**: LeetCode, HackerRank, Codewars
- **Specializations**: Web development (Django/Flask), Data Science (pandas/numpy), AI/ML (tensorflow/pytorch)

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
