# Python is a dynamically typed language
# REPL -- Read Evaluate Print Loop

# operators

a = 5
b = 2
print(a+b)
print(a*b)
print(a/b)
print(a-b)
print(a % b)
print(a//b)

# Exponents
print(a**b)


# Comparisons

# < > <= >=

print(not None)
print(not 0)
print(not "")

print(bool(None))

# Logical Operators
# and
# or
# not


# Membership operators

# in
# not in

fruits = ["apple", "banana", "orange"]
print("banana" in fruits)

# Identity Operators
x = "Asim"
y = "Asim"
print(x is y)  # returns True

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)  # returns false as both lists point to different memory locations
