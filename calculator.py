def calculator():
    while True:
        print("\n=== Simple Calculator ===")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the program. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        # Get the two numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Perform the chosen operation
        if choice == '1':
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division is: {result}")

# Run the calculator
calculator()