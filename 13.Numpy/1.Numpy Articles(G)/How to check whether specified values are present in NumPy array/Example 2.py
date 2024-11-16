# importing Numpy package
import numpy as np

# creating a Numpy array
n_array = np.array([[2.14, 3, 0.5],
					[4.5, 1.2, 6.2],
					[20.2, 5.9, 8.8]])

print("Given array:")
print(n_array)

# Checking whether specific values
# are present in "n_array" or not
print(2.14 in n_array)
print(5.28 in n_array)
print(6.2 in n_array)
print(5.9 in n_array)
print(8.5 in n_array)
