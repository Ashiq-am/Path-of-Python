# import library
import numpy as np

# create a numpy 3d-array
array = np.array([
    [[1, -2, 3],
     [-4, 5, -6]],

    [[-7.5, -8.22, 9.0],
     [10.0, 11.5, -12.5]]
])

print("Given array:\n",
      array)

# find element-wise
# absolute value
rslt = np.absolute(array)

print("Absolute array:\n",
      rslt)
