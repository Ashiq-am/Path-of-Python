# import required modules
import numpy as np


# creating the array
sample_array1 = np.arange(5)

# initialization the decimal number
sample_array2 = [1.0, 2.0, 3.0, 3.0, 2.0]

print("Orignal array ")
print("array1 ", sample_array1)
print("array2 ", sample_array2)

# calculating element-wise power
power_array = np.power(sample_array1, sample_array2)

print("power to the array1 and array 2 : ", power_array)
