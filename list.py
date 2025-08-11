import random

rand_list = [random.randint(-50, 100) for _ in range(20)]
print("List of 20 random integers:", rand_list)

print("First 10 elements:", rand_list[:10])
print("Last 5 elements:", rand_list[-5:])

even_list = [el for el in rand_list if el % 2 == 0]
print("List of even numbers:", even_list)

positive_sorted_list = sorted([el for el in rand_list if el >= 0])
print("Positive numbers sorted:", positive_sorted_list)

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]
print("3x3 Matrix:", matrix)

flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)

people = [("Ali", 25), ("Zara", 19), ("Fahad", 30), ("Hina", 22)]
print("Original list of people:", people)

sorted_people = sorted(people, key=lambda x: x[1])
print("Sorted by age:", sorted_people)
