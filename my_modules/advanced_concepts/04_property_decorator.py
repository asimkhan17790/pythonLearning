class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        return self.name.split(" ")[0]

    @first_name.setter
    def first_name(self, new_first_name):
        l = self.name.split(" ")
        new_name = f"{new_first_name} {l[1]}"
        self.name = new_name


e = Employee("Asim Khan", 180000)
print(e.first_name)
e.first_name = "JACK"
print(e.first_name)

print(e.name)
