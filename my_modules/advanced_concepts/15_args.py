# similar to String ...s in JAVA - function receiving multiple number inputs

def sum(*inputs):
    total = 0
    for item in inputs:
        total += item
    return total


def product(*args):
    p = 1
    for item in args:
        p *= item
    return p


print(sum(45, 5, 6))
print(sum(45, 5, 6, 56, 43, 6))

print(product(1, 2, 3))
print(product(10, 10, 20))
