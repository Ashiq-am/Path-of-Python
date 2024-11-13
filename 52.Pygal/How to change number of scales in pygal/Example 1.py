# importing pygal
import pygal
import numpy


# creating the chart object
# minimum number of scale
chart = pygal.Line(min_scale=40)

# Random data
chart.add('line', [0, .02, .05, .0035])

# naming the title
chart.title = 'Line Chart'

chart.render_to_png('aa.png')
