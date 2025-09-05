from functools import reduce


nums = [1, 3, 4, 5, 10, 21]


def sum(a, b):
    return a+b


def minus(a, b):
    return a-b


def multiply(a, b):
    return a*b


c = reduce(sum, nums)
print(c)


c2 = reduce(minus, nums)
print(c2)
print(nums)

c3 = reduce(multiply, nums)
print(c3)

# Using Lambda

c4 = reduce(lambda a, b:  a+b, nums)
print("Sum using lambda:", c4)
