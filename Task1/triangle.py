a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if ((a+b > c) and (a+c > b) and (b+c > a)):
    print("They can form a triangle")
else:
    print("They cannot form a triangle")
