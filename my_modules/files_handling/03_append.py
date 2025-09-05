# Append to a file

f = open("SN.txt", "a")
str = """
Asim misses SN
"""
f.write(str)
f.close()
print("Append complete")
