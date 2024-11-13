# Implementation of matplotlib function
from matplotlib.axis import Tick
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

x = np.linspace(0, 4 * np.pi)
y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure()

ax = fig.add_subplot(111)
ax.plot(x, y1, c='b', label='y1', linewidth=1.0)
ax.plot(x, y2, c='g', label='y2')

linewidth = 7


def update(prop1, prop2):
    Tick.update_from(prop1, prop2)
    prop1.set_linewidth(7)


plt.legend(handler_map={plt.Line2D: HandlerLine2D(update_func=update)})

ax.set_title('matplotlib.axis.Tick.update_from() \
function Example', fontweight="bold")

plt.show()
