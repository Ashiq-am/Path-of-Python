# Python program to demonstrate
# subclasshook


from abc import ABCMeta


class A(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, C):
        if cls is A:

            # condition to check if the
            # function anyfun() is present
            # in any sub class or not
            if any("__anyfun__" in Q.__dict__
                   for Q in C.__mro__):
                return True

        return False


class P(object):
    pass


class Q(object):

    def __anyfun__(self):
        return 0


# Driver's code
print(issubclass(Q, A))
print(issubclass(P, A))
