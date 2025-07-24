class Student:
    def __init__(self, name, roll_no, marks): 
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):  
        print(f"Enrolled student name: {self.name}")
        print(f"Enrolled Student Roll Number: {self.roll_no}")
        print(f"Enrolled Student Marks: {self.marks}")

    def calculate_grade(self):  
        if self.marks > 85:
            return 'A'
        elif self.marks > 79:
            return 'A-'
        elif self.marks > 74:
            return 'B+'
        elif self.marks > 70:
            return 'B'
        else:
            return 'F'

# Input and usage
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = int(input("Enter marks: "))

s = Student(name, roll_no, marks)
s.display_info()
print("Grade:", s.calculate_grade())
