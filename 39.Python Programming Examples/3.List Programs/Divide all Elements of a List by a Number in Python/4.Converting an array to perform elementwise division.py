import numpy as np

# A list containing integers
l = [14, 8, 0, 12, 981, 21, -99]

# Converting the list to an array and storing it in separate variable
arr = np.array(l)

# Number which will be used for elementwise division
divisor = 7

# Performing elementwise division operation on all elements of the array
result = arr/divisor

# Converting the array back to list
l = result.tolist()

print(l)
