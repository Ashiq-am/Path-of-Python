# importing Numpy package
import numpy as np

# creating a 4X4 Numpy matrix
n_array = np.array([[55, 25, 15, 41],
					[30, 44, 2, 54],
					[11, 45, 77, 11],
					[11, 212, 4, 20]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the Trace of a matrix
trace = np.trace(n_array)


print("\nTrace of given 4X4 matrix:")
print(trace)
