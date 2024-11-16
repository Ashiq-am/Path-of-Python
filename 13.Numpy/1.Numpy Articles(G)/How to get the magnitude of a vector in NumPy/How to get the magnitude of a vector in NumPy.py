# program to compute magnitude of a vector

# importing required libraries
import numpy
import math

# function defination to compute magnitude o f the vector
def magnitude(vector):
	return math.sqrt(sum(pow(element, 2) for element in vector))

# displaying the original vector
v = numpy.array([0, 1, 2, 3, 4])
print('Vector:', v)

# computing and displaying the magnitude of the vector
print('Magnitude of the Vector:', magnitude(v))
