# importing hermite_e library
from numpy.polynomial import hermite_e

# creating an array 'arr' of complex coefficient
a = complex(1,2)
b = complex(2,0)
arr = [a, b]

# Evaluating roots of a Hermite_e
# series using hermeroots() function
print(hermite_e.hermeroots(arr))
