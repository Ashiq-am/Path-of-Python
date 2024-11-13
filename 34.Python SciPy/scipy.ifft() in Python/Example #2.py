# import scipy and numpy
import scipy
import numpy as np

x = np.array(np.arange(5))
gfg_transformed = scipy.fft(x)
# Using scipy.ifft() method
gfg_inversed = scipy.ifft(gfg_transformed)

print(gfg_inversed)
