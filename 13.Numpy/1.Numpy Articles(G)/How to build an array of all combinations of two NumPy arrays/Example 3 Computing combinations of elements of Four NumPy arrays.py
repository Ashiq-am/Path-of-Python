# importing Numpy package
import numpy as np

# creating 4 numpy arrays
array_1 = np.array([50, 21])
array_2 = np.array([4, 4])
array_3 = np.array([1, 10])
array_4 = np.array([7, 14])


print("Array-1")
print(array_1)

print("Array-2")
print(array_2)

print("Array-3")
print(array_3)

print("Array-4")
print(array_4)


# combination of elements of array_1,
# array_2, array_3 and array_4
# using numpy.meshgrid().T.reshape()
comb_array = np.array(np.meshgrid(
	array_1, array_2, array_3, array_4)).T.reshape(-1, 4)

print("\nCombine array:")
print(comb_array)
