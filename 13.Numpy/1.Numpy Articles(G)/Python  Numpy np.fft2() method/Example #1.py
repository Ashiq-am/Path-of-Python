# import numpy
import numpy as np

a = np.array([[5, 4, 6, 3, 7], [-1, -3, -4, -7, 0]])
# using np.fft2() method
gfg = np.fft.fft2(a)

print(gfg)
