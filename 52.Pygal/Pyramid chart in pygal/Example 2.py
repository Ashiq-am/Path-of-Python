import pygal
import random


# Random Data
data = [[26, 22, 39, 39, 32, 30, 33, 24, 24, 30],
		[31, 40, 22, 30, 21, 34, 40, 32, 25, 31],
		[37, 27, 31, 20, 38, 32, 24, 39, 29, 22],
		[38, 30, 20, 29, 33, 23, 32, 33, 32, 23]]

types = ['A', 'B',
		'C', 'D', ]

pyramid_chart = pygal.Pyramid()

# Naming the title
pyramid_chart.title = 'Pyramid Chart'

for type, dat in zip(types, data):
	pyramid_chart.add(type, dat)

pyramid_chart
