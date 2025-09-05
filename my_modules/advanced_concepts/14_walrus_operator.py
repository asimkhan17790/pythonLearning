def very_slow_function():

    for i in range(1, 11):
        print("Something", "."*i, sep="")

    return 80


if ((a := very_slow_function()) > 10):
    print(a)
else:
    print("Its not greater than 10")


while (data := input("Enter value:")):
    print(data)
    if (data.lower() == "q"):
        print("Quitting")
        break
