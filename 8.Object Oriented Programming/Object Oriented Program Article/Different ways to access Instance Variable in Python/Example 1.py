# creating class
class student:

    # constructor
    def __init__(self, name, rollno):
        # instance variable
        self.name = name
        self.rollno = rollno

    def display(self):
        # using self to access
        # variable inside class
        print("hello my name is:", self.name)
        print("my roll number is:", self.rollno)


# Driver Code
# object created
s = student('HARRY', 1001)

# function call through object
s.display()

# accessing variable from
# outside the class
print(s.name)
