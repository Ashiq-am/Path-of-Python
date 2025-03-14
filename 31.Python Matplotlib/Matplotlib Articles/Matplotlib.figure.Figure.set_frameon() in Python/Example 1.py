# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

fig.set_frameon(True)

fig.suptitle("""matplotlib.figure.Figure.set_frameon() 
function Example\n\n""", fontweight="bold")

plt.show()
