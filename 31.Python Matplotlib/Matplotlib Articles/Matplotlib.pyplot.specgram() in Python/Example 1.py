# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

dt = 0.005
t = np.arange(0.0, 20.0, dt)
x = np.sin(np.pi * t) + 1.5 * np.cos(np.pi * 2 * t)

plt.specgram(x, Fs=1)
plt.title('matplotlib.pyplot.specgram() Example\n',
          fontsize=14, fontweight='bold')

plt.show()
