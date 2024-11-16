# importing library
import numpy

# create numpy array
arr = numpy.array([1, 2, 3, 4, 5,
				6, 7, 8, 9, 10,
				11, 12, 13, 14,
				15, 16])

# view array
print("Given Array:\n", arr)

# declare k
k = 2

# find the mean
output = numpy.mean(arr.reshape(-1, k),
					axis=1)

# view output
print("Output Array:\n", output)
