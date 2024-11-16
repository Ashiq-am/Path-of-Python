# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.array([1 + 2j, 2 + 3j])

# applying ndarray.real() method
geeks = np.real(gfg)

print(geeks, end='\n\n')
print(np.real(geeks).dtype)
