# Strings

a = [1, 2, 3]

print(a[-1])


print("String Slicing")

name = "AsimKhan123456789"

print(name[0:-1])

print(name[0:10])
print(name[0:10:2])

print(name[0:])
print(name[:5])

print("String methods")

# Strings are immutable in Python as well
# That is why we have few string methods

name = "asim khan"
a = len(name)
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

TEXT = "Apples,Bananas,Pineapples"
print(TEXT.split(","))

print("|".join(["Apple", "Bananas", "Oranges"]))


print(type(3.2))
print(type('A'))


# GEtting  ascii value
print(ord('A'))

# Getting char value from asccii

print(chr(65))
print(chr(97))

test = "**AsimKHan**.     "
print(test.strip("%"))

print(test.find('A'))
