# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(9360801)

dt = 0.0005
t = np.arange(0.0, 20.0, dt)
s1 = np.sin(4 * np.pi * 100 * t)
s2 = 1.5 * np.sin(1.5 * np.pi * 400 * t)

s2[t <= 10] = s2[12 <= t] = 0

nse = 0.2 * np.random.random(size = len(t))

x = s1 + s2 + nse
NFFT = 512
Fs = int(1.0 / dt)

fig, ax1 = plt.subplots()
ax1.specgram(x, Fs = Fs, cmap = plt.cm.bone)
ax1.set_title('matplotlib.axes.Axes.specgram() Example')

plt.show()
