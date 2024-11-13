import numpy as np

# creating a numpy array(matrix) with 3-columns and 4-rows
arr = np.array([
	['c1', 'c2', 'c3'],
	[10, 20, 30],
	[40, 50, 60],
	[70, 80, 90]])

# reversing column order in matrix
flipped_arr = np.fliplr(arr)

print('Array before changing column order:\n', arr)
print('\nArray after changing column order:\n', flipped_arr)
