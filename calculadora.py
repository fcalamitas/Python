print("Welcome to Fiori's Calculator")
print("=====Tutorial=====")
print("Operations:")
print("- Sum: Type '+' to sum")
print("- Subtractio: Type '-' to subtract")
print("- Multiplication: Type '*' to multiply")
print("- Division: Type '/' to divide ")
print("- Percentage: Type %")
print("- Squareroot: Type @")
print("Obs: Type 'out' in any moment to leave of calculator")
while True:
    try:
        number1 = float(input("Number 1:"))
        break
    except ValueError:
        print("Please type a valid number")
        break
while True:
    operation = input("Operation:\n")
    if operation == "+":
        while True:
            try:
                number2 = float(input("\n"))
                break
            except ValueError:
                print("Please type a valid input")
                break
        number1 = number1 + number2 
        print(f"{number1}")
    elif operation == "-":
        while True:
            try:
                number2 = float(input("\n"))
                break
            except: 
                print("Please type a valid input")
                break
        number1 = number1 - number2 
        print(f"{number1}")
    elif operation == "*":
        while True:
            try:
                number2 = float(input("\n"))
                break
            except:
                print("Please type a valid number")
        number1 = number1 * number2
        print(f"{number1}")
    elif operation == "/":
        while True:
            try:
                number2 = float(input("\n"))
                break
            except:
                print("Please type a valid input")
                break
        number1 = number1 / number2
        print(f"{number1}")
    elif operation == "%":
        while True:
            try:
                number2 = float(input("\n"))
                break
            except: 
                print("Please type a valid input")
                break
        number1 = number1 * (number2/100)
        print(f"{number1}")
    elif operation == "@":
        number1 = number1 ** 0.5
        print(f"{number1}")
    elif operation == "out":
        break
    elif operation not in ["+", "-", "*", "/","out"]:
        print("Please type a valid input")
        break
print("Thanks to use Fiori's calculator")