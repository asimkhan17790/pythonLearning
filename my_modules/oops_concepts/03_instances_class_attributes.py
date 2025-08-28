class Employee:
    """Employee class to test out Employee class"""

    company = "Asus"

    def __init__(self, name, salary, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        """
        Prints the employee's information in a formatted string.
        """
        print(f"""
             Employee Name: {self.name}
             Employee Salary: {self.get_salary()}
             Employee Bond: {self.bond} years
             Employee Compan: {self.company} INC
             """
              )


e1 = Employee("Taran", 100000, 6, "Google")
e1.get_info()
# Will always print instance attribute. If its not present then class attribtue is printed
print(e1.company)
print("To print Class Attribute --> ", Employee.company)


# object introspection
# print(dir(e1))
