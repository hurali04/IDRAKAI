import random
numbers=[random.randint(1,101) for _ in range(10)]
print("Random Numbers from 1 to 10: ",numbers)

print("Maximum Number is: ",max(numbers))
print("Minimum Number is: ",min(numbers))
print("Average Number is: ",sum(numbers)/len(numbers))

print("Random Numbers from 1 to 10 in ascending order: ",sorted(numbers))
print("Random Numbers from 1 to 10 in descending order: ",sorted(numbers,reverse=True))

print("Removing Duplicate Values: ",list(set(numbers)))

even_numbers=[num for num in numbers if num%2==0]
print("Even Numbers are: ",even_numbers)