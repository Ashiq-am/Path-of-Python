# decorator accepts a class as
# a parameter
def decorator(cls):
    class Wrapper:

        def __init__(self, x):
            self.wrap = cls(x)

        def get_name(self):
            # fetches the name attribute
            return self.wrap.name

    return Wrapper


@decorator
class C:
    def __init__(self, y):
        self.name = y


# its equivalent to saying
# C = decorator(C)
x = C("Geeks")
print(x.get_name())
