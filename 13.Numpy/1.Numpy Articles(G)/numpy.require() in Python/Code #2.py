import numpy as np

# Python program explaining
# numpy.require()
from numpy.random.tests import data

b = np.require(data, dtype=np.float32,
			requirements=['A', 'W', 'O', 'C'])
b.flags
