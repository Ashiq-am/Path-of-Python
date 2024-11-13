# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from numpy.random import rand

fig, ax2 = plt.subplots()

ax2.bar(range(10), rand(10), picker=True)

print("Value return : \n", *list(Axis.findobj(ax2)), sep="\n")

fig.suptitle("""matplotlib.axis.Axis.findobj() 
function Example\n""", fontweight="bold")

plt.show()
