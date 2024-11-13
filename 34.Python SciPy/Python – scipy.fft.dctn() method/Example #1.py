# import scipy and numpy
from scipy import fft
import numpy as np

array_gfg = np.random.randn(3, 3)

# Using scipy.fft.dctn() method
gfg = fft.dctn(array_gfg)

print(gfg)
