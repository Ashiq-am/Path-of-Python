# importing Numpy package
import numpy as np

# creating an empty 3d array of int type
empt_array = np.empty((0,3), int)
print("Empty array:")
print(empt_array)

# adding three new rows to empt_array
# using np.append()
empt_array = np.append(empt_array, np.array([[10,20,40]]), axis=0)
empt_array = np.append(empt_array, np.array([[40,50,55]]), axis=0)
empt_array = np.append(empt_array, np.array([[40,50,55]]), axis=0)

print("\nNow array is:")
print(empt_array)
