# Implementation of matplotlib function
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np

fig = plt.figure(figsize =(4, 3))

# Zero is the base
ax = SubplotZero(fig, 1, 1, 1)
fig.add_subplot(ax)

xx = np.arange(0, 2 * np.pi, 0.01)
ax.plot(xx, np.sin(xx))

fig.suptitle('matplotlib.axes.SubplotBase() class Example\n\n',
			fontweight ="bold")

plt.show()
