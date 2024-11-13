# import sympy and Point3D, Line3D
from sympy import Point3D, Line3D

p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(0, 2, 0)
l1 = Line3D(p1, p2)

# using perpendicular_segment() method
s1 = l1.perpendicular_segment(p3)

perpendicularSegment = l1.perpendicular_segment(p3)

print(perpendicularSegment)
