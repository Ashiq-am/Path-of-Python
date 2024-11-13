# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt

s1 = np.cos(np.pi * t) + cnse1 + np.sin(2 * np.pi * 10 * t)

plt.psd(s1, 2 ** 14, dt)
plt.ylabel('PSD(db)')
plt.xlabel('Frequency')
plt.title('matplotlib.pyplot.psd() Example\n',
          fontsize=14, fontweight='bold')

plt.show()
