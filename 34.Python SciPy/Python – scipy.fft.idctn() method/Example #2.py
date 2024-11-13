# import scipy and numpy
from scipy import fft
import numpy as np

array_gfg = np.random.randn(4, 2)

# Using scipy.fft.idctn() method
gfg = fft.idctn(array_gfg, 4)

print(gfg)
