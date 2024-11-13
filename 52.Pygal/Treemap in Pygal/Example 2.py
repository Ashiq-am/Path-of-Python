# importing pygal
import pygal
import numpy


# creating the chart object
treemap = pygal.Treemap()

# naming the title
treemap.title = 'Treemap'

# Random data
treemap.add('A', [26, 22, 39, 39, 32, 30, 33, 24, 24, 30])
treemap.add('B', [31, 40, None, None, None, None, 40, 32, 25, 31])
treemap.add('C', [37, 27, 31, 20, None, 32, 24, 39, 29, 22])
treemap.add('D', [38, None, 20, 29, 33, 23, 32, 33, 32, 23])

treemap
