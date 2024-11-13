# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)

dt = 0.01
Fs = 1 / dt
t = np.arange(0, 10, dt)
res = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cres = np.convolve(res, r)*dt
cres = cres[:len(t)]
s = 0.5 * np.sin(1.5 * np.pi * t) + cres

# plot simple spectrum
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, s, color ="green")

# plot magnitude_spectrum
ax2.magnitude_spectrum(s, Fs = Fs,
					color ="green")

ax1.set_title('matplotlib.axes.Axes.magnitude_spectrum() Example')

plt.show()
