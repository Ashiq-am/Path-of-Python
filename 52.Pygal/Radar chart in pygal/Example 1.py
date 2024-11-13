# importing pygal
import pygal
import numpy


# creating the chart object
radar_chart = pygal.Radar()

# naming the title
radar_chart.title = 'Radar chart'

# Random data
radar_chart.add('A', numpy.random.rand(5))
radar_chart.add('B', numpy.random.rand(5))
radar_chart.add('C', numpy.random.rand(5))
radar_chart.add('D', numpy.random.rand(5))

radar_chart
