# import the important module in python
import numpy as np

# make a matrix with numpy
gfg1 = np.matrix('[1, 2, 3, 4]')
gfg2 = np.matrix('[1, 2]')

# applying matrix.any() method
geeks = (gfg1 == gfg2).any()

print(geeks)
