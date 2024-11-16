# import hermite_e libraries
from numpy.polynomial import hermite_e as h

# create a multidimensional array
# 'arr' of coefficients
arr = [[0, 1, 2],[3, 4, 5]]

# integrate a Hermite_e series using
# hermite_e.hermeint() function
print(h.hermeint(arr, m=2, k=[1, 2], lbnd=-1, axis=0))
