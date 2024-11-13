""


'''

# cwork.pxd
#
# Declarations of "external" C
# functions and structures

cdef extern from "work.h":

	int gcd(int, int)
	int divide(int, int, int *)
	double avg(double *, int) nogil
	
	ctypedef struct Point:
		double x
		double y
		
	double distance(Point *, Point *)



'''