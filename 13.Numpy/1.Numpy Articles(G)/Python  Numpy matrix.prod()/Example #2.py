# import the important module in python
import numpy as np

# make a matrix with numpy
gfg = np.matrix('[1, 2, 3; 4, 5, 6; 7, 8, -9]')

# applying matrix.prod() method
geeks = gfg.prod(0)

print(geeks)
