import pygal

# Create a bar chart with default spacing
bar_chart = pygal.Bar()

# Set the title of bar chart
bar_chart.title = "Weekly sales data"

# Set the labels of x-axis
bar_chart.x_labels = ['Monday', 'Tuesday',
					'Wednesday', 'Thrusday',
					'Friday', 'Saturday',
						'Sunday']

# Add data to bar chart
bar_chart.add('Sales_Data', [5, 8, 12, 6, 10, 9, 4])

# Render the bar chart to SVG file
bar_chart.render_to_file('bar_chart_spacing.svg')
