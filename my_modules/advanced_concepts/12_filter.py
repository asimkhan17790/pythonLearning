nums = [1, 3, 4, 5, 10, 21]


def is_greater_than_9(num):
    if (num > 9):
        return True
    else:
        return False


result = filter(is_greater_than_9, nums)
print("Nums greater than 9:", list(result))

result_less_than_5 = filter(lambda x: True if x < 5 else False, nums)
print("nums less than 5:", list(result_less_than_5))
