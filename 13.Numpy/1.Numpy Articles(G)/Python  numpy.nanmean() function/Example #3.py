# Python code to demonstrate the
# use of numpy.nanmedian
# with axis = 1
import numpy as np

# create 2d matrix with nan value
arr = np.array([[32, 20, 24],
                [47, 63, np.nan],
                [17, 28, np.nan],
                [10, 8, 9]])

print("Shape of array is", arr.shape)

print("Mean of array with axis = 1:",
      np.mean(arr, axis=1))

print("Using nanmedian function:",
      np.nanmean(arr, axis=1))
