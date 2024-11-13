class geek:
    def __init__(self, name):
        self.name = name

    # defining __repr__() method to control what
    # to return for objects of geek
    def __repr__(self):
        return self.name


geek1 = geek('mohan')
print(repr(geek1))
