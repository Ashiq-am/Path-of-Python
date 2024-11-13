# Implementation of matplotlib function
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(19680801)

fig, ax = plt.subplots()

x = 2 * np.cos(2 * np.pi*(np.arange(-3, 3, 0.005)))
y = 2 * np.sin(2 * np.pi*(np.arange(0, 6, 0.005)))
ax.plot(x, y, 'g')
ax.set_xbound(-4, 4)

ax.set_title('matplotlib.axes.Axes.set_xbound() Example\n', fontsize = 14, fontweight ='bold')
plt.show()
