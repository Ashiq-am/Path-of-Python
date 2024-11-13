# importing pygal
import pygal
import numpy

# creating the chart object
# Resize legend box size
chart = pygal.Funnel(legend_box_size=48)

# Random data
chart.add('Serie 1', [1, 2, 3])
chart.add('Serie 2', [4, 2, 0])
chart.add('Serie 3', [1, -1, 1])
chart.add('Serie 4', [3, 1, 5])


# naming the title
chart.title = 'Funnel Chart'

chart.render_to_png('aa.png')
