# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

dt = 0.005
t = np.arange(0.0, 20.0, dt)
x = np.sin(np.pi * t) + 1.5 * np.cos(np.pi * t)

fig, ax1 = plt.subplots()
ax1.specgram(x, Fs = 1)
ax1.set_title('matplotlib.axes.Axes.specgram() Example')

plt.show()
