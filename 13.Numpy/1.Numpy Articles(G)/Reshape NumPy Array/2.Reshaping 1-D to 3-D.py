# importing numpy
import numpy as np

# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# printing array
print("Array : " + str(array))


# reshaping numpy array
# coverting it to 3-D from 1-D array
reshaped = array.reshape((2, 2, 4))

# printing reshaped array
print("Reshaped 3-D Array : ")
print(reshaped)
