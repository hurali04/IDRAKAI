import json
data='{"Name":"Syed Muhammad Hur Ali","Age":"21","city":"Islamabad"}'
data_print=json.dumps(data)
print(data_print)

Name=input("Enter student Name: ")
Age=int(input("Enter Student's Age: "))
City=input("Enter City: ")

data1={"Name":Name,"Age":Age,"city":City}
with open("student_data","w")as file:
    json.dump(data1,file)

