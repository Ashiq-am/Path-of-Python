# import required libraries
import numpy as np

# creating an array using numpy
a = np.array([[9, 8, 5], [11, 12, 14], [20, 21, 22]])

# using kron function upsampling the array
upsampled_array = np.kron(a, np.ones((2, 2)))

# printing the desired result
print(upsampled_array)
