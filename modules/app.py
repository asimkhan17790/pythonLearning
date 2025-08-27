import math
name = "Asim"
temp = 25

# # if (temp > 30):
# #     print("Hot")
# # elif (temp < 15):
# #     print("Cold")
# # else:
# #     print("Go Play!")

# age = 22
# if (age >= 18):
#     print("Eligible")
# else:
#     print("Not Eligible")

# # Similar to ternary operator ?: in java
# message = "Yes, can drink!!" if age >= 18 else "Sorry! Cant drink..."
# print(message)

# # logical operators

# # and
# # or
# # not

# # high_income = True
# # good_credit = True
# # student = False

# # if (high_income and (good_credit or student)):
# #     print("Eligible For Loan")
# # else:
# #     print("Not Eligible for Loan")

# # print("Done")


# # Short form for conditions
# # Chaining comparison operators
# # age = 22

# # if (18<=age<50):
# #     print("Young Lad")
# # else:
# #     print("Old")


# # LOOPS

# # name = "ASIM KHAN"
# # for i in range(len(name)):
# #     print(f"char:{i}  value:{name[i]}")

# # for i in range(10):
# #     print("." * (i+1))


# # for i in range(1, 10, 2):
# #     print("*" * i, end=" ")

# # print("DONE")

# # For else block
# success = False

# for num in range(3):
#     print("Attempt")
#     if (success):
#         print("Success")
#         break
# else:
#     print("Attempted 3 times but failed")


# #
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# x = ["asa", 12]
# count = 0
# for i in x:
#     print(type(i))
#     if (type(i) == str):
#         x[count] = i + " Hello"
#     count += 1

# print(x)

# Tuples cannot be mdodified while lists can be updated

# i = 100
# while (i > 0):
#     print(i, end=" ")
#     i -= 1

# command = ""
# while (True):
#     command = input(">>>>>>>")
#     if (command.lower() == "quit"):
#         print("User asked to Quit")
#         break†
#     print(f"User input: {command}")

# count=0    
# for i in range(2,10,2):
#     print(str(i) + " ")
#     count+=1
# print(f"We have {count} even numbers")

count=0
for i in range(1,10):
    if (i%2==0):
        count+=1
        print(i, end= " ")
print()
print(f"We have {count} even numbers...")