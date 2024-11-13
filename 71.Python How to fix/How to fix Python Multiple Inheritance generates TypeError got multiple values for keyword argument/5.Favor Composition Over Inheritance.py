class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class B:
    def __init__(self, z):
        self.z = z

class C:
    def __init__(self, x, y, z):
        self.a = A(x, y)
        self.b = B(z)

c = C(x=1, y=2, z=3)
