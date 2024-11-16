# Python3 code demonstrate conj() function

# importing numpy
import numpy as np

in_array = np.eye(2) + 3j * np.eye(2)
print ("Input array : ", in_array)

out_array = np.conjugate(in_array)
print ("Output conjugated array : ", out_array)
