# import polyval library from numpy
from numpy.polynomial.polynomial import polyval

# create a multidimensional array or matrix
Arr = [[7, 6], [2, 3]]

# evaluate polynomial at points x using
# polyval function
print(polyval([1, 2], Arr, tensor=True))
