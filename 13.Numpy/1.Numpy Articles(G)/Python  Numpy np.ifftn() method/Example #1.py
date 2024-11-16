# import numpy
import numpy as np

a = np.array([-1, 3, -4, 7, 0])

# using np.ifftn() method
gfg = np.fft.ifftn(a)

print(gfg)
