# Python program to demonstrate
# subclasscheck


class A(type):

    # __subclasscheck__() defined
    def __subclasscheck__(cls, sub):
        # Getting the L attribute of
        # subclass
        attr = getattr(cls, 'L', [])

        # Checking if the subclass
        # is present in the L attribute
        # of subclass or not
        if sub in attr:
            return True

        return False


class B(metaclass=A):
    # L Attribute
    L = [1, 2, 3, 4, 5]


class C(metaclass=A):
    # L Attribute
    L = ["Geeks", "For"]


# Driver's code
print(issubclass(1, B))
print(issubclass("Geeks", B))
print(issubclass("Geeks", C))
