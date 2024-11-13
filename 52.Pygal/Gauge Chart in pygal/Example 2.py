# importing pygal
import pygal

# creating the chart object
gauge = pygal.Gauge()

# naming the title
gauge.title = 'Gauge Chart'

gauge.range = [0, 5000]

# Random data
gauge.add('A', 1000)
gauge.add('B', 2000)
gauge.add('C', 3500)

gauge
