# import the important module in python
import numpy as np

# make a matrix with numpy
gfg = np.matrix('[1, 2, 3; 4, 5, 6; 7, 8, 9]')

# applying matrix.compress() method
geeks = np.compress([1, 0, 1, 1, 1, 0, 0, 1, 1], gfg)

print(geeks)
