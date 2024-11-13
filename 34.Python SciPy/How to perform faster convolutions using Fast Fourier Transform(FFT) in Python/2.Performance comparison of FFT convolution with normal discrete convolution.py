import timeit

import numpy as np
from scipy import signal

a = np.random.randn(10**5)
b = np.random.randn(10**5)

print('Time required for normal discrete convolution:')
timeit.np.convolve(a, b)

print('Time required for FFT convolution:')
timeit.signal.fftconvolve(a, b)
