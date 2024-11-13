# import scipy
from scipy import fft

# Using scipy.fft.idst() method
gfg = fft.idst([-6, 5, -4, 3, -2, 1], 3)

print(gfg)
