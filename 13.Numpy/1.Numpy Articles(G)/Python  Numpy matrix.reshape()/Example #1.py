# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[64, 1; 12, 3]')

# applying matrix.reshape() method
geeks = gfg.reshape((1, 4))

print(geeks)
