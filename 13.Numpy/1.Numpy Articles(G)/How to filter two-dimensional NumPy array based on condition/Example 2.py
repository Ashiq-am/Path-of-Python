import numpy as np


a = np.arange(12).reshape((3, 4))
print(a[:, np.all(a < 10, axis = 0)])
