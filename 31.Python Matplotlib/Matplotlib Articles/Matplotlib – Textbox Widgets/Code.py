# Import modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# Adjust illustration
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-4.0, 4.0, 0.01)
l, = ax.plot(t, np.zeros_like(t), lw=2)

# Function to plot graph
# according to expression
def visualizeGraph(expr):
	ydata = eval(expr)
	l.set_ydata(ydata)
	ax.relim()
	ax.autoscale_view()
	plt.draw()

# Adding TextBox to graph
graphBox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
txtBox = TextBox(graphBox, "Plot: ")
txtBox.on_submit(visualizeGraph)
txtBox.set_val("t**5")

# Plot graph
plt.show()
