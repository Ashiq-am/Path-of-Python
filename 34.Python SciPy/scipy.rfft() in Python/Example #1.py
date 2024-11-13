# import scipy and numpy
import scipy
import numpy as np

x = np.arange(5)
# Using scipy.fftfreq() method
gfg = scipy.fft.rfft(x)

print(gfg)
