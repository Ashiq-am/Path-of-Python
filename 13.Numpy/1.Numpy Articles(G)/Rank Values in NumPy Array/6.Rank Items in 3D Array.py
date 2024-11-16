# Python program to rank items in
# NumPy array using rankdata function

# Import the libraries numpy and rankdata
import numpy as np
from scipy.stats import rankdata

# Define the NumPy array
arr = np.array([[1, 2, 3],[5, 6, 4], [9, 8, 7]])

#calculate rank of each row in array
rank0 = rankdata(arr[0])
rank1= rankdata(arr[1])
rank2= rankdata(arr[2])

# Combine rank of each row to form 2D array
rank=np.row_stack((rank0,rank1,rank2))

# Print the rank of each element
print(rank)
