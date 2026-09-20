class Student:
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student = Student()
student.name = input("Enter student name: ")
student.age = int(input("Enter student age: "))
student.display()
