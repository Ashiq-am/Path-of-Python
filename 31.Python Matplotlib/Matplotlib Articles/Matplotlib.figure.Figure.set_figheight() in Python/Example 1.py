# Implementation of matplotlib function
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.axisartist.axislines import Subplot
import numpy as np

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

fig.set_figheight(7.6)

fig.suptitle("""matplotlib.figure.Figure.set_figheight() 
function Example\n\n""", fontweight="bold")

plt.show()
