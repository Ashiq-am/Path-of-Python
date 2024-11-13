class Base1:
    def __init__(self, x):
        self.x = x


class Base2:
    def __init__(self, y):
        self.y = y


class Derived(Base1, Base2):
    def __init__(self, x, y, z):
        super().__init__(x)  # Call first base class constructor
        # Call second base class constructor explicitly
        Base2.__init__(self, y)
        self.z = z


derived = Derived(1, 2, 3)

print("Derived:", derived.x, derived.y, derived.z)
