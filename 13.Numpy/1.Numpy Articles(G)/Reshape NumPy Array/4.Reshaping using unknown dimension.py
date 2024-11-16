# importing numpy
import numpy as np

# creating a numpy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# printing array
print("Array : " + str(array))


# reshaping numpy array
# coverting it to 3-D from 1-D array
reshaped1 = array.reshape((2, 2, -1))

# printing reshaped array
print("First Reshaped Array : ")
print(reshaped1)


# coverting it to 2-D array
reshaped2 = array.reshape((4, -1))

# printing reshaped array
print("Second Reshaped Array : ")
print(reshaped2)
