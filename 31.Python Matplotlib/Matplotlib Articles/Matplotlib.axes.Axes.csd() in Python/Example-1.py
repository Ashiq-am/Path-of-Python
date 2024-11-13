# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))
nse2 = np.random.randn(len(t))

s1 = 1.5 * np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.cos(np.pi * t) + nse2

fig, ax1 = plt.subplots()
ax1.csd(s1, s2**2, 128, 1./dt)
ax1.set_xlabel('Frequency')
ax1.set_ylabel('CSD(db)')

ax1.set_title('matplotlib.axes.Axes.csd() Example')
plt.show()
