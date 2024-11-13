# importing pygal
import pygal
import numpy


# creating the chart object
funnel = pygal.Funnel()

# naming the title
funnel.title = 'Funnel'

# Random data
funnel.add('A', numpy.random.rand(10))
funnel.add('B', numpy.random.rand(10))
funnel.add('C', numpy.random.rand(10))
funnel.add('D', numpy.random.rand(10))

funnel
