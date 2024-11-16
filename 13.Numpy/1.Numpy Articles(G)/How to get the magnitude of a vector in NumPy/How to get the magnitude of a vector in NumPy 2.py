# program to compute magnitude of a vector

# importing required libraries
import numpy

# displaying the original vector
v = numpy.array([1, 2, 3])
print('Vector:', v)

# computing and displaying the magnitude of
# the vector using norm() method
print('Magnitude of the Vector:', numpy.linalg.norm(v))
