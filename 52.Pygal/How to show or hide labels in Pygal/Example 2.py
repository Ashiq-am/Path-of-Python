# import library
import pygal

# enable/diable labels
chart = pygal.Line(show_y_labels=False, show_x_labels=True)

# X-label
chart.x_labels = 'Point 1', 'Point 2', 'Point 3'
# y-label
chart.add('line', [.0002, .0005, .00035])

# naming the title
chart.title = 'Line Chart'

chart.render_to_png('aa.png')
