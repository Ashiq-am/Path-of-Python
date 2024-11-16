# Importing Numpy library
import numpy as np

# Creating a 3-D Numpy array
num = np.array([[[3.141527, 2.718283],
				[6.6268574, 6.6743e-11]],
				[[34.8454, 8.6260e-34],
				[7, 8]]])

# Suppressing 3-D numpy array with precision 4
# using numpy.set_printoptions()
print("Numpy array values with precision 4:\n")
np.set_printoptions(precision = 4, suppress = True)
print(num)
