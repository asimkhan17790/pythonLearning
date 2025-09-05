class Employee:
    company = "HP"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # instance method
    def print_info(self):
        print(f"Name: {self.name} and Salary:{self.salary}")

    # Static Method

    @staticmethod
    def sum(a, b):
        return a+b

    # class methods

    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company_name(cls, new_company_name):
        cls.company = new_company_name


e1 = Employee("Jack", 21231)
e2 = Employee("Asim", 180000)

print(e1.company)
print(e2.company)
print(Employee.company)


# calling instance method
e1.print_info()

# Calling static method
print(e1.sum(5, 4))
print(Employee.sum(5, 4))

print(Employee.company)
print(e1.company)

print(e1.change_company_name("Microsoft"))
print(Employee.company)
print(e2.company)
e2.change_company_name("HP Again")
print(Employee.company)
Employee.change_company_name("Google")
print(e2.company)
print(e1.company)
print(Employee.company)
