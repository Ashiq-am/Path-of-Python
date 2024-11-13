""


'''

# Destructor for cleaning up Point objects
cdef del_Point(object obj):
	pt = <csample.Point *> PyCapsule_GetPointer(obj, "Point")
	free(<void *> pt)
	
# Create a Point object and return as a capsule
def Point(double x, double y):
	cdef csample.Point * p
	p = <csample.Point *> malloc(sizeof(csample.Point))
	
	if p == NULL:
		raise MemoryError("No memory to make a Point")
		
	p.x = x
	p.y = y
	
	return PyCapsule_New(<void *>p, "Point",
						<PyCapsule_Destructor>del_Point)

def distance(p1, p2):
	pt1 = <csample.Point *> PyCapsule_GetPointer(p1, "Point")
	pt2 = <csample.Point *> PyCapsule_GetPointer(p2, "Point")
	
	return csample.distance(pt1, pt2)


'''