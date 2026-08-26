print("""
================================================================================
                              CALCULATOR
================================================================================
""")

number1 = int(input("Please enter your number 1: "))
number2 = int(input("Please enter your number 2: "))

print("""
1. Addition '+'
2. Subtraction '-'
3. Multiplication '*'
4. Division '/'
""")

choice = int(input("Please select an operation (1-4): "))

if choice == 1:
    print("Result =", number1 + number2)

elif choice == 2:
    print("Result =", number1 - number2)

elif choice == 3:
    print("Result =", number1 * number2)

elif choice == 4:
    print("Result =", number1 / number2)

else:
    print("Invalid choice!")

