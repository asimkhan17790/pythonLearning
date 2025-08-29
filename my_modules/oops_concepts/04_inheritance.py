class Animal:
    country = "Australia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...", end=" ")


class Dog(Animal):
    country = "India"  # Class attribute is shadowed by the child class so India will be printed

    def speak(self):
        super().speak()
        print("Woof!!")


class Cat(Animal):
    def speak(self):
        print("Meow!!")


# a = Animal("Dog")
# a.speak()

d = Dog("Bruno")
d.speak()
d.country = "Nepal"
# Instance just creates an instance attribute with same name as class attribute (Shadows)
print("Bruno Country:", d.country)

print("Dog class country: ", Dog.country)

c = Cat("Kitty")
c.speak()
