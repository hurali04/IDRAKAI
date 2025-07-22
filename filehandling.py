name = input("Enter your name: ")
age = input("Enter your age: ")
language = input("Enter your favorite programming language: ")


with open("profiles.txt", "a") as file:
    file.write(f"{name}, {age}, {language}\n")


print("\nAll saved profiles:")
with open("profiles.txt", "r") as file:
    for line in file:
        print(line.strip())
