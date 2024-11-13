# import Triangle, Point
from sympy.geometry import Triangle, Point

# using Triangle()
t1 = Triangle(Point(0, 0), Point(4, 0), Point(4, 3))

# using is_right()
isRight = t1.is_right()
print(isRight)
