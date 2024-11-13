# importing pygal
import pygal
import numpy


# creating the chart object
gauge = pygal.Gauge()

# naming the title
gauge.title = 'Gauge Chart'

# Random data
gauge.add('A', numpy.random.rand(10))
gauge.add('B', numpy.random.rand(10))
gauge.add('C', numpy.random.rand(10))
gauge.add('D', numpy.random.rand(10))

gauge
