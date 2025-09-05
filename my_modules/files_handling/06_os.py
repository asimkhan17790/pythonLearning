import os  # Module used for handling OS related operations

a = os.listdir("dir")
print(a)


# Current directory
print(os.getcwd())

print(os.path.exists("dir"))


# os.remove("dir/file1.txt")
# os.remove("dir/file2.txt")
# os.rmdir("dir")  # It can only remove folders
