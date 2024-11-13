# importing pygal
import pygal
import numpy

# creating the chart object
chart = pygal.Line(x_label_rotation=90)

# Random data
chart.x_labels = [
	'First Point !',
	'Second point !',
	'Third Point !',
	'Fourth Point !']
chart.add('line', [0.1, .034, .065, .035])

# naming the title
chart.title = 'Line Chart'

chart.render_to_png('Python OpenCV – Roberts Edge Detection 8.png')
