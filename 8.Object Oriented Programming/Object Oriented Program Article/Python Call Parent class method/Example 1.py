# Python program to demonstrate
# classes


class cls:

    # Constructor
    def __init__(self, fname, mname, lname):
        self.firstname = fname
        self.middlename = mname
        self.lastname = lname

    # class Function
    def print(self):
        print(self.firstname, self.middlename, self.lastname)


# Use the Parent class to create an object
# and then execute the print method:
x = cls("Geeks", "for", "Geeks")
x.print()
