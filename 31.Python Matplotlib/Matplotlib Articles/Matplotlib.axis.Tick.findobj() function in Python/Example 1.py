# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from numpy.random import rand

fig, ax2 = plt.subplots()

ax2.bar(range(10), rand(10), picker=True)

print("Value return : \n",
      *list(Tick.findobj(ax2)), sep="\n")

fig.suptitle("""matplotlib.axis.Tick.findobj() 
function Example\n""", fontweight="bold")

plt.show()
