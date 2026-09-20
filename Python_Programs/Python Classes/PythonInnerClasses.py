class Student:
    def __init__(self, name):
        self.name = name

    class Details:
        def __init__(self, course):
            self.course = course

student = Student(input("Enter student name: "))
details = Student.Details(input("Enter course: "))
print("Name:", student.name)
print("Course:", details.course)
