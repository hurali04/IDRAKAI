import random
student_names=["Ali","Asad","Fahad","Hamza","Abbasi"]
student_scores=[random.randint(50,100) for _ in range(5)]
highest_score=max(student_scores)
average_score=sum(student_scores)/len(student_scores)

print("Highest Score is: ",highest_score)
print("Average Score is: ",average_score)