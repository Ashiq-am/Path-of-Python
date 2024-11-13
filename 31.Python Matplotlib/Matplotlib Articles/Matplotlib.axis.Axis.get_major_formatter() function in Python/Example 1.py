# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = 0.000001 * np.sin(10 * x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y)

print(Axis.get_major_formatter(ax.yaxis))

plt.title("Matplotlib.axis.Axis.get_major_formatter()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
