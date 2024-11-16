# importing numpy
import numpy as np

# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# printing array
print("Array : " + str(array))

# length of array
n = array.size

# N-D array N dimenssion
N = 4

# calculating M
M = n//N

# reshaping numpy array
# coverting it to 2-D from 1-D array
reshaped1 = array.reshape((N, M))

# printing reshaped array
print("First Reshaped Array : ")
print(reshaped1)

# creating another reshaped array
reshaped2 = np.reshape(array, (2, 8))

# printing reshaped array
print("Second Reshaped Array : ")
print(reshaped2)
