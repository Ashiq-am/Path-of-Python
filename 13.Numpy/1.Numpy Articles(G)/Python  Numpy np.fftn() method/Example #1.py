# import numpy
import numpy as np

a = np.array([-1, 3, -4, 7, 0])
# using np.fftn() method
gfg = np.fft.fftn(a)

print(gfg)
