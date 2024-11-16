import numpy as np
# take data
data = np.array([[1, 2, 3], [0, 0, 0], [4, 5, 6],
				[0, 0, 0], [7, 8, 9], [0, 0, 0]])
# print original data having rows with all zeroes
print("Original Dataset")
print(data)

# remove rows having all zeroes
data = data[~np.all(data == 0, axis=1)]

# data after removing rows having all zeroes
print("After removing rows")
print(data)
