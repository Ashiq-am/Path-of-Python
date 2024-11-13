# Python program to demonstrate
# __del__ and __delete__


class Example(object):

    # Initializing
    def __init__(self):
        self.value = ''

    # deletes an attribute
    def __delete__(self, instance):
        print("Inside __delete__")

    # Destructor
    def __del__(self):
        print("Inside __del__")


class Foo(object):
    exp = Example()


# Driver's code
f = Foo()
del f.exp
