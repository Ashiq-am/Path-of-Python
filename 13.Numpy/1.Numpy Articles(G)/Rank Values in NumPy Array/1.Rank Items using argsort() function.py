# Python program to rank items in
# NumPy array using argsort function

# Import the library numpy
import numpy as np

# Define the NumPy array
arr = np.array([[1, 2, 3],[5, 6, 4], [9, 8, 7]])

# Rank items in NumPy array using argort() function
rank = np.array(arr).argsort().argsort()

# Print the rank of elements
print(rank)
