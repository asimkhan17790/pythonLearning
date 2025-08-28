class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic Animal Sound")


a = Animal("Dog")
a.speak()
