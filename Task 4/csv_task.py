import csv
data = [
    ["Name", "Marks"],
    ["Ali", 85],
    ["Sara", 92],
    ["Usman", 78],
    ["Zainab", 88]
]
with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created: students.csv")

# Read and analyze CSV file
with open("students.csv", "r") as file:
    reader = list(csv.reader(file))
    
    row_count = len(reader) - 1
    print("Total students:", row_count)

    marks = [int(row[1]) for row in reader[1:]]
    print("Marks:", marks)

    print("Highest marks:", max(marks))