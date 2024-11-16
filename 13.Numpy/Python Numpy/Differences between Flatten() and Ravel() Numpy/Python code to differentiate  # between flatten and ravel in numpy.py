# Python code to differentiate
# between flatten and ravel in numpy
import numpy as np

# Create a numpy array
a = np.array([(1,2,3,4),(3,1,4,2)])

# Let's print the array a
print ("Original array:\n ")
print(a)

# To check the dimension of array (dimension =2) ( and type is numpy.ndarray )
print ("Dimension of array-> " , (a.ndim))


print("\nOutput for RAVEL \n")
# Convert nd array to 1D array
b = a.ravel()

# Ravel only passes a view of original array to array 'b'
print(b)
b[0]=1000
print(b)

# Note here that value of original array 'a' at also a[0][0] becomes 1000
print(a)

# Just to check the dimension i.e. 1 (and type is same numpy.ndarray )
print ("Dimension of array->" ,(b.ndim))

print("\nOutput for FLATTEN \n")

# Convert nd array to 1D array
c = a.flatten()

# Flatten passes copy of original array to 'c'
print(c)
c[0]=0
print(c)

# Note that by changing value of c there is no affect on value of original array 'a'
print(a)

print ("Dimension of array-> " , (c.ndim))
