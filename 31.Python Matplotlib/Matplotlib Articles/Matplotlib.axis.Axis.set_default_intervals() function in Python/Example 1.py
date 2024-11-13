# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.linspace(0, 4 * np.pi, 100)
y = 2 * np.sin(x)

ax = fig.add_subplot()
ax.plot(x, y)

ax.xaxis.set_default_intervals()

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.set_default_intervals() 
function Example\n""", fontweight="bold")

plt.show()
