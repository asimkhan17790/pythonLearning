# Writing Functions
# We have 2 types of functions
# 1 - That return a ValueError
# 2 - That do something

def greet_me(name, age=-1):
    print(f"Hello {name}... Your age is {age}")


#   2greet_me("Asim", 33)


def increment(number, by=1, printMessage=" Default Message"):
    print(printMessage)
    return number + by


# print(increment(19, printMessage="asim"))

def multiply(*nums):
    total = 1
    for n in nums:
        print(n)
        total *= n
    return total


print(f"Total: {multiply(1, 2, 3)}")
