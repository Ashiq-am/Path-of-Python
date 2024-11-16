# Importing Numpy library
import numpy as np

# Creating a 2-D Numpy array
num = np.array([[3.1415, 2.7182],
				[6.6260e-34, 6.6743e-11]])

# Suppressing 2-D numpy array with precision 3
# using numpy.set_printoptions()
print("Numpy array values with precision 3:\n")
np.set_printoptions(precision = 3, suppress = True)
print(num)
