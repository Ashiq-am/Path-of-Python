import pygal

# Create a bar chart with custom Bottom margin
bar_chart = pygal.Bar(margin_bottom=100)

# Set the title of bar chart
bar_chart.title = "Weekly sales data"
bar_chart.x_title = "Week days"

# Set the labels of x-axis
bar_chart.x_labels = ['Monday', 'Tuesday',
					'Wednesday', 'Thrusday',
					'Friday', 'Saturday',
						'Sunday']

# Add data to bar chart
bar_chart.add('Sales_Data', [5, 8, 12, 6, 10, 9, 4])

# Render the bar chart to SVG file
bar_chart.render_to_file('bar_chart_margin.svg')
