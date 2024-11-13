# Implementation of matplotlib function
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
plt.title('matplotlib.pyplot.magnitude_spectrum() function Example',
												fontweight ="bold")

plt.subplot(2, 1, 2)
plt.magnitude_spectrum(s, Fs = Fs)

plt.show()
