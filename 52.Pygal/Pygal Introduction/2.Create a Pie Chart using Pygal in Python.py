# importing pygal
import pygal

# Creating Pie chart object
pie_chart = pygal.Pie()

# Set the title of pie chart
pie_chart.title = '% of different section in SDE Interview'


# Add data to pie chart
pie_chart.add('Aptitude', 10)
pie_chart.add('OOPs', 20)
pie_chart.add('DSA', 40)
pie_chart.add('Project', 30)

# Render the bar chart to SVG file
pie_chart.render_to_file('Pie_chart.svg')
