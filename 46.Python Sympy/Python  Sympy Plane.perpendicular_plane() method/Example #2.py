# import sympy, Point3D and Plane, Line3D
from sympy import Point3D, Plane, Line3D

l3, l4 = Point3D(0, 0, 0), Point3D(1, 1, 0)
z2 = (0, 1, 1)

# using Plane()
p2 = Plane(l3, normal_vector = z2)

# using perpendicular_plane() with one parameter
perpendicularPlane = p2.perpendicular_plane(l4)

print(perpendicularPlane)
