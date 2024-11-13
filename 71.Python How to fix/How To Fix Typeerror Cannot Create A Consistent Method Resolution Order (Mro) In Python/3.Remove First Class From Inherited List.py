# Base class 1
class A(object):
    def a_method(self):
        print('A')


# Base class 2
class B(object):
    def b_method(self):
        print('B')


# Child class
class C(B):
    def c_method(self):
        print('C')
