# Implementation of matplotlib function
from matplotlib.axis import Tick
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [0, 2]
y = [2, 1]
line, = ax.plot(x, y)

ax.legend(("Line_1",))

ax.text(0.2, 1.02, "Value Return by get_label()\
: " + str(line.get_label()))

fig.suptitle("""matplotlib.axis.Tick.get_label()
function Example\n""", fontweight="bold")

plt.show()
