import random
numbers=[random.randint(1,100) for _ in range(10)]
print("The numbers are:",numbers)
print("Maximum Number is: ",max(numbers))
print("Minimum Number is: ",min(numbers))
print("Average Number is: ",sum(numbers)/len(numbers))
print("Numbers in ascending form: ",sorted(numbers))
print("Numbers in descending form: ",sorted(numbers,reverse=True))
print("Removing Duplicates: ",set(numbers))
even_lc = [num for num in numbers if num % 2 == 0]
print("Even numbers (list comprehension):", sorted(even_lc))