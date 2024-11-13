# import pygal module
import pygal

# Create scatter plot object
scatter_plot = pygal.XY(stroke=False)

# Set title for scatter plot
scatter_plot.title = 'Happiness Index VS Income per person'

# Set title for x-axis and y-axis
scatter_plot.x_title = 'Average Happiness score'
scatter_plot.y_title = 'Average Income per person'

# Create sample data
data = [(10, 20000), (20, 39000),
		(30, 43000), (40, 55000),
		(50, 60000), (40,20000),
		(70, 95000), (80, 79000),
		(55, 55000), (65, 75000),
		(85, 98000), (45,35000)]

# Add data to scatter plot
scatter_plot.add('Series', data)

# Save plot to a file
scatter_plot.render_to_file('scatter_plot.svg')
