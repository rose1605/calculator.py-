def basic_calculator():
    print("Welcome to the basic calculator!")

    # Get user input for numbers and operator
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        elif operator == "%":
            result = num1 % num2
        else:
            print("Invalid operator. Please use one of +, -, *, /, %.")
            return

        # Display the result
        print(f"The result of {num1} {operator} {num2} is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")


# Run the calculator
basic_calculator()
