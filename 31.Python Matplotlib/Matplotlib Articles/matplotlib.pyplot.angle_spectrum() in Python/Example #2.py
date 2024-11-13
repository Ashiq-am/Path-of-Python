# Implementation of matplotlib.pyplot.angle_spectrum()
# function

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

dt = 0.01
Fs = 1 / dt
t = np.arange(0, 10, dt)
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse = np.convolve(nse, r)*dt
cnse = cnse[:len(t)]
s = 0.1 * np.sin(2 * np.pi * t) + cnse

# plot simple spectrum
plt.subplot(2, 1, 1)
plt.plot(t, s)

# plot angle_spectrum
plt.subplot(2, 1, 2)
plt.angle_spectrum(s, Fs = Fs)

# Display the simple spectrum and
# angle_spectrum plot
plt.show()
