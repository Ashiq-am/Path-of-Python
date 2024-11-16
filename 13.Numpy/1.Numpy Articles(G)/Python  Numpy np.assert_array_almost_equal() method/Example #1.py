# import numpy and assert_array_almost_equal
import numpy as np
import numpy.testing as npt

# using np.assert_array_almost_equal() method
gfg = npt.assert_array_almost_equal([0.2222, 1.2222], [0.2222, 1.2222], decimal = 3)

print(gfg)
