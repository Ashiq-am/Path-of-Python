#Using Parent class name
# Python example to show that base
# class members can be accessed in
# derived class using base class name
import self


class Base(object):

    # Constructor
    def __init__(self, x):
        self.x = x


class Derived(Base):

    # Constructor
    def __init__(self, x, y):
        Base.x = x
        self.y = y

    def printXY(self):
        print(self.x, self.y)                 #will also work
        print(Base.x, self.y)


# Driver Code
d = Derived(10, 20)
d.printXY()











#Using super()We can also access parent class members using super.
# Python example to show that base
# class members can be accessed in
# derived class using super()
class Base(object):

    # Constructor
    def __init__(self, x):
        self.x = x


class Derived(Base):

    # Constructor
    def __init__(self, x, y):
        ''' In Python 3.x, "super().__init__(name)"
            also works'''
        super(Derived, self).__init__(x)
        self.y = y

    def printXY(self):
        print(self.x, self.y)               # Note that Base.x won't work here
                                            # because super() is used in constructor


# Driver Code
d = Derived(10, 20)
d.printXY()

