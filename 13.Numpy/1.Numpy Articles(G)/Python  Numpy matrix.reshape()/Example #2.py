# import the important module in python
import numpy as np

# make a matrix with numpy
gfg = np.matrix('[1, 2; 4, 5; 7, 8]')

# applying matrix.reshape() method
geeks = gfg.reshape((2, 3))

print(geeks)
