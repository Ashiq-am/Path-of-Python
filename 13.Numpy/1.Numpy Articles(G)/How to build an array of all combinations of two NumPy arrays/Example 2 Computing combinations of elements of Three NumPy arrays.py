# importing Numpy package
import numpy as np

# creating 3 numpy arrays
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 6, 4])
array_3 = np.array([3, 6])

print("Array-1")
print(array_1)

print("Array-2")
print(array_2)

print("Array-3")
print(array_3)


# combination of elements of array_1,
# array_2 and array_3 using
# numpy.meshgrid().T.reshape()
comb_array = np.array(
np.meshgrid(array_1, array_2, array_3)).T.reshape(-1, 3)

print("\nCombine array:")
print(comb_array)
