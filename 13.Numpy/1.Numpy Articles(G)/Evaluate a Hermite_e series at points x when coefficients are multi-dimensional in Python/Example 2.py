# import hermite_e library
from numpy.polynomial import hermite_e as H

# create a multidimensional array
Mul_Array = [[2, 2], [4, 3]]

# evaluate hermite_e series and print
# the result
print(H.hermeval([2, 1], Mul_Array))
