# import numpy and matrix_power
import numpy
from numpy.linalg import matrix_power

# Create a 2D array
input_array = numpy.array(
	[[3, 4, 3, 4], [4, 5, 2, 2], [1, 1, 0, -2],
	[-4, 5, 4, -1]])

# Display array
print(input_array)

# Using numpy.linalg.matrix_power() to
# return raise 0 th power of matrix
print(matrix_power(input_array, 0))

print()

# Using numpy.linalg.matrix_power() to
# return raise 4 th power of matrix
print(matrix_power(input_array, 4))

print()

# Using numpy.linalg.matrix_power() to
# return raise 5 th power of matrix
print(matrix_power(input_array, 5))
