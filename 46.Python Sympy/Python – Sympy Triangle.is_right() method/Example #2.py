# import Triangle, Point
from sympy.geometry import Triangle, Point

# using Triangle()
t2 = Triangle(Point(0, 0), Point(2, 0), Point(4, 3))

# using is_right()
isRight = t2.is_right()
print(isRight)
