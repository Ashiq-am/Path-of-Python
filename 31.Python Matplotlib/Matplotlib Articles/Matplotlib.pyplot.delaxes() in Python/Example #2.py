# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt

s1 = np.cos(np.pi * t) + cnse1 + np.sin(2 * np.pi * 10 * t)

fig, [ax1, ax2] = plt.subplots(2, 1)
ax1.plot(t, s1)
ax1.set_xlim(0, 5)
ax1.set_ylabel('value s1')
ax1.grid(True)

ax2.psd(s1, 256, 1. / dt)
ax2.set_ylabel('PSD(db)')
ax2.set_xlabel('Frequency')

plt.delaxes(ax=ax1)

plt.suptitle('matplotlib.pyplot.delaxes() function Example',
             fontweight="bold")

plt.show()
