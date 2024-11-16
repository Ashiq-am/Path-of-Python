# importing Numpy package
import numpy as np

# creating a Numpy array
num_array = np.arange(12).reshape(3, 4)

print("Array:")
print(num_array)

# Display array in Fortran order
# using numpy.nditer()
print("\nElements of the array in Fortan array:")
for num_array in np.nditer(num_array, order="F"):
	print(num_array, end=' ')
