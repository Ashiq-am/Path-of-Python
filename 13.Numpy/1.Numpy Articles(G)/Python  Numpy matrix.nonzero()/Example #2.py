# import the important module in python
import numpy as np

# make a matrix with numpy
gfg = np.matrix('[11, 0, 3; 34, 0, 65; 7, 68, 0]')

# applying matrix.nonzero() method
geeks = gfg.nonzero()

print(geeks)
