# import library
import numpy as np

# create a numpy 1d-array
array = np.array([1, 2, 3,
				0, -1, -2])

# find index of max element
# in an array
max_ele_index = np.argmax(array)

# find max element in an array
max_ele = array[max_ele_index]

# find index of min element
# in an array
min_ele_index = np.argmin(array)

# find min element in an array
min_ele = array[min_ele_index]

# show the outputs
print("Given Array:", array)

print("Max Element:", max_ele)

print("Min Element:", min_ele)
