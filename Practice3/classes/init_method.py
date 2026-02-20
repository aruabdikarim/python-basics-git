# Class with constructor (__init__)
class Student:

    # Constructor initializes instance variables
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Instance method
    def show_info(self):
        print(self.name, "has grade", self.grade)

student1 = Student("Asyl", 90)
student2 = Student("Dana", 85)

student1.show_info()
student2.show_info()