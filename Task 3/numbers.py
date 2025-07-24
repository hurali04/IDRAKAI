number_list = input("Enter numbers separated by space: ")
numbers = [int(num) for num in number_list.split()]
unique_numbers = list(set(numbers))
even_numbers = [num for num in unique_numbers if num % 2 == 0]
odd_numbers = [num for num in unique_numbers if num % 2 != 0]
square_odd = [num ** 2 for num in odd_numbers]
print("Unique numbers:", unique_numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Squares of odd numbers:", square_odd)
