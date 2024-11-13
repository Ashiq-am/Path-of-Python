# import scipy
from scipy import fft

# Using scipy.fft.dct() method
gfg = fft.dct([-6, 5, -4, 3, -2, 1], 3)

print(gfg)
