# importing numpy
import numpy as np

# creating a numpy array
array = np.array([[1, 2, 3],
				[4, 5, 6],
				[7, 8, 9]])

# printing array
print(" 2-D Array : ")
print(array)


# reshaping numpy array
# converting it to 1-D from 2-D array
# rehaping it into 1, 5
reshaped = array.reshape((1, 5))

# or we can use

# printing reshaped array
print("Reshaped 1-D Array : ")
print(reshaped)
