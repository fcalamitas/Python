#This first part is a tutorial for the user on how the calculator works.
print("Welcome to Fiori's Calculator")
print("=========================Tutorial=========================")
print("Operations:")
print("- Sum: Type '+' to sum")
print("- Subtraction: Type '-' to subtract")
print("- Multiplication: Type '*' to multiply")
print("- Division: Type '/' to divide")
print("- Percentage: Type %")
print("- Squareroot: Type @")
print("- Clean: Type 'C'")
print("- Type '=' to show the result")
print("- Type 'M' to see the value of memory")
print("- Type 'M+' to sum/add a number in the memory")
print("- Type 'M-' to subtract at the memory" )
print("- Type 'MC' to clean the memory")
print("Obs: Type 'out' in any moment to leave of calculator")
#========================================================================================
#Declaring the memory variable that will store the values used in the memory operations.
#========================================================================================
memory = 0 
#=================================================================================================
# This entire loop handles setting up the "number1" variable.
# It checks if the user's input is the exit command; if so, SystemExit.
# It also tries to convert the value to a float. If it fails, it's invalid and loops back.
# If it successfully converts to a float, it just breaks the loop and carries on with the code.
#=================================================================================================
while True:
    number1 = input("Number 1:").strip().lower()
    if number1 == "out":
        print("Thanks for using Fiori's calculator")
        raise SystemExit
    try:
        number1 = float(number1)
        break
    except ValueError:
        print("Please type a valid number")
#===========================================================================================================
# This whole loop is responsible for setting up the "operation" variable.
# It's made up of a bunch of "if" and "elif" statements covering all the calculator's operations.
# The if/elif blocks for +, -, *, / and % have another loop nested inside them.
# That nested loop handles the "number2" variable.
# Just like the "number1" loop, it checks if the user entered a command to quit.
# It also tries to cast the input to a float.
# However, there's a difference inside this "number2" loop: the 'm' (memory) operations.
# The 'm' operations for "number1" are applied in the main loop.
# Since this is a massive loop, I'll comment it bit by bit.
# The logic is exactly the same for +, -, *, / and @, so I'll just explain it on the + block.
#===========================================================================================================
while True:
    operation = input("Operation or M operations:\n").strip().lower()
    if operation == "+":
        while True:
            number2 = input("Number2:\n").strip().lower()
            if number2 == "out":
                print("Thans for using Fiori's calculator")
                raise SystemExit
            #===============================================================================================
            #Since the clear option is available, it needs to be applied now to clear the variable number1.
            #===============================================================================================
            if number2 == "c":
                number1 = 0
                print(f"{number1}")
                break
            try:
                number2 = float(number2)
                #=====================================================================================================================
                #This is the loop responsible for the m operations; it checks what the user wants to do before displaying the result.
                #=====================================================================================================================
                while True:
                    choice = input("= or M operations:\n").strip().lower()
                    if choice == "m+":
                        memory = memory + number2
                        print(f"M:{memory}")
                    elif choice == "m-":
                        memory = memory - number2
                        print(f"M:{memory}")
                    elif choice == "mc":
                        memory = 0
                        print(f"M:{memory}")
                    elif choice == "m":
                        number2 = memory
                        print(f"M:{memory}")
                    elif choice == "=":
                        break
                    elif choice == "out":
                        print("Thank's for using Fiori's calculator")
                        raise SystemExit
                    elif choice not in ["m+","m-","mc","m","=","out"]:
                        print("Please try a valid input.")
                        continue
                break
            except ValueError:
                print("Please type a valid input")
        if number2 == "c":
            continue
        #======================
        #Finally the operation
        #======================
        number1 = number1 + number2 
        print(f"{number1}")
    elif operation == "-":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thank for using Fiori's calculator")
                raise SystemExit
            if number2 == "c":
                number1 = 0
                print(f"{number1}")
                break
            try:
                number2 = float(number2)
                while True:
                    choice = input("= or M operations:\n").strip().lower()
                    if choice == "m+":
                        memory = memory + number2
                        print(f"M:{memory}")
                    elif choice == "m-":
                        memory = memory - number2
                        print(f"M:{memory}")
                    elif choice == "mc":
                        memory = 0
                        print(f"M:{memory}")
                    elif choice == "m":
                        number2 = memory
                        print(f"M:{memory}")
                    elif choice == "=":
                        break
                    elif choice == "out":
                        print("Thank's for using Fiori's calculator")
                        raise SystemExit
                    elif choice not in ["m+","m-","mc","m","=","out"]:
                        print("Please try a valid input.")
                        continue
                break
            except: 
                print("Please type a valid input")
        if number2 == "c":
            continue
        number1 = number1 - number2 
        print(f"{number1}")
    elif operation == "*":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thanks for using Fiori's calculator")
                raise SystemExit
            if number2 == "c":
                number1 = 0
                print(f"{number1}")
                break
            try:
                number2 = float(number2)
                while True:
                    choice = input("= or M operations:\n").strip().lower()
                    if choice == "m+":
                        memory = memory + number2
                        print(f"M:{memory}")
                    elif choice == "m-":
                        memory = memory - number2
                        print(f"M:{memory}")
                    elif choice == "mc":
                        memory = 0
                        print(f"M:{memory}")
                    elif choice == "m":
                        number2 = memory
                        print(f"M:{memory}")
                    elif choice == "=":
                        break
                    elif choice == "out":
                        print("Thank's for using Fiori's calculator")
                        raise SystemExit
                    elif choice not in ["m+","m-","mc","m","=","out"]:
                        print("Please try a valid input.")
                        continue
                break
            except:
                print("Please type a valid number")
        if number2 == "c":
            continue
        number1 = number1 * number2
        print(f"{number1}")
    elif operation == "/":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thanks for using Fiori's calculator")
                raise SystemExit
            if number2 == "c":
                number1 = 0
                print(f"{number1}")
            try:
                number2 = float(number2)
                while True:
                    choice = input("= or M operations:\n").strip().lower()
                    if choice == "m+":
                        memory = memory + number2
                        print(f"M:{memory}")
                    elif choice == "m-":
                        memory = memory - number2
                        print(f"M:{memory}")
                    elif choice == "mc":
                        memory = 0
                        print(f"M:{memory}")
                    elif choice == "m":
                        number2 = memory
                        print(f"M:{memory}")
                    elif choice == "=":
                        break
                    elif choice == "out":
                        print("Thank's for using Fiori's calculator")
                        raise SystemExit
                    elif choice not in ["m+","m-","mc","m","=","out"]:
                        print("Please try a valid input.")
                        continue
                break
            except:
                print("Please type a valid input")
        if number1 == "c":
            continue
        number1 = number1 / number2
        print(f"{number1}")
    elif operation == "%":
        while True:
            number2 = input("\n")
            if number2 == "out":
                print("Thanks for using FIori's calculator")
                raise SystemExit
            if number2 == "c":
                number1 = 0
                print(f"{number1}")
            try:
                number2 = float(input("\n"))
                while True:
                    choice = input("= or M operations:\n").strip().lower()
                    if choice == "m+":
                        memory = memory + number2
                        print(f"M:{memory}")
                    elif choice == "m-":
                        memory = memory - number2
                        print(f"M:{memory}")
                    elif choice == "mc":
                        memory = 0
                        print(f"M:{memory}")
                    elif choice == "m":
                        number2 = memory
                        print(f"M:{memory}")
                    elif choice == "=":
                        break
                    elif choice == "out":
                        print("Thank's for using Fiori's calculator")
                        raise SystemExit
                    elif choice not in ["m+","m-","mc","m","=","out"]:
                        print("Please try a valid input.")
                        continue
                break
            except: 
                print("Please type a valid input")
        if number2 == "c":
            continue
        number1 = number1 * (number2/100)
        print(f"{number1}")
    #================================================================================
    #To perform a square root operation, simply raise the value to the power of 0.5.
    #================================================================================
    elif operation == "@":
        number1 = number1 ** 0.5
        print(f"{number1}")
    #======================================
    #Function clear to "number1" directly
    #=====================================
    elif operation == "c":
        number1 = 0
        continue
    elif operation == "out":
        break
    #=============================
    #Block of m operation
    elif operation == "m+":
        memory = memory + number1
        print(f"M:{memory}")
    elif operation == "m-":
        memory = memory - number1
        print(f"M:{memory}")
    elif operation == "mc":
        memory = 0
        print(f"M:{memory}")
    elif operation == "m":
        number1 = memory
        print(f"M:{memory}")
    #=============================
    elif operation not in ["+", "-", "*", "/","%", "@","c","out","m+","m-","mc","m"]:
        print("Please type a valid input")
print("Thanks for using Fiori's calculator")