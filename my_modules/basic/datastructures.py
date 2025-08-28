# Lists
# Tuples
# Sets
# Dictionaries


# Lists - ordered, mutable collection of items
marks = [1, 2, 3, 4]

mixed = [34, 1, "Hello", False]

print(mixed[2])

# Slicing a list
print(mixed[1:4])


# Common list methods

mixed.clear()
print(mixed)
mixed.append(1)
print(mixed)
mixed.extend([2, 3, 4, 5, 1, 1, 1])
print(mixed)


mixed.insert(len(mixed)-1, 22)

print(mixed)
print(mixed.count(1))


# List Comprehension


# Tedious  way to create a list
table = []
for i in range(1, 11):
    table.append(5*i)

print(table)

# Shortcut way / List comprehension


def test(x): return x*5


table2 = [test(i) for i in range(1, 11)]

print(table2)


list = [1, 2, 3]

x, y, z = list

print(f"X is {x}, Z is {z}")

list.insert(len(list), 44)
print(list)

# Tuples

tuple = (1, 2, 3)
print(tuple[0])

# A Comma is aways required in the end if you wish to create a tuple with single element

singleTuple = (4,)
print(singleTuple[0])

# Assiging variables to individual values of tuples. This I could do on the list elements too
tu = (3, 2, 4)

a, b, c = tu

print(f"Tuple elements are : {a} {b} {c}")


# tuples operations - only read only functions available
tu = (1, 5, 6, 4, 6, 44, 5, 66, 33, 23, 6, 6,)
print(tu.count(6))

print(len(tu))

try:
    print(tu.index(12))
except ValueError:
    print("Value not found")
