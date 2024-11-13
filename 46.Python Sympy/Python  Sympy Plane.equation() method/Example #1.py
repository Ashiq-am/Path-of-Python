# import sympy, Point3D and Plane
from sympy import Point3D, Plane

# using Plane()

p1 = Plane(Point3D(1, 2, 3), Point3D(4, 5, 6), Point3D(0, 2, 0))
p2 = p1.equation()

print(p2)
