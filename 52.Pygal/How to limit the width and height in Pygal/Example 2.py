# importing pygal
import pygal
import numpy

# creating the chart object
chart = pygal.Line(width=400, height=200)

# naming the title
chart.title = 'Line Chart'

# Random data
chart.add('A', numpy.random.rand(2))
chart.add('B', numpy.random.rand(2))
chart.add('C', numpy.random.rand(2))

chart.render_to_png('Python OpenCV – Roberts Edge Detection 8.png')
