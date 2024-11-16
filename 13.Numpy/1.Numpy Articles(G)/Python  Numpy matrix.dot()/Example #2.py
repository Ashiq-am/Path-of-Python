# import the important module in python
import numpy as np

# make a matrix with numpy
gfg1 = np.matrix('[1, 2, 3; 4, 5, 6; 7, 8, 9]')
gfg2 = np.matrix('[1, 2, 3; 4, 5, 6; 7, 8, 9]')

# applying matrix.dot() method
geeks = gfg1.dot(gfg2)

print(geeks)
