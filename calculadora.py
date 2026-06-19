while True:
    operation = input("Operation:\n")
    if operation == "+":
        number2 = float(input("\n"))
        number1 = number1 + number2 
        print(f"{number1}")
    elif operation == "-":
        number2 = float(input("\n"))
        number1 = number1 - number2 
        print(f"{number1}")
    elif operation == "*":
        number2 = float(input("\n"))
        number1 = number1 * number2
        print(f"{number1}")
    elif operation == "/":
        number2 = float(input("\n"))
        number1 = number1 / number2
        print(f"{number1}")
    elif operation or number1 or number2 == "out":
        break
    elif operation != "+" or "-" or "*" or "/" or "out":
        print("Please type a valid input")
        break