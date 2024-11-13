# Implementation of matplotlib function
import numpy as np
from matplotlib.axis import Axis
import matplotlib.pyplot as plt

np.random.seed(19680801)

fig, ax = plt.subplots()

x, y, s, c = np.random.rand(4, 100)
s *= 100

ax.scatter(x, y, s, c)
ax.grid()

print(Axis.get_minor_locator(ax.xaxis))

plt.title("Matplotlib.axis.Axis.get_minor_locator()\n\
Function Example", fontsize=12, fontweight='bold')
plt.show()
