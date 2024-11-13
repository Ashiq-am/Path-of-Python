# importing matplotlib package
import matplotlib.pyplot as plt

# importing LassoSelector from
# Matplotlib.widgets
from matplotlib.widgets import LassoSelector

# Creating a Subplot in matplotlib
fig, axes = plt.subplots()

# Set the label of X-Axis
axes.set_xlabel('X-axis')

# Set the label of Y-Axis
axes.set_ylabel('Y-Axis')

# Set the title of the plot
axes.set_title('LassoSelector-Demo-Widget with axes created automatically with subplots')

# onSelect function gets triggered
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
lsso = LassoSelector(ax=axes, onselect=onSelect,
					lineprops=line, button=2)

# If you want to print x and y while pressing
# and releasing mouse, then use mpl_connect
# and replace pressed and released with event

# Shows the above plot
plt.show()
