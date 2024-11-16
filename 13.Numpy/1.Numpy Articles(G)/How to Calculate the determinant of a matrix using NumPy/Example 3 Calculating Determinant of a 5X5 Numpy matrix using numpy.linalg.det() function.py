# importing Numpy package
import numpy as np

# creating a 5X5 Numpy matrix
n_array = np.array([[5, 2, 1, 4, 6],
					[9, 4, 2, 5, 2],
					[11, 5, 7, 3, 9],
					[5, 6, 6, 7, 2],
					[7, 5, 9, 3, 3]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given 5X5 square matrix:")
print(int(det))
