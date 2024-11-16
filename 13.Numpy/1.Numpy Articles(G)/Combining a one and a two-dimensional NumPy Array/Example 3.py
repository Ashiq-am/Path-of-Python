# importing Numpy package
import numpy as np

num_1d = np.arange(2)
print("One dimensional array:")
print(num_1d)

num_2d = np.arange(12).reshape(6,2)
print("\nTwo dimensional array:")
print(num_2d)

# Combine 1-D and 2-D arrays and display
# their elements using numpy.nditer()
for a, b in np.nditer([num_1d, num_2d]):
	print("%d:%d" % (a, b),)
