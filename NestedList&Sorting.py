def input_marks():
    students = []
    for i in range(5):
        print(f"\nEnter marks for Student {i+1}:")
        s1 = int(input("Subject 1: "))
        s2 = int(input("Subject 2: "))
        s3 = int(input("Subject 3: "))
        avg = (s1 + s2 + s3) / 3
        students.append([s1, s2, s3, avg])
    return students

def sort_students(students):
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            if students[i][3] < students[j][3]:
                students[i], students[j] = students[j], students[i]
    return students

def display_students(students):
    print("\nStudents sorted by average marks:")
    i = 0
    while i < len(students):
        student = students[i]
        print("Student", i + 1, ": Marks =", student[:3], "Average =", round(student[3], 2))
        i += 1

data = input_marks()
sorted_data = sort_students(data)
display_students(sorted_data)
