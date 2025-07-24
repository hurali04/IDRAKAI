def factorial(number):
    if(number<0):
        return 1
    if(number==0 or number==1):
        return 1
    result=number*factorial(number-1)
    return result
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


number=int(input("Enter an integer: "))
fact=factorial(number)
fib=fibonacci(number)
sum=sum_of_digits(number)

print(f"The factorial of {number} is {fact}")
print(f"The fibonacci sequence of {number} is {fib}")
print(f"Sum of {number} is {sum}")