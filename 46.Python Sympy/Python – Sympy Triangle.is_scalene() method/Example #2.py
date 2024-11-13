# import Triangle, Point
from sympy.geometry import Triangle, Point

# using Triangle()
t2 = Triangle(Point(0, 0), Point(4, 0), Point(2, 4))

# using is_scalene()
isScalene = t2.is_scalene()
print(isScalene)
