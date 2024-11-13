# import scipy and numpy
import scipy
import numpy as np

x = np.arange(10)
# Using scipy.fftfreq() method
gfg = scipy.fft.rfft(x)

print(gfg)
