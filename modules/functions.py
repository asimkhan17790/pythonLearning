"""Functions testing"""


def average(a, b, c):
    """Return average"""
    return (a+b+c)/3


def sayHello(text, addressee="World!!"):
    print(f"""Hello {addressee},
Your Text here--> {text}""")


sayHello(addressee="Asim", text="Whats up?")

# print(average(2, 2, 2))

# Lambda Functions
print("Lambda Functions\n\n\n")


def square(x): return x*x


def multiply(x, y): return x*y


print(square(5))
print(multiply(5, 2))

print(lambda x, y: x*y)

# Recursion


def fibonacci(x):
    if (x == 0):
        return 0
    if (x == 1):
        return 1
    return fibonacci(x-1)+fibonacci(x-2)


# print(fibonacci(6))


# Fibonacci iterative
x = "Test"

print("X is: ", x)

# Do not update global variables inside functions


def fibo(num):

    a = 0
    b = 1
    # sum = 0
    for i in range(2, num+1):
        sum = (a+b)
        a = b
        b = sum
    return sum


print(fibo(6))
