import numpy as np

# input 2d array
in_arr = np.array([[2, 0, 1], [5, 4, 3]])
print("Input array :\n", in_arr)

# output sorted array indices
out_arr1 = np.argsort(in_arr, kind='mergesort', axis=0)
print("\nOutput sorteded array indices along axis 0:\n", out_arr1)

out_arr2 = np.argsort(in_arr, kind='heapsort', axis=1)
print("\nOutput sorteded array indices along axis 1:\n", out_arr2)
