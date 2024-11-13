# import sympy, Point3D and Plane, Line3D
from sympy import Point3D, Plane, Line3D

l1, l2 = Point3D(0, 0, 0), Point3D(1, 2, 3)
z1 = (1, 0, 1)

# using Plane()
p1 = Plane(a, normal_vector = z1)

# using perpendicular_plane() with two parameters
perpendicularPlane = p1.perpendicular_plane(l1, l2)

print(perpendicularPlane)
