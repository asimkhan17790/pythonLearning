def print_operation_messages():
    print("\n==============================")
    print("     Simple Calculator")
    print("==============================")
    print("Select an operation:")
    print("  +   Addition")
    print("  -   Subtraction")
    print("  *   Multiplication")
    print("  /   Division")
    print("==============================\n")


def initalize_calculator():
    try:
        a = int(input("Enter 1st number:"))
        b = int(input("Enter 2nd number:"))
        print_operation_messages()
        o = input("Enter Operation: ")
        match o:
            case "+":
                print(f"Result is : {a + b}")
            case "-":
                print(f"Result is : {a - b}")
            case "*":
                print(f"Result is : {a * b}")
            case "/":
                try:
                    print(f"Result is : {a / b}")
                except ZeroDivisionError as ee:
                    print("Cannot divide by ZERO")
            case default:
                print(f"There was an error")
    except Exception as e:
        print("Enter Valid Value for a and b", e)


if __name__ == "__main__":
    initalize_calculator()
