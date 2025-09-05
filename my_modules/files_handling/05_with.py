# file = open("asim.txt", "r")
# content = file.read()
# print(content)
# file.close()


with open("asim.txt", "r") as f:
    content = f.read()
    print(content)
    # NO need to write f.close as the with statement
    # automatically closes it
