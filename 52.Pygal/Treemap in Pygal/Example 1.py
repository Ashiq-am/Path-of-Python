# importing pygal
import pygal
import numpy


# creating the chart object
treemap = pygal.Treemap()

# naming the title
treemap.title = 'Treemap'


# Random data
treemap.add('A', numpy.random.rand(5))
treemap.add('B', numpy.random.rand(5))
treemap.add('C', numpy.random.rand(5))
treemap.add('D', numpy.random.rand(5))

treemap
