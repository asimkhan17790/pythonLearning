
class Employee:
    """
    Employee class demonstrates the use of constructors in Python.
    Attributes:
        name (str): Name of the employee.
        salary (float): Salary of the employee.
        bond (int): Bond period in years.
    """

    # Constructor
    # def __init__(self):  # No Args Constructor
    #     pass

    def __init__(self, name, salary, bond):
        """
        Parameterized constructor to initialize Employee object.
        Args:
            name (str): Name of the employee.
            salary (float): Salary of the employee.
            bond (int): Bond period in years.
        """
        self.salary = salary  # Create instance attribute of name salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        """
        Returns the salary of the employee.
        Returns:
            float: The salary of the employee.
        """
        return self.salary

    def get_info(self):
        """
        Prints the employee's information in a formatted string.
        """
        print(f"""
             Employee Name: {self.name}
             Employee Salary: {self.get_salary()}
             Employee Bond: {self.bond} years"""
              )


# Example usage
e = Employee("Asim", 55000, 7)
print("Getting Salary: ", e.get_salary())
e.get_info()
