# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as collections

t = np.arange(0.0, 5, 0.01)
s1 = np.sin(4 * np.pi * t)

fig, ax = plt.subplots()

ax.plot(t, s1, color ='black', alpha = 0.75, lw = 1)
ax.axvline(3, color ='green', lw = 2, alpha = 0.75)
ax.set_title('matplotlib.axes.Axes.axvline() Example')
plt.show()
