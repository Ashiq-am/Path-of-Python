# Implementation of matplotlib function
from matplotlib.axis import Axis
import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
y2 = y + 0.2 * np.random.normal(size=x.shape)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y2)

ax.set_xticks([0, np.pi, 2 * np.pi])
ax.set_xticklabels(['0', r'$\pi$', r'2$\pi$'])

for line in ax.yaxis.get_ticklines():
    # line is a Line2D instance
    line.set_color('tab:green')
    line.set_markersize(25)
    line.set_markeredgewidth(3)

ax.spines['left'].set_bounds(-1, 1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig.suptitle('Matplotlib.axis.Axis.get_ticklines()\n\
Function Example', fontweight="bold")
ax.grid()

plt.show()
