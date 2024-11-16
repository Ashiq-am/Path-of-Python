# import library
import numpy as np

# create a numpy 1d-array
array = np.array([1, 2, 3,
				0, -1, -2])

# find max element in an array
max_ele = np.amax(array)

# find man element in an array
min_ele = np.amin(array)


# show the outputs
print("Given Array:", array)

print("Max Element:", max_ele)

print("Min Element:", min_ele)
