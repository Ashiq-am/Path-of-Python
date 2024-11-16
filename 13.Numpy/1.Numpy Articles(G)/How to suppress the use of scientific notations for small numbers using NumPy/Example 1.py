# Importing Numpy library
import numpy as np

# Creating a 1-D Numpy array
num = np.array([1.8e-10, 1.586, 150.45, 0.2855])

# Suppressing 1-D numpy array with precision 2
# using numpy.set_printoptions()
print("Numpy array values with precision 2:\n")
np.set_printoptions(precision = 2, suppress = True)
print(num)
