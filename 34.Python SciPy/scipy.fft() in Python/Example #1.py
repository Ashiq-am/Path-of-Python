# import scipy and numpy
import scipy
import numpy as np

x = np.array(np.arange(10))
# Using scipy.fft() method
gfg = scipy.fft(x)

print(gfg)
