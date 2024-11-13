class Gfg:
    a = None
    _b = None
    __c = None

    # Constructor
    def __init__(self, a, b, c):
        # Data mambers
        # Public
        self.a = a

        # Protected
        self._b = b

        # Private
        self.__c = c

    # Methods
    # Private method
    def __display(self):
        print(self.a)
        print(self._b)
        print(self.__c)

    # Public method
    def accessPrivateMethod(self):
        self.__display()


# Driver code
# Creating object
Obj = Gfg('Geeks', 4, "Geeks!")

# Calling method
Obj.accessPrivateMethod()
