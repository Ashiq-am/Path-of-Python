# import polyval2d from numpy
from numpy.polynomial.polynomial import polyval2d

# create a 2 dimensional array
# of coefficient or a matrix
Arr = [[4,2], [6,3]]

# evaluate the 2D polynomial at
# point (x,y) using polyval2d
# function and print the result
print(polyval2d([2,3],[1,2],Arr))
