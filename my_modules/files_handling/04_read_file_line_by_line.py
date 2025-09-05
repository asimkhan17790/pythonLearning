try:
    file = open("SN.txt", "r")
    for line in file:
        print(f"**{line.strip()}**")
    file.close()
except FileNotFoundError as e:
    print("FILE NOT Found", e)
