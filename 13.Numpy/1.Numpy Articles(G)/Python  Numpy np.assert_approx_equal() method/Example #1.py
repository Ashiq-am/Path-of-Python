# import numpy and assert_approx_equal
import numpy as np
import numpy.testing as npt

# using np.assert_approx_equal() method
gfg = npt.assert_approx_equal(1.2222222222, 1.2222222222, significant = 5)

print(gfg)
