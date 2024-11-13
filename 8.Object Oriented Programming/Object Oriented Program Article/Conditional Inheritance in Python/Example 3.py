class A(object):
    def __init__(self, x):
        self.x = x

    def getX(self):
        return self.X


# Based on condition C inherits from
# A or it inherits from object i.e.
# does not inherit A
cond = False


## inherits from A or B
class C(A if cond else object):
    def isA(self):
        return True


# Object of C_A
ca = C(1)
print(ca.isA())
