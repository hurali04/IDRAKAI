name=input("Enter Your Name: ")
age=int(input("Enter your age: "))
fav_lang=input("Enter your language: ")

with open(" profiles.txt","a")as file:
    file.write(f"{name} , {age} , {fav_lang}")

print("All Profile:\n")
with open(" profiles.txt","r")as file:
    lines=file.readlines()
    for line in lines:
        print(line.strip())