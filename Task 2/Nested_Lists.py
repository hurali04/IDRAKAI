students = []
for i in range(5):
    print(f"\nEnter marks for Student {i+1}:")
    marks = []
    for j in range(3):
        mark = float(input(f"  Subject {j+1}: "))
        marks.append(mark)
    avg = sum(marks) / 3
    students.append([f"Student {i+1}", marks, avg])

students.sort(key=lambda x: x[2], reverse=True)

print("\nSorted Student Results:")
for student in students:
    name, marks, avg = student
    print(f"{name} | Marks: {marks} | Average: {avg:.2f}")
