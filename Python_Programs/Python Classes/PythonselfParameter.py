class Student:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student = Student()
student.set_details(input("Enter name: "), int(input("Enter age: ")))
student.display()
