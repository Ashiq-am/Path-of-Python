# Python program to rank items in
# NumPy array using rankdata function

# Import the libraries numpy and rankdata
import numpy as np
from scipy.stats import rankdata

# Define the NumPy array
arr = np.array([7, 4, 13, 2, 19, 5])

# Calculate rank of each item in array
rank_items = rankdata(arr)

# Print the rank of each element
print(rank_items)
