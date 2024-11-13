# import Triangle, Point
from sympy.geometry import Triangle, Point

# using Triangle()
t1 = Triangle(Point(0, 0), Point(6, 0), Point(3, 4))

# using is_isosceles()
isIsosceles = t1.is_isosceles()
print(isIsosceles)
