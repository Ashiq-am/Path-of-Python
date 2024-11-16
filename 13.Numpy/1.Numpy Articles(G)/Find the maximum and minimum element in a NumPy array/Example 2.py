# import numpy library
import numpy

# creating a two dimensional
# numpy array of integers
arr = numpy.array([[11, 2, 3],
					[4, 5, 16],
					[7, 81, 22]])

# finding the maximum and
# minimum element in the array
max_element = numpy.max(arr)
min_element = numpy.min(arr)

# printing the result
print('maximum element in the array is:',
	max_element)
print('minimumm element in the array is:',
	min_element)
