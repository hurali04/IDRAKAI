while True:
    num1 = int(input("Enter first number: "))
    op = input("Enter operation (+, -, x, /, or type 'exit' to quit): ")

    if op == 'exit':
        print("Calculator closed.")
        break

    if op != '+' and op != '-' and op != 'x' and op != '/':
        print("Invalid operator")
        continue

    num2 = int(input("Enter second number: "))

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == 'x':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", num1 / num2)
