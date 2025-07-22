def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)

def factorial():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial:", fact)


def reverse_string():
    text = input("Enter a string: ")
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    print("Reversed:", reversed_text)


while True:
    print("\n=== MENU ===")
    print("1. Add two numbers")
    print("2. Find factorial of a number")
    print("3. Reverse a string")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    match choice:
        case "1":
            add_numbers()
        case "2":
            factorial()
        case "3":
            reverse_string()
        case "4":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
