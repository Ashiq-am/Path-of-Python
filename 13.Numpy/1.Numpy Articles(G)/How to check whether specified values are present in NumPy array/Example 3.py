# importing Numpy package
import numpy as np

# creating a Numpy array
n_array = np.array([[4, 5.5, 7, 6.9, 10],
					[7.1, 5.3, 40, 8.8, 1],
					[4.4, 9.3, 6, 2.2, 11],
					[7.1, 4, 5, 9, 10.5]])


print("Given array:")
print(n_array)

# Checking whether specific values
# are present in "n_array" or not
print(2.14 in n_array)
print(5.28 in n_array)
print(8.5 in n_array)
