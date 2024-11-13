# importing matplotlib package
import matplotlib.pyplot as plt

# importing LassoSelector from
# Matplotlib.widgets
from matplotlib.widgets import LassoSelector

# Creating a figure of the plot
fig = plt.figure()

# Add set of axes to figure(Manually)
# left, bottom, width, height (ranging in between 0 and 1)
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Set the label of X-Axis
axes.set_xlabel('X-axis')

# Set the label of Y-Axis
axes.set_ylabel('Y-Axis')

# Set the title of the plot
axes.set_title('LassoSelector-Demo-Widget')

# OnSelect function:Gets triggered
# as soon as the mouse is pressed
# in the plot
def onSelect(geeksforgeeks):
	print(geeksforgeeks)

# line defines the color, width and opacity
# of the line to be drawn
line = {'color': 'green',
		'linewidth': 8, 'alpha': 1}

# Three parameters are passed inside the lasso
# Selector class defining the axis, line
# property and on select function
lsso = LassoSelector(ax=axes, onselect=onSelect, lineprops=line, button=2)

# Show the above plot
plt.show()
