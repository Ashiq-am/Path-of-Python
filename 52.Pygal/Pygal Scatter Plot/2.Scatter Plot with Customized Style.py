# Import pygal module
import pygal

# Create a scatter plot object
# XY for scatter plot, stroke=False
# to disable line connecting points
scatter_chart = pygal.XY(stroke=False)

# Set title of Graph
scatter_chart.title = 'Employee Salary Vs Age graph'

# Create a Sample data for the scatter plot
hr_data = [(10, 20000), (25, 30000), (30, 40000), (40, 50000), (53, 60000)]
sales_data = [(14, 10000), (20, 25000), (35, 30000), (44, 40000), (50, 55000)]

# Adding data to scatter plot
scatter_chart.add('HR Dept', hr_data)
scatter_chart.add('Sales Dept', sales_data)

# Set title to x-axis and y-axis
scatter_chart.x_title = 'Age'
scatter_chart.y_title = 'Salary'

# Customized the graph theme from light to dark
scatter_chart.style = pygal.style.DarkStyle

# Save the scatter plot to file
scatter_chart.render_to_file('scatterPlot.svg')
