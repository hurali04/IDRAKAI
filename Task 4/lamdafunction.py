from functools import reduce
x = lambda x: x**2
print(x(9))  
e = lambda e: print("Even") if e % 2 == 0 else print("Odd")
e(9)  
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print("Squared Numbers are:", squared)  

product = reduce(lambda x, y: x * y, nums)
print("Product of numbers:", product)  
