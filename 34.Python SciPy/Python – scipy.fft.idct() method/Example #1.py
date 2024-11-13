# import scipy
from scipy import fft

# Using scipy.fft.idct() method
gfg = fft.idct([0.1, 2.1, 0.3, 4.2])

print(gfg)
