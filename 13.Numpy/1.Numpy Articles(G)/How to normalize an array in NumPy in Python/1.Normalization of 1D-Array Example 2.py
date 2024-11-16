# import module
import numpy as np

# explicit function to normalize array
def normalize(arr, t_min, t_max):
	norm_arr = []
	diff = t_max - t_min
	diff_arr = max(arr) - min(arr)
	for i in arr:
		temp = (((i - min(arr))*diff)/diff_arr) + t_min
		norm_arr.append(temp)
	return norm_arr

# assign array and range
array_1d = [1, 2, 4, 8, 10, 15]
range_to_normalize = (0, 1)
normalized_array_1d = normalize(
	array_1d, range_to_normalize[0],
range_to_normalize[1])

# display original and normalized array
print("Original Array = ", array_1d)
print("Normalized Array = ", normalized_array_1d)
