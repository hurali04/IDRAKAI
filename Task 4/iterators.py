#1
class Square:
    def __init__(self,n):
        self.n=n
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.current<=self.n):
            result=self.current**2
            self.current+=1
            return result
        else:
            raise StopIteration
n=int(input(f"Enter a number to square: "))
sq=Square(n)
for i in sq:
    print(i)

#2
nums=[1,2,3,4,5]
it=iter(nums)
print(it)

print(next(it))
print(next(it))
print(next(it))

print("\nUsing enumerate():")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

print("\nUsing zip():")
students = ['Ali', 'Sara', 'Zain']
marks = [88, 92, 79]

for student, mark in zip(students, marks):
    print(f"{student} scored {mark} marks")
