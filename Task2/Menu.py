def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", a + b)

def factorial():
    num = int(input("Enter a number: "))
    result = 1
    for i in range(2, num + 1):
        result *= i
    print("Factorial:", result)

def reverse_string():
    s = input("Enter a string: ")
    print("Reversed string:", s[::-1])

while True:
    print("\n--- Menu ---")
    print("1. Add two numbers")
    print("2. Find factorial of a number")
    print("3. Reverse a string")
    print("4. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            add_numbers()
        case "2":
            factorial()
        case "3":
            reverse_string()
        case "4":
            print("Exiting program...")
            break
        case _:
            print("Invalid choice. Try again.")
