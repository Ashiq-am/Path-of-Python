# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots()

x, y, s, c = np.random.rand(4, 200)
s *= 200

ax.scatter(x, y, s, c)
ax.grid()

print(Axis.get_major_formatter(ax.xaxis))

plt.title("Matplotlib.axis.Axis.get_major_formatter()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
