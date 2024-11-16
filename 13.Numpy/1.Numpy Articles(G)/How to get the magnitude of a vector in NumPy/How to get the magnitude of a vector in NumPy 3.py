# program to compute the nth order of the
# magnitude of a vector

# importing required libraries
import numpy

# displaying the original vector
v = numpy.array([0, 1, 2, 3, 4])
print('Vector:', v)

# computing and displaying the magnitude of the vector
print('Magnitude of the Vector:', numpy.linalg.norm(v))

# Computing the nth order of the magnitude of vector
print('ord is 0: ', numpy.linalg.norm(v, ord = 0))
print('ord is 1: ', numpy.linalg.norm(v, ord = 1))
print('ord is 2: ', numpy.linalg.norm(v, ord = 2))
print('ord is 3: ', numpy.linalg.norm(v, ord = 3))
print('ord is 4: ', numpy.linalg.norm(v, ord = 4))
