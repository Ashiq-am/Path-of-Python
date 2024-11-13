# import Triangle, Point
from sympy.geometry import Triangle, Point

# using Triangle()
t1 = Triangle(Point(0, 0), Point(3, 0), Point(1, 2))

# using is_scalene()
isScalene = t1.is_scalene()
print(isScalene)
