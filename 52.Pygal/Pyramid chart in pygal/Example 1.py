import pygal
import random

# Random Data
data = [numpy.random.rand(100), numpy.random.rand(100),
		numpy.random.rand(100), numpy.random.rand(100)]

types = ['A', 'B',
		'C', 'D', ]

pyramid_chart = pygal.Pyramid()

# Naming the title
pyramid_chart.title = 'Pyramid Chart'

for type, dat in zip(types, data):
	pyramid_chart.add(type, dat)

pyramid_chart
