import numpy as np


# create numpy arrays
# 1-d numpy array
_1darr = np.arange(4)

# 2-d numpy array
_2darr = np.arange(15).reshape((5, 3))

# 3-d numpy array
_3darr = np.arange(18).reshape((3, 2, 3))

# printing the type of value obtained using
# attribute 'ndim'
print("Type of value obtained: ", type(_1darr.ndim))

# printing the dimensions of each numpy array
print("Dimensions in _1darr are: ", _1darr.ndim)
print("Dimensions in _2darr are: ", _2darr.ndim)
print("Dimensions in _3darr are: ", _3darr.ndim)

# numpy_arr.shape is the number of elements in
# each dimension numpy_arr.shape returns a tuple
# len() of the returned tuple is also gives number
# of dimensions
print("Dimensions in _3darr are: ", len(_3darr.shape))

# Use numpy.array() function to convert a list to
# numpy array
__1darr = np.array([5, 4, 1, 3, 2])
__2darr = np.array([[5, 4],[1,2], [4,5]])
print("Dimensions in __1darr are: ", __1darr.ndim)
print("Dimensions in __2darr are: ", __2darr.ndim)
