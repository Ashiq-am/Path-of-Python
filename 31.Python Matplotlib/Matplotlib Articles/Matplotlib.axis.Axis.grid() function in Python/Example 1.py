# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3])
ax.xaxis.grid()

fig.suptitle("Matplotlib.axis.Axis.grid()\
Function Example", fontsize=12, fontweight='bold')

plt.show()
