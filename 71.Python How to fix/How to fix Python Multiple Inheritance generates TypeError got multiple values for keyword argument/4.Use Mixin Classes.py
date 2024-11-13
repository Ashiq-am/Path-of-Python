class MixinA:
    def __init__(self, x):
        self.x = x

class MixinB:
    def __init__(self, z):
        self.z = z

class C(MixinA, MixinB):
    def __init__(self, x, z):
        MixinA.__init__(self, x)
        MixinB.__init__(self, z)

c = C(x=1, z=3)
