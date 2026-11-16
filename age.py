def greet():
    print("hello")
greet()

def show():
    return 100
show()

def add(a,b):
    return a+b  
result = add(10,20)
print(result)

fruits =["apple","mango"]
print("mango" in fruits)
print("mango" not in fruits)

a={1,2,3,4,4,5}
a.add(6)
a.remove(2)
a.remove(7)
print(a)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')

    def study(self, subject):
        print(f'{self.name} is studying {subject}')

