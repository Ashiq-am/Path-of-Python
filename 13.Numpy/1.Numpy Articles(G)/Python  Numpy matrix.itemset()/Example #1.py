# import the important module in python
import numpy as np

# make matrix with numpy
gfg = np.matrix('[6, 1; 2, 3]')

# applying matrix.itemset() method
gfg.itemset((1, 0), 5)

print(gfg)
