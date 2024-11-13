# import scipy
from scipy import fft

# Using scipy.fft.idct() method
gfg = fft.idct([0.95238737, -0.80969772, 0.7286317, -0.82132135], 4)

print(gfg)
