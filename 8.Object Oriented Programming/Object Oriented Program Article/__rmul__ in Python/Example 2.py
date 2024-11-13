class Foo(object):

    def __init__(self, val):
        self.val = val

    def __mul__(self, other):
        return Foo(self.val * other.val)

    def __str__(self):
        return "Foo [% s]" % self.val


class Bar(object):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "Bar [% s]" % self.val


# Driver Code
f = Foo(5)
b = Bar(6)
print(f * b)
