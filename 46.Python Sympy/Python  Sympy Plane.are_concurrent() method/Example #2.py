# import sympy, Point3D and Plane
from sympy import Point3D, Plane

# using Plane()
p1 = Plane(Point3D(5, 0, 0), normal_vector =(1, -1, 1))
p2 = Plane(Point3D(0, -2, 0), normal_vector =(3, 1, 1))
p3 = Plane(Point3D(0, -1, 0), normal_vector =(5, -1, 9))

# using are_concurrent()
areConcurrent = Plane.are_concurrent(p1, p2, p3)

print(areConcurrent)
