while True:
    try:
        a = int(input("Enter 1st number..."))
        b = int(input("Enter 2nd number..."))
        print(f"The sum is {a+b}")
        print(f"Division result is : {a/b}")

    # Specific Exception to be put in first (Similar to JAVA)
    except ValueError as e:
        print("Only numbers are accepted...ERROR ->", e)
    except ZeroDivisionError as e:
        print("DIVISION BY ZERO ERROR OCCURRED!!", e)
    # Generic Exception to be put in last
    except Exception as e:
        print("Some Error Occurred!!", e)
