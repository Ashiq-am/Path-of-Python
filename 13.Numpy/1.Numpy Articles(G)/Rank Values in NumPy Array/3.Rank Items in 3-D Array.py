# Python program to rank items in
# NumPy array using rankdata function

# Import the libraries numpy and rankdata
import numpy as np
from scipy.stats import rankdata

# Define the NumPy array
arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 0]])

#calculate rank of each row in array
rank0 = rankdata(arr[0])
rank1= rankdata(arr[1])

# Combine rank of each row to form 2D array
rank=np.row_stack((rank0,rank1))

# Print the rank of each element
print(rank)
