# import sympy, Point3D and Plane
from sympy import Point3D, Plane

# using Plane()
p2 = Plane(Point3D(1, 1, 2), Point3D(2, 4, 7), Point3D(3, 5, 1))

# using parallel_plane()
parallelPlane = p2.parallel_plane(Point3D(1, 2, 3))

print(parallelPlane)
