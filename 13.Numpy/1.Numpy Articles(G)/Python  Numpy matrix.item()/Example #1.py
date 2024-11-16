# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[6, 1; 2, 3]')

# applying matrix.item() method
geeks = gfg.item((1, 0))

print(geeks)
