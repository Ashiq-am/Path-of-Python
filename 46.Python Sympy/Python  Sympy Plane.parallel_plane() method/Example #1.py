# import sympy, Point3D and Plane
from sympy import Point3D, Plane

# using Plane()
p1 = Plane(Point3D(1, 2, 3), normal_vector =(4, 5, 6))

# using parallel_plane()
parallelPlane = p1.parallel_plane(Point3D(2, 3, 5))

print(parallelPlane)
