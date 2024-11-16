# Python program explaining
# log10() function

import numpy as np

in_array = [1, 3, 5, 10**8]
print ("Input array : ", in_array)

out_array = np.log10(in_array)
print ("Output array : ", out_array)


print("\nnp.log10(4**4) : ", np.log10(100**4))
print("np.log10(2**8) : ", np.log10(10**8))
