# class A is declared
class A:

    # constructor
    def __init__(self):
        # keys are initialized with
        # their respective values
        self.A = 1
        self.B = 2
        self.C = 3
        self.D = 4


# object obj of class A
obj = A()

# calling vars method on obj object
print(vars(obj))
