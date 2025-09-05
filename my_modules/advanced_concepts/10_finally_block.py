def divide(a, b):
    try:
        c = a/b
        print("Inside function result:", c)
        return c
    except Exception as e:
        print(e)
        return None
    finally:
        print("Finally is always executed")


a = int(input("Enter 1st no. :"))
b = int(input("Enter 2nd no. :"))

print("Caller print:", divide(a, b))
