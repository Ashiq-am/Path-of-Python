# import library
import pygal
import numpy

# creating the chart object
chart = pygal.Bar(x_label_rotation=20)

# Random data
chart.x_labels = [
	'First Bar !',
	'Second Bar !',
	'Third Bar !',
	'Fourth Bar !']
chart.add('line', [0.1, .034, .065, .035])

# naming the title
chart.title = 'Bar Chart'

chart.render_to_png('Python OpenCV – Roberts Edge Detection 8.png');
