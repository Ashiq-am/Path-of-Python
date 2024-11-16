# Importing Numpy module
import numpy as np

# Creating a 3X4 2-D Numpy array
arr = np.array([[101, 20, 3, 10],
                [40, 5, 66, 7],
                [70, 88, 9, 141]])

print("Given Array :")
print(arr)

# Access the Middle row of array
res_arr = arr[1]
print("\nAccessed Row :")
print(res_arr)
