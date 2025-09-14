"""
Comprehensive Object-Oriented Programming Tutorial
=================================================

This module demonstrates all aspects of OOP in Python:
- Classes and Objects
- Attributes and Methods
- Inheritance and Polymorphism
- Encapsulation and Data Hiding
- Abstract Classes and Interfaces
- Magic Methods (Dunder Methods)
- Class Methods and Static Methods
- Properties and Descriptors
- Composition vs Inheritance
- Design Patterns
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum, auto
import json
import datetime


# 1. BASIC CLASS DEFINITION
class BasicPerson:
    """Basic person class demonstrating fundamental OOP concepts"""

    # Class attribute (shared by all instances)
    species = "Homo sapiens"
    population = 0

    def __init__(self, name: str, age: int, email: str = ""):
        """Initialize a new person instance"""
        # Instance attributes
        self.name = name
        self.age = age
        self.email = email
        self._id = id(self)  # Protected attribute (convention)
        BasicPerson.population += 1  # Update class attribute

    def introduce(self) -> str:
        """Instance method to introduce the person"""
        return f"Hi, I'm {self.name}, {self.age} years old."

    def celebrate_birthday(self) -> None:
        """Method that modifies instance state"""
        self.age += 1
        print(f"Happy birthday {self.name}! You're now {self.age} years old.")

    def __str__(self) -> str:
        """String representation for users"""
        return f"{self.name} ({self.age} years old)"

    def __repr__(self) -> str:
        """String representation for developers"""
        return f"BasicPerson(name='{self.name}', age={self.age}, email='{self.email}')"


# 2. INHERITANCE
class Employee(BasicPerson):
    """Employee class inheriting from BasicPerson"""

    def __init__(self, name: str, age: int, email: str, employee_id: str, salary: float):
        super().__init__(name, age, email)  # Call parent constructor
        self.employee_id = employee_id
        self.salary = salary
        self.is_active = True

    def introduce(self) -> str:
        """Override parent method (Polymorphism)"""
        return f"Hi, I'm {self.name}, employee #{self.employee_id}."

    def give_raise(self, amount: float) -> None:
        """Employee-specific method"""
        old_salary = self.salary
        self.salary += amount
        print(f"{self.name}'s salary increased from ${old_salary:,.2f} to ${self.salary:,.2f}")

    def terminate(self) -> None:
        """Terminate employment"""
        self.is_active = False
        print(f"Employee {self.name} ({self.employee_id}) has been terminated.")


class Manager(Employee):
    """Manager class inheriting from Employee"""

    def __init__(self, name: str, age: int, email: str, employee_id: str,
                 salary: float, department: str):
        super().__init__(name, age, email, employee_id, salary)
        self.department = department
        self.team: List[Employee] = []

    def add_team_member(self, employee: Employee) -> None:
        """Add employee to team"""
        if employee not in self.team:
            self.team.append(employee)
            print(f"{employee.name} added to {self.name}'s team in {self.department}")

    def remove_team_member(self, employee: Employee) -> None:
        """Remove employee from team"""
        if employee in self.team:
            self.team.remove(employee)
            print(f"{employee.name} removed from {self.name}'s team")

    def introduce(self) -> str:
        """Override parent method"""
        return f"Hi, I'm {self.name}, manager of {self.department} department with {len(self.team)} team members."

    def conduct_team_meeting(self) -> None:
        """Manager-specific method"""
        print(f"\n{self.name} is conducting a team meeting for {self.department}:")
        for employee in self.team:
            print(f"  - {employee.name} ({employee.employee_id})")


# 3. ENCAPSULATION AND PROPERTIES
class BankAccount:
    """Demonstrates encapsulation, properties, and data validation"""

    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance  # Protected attribute
        self._transaction_history: List[Dict[str, Any]] = []
        self.__pin = None  # Private attribute (name mangling)

    @property
    def balance(self) -> float:
        """Getter for balance (read-only for external access)"""
        return self._balance

    @property
    def transaction_history(self) -> List[Dict[str, Any]]:
        """Read-only access to transaction history"""
        return self._transaction_history.copy()

    def set_pin(self, pin: str) -> None:
        """Set PIN for account security"""
        if len(pin) == 4 and pin.isdigit():
            self.__pin = pin
            print("PIN set successfully")
        else:
            raise ValueError("PIN must be exactly 4 digits")

    def verify_pin(self, pin: str) -> bool:
        """Verify PIN"""
        return self.__pin == pin

    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        """Deposit money to account"""
        if amount <= 0:
            print("Deposit amount must be positive")
            return False

        self._balance += amount
        self._record_transaction("DEPOSIT", amount, description)
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True

    def withdraw(self, amount: float, pin: str, description: str = "Withdrawal") -> bool:
        """Withdraw money from account"""
        if not self.verify_pin(pin):
            print("Invalid PIN")
            return False

        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False

        if amount > self._balance:
            print("Insufficient funds")
            return False

        self._balance -= amount
        self._record_transaction("WITHDRAWAL", -amount, description)
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True

    def transfer(self, amount: float, target_account: 'BankAccount',
                 pin: str, description: str = "Transfer") -> bool:
        """Transfer money to another account"""
        if not self.verify_pin(pin):
            print("Invalid PIN")
            return False

        if self.withdraw(amount, pin, f"Transfer to {target_account.account_number}"):
            target_account.deposit(amount, f"Transfer from {self.account_number}")
            return True
        return False

    def _record_transaction(self, transaction_type: str, amount: float, description: str) -> None:
        """Private method to record transaction"""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "description": description,
            "timestamp": datetime.datetime.now(),
            "balance_after": self._balance
        }
        self._transaction_history.append(transaction)

    def get_statement(self, last_n: int = 10) -> None:
        """Print account statement"""
        print(f"\nAccount Statement for {self.account_number} ({self.owner})")
        print(f"Current Balance: ${self._balance:.2f}")
        print(f"\nLast {min(last_n, len(self._transaction_history))} transactions:")
        print("-" * 80)

        for transaction in self._transaction_history[-last_n:]:
            print(f"{transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} | "
                  f"{transaction['type']:<12} | "
                  f"${transaction['amount']:>8.2f} | "
                  f"${transaction['balance_after']:>10.2f} | "
                  f"{transaction['description']}")

    def __str__(self) -> str:
        return f"BankAccount({self.account_number}, {self.owner}, ${self._balance:.2f})"


# 4. ABSTRACT CLASSES AND INTERFACES
class Shape(ABC):
    """Abstract base class for shapes"""

    def __init__(self, color: str = "white"):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """Calculate area of the shape"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter of the shape"""
        pass

    @abstractmethod
    def draw(self) -> str:
        """Return string representation of the shape"""
        pass

    def describe(self) -> str:
        """Concrete method available to all subclasses"""
        return f"This is a {self.color} {self.__class__.__name__.lower()} with area {self.area():.2f}"


class Rectangle(Shape):
    """Rectangle implementation of Shape"""

    def __init__(self, width: float, height: float, color: str = "white"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def draw(self) -> str:
        return f"Drawing a {self.color} rectangle ({self.width} x {self.height})"


class Circle(Shape):
    """Circle implementation of Shape"""

    def __init__(self, radius: float, color: str = "white"):
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius

    def draw(self) -> str:
        return f"Drawing a {self.color} circle (radius: {self.radius})"


# 5. MAGIC METHODS (DUNDER METHODS)
class Vector:
    """Demonstrates magic methods for operator overloading"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other: 'Vector') -> 'Vector':
        """Addition: vector1 + vector2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtraction: vector1 - vector2"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Union[float, int]) -> 'Vector':
        """Scalar multiplication: vector * scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: Union[float, int]) -> 'Vector':
        """Reverse multiplication: scalar * vector"""
        return self.__mul__(scalar)

    def __eq__(self, other: 'Vector') -> bool:
        """Equality comparison"""
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        """Length of vector (magnitude as int)"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __getitem__(self, index: int) -> float:
        """Index access: vector[0] -> x, vector[1] -> y"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

    def __setitem__(self, index: int, value: float) -> None:
        """Index assignment"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")

    def __iter__(self):
        """Make vector iterable"""
        yield self.x
        yield self.y

    def __bool__(self) -> bool:
        """Truth value: False if zero vector"""
        return self.x != 0 or self.y != 0

    def magnitude(self) -> float:
        """Calculate vector magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self) -> 'Vector':
        """Return normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)


# 6. CLASS METHODS AND STATIC METHODS
class Temperature:
    """Demonstrates class methods, static methods, and alternative constructors"""

    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> 'Temperature':
        """Alternative constructor from Fahrenheit"""
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @classmethod
    def from_kelvin(cls, kelvin: float) -> 'Temperature':
        """Alternative constructor from Kelvin"""
        celsius = kelvin - 273.15
        return cls(celsius)

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Static utility method"""
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Static utility method"""
        return celsius * 9 / 5 + 32

    @staticmethod
    def is_freezing_celsius(celsius: float) -> bool:
        """Static utility method"""
        return celsius <= 0

    @property
    def fahrenheit(self) -> float:
        """Get temperature in Fahrenheit"""
        return self.celsius * 9 / 5 + 32

    @property
    def kelvin(self) -> float:
        """Get temperature in Kelvin"""
        return self.celsius + 273.15

    def __str__(self) -> str:
        return f"{self.celsius}°C ({self.fahrenheit:.1f}°F, {self.kelvin:.1f}K)"


# 7. COMPOSITION OVER INHERITANCE
class Engine:
    """Component class for composition example"""

    def __init__(self, horsepower: int, fuel_type: str):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False

    def start(self) -> None:
        if not self.is_running:
            self.is_running = True
            print(f"Engine started! {self.horsepower}HP {self.fuel_type} engine running.")

    def stop(self) -> None:
        if self.is_running:
            self.is_running = False
            print("Engine stopped.")

    def __str__(self) -> str:
        status = "running" if self.is_running else "stopped"
        return f"{self.horsepower}HP {self.fuel_type} engine ({status})"


class GPS:
    """Another component for composition"""

    def __init__(self):
        self.current_location = "Unknown"
        self.destination = None

    def set_destination(self, destination: str) -> None:
        self.destination = destination
        print(f"GPS destination set to: {destination}")

    def navigate(self) -> str:
        if self.destination:
            return f"Navigate from {self.current_location} to {self.destination}"
        return "No destination set"


class Car:
    """Car class using composition instead of inheritance"""

    def __init__(self, make: str, model: str, year: int, horsepower: int, fuel_type: str):
        self.make = make
        self.model = model
        self.year = year

        # Composition: Car HAS an Engine and GPS
        self.engine = Engine(horsepower, fuel_type)
        self.gps = GPS()

        self.is_locked = True
        self.current_speed = 0

    def unlock(self) -> None:
        self.is_locked = False
        print(f"{self.make} {self.model} unlocked")

    def lock(self) -> None:
        self.is_locked = True
        self.engine.stop()
        print(f"{self.make} {self.model} locked")

    def start(self) -> None:
        if not self.is_locked:
            self.engine.start()
        else:
            print("Cannot start engine: car is locked")

    def drive(self, speed: int) -> None:
        if self.engine.is_running:
            self.current_speed = speed
            print(f"Driving at {speed} mph")
        else:
            print("Cannot drive: engine is not running")

    def navigate_to(self, destination: str) -> None:
        self.gps.set_destination(destination)
        print(self.gps.navigate())

    def __str__(self) -> str:
        locked_status = "locked" if self.is_locked else "unlocked"
        return f"{self.year} {self.make} {self.model} ({locked_status})"


# 8. SINGLETON PATTERN
class DatabaseConnection:
    """Singleton pattern implementation"""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not DatabaseConnection._initialized:
            self.connection_string = "postgresql://localhost:5432/mydb"
            self.is_connected = False
            DatabaseConnection._initialized = True
            print("Database connection instance created")

    def connect(self) -> None:
        if not self.is_connected:
            self.is_connected = True
            print(f"Connected to {self.connection_string}")

    def disconnect(self) -> None:
        if self.is_connected:
            self.is_connected = False
            print("Database connection closed")

    def query(self, sql: str) -> List[Dict]:
        if self.is_connected:
            print(f"Executing: {sql}")
            return [{"id": 1, "name": "Sample Data"}]
        else:
            raise Exception("Not connected to database")


# 9. OBSERVER PATTERN
class EventEmitter:
    """Simple observer pattern implementation"""

    def __init__(self):
        self._observers: Dict[str, List[callable]] = {}

    def subscribe(self, event: str, callback: callable) -> None:
        """Subscribe to an event"""
        if event not in self._observers:
            self._observers[event] = []
        self._observers[event].append(callback)

    def unsubscribe(self, event: str, callback: callable) -> None:
        """Unsubscribe from an event"""
        if event in self._observers:
            try:
                self._observers[event].remove(callback)
            except ValueError:
                pass

    def emit(self, event: str, *args, **kwargs) -> None:
        """Emit an event to all subscribers"""
        if event in self._observers:
            for callback in self._observers[event]:
                callback(*args, **kwargs)


class ShoppingCart(EventEmitter):
    """Shopping cart with event notifications"""

    def __init__(self):
        super().__init__()
        self.items: List[Dict[str, Any]] = []
        self.total = 0.0

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Add item to cart"""
        item = {"name": name, "price": price, "quantity": quantity}
        self.items.append(item)
        self.total += price * quantity

        # Emit event
        self.emit("item_added", item, self.total)

    def remove_item(self, name: str) -> bool:
        """Remove item from cart"""
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                self.total -= item["price"] * item["quantity"]

                # Emit event
                self.emit("item_removed", item, self.total)
                return True
        return False

    def clear_cart(self) -> None:
        """Clear all items"""
        self.items.clear()
        self.total = 0.0
        self.emit("cart_cleared")


# 10. DATA CLASSES (Python 3.7+)
@dataclass
class Product:
    """Product data class with automatic methods"""
    name: str
    price: float
    category: str
    in_stock: bool = True
    quantity: int = 0
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Called after initialization"""
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")

    @property
    def total_value(self) -> float:
        """Calculate total value of stock"""
        return self.price * self.quantity

    def add_tag(self, tag: str) -> None:
        """Add a tag to the product"""
        if tag not in self.tags:
            self.tags.append(tag)

    def is_available(self) -> bool:
        """Check if product is available"""
        return self.in_stock and self.quantity > 0


# 11. ENUM CLASSES
class OrderStatus(Enum):
    """Enum for order statuses"""
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()

    def can_cancel(self) -> bool:
        """Check if order can be cancelled"""
        return self in [OrderStatus.PENDING, OrderStatus.PROCESSING]


@dataclass
class Order:
    """Order class using enum and dataclass"""
    order_id: str
    customer_name: str
    items: List[Product]
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    @property
    def total_amount(self) -> float:
        """Calculate total order amount"""
        return sum(item.price * item.quantity for item in self.items)

    def update_status(self, new_status: OrderStatus) -> bool:
        """Update order status"""
        if new_status == OrderStatus.CANCELLED and not self.status.can_cancel():
            print(f"Cannot cancel order {self.order_id}: already {self.status.name}")
            return False

        old_status = self.status
        self.status = new_status
        print(f"Order {self.order_id} status changed: {old_status.name} -> {new_status.name}")
        return True


# DEMONSTRATION FUNCTIONS
def demonstrate_basic_oop():
    """Demonstrate basic OOP concepts"""
    print("=" * 60)
    print("BASIC OBJECT-ORIENTED PROGRAMMING")
    print("=" * 60)

    # Create instances
    print("\n1. Creating Person instances:")
    person1 = BasicPerson("Alice", 25, "alice@email.com")
    person2 = BasicPerson("Bob", 30)

    print(f"Created: {person1}")
    print(f"Created: {person2}")
    print(f"Total population: {BasicPerson.population}")
    print(f"Species: {BasicPerson.species}")

    # Method calls
    print("\n2. Calling methods:")
    print(person1.introduce())
    person1.celebrate_birthday()
    print(f"Updated: {person1}")


def demonstrate_inheritance():
    """Demonstrate inheritance and polymorphism"""
    print("\n" + "=" * 60)
    print("INHERITANCE AND POLYMORPHISM")
    print("=" * 60)

    # Create employee and manager
    emp1 = Employee("Charlie", 28, "charlie@company.com", "E001", 50000)
    emp2 = Employee("Diana", 32, "diana@company.com", "E002", 55000)
    manager = Manager("Eve", 35, "eve@company.com", "M001", 80000, "Engineering")

    print("\n1. Polymorphism (same method, different behavior):")
    for person in [emp1, emp2, manager]:
        print(f"  {person.introduce()}")

    print("\n2. Manager managing team:")
    manager.add_team_member(emp1)
    manager.add_team_member(emp2)
    manager.conduct_team_meeting()

    print("\n3. Employee operations:")
    emp1.give_raise(5000)
    emp1.celebrate_birthday()  # Inherited method


def demonstrate_encapsulation():
    """Demonstrate encapsulation and properties"""
    print("\n" + "=" * 60)
    print("ENCAPSULATION AND PROPERTIES")
    print("=" * 60)

    # Create bank accounts
    account1 = BankAccount("ACC001", "Alice Johnson", 1000.0)
    account2 = BankAccount("ACC002", "Bob Smith", 500.0)

    print("\n1. Setting up accounts:")
    account1.set_pin("1234")
    account2.set_pin("5678")

    print(f"Account 1: {account1}")
    print(f"Account 2: {account2}")

    print("\n2. Performing transactions:")
    account1.deposit(500, "Salary deposit")
    account1.withdraw(200, "1234", "ATM withdrawal")
    account1.transfer(300, account2, "1234", "Transfer to Bob")

    print("\n3. Account statements:")
    account1.get_statement(5)
    account2.get_statement(5)

    print("\n4. Encapsulation demonstration:")
    print(f"Balance (read-only property): ${account1.balance:.2f}")
    # account1.balance = 9999  # This would cause an AttributeError


def demonstrate_abstract_classes():
    """Demonstrate abstract classes and interfaces"""
    print("\n" + "=" * 60)
    print("ABSTRACT CLASSES AND INTERFACES")
    print("=" * 60)

    # Create shapes
    shapes = [
        Rectangle(5, 3, "red"),
        Circle(4, "blue"),
        Rectangle(2, 8, "green"),
        Circle(2.5, "yellow")
    ]

    print("\n1. Working with shapes (polymorphism):")
    for shape in shapes:
        print(f"  {shape.draw()}")
        print(f"     Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
        print(f"     {shape.describe()}")
        print()


def demonstrate_magic_methods():
    """Demonstrate magic methods and operator overloading"""
    print("\n" + "=" * 60)
    print("MAGIC METHODS AND OPERATOR OVERLOADING")
    print("=" * 60)

    # Create vectors
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print("\n1. Vector operations:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 = {v1 * 3}")
    print(f"2 * v1 = {2 * v1}")

    print("\n2. Comparison and iteration:")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 magnitude: {v1.magnitude():.2f}")
    print(f"v1 components: x={v1[0]}, y={v1[1]}")
    print(f"Iterating v1: {list(v1)}")

    print(f"Boolean value of v1: {bool(v1)}")
    zero_vector = Vector(0, 0)
    print(f"Boolean value of zero vector: {bool(zero_vector)}")


def demonstrate_class_methods():
    """Demonstrate class methods and static methods"""
    print("\n" + "=" * 60)
    print("CLASS METHODS AND STATIC METHODS")
    print("=" * 60)

    print("\n1. Creating Temperature objects:")
    temp1 = Temperature(25)  # Regular constructor
    temp2 = Temperature.from_fahrenheit(77)  # Class method
    temp3 = Temperature.from_kelvin(298.15)  # Class method

    print(f"temp1 (25°C): {temp1}")
    print(f"temp2 (77°F): {temp2}")
    print(f"temp3 (298.15K): {temp3}")

    print("\n2. Static method utilities:")
    print(f"32°F in Celsius: {Temperature.fahrenheit_to_celsius(32):.1f}°C")
    print(f"100°C in Fahrenheit: {Temperature.celsius_to_fahrenheit(100):.1f}°F")
    print(f"Is -5°C freezing? {Temperature.is_freezing_celsius(-5)}")


def demonstrate_composition():
    """Demonstrate composition over inheritance"""
    print("\n" + "=" * 60)
    print("COMPOSITION OVER INHERITANCE")
    print("=" * 60)

    # Create a car (composition)
    car = Car("Toyota", "Camry", 2023, 203, "Gasoline")

    print("\n1. Car operations:")
    print(f"Car: {car}")
    print(f"Engine: {car.engine}")

    car.unlock()
    car.start()
    car.drive(60)
    car.navigate_to("Downtown Mall")

    print(f"\nCar status after operations:")
    print(f"  Car: {car}")
    print(f"  Engine: {car.engine}")
    print(f"  Current speed: {car.current_speed} mph")


def demonstrate_design_patterns():
    """Demonstrate design patterns"""
    print("\n" + "=" * 60)
    print("DESIGN PATTERNS")
    print("=" * 60)

    print("\n1. Singleton Pattern:")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Same instance? {db1 is db2}")

    db1.connect()
    db2.query("SELECT * FROM users")  # Same connection

    print("\n2. Observer Pattern:")
    cart = ShoppingCart()

    # Define event handlers
    def on_item_added(item, total):
        print(f"  📦 Added {item['name']} (${item['price']:.2f}) - Total: ${total:.2f}")

    def on_item_removed(item, total):
        print(f"  🗑️ Removed {item['name']} - Total: ${total:.2f}")

    def on_cart_cleared():
        print("  🧹 Cart cleared!")

    # Subscribe to events
    cart.subscribe("item_added", on_item_added)
    cart.subscribe("item_removed", on_item_removed)
    cart.subscribe("cart_cleared", on_cart_cleared)

    # Trigger events
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99)
    cart.remove_item("Mouse")
    cart.clear_cart()


def demonstrate_dataclasses_and_enums():
    """Demonstrate dataclasses and enums"""
    print("\n" + "=" * 60)
    print("DATACLASSES AND ENUMS")
    print("=" * 60)

    # Create products
    print("\n1. Creating products with dataclasses:")
    laptop = Product("Gaming Laptop", 1299.99, "Electronics", True, 5, ["gaming", "portable"])
    mouse = Product("Wireless Mouse", 49.99, "Electronics", True, 25)
    book = Product("Python Guide", 39.99, "Books", True, 100)

    print(f"Laptop: {laptop}")
    print(f"Mouse total value: ${mouse.total_value:.2f}")

    mouse.add_tag("wireless")
    mouse.add_tag("ergonomic")
    print(f"Mouse tags: {mouse.tags}")

    # Create order
    print("\n2. Creating order with enums:")
    order = Order("ORD001", "Alice Johnson", [laptop, mouse, book])
    print(f"Order: {order.order_id} for {order.customer_name}")
    print(f"Total amount: ${order.total_amount:.2f}")
    print(f"Status: {order.status.name}")

    # Update order status
    print("\n3. Order status transitions:")
    order.update_status(OrderStatus.PROCESSING)
    order.update_status(OrderStatus.SHIPPED)
    order.update_status(OrderStatus.CANCELLED)  # This should fail
    order.update_status(OrderStatus.DELIVERED)


def main():
    """Main function demonstrating all OOP concepts"""
    print("🐍 COMPREHENSIVE OBJECT-ORIENTED PROGRAMMING TUTORIAL")
    print("This tutorial covers all aspects of OOP in Python with practical examples.")

    demonstrate_basic_oop()
    demonstrate_inheritance()
    demonstrate_encapsulation()
    demonstrate_abstract_classes()
    demonstrate_magic_methods()
    demonstrate_class_methods()
    demonstrate_composition()
    demonstrate_design_patterns()
    demonstrate_dataclasses_and_enums()

    print("\n" + "=" * 60)
    print("OOP TUTORIAL COMPLETED!")
    print("=" * 60)

    print("\n💡 Key OOP Principles:")
    print("1. Encapsulation: Bundle data and methods, control access")
    print("2. Inheritance: Create new classes based on existing ones")
    print("3. Polymorphism: Same interface, different implementations")
    print("4. Abstraction: Hide complex implementation details")

    print("\n🛠️ Advanced OOP Features:")
    print("- Magic methods for operator overloading")
    print("- Property decorators for controlled access")
    print("- Class methods and static methods")
    print("- Abstract classes and interfaces")
    print("- Composition over inheritance")
    print("- Design patterns (Singleton, Observer)")
    print("- Dataclasses for automatic method generation")
    print("- Enums for named constants")


if __name__ == "__main__":
    main()