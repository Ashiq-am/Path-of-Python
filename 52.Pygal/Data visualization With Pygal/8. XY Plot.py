import pygal

xy_plot = pygal.XY(stroke=True)
xy_plot.add('Data', [(1, 2), (3, 4), (5, 6)])
xy_plot.render_to_file('xy_plot.svg')
