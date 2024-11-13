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
ax.grid()

print("Value of get_gridlines() :")
for i in ax.yaxis.get_gridlines():
    print(i)

fig.suptitle("Matplotlib.axis.Axis.get_gridlines()\
Function Example", fontsize=12, fontweight='bold')

plt.show()
