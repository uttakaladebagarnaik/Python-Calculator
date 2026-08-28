print("""
================================================================================
                              CALCULATOR V2
================================================================================
""")

while True:

    print("""
1. Addition '+'
2. Subtraction '-'
3. Multiplication '*'
4. Division '/'
5. Exit
""")

    choice = int(input("Please select an operation (1-5): "))

    if choice == 5:
        print("Thank you for using the calculator!")
        break

    if choice < 1 or choice > 5:
        print("Invalid choice! Please select between 1 and 5.")
        continue

    number1 = float(input("Please enter your number 1: "))
    number2 = float(input("Please enter your number 2: "))

    if choice == 1:
        print("Result =", number1 + number2)

    elif choice == 2:
        print("Result =", number1 - number2)

    elif choice == 3:
        print("Result =", number1 * number2)

    elif choice == 4:
        if number2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result =", number1 / number2)