# importing Numpy package
import numpy as np

# Creating a 4X4 Numpy matrix
array = np.ones((4, 4))

print("Original array")
print(array)

print("\n0 on the border and 1 inside the array")

# constructing border of 0 around 4D identity matrix
# using np.pad()
array = np.pad(array, pad_width=1, mode='constant',
			constant_values=0)

print(array)
