import numpy as np


nparray = np.array([[1, 2, 3], [11, 22, 33],
					[4, 5, 6], [8, 9, 10],
					[20, 30, 40]])
nparray = nparray.reshape(-1, 3)
print(nparray)

# calculating sum along axix=0
# i.e column-wise
output = nparray.sum(axis = 0)
print("\n\nSum column-wise: ", output)
