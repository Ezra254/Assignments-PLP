while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

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

    print(f"{num1} {operation} {num2} = {result}")

    again = input("Do you want to perform another calculation? (y/n): ")
    if again != 'y':
        print("Goodbye!")
        break