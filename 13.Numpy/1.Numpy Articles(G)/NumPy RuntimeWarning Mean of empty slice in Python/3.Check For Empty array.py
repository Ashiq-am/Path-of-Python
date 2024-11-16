import numpy as np

empty_array = np.array([])

# Checking for empty array before calculating the mean
if len(empty_array) > 0:
	mean_value = np.mean(empty_array[1:3])
	print("Mean:", mean_value)
else:
	print("Array is empty.")
