""


"""

# decorators
@cython.boundscheck(False)
@cython.wraparound(False)


cpdef
clip(double[:]
a, double
min, double
max, double[:]
out):

if min > max:
    raise ValueError("min must be <= max")

if a.shape[0] != out.shape[0]:
    raise ValueError
    ("input and output arrays must be the same size")

for i in range(a.shape[0]):
    out[i] = (a[i]
              if a[i] < max else max)
    if a[i] > min else min
    
    
"""
