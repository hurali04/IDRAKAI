student_data={'Hina':85 , 'Mahnoor':80 , 'Fahad': 75 ,'Asad':71,'Hamza':68}
student_data['Ali Ahsan']=65
maximum=max(student_data,key=student_data.get)
minimum=min(student_data,key=student_data.get)
average=sum(student_data.values())/len(student_data)
print("Maximum Number:", maximum)
print("Minimum Number:", minimum)
print("Average Number:", average)
nested = {
    'Ali': {'Math': 85, 'English': 78, 'Science': 90},
    'Sara': {'Math': 92, 'English': 88, 'Science': 95},
    'John': {'Math': 70, 'English': 72, 'Science': 75},
    'Ayesha': {'Math': 88, 'English': 90, 'Science': 84},
    'Usman': {'Math': 74, 'English': 69, 'Science': 71}
}
for name in nested:
    total = sum(nested[name].values())
    print(name, "Total Marks:", total)