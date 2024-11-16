import numpy as np
# 1-D array having elements [1 2 3 4 5 6 7 8]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Print the 1-D array
print ('Before reshaping:')
print (arr)
print ('\n')

# Now we can convert this 1-D array into 2-D in two ways

# 1. having dimension 4 x 2
arr1 = arr.reshape(4, 2)
print ('After reshaping having dimension 4x2:')
print (arr1)
print ('\n')

# 2. having dimension 2 x 4
arr2 = arr.reshape(2, 4)
print ('After reshaping having dimension 2x4:')
print (arr2)
print ('\n')
