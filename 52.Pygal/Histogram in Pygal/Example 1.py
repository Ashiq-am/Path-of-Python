# importing pygal
import pygal
import numpy


# creating the chart object
histogram = pygal.Histogram()

# naming the title
histogram.title = 'Stacked Bar Chart'

# Random data
for i in range(5, 20, 10):
	data = list(zip(numpy.random.rand(i),
					numpy.random.rand(3),
					numpy.random.rand(i)))
	histogram.add(str(i), data)

histogram
