"""
Comprehensive Library Import Tutorial
====================================

This module demonstrates all the different ways to import libraries in Python:
- Built-in modules
- Third-party packages
- Local modules and packages
- Different import syntaxes
- Import best practices
- Dynamic imports
- Package structure and __init__.py
"""

import os
import sys
import time
import datetime
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import json
import math
from math import sqrt, pi, sin, cos
import random
from random import choice, randint, shuffle
import re
from pathlib import Path
import importlib
import inspect

# Import aliasing
import numpy as np  # Standard alias (if available)
import pandas as pd  # Standard alias (if available)
import matplotlib.pyplot as plt  # Standard alias (if available)

# Try/except imports for optional dependencies
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("requests library not available")

try:
    import sqlite3
    SQLITE_AVAILABLE = True
except ImportError:
    SQLITE_AVAILABLE = False

# Conditional imports based on Python version
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol, TypedDict
    TYPING_EXTENSIONS_NEEDED = False
else:
    try:
        from typing_extensions import Protocol, TypedDict
        TYPING_EXTENSIONS_NEEDED = True
    except ImportError:
        Protocol = None
        TypedDict = None
        TYPING_EXTENSIONS_NEEDED = True


def demonstrate_builtin_imports():
    """Demonstrate importing and using built-in modules"""
    print("=" * 60)
    print("BUILT-IN MODULE IMPORTS")
    print("=" * 60)

    print("\n1. OS Module (Operating System Interface):")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Environment PATH: {os.environ.get('PATH', 'Not found')[:100]}...")
    print(f"Platform: {os.name}")

    print("\n2. Time and DateTime Modules:")
    # Using time module
    current_time = time.time()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Current timestamp: {current_time}")
    print(f"Formatted time: {formatted_time}")

    # Using datetime (imported with from)
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    print(f"Now: {now}")
    print(f"Tomorrow: {tomorrow}")

    print("\n3. Math Module:")
    # Using full module import
    print(f"math.pi: {math.pi}")
    print(f"math.sqrt(16): {math.sqrt(16)}")

    # Using imported functions directly
    print(f"sqrt(25): {sqrt(25)}")
    print(f"sin(pi/2): {sin(pi/2)}")

    print("\n4. Random Module:")
    numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {numbers}")
    shuffle(numbers)  # Imported function
    print(f"Shuffled list: {numbers}")
    print(f"Random choice: {choice(['apple', 'banana', 'cherry'])}")
    print(f"Random integer (1-10): {randint(1, 10)}")

    print("\n5. JSON Module:")
    data = {"name": "Alice", "age": 30, "hobbies": ["reading", "coding"]}
    json_string = json.dumps(data, indent=2)
    print(f"JSON string:\n{json_string}")

    parsed_data = json.loads(json_string)
    print(f"Parsed back: {parsed_data}")

    print("\n6. Regular Expressions (re module):")
    text = "Contact us at info@example.com or support@test.org"
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    print(f"Found emails: {emails}")

    print("\n7. Path Handling (pathlib):")
    current_file = Path(__file__)
    print(f"Current file: {current_file}")
    print(f"File name: {current_file.name}")
    print(f"Parent directory: {current_file.parent}")
    print(f"File exists: {current_file.exists()}")


def demonstrate_import_variations():
    """Demonstrate different import syntaxes and their uses"""
    print("\n" + "=" * 60)
    print("IMPORT SYNTAX VARIATIONS")
    print("=" * 60)

    print("\n1. Basic Import:")
    print("   import math")
    print(f"   math.sqrt(16) = {math.sqrt(16)}")

    print("\n2. Import with Alias:")
    print("   import datetime as dt")
    import datetime as dt
    print(f"   dt.datetime.now() = {dt.datetime.now()}")

    print("\n3. From Import (Specific Functions):")
    print("   from math import sqrt, pi")
    print(f"   sqrt(25) = {sqrt(25)}")
    print(f"   pi = {pi}")

    print("\n4. From Import with Alias:")
    print("   from datetime import datetime as dt_now")
    from datetime import datetime as dt_now
    print(f"   dt_now.now() = {dt_now.now()}")

    print("\n5. Import All (Generally Discouraged):")
    print("   from random import *")
    # Note: We already did this above, so functions like choice() are available

    print("\n6. Multiple Imports:")
    print("   from collections import defaultdict, Counter, namedtuple")
    from collections import defaultdict, Counter, namedtuple

    # Demonstrate usage
    dd = defaultdict(int)
    dd['a'] += 1
    print(f"   defaultdict example: {dict(dd)}")

    counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
    print(f"   Counter example: {counter}")

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(3, 4)
    print(f"   namedtuple example: {p}, distance from origin: {(p.x**2 + p.y**2)**0.5}")


def demonstrate_third_party_imports():
    """Demonstrate third-party package imports"""
    print("\n" + "=" * 60)
    print("THIRD-PARTY PACKAGE IMPORTS")
    print("=" * 60)

    print("\n1. Requests Library (HTTP):")
    if REQUESTS_AVAILABLE:
        print("   import requests")
        print("   ✅ requests is available")

        # Example usage (commented out to avoid actual network calls)
        print("   # response = requests.get('https://api.github.com')")
        print("   # print(response.status_code)")
    else:
        print("   ❌ requests not available")
        print("   Install with: pip install requests")

    print("\n2. NumPy (Numerical Computing):")
    try:
        print("   import numpy as np")
        array = np.array([1, 2, 3, 4, 5])
        print(f"   ✅ NumPy array: {array}")
        print(f"   Array sum: {np.sum(array)}")
    except ImportError:
        print("   ❌ NumPy not available")
        print("   Install with: pip install numpy")

    print("\n3. Pandas (Data Analysis):")
    try:
        print("   import pandas as pd")
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        print("   ✅ Pandas DataFrame:")
        print(f"   {df}")
    except ImportError:
        print("   ❌ Pandas not available")
        print("   Install with: pip install pandas")

    print("\n4. Matplotlib (Plotting):")
    try:
        print("   import matplotlib.pyplot as plt")
        print("   ✅ Matplotlib available")
        # Example (without actually displaying plot)
        print("   # plt.plot([1, 2, 3, 4], [1, 4, 2, 3])")
        print("   # plt.show()")
    except ImportError:
        print("   ❌ Matplotlib not available")
        print("   Install with: pip install matplotlib")


def demonstrate_local_imports():
    """Demonstrate importing local modules and packages"""
    print("\n" + "=" * 60)
    print("LOCAL MODULE AND PACKAGE IMPORTS")
    print("=" * 60)

    print("\n1. Importing from same directory:")
    print("   # If you have a file 'utils.py' in the same directory:")
    print("   # from utils import helper_function")
    print("   # import utils")

    print("\n2. Importing from subdirectory (package):")
    print("   # If you have a package structure like:")
    print("   # my_package/")
    print("   #   __init__.py")
    print("   #   module1.py")
    print("   #   subpackage/")
    print("   #     __init__.py")
    print("   #     module2.py")
    print("   #")
    print("   # You can import:")
    print("   # from my_package import module1")
    print("   # from my_package.subpackage import module2")

    print("\n3. Relative imports (within packages):")
    print("   # From within a package, you can use relative imports:")
    print("   # from . import sibling_module")
    print("   # from .. import parent_module")
    print("   # from ..sibling_package import module")

    print("\n4. Adding to Python path:")
    print("   # To import from arbitrary locations:")
    print("   # import sys")
    print("   # sys.path.append('/path/to/your/modules')")
    print("   # import your_module")

    # Demonstrate current Python path
    print(f"\n5. Current Python path (first 3 entries):")
    for i, path in enumerate(sys.path[:3]):
        print(f"   {i}: {path}")


def demonstrate_dynamic_imports():
    """Demonstrate dynamic imports using importlib"""
    print("\n" + "=" * 60)
    print("DYNAMIC IMPORTS")
    print("=" * 60)

    print("\n1. Dynamic import with importlib:")

    # Dynamic import of a built-in module
    module_name = "math"
    math_module = importlib.import_module(module_name)
    print(f"   Dynamically imported {module_name}")
    print(f"   math_module.sqrt(16) = {math_module.sqrt(16)}")

    print("\n2. Dynamic import with getattr:")
    # Get a function dynamically
    function_name = "sqrt"
    sqrt_function = getattr(math_module, function_name)
    print(f"   Got function '{function_name}' dynamically")
    print(f"   sqrt_function(25) = {sqrt_function(25)}")

    print("\n3. Checking if module is available:")
    def try_import(module_name):
        try:
            module = importlib.import_module(module_name)
            print(f"   ✅ {module_name} is available")
            return module
        except ImportError:
            print(f"   ❌ {module_name} is not available")
            return None

    try_import("sqlite3")
    try_import("nonexistent_module")

    print("\n4. Loading modules from string names:")
    module_names = ["json", "random", "datetime"]
    loaded_modules = {}

    for name in module_names:
        try:
            loaded_modules[name] = importlib.import_module(name)
            print(f"   ✅ Loaded {name}")
        except ImportError:
            print(f"   ❌ Failed to load {name}")

    # Use dynamically loaded modules
    if "json" in loaded_modules:
        json_module = loaded_modules["json"]
        data = {"dynamic": True}
        print(f"   JSON dumps: {json_module.dumps(data)}")


def demonstrate_import_inspection():
    """Demonstrate introspection of imported modules"""
    print("\n" + "=" * 60)
    print("MODULE INSPECTION AND INTROSPECTION")
    print("=" * 60)

    print("\n1. Module attributes:")
    print(f"   math module file: {math.__file__ if hasattr(math, '__file__') else 'Built-in'}")
    print(f"   math module name: {math.__name__}")
    print(f"   math module doc: {math.__doc__[:50]}...")

    print("\n2. Available functions in a module:")
    math_functions = [name for name in dir(math) if not name.startswith('_')]
    print(f"   Math functions: {math_functions[:10]}...")  # First 10

    print("\n3. Function signatures:")
    for func_name in ["sqrt", "sin", "cos"][:3]:
        func = getattr(math, func_name)
        sig = inspect.signature(func)
        print(f"   math.{func_name}{sig}")

    print("\n4. Module inspection with inspect:")
    print(f"   Is math a module? {inspect.ismodule(math)}")
    print(f"   Is math.sqrt a function? {inspect.isfunction(math.sqrt)}")

    # Get all functions from a module
    functions = inspect.getmembers(math, inspect.isfunction)
    print(f"   Number of functions in math: {len(functions)}")


def demonstrate_import_best_practices():
    """Demonstrate import best practices and patterns"""
    print("\n" + "=" * 60)
    print("IMPORT BEST PRACTICES")
    print("=" * 60)

    print("\n1. Import Order (PEP 8):")
    print("   # 1. Standard library imports")
    print("   import os")
    print("   import sys")
    print("   from pathlib import Path")
    print("")
    print("   # 2. Related third-party library imports")
    print("   import requests")
    print("   import numpy as np")
    print("")
    print("   # 3. Local application/library imports")
    print("   from mypackage import mymodule")
    print("   from . import sibling_module")

    print("\n2. Avoid Import * (except for specific cases):")
    print("   ❌ from math import *  # Pollutes namespace")
    print("   ✅ from math import sqrt, pi  # Explicit imports")
    print("   ✅ import math  # Use qualified names")

    print("\n3. Use meaningful aliases:")
    print("   ✅ import numpy as np  # Standard, widely recognized")
    print("   ✅ import pandas as pd  # Standard, widely recognized")
    print("   ❌ import numpy as n  # Not clear")

    print("\n4. Lazy imports (import when needed):")
    print("   def expensive_operation():")
    print("       import expensive_module  # Only imported when function is called")
    print("       return expensive_module.do_work()")

    print("\n5. Handling optional dependencies:")
    print("   try:")
    print("       import optional_package")
    print("       HAS_OPTIONAL = True")
    print("   except ImportError:")
    print("       HAS_OPTIONAL = False")
    print("")
    print("   def feature_that_needs_optional():")
    print("       if not HAS_OPTIONAL:")
    print("           raise ImportError('optional_package required for this feature')")

    print("\n6. Module-level imports vs function-level imports:")
    print("   # Module level (preferred for most cases)")
    print("   import requests")
    print("")
    print("   # Function level (for conditional/optional imports)")
    print("   def download_file():")
    print("       import requests  # Only if needed")


def demonstrate_package_structure():
    """Demonstrate package structure and __init__.py"""
    print("\n" + "=" * 60)
    print("PACKAGE STRUCTURE AND __init__.py")
    print("=" * 60)

    print("\n1. Basic Package Structure:")
    print("   mypackage/")
    print("   ├── __init__.py          # Makes it a package")
    print("   ├── module1.py           # Module in package")
    print("   ├── module2.py           # Another module")
    print("   └── subpackage/")
    print("       ├── __init__.py      # Subpackage")
    print("       └── submodule.py     # Module in subpackage")

    print("\n2. __init__.py purposes:")
    print("   - Makes directory a Python package")
    print("   - Controls what gets imported with 'from package import *'")
    print("   - Can contain package initialization code")
    print("   - Can define package-level variables and functions")

    print("\n3. Example __init__.py content:")
    print('   """My Package Documentation"""')
    print('   __version__ = "1.0.0"')
    print('   __author__ = "Your Name"')
    print('')
    print('   # Import commonly used functions')
    print('   from .module1 import important_function')
    print('   from .module2 import AnotherClass')
    print('')
    print('   # Define what gets imported with "from package import *"')
    print('   __all__ = ["important_function", "AnotherClass"]')

    print("\n4. Importing from packages:")
    print("   # Different ways to import from packages")
    print("   import mypackage")
    print("   import mypackage.module1")
    print("   from mypackage import module1")
    print("   from mypackage.module1 import important_function")
    print("   from mypackage.subpackage import submodule")


def create_sample_package():
    """Create a sample package structure for demonstration"""
    print("\n" + "=" * 60)
    print("CREATING SAMPLE PACKAGE")
    print("=" * 60)

    # Create sample package directory structure
    base_dir = Path("sample_package_demo")
    package_dir = base_dir / "myutils"

    try:
        # Create directories
        package_dir.mkdir(parents=True, exist_ok=True)
        subpackage_dir = package_dir / "helpers"
        subpackage_dir.mkdir(exist_ok=True)

        # Create __init__.py files
        init_content = '''"""
MyUtils Package - A sample package for demonstration
"""

__version__ = "1.0.0"
__author__ = "Python Tutorial"

# Import commonly used functions
from .math_utils import add, multiply
from .string_utils import reverse_string

# Define what gets imported with "from myutils import *"
__all__ = ["add", "multiply", "reverse_string"]

print("MyUtils package initialized!")
'''

        with open(package_dir / "__init__.py", "w") as f:
            f.write(init_content)

        # Create math_utils.py
        math_utils_content = '''"""
Mathematical utility functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
'''

        with open(package_dir / "math_utils.py", "w") as f:
            f.write(math_utils_content)

        # Create string_utils.py
        string_utils_content = '''"""
String utility functions
"""

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def capitalize_words(s):
    """Capitalize each word in a string"""
    return ' '.join(word.capitalize() for word in s.split())

def count_vowels(s):
    """Count vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
'''

        with open(package_dir / "string_utils.py", "w") as f:
            f.write(string_utils_content)

        # Create subpackage
        subpackage_init = '''"""
Helper utilities subpackage
"""

from .formatters import format_number, format_date

__all__ = ["format_number", "format_date"]
'''

        with open(subpackage_dir / "__init__.py", "w") as f:
            f.write(subpackage_init)

        formatters_content = '''"""
Formatting helper functions
"""

def format_number(num, decimals=2):
    """Format a number with specified decimal places"""
    return f"{num:.{decimals}f}"

def format_date(date_obj):
    """Format a date object as a string"""
    return date_obj.strftime("%Y-%m-%d")
'''

        with open(subpackage_dir / "formatters.py", "w") as f:
            f.write(formatters_content)

        print(f"✅ Created sample package at: {package_dir.absolute()}")
        print("\nPackage structure:")
        for root, dirs, files in os.walk(package_dir):
            level = root.replace(str(package_dir), '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")

        # Demonstrate importing from the created package
        print("\n3. Importing from created package:")

        # Add the package to Python path
        if str(base_dir.absolute()) not in sys.path:
            sys.path.insert(0, str(base_dir.absolute()))

        try:
            # Import the package
            import myutils
            print(f"   ✅ Imported myutils package (version {myutils.__version__})")

            # Use functions from the package
            result1 = myutils.add(5, 3)
            result2 = myutils.multiply(4, 6)
            result3 = myutils.reverse_string("hello")

            print(f"   myutils.add(5, 3) = {result1}")
            print(f"   myutils.multiply(4, 6) = {result2}")
            print(f"   myutils.reverse_string('hello') = '{result3}'")

            # Import from subpackage
            from myutils.helpers import format_number
            formatted = format_number(3.14159, 3)
            print(f"   format_number(3.14159, 3) = '{formatted}'")

        except ImportError as e:
            print(f"   ❌ Failed to import created package: {e}")

    except Exception as e:
        print(f"❌ Failed to create sample package: {e}")


def main():
    """Main function demonstrating all import concepts"""
    print("📦 COMPREHENSIVE LIBRARY IMPORT TUTORIAL")
    print("This tutorial covers all aspects of importing libraries and modules in Python.")

    demonstrate_builtin_imports()
    demonstrate_import_variations()
    demonstrate_third_party_imports()
    demonstrate_local_imports()
    demonstrate_dynamic_imports()
    demonstrate_import_inspection()
    demonstrate_import_best_practices()
    demonstrate_package_structure()
    create_sample_package()

    print("\n" + "=" * 60)
    print("LIBRARY IMPORT TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\n💡 Key Import Concepts:")
    print("- import module_name")
    print("- from module import function")
    print("- import module as alias")
    print("- from package.module import function")
    print("- Relative imports with . and ..")

    print("\n🛠️ Best Practices:")
    print("- Follow PEP 8 import ordering")
    print("- Use meaningful aliases")
    print("- Avoid 'from module import *'")
    print("- Handle optional dependencies gracefully")
    print("- Use __init__.py for package initialization")
    print("- Prefer absolute imports over relative imports")

    print("\n📚 Next Steps:")
    print("- Learn about virtual environments (venv, conda)")
    print("- Explore package management with pip")
    print("- Study Python's import system in depth")
    print("- Learn to create and publish your own packages")
    print("- Understand namespace packages")


if __name__ == "__main__":
    main()