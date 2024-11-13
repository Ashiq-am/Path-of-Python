# Python program to demonstrate
# classes


class Student:
    # class variable
    stream = "COE"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no


# Driver's code
a = Student("Shivam", 3425)
b = Student("Sachin", 3624)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)

# Class variables can be accessed
# using class name also
print(Student.stream)
