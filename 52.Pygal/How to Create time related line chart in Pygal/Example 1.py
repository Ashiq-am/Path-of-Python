# importing pygal
import pygal
from datetime import datetime
import numpy

# creating line chart object
line_chart = pygal.Line()

# naming the title
line_chart.title = 'Time Related chart'

# Formatting labels
line_chart.x_labels = map(lambda d: d.strftime('% Y-% m-% d'),
                          [datetime(2020, 1, 10),
                           datetime(2020, 4, 5),
                           datetime(2020, 2, 25),
                           datetime(2020, 8, 12),
                           datetime(2020, 5, 2)])

# adding lines
line_chart.add('A', numpy.random.rand(5))

line_chart
