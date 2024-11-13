# importing pygal
import pygal
import numpy

# creating the chart object
Radar_Chart = pygal.Radar(legend_at_bottom=True)


Radar_Chart.x_labels = ['Radii 1', 'Radii 2',
						'Radii 3', 'Radii 4',
						'Radii 5']

# Random data
Radar_Chart.add('A', numpy.random.rand(6))
Radar_Chart.add('B', numpy.random.rand(6))
Radar_Chart.add('C', numpy.random.rand(6))
Radar_Chart.add('D', numpy.random.rand(6))

# naming the title
Radar_Chart.title = 'Radar Chart'

Radar_Chart.render_to_png('aa.png')
