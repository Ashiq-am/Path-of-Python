# importing Numpy package
import numpy as np

# creating an empty 4d array of int type
empt_array = np.empty((0,4), int)
print("Empty array:")
print(empt_array)

# adding four new rows to empt_array
# using np.append()
empt_array = np.append(empt_array, np.array([[100,200,400,888]]), axis=0)
empt_array = np.append(empt_array, np.array([[405,500,550,558]]), axis=0)
empt_array = np.append(empt_array, np.array([[404,505,555,145]]), axis=0)
empt_array = np.append(empt_array, np.array([[44,55,550,150]]), axis=0)

print("\nNow array is:")
print(empt_array)
