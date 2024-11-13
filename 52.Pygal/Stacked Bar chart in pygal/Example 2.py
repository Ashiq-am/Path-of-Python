# importing pygal
import pygal

# creating the chart object
bar_chart = pygal.StackedBar()

# naming the title
bar_chart.title = 'Stacked Bar Chart'

bar_chart.range = [0, 5000]

# Random data
bar_chart.add('A', 1000)
bar_chart.add('B', 2000)
bar_chart.add('C', 3500)

bar_chart
