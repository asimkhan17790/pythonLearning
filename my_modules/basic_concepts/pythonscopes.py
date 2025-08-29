def sum(a, b):
    # a b are local variables here

    z = 1  # Local z variable
    return (a+b)


def greet():
    print("Called greet to update Global Z")
    global z
    z = 1  # Local z variable


z = 9  # Global variable

print("Initial Z: ", z)
print(sum(4, 6))
print("Z after calling sum(): ", z)

greet()
print("Z after calling greet(): ", z)
