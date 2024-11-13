# importing pygal
import pygal
import numpy


# creating line chart object
pie_chart = pygal.Pie(half_pie = True)

# naming the title
pie_chart.title = 'Half Pie chart'


# Random data
pie_chart.add('A', numpy.random.rand(5))
pie_chart.add('B', numpy.random.rand(5))
pie_chart.add('C', numpy.random.rand(5))
pie_chart.add('D', numpy.random.rand(5))

pie_chart
