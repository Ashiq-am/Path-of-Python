# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)

ax = fig.add_subplot()
ax.plot(x, y)
ax.yaxis.set_ticks([1, 2, 3, 4, 5, 6, 7])

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.set_ticks() 
function Example\n""", fontweight="bold")

plt.show()
