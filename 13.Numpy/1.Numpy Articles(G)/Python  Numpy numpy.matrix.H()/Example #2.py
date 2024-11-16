# import the important module in python
import numpy as np

# make a matrix with numpy
gfg = np.matrix([[1 - 5j, 2 + 5j, 3 - 3j], [4 + 6j, 5 - 8j, 6 - 2j], [7 + 6j, 8 - 6j, 9 + 1.j]])

# applying matrix.H() method
geeks = gfg.getH()

print(geeks)
