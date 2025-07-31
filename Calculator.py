while True:
    # Get input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the operation and store result
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero!")
            continue
    else:
        print("Invalid operation!")
        continue

    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

    # Ask if the user wants to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Goodbye!")
        break