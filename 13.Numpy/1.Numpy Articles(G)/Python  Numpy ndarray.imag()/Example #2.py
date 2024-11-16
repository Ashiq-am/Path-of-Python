# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.array([1 + 2j, 2 + 3j])
gfg = np.sqrt(gfg)

# applying ndarray.imag() method
geeks = np.imag(gfg)

print(geeks, end='\n\n')
print(np.imag(geeks).dtype)
