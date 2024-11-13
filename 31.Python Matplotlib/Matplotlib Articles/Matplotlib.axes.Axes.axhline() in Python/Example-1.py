# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as collections

t = np.arange(0.0, 2, 0.01)
s1 = np.sin(4 * np.pi * t)
s2 = 0.75 * np.sin(8 * np.pi * t)

fig, ax = plt.subplots()

ax.plot(t, s1, color ='black')
ax.axhline(0, color ='green', lw = 2)
ax.set_title('matplotlib.axes.Axes.axhline() Example')
plt.show()
