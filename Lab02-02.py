class Student:
    def data(self):
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
    def display(self):
        print(self.name)
        print(self.age)
        
s1=Student()
s1.data()
s1.display()

class TimeTable:
    def data(lecture):
        lecture.first=input("1st lecture: ")
        lecture.name=input("Name of faculty: ")
    def display(lecture):
        print(lecture.first)
        print(lecture.name)


s1=TimeTable()
s1.data()
s1.display()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name, self.age)
        
s1=Student("Muskan", 18)
s2=Student("Tanishka", 15)
s3=Student("Mahi", 10)
s4=Student("Ira", 8)
s5=Student("Kia", 21)

class Faculty:
    def __init__(self,name,subject,salary):
        self.name=name
        self.subject=subject
        self.salary=salary
        print(self.name, self.subject, self.salary)
    def greet(self):
        print("Good Morning!", self.name)

s1=Faculty("Muskan", "PAI", 7362467845)
s1.greet()

class Add:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)

a1=Add()
a1.add(65,54)

class Add:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)

a1=Add(356,678)