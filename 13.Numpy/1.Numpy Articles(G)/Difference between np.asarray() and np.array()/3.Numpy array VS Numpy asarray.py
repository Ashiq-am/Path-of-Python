import numpy as np

# craeting array
a = np.array([ 2, 3, 4, 5, 6])
print("Original array : ",a)

# assigning value to np.array
np_array = np.array(a)
a[3] = 0
print("np.array Array : ",np_array)

# asigning value to np.asarray
np_array = np.asarray(a)
a[3] = 0
print("np.asarray Array : ",np_array)
