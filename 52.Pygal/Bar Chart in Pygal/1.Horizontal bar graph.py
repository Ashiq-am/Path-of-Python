# importing pygal
import pygal
import numpy


# creating the chart object
horizontal_chart = pygal.HorizontalBar()

# naming the title
horizontal_chart.title = 'Horizontal Chart'

# Random data
horizontal_chart.add('A', numpy.random.rand(10))
horizontal_chart.add('B', numpy.random.rand(10))
horizontal_chart.add('C', numpy.random.rand(10))
horizontal_chart.add('D', numpy.random.rand(10))

horizontal_chart
