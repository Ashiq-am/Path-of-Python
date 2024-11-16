# importing the module
import numpy as np

# created an array
arr1 = np.array(['Geeks', 'for', 'Geeks'])
print("Original Array :")
print(arr1)

# number of times to be repeated
i = 2

# using the char.multiply() method
arr2 = np.char.multiply(arr1, i)
print("\nNew array :")
print(arr2)
