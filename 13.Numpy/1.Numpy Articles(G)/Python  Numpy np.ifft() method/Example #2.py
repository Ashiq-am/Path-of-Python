# import numpy
import numpy as np

a = np.array([-5.5, 4.4, -6.6, 3.3, -7.7])
# using np.ifft() method
gfg = np.fft.ifft(a)

print(gfg)
