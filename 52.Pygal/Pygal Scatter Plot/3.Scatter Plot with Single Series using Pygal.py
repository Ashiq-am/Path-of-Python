import pygal

# Create a Sample data for the scatter plot
data = [
	{'x': 1, 'y': 5},
	{'x': 2, 'y': 3},
	{'x': 3, 'y': 7},
	{'x': 4, 'y': 2},
	{'x': 5, 'y': 8},
	{'x': 6, 'y': 4},
	{'x': 7, 'y': 6},
	{'x': 8, 'y': 9},
	{'x': 9, 'y': 2},
	{'x': 10, 'y': 5}
]

# Create a scatter plot object
# XY for scatter plot, stroke=False
# to disable line connecting points
scatter_plot = pygal.XY()

# Add data to the scatter plot
for point in data:
	scatter_plot.add('Data',
					[(point['x'],
					point['y'])])

# Customize the chart
scatter_plot.title = 'Sample Scatter Plot'
scatter_plot.x_title = 'X-axis'
scatter_plot.y_title = 'Y-axis'

# Disable the legend
scatter_plot.show_legend = False

# Set custom labels for the X-axis
scatter_plot.x_labels = map(str, range(1, 11))

# Save the scatter plot to a file in svg format
scatter_plot.render_to_file('scatter_plot.svg')

# Below line to used render the plot in the browser
# scatter_plot.render_in_browser()
