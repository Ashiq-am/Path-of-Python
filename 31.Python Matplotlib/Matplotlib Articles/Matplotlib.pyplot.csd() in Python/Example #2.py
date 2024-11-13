# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))
nse2 = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse1 = np.convolve(nse1, r, mode='same') * dt
cnse2 = np.convolve(nse2, r, mode='same') * dt

s1 = 1.5 * np.sin(2 * np.pi * 10 * t) + cnse1
s2 = np.cos(np.pi * t) + cnse2 + np.sin(2 * np.pi * 10 * t)

plt.plot(t, s1, t, s2)
plt.xlim(0, 5)
plt.ylabel('s1 and s2')
plt.grid(True)
plt.show()

plt.csd(s1, s2, 256, 1. / dt)
plt.ylabel('CSD(db)')
plt.xlabel('Frequency')

plt.title('matplotlib.pyplot.csd() function Example'
          , fontweight="bold")

plt.show()
