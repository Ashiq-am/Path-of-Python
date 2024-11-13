class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class B:
    def __init__(self, z):
        self.z = z

class C(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x=x, y=y)
        B.__init__(self, z=z)

c = C(x=1, y=2, z=3)
