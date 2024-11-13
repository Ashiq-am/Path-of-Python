# importing packages
from sympy.geometry import Point, Triangle

# constructing a triangle with three points
triangle = Triangle(Point(0, 0), Point(3, 0), Point(3, 3))

# area of the triangle
print('area of the triangle is : '+str(triangle.area))
