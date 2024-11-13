# importing pygal
import pygal

# creating the chart object
Solid_Gauge = pygal.SolidGauge(inner_radius = 0.75)

# naming the title
Solid_Gauge.title = 'Solid Gauge Chart'

# Random data
Solid_Gauge.add('A', [{'value': 1000, 'max_value': 5000}])
Solid_Gauge.add('B', [{'value': 12, 'max_value': 20}])
Solid_Gauge.add('C', [{'value': 99, 'max_value': 100}])

Solid_Gauge
