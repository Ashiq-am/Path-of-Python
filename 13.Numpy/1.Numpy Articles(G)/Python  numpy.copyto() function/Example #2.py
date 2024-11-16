# import the important module in python
import numpy as np

# make an array with numpy
gfg = np.array([[1, 2, 3], [4, 5, 6]])
geeks = [[4, 5, 6], [7, 8, 9]]

# applying numpy.copyto() method
np.copyto(gfg, geeks)

print(gfg)
