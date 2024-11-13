# import packages
from sympy.geometry import Point

# create points
x = Point(1, 1)
y = Point(2, 2)
z = Point(3, 3)
w = Point(5, 2)

# checking if points are collinear.
print(Point.is_collinear(x, y, z))
print(Point.is_collinear(y, z, w))

# calculating distance between two points
print('Distance between x and y points is ' + str(x.distance(y)))
