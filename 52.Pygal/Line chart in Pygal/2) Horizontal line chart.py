# importing pygal
import pygal
import numpy


# creating line chart object
line_chart = pygal.HorizontalLine()

# naming the title
line_chart.title = 'Horizontal Line chart'


# adding lines
line_chart.add('A', numpy.random.rand(5))
line_chart.add('B', numpy.random.rand(5))
line_chart.add('C', numpy.random.rand(5))
line_chart.add('D', numpy.random.rand(5))

line_chart
