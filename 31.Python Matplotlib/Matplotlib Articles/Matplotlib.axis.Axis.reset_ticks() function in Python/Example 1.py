# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.gridspec as gridspec
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"
plt.rcParams['figure.figsize'] = 6, 5

fig, ax = plt.subplots()

ax.plot([1, 2])

ax.locator_params("x", nbins=3)
ax.locator_params("y", nbins=5)

ax.set_xlabel('x-label')
ax.set_ylabel('y-label')

ax.yaxis.reset_ticks()

ax.grid()

fig.suptitle("""matplotlib.axis.Axis.reset_ticks() 
function Example\n""", fontweight="bold")

plt.show()
