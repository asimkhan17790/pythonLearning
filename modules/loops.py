for i in range(1, 11):
    print("5 x", i, "=", 5*i)


# While loops
print("WHILE LOOPS")
i = 1
while i < 6:
    print(i)
    i += 1


# Continue statement
print("using contiue")
i = 1
while (i < 10 and i < 100):
    if (i in (7, 8)):
        i += 1
        continue
    print(i)
    i += 1
