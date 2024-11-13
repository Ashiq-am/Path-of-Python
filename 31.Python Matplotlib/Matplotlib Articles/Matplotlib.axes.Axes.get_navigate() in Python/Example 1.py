# Implementation of matplotlib function
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np

fig, ax = plt.subplots()

xx = np.arange(0, 2 * np.pi, 0.01)
ax.plot(xx, np.sin(xx))

ax.set_navigate(False)
w = ax.get_navigate()

ax.text(2, 0, "Value Return : " + str(w),
        fontweight="bold")

fig.suptitle('matplotlib.axes.Axes.get_navigate() function\
Example\n\n', fontweight="bold")

plt.show()
