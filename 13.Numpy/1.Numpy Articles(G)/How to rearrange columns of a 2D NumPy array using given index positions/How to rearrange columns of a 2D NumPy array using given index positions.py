# importing package
import numpy

# create a numpy array
arr = numpy.array([[1,2,3,4,5],
				[1,2,3,4,5],
				[1,2,3,4,5],
				[1,2,3,4,5],
				[1,2,3,4,5]
				])

# view array
print(arr)

# declare index list
i = [2,4,0,3,1]

# create output
output = arr[:,i]

# view output
print(output)
