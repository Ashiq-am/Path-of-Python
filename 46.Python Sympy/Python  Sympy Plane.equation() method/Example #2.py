# import sympy, Point3D and Plane
from sympy import Point3D, Plane

# using Plane()

p3 = Plane(Point3D(1, 2, 3), normal_vector =(2, 2, 2))
p4 = p3.equation()

print(p4)
