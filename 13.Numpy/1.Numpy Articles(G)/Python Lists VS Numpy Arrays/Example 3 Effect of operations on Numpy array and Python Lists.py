# importing Numpy package
import numpy as np

# declaring a list
ls = [1, 2, 3]

# converting the list into a Numpy array
arr = np.array(ls)

try:
    # adding 4 to each element of list
    ls = ls + 4

except(TypeError):
    print("Lists don't support list + int")

# now on array
try:
    # adding 4 to each element of Numpy array
    arr = arr + 4

    # printing the Numpy array
    print("Modified Numpy array: ", arr)

except(TypeError):
    print("Numpy arrays don't support list + int")
