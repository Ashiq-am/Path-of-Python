# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[64, 1; 12, 3]')

# applying matrix.prod() method
geeks = gfg.prod(1)

print(geeks)
