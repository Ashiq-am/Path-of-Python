# importing Numpy package
import numpy as np

# creating a 3X3 Numpy matrix
n_array = np.array([[55, 25, 15],
					[30, 44, 2],
					[11, 45, 77]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# Finding the diagonal elements of a matrix
diag = np.diagonal(n_array)

print("\nDiagonal elements are:")
print(diag)

print("\nSum of Diagonal elements is:")
print(sum(diag))
