# Base class 1
class A:
    def a_method(self):
        print('A')


# Base class 2
class B(A):
    def b_method(self):
        print('B')


# Child class
class C(A, B):
    def c_method(self):
        print('C')
