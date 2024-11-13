# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from numpy.random import rand

fig, ax2 = plt.subplots()

ax2.hexbin(range(10), rand(10), picker=True)

print("First 10 child Artists of this Artist \n",
	*list(ax2.get_children())[:10], sep="\n")

fig.suptitle("""matplotlib.axis.Tick.get_children()
function Example\n""", fontweight="bold")

plt.show()
