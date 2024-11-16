# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[64, 1; 0, 3]')

# applying matrix.nonzero() method
geeks = gfg.nonzero()

print(geeks)
