""



'''
# work.pyx
# Import the low-level C declarations
		
cimport cwork
# Importing functionalities from Python
# and the C stdlib
from cpython.pycapsule cimport *
from libc.stdlib cimport malloc, free

# Wrappers
def gcd(unsigned int x, unsigned int y):
	return cwork.gcd(x, y)

def divide(x, y):
	cdef int rem
	quot = cwork.divide(x, y, &rem)
	return quot, rem

def avg(double[:] a):
	cdef:
		int sz
		double result

	sz = a.size

	with nogil:
		result = cwork.avg(<double *> &a[0], sz)

	return result



'''