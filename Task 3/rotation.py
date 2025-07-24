lst = [1, 2, 3, 4]
k=int(input("Enter number of steps to rotate: "))
first_part = lst[k:]      
second_part = lst[:k]     
rotated = first_part + second_part
print(rotated)
