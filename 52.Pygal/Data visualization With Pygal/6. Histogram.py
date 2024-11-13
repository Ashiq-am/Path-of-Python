import pygal

histogram = pygal.Histogram()
histogram.add('Data', [(0, 1), (5, 2), (10, 3)])
histogram.render_to_file('histogram.svg')
