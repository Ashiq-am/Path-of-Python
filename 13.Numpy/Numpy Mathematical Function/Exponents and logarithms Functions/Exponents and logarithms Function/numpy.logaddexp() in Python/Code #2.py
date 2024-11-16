# Python3 code demonstrate logaddexp() function

# importing numpy
import numpy as np

in_arr1 = [2, 3, 8]
in_arr2 = [1, 2, 3]
print("Input array1 : ", in_arr1)
print("Input array2 : ", in_arr2)

out_arr = np.logaddexp(in_arr1, in_arr2)
print("Output array : ", out_arr)
