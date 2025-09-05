# DUNDER stands FOR DOUBLE UNDERSCORE

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name} Salary:{self.salary} Age:{self.age}"

    def __repr__(self):
        return f"Name---> {self.name} Salary:{self.salary} Age--->{self.age}"

    def __len__(self):
        return len(self.name)


e = Employee("Asim Khan", 180000)
print(e.name, e.salary)

e.age = 35

print("Directly printing object:-->", e)
print(str(e))
print(repr(e))
print(len(e))
