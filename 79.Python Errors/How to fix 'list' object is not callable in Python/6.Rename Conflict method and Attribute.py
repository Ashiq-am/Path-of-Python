class Student:
    def __init__(self, name, marks):
        self.name = name
        # Change the property name to _marks
        self._marks = marks
    # Rename the method to get_marks
    def get_marks(self):
        return self._marks

student = Student("Lalit", [95, 67, 81, 64, 87])
# Outputs the list of marks
print(student.get_marks())
