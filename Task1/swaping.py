a, b = int(input("Enter first number")), int(input("Enter second value"))
print("The values before swapping", a, b)
a = a ^ b
b = a ^ b
a = a ^ b
print("The values after swapping", a, b)
