def decorator(func):
    def wrapper():
        print("I am about execute a function...")
        func()
        print("I have executed this function..")
    return wrapper


def say_hello():
    print("Hello!!")


myFunc = decorator(say_hello)
myFunc()


print("\n")
# Better way to write Above Code


@decorator
def say_hello_2():
    print("New Hello Function called")


say_hello_2()
