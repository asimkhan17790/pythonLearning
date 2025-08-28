# Dictionaries

marks = {
    "harry": 34,
    "jack": 45,
    "lily": 66,
    45: "Hello",
    # In java we can do that by creating class for the objects and then writing compareTo() and Equals methods.
    (1, 2, 3): "Can use tuples as Keys too?? Woah!",
    (1, 2, 4): [1, 2, 3, 33]}

print(marks)
print("Lily marks:  ", marks.get("lily"))
print("45 key:  ", marks[45])

# Methods

# print(marks.keys())
# print(marks.values())
# print(marks.items())


# Keys set
for i in marks.keys():
    print(i, "->", marks[i])


# Items set
for eachItem in marks.items():
    print(eachItem[0], "----->", eachItem[1])

print("\n\n POPPING LILY ")
marks.pop("lily")
print(marks)

# Dictionary Comprehensions:

table_of_5 = {i: 5*i for i in range(1, 11)}
print(table_of_5)
