# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.linspace(0, 4 * np.pi, 100)
y = 2 * np.sin(x)

ax = fig.add_subplot()
ax.plot(x, y)

ax.xaxis.set_data_interval(2, 4, True)

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.set_data_interval() 
function Example\n""", fontweight="bold")

plt.show()
