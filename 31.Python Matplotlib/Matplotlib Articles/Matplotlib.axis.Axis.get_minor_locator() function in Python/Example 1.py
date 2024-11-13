# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(2 * x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y)
ax.grid()

print(Axis.get_minor_locator(ax.yaxis))

plt.title("Matplotlib.axis.Axis.get_minor_locator()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
