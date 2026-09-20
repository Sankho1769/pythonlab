class Person:
    def display_name(self, name):
        print("Name:", name)

class Student(Person):
    def display_course(self, course):
        print("Course:", course)

student = Student()
student.display_name(input("Enter name: "))
student.display_course(input("Enter course: "))
