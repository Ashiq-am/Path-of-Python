# import numpy
import numpy as np

# using numpy.assert_allclose() method
gfg1 = [1, 2, 3]
gfg2 = np.array(gfg1)

if np.testing.assert_allclose(gfg1, gfg2):
	print("Matched")
