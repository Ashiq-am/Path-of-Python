# Python3 code demonstrate clip() function

# importing the numpy
import numpy as np

in_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("Input array : ", in_array)

out_array = np.clip(in_array, a_min =[3, 4, 1, 1, 1, 4, 4, 4, 4, 4],
														a_max = 9)
print ("Output array : ", out_array)
