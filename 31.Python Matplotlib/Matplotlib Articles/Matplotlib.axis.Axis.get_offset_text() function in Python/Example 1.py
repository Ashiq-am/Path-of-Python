# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
import matplotlib.text

fig, ax = plt.subplots()

ax.plot([5, 1], label="Label 1")
ax.plot([3, 0], label="Label 2")

legend = ax.legend(loc="upper right")
offset = matplotlib.text.OffsetFrom(legend, (1.0, 0.0))

ax.annotate("String - Info",
            xy=(0, 0),
            size=14,
            xycoords='figure fraction',
            xytext=(0, -20),
            textcoords=offset,
            horizontalalignment='right',
            verticalalignment='top')

fig.canvas.draw()
fig.suptitle('Matplotlib.axis.Axis.get_offset_text()\n\
Function Example')
ax.grid()

print("Value of get_offset_text() :", ax.xaxis.get_offset_text())

plt.show()
