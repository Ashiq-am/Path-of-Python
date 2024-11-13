# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3])

ax.xaxis.pan(3)

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.pan() 
function Example\n""", fontweight="bold")

plt.show()
