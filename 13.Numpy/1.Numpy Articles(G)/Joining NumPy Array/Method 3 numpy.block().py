import numpy as np

block_1 = np.array([[1, 1], [1, 1]])
block_2 = np.array([[2, 2, 2], [2, 2, 2]])
block_3 = np.array([[3, 3], [3, 3], [3, 3]])
block_4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])

block_new = np.block([
	[block_1, block_2],
	[block_3, block_4]
])

print(block_new)
