# parent class
class Programming:
    # properties
    DataStructures = True
    Algorithms = True

    # function practice
    def practice(self):
        print("Practice makes a man perfect")

    # function consistency
    def consistency(self):
        print("Hard work along with consistency can defeat Talent")


# child class
class Python(Programming):

    # function
    def consistency(self):
        print("Hard work along with consistency can defeat Talent.")


Py = Python()
Py.consistency()
Py.practice()
