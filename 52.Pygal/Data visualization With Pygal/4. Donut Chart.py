import pygal

# Create a pie chart with an inner radius to simulate a donut chart
pie_chart = pygal.Pie(inner_radius=0.4)
pie_chart.add('Part A', 10)
pie_chart.add('Part B', 20)
pie_chart.add('Part C', 30)

# Render to SVG
pie_chart.render_to_file('donut_chart.svg')
