class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

name = input("Enter student name: ")
age = int(input("Enter student age: "))
Student(name, age).display()
