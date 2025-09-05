class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_first_name(self):
        return self.name.split(" ")[0]

    def set_first_name(self, new_first_name):
        l = self.name.split(" ")
        new_name = f"{new_first_name} {l[1]}"
        self.name = new_name


e = Employee("Jack Khan", 75000)
e.projects = 6
print(f"Projects: {e.projects}")


print(f"Current First name: {e.get_first_name()}")
print(f"Current Full Name: {e.name}")

print("Updating Name to Asim: ")

e.set_first_name("Asim")
print("Now the full name is :", e.name)

# Property decorator
