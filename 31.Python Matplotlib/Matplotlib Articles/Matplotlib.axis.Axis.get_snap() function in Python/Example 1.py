# Implementation of matplotlib function
from matplotlib.axis import Axis
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import Subplot

fig = plt.figure()

ax = Subplot(fig, 111)
fig.add_subplot(ax)

ax.axis["left"].set_visible(False)
ax.axis["top"].set_visible(False)

ax.text(0.3, 0.5, "Snap Setting : "
        + str(Axis.get_snap(ax)),
        fontweight="bold")

fig.suptitle("""matplotlib.axis.Axis.get_snap() 
function Example\n""", fontweight="bold")

plt.show()
