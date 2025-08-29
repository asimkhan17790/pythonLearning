set = {3, 4, 5, 12}
set.add(32)


# print(set, type(set))
# print(set.__contains__(444))
if (not set.__contains__(444)):
    # print("444 not found")
    pass
else:
    pass
    # print("444 is found")

setCopy = set.copy()
print("Copy of set: ", setCopy)
print(set == setCopy)
set.remove(3)
print(set == setCopy)

try:
    set.remove(11)
except KeyError:
    print("Element not found")
print(f"set after element removal {set}")

################
# SET OPERATIONS
################

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9}

print(set1.difference(set2))
print(set2.difference(set1))

print("Intersection: ", set & set2)
print("Union: ", set.union(set2))


set1.intersection_update(set2)
print("Intersection Update", set1)

set1.add(44)
set1.difference_update(set2)
print("difference Update", set1)
