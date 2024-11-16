# import numpy
import numpy as np

a = np.array([[-5.5, 4.4, -6.6, 3.3, -7.7], [1.1, -3.3, 4.4, -7.7, 0]])
# using np.ifft2() method
gfg = np.fft.ifft2(a)

print(gfg)
