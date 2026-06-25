# Import the math module for scientific calculations
import math

# Run the calculator continuously until the user chooses to exit
while True:
    print("\n===== Scientific Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log")
    print("11. Natural Log")
    print("12. Percentage")
    print("13. Factorial")
    print("14. Round Number")
    print("15. Exit")

    # Ask the user to choose an operation
    choice = input("Enter your choice (1-15): ")

    if choice == "15":
        print("Thank you for using the Scientific Calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]:
        print("Invalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice in ["1", "2", "3", "4", "5"]:
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

    if choice == "1":
        # Perform addition
        print("Result:", num1 + num2)

    elif choice == "2":
        # Perform subtraction
        print("Result:", num1 - num2)

    elif choice == "3":
        # Perform multiplication
        print("Result:", num1 * num2)

    elif choice == "4":
        # Perform division:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Cannot divide by zero.")

    elif choice == "5":
        # Calculate power
        print("Result:", num1 ** num2)

    elif choice == "6":
        #Calculate square root
        if num1 >= 0:
            print("Result:", math.sqrt(num1))
        else:
            print("Error! Cannot find square root of a negative number.")

    elif choice == "7":
        # Calculate sine
        print("Result:", math.sin(math.radians(num1)))

    elif choice == "8":
        # Calculate cosine
        print("Result:", math.cos(math.radians(num1)))

    elif choice == "9":
        # Calculate tangent
        print("Result:", math.tan(math.radians(num1)))

    elif choice == "10":
        # Calculate base-10 logarithm
        if num1 > 0:
            print("Result:", math.log10(num1))
        else:
            print("Error! Log is only defined for positive numbers.")

    elif choice == "11":
        # Calculate natural logarithm
        if num1 > 0:
            print("Result:", math.log(num1))
        else:
            print("Error! Natural log is only defined for positive numbers.")

    elif choice == "12":
        # Convert the number to a percentage
        print("Result:", num1 / 100)

    elif choice == "13":
        # Calculate factorial
        if num1 >= 0 and num1.is_integer():
            print("Result:", math.factorial(int(num1)))
        else:
            print("Error! Factorial is only defined for non-negative integers.")

    elif choice == "14":
        # Round the number to a specified number of decimal places
        try:
            decimal_places = int(input("Enter number of decimal places: "))
            print("Result:", round(num1, decimal_places))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue