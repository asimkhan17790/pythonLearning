# Oops core concepts

# Abstraction - not knowing how something functions internally.
# Encapsulation bundles data (attributes) and methods that operate on that data within a class.
# This protects the data from being accidentally changed or misused from outside the object. It controls ACCESS
# Encapsulation - packaging correlated things together
# Inheritence - extensds in java. Building things on top of some existing things
# Polymorphism - same method name different behavior

class Employee:
    """ Employee Class"""

    company = "HP"

    def getSalary(self):  # Self is import. It is always the fir param in all methods
        return 50000


e = Employee()
print(e.getSalary())


e2 = Employee()
print(e2.getSalary())
print(e2.company)
