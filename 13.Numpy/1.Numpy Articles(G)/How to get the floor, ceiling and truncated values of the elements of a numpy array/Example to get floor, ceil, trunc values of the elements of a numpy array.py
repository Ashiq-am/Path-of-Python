import numpy as np


input_arr = np.array([-1.8, -1.6, -0.5, 0.5,
					1.6, 1.8, 3.0])
print(input_arr)

floor_values = np.floor(input_arr)
print("\nFloor values : \n", floor_values)

ceil_values = np.ceil(input_arr)
print("\nCeil values : \n", ceil_values)

trunc_values = np.trunc(input_arr)
print("\nTruncated values : \n", trunc_values)
