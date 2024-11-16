# importing hermite_e library
from numpy.polynomial import hermite_e

# creating an array 'arr' of complex coefficient
a = complex(1,2)

# Evaluating roots of a Hermite_e
# series using hermeroots() function
print(hermite_e.hermeroots([a,-a]))
