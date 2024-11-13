# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np

fig = plt.figure(facecolor="lightgreen")

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis["left"].set_visible(False)
ax.axis["top"].set_visible(False)

fig.set_dpi(90.0)

fig.suptitle("""matplotlib.figure.Figure.set_dpi() 
function Example\n\n""", fontweight="bold")

plt.show()
