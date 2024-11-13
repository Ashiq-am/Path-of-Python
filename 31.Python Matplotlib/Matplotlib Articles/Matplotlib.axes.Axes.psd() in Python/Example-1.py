# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))

s1 = 1.5 * np.sin(2 * np.pi * 10 * t) + nse1 + np.cos(np.pi * t)

fig, ax1 = plt.subplots()
ax1.psd(s1**2, 512, 1./dt, color ="green")
ax1.set_xlabel('Frequency')
ax1.set_ylabel('PSD(db)')

ax1.set_title('matplotlib.axes.Axes.psd() Example')
plt.show()
