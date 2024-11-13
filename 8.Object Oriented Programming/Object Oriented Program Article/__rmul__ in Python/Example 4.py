class Foo(object):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "Foo [% s]" % self.val


class Bar(object):

    def __init__(self, val):
        self.val = val

    def __rmul__(self, other):
        return Bar(self.val * other.val)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __str__(self):
        return "Bar [% s]" % self.val


# Driver Code
f = Foo(5)
b = Bar(6)

print(b * f)
print(f * b)
