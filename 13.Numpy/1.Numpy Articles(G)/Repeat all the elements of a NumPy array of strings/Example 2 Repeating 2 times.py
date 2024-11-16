# importing the module
import numpy as np

# created array of strings
arr = np.array(['Geeks', 'for', 'Geeks'])
print("Original Array :")
print(arr)

# with the help of np.char.multiply()
# repeating the characters 3 times
new_array = np.char.multiply(arr, 2)
print("\nNew array :")
print(new_array)
