# Command Utility Tool Example
# os, shutil, argparse are all built in modules
#
#
import argparse

if __name__ == "__main__":
    # This block ensures that the code inside it only runs
    # when the script is executed directly (not when imported as a module).

    parser = argparse.ArgumentParser(description="Simple Calculator")

    parser.add_argument("num1", type=float, help="First Number")
    parser.add_argument("num2", type=float, help="Second Number")

    parser.add_argument("operation", choices=[
                        "add", "sub", "div", "mul"], help="Operation to perform")

    args = parser.parse_args()

    print(args)

    if (args.operation == "add"):
        print(f"The result is: {args.num1 + args.num2}")
    elif (args.operation == "mul"):
        print(f"The result is: {args.num1 * args.num2}")
    elif (args.operation == "sub"):
        print(f"The result is: {args.num1 - args.num2}")
    elif (args.operation == "div"):
        print(f"The result is: {args.num1 / args.num2}")
    else:
        print("Wrong input provided!!")
