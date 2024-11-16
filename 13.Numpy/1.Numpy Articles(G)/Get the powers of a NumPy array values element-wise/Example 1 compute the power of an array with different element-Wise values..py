# import required modules
import numpy as np


# creating the array
sample_array1 = np.arange(5)
sample_array2 = np.arange(0, 10, 2)

print("Orignal array ")
print("array1 ", sample_array1)
print("array2 ", sample_array2)

# calculating element-wise power
power_array = np.power(sample_array1, sample_array2)

print("power to the array1 and array 2 : ", power_array)
