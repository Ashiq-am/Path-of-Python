# import numpy
import numpy as np

a = np.array([[12, -13j], [4j, 8]])
# using np.cholesky() method
gfg = np.linalg.cholesky(a)

print(gfg)
