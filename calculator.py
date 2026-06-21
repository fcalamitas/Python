#Hi everone, i dont't speak english, but a will try my best. 
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
    number1 = input("Number 1:").strip().lower()
    if number1 == "out":
        print("Thanks to use Fiori's calculator")
        raise SystemExit
    try:
        number1 = float(number1)
        break
    except ValueError:
        print("Please type a valid number")
        break
while True:
    operation = input("Operation:\n").strip().lower()
    if operation == "+":
        while True:
            number2 = input("\n").strip()
            if number2 == "out":
                print("Thans to use Fiori's calculator")
                raise SystemExit
            try:
                number2 = float(number2)
                break
            except ValueError:
                print("Please type a valid input")
        number1 = number1 + number2 
        print(f"{number1}")
    elif operation == "-":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thank to use Fiori's calculator")
                raise SystemExit
            try:
                number2 = float(number2)
                break
            except: 
                print("Please type a valid input")
        number1 = number1 - number2 
        print(f"{number1}")
    elif operation == "*":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thanks to use Fiori's calculator")
                raise SystemExit
            try:
                number2 = float(number2)
                break
            except:
                print("Please type a valid number")
        number1 = number1 * number2
        print(f"{number1}")
    elif operation == "/":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thanks to use Fiori's calculator")
                raise SystemExit
            try:
                number2 = float(number2)
                break
            except:
                print("Please type a valid input")
        number1 = number1 / number2
        print(f"{number1}")
    elif operation == "%":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thanks to use FIori's calculator")
                raise SystemExit
            try:
                number2 = float(input("\n"))
                break
            except: 
                print("Please type a valid input")
        number1 = number1 * (number2/100)
        print(f"{number1}")
    elif operation == "@":
        number1 = number1 ** 0.5
        print(f"{number1}")
    elif operation == "out":
        break
    elif operation not in ["+", "-", "*", "/","out"]:
        print("Please type a valid input")
print("Thanks to use Fiori's calculator")
#The next objective is to add the function 'Clean' at the calculator