string=input("Enter a string: ")
count=0
for char in string:
    if(string.count(char)>1):
        count+=1

print("Number of repeated words: ",count)