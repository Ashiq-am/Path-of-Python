# Python program to demonstrate
# classes and objects


# Creating a class
class Student:
    # Class Variable
    stream = 'COE'

    def __init__(self, name, roll_no):
        # Instance Variable
        self.name = name
        self.roll_no = roll_no


# Objects of Student class
a = Student('SHIVAM', 3425)
b = Student('SACHIN', 3624)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll_no)
print(b.roll_no)

# Class variables can be
# accessed using class
# name also
print(Student.stream)
