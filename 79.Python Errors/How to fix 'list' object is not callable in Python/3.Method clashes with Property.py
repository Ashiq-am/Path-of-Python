class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def marks(self):
        return self.marks

student = Student("Lalit", [95, 67, 81, 64, 87])
# Generates the error
print(student.marks())
