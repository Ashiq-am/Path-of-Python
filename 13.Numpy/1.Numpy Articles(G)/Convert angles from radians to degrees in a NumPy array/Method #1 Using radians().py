# python code demonstrating usage of radians
# method to convert degrees to radians
# importing numpy library
import numpy as np
import math


# initialising an array
array=np.arange(20.)*90

# printing degree values
print('Values of array in Degrees:',array)

# converting to radians
radian_array=np.radians(array)

# printing radian values
print('Values of array in radians:',radian_array)
