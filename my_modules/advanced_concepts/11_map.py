numbers = [1, 2, 3, 4, 5, 6]


def add_5(num):
    return num+5


square = map(lambda x: x**2, numbers)

print(list(square))

plus_five = map(add_5, numbers)
print(list(plus_five))
