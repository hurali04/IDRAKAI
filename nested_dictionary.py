students = {
    "Ali": {"Math": 85, "English": 78, "Science": 92},
    "Sara": {"Math": 90, "English": 88, "Science": 84},
    "Fahad": {"Math": 70, "English": 75, "Science": 80}
}

for name, subjects in students.items():
    grades = list(subjects.values())
    avg = sum(grades) / len(grades)
    best_subject = max(subjects, key=subjects.get)
    total = sum(grades)
    print(name, "Average:", avg, "Best Subject:", best_subject, "Total:", total)
