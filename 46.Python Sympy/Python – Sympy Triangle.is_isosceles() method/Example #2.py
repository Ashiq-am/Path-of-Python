# import Triangle, Point
from sympy.geometry import Triangle, Point

# using Triangle()
t2 = Triangle(Point(0, 0), Point(3, 0), Point(3, 4))

# using is_isosceles()
isIsosceles = t2.is_isosceles()
print(isIsosceles)
