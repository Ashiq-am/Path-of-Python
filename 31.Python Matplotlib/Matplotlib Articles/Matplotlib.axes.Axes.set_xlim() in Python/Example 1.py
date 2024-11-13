# Implementation of matplotlib function
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots(facecolor='#A0F0CC')

x, y = 4 * (np.random.rand(2, 100) - .5)
ax.plot(x, y, 'g')
ax.set_xlim(-3, 3)

cursor = Cursor(ax, useblit=True, color='red',
                linewidth=2)

ax.set_title('matplotlib.axes.Axes.set_xlim() \
Example\n', fontsize=14, fontweight='bold')
plt.show()
