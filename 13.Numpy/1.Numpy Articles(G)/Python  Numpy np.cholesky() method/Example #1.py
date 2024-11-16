# import numpy
import numpy as np

a = np.array([[2, -3j], [5j, 15]])
# using np.cholesky() method
gfg = np.linalg.cholesky(a)

print(gfg)
