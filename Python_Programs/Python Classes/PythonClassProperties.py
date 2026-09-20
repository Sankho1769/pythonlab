class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

student = Student(input("Enter student name: "))
student.name = input("Enter new student name: ")
print("Name:", student.name)
