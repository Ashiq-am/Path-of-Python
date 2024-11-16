import numpy as np


a = np.arange(12).reshape((3, 4))
print(a[:, np.any(a < 2, axis = 0)])
