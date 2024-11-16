# importing Numpy package
import numpy as np

# creating an empty 2d array of int type
empt_array = np.empty((0,2), int)
print("Empty array:")
print(empt_array)

# adding two new rows to empt_array
# using np.append()
empt_array = np.append(empt_array, np.array([[10,20]]), axis=0)
empt_array = np.append(empt_array, np.array([[40,50]]), axis=0)

print("\nNow array is:")
print(empt_array)
