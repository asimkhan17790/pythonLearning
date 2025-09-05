class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        if (age < 18):
            raise ValueError("Age of Employee should be greater than 18")
        self.age = age

    def __str__(self):
        return f"Name:{self.name} Age:{self.age} Salary:{self.salary}"


try:
    employee = Employee("Asim", 15000, 15)
    print(employee)
except Exception as e:
    print("WRONG AGE ENTERED ---", e)
