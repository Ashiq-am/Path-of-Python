# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from numpy.random import rand

fig, ax2 = plt.subplots()

ax2.bar(range(10), rand(10), picker=True)

print("List of the child Artists of this Artist \n",
      *list(ax2.get_children()), sep="\n")

fig.suptitle("""matplotlib.axis.Axis.get_children() 
function Example\n""", fontweight="bold")

plt.show()
