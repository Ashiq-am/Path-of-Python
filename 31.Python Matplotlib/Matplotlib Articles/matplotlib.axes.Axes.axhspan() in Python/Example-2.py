# Implementation of matplotlib function
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-2, 3, .01)
s = np.sin(np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s, color ='black')
ax.axhline(y = 1, color ='black')
ax.axvline(x = 1, color ='black')
ax.axvline(x = 0, ymin = 0.75, linewidth = 8, color ='green')
ax.axhline(y =.5, xmin = 0.25, xmax = 0.75, color ='black')

ax.axhspan(0.25, 0.75, facecolor ='0.5', alpha = 0.5)
ax.axvspan(1.25, 1.55, facecolor ='green', alpha = 0.5)

ax.set_title('matplotlib.axes.Axes.axhspan() Example')

plt.show()
