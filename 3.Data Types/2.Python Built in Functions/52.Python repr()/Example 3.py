class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person("{self.name}")'


p = Person("Kiran")
# returns a string which can be used to recontruct Person object
print(repr(p))
