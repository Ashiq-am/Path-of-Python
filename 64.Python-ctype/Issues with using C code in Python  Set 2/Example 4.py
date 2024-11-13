class Point(ctypes.Structure):
	_fields_ = [('x', ctypes.c_double),
				('y', ctypes.c_double)]

point1 = sample.Point(1, 2)
point2 = sample.Point(4, 5)

print ("pt1 x : ", point1.x)

print ("\npt1 y : ", point1.y)

print ("\nDistance between pt1 and pt2 : ",
		sample.distance(point1, point2))
