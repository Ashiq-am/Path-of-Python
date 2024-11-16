# Importing Module
import numpy as np


# Creating array
my_array = np.arange(12).reshape(4, 3)
print("Orginal Array : ")
print(my_array)
# creating function for swap

def Swap(arr, start_index, last_index):
	arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]

# passing parameter into the function
Swap(my_array, 0, 1)
print(" After Swapping :")
print(my_array)
