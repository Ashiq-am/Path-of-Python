# import scipy
from scipy import fft

# Using scipy.fft.dst() method
gfg = fft.dst([-6, 5, -4, 3, -2, 1], 3)

print(gfg)
