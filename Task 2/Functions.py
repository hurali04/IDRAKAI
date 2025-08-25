def get_marks():
    marks = []
    for i in range(3):
        mark = float(input(f"  Enter mark for subject {i+1}: "))
        marks.append(mark)
    return marks

def average(marks):
    return sum(marks) / len(marks)

def main():
    students = []

    for i in range(5):
        print(f"\nStudent {i+1}")
        marks = get_marks()
        avg = average(marks)
        students.append([marks, avg])
        
    students.sort(key=lambda x: x[1], reverse=True)

    print("\nSorted Students by Average Marks:")
    for i, (marks, avg) in enumerate(students, 1):
        print(f"Student {i}: Marks = {marks}, Average = {avg:.2f}")

main()
