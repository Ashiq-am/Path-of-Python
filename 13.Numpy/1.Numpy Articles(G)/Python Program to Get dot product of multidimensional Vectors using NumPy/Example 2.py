# import numpy
import numpy as np

# initialize vectors
a = np.array([[3,9],
			[2,5]])
b = np.array([[6,1],
			[4,8],
			[7,5]])
print("Shape of vector a: ",a.shape)
print("Shape of vector b: ",b.shape)

# calculating Dot product using np.dot
c = np.dot(a,b)
print("Dot product of a and b is:\n",c)
