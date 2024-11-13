# importing pygal
import pygal
import numpy


# creating the chart object
radar_chart = pygal.Radar()

# naming the title
radar_chart.title = 'Radar chart'

radar_chart.x_labels = ['radii 1', 'radii 2',
						'radii 3', 'radii 4',
						'radii 5']

# Random data
radar_chart.add('A', numpy.random.rand(5))
radar_chart.add('B', numpy.random.rand(5))
radar_chart.add('C', numpy.random.rand(5))
radar_chart.add('D', numpy.random.rand(5))

radar_chart
