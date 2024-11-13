# create a class
class Employee:

    # constructor
    def __init__(self):
        # instance attribute
        self.name = 'Gfg'
        self.salary = 4000

    # define a method
    def show(self):
        print(self.name)
        print(self.salary)


# create an object of
# Employee class
x = Employee()

# method calling
x.show()
