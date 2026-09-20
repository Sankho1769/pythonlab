class Student:
    school = "Unknown"

    @classmethod
    def set_school(cls, school):
        cls.school = school

school = input("Enter school name: ")
Student.set_school(school)
print("School:", Student.school)
