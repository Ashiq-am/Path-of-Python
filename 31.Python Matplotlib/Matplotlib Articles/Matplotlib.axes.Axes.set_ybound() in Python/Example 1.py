# Implementation of matplotlib function
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots()

x, y = 4 * (np.random.rand(2, 50) - .5)
ax.plot(x, y, 'g')
ax.set_ybound(-4, 4)

ax.set_title('matplotlib.axes.Axes.set_ybound() Example\n',
             fontsize=14, fontweight='bold')
plt.show()
