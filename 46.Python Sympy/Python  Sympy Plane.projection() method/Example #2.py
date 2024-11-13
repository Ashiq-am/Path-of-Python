# import sympy and Plane, Point, Point3D
from sympy import Plane, Point, Point3D

p = Point3D(2, 2, 2)

# using Plane()
p1 = Plane(Point3D(1, 2, 3), normal_vector =(0, 1, 1))

# using projection()
projectionPoint = p1.projection(p)

print(projectionPoint)
