# import scipy and numpy
import scipy
import numpy as np

x = np.arange(11)
# Using scipy.fftfreq() method
gfg = scipy.fft.fftshift(x)

print(gfg)
