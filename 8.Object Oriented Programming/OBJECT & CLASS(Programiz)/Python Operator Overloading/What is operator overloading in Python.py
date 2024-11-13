class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y




#>>> p1 = Point(2,3)
#>>> p2 = Point(-1,2)
#>>> p1 + p2
#Traceback (most recent call last):
#...
#TypeError: unsupported operand type(s) for +: 'Point' and 'Point'