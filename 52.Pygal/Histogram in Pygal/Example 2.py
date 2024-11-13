# importing pygal
import pygal
import numpy


# creating the chart object
histogram = pygal.Histogram()

# naming the title
histogram.title = 'Histogram'

histogram.add('A', [(2, 2, 3.9), (3, 2, 8), (3, 4, 2.4)])
histogram.add('B', [(1.5, 0, 2), (6, 2, 3), (7, 3, 2)])

histogram
