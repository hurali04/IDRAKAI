number = int(input("Enter a number: "))
digits = str(number)
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if total == number:
    print("It is an Armstrong number.")
else:
    print("It is NOT an Armstrong number.")
