class A(object):
    def __init__(self, x):
        self.x = x

    def getX(self):
        return self.X


class B(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getSum(self):
        return self.X + self.y


# inherits from A
class C_A(A):
    def isA(self):
        return True

    def isB(self):
        return False


# inherits from B
class C_B(B):
    def isA(self):
        return False

    def isB(self):
        return True


# return required Object of C based on cond
def getC(cond):
    if cond:
        return C_A(1)
    else:
        return C_B(1, 2)


# Object of C_A
ca = getC(True)
print(ca.isA())
print(ca.isB())

# Object of C_B
cb = getC(False)
print(cb.isA())
print(cb.isB())
