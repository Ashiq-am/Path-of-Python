# Import Pygal module
import pygal

# Sample data for positive and negative values dot chart
margins = {
	'Java Backend': -10,
	'System Design': 5,
	'DSA Self Paced': 15,
	'CP': -5,
	'CIP': 8
}

# Create a dot chart object
dot_chart_margins = pygal.Dot()

# Add data to the dot chart
for department, profit_margin in margins.items():
	dot_chart_margins.add(department, profit_margin)

# Customize the chart and set titles
dot_chart_margins.title = 'Profit Margins of Courses'
dot_chart_margins.x_title = 'Courses'
dot_chart_margins.y_title = 'Profit Margin (%)'

# Save the dot chart to a file
dot_chart_margins.render_to_file('course_margins.svg')
